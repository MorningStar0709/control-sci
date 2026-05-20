import { PROFILE_LABELS, privacyBoundaryText } from '../../lib/runtimeDefaults';

export default function RuntimeSummary({ runtimeConfig, variant = 'default', extraItems = [] }) {
  const isMedical = variant === 'medical';
  const items = isMedical ? [
    ['策略', PROFILE_LABELS[runtimeConfig?.profile] || runtimeConfig?.profile || '-'],
    ['RAG 展示', 'trace 回放'],
    ['合成方式', '已验证回答'],
    ['检索索引', displayRetrievalIndex(runtimeConfig?.retrieval_index)],
    ['安全边界', '诊疗拒答'],
    ...extraItems,
  ] : [
    ['策略', PROFILE_LABELS[runtimeConfig?.profile] || runtimeConfig?.profile || '-'],
    ['云端 API', displayProvider(runtimeConfig?.api_provider)],
    ['模型入口', '服务端代理/回放'],
    ['解析', displayParser(runtimeConfig?.parser_backend)],
    ['赛道三合成', displayProvider(runtimeConfig?.t3_synthesis)],
    ...extraItems,
  ];

  return (
    <div className="border rounded-lg bg-gray-50 p-3">
      <div className="grid grid-cols-2 md:grid-cols-5 gap-2 text-xs">
        {items.map(([k, v]) => (
          <div key={k}>
            <div className="text-[11px] text-gray-600 font-mono leading-snug">{k}</div>
            <div className="text-gray-800 truncate leading-snug">{v}</div>
          </div>
        ))}
      </div>
      <div className="mt-2 text-[11px] text-gray-600 leading-relaxed">
        {isMedical ? '云端医学页只展示已验证 trace 与安全边界，不暴露私有原文、chunk、索引或模型入口。' : privacyBoundaryText(runtimeConfig)}
      </div>
    </div>
  );
}

function displayRetrievalIndex(indexId) {
  if (indexId === 'bge_m3') return 'BGE M3';
  if (indexId === 'bge_small') return 'BGE Small';
  if (indexId === 'qwen') return '高维索引';
  return indexId || 'BGE M3';
}

function displayProvider(provider) {
  if (provider === 'deepseek') return 'DeepSeek';
  if (provider === 'replay') return '回放';
  return provider || '未启用';
}

function displayParser(parser) {
  if (parser === 'mineru_official') return 'MinerU 官方 API';
  if (parser === 'replay') return '回放';
  return parser || '回放';
}
