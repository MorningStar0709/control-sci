import StatusPill from './StatusPill';

export default function StepCard({ index, title, desc, status = 'pending', children, actions }) {
  return (
    <section className="border rounded-lg bg-white overflow-hidden">
      <div className="px-5 py-4 border-b bg-gray-50 flex items-start gap-3">
        <span className="w-7 h-7 rounded-full bg-gray-900 text-white flex items-center justify-center text-xs font-bold flex-shrink-0">{index}</span>
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <h2 className="text-sm font-semibold text-gray-800">{title}</h2>
            <StatusPill status={status} />
          </div>
          {desc && <p className="text-xs text-gray-600 mt-1 leading-relaxed">{desc}</p>}
        </div>
        {actions && <div className="flex-shrink-0">{actions}</div>}
      </div>
      <div className="p-5">{children}</div>
    </section>
  );
}
