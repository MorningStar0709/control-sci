import { useRuntime } from './RuntimeProvider';
import StatusPill from './StatusPill';
import ControlMindLogo from './ControlMindLogo';

const serviceDefs = [
  { key: 'mineru_api', label: 'MinerU', critical: true },
  { key: 'ollama', label: 'Ollama', critical: false },
];

const profileDefs = [
  { id: 'demo_replay', label: '产物复现', short: '复现' },
  { id: 'local_private', label: '本地私有', short: '本地' },
  { id: 'hybrid_judge', label: '混合裁判', short: '混合' },
  { id: 'cloud_fast', label: '云端执行', short: '云端' },
];

export default function TopStatusBar({ profile, onProfileChange, onOpenSettings }) {
  const { health, refreshHealth } = useRuntime();

  const statusColor = (ok, critical) => ok ? 'bg-green-500' : critical ? 'bg-red-400' : 'bg-amber-400';

  return (
    <div className="h-12 border-b bg-white flex items-center text-xs overflow-hidden">
      <span className="w-52 flex-shrink-0 h-full px-4 border-r flex items-center gap-2 text-gray-900 whitespace-nowrap">
        <ControlMindLogo size="sm" />
        <span className="leading-tight">
          <span className="block text-[15px] font-semibold tracking-tight">ControlMind</span>
          <span className="block text-[11px] text-gray-600 font-normal leading-snug">科学复现工作台</span>
        </span>
      </span>

      <div className="min-w-0 flex-1 px-4 flex items-center gap-4 overflow-hidden">
        {health ? (
          <>
          <div className="flex items-center gap-3 overflow-x-auto">
            {serviceDefs.map(s => {
              const ok = health.components?.[s.key]?.available;
              return (
                <span
                  key={s.key}
                  className="flex items-center gap-1.5 whitespace-nowrap"
                  title={!ok && !s.critical ? '可选依赖未就绪，工作台可降级运行' : undefined}
                >
                  <span className={`w-1.5 h-1.5 rounded-full ${statusColor(ok, s.critical)}`} />
                  <span className="text-gray-700">{s.label}</span>
                </span>
              );
            })}
          </div>
          <span className="text-gray-300">|</span>
          <StatusPill status={health?.status || 'offline'} label={health?.status === 'ready' ? '就绪' : health?.status === 'offline' ? '离线' : '降级'} />
          </>
        ) : (
          <span className="text-gray-600">检查服务中...</span>
        )}

        <span className="text-gray-300 ml-auto">|</span>

        <div className="flex items-center gap-1">
          {profileDefs.map(p => (
            <button key={p.id} onClick={() => onProfileChange?.(p.id)}
              className={`px-2 py-1 rounded text-xs transition-colors ${
                profile === p.id ? 'bg-sky-600 text-white' : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
              }`} title={p.label}>
              {p.short}
            </button>
          ))}
        </div>

        <button onClick={onOpenSettings}
          className="px-2 py-1 rounded text-gray-600 hover:bg-gray-100 hover:text-gray-900 text-xs transition-colors" title="运行配置">
          设置
        </button>
        <button onClick={refreshHealth}
          className="px-2 py-1 rounded text-gray-600 hover:bg-gray-100 hover:text-gray-900 text-xs transition-colors" title="刷新依赖状态">
          刷新
        </button>
      </div>
    </div>
  );
}
