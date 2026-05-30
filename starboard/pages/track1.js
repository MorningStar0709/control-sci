import { useEffect, useMemo, useState } from 'react';
import SectionWrapper from '../components/SectionWrapper';
import ErrorCallout from '../components/workbench/ErrorCallout';
import PipelineStep from '../components/workbench/PipelineStep';
import RuntimeSummary from '../components/workbench/RuntimeSummary';
import StepCard from '../components/workbench/StepCard';
import StatusPill from '../components/workbench/StatusPill';
import WorkbenchLoadingCard from '../components/workbench/WorkbenchLoadingCard';
import MarkdownText from '../components/workbench/MarkdownText';
import { apiGet, apiRequest, getApiTask, startApiTask, startApiSequenceTask, toFailure } from '../lib/apiClient';
import { adaptScoringReason, adaptTrack1Question, adaptTrack1ScoreResult } from '../lib/track1DisplayAdapter';
import useSessionState from '../lib/useSessionState';

const CLIENT_TASK_TIMEOUT_MS = 6 * 60 * 1000;
const TRACK1_SESSION_VERSION = 3;

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
    desc: '原文、chunk、向量索引和微调样本默认本地，公开或脱敏任务才允许云端兜底。',
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
  ['部署边界', '本地优先，API 只处理公开或脱敏派生任务'],
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

  const inputReady = Boolean(selected || uploadResult?.filename);

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

  useEffect(() => {
    if ((loading === 'examples' || loading === 'upload') && !pendingTask?.id) {
      patchPersisted({ loading: '', pendingTask: null });
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

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
    if (loading && !pendingTask?.id && loading !== 'examples' && loading !== 'upload') {
      patchPersisted({ loading: '', pendingTask: null });
      return;
    }
    if (pendingTask?.id && loading) pollTrack1Task(pendingTask);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pendingTask?.id, loading]);

  async function loadExamples() {
    setLoading('examples');
    try {
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
    } finally {
      setLoading('');
    }
  }

  async function runTrack1Demo() {
    setLoading('demo');
    setError(null);
    setUploadResult(null);
    setParseResult(null);
    setQuestions(null);
    setScoreResult(null);

    const examples = await apiGet('/api/demo/track1/examples', { timeoutMs: 12000 });
    if (!examples.ok || !examples.data.papers?.length) {
      setError(toFailure(examples.error || '未找到赛道一样例论文'));
      setLoading('');
      return;
    }

    const paper = examples.data.papers[0];
    setPapers(examples.data.papers || []);
    setSelected(paper.id);
    setSource('selected');

    const task = await startApiSequenceTask([
      { key: 'parse', path: '/api/demo/track1/parse', body: { paper_id: paper.id, mode: runtimeConfig.parser_backend || 'replay' }, timeoutMs: 30000 },
      { key: 'questions', path: '/api/demo/track1/generate_questions/v2', body: { source: 'core_json', paper_id: paper.id, n: 4 }, timeoutMs: 90000 },
      { key: 'score', path: '/api/demo/track1/answer_and_score', body: {
        paper_id: paper.id,
        model_choice: runtimeConfig.t1_answer_model || runtimeConfig.local_model || 'replay',
        judge_model: runtimeConfig.t1_judge_model || 'replay',
      }, timeoutMs: 90000 },
    ], { runtimeConfig, timeoutMs: 210000 });
    if (task.ok) patchPersisted({ loading: 'demo', pendingTask: createPendingTask(task.data, 'demo', 240000) });
    else { setError(toFailure(task.error)); setLoading(''); }
  }

  async function uploadPdf() {
    if (!uploadedFile) return;
    setLoading('upload');
    setError(null);
    const form = new FormData();
    form.append('pdf', uploadedFile);
    const result = await apiRequest('/api/demo/track1/upload', {
      method: 'POST',
      body: form,
      runtimeConfig,
      timeoutMs: 60000,
    });
    if (result.ok) {
      setUploadResult(result.data);
      setSelected('');
      setSource('uploaded');
      setParseResult(null);
      setQuestions(null);
      setScoreResult(null);
    } else {
      setError(toFailure(result.error));
    }
    setLoading('');
  }

  async function parseUploadedPdf() {
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
    const result = await startApiTask('/api/demo/track1/parse_url', {
      url: officialUrl.trim(),
      model_version: 'vlm',
    }, { runtimeConfig, timeoutMs: 45000 });
    if (result.ok) {
      patchPersisted({ loading: 'official_url', pendingTask: createPendingTask(result.data, 'parse', 75000) });
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

  async function continueQuestionAndScore() {
    if (!inputReady) return;
    setLoading('continue');
    setError(null);

    const body = source === 'uploaded' && uploadResult
      ? { source: 'uploaded', uploaded_filename: uploadResult.filename, n: 4 }
      : { source: 'core_json', paper_id: selected, n: 4 };

    const task = await startApiTask('/api/demo/track1/validate_chain', {
      ...body,
      paper_id: selected || 'uploaded',
      model_choice: runtimeConfig.t1_answer_model || runtimeConfig.local_model || 'replay',
      judge_model: runtimeConfig.t1_judge_model || 'replay',
    }, { runtimeConfig, timeoutMs: 180000 });
    if (task.ok) patchPersisted({ loading: 'continue', pendingTask: createPendingTask(task.data, 'continue', 210000) });
    else { setQuestions(toFailure(task.error)); setLoading(''); }
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
    if (!inputReady) return;
    setLoading('questions');
    setError(null);
    const body = source === 'uploaded' && uploadResult
      ? { source: 'uploaded', uploaded_filename: uploadResult.filename, n: 4 }
      : { source: 'core_json', paper_id: selected, n: 4 };
    const result = await startApiTask('/api/demo/track1/generate_questions/v2', body, { runtimeConfig, timeoutMs: 90000 });
    if (result.ok) patchPersisted({ loading: 'questions', pendingTask: createPendingTask(result.data, 'questions', 120000) });
    else { setQuestions(toFailure(result.error)); setLoading(''); }
  }

  async function answerAndScore() {
    if (!inputReady) return;
    setLoading('score');
    const result = await startApiTask('/api/demo/track1/answer_and_score', {
      paper_id: selected || 'uploaded',
      model_choice: runtimeConfig.t1_answer_model || runtimeConfig.local_model || 'replay',
      judge_model: runtimeConfig.t1_judge_model || 'replay',
      source,
      uploaded_filename: source === 'uploaded' ? uploadResult?.filename : '',
      questions: questions?.questions || [],
    }, { runtimeConfig, timeoutMs: 90000 });
    if (result.ok) patchPersisted({ loading: 'score', pendingTask: createPendingTask(result.data, 'score', 120000) });
    else { setScoreResult(toFailure(result.error)); setLoading(''); }
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
  const runMode = buildTrack1RunMode(runtimeConfig, scoreResult);

  return (
    <SectionWrapper>
      <div className="custom-screen space-y-6">
        <div>
          <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-3">
            <div>
              <h1 className="text-gray-800 text-3xl font-semibold sm:text-4xl mb-2">赛道一：Sci-Align 最小复现工作台</h1>
              <p className="text-gray-600 text-sm">本地体验 PDF 结构化、四维出题、模型答题和评分绑定；完整实验论证保留在报告一与 DATA-TRACE。</p>
              <p className="mt-1 text-[11px] text-gray-500">工作台负责可感知的最小闭环，不复刻报告 dashboard；批量排行榜、Judge 校准与训练探针请从复核入口进入。</p>
            </div>
            <button type="button" onClick={runTrack1Demo} disabled={loading === 'demo'} className="px-4 py-2 bg-gray-900 text-white rounded text-xs disabled:opacity-50">
              {loading === 'demo' ? '最小复现执行中' : '运行最小复现链路'}
            </button>
          </div>
        </div>

        <RuntimeSummary runtimeConfig={runtimeConfig} variant="track1" extraItems={runMode.items} />
        <div className="rounded-lg border border-amber-100 bg-amber-50 px-4 py-3 text-xs leading-5 text-amber-900">
          <div className="font-semibold">运行边界：{runMode.label}</div>
          <div className="mt-1">{runMode.desc}</div>
        </div>
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
              <div className="text-sm font-semibold text-sky-950">推荐复现路径</div>
              <div className="mt-1 text-xs leading-5 text-sky-900">
                本页只证明交互闭环可运行；完整报告、DATA-TRACE、证据包和 CLI 入口统一收敛到“来源矩阵”，避免在最小工作台里分散跳转。需要动手时，点击右上角“运行最小复现链路”。
              </div>
              <div className="mt-3 rounded border border-sky-200 bg-white/70 px-3 py-2 text-[11px] leading-5 text-sky-900">
                复核入口：请使用顶部 / 侧栏的“来源矩阵”查看报告、DATA-TRACE、manifest 与复现命令；本页不直接打开磁盘文档。
              </div>
            </div>
            <button type="button" onClick={continueQuestionAndScore} disabled={!inputReady || loading === 'continue'} className="w-full md:w-auto px-4 py-2 bg-sky-700 text-white rounded text-xs disabled:opacity-50">
              {loading === 'continue' ? '分步复核中' : '继续出题评分'}
            </button>
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
                <button type="button" onClick={uploadPdf} disabled={!uploadedFile || loading === 'upload'} className="px-4 py-2 bg-gray-900 text-white text-xs rounded disabled:opacity-50">
                  {loading === 'upload' ? '上传中' : '上传'}
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
                <button type="button" onClick={parseOfficialUrl} disabled={!officialUrl.trim() || loading === 'official_url'} className="w-full px-4 py-2 bg-gray-900 text-white text-xs rounded disabled:opacity-50">
                  {loading === 'official_url' ? '提交中' : '提交官方解析'}
                </button>
              </div>
              <div className="mt-2 text-[11px] text-gray-500">仅适合公开/脱敏 URL；本地 PDF 和敏感文档仍走 Docker 或已验证产物。</div>
            </div>

            <div className="border rounded-lg p-4 bg-gray-50">
              <div className="flex items-center justify-between mb-3">
                <div className="text-xs font-semibold text-gray-700">样例论文</div>
                <button type="button" onClick={loadExamples} disabled={loading === 'examples'} className="px-3 py-1.5 border rounded text-xs hover:bg-white">
                  {loading === 'examples' ? '加载中' : '加载样例'}
                </button>
              </div>
              <select value={selected} onChange={e => { setSelected(e.target.value); setSource('selected'); setUploadResult(null); resetAfterInput(); }} className="w-full border rounded px-3 py-2 text-sm">
                <option value="">选择一篇样例论文</option>
                {papers.map(p => <option key={p.id} value={p.id}>{p.arxiv_id} - {p.title}</option>)}
              </select>
              <div className="mt-2 text-[11px] text-gray-500">样例路径来自数据飞轮产物，默认按 PDF 大小排序以缩短现场验证时间。</div>
            </div>
          </div>
        </StepCard>

        <StepCard
          index="2"
          title="解析与结构化"
          desc="优先调用 MinerU Docker；依赖不可用时读取已验证解析产物。"
          status={parseResult?.parse_ok ? 'done' : parseResult?.status === 'replay' ? 'replay' : loading === 'parse' || loading === 'demo' ? 'running' : parseSteps.length ? 'ready' : 'pending'}
          actions={
            <div className="flex gap-2">
              <button type="button" onClick={inspectSelectedPaper} disabled={!selected || loading === 'parse'} className="px-3 py-1.5 border rounded text-xs hover:bg-white disabled:opacity-50">检查样例</button>
              <button type="button" onClick={parseUploadedPdf} disabled={!uploadResult?.filename || loading === 'parse'} className="px-3 py-1.5 bg-gray-900 text-white rounded text-xs disabled:opacity-50">解析上传</button>
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
          desc="生成 A/B/C/D 四维题目，并把本轮题目、回答和评分绑定到同一复现链路。"
          status={scoreResult ? 'done' : loading === 'questions' || loading === 'score' || loading === 'continue' || loading === 'demo' ? 'running' : questions ? 'ready' : 'pending'}
          actions={
            <div className="flex gap-2">
              <button type="button" onClick={generateQuestions} disabled={!inputReady || loading === 'questions'} className="px-3 py-1.5 border rounded text-xs hover:bg-white disabled:opacity-50">生成题目</button>
              <button type="button" onClick={answerAndScore} disabled={!inputReady || loading === 'score'} className="px-3 py-1.5 bg-gray-900 text-white rounded text-xs disabled:opacity-50">答题评分</button>
              <button type="button" onClick={continueQuestionAndScore} disabled={!inputReady || loading === 'continue'} className="px-3 py-1.5 bg-sky-600 text-white rounded text-xs disabled:opacity-50">{loading === 'continue' ? '分步复核中' : '继续出题评分'}</button>
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

function isClientTaskExpired(task) {
  if (!task?.startedAt) return true;
  return Date.now() - task.startedAt > (task.timeoutMs || CLIENT_TASK_TIMEOUT_MS);
}

function buildTrack1RunMode(runtimeConfig, scoreResult) {
  const answerModel = runtimeConfig?.t1_answer_model || 'replay';
  const judgeModel = runtimeConfig?.t1_judge_model || 'replay';
  const usage = scoreResult?.usage || scoreResult?.token_usage || null;
  const provider = usage?.provider || runtimeConfig?.api_provider || '未启用';
  if (answerModel === 'replay' && judgeModel === 'replay') {
    return {
      label: '产物复现 · 0 API tokens',
      desc: '当前使用已验证产物复现最小链路，不调用云端模型，不上传原文。完整大规模实验仍以报告与证据包为准。',
      items: [['T1 模式', 'replay'], ['API tokens', '0']],
    };
  }
  if (usage) {
    const tokens = usage.total_tokens ?? usage.tokens ?? '-';
    const cost = usage.cost_cny ?? usage.estimated_cost_cny;
    return {
      label: `${provider} · ${tokens} tokens`,
      desc: cost !== undefined ? `本轮由后端返回 token usage，估算成本 ${cost} CNY；仅公开或脱敏派生任务允许进入云端。` : '本轮由后端返回 token usage；仅公开或脱敏派生任务允许进入云端。',
      items: [['T1 模式', 'api'], ['API tokens', String(tokens)]],
    };
  }
  return {
    label: '混合/本地模式 · usage 待后端返回',
    desc: '页面会显示当前模型选择；若后端返回 usage，将在本区块更新 token 与成本。未授权原文不会上传云端。',
    items: [['T1 Answer', answerModel], ['T1 Judge', judgeModel]],
  };
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
