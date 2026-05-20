import Link from 'next/link';
import SectionWrapper from '../components/SectionWrapper';
import RuntimeSummary from '../components/workbench/RuntimeSummary';
import StatusPill from '../components/workbench/StatusPill';

const cards = [
  { track: 'Track1', title: '论文解析与出题评测', desc: 'PDF/样例论文 → MinerU 解析 → 四维出题 → 答题评分', href: '/track1' },
  { track: 'Track2', title: 'Agent 自动化工作流', desc: '任务目标 → Intent Router → DAG → 资源调度 → 来源日志', href: '/track2' },
  { track: 'Track3', title: 'Medical RAG', desc: '临床查询 → 混合检索 → chunk 来源 → 引用回答', href: '/track3' },
];

const metrics = [
  { v: '500', l: '核心题目', s: 'A/B/C/D 四维评测' },
  { v: '14', l: 'Agent Intent', s: '任务路由与调度' },
  { v: '3,348', l: '医学 Chunk', s: 'FAISS + BM25' },
  { v: '730', l: '视觉描述', s: '图文来源增强' },
  { v: '5090', l: '本地算力', s: '隐私任务本地执行' },
  { v: '3', l: '公开报告', s: 'docs/submissions' },
];

const evidenceFlow = [
  { title: '努力', body: '本地小模型、5090、MinerU Docker、Agent CLI、医学索引与多轮实验。' },
  { title: '来源', body: '数据集、排行榜、chunk 索引、dry-run 日志、验收包和三份公开报告。' },
  { title: '评分理由', body: '把工程可复现、可解释、可信、隐私边界逐项映射到评分细则。' },
  { title: '交付物', body: '前端工作台、demo CLI、docs/submissions 报告与可溯源数据。' },
];

export default function Home({ runtimeConfig }) {
  return (
    <SectionWrapper>
      <div className="custom-screen space-y-8">
        <section className="pt-4">
          <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-5">
            <div>
              <div className="flex items-center gap-2 mb-3">
                <StatusPill status="ready" label="可复现" />
                <span className="text-[11px] text-gray-600 font-mono">ControlMind · Local-first Scientific Evaluation Workbench</span>
              </div>
              <h1 className="text-3xl text-gray-800 font-extrabold sm:text-5xl tracking-tight">ControlMind：本地优先的科学评测工作台</h1>
              <p className="text-base text-gray-600 max-w-3xl mt-4 leading-relaxed">
                把已经通过终端验证的解析、评测、Agent 和 Medical RAG 能力，组织成评委可点击、可复现、可追溯的交付界面。
              </p>
            </div>
            <Link href="/demo" className="px-5 py-3 bg-gray-900 text-white rounded-lg text-sm font-medium hover:bg-gray-800">进入演示路径</Link>
          </div>
        </section>

        <RuntimeSummary runtimeConfig={runtimeConfig} />

        <section className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
          {metrics.map(m => (
            <div key={m.l} className="border rounded-lg p-4 bg-white">
              <div className="text-2xl font-bold text-gray-800">{m.v}</div>
              <div className="text-xs text-gray-600 mt-1">{m.l}</div>
              <div className="text-[11px] text-gray-500 mt-1">{m.s}</div>
            </div>
          ))}
        </section>

        <section className="border rounded-lg bg-white p-5">
          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-2 mb-4">
            <div>
              <h2 className="text-xl font-semibold text-gray-800">评审可确认的来源链</h2>
              <p className="text-sm text-gray-600 mt-1">不是把工作量堆给评委，而是把工作量整理成可核验理由。</p>
            </div>
            <Link href="/evidence" className="text-sm text-sky-700 hover:text-sky-800">打开完整来源矩阵</Link>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-3">
            {evidenceFlow.map((item, index) => (
              <div key={item.title} className="border rounded-lg p-4 bg-gray-50">
                <div className="flex items-center gap-2 mb-2">
                  <span className="w-6 h-6 rounded-full bg-gray-900 text-white text-xs flex items-center justify-center">{index + 1}</span>
                  <h3 className="text-sm font-semibold text-gray-800">{item.title}</h3>
                </div>
                <p className="text-xs text-gray-600 leading-relaxed">{item.body}</p>
              </div>
            ))}
          </div>
        </section>

        <section>
          <div className="flex items-end justify-between mb-4">
            <div>
              <h2 className="text-xl font-semibold text-gray-800">三赛道验证入口</h2>
              <p className="text-sm text-gray-600 mt-1">每个页面都对应一条端到端能力链，并展示降级、来源与产物路径。</p>
            </div>
            <Link href="/evidence" className="text-sm text-sky-700 hover:text-sky-800">查看来源矩阵</Link>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {cards.map(c => (
              <Link key={c.track} href={c.href} className="border rounded-lg p-5 bg-white hover:shadow-md transition-shadow">
                <span className="text-xs font-mono bg-gray-900 text-white px-2 py-0.5 rounded">{c.track}</span>
                <h3 className="font-semibold text-gray-800 mt-3 mb-1">{c.title}</h3>
                <p className="text-xs text-gray-600 leading-relaxed">{c.desc}</p>
              </Link>
            ))}
          </div>
        </section>

        <section className="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <div className="border rounded-lg p-5 bg-gray-50">
            <h3 className="text-sm font-semibold text-gray-800 mb-3">隐私与资源边界</h3>
            <div className="space-y-2 text-sm text-gray-600">
              <p>公开/脱敏任务可使用云端 API 提升效率。</p>
              <p>原文、医疗数据、微调产物、中间 chunk 与本地索引保留在本地环境。</p>
              <p>当 Docker、GPU 或 API 不可用时，工作台降级到已验证产物复现，不伪装成实时执行。</p>
            </div>
          </div>
          <div className="border rounded-lg p-5 bg-gray-50">
            <h3 className="text-sm font-semibold text-gray-800 mb-3">交付物定位</h3>
            <div className="space-y-2 text-sm text-gray-600">
              <p>终端脚本负责真实计算与评测，前端负责把链路、来源和产物组织成可核验流程。</p>
              <p>demo CLI 是三赛道复现基线：`python demo/cli/controlscidemo all --quick` 可独立验证关键样例。</p>
              <p>每个输出都尽量指向报告、数据集、日志或索引产物，避免只展示口号。</p>
              <p>面向评审时可以按演示路径顺序点击，也可以直接进入任一赛道独立验证。</p>
            </div>
          </div>
        </section>
      </div>
    </SectionWrapper>
  );
}
