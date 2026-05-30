export const DEFAULT_RUNTIME_CONFIG = {
  profile: 'pure_cloud_demo',
  api_provider: 'deepseek',
  parser_backend: 'mineru_official',
  privacy_policy: 'public_desensitized_cloud',
  data_class: 'public_open',
  allow_cloud_upload: true,
  t1_answer_model: 'deepseek',
  t1_judge_model: 'deepseek',
  t2_planner: 'deepseek',
  t3_synthesis: 'deepseek',
  retrieval_index: 'public_demo',
};

export const PROFILE_PRESETS = {
  pure_cloud_demo: DEFAULT_RUNTIME_CONFIG,
};

export const PROFILE_LABELS = {
  pure_cloud_demo: '在线展示版',
};

export function privacyBoundaryText() {
  return '在线展示版只处理公开或脱敏材料；私有原文、chunk、向量索引和批量实验不进入云端。';
}

export function mergeRuntimeDefaults(options, current) {
  const defaults = options?.defaults || {};
  return {
    ...DEFAULT_RUNTIME_CONFIG,
    ...(current || {}),
    ...defaults,
    profile: 'pure_cloud_demo',
    parser_backend: 'mineru_official',
    api_provider: 'deepseek',
    privacy_policy: 'public_desensitized_cloud',
    allow_cloud_upload: true,
    t3_synthesis: 'deepseek',
    retrieval_index: 'public_demo',
  };
}
