import { useCallback, useEffect, useMemo, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';
import SectionWrapper from '../components/SectionWrapper';
import ErrorCallout from '../components/workbench/ErrorCallout';
import EvidenceBadge from '../components/workbench/EvidenceBadge';
import RuntimeSummary from '../components/workbench/RuntimeSummary';
import StepCard from '../components/workbench/StepCard';
import StatusPill from '../components/workbench/StatusPill';
import { apiGet } from '../lib/apiClient';
import { findMedicalAskReplay } from '../lib/medicalAskReplay';
import useSessionState from '../lib/useSessionState';

const QUICK_PROOF_K = 3;
const DEFAULT_QUERY = '化疗剂量减少和治疗延迟的不良事件来源';

const modes = [
  { id: 'hybrid', label: '混合检索', desc: 'RRF 默认推荐' },
  { id: 'dense', label: '语义检索', desc: '向量' },
  { id: 'bm25', label: 'BM25', desc: '关键词' },
  { id: 'vision', label: '图文融合', desc: '图片+文本' },
];

const indexOptions = [
  { id: 'bge_m3', label: 'BGE M3', desc: '1024 维 · 强检索' },
  { id: 'qwen', label: '高维索引', desc: '2560 维 · 对照组' },
  { id: 'bge_small', label: 'BGE Small', desc: '384 维 · 轻量' },
];

const useCases = [
  { label: '临床研究者', text: '终点、安全性、ITT 和纳排标准快速追溯', color: 'blue' },
  { label: '药企医学事务', text: '剂量调整、不良事件和治疗延迟来源核验', color: 'emerald' },
  { label: '受控医学资产', text: '原文、文段和问答上下文不进入在线展示版', color: 'purple' },
];

const promptGroups = [
  {
    title: '用户自然问题',
    desc: '面向正常医学文献用户，点击即载入已验证回放。',
    prompts: [
      { label: '闭环胰岛素低血糖', query: '闭环胰岛素低血糖来源', replay: true },
      { label: '化疗剂量调整', query: '化疗剂量减少和治疗延迟的不良事件来源', replay: true },
      { label: 'OS / PFS 边界', query: '总生存期和无进展生存期，是终点定义还是生存获益结论？', replay: true },
    ],
  },
  {
    title: '研究者验证',
    desc: '覆盖临床试验统计口径和方法学来源。',
    prompts: [
      { label: '主要终点与安全性', query: '主要终点和安全性来源', replay: true },
      { label: 'ITT 分析人群', query: '意向治疗分析人群的统计分析来源', replay: true },
      { label: '纳入排除标准', query: '随机对照试验的纳入排除标准', replay: true },
    ],
  },
  {
    title: '安全边界',
    desc: '展示个人诊疗或急症问题不会进入 RAG 检索。',
    prompts: [
      { label: '胸痛急症拒答', query: '胸痛并且呼吸困难怎么办', replay: true, safety: true },
      { label: '个人用药拒答', query: '发烧吃什么药', replay: true, safety: true },
    ],
  },
];

export default function Track3Page({ runtimeConfig }) {
  const defaultReplay = findMedicalAskReplay(DEFAULT_QUERY);
  const [session, setSession] = useSessionState('controlmind.track3.session.v2', {
    query: DEFAULT_QUERY,
    mode: 'hybrid',
    indexId: 'bge_m3',
    results: defaultReplay ? replayToSearchResults(defaultReplay) : null,
    synthesis: defaultReplay ? normalizeSynthesis(defaultReplay) : null,
    selectedPrompt: '化疗剂量调整',
  });
  const { query, mode, indexId, results, synthesis, selectedPrompt } = session;
  const patchSession = useCallback((patch) => setSession(prev => ({ ...prev, ...patch })), [setSession]);
  const [stats, setStats] = useState(null);
  const [qlora, setQlora] = useState(null);
  const [evalSummary, setEvalSummary] = useState(null);
  const [expanded, setExpanded] = useState(null);

  const replayForQuery = useMemo(() => findMedicalAskReplay(query), [query]);
  const primaryStats = useMemo(() => buildPrimaryStats(stats, evalSummary, synthesis), [stats, evalSummary, synthesis]);

  const loadStats = useCallback(async function loadStats() {
    const [statsRes, qloraRes, evalRes] = await Promise.all([
      apiGet('/api/demo/kb/stats', { runtimeConfig }),
      apiGet('/api/demo/qlora/summary', { runtimeConfig }),
      apiGet('/api/demo/medical-rag/eval-summary', { runtimeConfig }),
    ]);
    if (statsRes.ok) setStats(statsRes.data);
    if (qloraRes.ok) setQlora(qloraRes.data);
    if (evalRes.ok) setEvalSummary(evalRes.data);
  }, [runtimeConfig]);

  useEffect(() => {
    loadStats();
  }, [loadStats]);

  useEffect(() => {
    if (results || synthesis || !query.trim()) return;
    const replay = replayForQuery;
    if (!replay) return;
    patchSession({
      results: replayToSearchResults(replay),
      synthesis: normalizeSynthesis(replay),
    });
  }, [patchSession, query, replayForQuery, results, synthesis]);

  function replayCurrentQuestion() {
    if (!replayForQuery) return;
    patchSession({
      results: replayToSearchResults(replayForQuery),
      synthesis: normalizeSynthesis(replayForQuery),
    });
  }

  function loadPrompt(prompt) {
    const replay = prompt.replay ? findMedicalAskReplay(prompt.query) : null;
    patchSession({
      query: prompt.query,
      selectedPrompt: prompt.label,
      mode: prompt.safety ? mode : 'hybrid',
      indexId: 'bge_m3',
      results: replay ? replayToSearchResults(replay) : null,
      synthesis: replay ? normalizeSynthesis(replay) : null,
    });
  }

  return (
    <SectionWrapper>
      <div className="custom-screen space-y-6">
        <header className="space-y-5">
          <div className="flex flex-col gap-4 xl:flex-row xl:items-end xl:justify-between">
            <div className="max-w-3xl">
              <div className="mb-2 flex flex-wrap items-center gap-2">
                <EvidenceBadge text="赛道三" color="emerald" />
                <EvidenceBadge text="RAG 回放" color="blue" />
                <EvidenceBadge text="来源可追溯" color="gray" />
              </div>
              <h1 className="text-3xl font-semibold text-gray-900 sm:text-4xl">赛道三：医学 RAG 来源回放</h1>
              <p className="mt-3 text-sm leading-relaxed text-gray-600">
                将医学 RAG 的已验证 trace 转化为在线展示：中文问题、英文文献来源、片段回溯、结论引用校验和安全拒答边界保持一致。
              </p>
            </div>
            <button onClick={loadStats} className="rounded border px-4 py-2 text-xs text-gray-700 hover:bg-gray-50">刷新指标</button>
          </div>

          <RuntimeSummary runtimeConfig={{ ...runtimeConfig, retrieval_index: indexId }} variant="medical" />

          <div className="grid grid-cols-1 gap-3 md:grid-cols-3">
            {useCases.map(item => (
              <div key={item.label} className="rounded-lg border bg-white p-4">
                <EvidenceBadge text={item.label} color={item.color} />
                <p className="mt-3 text-sm leading-relaxed text-gray-700">{item.text}</p>
              </div>
            ))}
          </div>

          <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
            {primaryStats.map(item => (
              <div key={item.label} className="rounded-lg border bg-gray-50 p-3">
                <div className="font-mono text-lg font-semibold text-gray-900">{item.value}</div>
                <div className="mt-1 text-[11px] text-gray-600">{item.label}</div>
              </div>
            ))}
          </div>
        </header>

        <div className="grid grid-cols-1 gap-6 xl:grid-cols-[1fr_360px]">
          <main className="space-y-4">
            <StepCard
              index="1"
              title="选择问题"
              desc="预置问题来自已保存 trace，可立即回放；手动输入只匹配公开回放或安全边界，不现场访问受控链路。"
              status={synthesis?.status === 'replay' || synthesis?.status === 'safety_refusal' ? synthesis.status : query ? 'ready' : 'pending'}
            >
              <div className="mb-4 space-y-3">
                {promptGroups.map(group => (
                  <div key={group.title} className="rounded-lg border bg-gray-50 p-3">
                    <div className="mb-2 flex items-center justify-between gap-3">
                      <div>
                        <div className="text-sm font-semibold text-gray-900">{group.title}</div>
                        <div className="text-[11px] text-gray-500">{group.desc}</div>
                      </div>
                    </div>
                    <div className="flex flex-wrap gap-2">
                      {group.prompts.map(prompt => (
                        <button
                          key={prompt.label}
                          onClick={() => loadPrompt(prompt)}
                          className={`rounded border px-3 py-1.5 text-xs ${selectedPrompt === prompt.label ? 'border-gray-900 bg-gray-900 text-white' : 'bg-white text-gray-700 hover:bg-gray-50'}`}
                        >
                          {prompt.label}
                        </button>
                      ))}
                    </div>
                  </div>
                ))}
              </div>

              <textarea
                value={query}
                onChange={e => patchSession({ query: e.target.value, selectedPrompt: '', results: null, synthesis: null })}
                rows={3}
                className="w-full rounded-lg border px-3 py-2 text-sm leading-relaxed"
                placeholder="输入一个医学文献来源问题，例如：化疗剂量减少和治疗延迟的不良事件来源"
              />

              <div className="mt-3 flex flex-wrap gap-2">
                {modes.map(item => (
                  <button key={item.id} onClick={() => patchSession({ mode: item.id })} className={`rounded border px-3 py-1.5 text-left text-xs ${mode === item.id ? 'border-gray-900 bg-gray-900 text-white' : 'text-gray-600 hover:bg-gray-50'}`}>
                    <span className="font-medium">{item.label}</span>
                    <span className={`ml-1 ${mode === item.id ? 'text-gray-200' : 'text-gray-400'}`}>{item.desc}</span>
                  </button>
                ))}
              </div>
              <div className="mt-2 flex flex-wrap gap-2">
                {indexOptions.map(item => (
                  <button key={item.id} onClick={() => patchSession({ indexId: item.id, results: null, synthesis: null })} className={`rounded border px-3 py-1.5 text-left text-xs ${indexId === item.id ? 'border-sky-600 bg-sky-600 text-white' : 'text-gray-600 hover:bg-gray-50'}`}>
                    <span className="font-medium">{item.label}</span>
                    <span className={`ml-1 ${indexId === item.id ? 'text-sky-100' : 'text-gray-400'}`}>{item.desc}</span>
                  </button>
                ))}
              </div>
            </StepCard>

            <StepCard
              index="2"
              title="检索来源"
              desc="展示命中文段、章节标签、融合分数与公开边界。"
              status={results?.results?.length ? 'done' : results?.error ? 'failed' : 'pending'}
            >
              {results?.error && <ErrorCallout message={results.error} hint="确认 FastAPI 与医学索引服务已启动。" />}
              {results?.results?.length ? (
                <div className="space-y-3">
                  {results.results.map((item, i) => (
                    <div key={`${item.chunk_id}-${i}`} className="overflow-hidden rounded-lg border">
                      <button onClick={() => setExpanded(expanded === i ? null : i)} className="w-full p-3 text-left hover:bg-gray-50">
                        <div className="mb-2 flex flex-wrap items-center gap-2 text-[11px]">
                          <span className="font-mono text-gray-400">#{item.rank || i + 1}</span>
                          <EvidenceBadge text={item.medical_label || 'medical'} color="blue" />
                          <EvidenceBadge text={displayRetrievalMode(item.mode || mode)} color={mode === 'vision' ? 'purple' : 'green'} />
                          <span className="font-mono text-amber-700">融合分 {formatScore(item.rrf_score)}</span>
                          <span className="truncate text-gray-400">{displaySourceFile(item.source_file)}</span>
                        </div>
                        <p className="text-xs leading-relaxed text-gray-700">{item.text_preview || item.preview || '已命中文献片段。'}</p>
                      </button>
                      {expanded === i && (
                        <div className="space-y-1 border-t bg-gray-50 px-3 py-3 text-[11px] text-gray-600">
                          <div>文段 ID：<span className="font-mono">{item.chunk_id}</span></div>
                          <div>章节：{item.source_section || '-'}</div>
                          <div>医学层级：{item.medical_parent || '-'} / {item.medical_label || '-'}</div>
                          <div>边界：原文、文段和检索上下文不进入在线展示版。</div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              ) : !results?.error && (
                <div className="rounded-lg border bg-gray-50 p-4 text-xs text-gray-500">选择案例会立即展示可复现回放来源；手动问题只做公开回放匹配或安全边界展示。</div>
              )}
            </StepCard>

            <StepCard
              index="3"
              title="中文回答与结论校验"
              desc="每条事实结论必须有来源；个人诊疗和急症问题进入安全边界。"
              status={synthesis ? (synthesis.status === 'failed' ? 'failed' : synthesis.status || 'done') : 'pending'}
            >
              {synthesis ? (
                <SynthesisPanel synthesis={synthesis} query={query} />
              ) : (
                <div className="rounded-lg border bg-gray-50 p-4 text-xs text-gray-500">选择上方预置案例后，会直接展示已验证回放的中文回答与结论校验。</div>
              )}
            </StepCard>
          </main>

          <aside className="space-y-4">
            <StepCard index="A" title="回放资产" desc="随在线展示版提供的 trace、案例和来源摘要。" status={stats ? 'done' : 'pending'} actions={<button onClick={loadStats} className="rounded border px-3 py-1.5 text-xs hover:bg-white">刷新</button>}>
              {stats ? (
                <div className="space-y-3 text-xs">
                  <MetricRow label="医学文段" value={stats.total_chunks || 0} />
                  <MetricRow label="回放 trace" value={stats.trace_bundle?.available ? '随包提供' : '未提供'} />
                  <MetricRow label="预置案例" value={`${stats.replay_cases || 0} 个`} />
                  <MetricRow label="来源摘要" value={stats.source_manifest ? '已收录' : '未收录'} />
                  <MetricRow label="训练摘要" value={qlora?.summary_available ? '已收录' : '未收录'} />
                </div>
              ) : <div className="text-xs text-gray-500">加载后展示随包提供的回放资产状态。</div>}
            </StepCard>

            <StepCard index="B" title="评测闭环" desc="固定题集、多索引命中和合成校验。" status={evalSummary?.available ? 'done' : 'pending'} actions={<button onClick={loadStats} className="rounded border px-3 py-1.5 text-xs hover:bg-white">刷新</button>}>
              {evalSummary?.available ? (
                <div className="space-y-3 text-xs">
                  <div className="grid grid-cols-3 gap-2">
                    <SmallMetric label="固定题" value={evalSummary.eval?.case_count || 0} />
                    <SmallMetric label="检索口径" value={`Top-${evalSummary.eval?.k || 3}`} />
                    <SmallMetric label="最佳索引" value={displayIndexLabel(evalSummary.eval?.best_label)} />
                  </div>
                  {(evalSummary.eval?.rows || []).map(row => (
                    <div key={row.label} className={`rounded border p-2 ${row.label === evalSummary.eval?.best_label ? 'border-emerald-100 bg-emerald-50' : 'bg-white'}`}>
                      <div className="flex items-center justify-between gap-2">
                        <div className="font-semibold text-gray-800">{displayIndexLabel(row.label)}</div>
                        <div className="font-mono text-[11px] text-gray-500">{row.query_embed_seconds}s</div>
                      </div>
                      <div className="mt-1 flex flex-wrap gap-1.5 text-[11px] text-gray-600">
                        <span className="rounded bg-gray-100 px-1.5 py-0.5">命中 {row.hit_at_k}/{row.cases}</span>
                        <span className="rounded bg-gray-100 px-1.5 py-0.5">标签 {row.label_hit_at_k}/{row.cases}</span>
                        <span className="rounded bg-gray-100 px-1.5 py-0.5">均排 {row.mean_first_hit_rank || '-'}</span>
                      </div>
                    </div>
                  ))}
                  {evalSummary.smoke_case && (
                    <div className="rounded border bg-white p-2">
                      <div className="font-semibold text-gray-800">合成抽查</div>
                      <div className="mt-1 text-gray-600">{evalSummary.smoke_case.claim_count || 0} 条结论 · {evalSummary.smoke_case.supported_claims || 0} 条可支持 · 引用覆盖 {Math.round((evalSummary.smoke_case.citation_coverage || 0) * 100)}%</div>
                    </div>
                  )}
                </div>
              ) : (
                <div className="text-xs text-gray-500">{evalSummary?.reason || '生成 medical_rag_eval.json 后展示评测摘要。'}</div>
              )}
              <div className="mt-3 border-t border-gray-100 pt-2 text-[10px] text-gray-400 leading-relaxed">
                完整补充实验（阶段消融、安全拒答、EI taxonomy、隐私边界、语义切片、中文 Ask 鲁棒性、Evidence Card、部署 smoke）见 DATA-TRACE #182-190 与来源矩阵。
              </div>
            </StepCard>

            <div className="rounded-lg border bg-gray-50 p-4 text-xs leading-relaxed text-gray-600">
              <div className="mb-2 font-semibold text-gray-900">为什么可信</div>
              <div className="space-y-2">
                <p>先检索后回答，不凭模型记忆直接生成医学结论。</p>
                <p>回答包含文段引用与结论支撑状态，便于访问者逐条查看。</p>
                <p>来源不足、个人诊疗和急症问题不会强行进入 RAG。</p>
              </div>
            </div>
          </aside>
        </div>
      </div>
    </SectionWrapper>
  );
}

function SynthesisPanel({ synthesis, query }) {
  if (synthesis.status === 'failed') return <ErrorCallout message={synthesis.message} />;
  const status = synthesis.status === 'safety_refusal' ? 'safety_refusal' : synthesis.status === 'replay' ? 'replay' : synthesis.status === 'local_rag' ? 'local_rag' : 'done';
  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center gap-2">
        <StatusPill status={status} />
        <span className="text-xs text-gray-500">{synthesis.source}</span>
      </div>
      <div className="rounded-lg border bg-white p-4">
        <div className="prose prose-sm max-w-none text-gray-800">
          <ReactMarkdown remarkPlugins={[remarkMath]} rehypePlugins={[rehypeKatex]}>
            {synthesis.answer || ''}
          </ReactMarkdown>
        </div>
      </div>
      {synthesis.search_query && synthesis.search_query !== query && (
        <div className="rounded-lg border bg-gray-50 px-3 py-2 text-xs text-gray-600">
          <span className="font-semibold text-gray-800">英文检索词：</span>
          <span className="font-mono">{synthesis.search_query}</span>
          {synthesis.search_queries?.length > 1 && <span className="ml-2 text-[11px] text-gray-500">融合 {synthesis.search_queries.length} 组 query</span>}
        </div>
      )}
      {synthesis.citations?.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {synthesis.citations.map(c => <EvidenceBadge key={c} text={c} color="gray" />)}
        </div>
      )}
      <div className="text-xs text-gray-500">{synthesis.evidence_coverage}</div>
      {synthesis.claims?.length > 0 && (
        <div className="rounded-lg border bg-gray-50 p-3">
          <div className="mb-2 flex items-center justify-between gap-2">
            <div className="text-xs font-semibold text-gray-900">结论校验</div>
            <div className="text-[11px] text-gray-500">引用覆盖 {Math.round((synthesis.citation_coverage || 0) * 100)}%</div>
          </div>
          <div className="space-y-2">
            {synthesis.claims.map((claim, idx) => (
              <div key={`${claim.claim}-${idx}`} className="rounded border bg-white p-2">
                <div className="flex items-start gap-2">
                  <span className={`mt-0.5 rounded border px-1.5 py-0.5 text-[10px] ${claim.supported ? 'border-emerald-100 bg-emerald-50 text-emerald-700' : 'border-amber-100 bg-amber-50 text-amber-700'}`}>
                    {claim.supported ? '可支持' : '来源不足'}
                  </span>
                  <div className="min-w-0 flex-1">
                    <div className="text-xs leading-relaxed text-gray-700">{claim.claim}</div>
                    {claim.citations?.length > 0 && (
                      <div className="mt-1 flex flex-wrap gap-1">
                        {claim.citations.map(c => <span key={c} className="rounded border bg-gray-50 px-1.5 py-0.5 font-mono text-[10px] text-gray-600">{c}</span>)}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      {synthesis.abstain_reason && <div className="rounded border border-amber-100 bg-amber-50 px-3 py-2 text-xs text-amber-700">拒答原因：{synthesis.abstain_reason}</div>}
      <div className="text-[11px] leading-relaxed text-gray-400">{synthesis.limitation}</div>
    </div>
  );
}

function MetricRow({ label, value }) {
  return (
    <div className="flex items-center justify-between rounded border bg-gray-50 px-2.5 py-2">
      <span className="text-gray-500">{label}</span>
      <span className="font-mono font-semibold text-gray-800">{value}</span>
    </div>
  );
}

function SmallMetric({ label, value }) {
  return (
    <div className="rounded border bg-gray-50 p-2">
      <div className="truncate font-mono text-gray-800">{value}</div>
      <div className="mt-1 text-[11px] text-gray-500">{label}</div>
    </div>
  );
}

function buildPrimaryStats(stats, evalSummary, synthesis) {
  const bestEvalRow = evalSummary?.eval?.rows?.find(r => r.label === 'index_bge_m3') || evalSummary?.eval?.rows?.find(r => r.label === evalSummary?.eval?.best_label);
  const hitValue = Number.isFinite(bestEvalRow?.hit_at_k) && Number.isFinite(evalSummary?.eval?.case_count)
    ? `${bestEvalRow.hit_at_k}/${evalSummary.eval.case_count}`
    : '待加载';
  const claimValue = synthesis?.claims?.length
    ? `${synthesis.claims.filter(c => c.supported).length}/${synthesis.claims.length}`
    : '待加载';
  const citationValue = synthesis?.citation_coverage !== undefined
    ? `${Math.round((synthesis.citation_coverage || 0) * 100)}%`
    : '待加载';
  return [
    { label: '医学文段', value: stats?.total_chunks ? String(stats.total_chunks) : '待加载' },
    { label: '中文 Ask Hit@3', value: hitValue },
    { label: '结论支撑', value: claimValue },
    { label: '引用覆盖', value: citationValue },
  ];
}

function replayToSearchResults(replay) {
  return {
    status: replay.status === 'safety_refusal' ? 'safety_refusal' : 'replay',
    results: (replay.evidence_items || []).map((item, index) => ({
      rank: index + 1,
      source_file: item.source_file || '已验证回放',
      source_section: item.source_section || '',
      mode: replay.retrieval_mode || 'hybrid',
      rrf_score: item.rrf_score || '回放',
      text_preview: item.text_preview || item.preview || '',
      ...item,
    })),
  };
}

function displayIndexLabel(label) {
  if (label === 'medical_qwen3_embedding_4b') return '高维索引';
  if (label === 'index_bge_small') return 'BGE Small';
  if (label === 'index_bge_m3') return 'BGE M3';
  return label || '-';
}

function displayRetrievalMode(modeId) {
  if (modeId === 'hybrid') return '混合检索';
  if (modeId === 'dense') return '语义检索';
  if (modeId === 'vision') return '图文融合';
  if (modeId === 'bm25') return 'BM25';
  return modeId || '回放';
}

function displaySourceFile(sourceFile) {
  if (!sourceFile || sourceFile === 'verified_trace' || sourceFile === 'local chunk') return '已验证回放';
  return sourceFile;
}

function displayTaskId(taskId) {
  if (!taskId || taskId === 'verified_replay') return '已验证回放';
  return taskId;
}

function normalizeSynthesis(data) {
  if (data.status === 'safety_refusal') {
    return {
      status: 'safety_refusal',
      source: data.safety_triage?.triage_source || '安全分流',
      answer: data.answer,
      citations: [],
      claims: [],
      citation_coverage: 0,
      evidence_coverage: '未进入检索 · 0 个文段 · 安全边界',
      limitation: '该问题看起来像个人诊疗、用药建议或急症风险，系统不会把它包装成文献来源问答。',
      abstain_reason: data.safety_triage?.reason || data.safety_triage?.category || 'safety_boundary',
    };
  }

  const evidenceItems = data.evidence_items || [];
  const citations = evidenceItems.slice(0, QUICK_PROOF_K).map(item => item.chunk_id).filter(Boolean);
  const totalChunks = data.source_summary?.total_chunks || evidenceItems.length || 0;
  const totalSources = data.source_summary?.total_sources || 0;
  const base = {
    answer: data.answer,
    search_query: data.search_query,
    search_queries: data.search_queries || [],
    query_rewrites: data.query_rewrites || [],
    citations: data.citations?.length ? data.citations : citations,
    claims: data.claims || [],
    citation_coverage: data.citation_coverage || 0,
    evidence_sufficiency: data.evidence_sufficiency,
    abstain_reason: data.abstain_reason,
  };

  if (data.status === 'replay') {
    return {
      ...base,
      status: 'replay',
      source: `可复现回放 · ${data.retrieval_index?.label || 'BGE M3'} · ${displayTaskId(data.task_id)}`,
      evidence_coverage: `${totalChunks} 个文段 · ${totalSources} 个来源 · 已验证回放 · 引用覆盖 ${Math.round((data.citation_coverage || 0) * 100)}%`,
      limitation: data.limitations || '该结果来自已保存的可复现实验 trace；云端页面不现场访问受控资产。',
    };
  }

  if (data.status === 'local_rag') {
    return {
      ...base,
      status: 'local_rag',
      source: `RAG 回放 ${data.model || ''} · ${data.retrieval_index?.label || data.retrieval_index?.alias || ''} · ${displayTaskId(data.task_id)}`.trim(),
      evidence_coverage: `${totalChunks} 个文段 · ${totalSources} 个来源 · ${displayRetrievalMode(data.retrieval_mode)} · ${data.retrieval_index?.embedding_model || 'embedding'} · ${data.confidence || 'medium'} · 引用覆盖 ${Math.round((data.citation_coverage || 0) * 100)}%`,
      limitation: data.limitations || '该条目是实验 trace 的公开回放，不在云端重新访问私有医学资产。',
    };
  }

  return {
    status: 'replay',
    source: `trace 回放 ${displayTaskId(data.task_id)}`.trim(),
    answer: data.answer || `已基于可复现 trace 回放来源摘要：${totalChunks} 个文段，覆盖 ${totalSources} 个来源。`,
    citations,
    claims: data.claims || [],
    citation_coverage: data.citation_coverage || 0,
    evidence_coverage: `${totalChunks} 个文段 · ${totalSources} 个来源 · 已验证 trace 回放`,
    limitation: '公开云端页只回放已验证 trace，不将医疗原文发送到云端模型，也不现场访问私有资产。',
  };
}

function formatScore(score) {
  if (score === 'replay') return '回放';
  if (typeof score === 'number') return score.toFixed(4);
  if (score && score.toFixed) return score.toFixed(4);
  return score || '-';
}
