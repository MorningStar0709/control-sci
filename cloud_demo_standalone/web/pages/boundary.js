import SectionWrapper from '../components/SectionWrapper';
import { PageHeader } from '../components/workbench/CloudDemoBlocks';

const cloudRows = [
  ['输入范围', '公开论文、脱敏摘要、预置 trace、公开任务目标'],
  ['执行方式', '服务端代理 MinerU/DeepSeek；浏览器不接触 API Key'],
  ['展示方式', '可实时调用的公开 API + 已验证 trace 回放'],
  ['限制原则', '不开放私有语料上传、不触发长任务、不伪装完整系统索引状态'],
];

const completeRows = [
  ['资产范围', '私有 PDF、Markdown、chunk、索引、模型权重、批量实验日志'],
  ['执行方式', '受控环境内解析、检索、微调、Judge、飞轮长任务'],
  ['验收方式', 'DATA-TRACE、trace JSONL、CLI、报告附录与完整工作台复核'],
  ['边界原则', '默认本地，显式授权后云端兜底，非必要不上云'],
];

const trackRows = [
  ['赛道一', '公开 PDF 解析、单题出题评分、样例回放', '私有语料、全量榜单、批量 Judge、训练数据'],
  ['赛道二', '公开任务规划、DAG 和产物回放', '长任务执行、私有资源调度、批量日志重放'],
  ['赛道三', '医学来源回放、中文机制解释、安全边界', '医疗原文、chunk、索引、患者或机构私有材料'],
];

function BoundaryCard({ title, rows }) {
  return (
    <section className="rounded-lg border bg-white p-5">
      <h2 className="text-sm font-semibold text-gray-900">{title}</h2>
      <div className="mt-4 space-y-2">
        {rows.map(([label, value]) => (
          <div key={label} className="grid grid-cols-[6rem_1fr] gap-3 rounded border bg-gray-50 px-3 py-3 text-xs leading-5">
            <div className="font-semibold text-gray-900">{label}</div>
            <div className="text-gray-650">{value}</div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default function BoundaryPage() {
  return (
    <SectionWrapper>
      <div className="custom-screen space-y-6">
        <PageHeader title="公开云端展示边界" desc="把云端 Demo 与完整系统分清楚：云端用于公开体验和可核验回放，完整系统负责私有资产、长任务、索引模型和批量实验。" />

        <div className="grid grid-cols-1 xl:grid-cols-2 gap-4">
          <BoundaryCard title="云端 Demo" rows={cloudRows} />
          <BoundaryCard title="完整系统" rows={completeRows} />
        </div>

        <section className="rounded-lg border bg-white overflow-hidden">
          <div className="border-b bg-gray-50 p-5">
            <h2 className="text-sm font-semibold text-gray-900">三赛道边界映射</h2>
            <p className="mt-1 text-xs text-gray-600">云端保留可公开体验的部分；完整链路通过 trace、CLI、报告和本地工作台复核。</p>
          </div>
          <div className="overflow-x-auto">
            <table className="w-full text-xs">
              <thead className="bg-gray-50 text-gray-500">
                <tr>
                  {['赛道', '云端展示', '完整系统'].map(header => (
                    <th key={header} className="px-4 py-3 text-left font-medium whitespace-nowrap">{header}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {trackRows.map(row => (
                  <tr key={row[0]} className="border-t">
                    <td className="px-4 py-3 font-semibold text-gray-900">{row[0]}</td>
                    <td className="px-4 py-3 text-gray-650 leading-5">{row[1]}</td>
                    <td className="px-4 py-3 text-gray-650 leading-5">{row[2]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <section className="rounded-lg border bg-amber-50 p-5 text-sm leading-7 text-amber-900">
          <strong>演示口径：</strong>云端不是第二套系统，也不是把所有能力搬到公网。它是把完整系统中适合公开评审的动作压缩成可操作页面，并用 trace 回放证明重资产能力已经在受控环境完成。
        </section>
      </div>
    </SectionWrapper>
  );
}
