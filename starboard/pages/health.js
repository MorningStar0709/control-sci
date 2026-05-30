import SectionWrapper from '../components/SectionWrapper';
import RuntimeSummary from '../components/workbench/RuntimeSummary';
import StatusPill from '../components/workbench/StatusPill';
import { useRuntime } from '../components/workbench/RuntimeProvider';

const runtimeServiceDefs = [
  { key: 'workbench_api', label: '工作台 API', critical: true, action: '启动 FastAPI 17001' },
  { key: 'mineru_api', label: 'MinerU API', critical: true, action: '检查 CONTROLMIND_MINERU_URL / CONTROLSCI_MINERU_URL 指向的服务是否可访问' },
  { key: 'ollama', label: 'Ollama', critical: false, action: '启动 Ollama 11434，或切换到产物复现模式' },
];

const artifactDefs = [
  { key: 'medical_index', label: '医学索引', critical: true, action: '生成或恢复 FAISS/BM25 索引' },
  { key: 'evidence_bundle', label: '证据来源包', critical: false, action: '检查 docs/submissions/data_trace_bundle' },
  { key: 'track1_dataset', label: '赛道一数据集', critical: true, action: '检查 benchmark/dataset/core.json' },
];

function StatusCard({ def, health, loading }) {
  const comp = health?.components?.[def.key] || {};
  const ok = Boolean(comp.available);
  const status = loading ? 'running' : ok ? 'done' : def.critical ? 'failed' : 'degraded';
  const label = loading ? '检查中' : ok ? '可用' : def.critical ? '不可用' : '可选未就绪';

  return (
    <div className={`border rounded-lg p-4 ${!loading && def.critical && !ok ? 'border-red-200 bg-red-50' : 'bg-gray-50'}`}>
      <div className="flex items-center justify-between gap-2">
        <span className="text-sm font-medium text-gray-800">{def.label}</span>
        <StatusPill status={status} label={label} />
      </div>
      {comp.url && <div className="text-[11px] text-gray-400 mt-2 font-mono">{comp.url}</div>}
      {comp.path && <div className="text-[11px] text-gray-400 mt-2 font-mono">{comp.path}</div>}
      {comp.detail && <div className="text-[11px] text-gray-500 mt-2">{comp.detail}</div>}
      {def.key === 'medical_index' && (
        <div className="text-[11px] text-gray-500 mt-2">FAISS {comp.faiss ? 'OK' : 'MISS'} · BM25 {comp.bm25 ? 'OK' : 'MISS'} · Vision {comp.vision ? 'OK' : 'MISS'}</div>
      )}
      {def.key === 'ollama' && comp.models?.length > 0 && (
        <div className="flex flex-wrap gap-1 mt-2">
          {comp.models.slice(0, 5).map(m => <span key={m} className="text-[10px] bg-white border px-1 rounded font-mono">{m}</span>)}
        </div>
      )}
      {!loading && !ok && <div className="text-[11px] text-gray-500 mt-3">建议：{def.action}</div>}
    </div>
  );
}

export default function HealthPage({ runtimeConfig }) {
  const { health, refreshHealth } = useRuntime();
  const loading = !health;

  return (
    <SectionWrapper>
      <div className="custom-screen space-y-6">
        <div className="flex items-end justify-between gap-4">
          <div>
            <h1 className="text-gray-800 text-3xl font-semibold sm:text-4xl mb-2">系统依赖</h1>
            <p className="text-gray-500 text-sm">检查工作台运行服务和可复现产物是否就绪。</p>
          </div>
          <button onClick={refreshHealth} className="px-4 py-2 bg-gray-900 text-white rounded text-xs">刷新状态</button>
        </div>

        <RuntimeSummary runtimeConfig={runtimeConfig} />

        <section className="border rounded-lg bg-white p-5">
          <div className="flex items-center gap-3 mb-5">
            <StatusPill status={health?.status || 'running'} label={loading ? '检查中' : health?.status === 'ready' ? '复现就绪' : health?.status === 'offline' ? '服务离线' : '可降级复现'} />
            <span className="text-xs text-gray-500">{loading ? '正在读取运行服务与产物完整性' : `${health?.privacy_mode || runtimeConfig.privacy_policy} · ${health?.profile || runtimeConfig.profile}`}</span>
          </div>

          <div className="space-y-5">
            <div>
              <h2 className="text-sm font-semibold text-gray-800 mb-3">运行服务</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                {runtimeServiceDefs.map(def => <StatusCard key={def.key} def={def} health={health} loading={loading} />)}
              </div>
            </div>

            <div>
              <h2 className="text-sm font-semibold text-gray-800 mb-3">产物完整性</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                {artifactDefs.map(def => <StatusCard key={def.key} def={def} health={health} loading={loading} />)}
              </div>
            </div>
          </div>
        </section>

        {health?.runtime_issues?.length > 0 && (
          <section className="border border-amber-200 bg-amber-50 rounded-lg p-4">
            <h2 className="text-sm font-semibold text-amber-800 mb-2">运行降级原因</h2>
            <ul className="space-y-1">{health.runtime_issues.map((issue, i) => <li key={i} className="text-xs text-amber-700">{issue}</li>)}</ul>
          </section>
        )}

        {health?.artifact_issues?.length > 0 && (
          <section className="border border-slate-200 bg-slate-50 rounded-lg p-4">
            <h2 className="text-sm font-semibold text-slate-800 mb-2">产物完整性提醒</h2>
            <ul className="space-y-1">{health.artifact_issues.map((issue, i) => <li key={i} className="text-xs text-slate-600">{issue}</li>)}</ul>
          </section>
        )}

        <section className="border rounded-lg p-4 bg-gray-50 text-xs text-gray-600">
          <strong>复现判断：</strong>{' '}
          {health?.status === 'ready'
            ? '运行服务可用；产物完整性请以上方来源包检查为准。'
            : health?.status === 'offline'
              ? '后端服务未连通，需先启动工作台 API。'
              : '部分运行服务不可用，但可通过已验证产物复现关键结果。'}
        </section>
      </div>
    </SectionWrapper>
  );
}
