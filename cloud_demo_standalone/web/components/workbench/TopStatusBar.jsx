import { useEffect, useState } from 'react';
import { useRuntime } from './RuntimeProvider';
import { getDemoAccessCode, setDemoAccessCode } from '../../lib/apiClient';
import StatusPill from './StatusPill';
import ControlMindLogo from './ControlMindLogo';

const serviceDefs = [
  { key: 'mineru_official_api', label: 'MinerU', critical: true },
  { key: 'deepseek_api', label: 'DeepSeek', critical: true },
];

export default function TopStatusBar() {
  const { health, refreshHealth } = useRuntime();
  const [accessCode, setAccessCode] = useState('');
  const [hasAccessCode, setHasAccessCode] = useState(false);
  const quota = health?.components?.quota || health?.quota;
  const ready = health?.status === 'ready';
  const statusColor = (ok) => ok ? 'bg-emerald-500' : 'bg-amber-400';
  const quotaText = quota ? `${quota.remaining}/${quota.limit}` : '-/-';
  const replayMode = health && !ready;
  const backendDisconnected = Array.isArray(health?.issues) && health.issues.some(issue => String(issue).includes('API is not reachable'));

  useEffect(() => {
    const saved = getDemoAccessCode();
    setAccessCode(saved);
    setHasAccessCode(Boolean(saved));
  }, []);

  function saveAccessCode() {
    const saved = setDemoAccessCode(accessCode);
    setAccessCode(saved);
    setHasAccessCode(Boolean(saved));
  }

  function clearAccessCode() {
    setDemoAccessCode('');
    setAccessCode('');
    setHasAccessCode(false);
  }

  return (
    <div className="h-12 border-b bg-white flex items-center text-xs overflow-hidden">
      <span className="w-52 flex-shrink-0 h-full px-4 border-r flex items-center gap-2 text-gray-900 whitespace-nowrap">
        <ControlMindLogo size="sm" />
        <span className="leading-tight">
          <span className="block text-[15px] font-semibold tracking-tight">ControlMind</span>
          <span className="block text-[11px] text-gray-600 font-normal leading-snug">成果展示台</span>
        </span>
      </span>

      <div className="min-w-0 flex-1 px-4 flex items-center gap-3 overflow-hidden">
        {health ? (
          <>
            <div className="flex items-center gap-2 whitespace-nowrap">
              <StatusPill status={ready ? 'ready' : 'replay'} label={ready ? '在线展示就绪' : backendDisconnected ? '后端未连接' : '回放模式'} />
              <span className="hidden lg:inline text-gray-500">公开/脱敏材料 · 服务端密钥</span>
            </div>

            <span className="hidden md:inline text-gray-300">|</span>

            <div className="flex items-center gap-2 overflow-x-auto">
              {serviceDefs.map(s => {
                const ok = health.components?.[s.key]?.available;
                return (
                  <span key={s.key} className="flex items-center gap-1.5 whitespace-nowrap rounded border bg-gray-50 px-2 py-1" title={ok ? `${s.label} 已配置` : `${s.label} 未配置`}>
                    <span className={`w-1.5 h-1.5 rounded-full ${statusColor(ok)}`} />
                    <span className="text-gray-700">{s.label}</span>
                    <span className="hidden sm:inline text-gray-400">{ok ? '已就绪' : backendDisconnected ? '后端' : replayMode ? '回放' : '未配置'}</span>
                  </span>
                );
              })}
            </div>

            <span className="hidden md:inline text-gray-300">|</span>
            <span className="whitespace-nowrap rounded border bg-gray-50 px-2 py-1 text-gray-700">
              今日额度 <span className="font-mono text-gray-900">{quotaText}</span>
            </span>
          </>
        ) : (
          <span className="text-gray-600">检查服务中...</span>
        )}

        <span className="text-gray-300 ml-auto">|</span>
        <div className="hidden lg:flex items-center gap-1 whitespace-nowrap">
          <input
            type="password"
            value={accessCode}
            onChange={event => setAccessCode(event.target.value)}
            onKeyDown={event => {
              if (event.key === 'Enter') saveAccessCode();
            }}
            placeholder="访问码"
            autoComplete="off"
            className="h-7 w-28 rounded border border-gray-300 bg-white px-2 text-xs text-gray-800 outline-none focus:border-sky-500"
            title="访问码，仅保存在当前浏览器"
          />
          <button onClick={saveAccessCode} className={`h-7 px-2 rounded border text-xs ${hasAccessCode ? 'bg-emerald-50 text-emerald-700 border-emerald-200' : 'text-gray-600 hover:bg-gray-100'}`} title="保存到当前浏览器">
            {hasAccessCode ? '已保存' : '保存'}
          </button>
          {hasAccessCode ? (
            <button onClick={clearAccessCode} className="h-7 px-2 rounded border text-xs text-gray-500 hover:bg-gray-100" title="清除当前浏览器访问码">
              清除
            </button>
          ) : null}
        </div>
        <span className="hidden sm:inline rounded bg-gray-900 px-2 py-1 text-white text-xs" title="在线展示模式">在线展示</span>
        <button onClick={refreshHealth} className="px-2 py-1 rounded border text-gray-600 hover:bg-gray-100 hover:text-gray-900 text-xs transition-colors" title="刷新依赖状态">
          刷新
        </button>
      </div>
    </div>
  );
}
