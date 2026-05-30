import { useEffect, useMemo, useState } from 'react';
import SectionWrapper from '../components/SectionWrapper';
import { apiGet } from '../lib/apiClient';

const trackStyles = {
  Track1: {
    code: 'T1',
    role: 'Scientific alignment benchmark',
  },
  Track2: {
    code: 'T2',
    role: 'Agent workflow and data flywheel',
  },
  Track3: {
    code: 'T3',
    role: 'Local-first medical evidence RAG',
  },
};

function formatSize(sizeKb) {
  if (sizeKb === undefined || sizeKb === null) return 'Unknown';
  if (sizeKb >= 1024) return `${(sizeKb / 1024).toFixed(1)} MB`;
  return `${sizeKb} KB`;
}

function effortParts(text = '') {
  return text.split(/[·]/).map(part => part.trim()).filter(Boolean);
}

function LoadingState() {
  return (
    <div className="border rounded-lg border-gray-200 bg-white p-6">
      <div className="h-4 w-36 bg-gray-100 rounded mb-5" />
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
        {[0, 1, 2].map(i => (
          <div key={i} className="border-t-2 border-gray-200 pt-4">
            <div className="h-5 w-24 bg-gray-100 rounded mb-4" />
            <div className="space-y-2">
              <div className="h-3 bg-gray-100 rounded" />
              <div className="h-3 bg-gray-100 rounded w-5/6" />
              <div className="h-3 bg-gray-100 rounded w-2/3" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function EvidenceRow({ item, expanded, onToggle }) {
  return (
    <li className="border-b border-gray-100 last:border-b-0">
      <button
        type="button"
        onClick={onToggle}
        className="w-full py-3 text-left grid grid-cols-1 sm:grid-cols-[minmax(0,1fr)_auto_auto] sm:items-center gap-2 sm:gap-3 hover:bg-gray-50 transition-colors"
      >
        <span className="min-w-0">
          <span className="block font-mono text-xs text-gray-800 truncate">{item.file}</span>
          <span className="block text-[11px] text-gray-500 truncate">{item.path}</span>
        </span>
        <div className="flex items-center gap-2 sm:contents">
          <span className="font-mono text-[11px] text-gray-500 whitespace-nowrap">{formatSize(item.size_kb)}</span>
          <span className="text-[10px] px-2 py-0.5 border border-gray-200 bg-white text-gray-700 whitespace-nowrap">
            已验证
          </span>
        </div>
      </button>

      {expanded && (
        <div className="pb-3 pr-2 text-[11px] text-gray-600 leading-relaxed">
          <div className="border-l-2 border-gray-200 pl-3 space-y-1">
            <div className="grid grid-cols-[56px_minmax(0,1fr)] gap-2">
              <span className="text-gray-500">路径</span>
              <span className="font-mono text-gray-700 break-all">{item.path}</span>
            </div>
            <div className="grid grid-cols-[56px_minmax(0,1fr)] gap-2">
              <span className="text-gray-500">验证</span>
              <span className="font-mono text-gray-700 break-all">Get-Content {item.path}</span>
            </div>
          </div>
        </div>
      )}
    </li>
  );
}

function TrackPanel({ track, expanded, setExpanded }) {
  const style = trackStyles[track.track] || trackStyles.Track1;
  const parts = effortParts(track.effort);
  const evidence = track.evidence || [];

  return (
    <article className="border rounded-lg bg-white overflow-hidden">
      <div className="p-5 border-b bg-gray-50">
        <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
          <div className="min-w-0">
            <div className="flex items-center gap-2 mb-2">
              <span className="text-[11px] px-2 py-0.5 rounded-md bg-gray-900 text-white font-mono">{style.code}</span>
              <span className="text-xs text-gray-600">{style.role}</span>
            </div>
            <h2 className="text-xl font-semibold text-gray-900">{track.title}</h2>
          </div>
          <div className="sm:text-right">
            <div className="text-2xl font-semibold text-gray-900">{evidence.length}</div>
            <div className="text-[11px] text-gray-500">份来源文件</div>
          </div>
        </div>
      </div>

      <div className="p-5 grid grid-cols-1 xl:grid-cols-[0.9fr_1.25fr] gap-6">
        <div className="space-y-5">
          <section>
            <div className="text-[11px] font-mono tracking-wider text-gray-500 mb-2">已验证内容</div>
            <div className="flex flex-wrap gap-2">
              {parts.map(part => (
                <span key={part} className="text-xs px-2 py-1 bg-gray-50 border border-gray-100 text-gray-700">
                  {part}
                </span>
              ))}
            </div>
          </section>

          <section>
            <div className="text-[11px] font-mono tracking-wider text-gray-500 mb-2">评分依据</div>
            <p className="text-sm leading-6 text-gray-700">{track.scoring}</p>
          </section>
        </div>

        <section className="min-w-0">
          <div className="flex items-center justify-between gap-3 mb-2">
            <div className="text-[11px] font-mono tracking-wider text-gray-500">来源文件</div>
            <div className="text-[11px] text-gray-500">点击文件行查看验证详情</div>
          </div>
          <ul className="border-y border-gray-100">
            {evidence.map(item => (
              <EvidenceRow
                key={item.path}
                item={item}
                expanded={expanded === item.path}
                onToggle={() => setExpanded(expanded === item.path ? null : item.path)}
              />
            ))}
          </ul>
        </section>
      </div>

      <div className="px-5 py-4 border-t bg-gray-50 grid grid-cols-1 md:grid-cols-[minmax(0,1fr)_minmax(0,1.2fr)] gap-4">
        <div>
          <div className="text-[11px] font-mono tracking-wider text-gray-500 mb-1">交付物</div>
          <div className="font-mono text-xs text-gray-800 break-words">{track.deliverable}</div>
        </div>
        <div>
          <div className="text-[11px] font-mono tracking-wider text-gray-500 mb-1">公开报告路径</div>
          <div className="font-mono text-xs text-gray-500 break-all">{track.report_path}</div>
        </div>
      </div>
    </article>
  );
}

export default function EvidencePage({ initialMatrix = null, initialError = '' }) {
  const [matrix, setMatrix] = useState(initialMatrix);
  const [error, setError] = useState(initialError);
  const [expanded, setExpanded] = useState(null);

  async function loadMatrix() {
    setError('');
    const result = await apiGet('/api/demo/evidence/matrix', { timeoutMs: 15000 });
    if (result.ok) {
      setMatrix(result.data);
    } else {
      setError(result.error || '来源矩阵加载失败');
    }
  }

  useEffect(() => {
    if (!initialMatrix) loadMatrix();
  }, [initialMatrix]);

  const summary = useMemo(() => {
    const tracks = matrix?.tracks || [];
    const fileCount = tracks.reduce((sum, track) => sum + (track.evidence || []).length, 0);
    const totalKb = tracks.reduce(
      (sum, track) => sum + (track.evidence || []).reduce((inner, item) => inner + (item.size_kb || 0), 0),
      0
    );
    return { tracks: tracks.length, fileCount, totalKb };
  }, [matrix]);

  return (
    <SectionWrapper className="py-12 sm:py-14">
      <div className="custom-screen space-y-6">
        <header className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-5">
          <div className="max-w-3xl">
            <div className="text-xs font-mono text-gray-500 mb-3">数据追溯台</div>
            <h1 className="text-gray-900 text-3xl font-semibold sm:text-4xl mb-3">来源矩阵</h1>
            <p className="text-gray-600 text-sm leading-7">
              三条赛道的核心来源、评分理由和公开交付物集中在一屏。默认展示结论级信息，展开文件行查看可验证路径。
            </p>
          </div>
          <button
            type="button"
            onClick={loadMatrix}
            className="self-start lg:self-auto px-4 py-2 border rounded bg-white text-xs text-gray-700 hover:bg-gray-50"
          >
            刷新来源
          </button>
        </header>

        <section className="grid grid-cols-1 md:grid-cols-3 gap-3">
          <div className="border rounded-lg bg-white p-4">
            <div className="text-[11px] font-mono tracking-wider text-gray-500">赛道数量</div>
            <div className="mt-2 text-2xl font-semibold text-gray-900">{summary.tracks || '--'}</div>
            <div className="mt-1 text-xs text-gray-600 leading-relaxed">论文评测 / Agent / Medical RAG</div>
          </div>
          <div className="border rounded-lg bg-white p-4">
            <div className="text-[11px] font-mono tracking-wider text-gray-500">来源文件</div>
            <div className="mt-2 text-2xl font-semibold text-gray-900">{summary.fileCount || '--'}</div>
            <div className="mt-1 text-xs text-gray-600 leading-relaxed">全部列为本地可验证产物</div>
          </div>
          <div className="border rounded-lg bg-white p-4">
            <div className="text-[11px] font-mono tracking-wider text-gray-500">引用体量</div>
            <div className="mt-2 text-2xl font-semibold text-gray-900">
              {summary.totalKb ? formatSize(summary.totalKb) : '--'}
            </div>
            <div className="mt-1 text-xs text-gray-600 leading-relaxed">来源索引体量，非完整语料库大小</div>
          </div>
        </section>

        {error && (
          <div className="border border-red-200 bg-red-50 p-4 text-sm text-red-700">
            来源矩阵加载失败：{error}
          </div>
        )}

        {!matrix && !error && <LoadingState />}

        <div className="space-y-5">
          {matrix?.tracks?.map(track => (
            <TrackPanel key={track.track} track={track} expanded={expanded} setExpanded={setExpanded} />
          ))}
        </div>
      </div>
    </SectionWrapper>
  );
}

export async function getServerSideProps() {
  try {
    const backend = process.env.CONTROLMIND_BACKEND_URL || 'http://127.0.0.1:17001';
    const response = await fetch(`${backend}/api/demo/evidence/matrix`);
    if (!response.ok) {
      return { props: { initialMatrix: null, initialError: `HTTP ${response.status}` } };
    }
    return { props: { initialMatrix: await response.json(), initialError: '' } };
  } catch (error) {
    return { props: { initialMatrix: null, initialError: error.message || '来源矩阵加载失败' } };
  }
}
