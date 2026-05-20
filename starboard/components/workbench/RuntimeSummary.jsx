import { PROFILE_LABELS, privacyBoundaryText } from '../../lib/runtimeDefaults';

export default function RuntimeSummary({ runtimeConfig, variant = 'default', extraItems = [] }) {
  const isMedical = variant === 'medical';
  const items = isMedical ? [
    ['策略', PROFILE_LABELS[runtimeConfig?.profile] || runtimeConfig?.profile || '-'],
    ['RAG 后端', '本地私有'],
    ['本地模型', runtimeConfig?.local_model || '未选择'],
    ['检索索引', displayRetrievalIndex(runtimeConfig?.retrieval_index)],
    ['来源合成', runtimeConfig?.t3_synthesis || runtimeConfig?.local_model || '本地模型'],
    ...extraItems,
  ] : [
    ['策略', PROFILE_LABELS[runtimeConfig?.profile] || runtimeConfig?.profile || '-'],
    ['云端 API', runtimeConfig?.api_provider || '未启用'],
    ['本地模型', runtimeConfig?.local_model || '未选择'],
    ['解析', runtimeConfig?.parser_backend || 'replay'],
    ['T3 合成', runtimeConfig?.t3_synthesis || 'replay'],
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
        {isMedical ? '医学 RAG 的检索上下文、chunk、索引与合成均在后端私有环境内完成，不依赖云端 API。' : privacyBoundaryText(runtimeConfig)}
      </div>
    </div>
  );
}

function displayRetrievalIndex(indexId) {
  if (indexId === 'bge_m3') return 'BGE M3';
  if (indexId === 'bge_small') return 'BGE Small';
  if (indexId === 'qwen') return 'Qwen3';
  return indexId || 'BGE M3';
}
