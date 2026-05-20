export default function StatusPill({ status = 'pending', label }) {
  const styles = {
    ready: 'bg-green-100 text-green-700',
    ok: 'bg-green-100 text-green-700',
    done: 'bg-green-100 text-green-700',
    safety_refusal: 'bg-amber-100 text-amber-700',
    replay: 'bg-amber-100 text-amber-700',
    degraded: 'bg-amber-100 text-amber-700',
    planned: 'bg-sky-100 text-sky-700',
    validated: 'bg-emerald-100 text-emerald-700',
    live_execute: 'bg-emerald-100 text-emerald-700',
    live_check: 'bg-blue-100 text-blue-700',
    artifact_reuse: 'bg-amber-100 text-amber-700',
    running: 'bg-sky-100 text-sky-700',
    failed: 'bg-red-100 text-red-700',
    offline: 'bg-red-100 text-red-700',
    pending: 'bg-gray-100 text-gray-600',
  };
  const text = label || {
    ready: '就绪',
    ok: '完成',
    done: '完成',
    safety_refusal: '安全边界',
    replay: '复现',
    degraded: '降级',
    planned: '规划',
    validated: '已验证',
    live_execute: '专项回放',
    live_check: '来源检查',
    artifact_reuse: '产物复用',
    running: '处理中',
    failed: '失败',
    offline: '离线',
    pending: '待执行',
  }[status] || status;

  return <span className={`text-[11px] px-2 py-0.5 rounded font-medium ${styles[status] || styles.pending}`}>{text}</span>;
}
