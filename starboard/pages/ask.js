import SectionWrapper from '../components/SectionWrapper';
import { useAskSession } from '../components/workbench/AskSessionProvider';
import EvidenceBadge from '../components/workbench/EvidenceBadge';
import ErrorCallout from '../components/workbench/ErrorCallout';
import MarkdownText from '../components/workbench/MarkdownText';
import RuntimeSummary from '../components/workbench/RuntimeSummary';
import StatusPill from '../components/workbench/StatusPill';
import WorkbenchLoadingCard from '../components/workbench/WorkbenchLoadingCard';

const caseGroups = [
  {
    title: '用户自然问题',
    desc: '更接近医生、研究助理或患者教育场景里的自然问法。',
    items: [
      { label: '闭环胰岛素低血糖', text: '闭环胰岛素系统会不会增加低血糖风险？文献依据是什么？' },
      { label: '化疗剂量调整', text: '化疗时如果出现毒性反应，研究里通常怎么处理剂量减少或治疗延迟？' },
      { label: '生存获益判断', text: '这些研究里的总生存期和无进展生存期，是终点定义还是生存获益结论？' },
    ],
  },
  {
    title: '研究者验证',
    desc: '面向研究者或复现者，用于验证章节定位、统计设计和来源追溯。',
    items: [
      { label: '主要终点与安全性', text: '主要终点和安全性文献依据' },
      { label: 'ITT 分析人群', text: '意向治疗分析人群的统计分析依据' },
      { label: '纳入排除标准', text: '随机对照试验的纳入排除标准' },
    ],
  },
  {
    title: '安全边界',
    desc: '展示急症和个人用药问题不会进入文献检索。',
    items: [
      { label: '急症风险', text: '我现在胸痛呼吸困难怎么办' },
      { label: '个人用药建议', text: '我发烧了应该吃什么药' },
      { label: '个人诊断请求', text: '我头痛恶心是不是脑卒中' },
    ],
  },
];

const indexOptions = [
  { id: 'bge_m3', label: 'BGE M3', desc: '强检索 · 默认' },
  { id: 'qwen', label: 'Qwen3', desc: 'Ollama embedding' },
  { id: 'bge_small', label: 'BGE Small', desc: '轻量检索' },
];

const modeOptions = [
  { id: 'hybrid', label: 'Hybrid' },
  { id: 'dense', label: 'Dense' },
  { id: 'bm25', label: 'BM25' },
];

export default function AskPage({ runtimeConfig }) {
  const {
    question,
    setQuestion,
    messages,
    indexId,
    setIndexId,
    mode,
    setMode,
    loading,
    error,
    pendingQuestion,
    ask,
    clearChat,
  } = useAskSession();

  function submitAsk(nextQuestion = question, options = {}) {
    ask(nextQuestion, { runtimeConfig, ...options });
  }

  return (
    <SectionWrapper>
      <div className="custom-screen space-y-5">
        <div className="flex flex-col xl:flex-row xl:items-end xl:justify-between gap-3">
          <div>
            <h1 className="text-gray-800 text-3xl font-semibold sm:text-4xl mb-2">医学文献问答</h1>
            <p className="text-sm text-gray-600 leading-relaxed max-w-3xl">
              面向用户的 Medical RAG 入口：自然语言问题进入本地医学文献库，回答必须带引用、结论校验和安全边界。
            </p>
          </div>
          <button onClick={clearChat} disabled={loading} className="px-4 py-2 rounded border text-xs text-gray-700 hover:bg-white disabled:opacity-50">
            清空会话
          </button>
        </div>

        <RuntimeSummary runtimeConfig={{ ...runtimeConfig, retrieval_index: indexId }} variant="medical" />

        <div className="grid grid-cols-1 xl:grid-cols-[minmax(0,1fr)_20rem] gap-5">
          <div className="border rounded-lg bg-white min-h-[34rem] flex flex-col">
            <div className="border-b px-4 py-3 flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3">
              <div className="flex flex-wrap gap-2">
                {indexOptions.map(item => (
                  <button
                    key={item.id}
                    onClick={() => setIndexId(item.id)}
                    className={`px-3 py-1.5 rounded border text-xs ${indexId === item.id ? 'bg-gray-900 text-white border-gray-900' : 'text-gray-600 hover:bg-gray-50'}`}
                    title={item.desc}
                  >
                    {item.label}
                  </button>
                ))}
                {modeOptions.map(item => (
                  <button
                    key={item.id}
                    onClick={() => setMode(item.id)}
                    className={`px-3 py-1.5 rounded border text-xs ${mode === item.id ? 'bg-sky-600 text-white border-sky-600' : 'text-gray-600 hover:bg-gray-50'}`}
                  >
                    {item.label}
                  </button>
                ))}
              </div>
              <div className="text-[11px] text-gray-500">
                本地问答模式
              </div>
            </div>

            <div className="flex-1 overflow-auto p-4 space-y-4 bg-gray-50/60">
              {messages.length === 0 ? (
                <div className="h-full min-h-[20rem] flex items-center justify-center">
                  <div className="max-w-xl text-center">
                    <div className="text-sm font-semibold text-gray-800">从一个临床文献问题开始</div>
                    <div className="mt-2 text-xs text-gray-500 leading-relaxed">
                      可以问“文献依据是什么”，但不能把它当成个人诊断或用药建议。
                    </div>
                    <div className="mt-4 grid gap-3 text-left">
                      {caseGroups.map(group => (
                        <div key={group.title} className="rounded border bg-white p-3">
                          <div className="text-[11px] font-semibold text-gray-800">{group.title}</div>
                          <div className="mt-2 grid grid-cols-1 gap-2 sm:grid-cols-3">
                            {group.items.map(item => (
                              <button key={item.text} onClick={() => submitAsk(item.text, { preferReplay: true })} disabled={loading} className="min-h-[2.75rem] rounded border bg-gray-50 px-3 py-1.5 text-center text-xs text-gray-700 hover:border-gray-400 disabled:opacity-50">
                                {item.label}
                              </button>
                            ))}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              ) : (
                messages.map((message, idx) => (
                  <ChatBubble key={`${message.role}-${idx}`} message={message} />
                ))
              )}
              {loading && (
                <div className="flex justify-start">
                  <WorkbenchLoadingCard
                    title="本地 RAG 正在处理"
                    desc={pendingQuestion ? `正在处理：${pendingQuestion}` : '不会调用云端模型，正在本地完成检索、合成和引用校验。'}
                    steps={['检索本地来源', '合成回答', '校验引用']}
                    className="w-full max-w-xl"
                  />
                </div>
              )}
            </div>

            <div className="border-t p-3 bg-white">
              {error ? <div className="mb-3"><ErrorCallout message={error} /></div> : null}
              <div className="flex gap-2">
                <textarea
                  value={question}
                  onChange={e => setQuestion(e.target.value)}
                  onKeyDown={e => {
                    if (e.key === 'Enter' && !e.shiftKey) {
                      e.preventDefault();
                      submitAsk();
                    }
                  }}
                  className="min-h-[3rem] max-h-28 flex-1 resize-y rounded border px-3 py-2 text-sm text-gray-800 focus:outline-none focus:ring-2 focus:ring-gray-900/10"
                  placeholder="输入医学文献问题，或点击上方案例"
                />
                <button onClick={() => submitAsk()} disabled={loading || !question.trim()} className="w-24 rounded bg-gray-900 px-4 py-2 text-sm text-white disabled:opacity-50">
                  {loading ? <span className="inline-flex items-center gap-1">处理中<span className="inline-flex w-4 justify-between"><span className="h-1 w-1 animate-bounce rounded-full bg-white [animation-delay:-0.2s]" /><span className="h-1 w-1 animate-bounce rounded-full bg-white [animation-delay:-0.1s]" /><span className="h-1 w-1 animate-bounce rounded-full bg-white" /></span></span> : '提问'}
                </button>
              </div>
              <div className="mt-2 text-[11px] text-gray-500">
                Enter 发送，Shift+Enter 换行。回答不替代医生判断。
              </div>
            </div>
          </div>

          <aside className="space-y-4">
            <div className="border rounded-lg bg-white p-4">
              <div className="text-sm font-semibold text-gray-800">产品边界</div>
              <div className="mt-3 space-y-3 text-xs text-gray-600 leading-relaxed">
                <div>
                  <div className="font-semibold text-gray-800">本地资产</div>
                  <p>PDF 解析产物、chunk、嵌入索引和检索上下文留在本地。</p>
                </div>
                <div>
                  <div className="font-semibold text-gray-800">公开展示入口</div>
                  <p>前端页面可以部署到云端展示；医学来源链仍在后端私有环境内完成。</p>
                </div>
                <div>
                  <div className="font-semibold text-gray-800">风险控制</div>
                  <p>个人诊疗、用药剂量和急症问题触发安全边界；事实性结论必须能映射到 chunk 引用。</p>
                </div>
              </div>
            </div>

            <div className="border rounded-lg bg-white p-4">
              <div className="text-sm font-semibold text-gray-800">展示案例</div>
              <div className="mt-3 space-y-3">
                {caseGroups.map(group => (
                  <div key={group.title} className="rounded border bg-gray-50 p-3">
                    <div className="text-xs font-semibold text-gray-800">{group.title}</div>
                    <div className="mt-1 text-[11px] text-gray-500 leading-relaxed">{group.desc}</div>
                    <div className="mt-2 space-y-1.5">
                      {group.items.map(item => (
                        <button key={item.text} onClick={() => submitAsk(item.text, { preferReplay: true })} disabled={loading} className="w-full rounded border bg-white px-2.5 py-2 text-left hover:border-gray-400 disabled:opacity-50">
                          <div className="text-[11px] font-semibold text-gray-800">{item.label}</div>
                          <div className="mt-0.5 text-[11px] text-gray-500 leading-snug">{item.text}</div>
                        </button>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div className="border rounded-lg bg-white p-4">
              <div className="text-sm font-semibold text-gray-800">当前会话</div>
              <div className="mt-3 grid grid-cols-2 gap-2 text-xs">
                <Metric label="轮次" value={Math.ceil(messages.length / 2)} />
                <Metric label="索引" value={indexOptions.find(i => i.id === indexId)?.label || indexId} />
                <Metric label="模式" value={mode} />
                <Metric label="隐私" value="local" />
              </div>
            </div>
          </aside>
        </div>
      </div>
    </SectionWrapper>
  );
}

function ChatBubble({ message }) {
  const isUser = message.role === 'user';
  if (isUser) {
    return (
      <div className="flex justify-end">
        <div className="max-w-2xl rounded-lg bg-gray-900 px-4 py-3 text-sm text-white">
          {message.content}
        </div>
      </div>
    );
  }

  const evidenceItems = message.evidence_items || [];
  return (
    <div className="flex justify-start">
      <div className="max-w-3xl rounded-lg border bg-white p-4 shadow-sm space-y-3">
        <div className="flex flex-wrap items-center gap-2">
          <StatusPill status={message.status === 'failed' ? 'failed' : message.status === 'replay' ? 'replay' : message.status === 'safety_refusal' ? 'safety_refusal' : 'local_rag'} />
          <span className="text-[11px] text-gray-500">{message.model || message.privacy || 'local_only'}</span>
          {message.rag_mode === 'evidence_structured' ? <EvidenceBadge text="结构化 RAG" color="blue" /> : null}
          {message.question_type ? <EvidenceBadge text={questionTypeLabel(message.question_type)} color="gray" /> : null}
          {message.confidence ? <EvidenceBadge text={`置信度 ${message.confidence}`} color="green" /> : null}
          {message.abstain ? <EvidenceBadge text="依据不足" color="amber" /> : null}
        </div>
        <MarkdownText>{message.answer}</MarkdownText>
        {message.status === 'local_rag' ? <RagTraceSummary message={message} /> : null}
        {message.answer_audit?.issues?.length ? (
          <div className="rounded border border-amber-100 bg-amber-50 p-3 text-xs leading-relaxed text-amber-800">
            <div className="font-semibold">回答审查：需要注意</div>
            <div className="mt-1">{message.answer_audit.issues.join('；')}</div>
          </div>
        ) : message.answer_audit?.status === 'passed' ? (
          <div className="rounded border border-emerald-100 bg-emerald-50 p-3 text-xs leading-relaxed text-emerald-800">
            <div className="font-semibold">回答审查：通过</div>
            <div className="mt-1">{(message.answer_audit.passed || []).slice(0, 2).join('；')}</div>
          </div>
        ) : null}
        {message.search_query && message.search_query !== message.question ? (
          <div className="rounded border bg-gray-50 px-3 py-2 text-xs text-gray-600">
            <span className="font-semibold text-gray-800">英文检索词：</span>
            <span className="font-mono">{message.search_query}</span>
            {message.search_queries?.length > 1 ? (
              <span className="ml-2 text-[11px] text-gray-500">融合 {message.search_queries.length} 组 query</span>
            ) : null}
            {message.query_rewrites?.length ? (
              <span className="ml-2 text-[11px] text-gray-500">自动桥接中文问题与英文文献库</span>
            ) : null}
          </div>
        ) : null}
        {message.citations?.length ? (
          <div className="flex flex-wrap gap-1.5">
            {message.citations.map(item => <EvidenceBadge key={item} text={item} color="gray" />)}
          </div>
        ) : null}
        {message.claims?.length ? (
          <div className="rounded border bg-gray-50 p-3 space-y-2">
            <div className="flex items-center justify-between gap-2">
              <div className="text-xs font-semibold text-gray-800">结论校验</div>
              <div className="text-[11px] text-gray-500">引用覆盖 {Math.round((message.citation_coverage || 0) * 100)}%</div>
            </div>
            {message.claims.map((claim, idx) => (
              <div key={`${claim.claim}-${idx}`} className="rounded border bg-white p-2">
                <div className="flex gap-2">
                  <span className={`h-fit whitespace-nowrap rounded px-1.5 py-0.5 text-[10px] ${claim.supported ? 'bg-emerald-50 text-emerald-700 border border-emerald-100' : 'bg-amber-50 text-amber-700 border border-amber-100'}`}>
                    {claim.supported ? '可支持' : '依据不足'}
                  </span>
                  <div className="min-w-0">
                    <div className="text-xs text-gray-700">{claim.claim}</div>
                    <div className="mt-1 flex flex-wrap gap-1">
                      {(claim.citations || []).map(c => <span key={c} className="rounded bg-gray-100 px-1.5 py-0.5 font-mono text-[10px] text-gray-600">{c}</span>)}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : null}
        {message.safety_triage ? (
          <div className={`rounded border p-3 text-xs leading-relaxed ${message.safety_triage.allow_rag ? 'bg-emerald-50 border-emerald-100 text-emerald-800' : 'bg-amber-50 border-amber-100 text-amber-800'}`}>
            <div className="font-semibold">安全分诊：{triageLabel(message.safety_triage.category)} · {riskLabel(message.safety_triage.risk_level)}</div>
            <div className="mt-1">{message.safety_triage.user_message}</div>
          </div>
        ) : null}
        {evidenceItems.length ? (
          <details className="rounded border bg-white">
            <summary className="cursor-pointer px-3 py-2 text-xs font-semibold text-gray-800">查看检索来源</summary>
            <div className="border-t p-3 space-y-2">
              {evidenceItems.slice(0, 3).map(item => (
                <div key={item.chunk_id} className="rounded bg-gray-50 p-2">
                  <div className="flex flex-wrap gap-2 text-[11px]">
                    <span className="font-mono text-gray-500">{item.chunk_id}</span>
                    <span className="text-blue-700">{item.medical_label}</span>
                    <span className="text-amber-700">RRF {item.rrf_score}</span>
                  </div>
                  <div className="mt-1 text-xs text-gray-600 leading-relaxed">{item.text_preview}</div>
                </div>
              ))}
            </div>
          </details>
        ) : null}
        {message.limitations || message.abstain_reason ? (
          <div className="text-[11px] text-gray-500">
            {message.limitations}
            {message.abstain_reason ? ` 拒答原因：${message.abstain_reason}` : ''}
          </div>
        ) : null}
      </div>
    </div>
  );
}

function RagTraceSummary({ message }) {
  const evidenceCount = message.evidence_items?.length || message.source_summary?.total_chunks || 0;
  const sourceCount = message.source_summary?.total_sources || 0;
  const cardCount = message.evidence_cards?.length || 0;
  const traceCount = message.reasoning_trace?.length || 0;
  const claimCount = message.claim_count ?? message.claims?.length ?? 0;
  const supported = message.supported_claims ?? message.claims?.filter(item => item.supported).length ?? 0;
  const coverage = Math.round((message.citation_coverage || 0) * 100);
  const queryCount = message.search_queries?.length || 1;
  const bridged = message.query_language === 'zh' && message.rewrite_method !== 'identity';
  const auditItems = [
    { label: '本地链路', value: message.privacy === 'local_only' ? '已启用' : (message.privacy || '未知') },
    { label: '中文桥接', value: bridged ? '已桥接' : '原文检索' },
    { label: '来源卡', value: `${cardCount}` },
    { label: '安全边界', value: message.safety_triage ? riskLabel(message.safety_triage.risk_level) : '已检查' },
  ];

  return (
    <div className="rounded-lg border bg-slate-50 p-3">
      <div className="flex flex-wrap items-center gap-2">
        <span className="text-xs font-semibold text-gray-800">RAG 闭环追踪</span>
        {bridged ? <EvidenceBadge text="中英桥接" color="blue" /> : null}
        {queryCount > 1 ? <EvidenceBadge text={`${queryCount} 组 query 融合`} color="amber" /> : null}
        <EvidenceBadge text="本地来源" color="emerald" />
      </div>
      <div className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-4">
        {auditItems.map(item => (
          <div key={item.label} className="rounded border bg-white px-2.5 py-2">
            <div className="text-[10px] font-semibold text-gray-500">{item.label}</div>
            <div className="mt-0.5 truncate text-xs font-semibold text-gray-900">{item.value}</div>
          </div>
        ))}
      </div>
      {message.answer_strategy?.length ? (
        <div className="mt-3 rounded border bg-white px-3 py-2 text-xs text-gray-700">
          <span className="font-semibold text-gray-900">{questionTypeLabel(message.question_type)}</span>
          <span className="mx-2 text-gray-400">·</span>
          <span>{message.answer_strategy.join(' → ')}</span>
        </div>
      ) : null}
      <div className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-6">
        <TraceMetric label="来源 chunks" value={evidenceCount} />
        <TraceMetric label="来源文献" value={sourceCount} />
        <TraceMetric label="来源卡" value={cardCount} />
        <TraceMetric label="追踪步骤" value={traceCount} />
        <TraceMetric label="支撑 claims" value={`${supported}/${claimCount}`} />
        <TraceMetric label="引用覆盖" value={`${coverage}%`} />
      </div>
      {message.reasoning_trace?.length ? (
        <div className="mt-3 space-y-1.5">
          {message.reasoning_trace.slice(0, 4).map((step, idx) => (
            <div key={`${step.step}-${idx}`} className="rounded border bg-white px-2.5 py-2 text-xs text-gray-700">
              <span className="font-semibold text-gray-900">S{idx + 1}</span>
              <span className="mx-2 text-gray-400">·</span>
              <span>{step.step}</span>
              {step.citations?.length ? <span className="ml-2 font-mono text-[10px] text-gray-500">{step.citations.join(', ')}</span> : null}
            </div>
          ))}
        </div>
      ) : null}
      {message.evidence_cards?.length ? (
        <div className="mt-3 grid gap-2 sm:grid-cols-2">
          {message.evidence_cards.slice(0, 4).map(card => (
            <div key={`${card.card_id}-${card.chunk_id}`} className="rounded border bg-white p-2">
              <div className="flex flex-wrap items-center gap-1.5 text-[11px]">
                <span className="font-semibold text-gray-900">{card.card_id}</span>
                <EvidenceBadge text={evidenceRoleLabel(card.role)} color="gray" />
                {card.support_level ? <EvidenceBadge text={supportLevelLabel(card.support_level)} color={card.support_level === 'direct' ? 'green' : 'amber'} /> : null}
                <span className="font-mono text-gray-500">{card.chunk_id}</span>
              </div>
              <div className="mt-1 line-clamp-2 text-[11px] leading-relaxed text-gray-600">{card.key_text}</div>
            </div>
          ))}
        </div>
      ) : null}
      {message.query_rewrites?.length ? (
        <div className="mt-3 flex flex-wrap gap-1.5">
          {message.query_rewrites.slice(0, 8).map(item => (
            <span key={`${item.source}-${item.rewrite}`} className="rounded border bg-white px-2 py-1 text-[11px] text-gray-600">
              <span className="font-semibold text-gray-800">{item.source}</span>
              <span className="mx-1 text-gray-400">→</span>
              <span className="font-mono">{item.rewrite}</span>
            </span>
          ))}
        </div>
      ) : null}
      {message.search_queries?.length > 1 ? (
        <div className="mt-2 space-y-1">
          {message.search_queries.map((query, idx) => (
            <div key={`${query}-${idx}`} className="rounded bg-white px-2 py-1 font-mono text-[11px] text-gray-600">
              Q{idx + 1}: {query}
            </div>
          ))}
        </div>
      ) : null}
    </div>
  );
}

function questionTypeLabel(type) {
  const labels = {
    mechanism_explanation: '机制解释型',
    endpoint_definition: '终点定义型',
    survival_benefit_judgement: '生存获益判断型',
    safety_judgement: '安全判断型',
    efficacy_judgement: '疗效判断型',
    population_applicability: '人群适用型',
    study_design: '研究设计型',
    evidence_summary: '来源汇总型',
  };
  return labels[type] || '来源问答型';
}

function evidenceRoleLabel(role) {
  const labels = {
    endpoint_definition: '终点定义',
    survival_outcome: '生存结局',
    safety: '安全性',
    endpoint: '终点',
    population: '人群',
    intervention: '干预',
    method: '方法',
    context: '背景',
  };
  return labels[role] || role || '来源';
}

function supportLevelLabel(level) {
  const labels = {
    direct: '直接来源',
    supporting: '辅助来源',
    context: '背景来源',
  };
  return labels[level] || level || '来源';
}

function TraceMetric({ label, value }) {
  return (
    <div className="rounded border bg-white px-2.5 py-2">
      <div className="truncate text-sm font-semibold text-gray-800">{value}</div>
      <div className="mt-0.5 text-[10px] text-gray-500">{label}</div>
    </div>
  );
}

function Metric({ label, value }) {
  return (
    <div className="rounded border bg-gray-50 p-2">
      <div className="truncate text-sm font-semibold text-gray-800">{value}</div>
      <div className="mt-1 text-[11px] text-gray-500">{label}</div>
    </div>
  );
}

function triageLabel(category) {
  const labels = {
    medical_evidence_question: '文献来源问题',
    general_medical_question: '一般医学问题',
    personal_medical_advice: '个人诊疗建议',
    urgent_or_emergency: '急症风险',
  };
  return labels[category] || category || '未分类';
}

function riskLabel(level) {
  const labels = { low: '低风险', medium: '中风险', high: '高风险' };
  return labels[level] || level || '未知风险';
}
