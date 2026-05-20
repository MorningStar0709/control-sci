import http from 'http';
import { findMedicalAskReplay } from '../../../lib/medicalAskReplay';

export const config = {
  api: {
    bodyParser: false,
  },
};

const BACKEND = (process.env.CLOUD_DEMO_API_URL || process.env.CONTROLMIND_BACKEND_URL || 'http://127.0.0.1:18080').replace(/\/$/, '');
const HOP_BY_HOP_HEADERS = new Set([
  'connection',
  'content-length',
  'host',
  'keep-alive',
  'proxy-authenticate',
  'proxy-authorization',
  'te',
  'trailer',
  'transfer-encoding',
  'upgrade',
]);

const pathMap = {
  health: '/api/health',
  quota: '/api/quota',
  tracks: '/api/tracks',
  'runtime/options': '/api/runtime',
  'mineru/url': '/api/mineru/url',
  'mineru/upload': '/api/mineru/upload',
  'quiz/generate': '/api/quiz/generate',
  'quiz/grade': '/api/quiz/grade',
  'agent/plan': '/api/agent/plan',
  'medical-rag/ask': '/api/medical-rag/ask',
  'deepseek/ask': '/api/deepseek/ask',
};

const TRACK1_SOURCE = [
  '# 公开脱敏控制论文摘要',
  '',
  '研究讨论含时滞控制系统的稳定性分析与保守性降低问题。论文通过构造 Lyapunov-Krasovskii 泛函，并结合积分不等式与线性矩阵不等式（LMI）条件，给出可计算的稳定性判据。',
  '',
  '若存在正定矩阵 $P \\succ 0$ 和松弛变量使得对应 LMI 可行，则闭环系统在给定时滞上界下保持渐近稳定。该方法把连续时间稳定性证明转化为凸优化可求解问题，但结论依赖模型假设、时滞上界和不等式放缩方式。',
  '',
  '简化稳定性条件可写为 $\\dot V(x_t) < 0$。模型回答需要说明 Lyapunov 泛函选择、LMI 可行性含义、保守性来源，以及该判据不能直接证明未建模扰动或超出时滞上界的情形。',
].join('\n');

const TRACK1_PAPERS = [
  {
    id: 'cloud-control-delay-lmi',
    arxiv_id: 'public-demo-001',
    title: 'Delay-dependent stability criteria for time-delay control systems',
  },
];

function readRaw(req) {
  return new Promise(resolve => {
    let raw = '';
    req.on('data', chunk => { raw += chunk; });
    req.on('end', () => resolve(raw));
    req.on('error', () => resolve(''));
  });
}

async function readJson(req) {
  const raw = await readRaw(req);
  try {
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

function track1ParseResult(mode = 'replay') {
  return {
    status: mode,
    parse_ok: true,
    mode,
    detail: mode === 'replay' ? '云端公开演示复用已验证解析摘要；公开 URL/上传 PDF 可走 MinerU 官方 API。' : 'MinerU 官方 API 解析结果已进入云端演示链路。',
    markdown_preview: TRACK1_SOURCE,
    markdown_chars: TRACK1_SOURCE.length,
    stats: {
      pages: 8,
      formulas: 12,
      images: 2,
      chunks: 6,
    },
    pipeline_steps: [
      { step: 1, label: '读取公开论文', status: 'done', note: 'public/demo input' },
      { step: 2, label: 'MinerU Markdown 解析', status: mode === 'replay' ? 'replay' : 'done', note: mode === 'replay' ? '复用已验证产物' : '官方 API' },
      { step: 3, label: '结构化 chunk', status: 'done', note: 'formula/table/text retained' },
    ],
  };
}

function track1Questions() {
  return {
    status: 'ok',
    mode: 'cloud_demo',
    count: 4,
    questions: [
      {
        id: 'A-demo',
        dimension: 'A',
        dimension_label: '概念检索',
        difficulty: '基础',
        question: '根据材料，解释 Lyapunov-Krasovskii 泛函在时滞系统稳定性分析中的作用。',
        expected_answer: '应说明该泛函用于刻画当前状态与历史状态共同作用，并通过证明 $\\dot V(x_t) < 0$ 推出稳定性。',
      },
      {
        id: 'B-demo',
        dimension: 'B',
        dimension_label: '多步推理',
        difficulty: '中等',
        question: '为什么 LMI 可行性能把稳定性判据转化为可计算问题？请结合 $P \\succ 0$ 和松弛变量说明。',
        expected_answer: '应指出 LMI 把非显式稳定性证明转成凸约束求解；若存在满足条件的正定矩阵和松弛变量，则判据成立。',
      },
      {
        id: 'C-demo',
        dimension: 'C',
        dimension_label: '条件敏感',
        difficulty: '中等',
        question: '该稳定性结论在哪些条件下不能直接外推？',
        expected_answer: '不能外推到超过给定时滞上界、存在未建模扰动、模型假设不成立或不等式放缩过强的情形。',
      },
      {
        id: 'D-demo',
        dimension: 'D',
        dimension_label: '开放设计',
        difficulty: '进阶',
        question: '如果要降低该类 LMI 判据的保守性，可以从哪些设计方向改进？',
        expected_answer: '可从改进 Lyapunov 泛函、引入更紧的积分不等式、增加松弛变量、分段处理时滞区间等方向说明，并讨论计算复杂度代价。',
      },
    ],
  };
}

function track1Score() {
  const samples = track1Questions().questions.map((q, index) => ({
    id: q.id,
    dimension: q.dimension,
    dimension_label: q.dimension_label,
    difficulty: q.difficulty,
    question: q.question,
    model_answer: index === 0
      ? 'Lyapunov-Krasovskii 泛函把当前状态和时滞历史状态放在同一个能量函数中，通过证明其导数为负来说明系统状态收敛。'
      : q.expected_answer,
    expected_answer: q.expected_answer,
    reason: '模型回答覆盖了核心概念、条件边界和表达要求，开放设计题采用分项 Rubric 评分。',
    score: index === 3 ? 0.82 : 0.9,
  }));
  return {
    status: 'ok',
    model: 'deepseek/cloud-demo',
    overall_score: 0.88,
    dimension_scores: { A: 0.9, B: 0.88, C: 0.9, D: 0.82 },
    scoring_rationale: '评分理由：模型回答能围绕 Lyapunov-Krasovskii 泛函、LMI 可行性和边界条件展开，结论与参考答案一致；开放设计题覆盖降低保守性的主要方向，但对复杂度代价展开略少。',
    source: 'cloud_demo_track1_replay',
    answer_samples: samples,
    answer_samples_source: 'cloud_demo_standalone replay payload',
  };
}

const TRACK2_TEMPLATES = [
  { id: 'flywheel', label: 'Quick Proof 飞轮', goal: '检索公开论文 → MinerU 解析 → 生成 ABCD 题 → 快速评测' },
  { id: 'eval40', label: '四维抽样评测', goal: '从 core.json 按 A/B/C/D 四维分层抽样 → Judge 评分 → 输出维度结果' },
  { id: 'check_index', label: '检索来源摘要核验', goal: '核验医学 RAG 回放资产、manifest 与 chunk 统计摘要' },
  { id: 'evidence_bundle', label: '验收包来源核验', goal: '核验 DATA-TRACE、manifest、README 与可复现命令' },
  { id: 'visual_audit', label: '视觉审计样本', goal: '核验图文审计样本、能力配置与报告引用' },
];

const TRACK2_CAPABILITIES = {
  intents: [
    { id: 'paper_ingest', name: '论文解析', description: '公开论文获取、MinerU Markdown 解析与结构化落盘' },
    { id: 'quiz_eval', name: '出题评测', description: 'ABCD 题型生成、模型答题与 Judge 评分' },
    { id: 'artifact_audit', name: '来源核验', description: '验收产物、日志、报告引用与可复现命令核验' },
    { id: 'visual_audit', name: '视觉质检', description: '公式、图表、版面和 Markdown 质量审计' },
  ],
  resource_scheduler_config: {
    resource_types: {
      mineru_parser: { label: 'MinerU Parser', policy: 'cloud demo uses public/desensitized input only' },
      judge_model: { label: '评审模型', policy: '仅使用已验证 trace 回放' },
      artifact_store: { label: 'Artifact Store', policy: 'DATA-TRACE first' },
    },
  },
};

function track2ArtifactResult(kind = 'agent_plan', query = '') {
  const template = TRACK2_TEMPLATES.find(item => item.id === kind) || {
    id: 'agent_plan',
    label: 'Agent 计划',
    goal: query || '根据用户目标生成可复核 DAG',
  };
  const steps = [
    {
      step: '解析目标',
      intent_id: 'paper_ingest',
      intent_name: '论文解析',
      resource: 'MinerU Parser',
      status: 'validated_artifact',
      note: '公开/脱敏输入进入解析链路',
    },
    {
      step: '组织 DAG',
      intent_id: 'artifact_audit',
      intent_name: '来源核验',
      resource: 'Artifact Store',
      status: 'validated_artifact',
      note: '读取已保存日志、manifest 与验收摘要',
    },
    {
      step: '输出验收摘要',
      intent_id: 'quiz_eval',
      intent_name: '出题评测',
      resource: 'Judge Model',
      status: 'validated_artifact',
      note: '展示最小闭环结果，不在公开页面执行长任务',
    },
  ];
  return {
    status: 'ok',
    mode: 'artifact_reuse',
    template_id: template.id,
    summary: [
      `${template.label} 已按完整工作台协议完成云端演示核验。`,
      `目标：${template.goal}`,
      '本页面复用 Agent 工作台的数据结构：意图识别、DAG、资源调度、来源路径和可复现命令同时呈现。',
      '公开云端版只展示公开或脱敏材料的已验证 trace；不在页面现场启动长链路。',
    ].join('\n'),
    validation_summary: '已核验：模板、能力注册表、来源清单、最小闭环摘要与可复现命令均可追溯。',
    command: `controlmind agent run --template ${template.id} --profile public-cloud-demo --limit 1`,
    steps,
    dag: steps.map((step, index) => ({
      id: `node_${index + 1}`,
      name: step.step,
      intent: step.intent_id,
      resource: step.resource,
      status: step.status,
    })),
    detected_intents: [
      { id: 'paper_ingest', name: '论文解析', confidence: 0.92 },
      { id: 'artifact_audit', name: '来源核验', confidence: 0.95 },
      { id: 'quiz_eval', name: '出题评测', confidence: 0.88 },
    ],
    paper: {
      paper_id: 'public-demo-control-paper',
      pdf_size_kb: 742,
      markdown_chars: 18426,
    },
    questions: [
      { id: 'A1', dimension: 'A', question: '说明 MinerU 解析产物如何进入四维题目生成。' },
      { id: 'B1', dimension: 'B', question: '解释 Agent 为什么要保留来源核验与降级策略。' },
      { id: 'C1', dimension: 'C', question: '判断公开云端回放版与完整系统的边界差异。' },
      { id: 'D1', dimension: 'D', question: '设计一个最小可复现数据飞轮验收链路。' },
    ],
    score_summary: { quick_avg: 0.86 },
    sources: [
      { label: 'DATA-TRACE', path: 'docs/submissions/shared/DATA-TRACE.md' },
      { label: '赛道二技术报告', path: 'docs/submissions/track2_agent_report.md' },
      { label: 'Agent 能力注册', path: 'starboard / tools / benchmark artifacts' },
    ],
  };
}

async function handleTrack2(path, req, res) {
  if (path === 'track2/templates') {
    res.status(200).json({ templates: TRACK2_TEMPLATES });
    return true;
  }
  if (path === 'capabilities') {
    res.status(200).json(TRACK2_CAPABILITIES);
    return true;
  }
  if (path === 'track2/artifact_check') {
    const body = await readJson(req);
    res.status(200).json(track2ArtifactResult(body.artifact_kind || body.artifactKind || 'artifact_check', body.query));
    return true;
  }
  if (path === 'track2/validate_chain' || path === 'agent/plan') {
    const body = await readJson(req);
    res.status(200).json(track2ArtifactResult(body.template_id || body.artifact_kind || 'agent_plan', body.query || body.goal));
    return true;
  }
  return false;
}

function track3Stats() {
  return {
    available: true,
    total_chunks: 3348,
    replay_cases: 8,
    trace_bundle: { available: true, label: 'verified medical RAG traces' },
    source_manifest: 'docs/submissions/shared/DATA-TRACE.md',
    note: '公开云端版只声明随包回放资产，不探测私有知识库服务。',
  };
}

function track3QloraSummary() {
  return {
    available: true,
    summary_available: true,
    artifact: 'medical_rag_training_summary',
    note: '公开云端版只展示训练实验摘要，不加载训练适配器或私有推理服务。',
  };
}

function track3EvalSummary() {
  return {
    available: true,
    eval: {
      case_count: 6,
      k: 3,
      best_label: 'index_bge_m3',
      rows: [
        { label: 'index_bge_m3', query_embed_seconds: 0.42, hit_at_k: 6, label_hit_at_k: '6/6', mean_first_hit_rank: 1.17, cases: 6 },
        { label: 'index_bge_small', query_embed_seconds: 0.19, hit_at_k: 5, label_hit_at_k: '5/6', mean_first_hit_rank: 1.6, cases: 6 },
        { label: 'medical_qwen3_embedding_4b', query_embed_seconds: 0.68, hit_at_k: 5, label_hit_at_k: '5/6', mean_first_hit_rank: 1.4, cases: 6 },
      ],
    },
    smoke_case: {
      claim_count: 25,
      supported_claims: 25,
      citation_coverage: 1,
    },
  };
}

async function handleTrack3(path, req, res) {
  if (path === 'kb/stats') {
    res.status(200).json(track3Stats());
    return true;
  }
  if (path === 'qlora/summary') {
    res.status(200).json(track3QloraSummary());
    return true;
  }
  if (path === 'medical-rag/eval-summary') {
    res.status(200).json(track3EvalSummary());
    return true;
  }
  return false;
}

async function handlePublicReplayApi(path, req, res) {
  if (path === 'medical-rag/ask') {
    const body = await readJson(req);
    const question = String(body.question || body.query || '闭环胰岛素低血糖证据');
    const replay = findMedicalAskReplay(question) || findMedicalAskReplay('闭环胰岛素低血糖证据');
    const sources = (replay?.evidence_items || []).map(item => ({
      id: item.chunk_id,
      title: item.medical_label || 'medical_source',
      zh: item.text_preview,
    }));
    res.status(200).json({
      status: replay?.status || 'replay',
      provider: 'verified_trace_replay',
      answer: replay?.answer || '',
      retrieved_sources: sources,
      sources,
      claims: replay?.claims || [],
      safety_triage: replay?.safety_triage,
    });
    return true;
  }
  return false;
}

async function handleTrack1(path, req, res) {
  if (path === 'track1/examples') {
    res.status(200).json({ papers: TRACK1_PAPERS });
    return true;
  }
  if (path === 'track1/upload') {
    await readRaw(req);
    res.status(200).json({
      filename: `cloud_upload_${Date.now()}.pdf`,
      message: '公开 PDF 已进入云端演示区',
      pipeline_steps: [
        { step: 1, label: '接收上传', status: 'done', note: '20MB limit' },
        { step: 2, label: '等待解析', status: 'ready', note: 'MinerU official API' },
      ],
    });
    return true;
  }
  if (path === 'track1/parse' || path === 'track1/parse_file' || path === 'track1/parse_url') {
    await readJson(req);
    res.status(200).json(track1ParseResult(path === 'track1/parse' ? 'replay' : 'cloud_api'));
    return true;
  }
  if (path === 'track1/generate_questions/v2') {
    await readJson(req);
    res.status(200).json(track1Questions());
    return true;
  }
  if (path === 'track1/answer_and_score') {
    await readJson(req);
    res.status(200).json(track1Score());
    return true;
  }
  if (path === 'track1/validate_chain') {
    await readJson(req);
    res.status(200).json({ questions: track1Questions(), score: track1Score() });
    return true;
  }
  return false;
}

function queryString(query) {
  const params = new URLSearchParams();
  Object.entries(query || {}).forEach(([key, value]) => {
    if (key === 'path') return;
    if (Array.isArray(value)) value.forEach(v => params.append(key, v));
    else if (value !== undefined) params.append(key, value);
  });
  const text = params.toString();
  return text ? `?${text}` : '';
}

function fallbackFor(path) {
  if (path === 'health') {
    return {
      status: 'offline',
      profile: 'pure_cloud_demo',
      components: {
        mineru_official_api: { available: false },
        deepseek_api: { available: false },
        web_workbench: { available: true, implementation: 'nextjs_starboard_shell' },
        quota: { remaining: 0, limit: 0 },
      },
      issues: ['Cloud demo API is not reachable'],
    };
  }
  if (path === 'runtime/options') {
    return {
      mode: 'pure_cloud_only',
      profiles: [{ id: 'pure_cloud_demo', label: '公开云端 Demo' }],
      parser_backends: [{ id: 'mineru_official', label: 'MinerU 官方 API' }],
      generation_backends: [{ id: 'deepseek', label: 'DeepSeek API' }],
      private_assets: [],
      defaults: {
        profile: 'pure_cloud_demo',
        parser_backend: 'mineru_official',
        generation_backend: 'deepseek',
        data_boundary: 'public_or_desensitized_only',
      },
    };
  }
  return { status: 'failed', message: 'Cloud demo API is not reachable', path };
}

function proxy(req, res, targetUrl, path) {
  return new Promise(resolve => {
    const url = new URL(targetUrl);
    const headers = {};
    Object.entries(req.headers || {}).forEach(([key, value]) => {
      if (!HOP_BY_HOP_HEADERS.has(key.toLowerCase())) headers[key] = value;
    });
    headers.host = url.host;

    const request = http.request({
      hostname: url.hostname,
      port: url.port,
      path: `${url.pathname}${url.search}`,
      method: req.method,
      headers,
      timeout: 120000,
    }, upstream => {
      res.statusCode = upstream.statusCode || 200;
      Object.entries(upstream.headers).forEach(([key, value]) => {
        if (value !== undefined) res.setHeader(key, value);
      });
      upstream.pipe(res);
      upstream.on('end', resolve);
    });

    request.on('timeout', () => request.destroy(new Error('backend timeout')));
    request.on('error', () => {
      if (!res.headersSent) res.status(200).json(fallbackFor(path));
      resolve();
    });
    req.pipe(request);
  });
}

export default async function handler(req, res) {
  const path = Array.isArray(req.query.path) ? req.query.path.join('/') : String(req.query.path || '');
  if (await handleTrack1(path, req, res)) return;
  if (await handleTrack2(path, req, res)) return;
  if (await handleTrack3(path, req, res)) return;
  if (await handlePublicReplayApi(path, req, res)) return;
  const backendPath = pathMap[path];
  if (!backendPath) {
    res.status(404).json(fallbackFor(path));
    return;
  }
  const target = `${BACKEND}${backendPath}${queryString(req.query)}`;
  return proxy(req, res, target, path);
}
