import { useEffect, useMemo, useState } from 'react';
import { apiGet, apiPost } from '../../lib/apiClient';
import { applyProfilePreset } from '../../lib/runtimeDefaults';

export default function SettingsDrawer({ open, onClose, runtimeConfig, onConfigChange }) {
  const [options, setOptions] = useState(null);
  const [draft, setDraft] = useState(runtimeConfig);
  const [resolving, setResolving] = useState(false);
  const [resolveResult, setResolveResult] = useState(null);
  const apiModelOptions = useMemo(() => (options?.api_providers || []).filter(p => p.available), [options]);

  useEffect(() => {
    if (open) {
      setDraft(runtimeConfig);
      setResolveResult(null);
      apiGet('/api/demo/runtime/options').then(r => r.ok && setOptions(r.data));
    }
  }, [open, runtimeConfig]);

  function update(key, value) {
    setDraft(prev => ({ ...prev, [key]: value }));
    setResolveResult(null);
  }

  function applyDraft() {
    onConfigChange?.(draft);
  }

  async function resolveDraft() {
    setResolving(true);
    const r = await apiPost('/api/demo/runtime/resolve', draft);
    setResolveResult(r.ok ? r.data : { error: r.error });
    setResolving(false);
  }

  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex">
      <div className="absolute inset-0 bg-black/20" onClick={onClose} />
      <div className="relative ml-auto w-80 bg-white border-l shadow-2xl h-full overflow-y-auto">
        <div className="sticky top-0 bg-white border-b px-5 py-3 flex items-center justify-between">
          <span className="font-semibold text-gray-800 text-sm">运行配置</span>
          <button onClick={onClose} className="text-gray-400 hover:text-gray-600 text-lg">✕</button>
        </div>

        <div className="p-5 space-y-5">
          {/* Execution Profile */}
          <div>
            <label className="text-[11px] text-gray-400 font-mono mb-1 block">执行策略</label>
            <div className="mb-2 text-[10px] leading-relaxed text-gray-500">
              默认本地，云端兜底，非必要不上云。文档上传云端必须同时满足公开分级与显式授权。
            </div>
            <div className="grid grid-cols-2 gap-1">
              {(options?.profiles || []).map(p => (
                <button key={p.id} onClick={() => { setDraft(applyProfilePreset(draft, p.id)); setResolveResult(null); }}
                  className={`text-xs px-2 py-1.5 rounded border text-left ${
                    draft.profile === p.id ? 'bg-sky-500 text-white border-sky-500' : 'text-gray-600 hover:bg-gray-50'
                  }`} title={p.desc}>
                  <div className="font-medium">{p.label}</div>
                  <div className="text-[10px] opacity-70 truncate">{p.desc}</div>
                </button>
              ))}
            </div>
          </div>

          {/* API Provider */}
          <div>
            <label className="text-[11px] text-gray-400 font-mono mb-1 block">API 厂商</label>
            <select value={draft.api_provider || ''}
              onChange={e => update('api_provider', e.target.value)}
              className="w-full border rounded px-3 py-1.5 text-xs">
              <option value="">不使用云端 API</option>
              {(options?.api_providers || []).map(a => (
                <option key={a.id} value={a.id} disabled={!a.available}>{a.label}{!a.available ? ` (${a.reason || '未配置'})` : ''}</option>
              ))}
            </select>
            <div className="mt-1 text-[10px] text-gray-400">云端模型只作为公开/脱敏任务的增强路径；本地与回放仍是默认路径。</div>
          </div>

          {/* Local Model */}
          <div>
            <label className="text-[11px] text-gray-400 font-mono mb-1 block">本地模型 (Ollama)</label>
            <select value={draft.local_model || ''}
              onChange={e => update('local_model', e.target.value)}
              className="w-full border rounded px-3 py-1.5 text-xs">
              <option value="">— 选择模型 —</option>
              {(options?.local_models || []).map(m => (
                <option key={m.id} value={m.id} disabled={!m.available}>{m.label}{!m.available ? ' (未找到)' : ''}</option>
              ))}
            </select>
          </div>

          {/* Parser Backend */}
          <div>
            <label className="text-[11px] text-gray-400 font-mono mb-1 block">解析后端</label>
            <div className="space-y-1">
              {(options?.parser_backends || []).map(b => (
                <button key={b.id}
                  onClick={() => b.available && update('parser_backend', b.id)}
                  disabled={!b.available}
                  className={`w-full text-left text-xs px-2 py-1.5 rounded border ${
                    draft.parser_backend === b.id ? 'bg-sky-500 text-white border-sky-500' :
                    b.available ? 'text-gray-600 hover:bg-gray-50' : 'text-gray-300 bg-gray-50'
                  }`}>
                  <div className="font-medium">{b.label} {!b.available && <span className="text-[10px] opacity-70">({b.reason})</span>}</div>
                  {b.note && <div className="text-[10px] opacity-70 mt-0.5">{b.note}</div>}
                </button>
              ))}
            </div>
          </div>

          {/* Data Classification */}
          <div>
            <label className="text-[11px] text-gray-400 font-mono mb-1 block">数据分级</label>
            <div className="mb-2 text-[10px] leading-relaxed text-gray-500">
              分级不做自动判密，只作为云端兜底的放行条件；未确认公开时请保持默认私有。
            </div>
            <select value={draft.data_class || 'private_enterprise'}
              onChange={e => {
                const next = e.target.value;
                setDraft(prev => ({
                  ...prev,
                  data_class: next,
                  allow_cloud_upload: ['public_open', 'public_but_regulated'].includes(next) ? prev.allow_cloud_upload : false,
                }));
                setResolveResult(null);
              }}
              className="w-full border rounded px-3 py-1.5 text-xs">
              {(options?.data_classes || []).map(c => (
                <option key={c.id} value={c.id}>{c.label} - {c.desc}</option>
              ))}
            </select>
            <label className={`mt-2 flex items-start gap-2 rounded border px-2 py-2 text-xs ${
              ['public_open', 'public_but_regulated'].includes(draft.data_class)
                ? 'text-gray-700 bg-white'
                : 'text-gray-400 bg-gray-50'
            }`}>
              <input
                type="checkbox"
                className="mt-0.5"
                checked={Boolean(draft.allow_cloud_upload)}
                disabled={!['public_open', 'public_but_regulated'].includes(draft.data_class)}
                onChange={e => update('allow_cloud_upload', e.target.checked)}
              />
              <span>
                允许公开文档在必要时使用官方 MinerU API 兜底
                <span className="block text-[10px] text-gray-400 mt-0.5">默认不勾选；未授权时 official/auto 会回退到本地或回放。</span>
              </span>
            </label>
          </div>

          {/* Privacy Policy */}
          <div>
            <label className="text-[11px] text-gray-400 font-mono mb-1 block">隐私策略</label>
            <div className="space-y-1">
              {(options?.privacy_policies || []).map(p => (
                <button key={p.id}
                  onClick={() => update('privacy_policy', p.id)}
                  className={`w-full text-left text-xs px-2 py-1.5 rounded border ${
                    draft.privacy_policy === p.id ? 'bg-sky-500 text-white border-sky-500' : 'text-gray-600 hover:bg-gray-50'
                  }`}>
                  <div className="font-medium">{p.label}</div>
                  <div className="text-[10px] opacity-70">{p.desc}</div>
                </button>
              ))}
            </div>
          </div>

          {/* Advanced: Per-track overrides */}
          <details>
            <summary className="text-[11px] text-gray-400 font-mono cursor-pointer">高级：赛道覆盖配置</summary>
            <div className="mt-2 space-y-3 pl-2 border-l-2 border-gray-100">
              <div>
                <label className="text-[10px] text-gray-400 block">赛道一 答题模型</label>
                <select value={draft.t1_answer_model || 'replay'}
                  onChange={e => update('t1_answer_model', e.target.value)}
                  className="w-full border rounded px-2 py-1 text-[10px]">
                  <option value="replay">回放</option>
                  {(options?.local_models || []).filter(m => m.available && !m.id.includes('embedding')).map(m => (
                    <option key={m.id} value={m.id}>{m.label}</option>
                  ))}
                  {apiModelOptions.map(a => <option key={a.id} value={a.id}>{a.label} API</option>)}
                </select>
              </div>
              <div>
                <label className="text-[10px] text-gray-400 block">赛道一 裁判模型</label>
                <select value={draft.t1_judge_model || 'replay'}
                  onChange={e => update('t1_judge_model', e.target.value)}
                  className="w-full border rounded px-2 py-1 text-[10px]">
                  <option value="replay">回放</option>
                  {apiModelOptions.map(a => <option key={a.id} value={a.id}>{a.label} API</option>)}
                  {(options?.local_models || []).filter(m => m.available && !m.id.includes('embedding')).map(m => (
                    <option key={m.id} value={m.id}>{m.label}</option>
                  ))}
                </select>
              </div>
              <div>
                <label className="text-[10px] text-gray-400 block">赛道二 计划模型</label>
                <select value={draft.t2_planner || 'deepseek'}
                  onChange={e => update('t2_planner', e.target.value)}
                  className="w-full border rounded px-2 py-1 text-[10px]">
                  <option value="replay">回放 / dry-run</option>
                  {apiModelOptions.map(a => <option key={a.id} value={a.id}>{a.label} API</option>)}
                  {(options?.local_models || []).filter(m => m.available && !m.id.includes('embedding')).map(m => (
                    <option key={m.id} value={m.id}>{m.label}</option>
                  ))}
                </select>
              </div>
              <div>
                <label className="text-[10px] text-gray-400 block">赛道三 合成模型</label>
                <select value={draft.t3_synthesis || 'replay'}
                  onChange={e => update('t3_synthesis', e.target.value)}
                  className="w-full border rounded px-2 py-1 text-[10px]">
                  <option value="replay">回放</option>
                  {(options?.local_models || []).filter(m => m.available && !m.id.includes('embedding')).map(m => (
                    <option key={m.id} value={m.id}>{m.label} 本地</option>
                  ))}
                  {apiModelOptions.map(a => <option key={a.id} value={a.id}>{a.label} API</option>)}
                </select>
              </div>
            </div>
          </details>

          {/* Presets */}
          <div className="pt-2 border-t">
            <label className="text-[11px] text-gray-400 font-mono mb-1 block">快速预设</label>
            <div className="flex gap-1">
              {[
                { idx: 'demo_replay', label: '回放' },
                { idx: 'local_private', label: '本地' },
                { idx: 'hybrid_judge', label: '混合' },
                { idx: 'cloud_fast', label: '云端' },
              ].map(p => (
                <button key={p.idx}
                  onClick={() => {
                    setDraft(applyProfilePreset(draft, p.idx));
                    setResolveResult(null);
                  }}
                  className={`px-2 py-1 text-[10px] rounded border hover:bg-gray-50 ${
                    draft.profile === p.idx ? 'bg-sky-500 text-white border-sky-500' : 'text-gray-500'
                  }`}>{p.label}</button>
              ))}
            </div>
          </div>

          {/* Resolve result */}
          <div className="pt-2 border-t">
            <div className="grid grid-cols-2 gap-2">
              <button onClick={resolveDraft} disabled={resolving} className="px-3 py-1.5 border text-gray-700 text-xs rounded hover:bg-gray-50 disabled:opacity-50">
                {resolving ? '校验中' : '校验配置'}
              </button>
              <button onClick={applyDraft} className="px-3 py-1.5 bg-gray-800 text-white text-xs rounded hover:bg-gray-700">
                应用配置
              </button>
            </div>
            {resolveResult && (
              <div className="mt-3 border rounded-lg bg-gray-50 p-3 text-[11px] text-gray-600 space-y-2">
                {resolveResult.error ? (
                  <div className="text-red-600">{resolveResult.error}</div>
                ) : (
                  <>
                    <div className="font-semibold text-gray-800">配置校验结果</div>
                    {(resolveResult.checks || []).map(item => (
                      <div key={item.name} className="flex items-center justify-between gap-2">
                        <span>{item.name}</span>
                        <span className="font-mono text-gray-700">{item.selected}</span>
                      </div>
                    ))}
                    {resolveResult.disabled?.length > 0 && (
                      <div className="space-y-1">
                        {resolveResult.disabled.map((item, index) => (
                          <div key={index} className="text-amber-700">{item.option}：{item.reason}，回退到 {item.fallback}</div>
                        ))}
                      </div>
                    )}
                    <div className="text-gray-500">{resolveResult.privacy_enforcement?.reason}</div>
                  </>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
