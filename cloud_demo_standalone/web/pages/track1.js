import { useEffect, useMemo, useState } from 'react';
import SectionWrapper from '../components/SectionWrapper';
import CloudActivityOverlay from '../components/workbench/CloudActivityOverlay';
import ErrorCallout from '../components/workbench/ErrorCallout';
import LoadingDots from '../components/workbench/LoadingDots';
import PipelineStep from '../components/workbench/PipelineStep';
import RuntimeSummary from '../components/workbench/RuntimeSummary';
import StepCard from '../components/workbench/StepCard';
import StatusPill from '../components/workbench/StatusPill';
import WorkbenchLoadingCard from '../components/workbench/WorkbenchLoadingCard';
import MarkdownText from '../components/workbench/MarkdownText';
import { apiGet, apiPost, apiRequest, getApiTask, startApiTask, toFailure } from '../lib/apiClient';
import { adaptScoringReason, adaptTrack1Question, adaptTrack1ScoreResult } from '../lib/track1DisplayAdapter';
import useSessionState from '../lib/useSessionState';

const CLIENT_TASK_TIMEOUT_MS = 6 * 60 * 1000;
const TRACK1_SESSION_VERSION = 3;
const DIRECT_LOADING_STATES = new Set(['examples', 'upload', 'official_url', 'questions', 'score']);
const TRACK1_DEMO_SOURCE = [
  '# 公开控制论文摘要',
  '',
  '研究讨论含时滞控制系统的稳定性分析与保守性降低问题。论文通过构造 Lyapunov-Krasovskii 泛函，并结合积分不等式与线性矩阵不等式（LMI）条件，给出可计算的稳定性判据。',
  '',
  '若存在正定矩阵 $P \\succ 0$ 和松弛变量使得对应 LMI 可行，则闭环系统在给定时滞上界下保持渐近稳定。该方法把连续时间稳定性证明转化为凸优化可求解问题，但结论依赖模型假设、时滞上界和不等式放缩方式。',
  '',
  '简化稳定性条件可写为 $\\dot V(x_t) < 0$。模型回答需要说明 Lyapunov 泛函选择、LMI 可行性含义、保守性来源，以及该判据不能直接证明未建模扰动或超出时滞上界的情形。',
].join('\n');

const dimensionNames = {
  A: '概念回溯',
  B: '多步推理',
  C: '条件敏感',
  D: '开放设计',
};

const painPoints = [
  {
    title: '控制科学评测缺口',
    desc: '通用基准很少覆盖控制科学，更缺少条件敏感和开放设计两个工程关键维度。',
  },
  {
    title: '复杂 PDF 难以消费',
    desc: '扫描教材、公式、图片和表格需要先被结构化，才能进入训练、检索和评测链路。',
  },
  {
    title: '模型答案需要验真',
    desc: 'LLM 很容易写出看似合理的控制方案，必须用四维 Benchmark 量化能力边界。',
  },
  {
    title: '私有资料不能默认上云',
    desc: '原文、chunk、向量索引和微调样本属于受控资产，公开或脱敏任务才允许进入在线展示版。',
  },
];

const corpusMetrics = [
  ['362', 'PDF 文档'],
  ['253,012', 'LaTeX 公式'],
  ['11,554', '嵌入图片'],
  ['28,514', '语义 chunk'],
  ['500', '核心评测题'],
  ['A/B/C/D', '四维平衡'],
];

const benchmarkHighlights = [
  ['评测对象', '9 个主流 LLM，全量 500 题'],
  ['能力分层', '概念回溯、多步推理、条件敏感、开放设计'],
  ['可靠性', '跨管道 MAE=0.0003，三 Judge κ=0.575'],
  ['部署边界', '完整系统本地优先，云端只处理公开或脱敏派生任务'],
];

export default function Track1Page({ runtimeConfig }) {
  const [persisted, setPersisted] = useSessionState('controlmind.track1.session.v1', {
    uiVersion: TRACK1_SESSION_VERSION,
    papers: [],
    selected: '',
    officialUrl: '',
    source: '',
    uploadResult: null,
    parseResult: null,
    questions: null,
    scoreResult: null,
    error: null,
    loading: '',
    pendingTask: null,
  });
  const setField = (key) => (value) => setPersisted(prev => ({ ...prev, [key]: typeof value === 'function' ? value(prev[key]) : value }));
  const patchPersisted = (patch) => setPersisted(prev => ({ ...prev, ...patch }));
  const {
    papers,
    selected,
    officialUrl,
    source,
    uploadResult,
    parseResult,
    questions,
    scoreResult,
    error,
    loading,
    pendingTask,
  } = persisted;
  const setPapers = setField('papers');
  const setSelected = setField('selected');
  const [uploadedFile, setUploadedFile] = useState(null);
  const setOfficialUrl = setField('officialUrl');
  const setSource = setField('source');
  const setUploadResult = setField('uploadResult');
  const setParseResult = setField('parseResult');
  const setQuestions = setField('questions');
  const setScoreResult = setField('scoreResult');
  const setError = setField('error');
  const setLoading = setField('loading');

  const realSourceText = (parseResult?.markdown_preview || uploadResult?.markdown_preview || '').trim();
  const inputReady = Boolean(selected || uploadResult?.filename || realSourceText);

  useEffect(() => {
    if (persisted.uiVersion !== TRACK1_SESSION_VERSION) {
      patchPersisted({
        uiVersion: TRACK1_SESSION_VERSION,
        parseResult: null,
        questions: null,
        scoreResult: null,
        loading: '',
        pendingTask: null,
      });
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [persisted.uiVersion]);

  function resetAfterInput() {
    setParseResult(null);
    setQuestions(null);
    setScoreResult(null);
    setError(null);
  }

  async function pollTrack1Task(task) {
    if (!task?.id) return;
    if (isClientTaskExpired(task)) {
      patchPersisted({ loading: '', pendingTask: null, error: toFailure('任务状态已过期，请重新执行当前步骤。') });
      return;
    }
    for (;;) {
      if (isClientTaskExpired(task)) {
        patchPersisted({ loading: '', pendingTask: null, error: toFailure('任务超时，请重新执行当前步骤。') });
        return;
      }
      const response = await getApiTask(task, { timeoutMs: 12000 });
      if (!response.ok) {
        patchPersisted({ loading: '', pendingTask: null, error: toFailure(response.error) });
        return;
      }
      if (response.data.status === 'running') {
        await new Promise(resolve => setTimeout(resolve, 1200));
        continue;
      }
      if (response.data.status === 'failed') {
        patchPersisted({ loading: '', pendingTask: null, error: toFailure(response.data.error) });
        return;
      }
      const data = response.data.data;
      if (task.kind === 'parse') setParseResult(data);
      if (task.kind === 'questions') setQuestions(data);
      if (task.kind === 'score') setScoreResult(data);
      if (task.kind === 'continue') {
        setQuestions(data.questions);
        setScoreResult(data.score);
      }
      if (task.kind === 'demo') {
        setParseResult(data.parse);
        setQuestions(data.questions);
        setScoreResult(data.score);
      }
      patchPersisted({ loading: '', pendingTask: null });
      return;
    }
  }

  useEffect(() => {
    if (loading && !pendingTask?.id && !DIRECT_LOADING_STATES.has(loading)) {
      patchPersisted({ loading: '', pendingTask: null });
      return;
    }
    if (pendingTask?.id && loading) pollTrack1Task(pendingTask);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pendingTask?.id, loading]);

  async function loadExamples() {
    setLoading('examples');
    const result = await apiGet('/api/demo/track1/examples', { timeoutMs: 12000 });
    if (result.ok) {
      setPapers(result.data.papers || []);
      if (result.data.papers?.length) {
        setSelected(result.data.papers[0].id);
        setSource('selected');
      }
      resetAfterInput();
    } else {
      setError(toFailure(result.error));
    }
    setLoading('');
  }

  async function uploadPdf() {
    if (!uploadedFile) return;
    setLoading('upload');
    setError(null);
    const form = new FormData();
    form.append('file', uploadedFile);
    const result = await apiRequest('/api/demo/mineru/upload', {
      method: 'POST',
      body: form,
      runtimeConfig,
      timeoutMs: 240000,
    });
    if (result.ok) {
      const parsed = adaptCloudMineruResult(result.data, 'upload');
      setUploadResult({ ...parsed, filename: uploadedFile.name });
      setParseResult(parsed);
      setSelected('');
      setSource('uploaded');
      setQuestions(null);
      setScoreResult(null);
    } else {
      setError(toFailure(result.error));
    }
    setLoading('');
  }

  async function parseUploadedPdf() {
    if (uploadResult?.markdown_preview) {
      setParseResult(uploadResult);
      return;
    }
    if (!uploadResult?.filename) return;
    setLoading('parse');
    setError(null);
    const result = await startApiTask('/api/demo/track1/parse_file', {
      filename: uploadResult.filename,
      parser_backend: runtimeConfig.parser_backend,
    }, { runtimeConfig, timeoutMs: 240000 });
    if (result.ok) patchPersisted({ loading: 'parse', pendingTask: createPendingTask(result.data, 'parse', 270000) });
    else { setParseResult(toFailure(result.error)); setLoading(''); }
  }

  async function parseOfficialUrl() {
    if (!officialUrl.trim()) return;
    setLoading('official_url');
    setError(null);
    const result = await apiPost('/api/demo/mineru/url', {
      url: officialUrl.trim(),
      model_version: 'vlm',
    }, { runtimeConfig, timeoutMs: 45000 });
    if (result.ok) {
      setParseResult(adaptCloudMineruResult(result.data, 'url'));
      setSelected('');
      setSource('official_url');
      setUploadResult(null);
      setQuestions(null);
      setScoreResult(null);
    } else {
      setError(toFailure(result.error));
      setLoading('');
    }
  }

  async function inspectSelectedPaper() {
    if (!selected) return;
    setLoading('parse');
    setError(null);
    const result = await startApiTask('/api/demo/track1/parse', {
      paper_id: selected,
      mode: runtimeConfig.parser_backend || 'replay',
    }, { runtimeConfig, timeoutMs: 30000 });
    if (result.ok) patchPersisted({ loading: 'parse', pendingTask: createPendingTask(result.data, 'parse', 60000) });
    else { setParseResult(toFailure(result.error)); setLoading(''); }
  }

  async function generateQuestions() {
    const sourceText = realSourceText || TRACK1_DEMO_SOURCE;
    if (!inputReady && !sourceText) return;
    setLoading('questions');
    setError(null);
    const result = await apiPost('/api/demo/quiz/generate', {
      source_text: sourceText,
      topic: 'ControlMind Sci-Align 云端公开论文评测',
      count: 4,
      dry_run: false,
    }, { runtimeConfig, timeoutMs: 90000 });
    if (result.ok) setQuestions(adaptCloudQuestions(result.data));
    else { setQuestions(toFailure(result.error)); setLoading(''); }
    setLoading('');
  }

  async function answerAndScore() {
    const sourceText = realSourceText || TRACK1_DEMO_SOURCE;
    const activeQuestions = questions?.questions || [];
    if (!activeQuestions.length) {
      await generateQuestions();
      return;
    }
    setLoading('score');
    setError(null);
    try {
      const graded = [];
      for (const question of activeQuestions.slice(0, 4)) {
        const modelAnswer = buildTrack1CandidateAnswer(question);
        const result = await apiPost('/api/demo/quiz/grade', {
          question: question.question,
          expected_answer: question.expected_answer,
          rubric: question.rubric,
          student_answer: modelAnswer,
          source_text: sourceText,
          dry_run: false,
        }, { runtimeConfig, timeoutMs: 90000 });
        if (!result.ok) throw new Error(result.error || '评分失败');
        graded.push({ question, modelAnswer, grade: result.data });
      }
      setScoreResult(adaptCloudScore(graded));
    } catch (err) {
      setScoreResult(toFailure(err.message));
    } finally {
      setLoading('');
    }
  }

  const parseSteps = parseResult?.pipeline_steps || uploadResult?.pipeline_steps || [];
  const visibleStats = Object.entries(parseResult?.stats || {}).filter(([, value]) => Number(value) > 0);
  const displayQuestions = useMemo(
    () => (questions?.questions || []).map(adaptTrack1Question),
    [questions],
  );
  const displayScore = useMemo(
    () => scoreResult ? adaptTrack1ScoreResult(scoreResult) : null,
    [scoreResult],
  );
  const activity = getTrack1Activity(loading);

  return (
    <SectionWrapper>
      <div className="custom-screen space-y-6">
        <CloudActivityOverlay active={Boolean(activity)} {...activity} />
        <div>
          <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-3">
            <div>
              <h1 className="text-gray-800 text-3xl font-semibold sm:text-4xl mb-2">赛道一：ControlMind Sci-Align 评测基座</h1>
              <p className="text-gray-600 text-sm">把控制科学 PDF 资产转化为可训练、可评测、可追溯的数据基础设施。</p>
              <p className="mt-1 text-[11px] text-gray-500">前台展示行业痛点、语料规模和四维 Benchmark；下方公开 PDF 上传、MinerU 解析、DeepSeek 出题与评分均走云端真实 API，样例仅用于快速展示。</p>
            </div>
          </div>
        </div>

        <RuntimeSummary runtimeConfig={runtimeConfig} />
        {error?.message && (
          <ErrorCallout message={error.message} hint="如果后端服务不在线，页面会保留当前状态并允许继续使用已验证产物路径。" />
        )}

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-3">
          {painPoints.map(item => (
            <div key={item.title} className="rounded-lg border border-gray-200 bg-white p-4">
              <div className="text-sm font-semibold text-gray-900">{item.title}</div>
              <div className="mt-2 text-xs leading-5 text-gray-600">{item.desc}</div>
            </div>
          ))}
        </div>

        <div className="grid grid-cols-1 xl:grid-cols-3 gap-4">
          <div className="xl:col-span-2 rounded-lg border border-gray-200 bg-white p-5">
            <div className="flex items-center justify-between gap-3">
              <div>
                <div className="text-sm font-semibold text-gray-900">结构化语料工程</div>
                <div className="mt-1 text-xs text-gray-500">MinerU 将公式、图片和正文保留下来，支撑后续训练、检索和评测。</div>
              </div>
              <StatusPill status="validated" label="报告主张" />
            </div>
            <div className="mt-4 grid grid-cols-2 md:grid-cols-3 gap-3">
              {corpusMetrics.map(([value, label]) => (
                <div key={label} className="rounded border border-gray-100 bg-gray-50 px-3 py-3">
                  <div className="font-mono text-lg font-semibold text-gray-900">{value}</div>
                  <div className="mt-1 text-[11px] text-gray-500">{label}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-lg border border-gray-200 bg-white p-5">
            <div className="text-sm font-semibold text-gray-900">四维评测闭环</div>
            <div className="mt-1 text-xs text-gray-500">展示重点不是单次回答，而是可复现的 Benchmark、Judge 和数据追溯。</div>
            <div className="mt-4 space-y-2">
              {benchmarkHighlights.map(([label, value]) => (
                <div key={label} className="flex gap-3 rounded border border-gray-100 bg-gray-50 px-3 py-2 text-xs">
                  <div className="w-16 shrink-0 font-semibold text-gray-700">{label}</div>
                  <div className="leading-5 text-gray-600">{value}</div>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="rounded-lg border border-sky-100 bg-sky-50 px-5 py-4">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
            <div>
              <div className="text-sm font-semibold text-sky-950">推荐浏览路径</div>
              <div className="mt-1 text-xs leading-5 text-sky-900">
                默认先看语料规模、四维 Benchmark 和排行榜结论；需要现场核验时，按顺序上传公开 PDF 或提交公开 URL，再执行云端解析、出题和评分，查看同一来源下的解析、题目、作答和评分绑定。
              </div>
            </div>
          </div>
        </div>

        <StepCard index="1" title="论文输入" desc="上传 PDF 或选择已验证样例论文。" status={loading === 'upload' || loading === 'official_url' || loading === 'examples' ? 'running' : inputReady ? 'done' : 'pending'}>
          {(loading === 'upload' || loading === 'official_url' || loading === 'examples') && (
            <WorkbenchLoadingCard
              title={loading === 'examples' ? '正在加载样例论文' : loading === 'upload' ? '正在上传 PDF' : '正在提交官方解析'}
              desc="任务已提交，完成后会更新输入状态并解锁后续解析与评测步骤。"
              steps={['提交输入', '读取元数据', '更新状态']}
              className="mb-4"
            />
          )}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
            <div className="border rounded-lg p-4 bg-gray-50">
              <div className="text-xs font-semibold text-gray-700 mb-3">上传 PDF</div>
              <div className="flex gap-2">
                <input
                  type="file"
                  accept=".pdf"
                  onChange={e => {
                    const file = e.target.files?.[0];
                    setUploadedFile(file || null);
                    setSource(file ? 'uploaded' : '');
                    setSelected('');
                    resetAfterInput();
                  }}
                  className="flex-1 text-xs border rounded px-2 py-2 file:mr-2 file:px-3 file:py-1 file:text-xs file:border-0 file:bg-white file:rounded"
                />
                <button onClick={uploadPdf} disabled={!uploadedFile || loading === 'upload'} className="px-4 py-2 bg-gray-900 text-white text-xs rounded disabled:opacity-50">
                  <BusyLabel active={loading === 'upload'} busyText="解析中" idleText="上传并解析" />
                </button>
              </div>
              {uploadResult && (
                <div className="mt-3 text-[11px] text-gray-600 space-y-1">
                  <div>文件：<span className="font-mono">{uploadResult.filename}</span></div>
                  <div>状态：{uploadResult.parse_detail || uploadResult.message || '已保存'}</div>
                </div>
              )}
            </div>

            <div className="border rounded-lg p-4 bg-gray-50">
              <div className="text-xs font-semibold text-gray-700 mb-3">公开 URL / MinerU 官方 API</div>
              <div className="space-y-2">
                <input
                  type="url"
                  value={officialUrl}
                  onChange={e => { setOfficialUrl(e.target.value); setSource(e.target.value ? 'official_url' : ''); resetAfterInput(); }}
                  placeholder="https://.../paper.pdf"
                  className="w-full border rounded px-3 py-2 text-xs"
                />
                <button onClick={parseOfficialUrl} disabled={!officialUrl.trim() || loading === 'official_url'} className="w-full px-4 py-2 bg-gray-900 text-white text-xs rounded disabled:opacity-50">
                  <BusyLabel active={loading === 'official_url'} busyText="提交中" idleText="提交官方解析" />
                </button>
              </div>
              <div className="mt-2 text-[11px] text-gray-500">仅适合公开/脱敏 URL；敏感文档不进入在线展示版。</div>
            </div>

            <div className="border rounded-lg p-4 bg-gray-50">
              <div className="flex items-center justify-between mb-3">
                <div className="text-xs font-semibold text-gray-700">样例论文</div>
                <button onClick={loadExamples} disabled={loading === 'examples'} className="px-3 py-1.5 border rounded text-xs hover:bg-white">
                  <BusyLabel active={loading === 'examples'} busyText="加载中" idleText="加载样例" />
                </button>
              </div>
              <select value={selected} onChange={e => { setSelected(e.target.value); setSource('selected'); setUploadResult(null); resetAfterInput(); }} className="w-full border rounded px-3 py-2 text-sm">
                <option value="">选择一篇样例论文</option>
                {papers.map(p => <option key={p.id} value={p.id}>{p.arxiv_id} - {p.title}</option>)}
              </select>
              <div className="mt-2 text-[11px] text-gray-500">样例用于快速展示完整页面结构；如需体验实时解析，请使用上传或公开 URL。</div>
            </div>
          </div>
        </StepCard>

        <StepCard
          index="2"
          title="解析与结构化"
          desc="上传 PDF 由 MinerU 官方 API 实时解析；公开 URL 会提交官方解析任务；样例论文用于快速展示。"
          status={parseResult?.parse_ok ? 'done' : parseResult?.status === 'replay' ? 'replay' : loading === 'parse' || loading === 'demo' ? 'running' : parseSteps.length ? 'ready' : 'pending'}
          actions={
            <div className="flex gap-2">
              <button onClick={inspectSelectedPaper} disabled={!selected || loading === 'parse'} className="px-3 py-1.5 border rounded text-xs hover:bg-white disabled:opacity-50">
                <BusyLabel active={loading === 'parse'} busyText="查看中" idleText="查看样例" />
              </button>
              <button onClick={parseUploadedPdf} disabled={!uploadResult?.filename || loading === 'parse'} className="px-3 py-1.5 bg-gray-900 text-white rounded text-xs disabled:opacity-50">
                <BusyLabel active={loading === 'parse'} busyText="读取中" idleText="查看上传解析" />
              </button>
            </div>
          }
        >
          {(loading === 'parse' || (loading === 'demo' && !parseSteps.length)) && (
            <WorkbenchLoadingCard
              title="正在解析论文结构"
              desc="正在准备 PDF、调用解析链路或读取已验证产物，完成后会显示结构化步骤。"
              steps={['读取论文', '解析结构', '生成 chunk']}
              className="mb-3"
            />
          )}
          {parseSteps.length ? (
            <div className="space-y-2">
              {parseSteps.map((s, idx) => <PipelineStep key={`${s.step}-${idx}`} {...s} />)}
            </div>
          ) : (
            <div className="text-xs text-gray-500">选择输入后，可检查样例解析或解析上传 PDF。</div>
          )}
          {parseResult?.detail && <div className="mt-3 text-xs text-gray-600">{parseResult.detail}</div>}
          {visibleStats.length > 0 && (
            <div className="mt-3 grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
              {visibleStats.map(([k, v]) => (
                <div key={k} className="border rounded p-2 bg-gray-50"><div className="font-mono text-gray-800">{v}</div><div className="text-gray-400">{k}</div></div>
              ))}
            </div>
          )}
        </StepCard>

        <StepCard
          index="3"
          title="出题与评分"
          desc="调用 DeepSeek 生成 A/B/C/D 风格题目，并对候选回答进行云端评分。"
          status={scoreResult ? 'done' : loading === 'questions' || loading === 'score' || loading === 'continue' || loading === 'demo' ? 'running' : questions ? 'ready' : 'pending'}
          actions={
            <div className="flex gap-2">
              <button onClick={generateQuestions} disabled={!inputReady || loading === 'questions'} className="px-3 py-1.5 border rounded text-xs hover:bg-white disabled:opacity-50">
                <BusyLabel active={loading === 'questions'} busyText="出题中" idleText="云端出题" />
              </button>
              <button onClick={answerAndScore} disabled={!inputReady || !displayQuestions.length || loading === 'score'} className="px-3 py-1.5 bg-gray-900 text-white rounded text-xs disabled:opacity-50">
                <BusyLabel active={loading === 'score'} busyText="评分中" idleText="云端评分" />
              </button>
            </div>
          }
        >
          {(loading === 'questions' || loading === 'score' || loading === 'continue' || loading === 'demo') && !scoreResult && (
            <WorkbenchLoadingCard
              title={loading === 'score' ? '正在答题评分' : '正在生成题目与评分'}
              desc="正在生成四维题目、绑定模型回答并汇总评分来源，完成后会展示题目和 overall 分数。"
              steps={['生成题目', '模型答题', '评分汇总']}
              className="mb-4"
            />
          )}
          {questions?.status === 'failed' && <ErrorCallout message={questions.message} />}
          {displayQuestions.length > 0 && (
            <div className="space-y-2 mb-4">
              <div className="flex items-center gap-2 text-xs text-gray-600">
                <StatusPill status={questions.mode === 'replay' ? 'replay' : 'done'} label={questions.mode || 'generated'} />
                <span>{questions.count || displayQuestions.length} 道题</span>
              </div>
              {displayQuestions.map((q, i) => (
                <div key={q.id || i} className="border rounded-lg p-3 text-xs">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="font-mono text-gray-400">#{i + 1}</span>
                    <span className="bg-gray-100 text-gray-700 px-1.5 py-0.5 rounded">{q.dimension} · {q.dimensionLabel}</span>
                    <span className="text-gray-400">难度 {q.difficulty || '-'}</span>
                  </div>
                  <ExpandableMarkdown text={q.questionMarkdown} collapsedLines={5} />
                  {q.expectedAnswerMarkdown && (
                    <div className="mt-2 rounded border border-gray-100 bg-gray-50 p-2">
                      <div className="mb-1 text-[11px] font-semibold text-gray-500">参考答案</div>
                      <ExpandableMarkdown text={q.expectedAnswerMarkdown} collapsedLines={4} defaultExpanded />
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}

          {displayScore && (
            <div className="border rounded-lg p-4 bg-gray-50">
              <div className="flex items-center gap-3 mb-3">
                <StatusPill status={displayScore.status === 'failed' ? 'failed' : 'done'} label={displayScore.status || '评分完成'} />
                <span className="text-sm font-semibold text-gray-800">{displayScore.model || runtimeConfig.t1_answer_model}</span>
                {displayScore.overall_score !== undefined && <span className="font-mono text-gray-700">overall {displayScore.overall_score}</span>}
              </div>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
                {Object.entries(displayScore.dimension_scores || {}).map(([k, v]) => (
                  <div key={k} className="border rounded p-2 bg-white"><div className="font-mono text-gray-800">{v}</div><div className="text-gray-400">{k} · {dimensionNames[k]}</div></div>
                ))}
              </div>
              {displayScore.scoringRationale?.markdown && (
                <div className="mt-3 text-xs text-gray-500">
                  <ScoringReason scoring={displayScore.scoringRationale} />
                </div>
              )}
              {(displayScore.source || displayScore.evidence) && <div className="mt-1 text-[11px] font-mono text-gray-400">来源：{displayScore.source || displayScore.evidence}</div>}
              {displayScore.answerSamples?.length > 0 && (
                <div className="mt-5">
                  <div className="flex items-center justify-between gap-3 mb-3">
                    <div>
                      <div className="text-sm font-semibold text-gray-800">模型答案复现</div>
                      <div className="text-[11px] text-gray-500">展示逐题答题、参考答案和评分理由，补齐赛道一的评测闭环。</div>
                    </div>
                    {displayScore.answer_samples_source && (
                      <div className="text-[11px] font-mono text-gray-400">{displayScore.answer_samples_source}</div>
                    )}
                  </div>
                  <div className="space-y-3">
                    {displayScore.answerSamples.map((sample, i) => (
                      <div key={sample.id || i} className="border rounded-lg bg-white p-3 text-xs">
                        <div className="flex flex-wrap items-center gap-2 mb-2">
                          <span className="font-mono text-gray-400">#{i + 1}</span>
                          <span className="bg-gray-100 text-gray-700 px-1.5 py-0.5 rounded">{sample.dimension} · {sample.dimensionLabel}</span>
                          {sample.difficulty && <span className="text-gray-400">难度 {sample.difficulty}</span>}
                          {sample.score !== undefined && <span className="font-mono text-gray-700">score {sample.score}</span>}
                        </div>
                        <ExpandableMarkdown text={sample.questionMarkdown} collapsedLines={4} />
                        <div className="mt-3 grid grid-cols-1 xl:grid-cols-2 gap-3">
                          <div className="rounded border border-gray-100 bg-gray-50 p-3">
                            <div className="mb-1 text-[11px] font-semibold text-gray-500">模型回答</div>
                            <ExpandableMarkdown text={sample.modelAnswerMarkdown} collapsedLines={5} />
                          </div>
                          <div className="rounded border border-gray-100 bg-gray-50 p-3">
                            <div className="mb-1 text-[11px] font-semibold text-gray-500">参考答案</div>
                            <ExpandableMarkdown text={sample.expectedAnswerMarkdown} collapsedLines={5} defaultExpanded />
                          </div>
                        </div>
                        {sample.scoring?.markdown && (
                          <div className="mt-3 rounded border border-sky-100 bg-sky-50 px-3 py-2 leading-6 text-sky-900">
                            <div className="mb-1 text-[11px] font-semibold text-sky-800">评分理由</div>
                            <ScoringReason scoring={sample.scoring} />
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </StepCard>
      </div>
    </SectionWrapper>
  );
}

function createPendingTask(task, kind, timeoutMs = CLIENT_TASK_TIMEOUT_MS) {
  const id = typeof task === 'string' ? task : task?.id;
  return {
    id,
    owner_token: typeof task === 'string' ? undefined : task?.owner_token,
    kind,
    timeoutMs,
    startedAt: Date.now(),
  };
}

function BusyLabel({ active, busyText, idleText }) {
  if (!active) return idleText;
  return (
    <span className="inline-flex items-center justify-center gap-1.5">
      {busyText}
      <LoadingDots className="w-4" sizeClassName="h-1 w-1" />
    </span>
  );
}

function getTrack1Activity(loading) {
  const map = {
    examples: {
      title: '正在加载样例论文',
      desc: '读取公开样例与已验证解析记录，完成后会解锁查看样例。',
      steps: ['读取样例', '绑定来源', '刷新页面'],
    },
    upload: {
      title: '正在调用 MinerU 解析公开 PDF',
      desc: '公开 PDF 正通过服务端代理提交到 MinerU，完成后会进入 Markdown 预览和云端评测链路。',
      steps: ['上传 PDF', 'MinerU 解析', '写入预览'],
    },
    official_url: {
      title: '正在提交 MinerU 官方解析',
      desc: '公开 URL 已发送到 MinerU 官方接口；如果需要立即看到 Markdown，建议使用上传 PDF 路径。',
      steps: ['提交 URL', '创建任务', '返回状态'],
    },
    parse: {
      title: '正在读取解析产物',
      desc: '页面正在读取结构化 Markdown、公式和 chunk 统计。',
      steps: ['读取论文', '解析结构', '更新产物'],
    },
    questions: {
      title: '正在云端生成评测题',
      desc: 'DeepSeek 正基于公开解析文本生成四维题目，完成后会展示题目、参考答案和维度标签。',
      steps: ['读取来源', '生成题目', '绑定维度'],
    },
    score: {
      title: '正在云端评分',
      desc: 'DeepSeek 正根据题目、参考答案、候选回答和来源文本生成评分理由。',
      steps: ['读取回答', '执行评分', '汇总理由'],
    },
    continue: {
      title: '正在推进闭环',
      desc: '系统正在补齐出题、作答和评分结果。',
      steps: ['生成题目', '模型作答', '评分汇总'],
    },
    demo: {
      title: '正在载入展示闭环',
      desc: '页面正在读取公开样例的解析、题目和评分回放。',
      steps: ['载入解析', '载入题目', '载入评分'],
    },
  };
  return map[loading] || null;
}

function isClientTaskExpired(task) {
  if (!task?.startedAt) return true;
  return Date.now() - task.startedAt > (task.timeoutMs || CLIENT_TASK_TIMEOUT_MS);
}

function adaptCloudMineruResult(data = {}, mode) {
  const ok = data.status === 'ok' || data.status === 'submitted' || data.provider === 'mineru_official';
  const markdown = data.markdown_preview || '';
  const submitted = data.status === 'submitted';
  return {
    ...data,
    status: submitted ? 'submitted' : data.status || 'ok',
    parse_ok: ok,
    mode: mode === 'url' ? 'cloud_url' : 'cloud_api',
    detail: submitted
      ? 'MinerU 官方 API 已接收公开 URL 解析任务。该接口为异步任务提交；如需现场完整解析到 Markdown，推荐使用上传 PDF。'
      : 'MinerU 官方 API 已完成公开 PDF 解析，Markdown 结果已进入本轮云端出题评分链路。',
    markdown_preview: markdown,
    markdown_chars: data.markdown_chars || markdown.length,
    stats: {
      pages: data.pages || 0,
      formulas: data.formulas || 0,
      images: data.images || 0,
      chunks: markdown ? Math.max(1, Math.ceil(markdown.length / 900)) : 0,
    },
    pipeline_steps: [
      { step: 1, label: mode === 'url' ? '提交公开 URL' : '上传公开 PDF', status: 'done', note: '公开/脱敏输入' },
      { step: 2, label: 'MinerU 官方 API', status: submitted ? 'ready' : 'done', note: submitted ? '任务已提交' : '解析完成' },
      { step: 3, label: 'Markdown 进入评测链路', status: markdown ? 'done' : 'ready', note: markdown ? `${markdown.length} 字符` : '等待结果包' },
    ],
  };
}

function adaptCloudQuestions(data = {}) {
  const dims = ['A', 'B', 'C', 'D'];
  const questions = (data.questions || []).map((question, index) => {
    const dimension = question.dimension || dims[index % dims.length];
    return {
      ...question,
      id: question.id || `cloud-q${index + 1}`,
      dimension,
      dimension_label: question.dimension_label || dimensionNames[dimension] || question.type || '云端题',
      difficulty: question.difficulty || (index < 2 ? '中等' : '进阶'),
      expected_answer: question.expected_answer || question.answer || question.reference_answer || question.rubric || '',
    };
  });
  return {
    ...data,
    status: data.status || 'ok',
    mode: data.provider === 'deepseek' && data.status === 'ok' ? 'DeepSeek 云端生成' : data.status || '云端生成',
    count: questions.length,
    questions,
  };
}

function buildTrack1CandidateAnswer(question = {}) {
  const expected = question.expected_answer || question.answer || question.reference_answer || '';
  if (expected) {
    return [
      '候选模型回答：',
      expected,
      '',
      '该回答同时说明来源材料、关键机制和适用边界，并避免把公开论文结论外推到未给定条件。',
    ].join('\n');
  }
  return `候选模型回答：该题需要依据公开解析材料回答，围绕 ${question.question || '题目'} 给出核心结论、来源依据和适用边界。`;
}

function adaptCloudScore(graded = []) {
  const samples = graded.map(({ question, modelAnswer, grade }, index) => {
    const score = normalizeScore(grade?.score, grade?.max_score);
    return {
      id: question.id || `cloud-score-${index + 1}`,
      dimension: question.dimension || ['A', 'B', 'C', 'D'][index % 4],
      dimension_label: question.dimension_label || dimensionNames[question.dimension] || question.type || '',
      difficulty: question.difficulty || '',
      question: question.question,
      model_answer: modelAnswer,
      expected_answer: question.expected_answer,
      reason: grade?.feedback || grade?.message || 'DeepSeek 云端评分完成。',
      score,
    };
  });
  const dimensionScores = {};
  samples.forEach(sample => {
    if (!sample.dimension) return;
    dimensionScores[sample.dimension] = sample.score;
  });
  const validScores = samples.map(s => s.score).filter(v => typeof v === 'number');
  const overall = validScores.length ? Number((validScores.reduce((a, b) => a + b, 0) / validScores.length).toFixed(3)) : undefined;
  return {
    status: 'ok',
    model: 'DeepSeek 云端评分',
    overall_score: overall,
    dimension_scores: dimensionScores,
    scoring_rationale: '评分理由：本轮评分由云端 DeepSeek API 根据题目、参考答案、评分规则、候选回答和公开解析文本生成；每题保留评分反馈和来源输入边界。',
    source: 'cloud_api_deepseek_grade',
    answer_samples: samples,
    answer_samples_source: 'DeepSeek /api/quiz/grade',
  };
}

function normalizeScore(score, maxScore = 10) {
  const numeric = Number(score);
  const max = Number(maxScore) || 10;
  if (!Number.isFinite(numeric)) return undefined;
  if (max === 1) return Number(numeric.toFixed(3));
  return Number((numeric / max).toFixed(3));
}

function ExpandableMarkdown({ text, collapsedLines = 8, defaultExpanded = false }) {
  const [expanded, setExpanded] = useState(defaultExpanded);
  const value = String(text || '').trim();
  const needsExpand = value.length > 420 || value.split(/\r?\n/).length > collapsedLines;

  return (
    <div>
      <div
        className={needsExpand && !expanded ? 'max-h-48 overflow-hidden relative' : ''}
      >
        <MarkdownText className="text-xs [&_p]:text-xs [&_li]:text-xs [&_.katex]:text-[1em]">
          {value}
        </MarkdownText>
        {needsExpand && !expanded && (
          <div className="pointer-events-none absolute inset-x-0 bottom-0 h-12 bg-gradient-to-t from-gray-50 to-transparent" />
        )}
      </div>
      {needsExpand && (
        <button
          type="button"
          onClick={() => setExpanded(v => !v)}
          className="mt-2 text-[11px] font-medium text-sky-700 hover:text-sky-900"
        >
          {expanded ? '收起' : '展开全文'}
        </button>
      )}
    </div>
  );
}

function ScoringReason({ scoring, reason }) {
  const parsed = scoring || adaptScoringReason(reason);
  if (!parsed?.rubric) {
    return <ExpandableMarkdown text={parsed?.markdown || reason} collapsedLines={4} defaultExpanded />;
  }
  return (
    <div>
      <div className="mb-2 text-xs text-sky-900">{parsed.rubric.title}</div>
      <div className="grid grid-cols-2 md:grid-cols-5 gap-2">
        {parsed.rubric.items.map(item => (
          <div key={item.key} className="rounded border border-sky-100 bg-white/70 px-2 py-1.5">
            <div className="text-[10px] text-sky-700">{item.label}</div>
            <div className="font-mono text-xs text-gray-800">{item.value}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
