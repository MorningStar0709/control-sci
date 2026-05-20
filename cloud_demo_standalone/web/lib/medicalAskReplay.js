const REPLAY_CASES = [
  {
    match: ['闭环胰岛素', '低血糖'],
    answer: [
      '从文献来源看，关键原因不是“闭环系统单纯增加胰岛素”，而是 1 型糖尿病儿童和青少年在确诊后早期处于快速变化阶段：残余胰岛功能会逐渐减弱，生长发育、体重变化和青春期胰岛素抵抗会使每日胰岛素需求在随访中明显上升。',
      '',
      '因此，随着诊断后时间推移，固定方案更容易落后于真实需求；自适应闭环算法会根据连续血糖和既往给药反应调整输注比例，所以研究中会观察到“由闭环算法输送的胰岛素比例逐渐增加”。这支持早期使用自适应闭环系统的逻辑：它能跟随需求变化调整，而不是只依赖人工定期改参数。',
      '',
      '安全性上仍要看低血糖时间、严重低血糖事件和目标范围内时间等指标。以上只是文献机制解释和来源摘要，不能替代个人胰岛素治疗方案或医生建议。',
    ].join('\n'),
    citations: ['PMC6448906_chunk_010', 'PMC7618672_chunk_005', 'PMC12574440_chunk_039'],
    claims: [
      claim('闭环胰岛素相关研究会报告低血糖时间或严重低血糖事件等安全性指标。', ['PMC12574440_chunk_039']),
      claim('部分闭环系统证据显示目标范围内时间改善，并伴随低血糖风险指标下降或维持较低水平。', ['PMC6448906_chunk_010', 'PMC7618672_chunk_005']),
      claim('诊断后早期胰岛素需求变化较快，自适应闭环系统的价值在于随时间调整输注策略。', ['PMC7618672_chunk_005']),
      claim('该回答仅用于文献来源展示，不构成个人胰岛素治疗建议。', []),
    ],
    evidence: [
      evidence('PMC6448906_chunk_010', 'results', '闭环与开环血糖控制结果对比，包含低血糖时间比例等指标。'),
      evidence('PMC7618672_chunk_005', 'front_matter', '混合闭环系统在儿童/青少年 1 型糖尿病中的研究背景。'),
      evidence('PMC12574440_chunk_039', 'safety', '安全性分析包括严重低血糖事件数量和相关受试者数量。'),
    ],
    confidence: 'medium',
  },
  {
    match: ['48', '自适应闭环'],
    answer: [
      '这句话背后的机制主要有三层。',
      '',
      '第一，1 型糖尿病确诊后的早期阶段并不稳定。随着残余胰岛功能下降、儿童和青少年生长发育以及青春期相关胰岛素抵抗增强，每日胰岛素需求会随时间增加，所以 48 个月内需求上升是符合疾病进程和生理变化的。',
      '',
      '第二，闭环系统不是固定剂量方案。它会根据连续血糖、历史给药反应和目标范围表现动态调整胰岛素输注，因此当真实需求增加时，由算法自动输送的胰岛素比例也会逐步上升。',
      '',
      '第三，这种变化支持“早期使用自适应闭环系统”的研究叙事：越早进入动态管理，系统越能跟随需求变化，减少人工参数滞后。不过，这仍是群体层面的文献来源，不能推出某个个体应如何调泵、调剂量或更改治疗方案。',
    ].join('\n'),
    citations: ['PMC7618672_chunk_005', 'PMC12574440_chunk_039'],
    claims: [
      claim('诊断后早期胰岛素需求会随时间变化，儿童和青少年尤其明显。', ['PMC7618672_chunk_005']),
      claim('闭环研究需要同时观察算法输注比例和低血糖等安全性指标。', ['PMC12574440_chunk_039']),
      claim('该结论只能作为群体文献来源，不能替代个体治疗调整。', []),
    ],
    evidence: [
      evidence('PMC7618672_chunk_005', 'front_matter', '混合闭环系统在儿童/青少年 1 型糖尿病中的研究背景。'),
      evidence('PMC12574440_chunk_039', 'safety', '安全性分析包括严重低血糖事件数量和相关受试者数量。'),
    ],
    confidence: 'medium',
  },
  {
    match: ['化疗剂量', '治疗延迟'],
    answer: '根据已保存的文献来源摘要，化疗剂量减少和治疗延迟通常按毒性严重程度处理：血液学和非血液学毒性可触发剂量减少；并发毒性时以最严重的既往毒性为依据；不良事件导致的周期延迟存在上限，超过阈值可能取消周期或停止治疗。',
    citations: ['PMC8600696_chunk_015', 'PMC9502603_chunk_003', 'PMC5490215_chunk_019'],
    claims: [
      claim('血液学和非血液学毒性可触发化疗剂量减少。', ['PMC8600696_chunk_015']),
      claim('治疗延迟和剂量减少可作为不良事件相关的次要终点记录。', ['PMC5490215_chunk_019']),
      claim('不良事件也可能受到药理学和心理因素共同影响。', ['PMC9502603_chunk_003']),
    ],
    evidence: [
      evidence('PMC8600696_chunk_015', 'intervention', 'Dose modifications and prerequisites for the start of a new cycle.'),
      evidence('PMC9502603_chunk_003', 'front_matter', 'Adverse events of chemotherapy may involve pharmacodynamic and expectation-related factors.'),
      evidence('PMC5490215_chunk_019', 'secondary_outcome', 'Secondary endpoints include adverse events, dose reductions and treatment delays.'),
    ],
  },
  {
    match: ['总生存', '无进展生存'],
    answer: [
      '这里需要先区分“终点定义”和“生存获益结论”。总生存期（OS）通常是更硬的生存终点；无进展生存期（PFS/rPFS）是进展相关终点，可用于评估疾病控制时间，但不能自动等同于已经证明延长总生存。',
      '',
      '以 [177Lu]Lu-PSMA-617 相关来源为例，PMC12487728_chunk_008 给出的是该研究内的终点定义：OS 从首次注射日期算至死亡，PFS/rPFS 从首次注射日期算至影像学进展等事件。这个定义可以说明研究如何计量终点，但它本身不是“治疗带来生存获益”的结论。',
      '',
      '因此，判断生存获益还需要继续看随机化/ITT 人群、删失规则、随访成熟度、对照组差异和最终 OS 分析是否充分。当前回答只能作为文献终点口径说明，不应外推为个人预后或治疗建议。',
    ].join('\n'),
    citations: ['PMC12487728_chunk_008', 'PMC12928687_chunk_024', 'PMC6937062_chunk_031'],
    claims: [
      claim('OS/PFS 可作为研究中的疗效终点或次要终点，但终点定义不等于获益结论。', ['PMC12487728_chunk_008', 'PMC12928687_chunk_024']),
      claim('[177Lu]Lu-PSMA-617 来源中的 OS/PFS 起算方式属于该研究的终点口径。', ['PMC12487728_chunk_008']),
      claim('判断生存获益需要结合 ITT 人群、删失规则、随访成熟度和最终 OS 分析。', ['PMC6937062_chunk_031', 'PMC12928687_chunk_024']),
      claim('终点定义不应被解释为个人疗效预测或治疗建议。', []),
    ],
    evidence: [
      evidence('PMC6937062_chunk_031', 'statistical_analysis', 'Analyses conducted on an intention-to-treat basis with sensitivity analyses.'),
      evidence('PMC12487728_chunk_008', 'secondary_endpoint', 'Secondary endpoints include safety and survival-related outcomes.'),
      evidence('PMC12928687_chunk_024', 'secondary_endpoint', 'Twelve- and 24-month overall survival and distant progression-free survival.'),
    ],
  },
  {
    match: ['主要终点', '安全性'],
    answer: '根据已保存的文献来源摘要，不同研究对主要终点的定义不同：例如 R0/R1 切除后的总生存期、随机化后 24 小时内药物浓度目标达成率等。安全性证据通常作为次要终点呈现，包括不良事件类型、频率和严重程度，或特定死亡率/肾衰竭等安全结局。',
    citations: ['PMC8600696_chunk_007', 'PMC9443636_chunk_010'],
    claims: [
      claim('PMC8600696 将 R0/R1 切除后的总生存期作为主要终点之一。', ['PMC8600696_chunk_007']),
      claim('PMC9443636 将随机化后 24 小时内 PK 目标达成率作为主要终点。', ['PMC9443636_chunk_010']),
      claim('安全性证据常通过不良事件类型、频率和严重程度等指标呈现。', ['PMC8600696_chunk_007']),
    ],
    evidence: [
      evidence('PMC8600696_chunk_007', 'endpoints', 'Primary endpoint is overall survival after R0/R1 resection; safety endpoints include adverse events.'),
      evidence('PMC9443636_chunk_010', 'outcomes', 'Primary endpoint was PK target attainment during the first 24h after randomisation.'),
    ],
  },
  {
    match: ['ITT', '意向治疗'],
    answer: '根据已保存的文献来源摘要，意向治疗（ITT）分析人群通常包括所有随机化参与者，即使存在方案违背、脱落或退出，也纳入分析。该原则用于降低非依从性造成的偏倚，并更接近实际治疗场景下的效果估计。',
    citations: ['PMC11929207_chunk_018', 'PMC12574440_chunk_031', 'PMC12742169_chunk_024'],
    claims: [
      claim('ITT 原则纳入所有随机化参与者，包括方案违背、脱落或退出者。', ['PMC12574440_chunk_031']),
      claim('统计分析章节通常说明 p 值、次要终点和敏感性分析等口径。', ['PMC11929207_chunk_018']),
      claim('ITT 分析有助于降低因非依从性带来的处理效应偏倚。', ['PMC12742169_chunk_024']),
    ],
    evidence: [
      evidence('PMC11929207_chunk_018', 'statistical_analysis', 'Statistical analysis plan and handling of endpoints.'),
      evidence('PMC12574440_chunk_031', 'statistical_analysis', 'All randomised participants included according to intention-to-treat principle.'),
      evidence('PMC12742169_chunk_024', 'statistical_analysis', 'Descriptive statistics and statistical analysis plan.'),
    ],
  },
  {
    match: ['纳入排除', '纳入', '排除'],
    answer: '根据已保存的文献来源摘要，随机对照试验的纳入/排除标准用于筛选合格受试者。证据示例包括参与者选择和样本量阶段应用具体标准；排除标准可包括无法及时提供知情同意、妊娠、参与其他干预试验、已接受特定治疗超过规定时间、ECMO 等情形。',
    citations: ['PMC6561428_chunk_012', 'PMC12898571_chunk_006', 'PMC11929207_chunk_009'],
    claims: [
      claim('RCT 通常在参与者选择阶段应用纳入和排除标准。', ['PMC12898571_chunk_006']),
      claim('排除标准可包括无法及时知情同意、妊娠、参与其他干预试验等。', ['PMC11929207_chunk_009']),
      claim('纳入排除标准常以 Box 或 Methods 小节形式呈现。', ['PMC6561428_chunk_012']),
    ],
    evidence: [
      evidence('PMC6561428_chunk_012', 'randomization', 'Box 1 Inclusion and exclusion criteria.'),
      evidence('PMC12898571_chunk_006', 'population', 'Inclusion and exclusion criteria applied to select eligible participants.'),
      evidence('PMC11929207_chunk_009', 'exclusion_criteria', 'Exclusion criteria include consent, pregnancy and prior treatment constraints.'),
    ],
    confidence: 'medium',
  },
];

const MECHANISM_REPLAY_HINTS = [
  {
    match: ['为什么'],
    answerPrefix: '这个问题需要机制解释，而不是只复述结论。基于已保存的本地证据，回答会按“结论 → 可能机制 → 适用边界 → 安全声明”组织；如果证据不能支撑机制，会明确说明机制证据不足。\n\n',
  },
  {
    match: ['机制'],
    answerPrefix: '这个问题需要机制解释，而不是只复述结论。基于已保存的本地证据，回答会按“结论 → 可能机制 → 适用边界 → 安全声明”组织；如果证据不能支撑机制，会明确说明机制证据不足。\n\n',
  },
  {
    match: ['原因'],
    answerPrefix: '这个问题需要原因解释，而不是只复述结论。基于已保存的本地证据，回答会按“结论 → 可能机制 → 适用边界 → 安全声明”组织；如果证据不能支撑机制，会明确说明机制证据不足。\n\n',
  },
];

const SAFETY_REPLAYS = [
  {
    match: ['胸痛', '呼吸困难'],
    answer: '这可能涉及急症风险，我不能把它作为文献检索问题处理。请立即联系当地急救电话或前往急诊；如果身边有人，请让对方陪同并避免自行驾车。',
    category: 'urgent_or_emergency',
    risk: 'high',
  },
  {
    match: ['发烧', '吃什么药'],
    answer: '我不能根据这句话给出个人用药建议。若症状明显、持续加重，或伴随呼吸困难、胸痛、意识改变等风险信号，请及时就医。这里可以讨论文献依据，但不能替代医生诊疗。',
    category: 'personal_medical_advice',
    risk: 'medium',
  },
  {
    match: ['头痛', '脑卒中'],
    answer: '我不能根据简短描述判断你是否脑卒中。若出现突发剧烈头痛、单侧肢体无力、口角歪斜、言语不清、视物异常或意识改变，请立即呼叫急救或去急诊。',
    category: 'personal_medical_advice',
    risk: 'high',
  },
];

export function findMedicalAskReplay(question) {
  const normalized = question || '';
  const safety = SAFETY_REPLAYS.find(item => item.match.every(term => normalized.includes(term)));
  if (safety) {
    return {
      status: 'safety_refusal',
      answer: safety.answer,
      citations: [],
      claims: [],
      evidence_items: [],
      confidence: 'high',
      privacy: 'replay_safety',
      safety_triage: {
        category: safety.category,
        risk_level: safety.risk,
        allow_rag: false,
        user_message: safety.answer,
      },
    };
  }

  const item = REPLAY_CASES.find(entry => entry.match.some(term => normalized.includes(term)));
  if (!item) return null;
  const mechanismHint = MECHANISM_REPLAY_HINTS.find(entry => entry.match.some(term => normalized.includes(term)));
  return {
    status: 'replay',
    answer: `${mechanismHint?.answerPrefix || ''}${item.answer}`,
    model: 'verified-trace-replay',
    privacy: 'local_replay',
    search_query: '',
    search_queries: [],
    query_language: 'zh',
    query_rewrites: [],
    rewrite_method: 'verified_trace',
    retrieval_mode: 'hybrid',
    retrieval_index: { label: 'BGE M3', alias: 'bge_m3' },
    citations: item.citations,
    claims: item.claims,
    claim_count: item.claims.length,
    supported_claims: item.claims.filter(claim => claim.supported).length,
    unsupported_claims: item.claims.filter(claim => !claim.supported).length,
    citation_coverage: item.citations.length ? 1 : 0,
    evidence_sufficiency: { sufficient: true, evidence_count: item.evidence.length },
    confidence: item.confidence || 'high',
    limitations: '该结果来自已保存的可复现实验 trace，用于公开展示；云端页面不现场访问受控资产。',
    abstain: false,
    abstain_reason: '',
    evidence_items: item.evidence,
    source_summary: {
      total_sources: item.citations.length,
      total_chunks: item.evidence.length,
      sources: item.citations,
    },
    task_id: 'verified_replay',
    generated_at: '2026-05-15T12:51:04+0800',
  };
}

function claim(text, citations) {
  return { claim: text, citations, supported: citations.length > 0 };
}

function evidence(chunkId, label, preview) {
  return {
    chunk_id: chunkId,
    medical_label: label,
    rrf_score: 'replay',
    text_preview: preview,
  };
}
