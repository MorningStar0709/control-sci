import Link from 'next/link';
import { useRouter } from 'next/router';

const navGroups = [
  {
    title: '工作台',
    items: [
      { href: '/home', label: '总览', desc: '项目能力地图', icon: 'overview' },
      { href: '/demo', label: '工作台导览', desc: '三赛道导览', icon: 'route' },
    ],
  },
  {
    title: '三赛道',
    items: [
      { href: '/track1', label: '论文评测', desc: '解析 · 出题 · 评分', icon: 'document' },
      { href: '/track2', label: 'Agent 工作流', desc: '意图 · DAG · 调度', icon: 'workflow' },
      { href: '/track3', label: 'Medical RAG', desc: '检索 · chunk · 合成', icon: 'search' },
      { href: '/ask', label: '医学问答', desc: '用户提问 · 引用回答', icon: 'chat' },
    ],
  },
  {
    title: '核验',
    items: [
      { href: '/evidence', label: '来源矩阵', desc: '评分理由与产物', icon: 'evidence' },
      { href: '/health', label: '系统依赖', desc: '服务与索引状态', icon: 'health' },
    ],
  },
];

function NavIcon({ name }) {
  const common = {
    className: 'w-4 h-4',
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    strokeWidth: '1.8',
    strokeLinecap: 'round',
    strokeLinejoin: 'round',
    'aria-hidden': 'true',
  };

  const icons = {
    overview: (
      <svg {...common}>
        <rect x="4" y="4" width="7" height="7" rx="1.5" />
        <rect x="13" y="4" width="7" height="7" rx="1.5" />
        <rect x="4" y="13" width="7" height="7" rx="1.5" />
        <path d="M14 16h5M14 20h5" />
      </svg>
    ),
    route: (
      <svg {...common}>
        <circle cx="6" cy="6" r="2" />
        <circle cx="18" cy="18" r="2" />
        <path d="M8 6h5a3 3 0 0 1 0 6h-2a3 3 0 0 0 0 6h5" />
      </svg>
    ),
    document: (
      <svg {...common}>
        <path d="M7 3h7l4 4v14H7z" />
        <path d="M14 3v5h5M9 13h6M9 17h6" />
      </svg>
    ),
    workflow: (
      <svg {...common}>
        <rect x="4" y="4" width="6" height="6" rx="1.5" />
        <rect x="14" y="14" width="6" height="6" rx="1.5" />
        <path d="M10 7h4a3 3 0 0 1 3 3v4M7 10v4a3 3 0 0 0 3 3h4" />
      </svg>
    ),
    search: (
      <svg {...common}>
        <circle cx="11" cy="11" r="6" />
        <path d="M16 16l4 4M8 11h6" />
      </svg>
    ),
    evidence: (
      <svg {...common}>
        <path d="M5 4h14v16H5z" />
        <path d="M8 8h8M8 12h8M8 16h5" />
      </svg>
    ),
    health: (
      <svg {...common}>
        <path d="M12 3l7 3v5c0 4.8-2.9 8.1-7 10-4.1-1.9-7-5.2-7-10V6z" />
        <path d="M9 12h6M12 9v6" />
      </svg>
    ),
    chat: (
      <svg {...common}>
        <path d="M5 5h14v10H8l-3 3z" />
        <path d="M8 9h8M8 12h5" />
      </svg>
    ),
  };

  return icons[name] || icons.overview;
}

export default function Sidebar() {
  const router = useRouter();

  return (
    <aside className="w-52 border-r bg-gray-50 flex-shrink-0 flex flex-col min-h-[calc(100vh-3rem)]">
      <nav className="flex-1 py-5 px-2 space-y-5">
        {navGroups.map(group => (
          <div key={group.title}>
            <div className="px-3 mb-2 text-[11px] font-semibold text-gray-500 tracking-wider leading-snug">{group.title}</div>
            <div className="space-y-1">
              {group.items.map(item => {
                const active = router.pathname === item.href;
                return (
                  <Link key={item.href} href={item.href} className={`group flex items-center gap-3 px-3 py-2.5 rounded-lg transition-colors ${
                    active ? 'bg-gray-900 text-white shadow-sm' : 'text-gray-600 hover:bg-white hover:text-gray-900'
                  }`}>
                    <span className={`w-8 h-8 rounded-md flex items-center justify-center flex-shrink-0 ${
                      active ? 'bg-white text-gray-900' : 'bg-gray-200 text-gray-600 group-hover:bg-gray-100'
                    }`}>
                      <NavIcon name={item.icon} />
                    </span>
                    <span className="min-w-0">
                      <span className="block text-sm font-medium leading-tight truncate">{item.label}</span>
                      <span className={`block text-[11px] leading-snug mt-0.5 truncate ${active ? 'text-gray-200' : 'text-gray-500'}`}>{item.desc}</span>
                    </span>
                  </Link>
                );
              })}
            </div>
          </div>
        ))}
      </nav>
      <div className="px-4 py-3 border-t text-[11px] text-gray-500 bg-white leading-snug">
        <div className="font-mono text-gray-600">Local-first</div>
        <div>原文 / 医疗 / chunk 留本地</div>
      </div>
    </aside>
  );
}
