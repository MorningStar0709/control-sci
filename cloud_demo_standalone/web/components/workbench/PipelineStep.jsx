export default function PipelineStep({ step, label, status, note, artifact }) {
  const statusColor = status === 'done' ? 'bg-green-500' : status === 'replay' ? 'bg-yellow-500' : status === 'failed' ? 'bg-red-500' : status === 'ready' ? 'bg-sky-500' : 'bg-gray-300';
  return (
    <div className="flex items-center gap-3 text-sm">
      <span className={`w-6 h-6 rounded-full flex items-center justify-center text-xs text-white ${statusColor}`}>{step}</span>
      <span className="text-gray-700">{label}</span>
      <span className="text-xs text-gray-500">{note || ''}</span>
      {status === 'done' && <span className="text-green-500 text-xs">✓</span>}
      {status === 'replay' && <span className="text-yellow-600 text-xs">复现</span>}
      {status === 'failed' && <span className="text-red-600 text-xs">失败</span>}
      {artifact && <span className="text-[11px] text-gray-500 font-mono truncate">{artifact}</span>}
    </div>
  );
}
