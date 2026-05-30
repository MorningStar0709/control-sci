export const DEFAULT_RUNTIME_CONFIG = {
  profile: 'demo_replay',
  api_provider: '',
  local_model: 'qwen3.5:9b',
  parser_backend: 'replay',
  privacy_policy: 'local_only',
  data_class: 'private_enterprise',
  allow_cloud_upload: false,
  t1_answer_model: 'replay',
  t1_judge_model: 'replay',
  t2_planner: 'deepseek',
  t3_synthesis: 'qwen3.5:9b',
  retrieval_index: 'bge_m3',
};

export const PROFILE_PRESETS = {
  demo_replay: {
    profile: 'demo_replay',
    api_provider: '',
    parser_backend: 'replay',
    privacy_policy: 'local_only',
    data_class: 'derived_sensitive',
    allow_cloud_upload: false,
    t1_answer_model: 'replay',
    t1_judge_model: 'replay',
    t2_planner: 'replay',
    t3_synthesis: 'qwen3.5:9b',
    retrieval_index: 'bge_m3',
  },
  local_private: {
    profile: 'local_private',
    api_provider: '',
    parser_backend: 'local',
    privacy_policy: 'local_only',
    data_class: 'private_enterprise',
    allow_cloud_upload: false,
    t1_answer_model: 'replay',
    t1_judge_model: 'replay',
    t2_planner: 'local',
    t3_synthesis: 'qwen3.5:9b',
    retrieval_index: 'bge_m3',
  },
  hybrid_judge: {
    profile: 'hybrid_judge',
    api_provider: 'deepseek',
    parser_backend: 'local',
    privacy_policy: 'desensitized_cloud',
    data_class: 'private_enterprise',
    allow_cloud_upload: false,
    t1_answer_model: 'replay',
    t1_judge_model: 'deepseek',
    t2_planner: 'deepseek',
    t3_synthesis: 'qwen3.5:9b',
    retrieval_index: 'bge_m3',
  },
  cloud_fast: {
    profile: 'cloud_fast',
    api_provider: 'deepseek',
    parser_backend: 'auto',
    privacy_policy: 'desensitized_cloud',
    data_class: 'public_open',
    allow_cloud_upload: false,
    t1_answer_model: 'deepseek',
    t1_judge_model: 'deepseek',
    t2_planner: 'deepseek',
    t3_synthesis: 'qwen3.5:9b',
    retrieval_index: 'bge_m3',
  },
};

export const PROFILE_LABELS = {
  demo_replay: '产物复现',
  local_private: '本地私有',
  hybrid_judge: '混合裁判',
  cloud_demo: '公开展示',
  cloud_fast: '云端候选（需授权）',
};

export function mergeRuntimeDefaults(options, current) {
  const defaults = options?.defaults || {};
  const hasCurrent = (key) => current && Object.prototype.hasOwnProperty.call(current, key);
  return {
    ...DEFAULT_RUNTIME_CONFIG,
    ...(current || {}),
    profile: hasCurrent('profile') ? current.profile : (defaults.profile || DEFAULT_RUNTIME_CONFIG.profile),
    api_provider: hasCurrent('api_provider') ? current.api_provider : (defaults.api_provider || DEFAULT_RUNTIME_CONFIG.api_provider),
    local_model: hasCurrent('local_model') ? current.local_model : (defaults.local_model || DEFAULT_RUNTIME_CONFIG.local_model),
    parser_backend: hasCurrent('parser_backend') ? current.parser_backend : (defaults.parser_backend || DEFAULT_RUNTIME_CONFIG.parser_backend),
    privacy_policy: hasCurrent('privacy_policy') ? current.privacy_policy : (defaults.privacy_policy || DEFAULT_RUNTIME_CONFIG.privacy_policy),
    data_class: hasCurrent('data_class') ? current.data_class : (defaults.data_class || DEFAULT_RUNTIME_CONFIG.data_class),
    allow_cloud_upload: hasCurrent('allow_cloud_upload') ? current.allow_cloud_upload : (defaults.allow_cloud_upload ?? DEFAULT_RUNTIME_CONFIG.allow_cloud_upload),
    t3_synthesis: hasCurrent('t3_synthesis') ? current.t3_synthesis : (defaults.t3_synthesis || DEFAULT_RUNTIME_CONFIG.t3_synthesis),
    retrieval_index: hasCurrent('retrieval_index') ? current.retrieval_index : (defaults.retrieval_index || DEFAULT_RUNTIME_CONFIG.retrieval_index),
  };
}

export function applyProfilePreset(current, profile) {
  const preset = PROFILE_PRESETS[profile] || { profile };
  return {
    ...DEFAULT_RUNTIME_CONFIG,
    ...(current || {}),
    ...preset,
    local_model: current?.local_model || DEFAULT_RUNTIME_CONFIG.local_model,
    parser_backend: preset.parser_backend || current?.parser_backend || DEFAULT_RUNTIME_CONFIG.parser_backend,
    data_class: preset.data_class || current?.data_class || DEFAULT_RUNTIME_CONFIG.data_class,
    allow_cloud_upload: preset.allow_cloud_upload ?? current?.allow_cloud_upload ?? DEFAULT_RUNTIME_CONFIG.allow_cloud_upload,
  };
}

export function privacyBoundaryText(config) {
  if (config?.profile === 'cloud_fast') {
    return '默认本地，云端兜底。公开文档只有显式授权后才会使用云端 API，私有/敏感文档仍本地解析。';
  }
  if (config?.profile === 'cloud_demo') {
    return '公开展示入口已开启；原文默认不上云，官方 API 只作为公开资料的显式兜底。';
  }
  if (config?.profile === 'hybrid_judge') {
    return '解析与检索默认本地；云端模型只处理公开/脱敏裁判任务。';
  }
  return '默认本地，非必要不上云；chunk、索引和微调产物保留在本地环境。';
}
