export default function WorkbenchLoadingCard({
  title = '正在处理',
  desc = '任务已提交，正在等待后端返回结果。',
  steps = [],
  className = '',
}) {
  const visibleSteps = steps.length ? steps : ['提交任务', '等待结果', '更新页面'];

  return (
    <div className={`rounded-lg border bg-white p-4 shadow-sm ${className}`}>
      <div className="flex items-center gap-3">
        <div className="relative h-8 w-8 flex-shrink-0">
          <div className="absolute inset-0 rounded-full border-2 border-gray-200" />
          <div className="absolute inset-0 animate-spin rounded-full border-2 border-gray-900 border-r-transparent border-t-transparent" />
        </div>
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2 text-sm font-semibold text-gray-800">
            {title}
            <span className="inline-flex gap-1">
              <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-gray-500 [animation-delay:-0.2s]" />
              <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-gray-500 [animation-delay:-0.1s]" />
              <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-gray-500" />
            </span>
          </div>
          {desc && <div className="mt-1 text-xs leading-relaxed text-gray-500">{desc}</div>}
        </div>
      </div>
      <div className="mt-4 grid grid-cols-1 gap-2 sm:grid-cols-3">
        {visibleSteps.map((step, index) => (
          <div key={step} className="rounded border bg-gray-50 px-2.5 py-2">
            <div className="flex items-center gap-2">
              <span className={`h-2 w-2 rounded-full animate-pulse ${index === 0 ? 'bg-gray-900' : index === 1 ? 'bg-gray-500 [animation-delay:0.25s]' : 'bg-gray-400 [animation-delay:0.5s]'}`} />
              <span className="text-[11px] font-medium text-gray-700">{step}</span>
            </div>
          </div>
        ))}
      </div>
      <div className="mt-3 h-1.5 overflow-hidden rounded-full bg-gray-100">
        <div className="h-full w-1/2 animate-[pulse_1.2s_ease-in-out_infinite] rounded-full bg-gray-900" />
      </div>
    </div>
  );
}
