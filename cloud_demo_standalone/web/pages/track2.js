import { useCallback, useEffect, useMemo, useState } from 'react';
import SectionWrapper from '../components/SectionWrapper';
import ErrorCallout from '../components/workbench/ErrorCallout';
import EvidenceBadge from '../components/workbench/EvidenceBadge';
import LoadingDots from '../components/workbench/LoadingDots';
import RuntimeSummary from '../components/workbench/RuntimeSummary';
import StepCard from '../components/workbench/StepCard';
import StatusPill from '../components/workbench/StatusPill';
import WorkbenchLoadingCard from '../components/workbench/WorkbenchLoadingCard';
import { apiGet, getApiTask, startApiTask } from '../lib/apiClient';
import useSessionState from '../lib/useSessionState';

const CLIENT_TASK_TIMEOUT_MS = 90000;

const agentPainPoints = [
  {
    title: '人工语料产线成本高',
    desc: '文献检索、解析调参、视觉质检、出题、评测和排行榜更新累计约 558 工时。',
  },
  {
    title: '脚本流水线不可恢复',
    desc: '固定 pipeline 只能按顺序跑，缺少失败降级、checkpoint 和质量验收协议。',
  },
  {
    title: '云端边界难执行',
    desc: '公开材料、私有原文、chunk、索引和微调产物需要由系统自动路由，而不是人工记规则。',
  },
  {
    title: '跨模态质检难规模化',
    desc: '图片、公式、表格和正文需要统一审计，不能依赖人工逐篇抽查。',
  },
];

const agentMetrics = [
  ['14', 'Intent 能力'],
  ['4', '推理轨道'],
  ['9,207', '视觉审计判决'],
  ['391s', '数据飞轮闭环'],
  ['62ms', '故障降级案例'],
  ['17', '跨领域零改动模块'],
];

const validationDimensions = [
  ['D1', '复杂文档理解', '28,514 chunk、4,996 共现 chunk、多格式解析'],
  ['D2', '难点攻克', '视觉审计、公式识别对比、QLoRA 反直觉发现'],
  ['D3', '任务规划', '自然语言目标转 Intent、DAG、Verifier 闭环'],
  ['D4', '稳定复现', '三层容错、失败恢复、LogStep、复现命令'],
  ['D5', '生态价值', '双赛道联动、开源资产、跨领域迁移'],
];

const executionProtocol = [
  ['意图路由', '自然语言目标转成可组合 intent 序列'],
  ['资源调度', '按 data_policy 选择公开 API、回放产物或离线脚本'],
  ['执行与校验', '执行、检查、重试、降级和写入日志'],
  ['日志与来源', '输出摘要、来源产物和可复现命令'],
];

function resourceColor(resource) {
  if (resource === 'api') return 'blue';
  if (resource === 'local_gpu') return 'green';
  if (resource === 'script') return 'gray';
  return 'yellow';
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

export default function Track2Page({ runtimeConfig }) {
  const [templates, setTemplates] = useState([]);
  const [capabilities, setCapabilities] = useState(null);
  const [session, setSession] = useSessionState('controlmind.track2.session.v1', {
    query: '',
    selectedTemplateId: '',
    result: null,
    loading: false,
    error: null,
    pendingTask: null,
  });
  const { query, result, loading, error, selectedTemplateId } = session;
  const pendingTask = useMemo(
    () => session.pendingTask || (session.pendingTaskId ? { id: session.pendingTaskId } : null),
    [session.pendingTask, session.pendingTaskId],
  );
  const patchSession = useCallback((patch) => setSession(prev => ({ ...prev, ...patch })), [setSession]);

  const pollPlanTask = useCallback(async function pollPlanTask(task) {
    if (!task?.id) return;
    if (isClientTaskExpired(task)) {
      patchSession({ loading: false, pendingTask: null, pendingTaskId: '', error: '任务状态已过期，请重新生成计划。', result: { status: 'failed', message: '任务状态已过期，请重新生成计划。', steps: [] } });
      return;
    }
    for (;;) {
      if (isClientTaskExpired(task)) {
        patchSession({ loading: false, pendingTask: null, pendingTaskId: '', error: '任务超时，请重新生成计划。', result: { status: 'failed', message: '任务超时，请重新生成计划。', steps: [] } });
        return;
      }
      const response = await getApiTask(task.id, { timeoutMs: 12000 });
      if (!response.ok) {
        patchSession({ loading: false, pendingTask: null, pendingTaskId: '', error: response.error, result: { status: 'failed', message: response.error, steps: [] } });
        return;
      }
      if (response.data.status === 'running') {
        await new Promise(resolve => setTimeout(resolve, 1000));
        continue;
      }
      const nextResult = response.data.status === 'done' ? response.data.data : { status: 'failed', message: response.data.error, steps: [] };
      patchSession({ loading: false, pendingTask: null, pendingTaskId: '', result: nextResult, error: nextResult.status === 'failed' ? nextResult.message : null });
      return;
    }
  }, [patchSession]);

  useEffect(() => {
    if (loading && !pendingTask?.id) {
      patchSession({ loading: false, pendingTask: null, pendingTaskId: '' });
      return;
    }
    if (pendingTask?.id && loading) pollPlanTask(pendingTask);
  }, [loading, patchSession, pendingTask, pollPlanTask]);

  const executeWithQuery = useCallback(async function executeWithQuery(task) {
    if (!task.trim()) return;
    const action = resolveTrack2Action(selectedTemplateId, task);
    patchSession({ result: null, error: null, query: task, pendingTask: null, pendingTaskId: '' });
    try {
      const response = await startApiTask(action.path, {
        query: task,
        live: action.live,
        artifact_kind: action.artifactKind,
        planner: runtimeConfig.t2_planner,
        api_provider: runtimeConfig.api_provider,
        privacy_policy: runtimeConfig.privacy_policy,
      }, { runtimeConfig, timeoutMs: action.timeoutMs });
      if (!response.ok) {
        patchSession({ loading: false, error: response.error, result: { status: 'failed', message: response.error, steps: [] } });
        return;
      }
      patchSession({ loading: true, pendingTask: createPendingTask(response.data.id), pendingTaskId: '' });
    } finally {
    }
  }, [patchSession, runtimeConfig, selectedTemplateId]);

  useEffect(() => {
    apiGet('/api/demo/track2/templates').then(r => {
      if (!r.ok) return;
      const loaded = r.data.templates || [];
      setTemplates(loaded);
      const demoTask = loaded.find(t => t.id === 'check_index') || loaded[0];
      if (demoTask && !query) patchSession({ query: demoTask.goal, selectedTemplateId: demoTask.id });
    });
    apiGet('/api/demo/capabilities').then(r => r.ok && setCapabilities(r.data));
    // Initial template hydration only; live task/session state is restored separately.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function execute() {
    return executeWithQuery(query);
  }

  async function validateChain() {
    const task = query?.trim() || '验收赛道二 Agent 工作流：意图识别 → DAG 生成 → 资源调度 → 执行摘要 → 来源产物核验';
    patchSession({ result: null, error: null, query: task, pendingTask: null, pendingTaskId: '' });
    const response = await startApiTask('/api/demo/track2/validate_chain', {
      query: task,
      planner: runtimeConfig.t2_planner,
      api_provider: runtimeConfig.api_provider,
      privacy_policy: runtimeConfig.privacy_policy,
    }, { runtimeConfig, timeoutMs: 45000 });
    if (!response.ok) {
      patchSession({ loading: false, error: response.error, result: { status: 'failed', message: response.error, steps: [] } });
      return;
    }
    patchSession({ loading: true, pendingTask: createPendingTask(response.data.id), pendingTaskId: '' });
  }

  const steps = result?.steps || [];
  const intents = capabilities?.intents || capabilities?.capabilities || [];
  const resourceTypes = Object.keys(capabilities?.resource_scheduler_config?.resource_types || {});
  const currentAction = resolveTrack2Action(selectedTemplateId, query);
  const resultMode = getResultModeMeta(result);

  return (
    <SectionWrapper>
      <div className="custom-screen space-y-6">
        <div>
          <h1 className="text-gray-800 text-3xl font-semibold sm:text-4xl mb-2">赛道二：ControlMind Data Agent</h1>
          <p className="text-gray-600 text-sm">把科学文档语料生产从脚本流水线升级为可规划、可恢复、可审计的 Agent 执行协议。</p>
              <p className="mt-1 text-[11px] text-gray-500">前台以来源核验和 trace 回放为主，不把评审页变成长任务控制台；主按钮只回放 Agent 协议闭环。</p>
        </div>

        <RuntimeSummary runtimeConfig={runtimeConfig} />
        {error && <ErrorCallout message={error} hint="Agent dry-run 超时或失败时，不影响能力注册表和可复现命令展示。" />}

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-3">
          {agentPainPoints.map(item => (
            <div key={item.title} className="rounded-lg border border-gray-200 bg-white p-4">
              <div className="text-sm font-semibold text-gray-900">{item.title}</div>
              <div className="mt-2 text-xs leading-5 text-gray-600">{item.desc}</div>
            </div>
          ))}
        </div>

        <div className="grid grid-cols-1 xl:grid-cols-3 gap-4">
          <div className="xl:col-span-2 rounded-lg border border-gray-200 bg-white p-5">
            <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-3">
              <div>
                <div className="text-sm font-semibold text-gray-900">Agent 执行协议</div>
                <div className="mt-1 text-xs text-gray-500">不是固定 pipeline，而是目标解析、资源调度、验收回放和日志审计的组合协议。</div>
              </div>
              <StatusPill status="validated" label="调度与验收层" />
            </div>
            <div className="mt-4 grid grid-cols-1 md:grid-cols-4 gap-3">
              {executionProtocol.map(([title, desc]) => (
                <div key={title} className="rounded border border-gray-100 bg-gray-50 px-3 py-3">
                  <div className="text-xs font-semibold text-gray-900">{title}</div>
                  <div className="mt-2 text-[11px] leading-5 text-gray-600">{desc}</div>
                </div>
              ))}
            </div>
            <div className="mt-4 grid grid-cols-2 md:grid-cols-3 gap-3">
              {agentMetrics.map(([value, label]) => (
                <div key={label} className="rounded border border-gray-100 bg-white px-3 py-3">
                  <div className="font-mono text-lg font-semibold text-gray-900">{value}</div>
                  <div className="mt-1 text-[11px] text-gray-500">{label}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-lg border border-gray-200 bg-white p-5">
            <div className="text-sm font-semibold text-gray-900">能力验收维度</div>
            <div className="mt-1 text-xs text-gray-500">概括系统在复杂文档处理、Agent 编排、可靠执行和开放复用方面的主要验证依据。</div>
            <div className="mt-4 space-y-2">
              {validationDimensions.map(([id, title, desc]) => (
                <div key={id} className="rounded border border-gray-100 bg-gray-50 px-3 py-2">
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-[11px] font-semibold text-gray-900">{id}</span>
                    <span className="text-xs font-semibold text-gray-800">{title}</span>
                  </div>
                  <div className="mt-1 text-[11px] leading-5 text-gray-600">{desc}</div>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="rounded-lg border border-emerald-100 bg-emerald-50 px-5 py-4">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
            <div>
              <div className="text-sm font-semibold text-emerald-950">评审验收路径</div>
              <div className="mt-1 text-xs leading-5 text-emerald-900">
                默认先看 Agent 协议、能力矩阵和关键验证依据；模板按钮只核验既有产物，主按钮用于核验 intent、DAG、资源选择、输出摘要和来源产物。
              </div>
            </div>
            <button onClick={validateChain} disabled={loading} className="w-full md:w-auto px-4 py-2 bg-emerald-700 text-white text-xs rounded disabled:opacity-50">
              <BusyLabel active={loading} busyText="核验中" idleText="核验 Agent 协议" />
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="space-y-4">
            <StepCard index="A" title="任务模板" desc="选择一个已验证任务，或输入目标查看规划回放。" status={query ? 'done' : 'pending'}>
              <div className="space-y-2">
                {templates.map(t => (
                  <button key={t.id} onClick={() => patchSession({ query: t.goal, selectedTemplateId: t.id, result: null })} className={`w-full text-left border rounded-lg p-3 hover:bg-gray-50 ${selectedTemplateId === t.id ? 'border-gray-900 bg-gray-50' : ''}`}>
                    <div className="flex items-start justify-between gap-2">
                      <div className="text-sm font-medium text-gray-800">{t.label}</div>
                      <StatusPill status={resolveTrack2Action(t.id, t.goal).status} />
                    </div>
                    <div className="text-[11px] text-gray-500 mt-1">{t.goal}</div>
                    <div className="mt-2 text-[10px] text-gray-400">{resolveTrack2Action(t.id, t.goal).label}</div>
                  </button>
                ))}
              </div>
            </StepCard>

            <StepCard index="B" title="能力注册表" desc="来自 agent_capabilities.json。" status={capabilities ? 'done' : 'pending'}>
              <div className="grid grid-cols-2 gap-2 text-xs">
                <div className="border rounded p-2 bg-gray-50">
                  <div className="font-mono text-gray-800">{intents.length || 14}</div>
                  <div className="text-gray-400">Intent</div>
                </div>
                <div className="border rounded p-2 bg-gray-50">
                  <div className="font-mono text-gray-800">{resourceTypes.join(' / ') || 'local + api'}</div>
                  <div className="text-gray-400">Resource</div>
                </div>
              </div>
              {intents.length > 0 && (
                <div className="mt-3 flex flex-wrap gap-1.5">
                  {intents.slice(0, 10).map(intent => (
                    <EvidenceBadge key={intent.intent_id || intent.id} text={intent.intent_id || intent.id} color={resourceColor(intent.resource_type)} />
                  ))}
                  {intents.length > 10 && <EvidenceBadge text={`+${intents.length - 10}`} color="gray" />}
                </div>
              )}
              <p className="text-[11px] text-gray-500 mt-3">公开/脱敏规划任务只回放已验证 trace；原文、医疗、chunk、微调产物不进入云端演示。</p>
            </StepCard>
          </div>

          <div className="lg:col-span-2 space-y-4">
            <StepCard
              index="1"
              title="意图路由"
              desc="把任务目标转成可核验的 intent 序列。"
              status={result ? (result.status === 'ok' ? 'done' : 'failed') : loading ? 'running' : 'pending'}
              actions={(
                <div className="flex flex-wrap gap-2">
                  <button onClick={execute} disabled={!query.trim() || loading} className="px-4 py-2 bg-gray-900 text-white text-xs rounded disabled:opacity-50">
                    <BusyLabel active={loading} busyText="核验中" idleText={currentAction.button} />
                  </button>
                  <button onClick={validateChain} disabled={loading} className="px-4 py-2 bg-sky-600 text-white text-xs rounded disabled:opacity-50">
                    <BusyLabel active={loading} busyText="核验中" idleText="核验 Agent 协议" />
                  </button>
                </div>
              )}
            >
              <textarea value={query} onChange={e => patchSession({ query: e.target.value })} rows={3} placeholder="输入任务目标，例如：核验赛道三医学 RAG 回放资产并输出来源摘要" className="w-full border rounded-lg px-3 py-2 text-sm" />
              <div className="mt-2 flex flex-wrap items-center gap-2 text-xs text-gray-500">
                <StatusPill status={currentAction.status} />
                <span>{currentAction.explain}</span>
              </div>
              {loading && (
                <WorkbenchLoadingCard
                  title="正在读取 Agent 回放计划"
                  desc="正在核验来源或 Agent 协议，完成后会展示步骤、来源和可复现命令。"
                  steps={currentAction.loadingSteps || ['启动核验', '检查来源', '收集结果']}
                  className="mt-3"
                />
              )}
              {!result && !loading && (
                <div className="mt-3 text-xs text-gray-500">已加载任务模板和能力注册表。模板按钮只核验既有产物；长任务只保留可复现命令。</div>
              )}
              {result?.status === 'failed' && (
                <div className="mt-3">
                  <ErrorCallout message={result.message || 'Agent 回放失败'} hint="云端评审页只读取已验证产物；如果回放失败，应检查 trace API 和静态资源是否完整。" />
                </div>
              )}
            </StepCard>

            <StepCard index="2" title="DAG 与资源调度" desc="展示来源核验、协议核验或必要降级的步骤状态。" status={steps.length ? 'done' : loading ? 'running' : result ? 'replay' : capabilities ? 'ready' : 'pending'}>
              {loading && !steps.length ? (
                <WorkbenchLoadingCard
                  title="正在组织 DAG"
                  desc="计划生成后会在这里展示步骤、工具和资源选择。"
                  steps={['拆解任务', '匹配工具', '排列步骤']}
                />
              ) : steps.length ? (
                <div className="space-y-2">
                  {steps.map((s, i) => (
                    <div key={`${s.intent_id}-${i}`} className="border rounded-lg p-3 text-xs">
                      <div className="flex items-center gap-2 mb-1">
                        <span className="font-mono text-gray-400">Step {s.step}</span>
                        <span className="font-semibold text-gray-800">{s.intent_id}</span>
                        <EvidenceBadge text={s.resource || 'script'} color={resourceColor(s.resource)} />
                        <StatusPill status={track2StepStatus(s.status)} />
                      </div>
                      <div className="text-gray-600">{s.intent_name}</div>
                      {s.tools && <div className="text-[11px] text-gray-400 mt-1 font-mono">{s.tools}</div>}
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-xs text-gray-500">
                  {result?.raw_stderr || result?.plan_output || '读取回放后会在这里展示 DAG；未选择模板前先展示左侧 intent 与资源类型。'}
                </div>
              )}
            </StepCard>

            <StepCard index="3" title="核验摘要与来源" desc="显示来源核验摘要、输出文件和可复现命令。" status={result ? (result.status === 'ok' ? 'done' : 'degraded') : loading ? 'running' : 'pending'}>
              {loading && !result ? (
                <WorkbenchLoadingCard
                  title="正在等待核验摘要"
                  desc="后端返回后会显示核验输出、命令和识别到的 Intent。"
                  steps={['核验来源', '收集摘要', '写入来源摘要']}
                />
              ) : result ? (
                <div className="space-y-3">
                  <pre className="border rounded-lg bg-gray-950 text-gray-100 text-[11px] p-3 overflow-auto max-h-72 whitespace-pre-wrap">{result.summary || result.plan_output || result.message || '无摘要输出'}</pre>
                  {result.command && (
                    <div className="border rounded bg-gray-50 px-3 py-2 text-[11px] text-gray-600">
                      <span className="text-gray-400">可复现命令：</span><code>{result.command}</code>
                    </div>
                  )}
                  {result.validation_summary && (
                    <div className="rounded border border-sky-100 bg-sky-50 px-3 py-2 text-xs leading-6 text-sky-900">
                      {result.validation_summary}
                    </div>
                  )}
                  {result.mode && (
                    <div className="border rounded bg-white px-3 py-2 text-xs text-gray-600">
                      <div className="flex flex-wrap items-center gap-2">
                        <span className="text-gray-400">展示模式：</span>
                        <StatusPill status={resultMode.status} label={resultMode.label} />
                        <code className="text-[11px]">{result.mode}</code>
                      </div>
                      <div className="mt-1 text-[11px] text-gray-500 leading-5">{resultMode.explain}</div>
                    </div>
                  )}
                  {result.paper && (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                      <div className="border rounded p-2 bg-gray-50"><div className="font-mono text-gray-800">{result.paper.paper_id}</div><div className="text-gray-400">arXiv 论文</div></div>
                      <div className="border rounded p-2 bg-gray-50"><div className="font-mono text-gray-800">{result.paper.pdf_size_kb} KB</div><div className="text-gray-400">PDF</div></div>
                      <div className="border rounded p-2 bg-gray-50"><div className="font-mono text-gray-800">{result.paper.markdown_chars}</div><div className="text-gray-400">Markdown 字符</div></div>
                    </div>
                  )}
                  {result.questions?.length > 0 && (
                    <div className="border rounded-lg p-3 bg-white">
                      <div className="flex items-center justify-between gap-3 mb-2">
                        <div className="text-[11px] text-gray-400">Quick Proof 题目与评分</div>
                        {result.score_summary?.quick_avg !== null && result.score_summary?.quick_avg !== undefined && (
                          <EvidenceBadge text={`avg ${result.score_summary.quick_avg}`} color="blue" />
                        )}
                      </div>
                      <div className="space-y-2">
                        {result.questions.map(item => (
                          <div key={item.question_id} className="rounded border bg-gray-50 p-2 text-xs">
                            <div className="flex flex-wrap items-center gap-2 mb-1">
                              <EvidenceBadge text={item.dimension} color={resourceColor('api')} />
                              <span className="font-mono text-gray-500">{item.question_id}</span>
                              {item.score !== null && item.score !== undefined && <span className="text-gray-500">score {item.score}</span>}
                            </div>
                            <div className="text-gray-800 leading-6">{item.question}</div>
                            <div className="mt-1 text-gray-500 leading-5">参考：{item.expected_answer}</div>
                            {item.score_reason && <div className="mt-1 text-gray-400 leading-5">评分：{item.score_reason}</div>}
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                  {result.detected_intents?.length > 0 && (
                    <div className="border rounded-lg p-3 bg-white">
                      <div className="text-[11px] text-gray-400 mb-2">识别到的 Intent</div>
                      <div className="space-y-2">
                        {result.detected_intents.map(intent => (
                          <div key={intent.intent_id} className="text-xs">
                            <span className="font-mono text-gray-800">{intent.intent_id}</span>
                            <span className="text-gray-500 ml-2">{intent.description}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                    <div className="border rounded p-2 bg-gray-50"><div className="font-mono">{runtimeConfig.t2_planner}</div><div className="text-gray-400">Planner</div></div>
                    <div className="border rounded p-2 bg-gray-50"><div className="font-mono">已验证回放</div><div className="text-gray-400">展示口径</div></div>
                    <div className="border rounded p-2 bg-gray-50"><div className="font-mono">benchmark/agent/logs</div><div className="text-gray-400">来源产物</div></div>
                  </div>
                  {result.sources?.length > 0 && (
                    <div className="border rounded-lg p-3 bg-white">
                      <div className="text-[11px] text-gray-400 mb-2">验收来源</div>
                      <div className="space-y-1.5">
                        {result.sources.map(item => (
                          <div key={item.path} className="flex items-center justify-between gap-3 text-xs">
                            <span className="text-gray-700">{item.label}</span>
                            <span className="font-mono text-gray-500 truncate">{item.path}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              ) : (
                <div className="text-xs text-gray-500">核验一次模板或 Agent 协议后会显示摘要与来源路径。</div>
              )}
            </StepCard>
          </div>
        </div>
      </div>
    </SectionWrapper>
  );
}

function createPendingTask(id) {
  return {
    id,
    timeoutMs: CLIENT_TASK_TIMEOUT_MS,
    startedAt: Date.now(),
  };
}

function isClientTaskExpired(task) {
  if (!task?.startedAt) return true;
  return Date.now() - task.startedAt > (task.timeoutMs || CLIENT_TASK_TIMEOUT_MS);
}

function track2StepStatus(status) {
  if (status === 'dry_run') return 'planned';
  if (status === 'validated_artifact') return 'validated';
  return status || 'pending';
}

function resolveTrack2Action(templateId, text) {
  const value = (text || '').toLowerCase();
  const id = templateId || (value.includes('quick proof') || value.includes('飞轮') || value.includes('arxiv') ? 'flywheel' : '');
  const actions = {
    flywheel: {
      path: '/api/demo/track2/artifact_check',
      artifactKind: 'flywheel',
      button: '核验飞轮来源',
      label: '来源核验：PDF / MinerU Markdown / 快速题集 / 已保存评测',
      explain: '只核验已沉淀产物，不调用出题或评测 API；完整飞轮保留可复现命令。',
      status: 'artifact_reuse',
      loadingSteps: ['检查 arXiv PDF', '检查 MinerU Markdown', '检查题集与评测结果'],
      timeoutMs: 45000,
      live: false,
    },
    eval40: {
      path: '/api/demo/track2/artifact_check',
      artifactKind: 'eval40',
      button: '核验抽样来源',
      label: '来源核验：core.json / 四维计划 / leaderboard',
      explain: '核验题库和排行榜来源，不在页面重新跑模型答题和 Judge。',
      status: 'artifact_reuse',
      loadingSteps: ['检查 core.json', '检查 leaderboard', '检查报告引用'],
      timeoutMs: 45000,
      live: false,
    },
    check_index: {
      path: '/api/demo/track2/artifact_check',
      artifactKind: 'check_index',
      button: '核验索引来源',
      label: '来源核验：manifest / 检索资产来源路径',
      explain: '只核验既有索引产物和来源路径，不重建向量索引。',
      status: 'artifact_reuse',
      loadingSteps: ['读取 manifest', '核验检索资产', '汇总来源路径'],
      timeoutMs: 45000,
      live: false,
    },
    evidence_bundle: {
      path: '/api/demo/track2/artifact_check',
      artifactKind: 'evidence_bundle',
      button: '查看验收包',
      label: '来源核验：DATA-TRACE / bundle manifest / README',
      explain: '默认查看和核验已生成验收包；重建脚本作为可复现命令展示。',
      status: 'artifact_reuse',
      loadingSteps: ['检查 DATA-TRACE', '检查 manifest', '检查 README'],
      timeoutMs: 45000,
      live: false,
    },
    visual_audit: {
      path: '/api/demo/track2/artifact_check',
      artifactKind: 'visual_audit',
      button: '核验视觉审计',
      label: '来源核验：visual_audit_results.jsonl / 审计来源',
      explain: '默认核验视觉审计产物，不调用视觉模型；专项复现命令保留在摘要中。',
      status: 'artifact_reuse',
      loadingSteps: ['检查审计结果', '检查能力配置', '检查报告引用'],
      timeoutMs: 45000,
      live: false,
    },
  };
  return actions[id] || {
    path: '/api/demo/agent/plan',
    button: '生成计划',
    label: '规划回放：展示 DAG，不执行长任务',
    explain: '只展示计划回放，不执行真实长任务。',
    status: 'planned',
    loadingSteps: ['识别意图', '生成 DAG', '输出命令'],
    timeoutMs: 45000,
    live: false,
  };
}

function getResultModeMeta(result) {
  const mode = result?.mode || '';
  if (mode === 'live_smoke' || mode === 'live_visual_audit' || mode === 'live_build' || mode === 'live_check' || mode === 'live_sample') {
    return {
      status: 'artifact_reuse',
      label: '来源回放',
      explain: '云端评审页不现场执行长链路；该模式统一解释为已验证 trace 与来源产物回放。',
    };
  }
  if (mode === 'validated_artifact' || mode === 'quick_proof' || mode === 'acceptance') {
    if (mode === 'acceptance') {
      return {
        status: 'validated',
        label: '协议核验',
        explain: '本次回放 Agent 协议闭环：意图、DAG、资源调度、摘要和来源产物都能回指到注册表、代码和报告。',
      };
    }
    return {
      status: 'artifact_reuse',
      label: '来源核验',
      explain: '本次不重跑长任务，而是核验已经沉淀的产物、来源路径和可复现命令。',
    };
  }
  return {
    status: 'planned',
    label: '规划',
    explain: '本次主要展示计划或摘要。',
  };
}
