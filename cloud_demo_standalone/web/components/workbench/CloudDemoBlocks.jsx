import { useState } from 'react';
import Link from 'next/link';
import { apiGet, apiPost, apiRequest } from '../../lib/apiClient';
import MarkdownText from './MarkdownText';
import StatusPill from './StatusPill';
import StepCard from './StepCard';
import PipelineStep from './PipelineStep';
import WorkbenchLoadingCard from './WorkbenchLoadingCard';
import ErrorCallout from './ErrorCallout';
import LoadingDots from './LoadingDots';

const SAMPLE_PDF_URL = 'https://cdn-mineru.openxlab.org.cn/demo/example.pdf';
const TRACK1_SAMPLE_SOURCE = [
  '# 公开脱敏论文摘要',
  '',
  '研究讨论了含时滞控制系统的稳定性分析与保守性降低问题。论文通过构造 Lyapunov-Krasovskii 泛函，并结合积分不等式与线性矩阵不等式（LMI）条件，给出一组可计算的稳定性判据。',
  '',
  '核心结论是：如果存在正定矩阵 $P \\succ 0$ 和松弛变量使得对应 LMI 可行，则闭环系统在给定时滞上界下保持渐近稳定。该方法的优势在于把连续时间稳定性证明转化为凸优化可求解问题，但结论依赖于模型假设、时滞上界和不等式放缩方式。',
  '',
  '一个简化稳定性条件可写为 $\\dot V(x_t) < 0$。在实际评测中，模型回答需要说明 Lyapunov 泛函选择、LMI 可行性含义、保守性来源，以及该判据不能直接证明未建模扰动或超出时滞上界的情形。',
].join('\n');

export function PageHeader({ title = '展示导览', desc }) {
  return (
    <div className="border-b pb-5">
      <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-3">
        <div>
          <h1 className="text-gray-900 text-3xl font-semibold sm:text-4xl mb-2">{title}</h1>
          <p className="text-gray-500 text-sm max-w-3xl">{desc}</p>
        </div>
        <div className="flex items-center gap-2 text-[11px] font-mono text-gray-500">
          <span className="rounded border bg-white px-2 py-1">公开云端模式</span>
          <span className="rounded border bg-white px-2 py-1">密钥服务端托管</span>
          <span className="rounded border bg-white px-2 py-1">公开/脱敏输入</span>
        </div>
      </div>
    </div>
  );
}

function BusyLabel({ active, busyText, idleText }) {
  if (!active) return idleText;
  return (
    <span className="inline-flex items-center justify-center gap-1.5">
      {busyText}
      <LoadingDots className="w-4" sizeClassName="h-1 w-1" />
    </span>
  );
}

export function ShowcaseHeader({ health }) {
  const mineruReady = health?.components?.mineru_official_api?.available;
  const deepseekReady = health?.components?.deepseek_api?.available;
  const backendDisconnected = Array.isArray(health?.issues) && health.issues.some(issue => String(issue).includes('API is not reachable'));
  const inactiveLabel = backendDisconnected ? '后端未连接' : '未配置';
  return (
    <section className="border rounded-lg bg-white overflow-hidden">
      <div className="p-6 lg:p-7 grid grid-cols-1 lg:grid-cols-[1.4fr_0.9fr] gap-6">
        <div>
          <div className="text-[11px] font-mono text-gray-500 mb-3">ControlMind 在线展示版</div>
          <h1 className="text-3xl sm:text-4xl font-semibold text-gray-900 leading-tight">科学文档智能处理成果展示台</h1>
          <p className="mt-4 text-sm text-gray-600 max-w-3xl">
            延续完整系统的三赛道设计，在线版本聚焦公开样例体验、成果浏览和来源回放；私有语料、长任务和本地索引保留在受控环境中复现。
          </p>
          <div className="mt-5 grid grid-cols-1 md:grid-cols-3 gap-2">
            {[
              ['赛道一', '公开 PDF 解析 → 出题 → 评分'],
              ['赛道二', '公开任务规划 → 产物回放'],
              ['赛道三', 'RAG trace → 来源回放 → 边界'],
            ].map(([label, text]) => (
              <div key={label} className="rounded border bg-gray-50 p-3">
                <div className="text-xs font-semibold text-gray-900">{label}</div>
                <div className="mt-1 text-[11px] text-gray-600 leading-snug">{text}</div>
              </div>
            ))}
          </div>
        </div>
        <div className="rounded-lg border bg-gray-50 p-4">
          <div className="text-xs font-semibold text-gray-900 mb-3">实时云端依赖</div>
          <div className="space-y-2">
            {[
              ['MinerU 官方 API', mineruReady ? '已配置' : inactiveLabel, mineruReady],
              ['DeepSeek API', deepseekReady ? '已配置' : inactiveLabel, deepseekReady],
              ['Next 工作台', '已部署', true],
              ['FastAPI 后端', health?.status === 'ready' ? '已连接' : '未连接', health?.status === 'ready'],
            ].map(([name, status, ok]) => (
              <div key={name} className="flex items-center justify-between rounded border bg-white px-3 py-2">
                <span className="text-xs text-gray-700">{name}</span>
                <span className={`text-[11px] px-2 py-0.5 rounded ${ok ? 'bg-green-100 text-green-700' : 'bg-amber-100 text-amber-700'}`}>{status}</span>
              </div>
            ))}
          </div>
          <div className="mt-4 rounded border bg-white p-3">
            <div className="text-[11px] text-gray-500">今日实时调用额度</div>
            <div className="mt-1 text-2xl font-mono font-semibold text-gray-900">
              {health?.components?.quota?.remaining ?? '-'}/{health?.components?.quota?.limit ?? '-'}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export function Notice() {
  return (
    <div className="border rounded-lg p-5 bg-gray-50 text-sm text-gray-600 space-y-2">
      <p><strong className="text-gray-800">展示原则：</strong>在线页面与完整工作台保持同构；适合公开体验的按钮提供轻量操作，重资产能力以结果回放和来源查看呈现。</p>
      <p>在线展示版只处理公开/脱敏材料；实时能力由服务端代理 MinerU 官方 API 与 DeepSeek，密钥不进入浏览器。</p>
    </div>
  );
}

export function OutcomeStrip() {
  const items = [
    ['可部署', 'Ubuntu 双服务部署，公网入口只暴露工作台。'],
    ['可体验', '公开 URL、PDF 上传、任务规划、医学来源回放都可浏览。'],
    ['可追溯', 'health/runtime/tracks/quiz/grade/rag 都有独立入口可查看。'],
    ['边界清楚', '无私有资产入口，密钥不进浏览器。'],
  ];
  return (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-3">
      {items.map(([title, desc]) => (
        <div key={title} className="border rounded-lg bg-white p-4">
          <div className="text-sm font-semibold text-gray-900">{title}</div>
          <div className="mt-2 text-xs text-gray-600 leading-relaxed">{desc}</div>
        </div>
      ))}
    </div>
  );
}

export function AchievementOverview() {
  const groups = [
    {
      title: '赛道一：Sci-Align',
      desc: '控制科学 PDF 资产进入可评测、可训练、可追溯的数据基座。',
      metrics: [
        ['362', 'PDF 文档'],
        ['253,012', 'LaTeX 公式'],
        ['28,514', '语义 chunk'],
        ['500', '核心评测题'],
      ],
    },
    {
      title: '赛道二：Data Agent',
      desc: '把语料生产从脚本流水线升级为可规划、可恢复、可审计的执行协议。',
      metrics: [
        ['15', 'Intent 能力'],
        ['4', '推理轨道'],
        ['9,207', '视觉审计判决'],
        ['391s', '飞轮闭环'],
      ],
    },
    {
      title: '赛道三：医学 RAG',
      desc: '医学文献问答保留检索来源、结论状态、安全拒答和中文机制解释。',
      metrics: [
        ['3,348', '医学文段'],
        ['FAISS + BM25', '混合检索'],
        ['混合 RRF', '融合策略'],
        ['100%', '样例引用覆盖'],
      ],
    },
  ];
  return (
    <section className="grid grid-cols-1 xl:grid-cols-3 gap-4">
      {groups.map(group => (
        <article key={group.title} className="border rounded-lg bg-white p-5">
          <h2 className="text-sm font-semibold text-gray-900">{group.title}</h2>
          <p className="mt-2 text-xs leading-5 text-gray-600">{group.desc}</p>
          <div className="mt-4 grid grid-cols-2 gap-2">
            {group.metrics.map(([value, label]) => (
              <div key={label} className="rounded border bg-gray-50 px-3 py-3">
                <div className="font-mono text-lg font-semibold text-gray-900">{value}</div>
                <div className="mt-1 text-[11px] text-gray-500">{label}</div>
              </div>
            ))}
          </div>
        </article>
      ))}
    </section>
  );
}

export function DemoRouteMap() {
  const routes = [
    ['1', '确认状态', '查看 MinerU、DeepSeek、额度、上传限制是否满足公开展示条件。', '/health'],
    ['2', '进入赛道一', '用公开 PDF URL 或摘要完成解析、出题和评分的最小闭环。', '/track1'],
    ['3', '进入赛道二', '输入公开任务目标，生成 intent、DAG、资源策略和产物来源摘要。', '/track2'],
    ['4', '进入赛道三', '回放医学 RAG 案例，展示来源、结论状态和安全边界。', '/track3'],
    ['5', '查看来源矩阵', '把三赛道报告、数据、API 和复现路径逐项对上。', '/evidence'],
  ];
  return (
    <section className="border rounded-lg bg-white p-5">
      <div className="flex items-center justify-between gap-3 mb-4">
        <div>
          <h2 className="text-sm font-semibold text-gray-900">推荐浏览顺序</h2>
          <p className="text-xs text-gray-500 mt-1">这页只保留操作路径，不再重复总览页的成果陈列。</p>
        </div>
        <span className="rounded border bg-gray-50 px-2 py-1 text-[11px] font-mono text-gray-600">五步导览</span>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-5 gap-3">
        {routes.map(([idx, title, desc, href]) => (
          <Link key={idx} href={href} className="rounded-lg border bg-gray-50 p-3 hover:bg-white hover:shadow-sm transition">
            <div className="w-7 h-7 rounded-full bg-gray-900 text-white flex items-center justify-center text-xs font-bold">{idx}</div>
            <div className="mt-3 text-sm font-semibold text-gray-900">{title}</div>
            <div className="mt-2 text-xs leading-5 text-gray-600">{desc}</div>
          </Link>
        ))}
      </div>
    </section>
  );
}

export function LocalCloudMirrorMap() {
  const rows = [
    ['赛道一', 'PDF 解析、ABCD 出题、模型答题、Judge 评分、全量榜单', '公开 PDF 解析、摘要出题、单题评分', '私有语料、全量批跑'],
    ['赛道二', 'Data Agent 飞轮、DAG、日志、恢复、跨模态审计', '公开任务规划、产物回放、来源矩阵', '长任务、私有语料重跑'],
    ['赛道三', '医学 RAG、混合检索、结论校验、安全拒答', '稳定来源回放、公开样例检索、中文机制解释', '患者材料、院内资产'],
  ];
  return (
    <section className="border rounded-lg bg-white overflow-hidden">
      <div className="p-5 border-b">
        <h2 className="text-sm font-semibold text-gray-900">公开展示边界</h2>
        <p className="text-xs text-gray-500 mt-1">三赛道能力按公开访问场景重新呈现：可实时体验的保留为云端操作，重资产能力以来源和产物回放方式呈现。</p>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-xs">
          <thead className="bg-gray-50 text-gray-500">
            <tr>
              {['赛道', '完整系统能力', '在线展示能力', '本地复现能力'].map(h => <th key={h} className="text-left font-medium px-4 py-3 whitespace-nowrap">{h}</th>)}
            </tr>
          </thead>
          <tbody>
            {rows.map(row => (
              <tr key={row[0]} className="border-t">
                {row.map((cell, idx) => <td key={cell} className={`px-4 py-3 align-top leading-5 ${idx === 0 ? 'font-semibold text-gray-900' : 'text-gray-600'}`}>{cell}</td>)}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export function ApiPipeline() {
  const steps = [
    ['1', '解析', '/api/mineru/url · /api/mineru/upload', 'MinerU 官方 API 接收公开 PDF，返回任务或 Markdown 预览。'],
    ['2', '出题', '/api/quiz/generate', 'DeepSeek 根据解析文本生成题目、标准答案和评分规则。'],
    ['3', '规划', '/api/agent/plan', '公开任务目标进入 intent、DAG、资源策略和核验摘要。'],
    ['4', 'RAG', '/api/medical-rag/ask', '医学问题先匹配公开来源，再回放稳定中文回答和边界声明。'],
  ];
  return (
    <section className="border rounded-lg bg-white p-5">
      <div className="flex items-center justify-between gap-3 mb-4">
        <div>
          <h2 className="text-sm font-semibold text-gray-900">在线服务与回放链路</h2>
          <p className="text-xs text-gray-500 mt-1">不是静态截图，在线版本保留适合公开体验的轻量操作；长任务与私有索引以产物回放呈现。</p>
        </div>
        <span className="rounded border bg-gray-50 px-2 py-1 text-[11px] font-mono text-gray-600">服务端代理</span>
      </div>
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-3">
        {steps.map(([idx, title, api, desc]) => (
          <div key={api} className="rounded-lg border bg-gray-50 p-3">
            <div className="flex items-center gap-2">
              <span className="w-7 h-7 rounded-full bg-gray-900 text-white flex items-center justify-center text-xs font-bold">{idx}</span>
              <span className="text-sm font-semibold text-gray-900">{title}</span>
            </div>
            <div className="mt-3 text-[11px] font-mono text-gray-700 break-all">{api}</div>
            <div className="mt-2 text-xs text-gray-600 leading-relaxed">{desc}</div>
          </div>
        ))}
      </div>
    </section>
  );
}

export function CapabilityMatrix() {
  const rows = [
    ['赛道一论文解析', '公开 PDF URL / 上传 PDF', 'MinerU 官方 API', '任务响应、Markdown 预览、解析字符数'],
    ['赛道一出题评分', '解析文本 / 摘要 / 作答', 'DeepSeek', '题型、题干、参考答案、评分规则、反馈'],
    ['赛道二任务规划', '公开任务目标', '云端确定性规划器', 'intent、DAG、资源策略、核验摘要'],
    ['赛道三 医学 RAG', '中文医学文献问题', '公开来源回放', '命中来源、中文回答、结论状态、安全声明'],
    ['部署核验', 'health/runtime/tracks', '服务端代理', '状态、额度、依赖状态、纯云端策略'],
  ];
  return (
    <section className="border rounded-lg bg-white overflow-hidden">
      <div className="p-5 border-b">
        <h2 className="text-sm font-semibold text-gray-900">成果矩阵</h2>
        <p className="text-xs text-gray-500 mt-1">把成果拆成输入、云端能力和可见输出，方便访问者逐项浏览。</p>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-xs">
          <thead className="bg-gray-50 text-gray-500">
            <tr>
              {['能力', '输入', '云端服务', '输出/来源'].map(h => <th key={h} className="text-left font-medium px-4 py-3 whitespace-nowrap">{h}</th>)}
            </tr>
          </thead>
          <tbody>
            {rows.map(row => (
              <tr key={row[0]} className="border-t">
                {row.map((cell, idx) => <td key={cell} className={`px-4 py-3 align-top ${idx === 0 ? 'font-semibold text-gray-900' : 'text-gray-600'}`}>{cell}</td>)}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

const trackEvidenceMatrix = [
  {
    track: '赛道一',
    code: 'T1',
    role: '科学对齐评测基座',
    title: 'ControlMind Sci-Align 评测基座',
    effort: '362 PDF 文档 · 253,012 LaTeX 公式 · 11,554 嵌入图片 · 28,514 语义 chunk · 500 核心评测题 · A/B/C/D 四维平衡',
    scoring: '评分依据不是单次 API 成功，而是控制科学语料被结构化后，能够进入四维 Benchmark、自动出题、模型答题与 Judge 评分，并保留题目、参考答案、评分理由和来源路径。',
    deliverable: '赛道一在线展示：MinerU 官方 API 解析公开 PDF，DeepSeek 基于解析文本出题并评分。',
    report_path: 'docs/submissions/track1_sci_align_report.md · docs/submissions/shared/DATA-TRACE.md',
    sources: [
      ['track1_sci_align_report.md', 'docs/submissions/track1_sci_align_report.md', 156],
      ['track1_sci_align_20_cases.md', 'docs/submissions/track1_sci_align_20_cases.md', 88],
      ['core.json', 'benchmark/dataset/core.json', 512],
      ['leaderboard_complete.json', 'benchmark/eval/results/leaderboard_complete.json', 64],
      ['云端出题评分 API', '/api/demo/quiz/generate · /api/demo/quiz/grade', 0],
    ],
  },
  {
    track: '赛道二',
    code: 'T2',
    role: 'Agent 工作流与数据飞轮',
    title: 'ControlMind Data Agent 执行协议',
    effort: '15 Intent 能力 · 4 推理轨道 · 9,207 视觉审计判决 · 391s 数据飞轮闭环 · 62ms 故障降级案例 · 17 跨领域协议复用',
    scoring: '依据说明是 Agent 把自然语言目标拆成 intent、DAG、资源调度、执行摘要和来源日志，而不是把固定 pipeline 包装成智能体。在线版展示公开任务规划和来源摘要，不执行长任务。',
    deliverable: '赛道二在线展示：呈现意图路由、资源调度、执行校验、日志与来源的协议结构。',
    report_path: 'docs/submissions/track2_agent_report.md · docs/submissions/judge_quickstart.md',
    sources: [
      ['track2_agent_report.md', 'docs/submissions/track2_agent_report.md', 132],
      ['Agent 能力注册表', 'benchmark/agent/agent_capabilities.json', 24],
      ['视觉审计摘要', 'docs/submissions/data_trace_bundle/05_cross_modal/cross_modal_audit_summary.json', 18],
      ['追溯包清单', 'docs/submissions/data_trace_bundle/manifest.json', 42],
      ['云端运行 API', '/api/demo/runtime/options · /api/demo/tracks', 0],
    ],
  },
  {
    track: '赛道三',
    code: 'T3',
    role: '医学来源约束 RAG',
    title: '医学 RAG 来源问答与安全边界',
    effort: '3,348 医学文段 · FAISS + BM25 · 混合 RRF · BGE M3 / 高维索引 / BGE Small · 结论校验 · 安全拒答',
    scoring: '依据说明是医学回答必须先检索后合成，保留文段、引用、结论支撑状态和拒答边界。在线版回放已验证 trace，不声称现场访问私有资产。',
    deliverable: '赛道三在线展示：按 Ask 页口径回放已验证来源、中文回答、结论状态和安全声明。',
    report_path: 'docs/submissions/track3_medical_rag_report.md · docs/submissions/shared/DATA-TRACE.md',
    sources: [
      ['track3_medical_rag_report.md', 'docs/submissions/track3_medical_rag_report.md', 148],
      ['医学 RAG 评测', 'docs/submissions/data_trace_bundle/07_medical_rag/', 96],
      ['视觉描述产物', 'docs/submissions/data_trace_bundle/06_medical_vision/', 72],
      ['快速导览', 'docs/submissions/judge_quickstart.md', 54],
      ['医学 RAG API', '/api/demo/medical-rag/ask', 0],
    ],
  },
];

const trackShowcases = {
  track1: {
    title: '赛道一：ControlMind Sci-Align 评测基座',
    subtitle: '把控制科学 PDF 资产转化为可训练、可评测、可追溯的数据基础设施。',
    note: '云端版本展示成果主张与公开轻量闭环；公开可操作能力只走服务端代理，不暴露私有资产入口。',
    pain: [
      ['控制科学评测缺口', '通用基准很少覆盖控制科学，更缺少条件敏感和开放设计两个工程关键维度。'],
      ['复杂 PDF 难以消费', '扫描教材、公式、图片和表格需要先被结构化，才能进入训练、检索和评测链路。'],
      ['模型答案需要验真', 'LLM 很容易写出看似合理的控制方案，必须用四维 Benchmark 量化能力边界。'],
      ['私有资料不能默认上云', '原文、chunk、向量索引和微调样本属于受控资产，公开或脱敏任务才允许云端兜底。'],
    ],
    metrics: [
      ['362', 'PDF 文档'],
      ['253,012', 'LaTeX 公式'],
      ['11,554', '嵌入图片'],
      ['28,514', '语义 chunk'],
      ['500', '核心评测题'],
      ['A/B/C/D', '四维平衡'],
    ],
    protocol: [
      ['评测对象', '9 个主流 LLM，全量 500 题'],
      ['能力分层', '概念回溯、多步推理、条件敏感、开放设计'],
      ['可靠性', '跨管道 MAE=0.0003，三 Judge κ=0.575'],
      ['云端边界', '只处理公开/脱敏输入，出题评分由服务端代理 API 完成'],
    ],
  },
  track2: {
    title: '赛道二：ControlMind Data Agent',
    subtitle: '把科学文档语料生产从脚本流水线升级为可规划、可恢复、可审计的 Agent 执行协议。',
    note: '在线版本展示 Agent 协议、能力矩阵和公开任务规划；不启动长任务或私有语料重跑。',
    pain: [
      ['人工语料产线成本高', '文献检索、解析调参、视觉质检、出题、评测和排行榜更新累计约 558 工时。'],
      ['脚本流水线不可恢复', '固定 pipeline 只能按顺序跑，缺少失败降级、checkpoint 和质量闭环协议。'],
      ['云端边界难执行', '公开材料、私有原文、chunk、索引和微调产物需要由系统自动路由。'],
      ['跨模态质检难规模化', '图片、公式、表格和正文需要统一审计，不能依赖人工逐篇抽查。'],
    ],
    metrics: [
      ['14', 'Intent 能力'],
      ['4', '推理轨道'],
      ['9,207', '视觉审计判决'],
      ['391s', '数据飞轮闭环'],
      ['62ms', '故障降级案例'],
      ['17', '跨领域模块'],
    ],
    protocol: [
      ['意图路由', '自然语言目标转成可组合 intent 序列'],
      ['资源调度', '按 data policy 选择公开 API、回放产物或脚本资源'],
      ['执行与校验', '执行、检查、重试、降级和写入日志'],
      ['日志与来源', '输出摘要、来源产物和可复现命令'],
    ],
  },
  track3: {
    title: '赛道三：医学 RAG 来源回放',
    subtitle: '按 Ask 页口径回放检索来源、中文回答、结论状态和安全边界。',
    note: '完整系统包含私有医学 RAG；在线版本展示公开/脱敏案例回放，不声称现场访问私有医学资产。',
    pain: [
      ['医学回答必须有来源', '不能凭模型记忆直接生成医学结论，必须先检索、再合成、再校验。'],
      ['中文问题对英文文献', '用户用中文问，系统要能命中英文论文 chunk 并回到中文解释。'],
      ['引用与 claim 要能复核', '每条关键结论需要 chunk 引用和 supported / insufficient 状态。'],
      ['安全边界不能含糊', '个人诊疗、用药建议和急症问题必须拒答或转向就医建议。'],
    ],
    metrics: [
      ['3,348', '医学文段'],
      ['FAISS + BM25', '混合检索'],
      ['混合 RRF', '默认融合'],
      ['BGE M3', '主索引'],
      ['100%', '引用覆盖样例'],
      ['拒答', '安全边界'],
    ],
    protocol: [
      ['问题改写', '中文问题转医学来源检索表达'],
      ['混合检索', 'Dense / BM25 / Vision 结果融合'],
      ['来源组织', '基于 chunk 生成中文回答和引用'],
      ['安全边界', '来源不足、个人诊疗和急症问题不强行回答'],
    ],
  },
};

function sizeText(sizeKb) {
  if (!sizeKb) return 'API';
  return sizeKb >= 1024 ? `${(sizeKb / 1024).toFixed(1)} MB` : `${sizeKb} KB`;
}

export function TrackShowcase({ id }) {
  const data = trackShowcases[id];
  if (!data) return null;
  return (
    <section className="space-y-4">
      <div className="border rounded-lg bg-white p-5">
      <div className="text-[11px] font-mono text-gray-500 mb-2">云端展示与完整工作台对齐</div>
        <h2 className="text-2xl font-semibold text-gray-900">{data.title}</h2>
        <p className="mt-2 text-sm text-gray-600 max-w-3xl">{data.subtitle}</p>
        <div className="mt-4 rounded border bg-sky-50 px-3 py-2 text-xs leading-6 text-sky-900">{data.note}</div>
      </div>
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-3">
        {data.pain.map(([title, desc]) => (
          <div key={title} className="rounded-lg border bg-white p-4">
            <div className="text-sm font-semibold text-gray-900">{title}</div>
            <div className="mt-2 text-xs leading-5 text-gray-600">{desc}</div>
          </div>
        ))}
      </div>
      <div className="grid grid-cols-1 xl:grid-cols-3 gap-4">
        <div className="xl:col-span-2 rounded-lg border bg-white p-5">
          <div className="text-sm font-semibold text-gray-900">核心成果指标</div>
          <div className="mt-1 text-xs text-gray-500">沿用完整工作台的成果口径，在线版本聚焦公开展示和轻量查看。</div>
          <div className="mt-4 grid grid-cols-2 md:grid-cols-3 gap-3">
            {data.metrics.map(([value, label]) => (
              <div key={label} className="rounded border bg-gray-50 px-3 py-3">
                <div className="font-mono text-lg font-semibold text-gray-900">{value}</div>
                <div className="mt-1 text-[11px] text-gray-500">{label}</div>
              </div>
            ))}
          </div>
        </div>
        <div className="rounded-lg border bg-white p-5">
          <div className="text-sm font-semibold text-gray-900">协议 / 依据说明</div>
          <div className="mt-4 space-y-2">
            {data.protocol.map(([label, text]) => (
              <div key={label} className="rounded border bg-gray-50 px-3 py-2">
                <div className="text-xs font-semibold text-gray-900">{label}</div>
                <div className="mt-1 text-[11px] leading-5 text-gray-600">{text}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

export function EvidenceMatrix() {
  const [expanded, setExpanded] = useState('');
  const fileCount = trackEvidenceMatrix.reduce((sum, t) => sum + t.sources.length, 0);
  const totalKb = trackEvidenceMatrix.reduce((sum, t) => sum + t.sources.reduce((inner, item) => inner + item[2], 0), 0);
  return (
    <section className="space-y-5">
      <header className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-5">
        <div className="max-w-3xl">
          <div className="text-xs font-mono text-gray-500 mb-3">数据追溯台 / 公开展示矩阵</div>
          <h1 className="text-gray-900 text-3xl font-semibold sm:text-4xl mb-3">来源矩阵</h1>
          <p className="text-gray-600 text-sm leading-7">
            三条赛道的核心来源、依据说明和公开交付物集中在一屏。在线版展示公开可讲的成果来源链，并把长任务替换为可访问 API 或公开报告路径。
          </p>
        </div>
        <Link href="/api/demo/health" className="self-start lg:self-auto px-4 py-2 border rounded bg-white text-xs text-gray-700 hover:bg-gray-50">打开 health API</Link>
      </header>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div className="border rounded-lg bg-white p-4"><div className="text-[11px] font-mono text-gray-500">赛道数量</div><div className="mt-2 text-2xl font-semibold text-gray-900">{trackEvidenceMatrix.length}</div><div className="mt-1 text-xs text-gray-600">论文评测 / Agent / 医学 RAG</div></div>
        <div className="border rounded-lg bg-white p-4"><div className="text-[11px] font-mono text-gray-500">来源条目</div><div className="mt-2 text-2xl font-semibold text-gray-900">{fileCount}</div><div className="mt-1 text-xs text-gray-600">报告、数据、API 与复现路径</div></div>
        <div className="border rounded-lg bg-white p-4"><div className="text-[11px] font-mono text-gray-500">引用体量</div><div className="mt-2 text-2xl font-semibold text-gray-900">{sizeText(totalKb)}</div><div className="mt-1 text-xs text-gray-600">公开索引体量，不代表完整私有语料</div></div>
      </div>
      <div className="space-y-5">
        {trackEvidenceMatrix.map(track => (
          <article key={track.track} className="border rounded-lg bg-white overflow-hidden">
            <div className="p-5 border-b bg-gray-50 flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
              <div>
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-[11px] px-2 py-0.5 rounded-md bg-gray-900 text-white font-mono">{track.code}</span>
                  <span className="text-xs text-gray-600">{track.role}</span>
                </div>
                <h2 className="text-xl font-semibold text-gray-900">{track.title}</h2>
              </div>
              <div className="sm:text-right"><div className="text-2xl font-semibold text-gray-900">{track.sources.length}</div><div className="text-[11px] text-gray-500">份来源条目</div></div>
            </div>
            <div className="p-5 grid grid-cols-1 xl:grid-cols-[0.9fr_1.25fr] gap-6">
              <div className="space-y-5">
                <section>
                  <div className="text-[11px] font-mono tracking-wider text-gray-500 mb-2">已验证内容</div>
                  <div className="flex flex-wrap gap-2">
                    {track.effort.split(/[·]/).map(part => part.trim()).filter(Boolean).map(part => <span key={part} className="text-xs px-2 py-1 bg-gray-50 border border-gray-100 text-gray-700">{part}</span>)}
                  </div>
                </section>
                <section>
                  <div className="text-[11px] font-mono tracking-wider text-gray-500 mb-2">依据说明</div>
                  <p className="text-sm leading-6 text-gray-700">{track.scoring}</p>
                </section>
              </div>
              <section className="min-w-0">
                <div className="flex items-center justify-between gap-3 mb-2">
                  <div className="text-[11px] font-mono tracking-wider text-gray-500">来源文件 / API</div>
                  <div className="text-[11px] text-gray-500">点击查看验证方式</div>
                </div>
                <ul className="border-y border-gray-100">
                  {track.sources.map(([file, path, size]) => {
                    const key = `${track.track}:${path}`;
                    return (
                      <li key={key} className="border-b border-gray-100 last:border-b-0">
                        <button type="button" onClick={() => setExpanded(expanded === key ? '' : key)} className="w-full py-3 text-left grid grid-cols-1 sm:grid-cols-[minmax(0,1fr)_auto_auto] sm:items-center gap-2 sm:gap-3 hover:bg-gray-50 transition-colors">
                          <span className="min-w-0"><span className="block font-mono text-xs text-gray-800 truncate">{file}</span><span className="block text-[11px] text-gray-500 truncate">{path}</span></span>
                          <span className="font-mono text-[11px] text-gray-500 whitespace-nowrap">{sizeText(size)}</span>
                          <span className="text-[10px] px-2 py-0.5 border border-gray-200 bg-white text-gray-700 whitespace-nowrap">已验证</span>
                        </button>
                        {expanded === key && (
                          <div className="pb-3 pr-2 text-[11px] text-gray-600 leading-relaxed">
                            <div className="border-l-2 border-gray-200 pl-3 space-y-1">
                              <div className="grid grid-cols-[56px_minmax(0,1fr)] gap-2"><span className="text-gray-500">路径</span><span className="font-mono text-gray-700 break-all">{path}</span></div>
                              <div className="grid grid-cols-[56px_minmax(0,1fr)] gap-2"><span className="text-gray-500">验证</span><span className="font-mono text-gray-700 break-all">{path.startsWith('/api') ? `curl ${path.split(' · ')[0]}` : `打开公开报告或 DATA-TRACE 对应条目：${path}`}</span></div>
                            </div>
                          </div>
                        )}
                      </li>
                    );
                  })}
                </ul>
              </section>
            </div>
            <div className="px-5 py-4 border-t bg-gray-50 grid grid-cols-1 md:grid-cols-[minmax(0,1fr)_minmax(0,1.2fr)] gap-4">
              <div><div className="text-[11px] font-mono tracking-wider text-gray-500 mb-1">交付物</div><div className="font-mono text-xs text-gray-800 break-words">{track.deliverable}</div></div>
              <div><div className="text-[11px] font-mono tracking-wider text-gray-500 mb-1">公开报告路径</div><div className="font-mono text-xs text-gray-500 break-all">{track.report_path}</div></div>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}

export function MetricGrid({ health }) {
  const quota = health?.components?.quota || {};
  const backendDisconnected = Array.isArray(health?.issues) && health.issues.some(issue => String(issue).includes('API is not reachable'));
  const inactiveLabel = backendDisconnected ? '后端未连接' : '回放模式';
  const items = [
    ['运行模式', health?.profile === 'pure_cloud_demo' ? '在线展示' : (health?.profile || '在线展示')],
    ['MinerU', health?.components?.mineru_official_api?.available ? '已配置' : inactiveLabel],
    ['DeepSeek', health?.components?.deepseek_api?.available ? '已配置' : inactiveLabel],
    ['今日额度', `${quota.remaining ?? '-'}/${quota.limit ?? '-'}`],
  ];
  return (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-3">
      {items.map(([label, value]) => (
        <div key={label} className="rounded-lg border bg-gray-50 p-3">
          <div className="font-mono text-lg font-semibold text-gray-900">{value}</div>
          <div className="mt-1 text-[11px] text-gray-600">{label}</div>
        </div>
      ))}
    </div>
  );
}

export function Track1Card() {
  const [url, setUrl] = useState('');
  const [file, setFile] = useState(null);
  const [sourceText, setSourceText] = useState('');
  const [result, setResult] = useState(null);
  const [quiz, setQuiz] = useState([]);
  const [studentAnswer, setStudentAnswer] = useState('');
  const [grade, setGrade] = useState(null);
  const [loading, setLoading] = useState('');

  async function parseUrl(nextUrl = url) {
    const target = (nextUrl || '').trim();
    if (!target) {
      setResult({ error: '请粘贴公开 PDF URL，或点击“内置样例”。' });
      return;
    }
    setLoading('url');
    const res = await apiPost('/api/demo/mineru/url', { url: target }, { timeoutMs: 120000 });
    setResult(res.ok ? res.data : { error: res.error, data: res.data });
    setLoading('');
  }

  async function upload() {
    if (!file) {
      setResult({ error: '请选择公开 PDF 文件。' });
      return;
    }
    const form = new FormData();
    form.append('file', file);
    setLoading('upload');
    const res = await apiRequest('/api/demo/mineru/upload', { method: 'POST', body: form, timeoutMs: 240000 });
    const data = res.ok ? res.data : { error: res.error, data: res.data };
    setResult(data);
    if (res.ok && data?.markdown_preview) setSourceText(data.markdown_preview);
    setLoading('');
  }

  async function generateQuizFrom(textValue = sourceText) {
    const text = textValue.trim();
    if (text.length < 20) {
      setResult({ error: '请先完成解析，或粘贴至少 20 个字符的公开/脱敏解析文本。' });
      return null;
    }
    setLoading('quiz');
    const res = await apiPost('/api/demo/quiz/generate', {
      source_text: text,
      topic: '时滞系统稳定性、LMI 判据与保守性边界',
      count: 3,
    }, { timeoutMs: 120000 });
    const data = res.ok ? res.data : { error: res.error, data: res.data };
    setResult(data);
    setQuiz(data?.questions || []);
    setGrade(null);
    setLoading('');
    return data?.questions || null;
  }

  async function generateQuiz() {
    return generateQuizFrom(sourceText);
  }

  async function runMiniChain() {
    setSourceText(TRACK1_SAMPLE_SOURCE);
    setResult({ status: 'sample_loaded', markdown_preview: TRACK1_SAMPLE_SOURCE, markdown_chars: TRACK1_SAMPLE_SOURCE.length });
    const questions = await generateQuizFrom(TRACK1_SAMPLE_SOURCE);
    const first = questions?.[0];
    if (!first) return;
    const sampleAnswer = '该材料说明时滞系统稳定性可以通过 Lyapunov-Krasovskii 泛函和 LMI 可行性来验证。若存在正定矩阵和松弛变量满足 LMI，则在给定时滞上界和模型假设内可推出渐近稳定；但该结论不能自动覆盖未建模扰动、参数不确定性或超过时滞上界的情形。';
    setStudentAnswer(sampleAnswer);
    setLoading('grade');
    const res = await apiPost('/api/demo/quiz/grade', {
      question: first.question,
      expected_answer: first.expected_answer,
      rubric: first.rubric,
      student_answer: sampleAnswer,
      source_text: TRACK1_SAMPLE_SOURCE,
    }, { timeoutMs: 120000 });
    setGrade(res.ok ? res.data : { error: res.error, data: res.data });
    setLoading('');
  }

  async function gradeAnswer(question) {
    if (!question || !studentAnswer.trim()) {
      setGrade({ error: '请选择题目并填写作答内容。' });
      return;
    }
    setLoading('grade');
    const res = await apiPost('/api/demo/quiz/grade', {
      question: question.question,
      expected_answer: question.expected_answer,
      rubric: question.rubric,
      student_answer: studentAnswer,
      source_text: sourceText,
    }, { timeoutMs: 120000 });
    setGrade(res.ok ? res.data : { error: res.error, data: res.data });
    setLoading('');
  }

  const chainStatus = [
    ['1', '解析输入', sourceText || result?.markdown_preview ? 'done' : loading === 'url' || loading === 'upload' ? 'running' : 'pending'],
    ['2', '生成题目', quiz.length ? 'done' : loading === 'quiz' ? 'running' : 'pending'],
    ['3', '作答评分', grade ? 'done' : loading === 'grade' ? 'running' : 'pending'],
  ];
  const parseSteps = [
    { step: 1, label: '接收公开输入', status: sourceText || result ? 'done' : 'ready', note: 'URL / 上传 / 内置摘要' },
    { step: 2, label: 'MinerU 解析或摘要复用', status: result?.error ? 'failed' : result ? 'done' : 'ready', note: result?.markdown_preview ? 'Markdown 已就绪' : '等待解析文本' },
    { step: 3, label: '生成评测材料', status: quiz.length ? 'done' : loading === 'quiz' ? 'ready' : 'ready', note: '题目、参考答案、评分规则' },
  ];
  const inputStatus = sourceText || result?.markdown_preview ? 'done' : loading === 'url' || loading === 'upload' ? 'running' : 'pending';
  const parseStatus = result?.markdown_preview ? 'done' : result?.error ? 'failed' : loading === 'url' || loading === 'upload' ? 'running' : inputStatus;
  const scoreStatus = grade ? 'done' : loading === 'quiz' || loading === 'grade' ? 'running' : quiz.length ? 'ready' : 'pending';

  return (
    <section className="border rounded-lg bg-white overflow-hidden">
      <div className="p-5 border-b bg-gray-50 flex flex-col lg:flex-row lg:items-start lg:justify-between gap-4">
        <div>
          <div className="text-[11px] font-mono text-gray-500 mb-2">赛道一 / Sci-Align public replay</div>
          <h3 className="text-xl font-semibold text-gray-900">公开论文解析、出题与评分闭环</h3>
          <p className="mt-2 text-sm text-gray-600 max-w-3xl">对齐赛道一工作台：公开 PDF 或脱敏摘要进入解析文本，随后展示题目、参考答案、评分规则和评分结果。</p>
        </div>
        <button onClick={runMiniChain} disabled={Boolean(loading)} className="px-4 py-2 rounded bg-gray-900 text-white text-xs disabled:opacity-50">
          <BusyLabel active={Boolean(loading)} busyText="处理中" idleText="载入公开闭环" />
        </button>
      </div>

      <div className="p-5 space-y-5">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
          {chainStatus.map(([idx, label, status]) => (
            <div key={label} className="rounded-lg border bg-gray-50 p-3">
              <div className="flex items-center justify-between gap-2">
                <span className="w-7 h-7 rounded-full bg-gray-900 text-white flex items-center justify-center text-xs font-bold">{idx}</span>
                <StatusPill status={status === 'done' ? 'done' : status === 'running' ? 'running' : 'pending'} />
              </div>
              <div className="mt-3 text-sm font-semibold text-gray-900">{label}</div>
              <div className="mt-1 text-xs text-gray-600">{status === 'done' ? '已完成' : status === 'running' ? '处理中' : '等待上一步'}</div>
            </div>
          ))}
        </div>

        <StepCard index="1" title="论文输入" desc="上传公开 PDF、提交公开 URL，或复用内置脱敏摘要。" status={inputStatus}>
          {(loading === 'url' || loading === 'upload') && (
            <WorkbenchLoadingCard
              className="mb-4"
              title={loading === 'upload' ? '正在上传公开 PDF' : '正在提交公开 URL'}
              desc="请求已进入云端代理；完成后会在解析区显示 Markdown 或任务状态。"
              steps={['提交输入', '调用服务端代理', '更新工作台']}
            />
          )}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
            <div className="rounded-lg border bg-gray-50 p-4">
              <div className="text-sm font-semibold text-gray-900">输入公开 PDF</div>
              <p className="mt-1 text-xs text-gray-500">URL 适合公开论文，上传限制由服务端控制；敏感材料不进入云端。</p>
              <label className="block text-[11px] text-gray-500 font-mono mt-4 mb-1">公开 PDF URL</label>
              <div className="flex flex-col md:flex-row gap-2">
                <input value={url} onChange={e => setUrl(e.target.value)} placeholder="粘贴公开 PDF URL" className="flex-1 border rounded px-3 py-2 text-sm" />
                <button onClick={() => parseUrl()} disabled={Boolean(loading)} className="px-4 py-2 rounded bg-gray-900 text-white text-xs disabled:opacity-50"><BusyLabel active={loading === 'url'} busyText="提交中" idleText="提交解析" /></button>
              </div>
              <button onClick={() => parseUrl(SAMPLE_PDF_URL)} disabled={Boolean(loading)} className="mt-2 px-3 py-1.5 rounded border text-gray-700 text-xs hover:bg-gray-50 disabled:opacity-50">使用 MinerU 公开样例 URL</button>
              <label className="block text-[11px] text-gray-500 font-mono mt-4 mb-1">或上传公开 PDF</label>
              <div className="flex flex-col md:flex-row gap-2">
                <input type="file" accept="application/pdf,.pdf" onChange={e => setFile(e.target.files?.[0] || null)} className="flex-1 border rounded px-3 py-2 text-sm" />
                <button onClick={upload} disabled={Boolean(loading)} className="px-4 py-2 rounded bg-gray-900 text-white text-xs disabled:opacity-50"><BusyLabel active={loading === 'upload'} busyText="上传中" idleText="上传解析" /></button>
              </div>
            </div>

            <div className="rounded-lg border bg-gray-50 p-4 lg:col-span-2">
              <div className="flex items-center justify-between gap-3">
                <div>
                  <div className="text-sm font-semibold text-gray-900">公开/脱敏解析文本</div>
              <p className="mt-1 text-xs text-gray-500">在线展示可直接使用内置摘要，保证出题评分闭环稳定。</p>
                </div>
                <button onClick={() => { setSourceText(TRACK1_SAMPLE_SOURCE); setResult({ status: 'sample_loaded', markdown_preview: TRACK1_SAMPLE_SOURCE, markdown_chars: TRACK1_SAMPLE_SOURCE.length }); }} className="px-3 py-1.5 rounded border text-xs text-gray-700 hover:bg-gray-50">填入内置摘要</button>
              </div>
              <label className="block text-[11px] text-gray-500 font-mono mt-4 mb-1">解析文本 / Markdown 摘要</label>
        <textarea
          value={sourceText}
          onChange={e => setSourceText(e.target.value)}
          rows={8}
          placeholder="上传解析完成后自动填入，也可以粘贴公开/脱敏摘要用于出题评分体验"
          className="w-full border rounded px-3 py-2 text-sm"
        />
              <div className="mt-2 flex flex-col md:flex-row gap-2">
                <button onClick={generateQuiz} disabled={Boolean(loading)} className="px-4 py-2 rounded bg-gray-900 text-white text-xs disabled:opacity-50"><BusyLabel active={loading === 'quiz'} busyText="出题中" idleText="API 出题" /></button>
                <input value={studentAnswer} onChange={e => setStudentAnswer(e.target.value)} placeholder="填写学生作答后点击某道题评分" className="flex-1 border rounded px-3 py-2 text-sm" />
              </div>
            </div>
          </div>
        </StepCard>

        <StepCard index="2" title="解析与结构化" desc="展示云端解析状态、Markdown 预览和与完整系统一致的解析流水线。" status={parseStatus}>
          <div className="space-y-3 mb-4">
            {parseSteps.map(item => <PipelineStep key={item.step} {...item} />)}
          </div>
          {result?.error && <ErrorCallout message={String(result.error)} hint="可改用内置摘要继续完成公开闭环体验。" />}
            {result && (
              <div className="overflow-hidden rounded-lg border bg-gray-50 p-4 text-xs text-gray-700">
                {result.markdown_preview ? (
                  <>
                    <div className="mb-2 font-semibold text-gray-900">Markdown 预览</div>
                    <MarkdownText className="max-h-80 overflow-auto rounded border bg-white p-3 text-xs [&_p]:text-xs [&_li]:text-xs [&_.katex]:text-[1em]">{result.markdown_preview}</MarkdownText>
                    <div className="mt-2 text-[11px] text-gray-500">解析字符数：{result.markdown_chars ?? '-'}</div>
                  </>
                ) : result.error ? (
                  <div className="text-red-700">{String(result.error)}</div>
                ) : (
                  <pre className="overflow-auto text-[11px] text-gray-700">{JSON.stringify(result, null, 2)}</pre>
                )}
              </div>
            )}
          {!result && <div className="text-xs text-gray-500">提交公开 PDF 或填入内置摘要后，这里会显示解析状态和 Markdown 预览。</div>}
        </StepCard>

        <StepCard
          index="3"
          title="出题与评分"
          desc="根据解析文本生成题目、参考答案和评分规则，并对作答进行评分。"
          status={scoreStatus}
          actions={<button onClick={runMiniChain} disabled={Boolean(loading)} className="px-3 py-1.5 rounded bg-gray-900 text-white text-xs disabled:opacity-50"><BusyLabel active={Boolean(loading)} busyText="处理中" idleText="载入闭环回放" /></button>}
        >
          {(loading === 'quiz' || loading === 'grade') && (
            <WorkbenchLoadingCard
              className="mb-4"
              title={loading === 'grade' ? '正在评分' : '正在生成题目'}
              desc="公开云端只处理公开/脱敏摘要，密钥不进入浏览器。"
              steps={loading === 'grade' ? ['读取题目', '载入评分结果', '汇总反馈'] : ['读取解析文本', '载入题目', '载入评分规则']}
            />
          )}
        {quiz.length > 0 && (
          <div className="space-y-2">
            <div className="text-sm font-semibold text-gray-900">生成题目</div>
            {quiz.map(q => (
              <div key={q.id || q.question} className="rounded border bg-gray-50 p-3 text-xs text-gray-700">
                <div className="font-semibold text-gray-900">{q.id || 'question'} · {q.type || '题目'}</div>
                <MarkdownText className="mt-1 text-xs [&_p]:text-xs [&_li]:text-xs [&_.katex]:text-[1em]">{q.question}</MarkdownText>
                {q.expected_answer && (
                  <div className="mt-2 rounded border bg-white px-3 py-2">
                    <div className="mb-1 text-[11px] font-semibold text-gray-500">参考答案</div>
                    <MarkdownText className="text-xs [&_p]:text-xs [&_li]:text-xs [&_.katex]:text-[1em]">{q.expected_answer}</MarkdownText>
                  </div>
                )}
                <div className="mt-2 rounded border bg-white px-3 py-2">
                  <div className="mb-1 text-[11px] font-semibold text-gray-500">评分规则</div>
                  <MarkdownText className="text-xs [&_p]:text-xs [&_li]:text-xs [&_.katex]:text-[1em]">{q.rubric}</MarkdownText>
                </div>
                <button onClick={() => gradeAnswer(q)} disabled={Boolean(loading)} className="mt-2 px-3 py-1.5 rounded border bg-white hover:bg-gray-100 disabled:opacity-50"><BusyLabel active={loading === 'grade'} busyText="评分中" idleText="API 评分" /></button>
              </div>
            ))}
          </div>
        )}
        {grade && (
          <div className="rounded-lg border bg-white p-4 text-xs text-gray-700">
            <div className="font-semibold text-gray-900">评分结果：{grade.score ?? '-'} / {grade.max_score ?? 10}</div>
            {grade.feedback && <MarkdownText className="mt-2 text-xs [&_p]:text-xs [&_li]:text-xs [&_.katex]:text-[1em]">{grade.feedback}</MarkdownText>}
            {Array.isArray(grade.rubric_hits) && grade.rubric_hits.length > 0 && <div className="mt-2 text-[11px] text-gray-500">命中项：{grade.rubric_hits.join(' · ')}</div>}
          </div>
        )}
            {!result && !quiz.length && !grade && (
              <div className="rounded-lg border bg-gray-50 p-5 text-sm text-gray-600">
                运行“公开最小闭环”后，这里会展示 Markdown 解析预览、生成题目、参考答案、评分规则和评分结果。
              </div>
            )}
        </StepCard>
      </div>
    </section>
  );
}

const track2ReplayCases = [
  {
    id: 'quick-proof',
    label: 'Quick Proof 飞轮',
    goal: 'arXiv PDF → MinerU Markdown → ABCD 快速题集 → 已保存评测结果',
    summary: '公开论文进入最小飞轮，复用已验证解析产物，生成 A/B/C/D 各 1 题并写入快速评测结果。',
    metrics: [['391s', '飞轮闭环'], ['4', 'ABCD 题型'], ['0', '失败步骤'], ['DATA-TRACE', '来源记录']],
    dag: ['检查公开 PDF', '复用 MinerU Markdown', '生成 ABCD 题集', '执行快速评测', '写入 DATA-TRACE'],
    logs: ['[OK] arXiv PDF 可访问', '[OK] MinerU Markdown 已存在', '[OK] ABCD quick questions generated', '[OK] quick eval saved'],
    artifacts: ['docs/submissions/data_trace_bundle/manifest.json', 'benchmark/dataset/core.json', 'docs/submissions/track2_agent_report.md'],
  },
  {
    id: 'visual-audit',
    label: '跨模态审计',
    goal: '公式、图片、表格和正文统一进入视觉质量核验',
    summary: 'Agent 将跨模态检查拆成图片描述、表格结构、公式保真和来源路径四类子任务。',
    metrics: [['9,207', '视觉审计判决'], ['4', '审计通道'], ['17', '跨领域模块'], ['62ms', '故障降级']],
    dag: ['读取图文产物', '生成视觉描述', '校验公式/表格', '记录失败降级', '汇总审计报告'],
    logs: ['[OK] visual descriptions loaded', '[OK] table/formula checks replayed', '[OK] fallback policy applied', '[OK] audit summary linked'],
    artifacts: ['docs/submissions/data_trace_bundle/05_cross_modal/cross_modal_audit_summary.json', 'docs/submissions/data_trace_bundle/06_medical_vision/'],
  },
];

export function Track2Card() {
  const [active, setActive] = useState(track2ReplayCases[0]);
  return (
    <section className="border rounded-lg bg-white overflow-hidden">
      <div className="p-5 border-b bg-gray-50">
        <div className="text-[11px] font-mono text-gray-500 mb-2">赛道二 / Data Agent 产物回放</div>
        <h3 className="text-xl font-semibold text-gray-900">Data Agent 产物回放</h3>
        <p className="mt-2 text-sm text-gray-600 max-w-3xl">对齐赛道二页面：展示任务目标、DAG、日志、指标和来源产物。在线版本不执行长任务，只回放已验证产物。</p>
      </div>
      <div className="p-5 space-y-5">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {track2ReplayCases.map(item => (
            <button key={item.id} type="button" onClick={() => setActive(item)} className={`rounded-lg border p-4 text-left transition ${active.id === item.id ? 'bg-gray-900 text-white border-gray-900' : 'bg-gray-50 text-gray-700 hover:bg-white'}`}>
              <div className="text-sm font-semibold">{item.label}</div>
              <div className={`mt-2 text-xs leading-5 ${active.id === item.id ? 'text-gray-200' : 'text-gray-600'}`}>{item.goal}</div>
            </button>
          ))}
        </div>

        <div className="grid grid-cols-1 xl:grid-cols-[0.9fr_1.1fr] gap-5">
          <div className="space-y-4">
            <div className="rounded-lg border bg-white p-4">
              <div className="text-sm font-semibold text-gray-900">执行摘要</div>
              <p className="mt-2 text-sm leading-7 text-gray-700">{active.summary}</p>
              <div className="mt-4 grid grid-cols-2 gap-2">
                {active.metrics.map(([value, label]) => (
                  <div key={label} className="rounded border bg-gray-50 px-3 py-3">
                    <div className="font-mono text-lg font-semibold text-gray-900">{value}</div>
                    <div className="mt-1 text-[11px] text-gray-500">{label}</div>
                  </div>
                ))}
              </div>
            </div>
            <div className="rounded-lg border bg-white p-4">
              <div className="text-sm font-semibold text-gray-900">来源产物</div>
              <div className="mt-3 space-y-2">
                {active.artifacts.map(path => <div key={path} className="rounded border bg-gray-50 px-3 py-2 font-mono text-[11px] text-gray-700 break-all">{path}</div>)}
              </div>
            </div>
          </div>
          <div className="space-y-4">
            <div className="rounded-lg border bg-white p-4">
              <div className="text-sm font-semibold text-gray-900">DAG 回放</div>
              <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-2">
                {active.dag.map((step, index) => (
                  <div key={step} className="rounded border bg-gray-50 p-3 text-xs text-gray-700">
                    <span className="mr-2 font-mono text-gray-400">{index + 1}</span>{step}
                  </div>
                ))}
              </div>
            </div>
            <div className="rounded-lg border bg-white p-4">
              <div className="text-sm font-semibold text-gray-900">执行日志</div>
              <div className="mt-3 rounded bg-gray-950 p-3 font-mono text-[11px] leading-6 text-gray-100">
                {active.logs.map(line => <div key={line}>{line}</div>)}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

const medicalReplayCases = [
  {
    id: 'closed-loop-48m',
    label: '闭环胰岛素机制解释',
    question: '为什么 1 型糖尿病诊断后 48 个月内胰岛素需求会上升，自适应闭环有什么意义？',
    answer: '机制解释：公开来源显示，新诊断 1 型糖尿病儿童和青少年在诊断后 48 个月内每日胰岛素需求明显上升，闭环算法输送的胰岛素比例也随时间增加。因此，这个案例支持的是“自适应系统能跟随需求变化调整输送”的机制，而不是“给出某个固定剂量”。安全性需要看低于目标血糖范围时间、严重低血糖等终点，并且只能解释群体层面的研究结论。\n\n边界：这不是个人治疗、处方或急诊判断。',
    claimStatus: 'supported',
    sources: [
      {
        id: 'pmc-t1d-closed-loop-48m-01',
        title: 'Adaptive closed-loop insulin delivery after diagnosis in children and adolescents',
        zh: '新诊断 1 型糖尿病儿童和青少年在诊断后 48 个月内每日胰岛素需求明显上升；闭环算法输送的胰岛素比例也随时间增加，说明自适应闭环系统的意义在于跟随需求变化调整输送，而不是给出固定剂量。',
      },
      {
        id: 'pmc-t1d-hypoglycaemia-02',
        title: 'Closed-loop therapy and hypoglycaemia safety endpoints',
        zh: '闭环治疗研究通常把低于目标血糖范围时间和严重低血糖作为安全性终点。文献层面的安全性结论只能说明群体趋势，不能替代个体剂量调整或设备处方。',
      },
    ],
  },
  {
    id: 'itt-survival',
    label: 'ITT 与生存获益',
    question: 'ITT 分析人群为什么会影响生存获益判断？',
    answer: '机制解释：ITT 分析保留原始随机分组，能减少因退出、换组或治疗依从性差异带来的选择偏倚。因此，当问题是“生存获益是否成立”时，不能只看完成治疗人群，还要看随机化人群、删失规则、随访定义和缺失数据。\n\n边界：这个回答只说明文献统计方法的适用边界，不推断具体患者预后。',
    claimStatus: 'supported',
    sources: [
      {
        id: 'pmc-survival-itt-04',
        title: 'Intention-to-treat population and survival endpoints',
        zh: 'ITT 分析保留原始随机分组，常用于主要疗效分析。生存获益判断需要同时说明删失规则、随访定义以及缺失数据处理。',
      },
    ],
  },
  {
    id: 'eligibility',
    label: '纳入排除与外推',
    question: '纳入排除标准为什么会限制临床试验结论外推？',
    answer: '机制解释：纳入排除标准决定研究结论最直接适用的人群。严格标准能降低混杂、保护受试者，但也会让试验人群和真实世界患者产生差距，所以外推结论时必须说明哪些人群没有被研究覆盖。\n\n边界：这个回答只讨论研究设计边界，不判断个体是否应入组或接受治疗。',
    claimStatus: 'supported',
    sources: [
      {
        id: 'pmc-inclusion-exclusion-05',
        title: 'Eligibility criteria in clinical trials',
        zh: '纳入排除标准决定研究结论最直接适用的人群。它既保护受试者并减少混杂，也会限制结论向真实世界患者外推。',
      },
    ],
  },
];

export function Track3Card() {
  const [result, setResult] = useState({ ...medicalReplayCases[0], provider: 'trace_replay' });

  function replay(caseItem) {
    setResult({ ...caseItem, provider: 'trace_replay' });
  }

  return (
    <section className="border rounded-lg bg-white overflow-hidden">
      <div className="p-5 border-b bg-gray-50">
        <div className="text-[11px] font-mono text-gray-500 mb-2">赛道三 / 医学 RAG trace</div>
        <h3 className="text-xl font-semibold text-gray-900">医学 RAG 来源回放</h3>
        <p className="mt-2 text-sm text-gray-600 max-w-3xl">对齐 Ask 页：只展示已验证案例的来源、回答、结论状态和安全边界；云端不开放自定义医学问诊。</p>
      </div>
      <div className="p-5 space-y-5">
        <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-2">
          {medicalReplayCases.map(item => (
            <button key={item.id} type="button" onClick={() => replay(item)} className="rounded border bg-gray-50 px-3 py-2 text-left text-xs text-gray-700 hover:bg-white">
              <span className="block font-semibold text-gray-900">{item.label}</span>
              <span className="mt-1 block">{item.question}</span>
            </button>
          ))}
        </div>
        {result && (
          <div className="grid grid-cols-1 xl:grid-cols-[1fr_0.9fr] gap-5">
            <div className="space-y-3">
              <div className="rounded-lg border bg-white p-4">
                <div className="text-[11px] font-mono text-gray-500">用户问题</div>
                <div className="mt-2 text-sm font-semibold text-gray-900">{result.question}</div>
              </div>
              <div className="rounded-lg border bg-gray-50 p-4">
                <div className="mb-2 text-sm font-semibold text-gray-900">回答回放</div>
                <MarkdownText>{result.answer || result.error}</MarkdownText>
              </div>
              <div className="rounded-lg border bg-amber-50 p-3 text-xs leading-6 text-amber-900">
                安全边界：该页面只回放公开/脱敏文献问答，不处理患者资料、个人诊断、处方或急症判断。
              </div>
            </div>
            <div className="space-y-3">
              <div className="rounded-lg border bg-white p-4">
                <div className="flex items-center justify-between gap-2">
                  <div className="text-sm font-semibold text-gray-900">结论状态</div>
                  <StatusPill status="validated" label={result.claimStatus || result.claim_status || 'supported'} />
                </div>
                <div className="mt-2 text-[11px] text-gray-500">来源模式：{result.provider === 'trace_replay' ? 'trace 回放' : (result.provider || 'trace 回放')}</div>
              </div>
              {Array.isArray(result.sources || result.retrieved_sources) && (result.sources || result.retrieved_sources).length > 0 && (
                <div className="space-y-2">
                  <div className="text-sm font-semibold text-gray-900">来源卡片</div>
                {(result.sources || result.retrieved_sources).map(source => (
                  <div key={source.id} className="rounded border bg-white p-3 text-xs text-gray-600">
                    <div className="font-mono text-[11px] text-gray-500">{source.id}</div>
                    <div className="mt-1 font-semibold text-gray-900">{source.title}</div>
                    <MarkdownText className="mt-1 text-xs [&_p]:text-xs [&_li]:text-xs [&_.katex]:text-[1em]">{source.zh}</MarkdownText>
                  </div>
                ))}
                </div>
              )}
              <div className="rounded-lg border bg-white p-4">
                <div className="text-sm font-semibold text-gray-900">RAG trace 链路</div>
                <div className="mt-3 grid grid-cols-1 gap-2 text-xs text-gray-700">
                  {['问题改写', '混合检索', '来源组织', '结论校验', '安全边界'].map((step, i) => (
                    <div key={step} className="rounded border bg-gray-50 px-3 py-2"><span className="mr-2 font-mono text-gray-400">{i + 1}</span>{step}</div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </section>
  );
}

export function AcceptanceCard({ runtime, health, tracks }) {
  const parserLabels = {
    mineru_official: 'MinerU 官方 API',
  };
  const checks = [
    `运行模式：${runtime?.mode === 'pure_cloud_only' ? '在线展示模式' : (runtime?.mode || '在线展示模式')}`,
    `私有资产入口：关闭`,
    `解析后端：${(runtime?.parser_backends || []).map(x => parserLabels[x.id] || x.label || x.id).join('、') || 'MinerU 官方 API'}`,
    `赛道数量：${tracks?.tracks?.length ?? 3}`,
    `上传限制：${health?.limits?.upload_max_mb ?? 20}MB`,
    '密钥只在服务端环境变量读取',
  ];
  return (
    <section className="border rounded-lg p-5 bg-white">
      <h2 className="text-sm font-semibold text-gray-800 mb-2">展示链路</h2>
      <p className="text-xs text-gray-500 mb-3">查看在线展示、运行策略、后端 API 与公开交付物之间的对应关系。</p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
        {checks.map(item => <div key={item} className="rounded border bg-gray-50 px-3 py-2 text-[11px] text-gray-700">{item}</div>)}
      </div>
      <div className="mt-3 grid grid-cols-1 md:grid-cols-4 gap-2">
        {['公开解析体验', '出题评分体验', '规划流程展示', 'RAG 来源回放'].map(item => (
          <div key={item} className="rounded border bg-green-50 px-3 py-2 text-[11px] text-green-700">{item}</div>
        ))}
      </div>
    </section>
  );
}

export async function loadCloudState() {
  const [healthRes, runtimeRes, tracksRes] = await Promise.all([
    apiGet('/api/demo/health', { timeoutMs: 15000 }),
    apiGet('/api/demo/runtime/options', { timeoutMs: 15000 }),
    apiGet('/api/demo/tracks', { timeoutMs: 15000 }),
  ]);
  return {
    health: healthRes.ok ? healthRes.data : null,
    runtime: runtimeRes.ok ? runtimeRes.data : null,
    tracks: tracksRes.ok ? tracksRes.data : null,
  };
}
