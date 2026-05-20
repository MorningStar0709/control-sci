import { useEffect, useState } from 'react';
import SectionWrapper from '../components/SectionWrapper';
import { MetricGrid, PageHeader, loadCloudState } from '../components/workbench/CloudDemoBlocks';

export default function HealthPage() {
  const [state, setState] = useState({ health: null, runtime: null, tracks: null });
  useEffect(() => {
    loadCloudState().then(setState);
    const syncHealth = event => setState(prev => ({ ...prev, health: event.detail }));
    window.addEventListener('cloud-demo-health', syncHealth);
    return () => window.removeEventListener('cloud-demo-health', syncHealth);
  }, []);
  const health = state.health;
  const quota = health?.components?.quota || {};
  const backendDisconnected = Array.isArray(health?.issues) && health.issues.some(issue => String(issue).includes('API is not reachable'));
  const inactiveLabel = backendDisconnected ? '后端未连接' : '未配置';
  const cards = [
    ['运行模式', health?.profile === 'pure_cloud_demo' ? '公开演示' : (health?.profile || '公开演示'), '公开演示模式，不暴露私有资产入口'],
    ['MinerU 官方 API', health?.components?.mineru_official_api?.available ? '已配置' : inactiveLabel, backendDisconnected ? '等待 FastAPI 云端后端返回真实配置状态' : '仅用于公开 PDF URL 或公开 PDF 上传'],
    ['DeepSeek API', health?.components?.deepseek_api?.available ? '已配置' : inactiveLabel, backendDisconnected ? '等待 FastAPI 云端后端返回真实配置状态' : '服务端代理调用，密钥不进入浏览器'],
    ['实时额度', `${quota.remaining ?? '-'}/${quota.limit ?? '-'}`, '每日统一额度，用完后停止实时调用'],
    ['上传限制', `${health?.limits?.upload_max_mb ?? 20}MB`, '只接受公开 PDF，患者材料和私有资料不上云'],
    ['重资产能力', '仅回放', '私有向量库、批量实验和长任务不在云端执行'],
  ];
  return (
    <SectionWrapper>
      <div className="custom-screen space-y-6">
        <PageHeader title="云端状态" desc="检查公开演示工作台的服务状态、额度、上传限制和完整系统能力边界。" />
        <MetricGrid health={health} />
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
          {cards.map(([label, value, desc]) => (
            <div key={label} className="border rounded-lg bg-white p-4">
              <div className="text-[11px] font-mono text-gray-500">{label}</div>
              <div className="mt-2 text-lg font-semibold text-gray-900">{value}</div>
              <div className="mt-1 text-xs leading-5 text-gray-600">{desc}</div>
            </div>
          ))}
        </div>
        <div className="border rounded-lg p-5 bg-white">
          <h2 className="text-sm font-semibold text-gray-800 mb-2">运行策略</h2>
          <p className="text-xs text-gray-500 mb-3">上方是评审可读状态；下方保留原始 JSON，方便部署排查。</p>
          <details className="rounded border bg-gray-50">
            <summary className="cursor-pointer px-3 py-2 text-xs font-semibold text-gray-700">展开原始 health/runtime JSON</summary>
            <pre className="overflow-auto border-t bg-white p-3 text-[11px] text-gray-700">{JSON.stringify({ health, runtime: state.runtime }, null, 2)}</pre>
          </details>
        </div>
      </div>
    </SectionWrapper>
  );
}
