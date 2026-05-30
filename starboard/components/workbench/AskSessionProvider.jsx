import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState } from 'react';
import { getApiTask, startApiTask } from '../../lib/apiClient';
import { findMedicalAskReplay } from '../../lib/medicalAskReplay';

const DEFAULT_QUESTION = '';
const STORAGE_KEY = 'controlmind.ask.session.v4';
const ASK_SESSION_VERSION = 4;
const CLIENT_TASK_TIMEOUT_MS = 3 * 60 * 1000;

const AskSessionContext = createContext(null);

function createSessionId() {
  return `ask_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 8)}`;
}

function readStoredSession() {
  if (typeof window === 'undefined') return null;
  try {
    const raw = window.sessionStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

function sanitizeStoredQuestion(value) {
  const text = String(value || '');
  if (text.includes('闭环胰岛素系统') && text.includes('文献里有什么')) return '';
  return text;
}

export function AskSessionProvider({ children }) {
  const [question, setQuestion] = useState(DEFAULT_QUESTION);
  const [messages, setMessages] = useState([]);
  const [indexId, setIndexId] = useState('bge_m3');
  const [mode, setMode] = useState('hybrid');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [pendingQuestion, setPendingQuestion] = useState('');
  const [pendingTaskId, setPendingTaskId] = useState('');
  const [pendingTaskToken, setPendingTaskToken] = useState('');
  const [pendingTaskStartedAt, setPendingTaskStartedAt] = useState(0);
  const [hydrated, setHydrated] = useState(false);
  const sessionIdRef = useRef(createSessionId());
  const messagesRef = useRef(messages);
  const inFlightRef = useRef(null);

  useEffect(() => {
    const stored = readStoredSession();
    if (stored?.uiVersion === ASK_SESSION_VERSION) {
      setQuestion(sanitizeStoredQuestion(stored.question) || DEFAULT_QUESTION);
      setMessages(Array.isArray(stored.messages) ? stored.messages : []);
      setIndexId(stored.indexId || 'bge_m3');
      setMode(stored.mode || 'hybrid');
      setPendingQuestion(stored.pendingQuestion || '');
      setPendingTaskId(stored.pendingTaskId || '');
      setPendingTaskStartedAt(stored.pendingTaskStartedAt || 0);
      setLoading(Boolean(stored.pendingTaskId));
      inFlightRef.current = stored.pendingTaskId || null;
      sessionIdRef.current = stored.sessionId || createSessionId();
    }
    setHydrated(true);
  }, []);

  useEffect(() => {
    if (!question.includes('证据')) return;
    setQuestion(question.replaceAll('证据', '依据'));
  }, [question]);

  useEffect(() => {
    messagesRef.current = messages;
  }, [messages]);

  useEffect(() => {
    if (!hydrated || typeof window === 'undefined') return;
    const payload = {
      question,
      messages,
      indexId,
      mode,
      uiVersion: ASK_SESSION_VERSION,
      sessionId: sessionIdRef.current,
      pendingQuestion,
      pendingTaskId,
      pendingTaskStartedAt,
      savedAt: new Date().toISOString(),
    };
    window.sessionStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
  }, [hydrated, question, messages, indexId, mode, pendingQuestion, pendingTaskId, pendingTaskStartedAt]);

  const finishTask = useCallback((task) => {
    if (task.status === 'failed') {
      const message = task.error || '医学问答请求失败';
      setError(message);
      setMessages(prev => [
        ...prev,
        { role: 'assistant', status: 'failed', answer: message, created_at: new Date().toISOString() },
      ]);
      setLoading(false);
      setPendingQuestion('');
      setPendingTaskId('');
      setPendingTaskToken('');
      setPendingTaskStartedAt(0);
      inFlightRef.current = null;
      return true;
    }
    if (task.status === 'done') {
      setMessages(prev => [...prev, { role: 'assistant', ...task.data, created_at: new Date().toISOString() }]);
      setLoading(false);
      setPendingQuestion('');
      setPendingTaskId('');
      setPendingTaskStartedAt(0);
      inFlightRef.current = null;
      return true;
    }
    return false;
  }, []);

  const pollTask = useCallback(async (taskId, ownerToken, startedAt) => {
    if (!taskId) return;
    if (isClientTaskExpired(startedAt)) {
      finishTask({ status: 'failed', error: '任务状态已过期，请重新提问。' });
      return;
    }
    for (;;) {
      if (isClientTaskExpired(startedAt)) {
        finishTask({ status: 'failed', error: '任务超时，请重新提问。' });
        return;
      }
      const response = await getApiTask({ id: taskId, owner_token: ownerToken }, { timeoutMs: 12000 });
      if (!response.ok) {
        finishTask({ status: 'failed', error: response.error || '任务状态恢复失败' });
        return;
      }
      if (finishTask(response.data)) return;
      await new Promise(resolve => setTimeout(resolve, 1200));
    }
  }, [finishTask]);

  useEffect(() => {
    if (hydrated && pendingTaskId && loading) {
      pollTask(pendingTaskId, pendingTaskToken, pendingTaskStartedAt);
    }
  }, [hydrated, loading, pendingTaskId, pendingTaskStartedAt, pendingTaskToken, pollTask]);

  const clearChat = useCallback(() => {
    if (inFlightRef.current) return;
    sessionIdRef.current = createSessionId();
    setMessages([]);
    setError('');
    setPendingQuestion('');
    setPendingTaskId('');
    setPendingTaskToken('');
    setPendingTaskStartedAt(0);
    setQuestion(DEFAULT_QUESTION);
  }, []);

  const ask = useCallback(async (nextQuestion, { runtimeConfig, preferReplay = false } = {}) => {
    const text = (nextQuestion || question || '').trim();
    if (!text || inFlightRef.current) return;
    inFlightRef.current = 'starting';

    const userMessage = { role: 'user', content: text, created_at: new Date().toISOString() };
    const history = messagesRef.current.slice(-6).map(item => ({
      role: item.role,
      content: item.content || item.answer || '',
    }));
    const localFollowup = createLocalFollowupResponse(text, messagesRef.current);

    setQuestion('');
    setError('');
    setPendingQuestion(text);
    setPendingTaskId('');
    setPendingTaskToken('');

    if (localFollowup) {
      setMessages(prev => [
        ...prev,
        userMessage,
        { role: 'assistant', question: text, ...localFollowup, created_at: new Date().toISOString() },
      ]);
      setLoading(false);
      setPendingQuestion('');
      setPendingTaskId('');
      setPendingTaskToken('');
      setPendingTaskStartedAt(0);
      inFlightRef.current = null;
      return;
    }

    setLoading(true);
    setMessages(prev => [...prev, userMessage]);

    const replay = preferReplay && runtimeConfig?.profile === 'demo_replay'
      ? findMedicalAskReplay(text)
      : null;
    if (replay) {
      setMessages(prev => [
        ...prev,
        {
          role: 'assistant',
          question: text,
          ...replay,
          created_at: new Date().toISOString(),
        },
      ]);
      setLoading(false);
      setPendingQuestion('');
      setPendingTaskId('');
      setPendingTaskToken('');
      setPendingTaskStartedAt(0);
      inFlightRef.current = null;
      return;
    }

    const response = await startApiTask('/api/medical-rag/ask', {
      question: text,
      k: 3,
      mode,
      index_id: indexId,
      synthesis_model: runtimeConfig?.t3_synthesis === 'replay'
        ? (runtimeConfig?.local_model || 'qwen3.5:9b')
        : (runtimeConfig?.t3_synthesis || runtimeConfig?.local_model || 'qwen3.5:9b'),
      triage_model: runtimeConfig?.local_model || 'qwen3.5:9b',
      session_id: sessionIdRef.current,
      history,
    }, { runtimeConfig, timeoutMs: 180000 });

    if (!response.ok) {
      const message = response.error || '医学问答请求失败';
      setError(message);
      setMessages(prev => [
        ...prev,
        { role: 'assistant', status: 'failed', answer: message, created_at: new Date().toISOString() },
      ]);
      setLoading(false);
      setPendingQuestion('');
      setPendingTaskStartedAt(0);
      setPendingTaskToken('');
      inFlightRef.current = null;
      return;
    }

    const taskId = response.data.id;
    inFlightRef.current = taskId;
    setPendingTaskStartedAt(Date.now());
    setPendingTaskToken(response.data.owner_token || '');
    setPendingTaskId(taskId);
  }, [indexId, mode, question]);

  const value = useMemo(() => ({
    question,
    setQuestion,
    messages,
    indexId,
    setIndexId,
    mode,
    setMode,
    loading,
    error,
    pendingQuestion,
    ask,
    clearChat,
  }), [ask, clearChat, error, indexId, loading, messages, mode, pendingQuestion, question]);

  return (
    <AskSessionContext.Provider value={value}>
      {children}
    </AskSessionContext.Provider>
  );
}

function isClientTaskExpired(startedAt) {
  if (!startedAt) return true;
  return Date.now() - startedAt > CLIENT_TASK_TIMEOUT_MS;
}

function createLocalFollowupResponse(question, messages) {
  if (!isGenericFollowup(question)) return null;
  const lastAssistant = [...messages].reverse().find(item => item.role === 'assistant' && item.answer);
  if (!lastAssistant) {
    return {
      status: 'replay',
      model: 'conversation-helper',
      privacy: 'local_ui',
      answer: '可以。请先给出一个具体的医学文献问题，例如“主要终点和安全性文献依据”或“闭环胰岛素低血糖风险的文献依据”。我会基于本地已审核文献库回答，并标注引用。',
      citations: [],
      claims: [],
      evidence_items: [],
      confidence: 'medium',
      limitations: '这是界面内的追问引导，没有执行医学文献检索。',
    };
  }

  const citations = lastAssistant.citations || [];
  const evidenceItems = lastAssistant.evidence_items || [];
  const evidenceText = evidenceItems.length
    ? `\n\n可继续查看的来源片段包括：${evidenceItems.slice(0, 3).map(item => item.chunk_id).join('、')}。`
    : '';
  return {
    status: 'replay',
    model: 'conversation-helper',
    privacy: 'local_ui',
    answer: `可以。上一条回答的核心依据是：${summarizeAnswer(lastAssistant.answer)}${evidenceText}\n\n如果你希望继续深入，建议追问一个更具体的方向，例如“这些引用分别支持哪条结论？”、“有没有依据不足的地方？”或“把主要终点和安全性分开解释”。`,
    citations,
    claims: lastAssistant.claims || [],
    evidence_items: evidenceItems,
    confidence: lastAssistant.confidence || 'medium',
    limitations: '这是基于当前会话上一条回答的本地追问展开，没有触发新的医学检索或模型调用。',
  };
}

function isGenericFollowup(question) {
  const text = (question || '').trim().toLowerCase();
  if (!text) return false;
  return [
    '更多信息',
    '详细一点',
    '展开',
    '继续说',
    '多说一点',
    '再解释',
    '什么意思',
    'more information',
    'tell me more',
    'explain more',
  ].some(term => text.includes(term));
}

function summarizeAnswer(answer) {
  const text = String(answer || '').replace(/\s+/g, ' ').trim();
  if (!text) return '上一条回答已经给出可引用的文献来源。';
  return text.length > 120 ? `${text.slice(0, 120)}...` : text;
}

export function useAskSession() {
  const context = useContext(AskSessionContext);
  if (!context) {
    throw new Error('useAskSession must be used within AskSessionProvider');
  }
  return context;
}
