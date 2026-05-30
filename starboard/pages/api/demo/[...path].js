import http from 'http';

export const config = {
  api: {
    bodyParser: false,
  },
};

const BACKEND = process.env.CONTROLMIND_BACKEND_URL || 'http://127.0.0.1:17001';
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
const PROXY_HEADER_ALLOWLIST = new Set(['accept', 'content-type', 'x-request-id', 'x-runtime-profile']);

function proxyHeaders(reqHeaders, targetHost) {
  const headers = {};
  Object.entries(reqHeaders || {}).forEach(([key, value]) => {
    const lower = key.toLowerCase();
    if (!HOP_BY_HOP_HEADERS.has(lower) && PROXY_HEADER_ALLOWLIST.has(lower)) headers[key] = value;
  });
  headers.host = targetHost;
  return headers;
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

function offlineHealth() {
  return {
    status: 'offline',
    profile: 'demo_replay',
    privacy_mode: 'local_only',
    components: {
      workbench_api: { available: false, url: 'http://localhost:17001', detail: 'FastAPI 17001 未连通' },
      mineru_api: { available: false, url: 'http://localhost:8000', detail: 'MinerU API 状态未知' },
      ollama: { available: false, models: [] },
      medical_index: { available: false, faiss: false, bm25: false, vision: false },
      evidence_bundle: { available: false, path: 'docs/submissions/data_trace_bundle' },
      track1_dataset: { available: false, path: 'benchmark/dataset/core.json' },
    },
    runtime_issues: ['工作台 API 未连通：请使用通过终端验证的 Python 环境启动 controlsci/api/medical_rag.py --port 17001'],
    artifact_issues: [],
    issues: ['工作台 API 未连通：请使用通过终端验证的 Python 环境启动 controlsci/api/medical_rag.py --port 17001'],
  };
}

function offlineRuntimeOptions() {
  return {
    profiles: [
      { id: 'demo_replay', label: '产物复现', desc: '使用已验证产物快速复现' },
      { id: 'local_private', label: 'Local Private', desc: '敏感原文和衍生产物留本地' },
      { id: 'hybrid_judge', label: 'Hybrid Judge', desc: '本地解析/检索，脱敏裁判上云' },
      { id: 'cloud_fast', label: 'Cloud Fallback', desc: '公开文档显式上云兜底' },
    ],
    api_providers: [
      { id: 'deepseek', label: 'DeepSeek', available: false, reason: '后端未连通' },
      { id: 'openai', label: 'OpenAI', available: false, reason: '后端未连通' },
      { id: 'minimax', label: 'MiniMax', available: false, reason: '后端未连通' },
      { id: 'mimo', label: 'MiMo Vision', available: false, reason: '后端未连通' },
      { id: 'qwen', label: 'Qwen / DashScope', available: false, reason: '后端未连通' },
      { id: 'kimi', label: 'Kimi / Moonshot', available: false, reason: '后端未连通' },
      { id: 'zhipu', label: '智谱 GLM', available: false, reason: '后端未连通' },
      { id: 'siliconflow', label: 'SiliconFlow', available: false, reason: '后端未连通' },
      { id: 'volcengine', label: '火山方舟', available: false, reason: '后端未连通' },
      { id: 'openrouter', label: 'OpenRouter', available: false, reason: '后端未连通' },
      { id: 'anthropic', label: 'Anthropic Claude', available: false, reason: '后端未连通' },
    ],
    local_models: [
      { id: 'qwen3.5:9b', label: 'qwen3.5:9b', available: false, reason: '后端未连通' },
      { id: 'qwen3-embedding:4b', label: 'qwen3-embedding:4b', available: false, reason: '后端未连通' },
    ],
    parser_backends: [
      { id: 'replay', label: 'Replay', available: true },
      { id: 'local', label: 'MinerU API', available: false, reason: '后端未连通' },
      { id: 'official', label: 'MinerU 官方 API', available: false, reason: '后端未连通' },
      { id: 'auto', label: '自动选择', available: true, note: '本地优先；云端只作为公开文档兜底' },
    ],
    privacy_policies: [
      { id: 'local_only', label: 'local-only', desc: '原文和中间产物不离开本地' },
      { id: 'desensitized_cloud', label: 'desensitized-cloud-allowed', desc: '公开/脱敏任务可上云' },
    ],
    data_classes: [
      { id: 'public_open', label: '公开开放', cloud_upload_allowed: true, desc: '论文、公开报告、公开网页等' },
      { id: 'public_but_regulated', label: '公开但受规制', cloud_upload_allowed: true, desc: '公开医学、金融、合规资料，需显式放行' },
      { id: 'private_enterprise', label: '企业私有', cloud_upload_allowed: false, desc: '制造、控制、航天、军工等内部文档' },
      { id: 'private_medical', label: '医疗私有', cloud_upload_allowed: false, desc: '病例、处方、院内资料或患者相关材料' },
      { id: 'confidential_defense', label: '保密/防务', cloud_upload_allowed: false, desc: '涉密或高度敏感资料' },
      { id: 'derived_sensitive', label: '派生敏感', cloud_upload_allowed: false, desc: 'chunk、索引、微调样本、评测私有衍生产物' },
    ],
    defaults: {
      profile: 'demo_replay',
      api_provider: '',
      local_model: 'qwen3.5:9b',
      t3_synthesis: 'qwen3.5:9b',
      retrieval_index: 'bge_m3',
      parser_backend: 'replay',
      privacy_policy: 'local_only',
      data_class: 'private_enterprise',
      allow_cloud_upload: false,
    },
  };
}

function fallbackTrack2Templates() {
  return {
    templates: [
      { id: 'flywheel', label: '查看数据飞轮来源', goal: '追溯 Quick Proof：arXiv PDF → MinerU Markdown → ABCD 快速题集 → 已保存评测结果' },
      { id: 'eval40', label: '查看 Track1 抽样来源', goal: '追溯 core.json、四维抽样计划、leaderboard 与已验证评测产物' },
      { id: 'check_index', label: '查看 Medical RAG 索引', goal: '追溯 FAISS + BM25 + chunk manifest 的存在性和来源路径' },
      { id: 'evidence_bundle', label: '查看证据包来源', goal: '追溯 data_trace_bundle、manifest 和 DATA-TRACE 来源文件' },
      { id: 'visual_audit', label: '查看视觉审计产物', goal: '追溯 visual_audit_results.jsonl 与跨模态审计来源' },
    ],
    mode: 'offline_fallback',
  };
}

function fallbackCapabilities() {
  return {
    meta: {
      project: 'ControlMind Data Agent',
      total_intents: 15,
      description: '后端离线时的能力注册表摘要',
    },
    intents: [
      { intent_id: 'arxiv_search', name: 'arXiv 论文检索', resource_type: 'script' },
      { intent_id: 'mineru_parse', name: '文档解析', resource_type: 'local_api' },
      { intent_id: 'corpus_parse', name: '语料解析', resource_type: 'local_api' },
      { intent_id: 'cross_modal_audit', name: '跨模态对齐审计', resource_type: 'api' },
      { intent_id: 'benchmark_build', name: '评测数据集构建', resource_type: 'api' },
      { intent_id: 'quality_arbitrate', name: '质量仲裁', resource_type: 'api' },
      { intent_id: 'model_evaluate', name: '模型评测', resource_type: 'api' },
      { intent_id: 'leaderboard_viz', name: '排行榜可视化', resource_type: 'script' },
      { intent_id: 'local_finetune', name: '本地微调', resource_type: 'local_gpu' },
      { intent_id: 'multi_format_parse', name: '多格式文档解析', resource_type: 'local_api' },
      { intent_id: 'medical_rag', name: '医学文献自动化合成', resource_type: 'local_gpu' },
      { intent_id: 'sciverse_search', name: 'Sciverse 文献检索', resource_type: 'api' },
      { intent_id: 'reproduce_all', name: '全量复现', resource_type: 'script' },
    ],
    resource_scheduler_config: {
      resource_types: {
        api: {},
        local_api: {},
        local_gpu: {},
        script: {},
      },
    },
  };
}

function fallbackFor(path) {
  if (path === 'health') return offlineHealth();
  if (path === 'runtime/options') return offlineRuntimeOptions();
  if (path === 'track2/templates') return fallbackTrack2Templates();
  if (path === 'capabilities') return fallbackCapabilities();
  if (path === 'runtime/resolve') {
    return {
      selected: offlineRuntimeOptions().defaults,
      disabled: [{ option: 'backend', reason: 'FastAPI 17001 未连通', fallback: '产物复现' }],
      privacy_enforcement: { original: 'local_only', enforced: 'local_only', reason: '后端离线时强制本地/回放' },
    };
  }
  return {
    status: 'failed',
    message: '工作台 API 未连通',
    fallback_available: true,
    path,
  };
}

function proxy(req, res, targetUrl, path) {
  return new Promise(resolve => {
    const url = new URL(targetUrl);
    const headers = proxyHeaders(req.headers, url.host);

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

    request.on('timeout', () => {
      request.destroy(new Error('backend timeout'));
    });

    request.on('error', () => {
      if (!res.headersSent) res.status(200).json(fallbackFor(path));
      resolve();
    });

    req.pipe(request);
  });
}

export default function handler(req, res) {
  const path = Array.isArray(req.query.path) ? req.query.path.join('/') : String(req.query.path || '');
  const target = `${BACKEND}/api/demo/${path}${queryString(req.query)}`;
  return proxy(req, res, target, path);
}
