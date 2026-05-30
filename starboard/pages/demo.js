import Link from 'next/link';
import SectionWrapper from '../components/SectionWrapper';

const steps = [
  { id: 1, label: '系统依赖', desc: '确认 FastAPI、MinerU、Ollama、索引与来源文件状态', href: '/health' },
  { id: 2, label: 'Track1：论文到评测', desc: '选择样例或上传 PDF，验证解析、出题与评分链路', href: '/track1' },
  { id: 3, label: 'Track2：Agent 工作流', desc: '输入任务目标，查看 intent、DAG 与资源调度', href: '/track2' },
  { id: 4, label: 'Track3：Medical RAG', desc: '输入临床文献问题，验证检索 chunk、引用回答与结论校验', href: '/track3' },
  { id: 5, label: '来源矩阵', desc: '查看努力、来源、依据说明与交付物之间的对应关系', href: '/evidence' },
];

const cliCommands = [
  'conda run --no-capture-output -n myenv python demo/cli/controlscidemo track1 --quick',
  'conda run --no-capture-output -n myenv python demo/cli/controlscidemo track2 --quick',
  'conda run --no-capture-output -n myenv python demo/cli/controlscidemo track3 --quick',
  'conda run --no-capture-output -n myenv python demo/cli/controlscidemo all --quick',
];

export default function DemoPage() {
  return (
    <SectionWrapper>
      <div className="custom-screen space-y-6">
        <div>
          <h1 className="text-gray-800 text-3xl font-semibold sm:text-4xl mb-2">工作台导览</h1>
          <p className="text-gray-500 text-sm">按顺序点击即可完整验证三赛道能力，也可以跳转到任一页面独立复现。</p>
        </div>

        <div className="space-y-3">
          {steps.map(s => (
            <Link key={s.id} href={s.href} className="border rounded-lg p-5 bg-white hover:shadow-md transition-shadow flex items-start gap-4">
              <span className="w-8 h-8 rounded-full bg-gray-900 text-white flex items-center justify-center text-sm font-bold flex-shrink-0">{s.id}</span>
              <div>
                <h3 className="font-semibold text-gray-800">{s.label}</h3>
                <p className="text-xs text-gray-500 mt-1">{s.desc}</p>
              </div>
              <span className="ml-auto text-gray-300">→</span>
            </Link>
          ))}
        </div>

        <div className="border rounded-lg p-5 bg-gray-50 text-sm text-gray-600 space-y-2">
          <p><strong className="text-gray-800">验证原则：</strong>先看依赖状态，再进三赛道，最后用来源矩阵确认每个结论都有产物支撑。</p>
          <p>完整系统可执行短链路；GPU、索引重建和批量评测等长任务以已验证产物复现，并明确标注降级原因。</p>
        </div>

        <div className="border rounded-lg p-5 bg-white">
          <h2 className="text-sm font-semibold text-gray-800 mb-2">CLI 复现基线</h2>
          <p className="text-xs text-gray-500 mb-3">前端工作台负责串联和展示；demo CLI 负责给出不依赖浏览器的三赛道标准库复现入口。</p>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
            {cliCommands.map(cmd => (
              <code key={cmd} className="block border rounded bg-gray-50 px-3 py-2 text-[11px] text-gray-700">{cmd}</code>
            ))}
          </div>
        </div>
      </div>
    </SectionWrapper>
  );
}
