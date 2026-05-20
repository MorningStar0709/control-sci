const dimensionNames = {
  A: '概念检索',
  B: '多步推理',
  C: '条件敏感',
  D: '开放设计',
};

const rubricLabels = {
  feasibility: '可行性',
  method_choice: '方法选择',
  completeness: '完整性',
  innovation: '创新性',
  clarity: '表达清晰度',
};

export function adaptTrack1Question(question = {}, index = 0) {
  const dimension = cleanText(question.dimension || question.dimension_id || '');
  return {
    id: cleanText(question.question_id || question.id || `question-${index + 1}`),
    dimension,
    dimensionLabel: cleanText(question.dimension_label || dimensionNames[dimension] || dimension),
    difficulty: question.difficulty_level || question.difficulty || '',
    questionMarkdown: normalizeDisplayMarkdown(question.question),
    expectedAnswerMarkdown: normalizeDisplayMarkdown(question.expected_answer || question.answer || question.reference_answer),
  };
}

export function adaptTrack1AnswerSample(sample = {}, index = 0) {
  const dimension = cleanText(sample.dimension || '');
  return {
    id: cleanText(sample.id || sample.question_id || `sample-${index + 1}`),
    dimension,
    dimensionLabel: cleanText(sample.dimension_label || dimensionNames[dimension] || dimension),
    difficulty: sample.difficulty_level || sample.difficulty || '',
    score: sample.score,
    questionMarkdown: normalizeDisplayMarkdown(sample.question),
    modelAnswerMarkdown: normalizeDisplayMarkdown(sample.model_answer || sample.answer || '暂无模型回答'),
    expectedAnswerMarkdown: normalizeDisplayMarkdown(sample.expected_answer || sample.reference_answer || '暂无参考答案'),
    scoring: adaptScoringReason(sample.reason || sample.scoring_rationale || ''),
  };
}

export function adaptTrack1ScoreResult(result = {}) {
  const rationale = result.scoring_rationale || result.message || '';
  return {
    ...result,
    scoringRationale: adaptScoringReason(rationale),
    answerSamples: (result.answer_samples || []).map(adaptTrack1AnswerSample),
  };
}

export function adaptScoringReason(reason) {
  const markdown = normalizeDisplayMarkdown(reason);
  const rubric = parseRubricReason(markdown);
  return {
    markdown,
    rubric,
    isRubric: Boolean(rubric),
  };
}

export function normalizeDisplayMarkdown(value) {
  if (value === null || value === undefined) return '';
  if (Array.isArray(value)) {
    return value.map((item, index) => `${index + 1}. ${normalizeDisplayMarkdown(item)}`).join('\n');
  }
  if (typeof value === 'object') {
    return Object.entries(value)
      .map(([key, item]) => `- **${translateKey(key)}**: ${normalizeDisplayMarkdown(item)}`)
      .join('\n');
  }

  let text = String(value)
    .replace(/\r\n/g, '\n')
    .replace(/\\n/g, '\n')
    .replace(/\u00a0/g, ' ')
    .trim();

  if (hasSevereCrossQuestionContamination(text)) {
    return [
      '**该模型回答存在跨题拼接或 OCR 污染，已隐藏原始坏文本。**',
      '',
      '建议重新生成该题答案，或以题目、参考答案和评分理由为准。',
    ].join('\n');
  }

  text = removeCrossQuestionContamination(text);
  text = repairQpOcrDerivation(text);
  text = normalizeRubricText(text);
  text = repairBrokenLatexText(text);
  text = repairAlignedMathBlocks(text);
  text = normalizeLatexCommandSlashes(text);
  text = repairDanglingMathDelimiters(text);
  text = normalizeLatexCommandSlashes(text);
  text = normalizeShortMathTokens(text);
  text = compactOcrDuplicateLines(text);
  text = normalizeControlMathText(text);
  text = ensureMarkdownParagraphBreaks(text);
  text = cleanupMathArtifacts(text);
  return text;
}

function normalizeLatexCommandSlashes(text) {
  return text.replace(
    /\\{2,}(?=(?:nabla|mathbb|left|right|sum|infty|gamma|log|pi|cdot|tilde|theta|tau|frac|begin|end|text|ge|le|quad|min|max)(?:\b|[_{}]))/g,
    '\\'
  );
}

function repairDanglingMathDelimiters(text) {
  let value = text
    .replace(
      /(^|[\n。；;])\s*(\\nabla_\{\\theta_i\}[\s\S]*?\\right\])\s*\$\$/g,
      (_, prefix, expr) => `${prefix}\n\n$$\n${repairPolicyGradientExpression(expr)}\n$$`
    )
    .replace(/\\mathbb\{E\}\s*\{\\tau\s*\\sim\s*\\pi_\{([^}]+)\}\}/g, '\\mathbb{E}_{\\tau \\sim \\pi_{$1}}')
    .replace(/其中\s*\n\s*其中\s*\\tilde\{r\}_i\$/g, '其中 $\\tilde{r}_i$')
    .replace(/其中\s*\\tilde\{r\}_i\$/g, '其中 $\\tilde{r}_i$')
    .replace(/\$\\tilde\{r\}_i\$\s*是/g, '$\\tilde{r}_i$ 是')
    .replace(/(奖励信号。)([一二三四五六七八九十]+、)/g, '$1\n\n$2');
  return value;
}

function normalizeRubricText(text) {
  const prefix = /^评分理由[:：]\s*/;
  if (/^评分理由[:：]\s*Rubric weighted score:/i.test(text)) {
    return text.replace(prefix, '');
  }
  return text;
}

function hasSevereCrossQuestionContamination(text) {
  const hasQpDerivation = /二次规划|\\begin\{aligned\}|J\(x,\s*u\)/.test(text);
  const hasOtherProblem = /教材建议取ρ=10×pz_max|高频极点不会影响系统响应|pz_max_actual|pz_max_est/.test(text);
  const singleCharLines = (text.match(/^\s*[A-Za-zωΩ≤=()_\-−,]\s*$/gm) || []).length;
  return hasQpDerivation && hasOtherProblem || singleCharLines > 24;
}

function repairQpOcrDerivation(text) {
  let value = text.replace(
    /(?:\\begin\{aligned\}\s*)?令\s*\n\s*u\s*\n\s*u\s*为决策变量，约束矩阵形式为：[\s\S]*?b\(x\)=\[−1,\s*\n\s*2\s*\n\s*x[\s\S]*?T\s*\n\s*。/g,
    () => '令 $u$ 为决策变量，约束矩阵形式为：\n\n$$\n\\begin{bmatrix} -1 \\\\ -1 \\\\ -1 \\end{bmatrix}u \\le \\begin{bmatrix} -1 \\\\ \\frac{1}{2}x - 2 \\\\ x - 2 \\end{bmatrix}\n$$\n\n即 $Au \\le b(x)$，其中 $A=[-1,-1,-1]^T$，$b(x)=[-1, x/2-2, x-2]^T$。'
  );
  value = value.replace(
    /(J\(x,\s*u\)\s*&=\s*\\frac\{1\}\{2\}\(x\^2 - 2xu \+ u\^2\) \+ \\frac\{1\}\{2\}u\^2)\s*\\\s*\n\s*(&=\s*\\frac\{1\}\{2\}u\^2 - xu \+ \\frac\{1\}\{2\}x\^2 \+ \\frac\{1\}\{2\}u\^2)\s*\\\s*\n\s*(&=\s*u\^2 - xu \+ \\frac\{1\}\{2\}x\^2)\s*\\?\s*(?:\\end\{aligned\})?/g,
    (_, row1, row2, row3) => `$$\n\\begin{aligned}\n${row1} \\\\\n${row2} \\\\\n${row3}\n\\end{aligned}\n$$`
  );
  return value;
}

function removeCrossQuestionContamination(text) {
  return text
    .replace(/。在\s*\n\s*ω[\s\S]*?试判断原结论[\s\S]*?并说明理由。\s*/g, '。\n\n')
    .replace(/。在\s*ω[\s\S]*?试判断原结论[\s\S]*?并说明理由。\s*/g, '。\n\n')
    .replace(/教材建议取ρ=10×pz_max[\s\S]*?并说明理由。\s*/g, '');
}

function repairBrokenLatexText(text) {
  let repaired = text
    .replace(/[\u200b-\u200f\u2028\u2029]/g, '')
    .replace(/(梯度表达式为：)\s*([\s\S]*?)(?:其中|$)/, (match, prefix, expr) => {
      if (!/RUDER|abla|nabla|mathbb|策略梯度|Policy Gradient/i.test(match)) return match;
      return `${prefix}\n\n$$\n${repairPolicyGradientExpression(expr)}\n$$\n\n其中 `;
    })
    .replace(/\babla_/g, '\\nabla_')
    .replace(/\bmathbb\{/g, '\\mathbb{')
    .replace(/\bleft\[/g, '\\left[')
    .replace(/\bright\]/g, '\\right]')
    .replace(/\bleft\(/g, '\\left(')
    .replace(/\bright\)/g, '\\right)')
    .replace(/\bcdot\b/g, '\\cdot')
    .replace(/\blog\s+pi_/g, '\\log \\pi_')
    .replace(/\bpi_\{/g, '\\pi_{')
    .replace(/\bgamma\^/g, '\\gamma^')
    .replace(/\bsum_\{/g, '\\sum_{')
    .replace(/\binfty\b/g, '\\infty')
    .replace(/\btau\s*\\sim/g, '\\tau \\sim')
    .replace(/\\mathbb\{E\}\s*\{\\?tau\s*\\sim\s*\\?pi\{([^}]+)\}\}/g, '\\mathbb{E}_{\\tau \\sim \\pi_{$1}}')
    .replace(/\\pi\{([^}]+)\}/g, '\\pi_{$1}')
    .replace(/\br\s*~\s*i\b/g, '\\tilde{r}_i')
    .replace(/r\s*\n\s*~\s*\n\s*i\s*\n\s*r\s*\n\s*~\s*[\s\S]{0,12}?i\s*/g, '\\tilde{r}_i ')
    .replace(/其中\s+\\tilde\{r\}_i/g, '\n\n其中 $\\tilde{r}_i$');
  repaired = repaired.replace(/其中\s+\$\\tilde\{r\}_i\$\s*\\tilde\{r\}_i\s*/g, '其中 $\\tilde{r}_i$ ');
  return repaired;
}

function repairAlignedMathBlocks(text) {
  return text.replace(/\\begin\{aligned\}[\s\S]*?\\end\{aligned\}/g, block => {
    if (isProseContaminatedMathBlock(block)) {
      return `\n\n${block
        .replace(/\\begin\{aligned\}/g, '')
        .replace(/\\end\{aligned\}/g, '')
        .trim()}\n\n`;
    }
    let fixed = block
      .replace(/\\\s+\\text\{s\.t\.\}/g, '\\\\\n\\text{s.t.}')
      .replace(/\\\s*&/g, '\\\\\n&')
      .replace(/([^\\])\s+\\{2}\s*&/g, '$1 \\\\\n&')
      .replace(/\\\s*$/gm, '\\\\')
      .replace(/\s+\n/g, '\n')
      .trim();
    fixed = fixed
      .replace(/\\begin\{aligned\}\s*/g, '\\begin{aligned}\n')
      .replace(/\s*\\end\{aligned\}/g, '\n\\end{aligned}')
      .replace(/\\{3,}/g, '\\\\');
    return `\n\n$$\n${fixed}\n$$\n\n`;
  });
}

function isProseContaminatedMathBlock(block) {
  const chineseChars = (block.match(/[\u4e00-\u9fff]/g) || []).length;
  const mathRows = (block.match(/&=|&\s|\\\\/g) || []).length;
  return chineseChars > 24 || /教材|试判断|说明理由|其中|即\s|为决策变量|约束矩阵形式/.test(block) && chineseChars > mathRows * 3;
}

function normalizeShortMathTokens(text) {
  return text
    .replace(/(?<!\$)\bH_\\+infty\b(?!\$)/g, '$H_\\infty$')
    .replace(/(?<!\$)\bH_infty\b(?!\$)/g, '$H_\\infty$')
    .replace(/(?<!\$)\bQP\b(?!\$)/g, 'QP')
    .replace(/(?<!\$)\\min\s+\\frac\{1\}\{2\}u\^T Q u \+ f\^T u \+ c(?!\$)/g, '$\\min \\frac{1}{2}u^T Q u + f^T u + c$')
    .replace(/(?<!\$)\\frac\{1\}\{2\}u\^T Q u \+ f\^T u \+ c(?!\$)/g, '$\\frac{1}{2}u^T Q u + f^T u + c$');
}

function compactOcrDuplicateLines(text) {
  let value = text
    .replace(/将目标函数展开并整理为关于\s*\n\s*将目标函数展开并整理为关于\s*([a-zA-Z])\s*\n\s*的二次型形式\s*\n\s*的二次型形式/g, '将目标函数展开并整理为关于 $1 的二次型形式')
    .replace(/在标准\s*\n\s*Q\s*\n\s*P\s*\n\s*形式\s*\n\s*在标准QP形式/g, '在标准 QP 形式')
    .replace(/：\s*\n\s*：/g, '：');

  const lines = value.split('\n');
  const compacted = [];
  for (const line of lines) {
    const trimmed = line.trim();
    const prev = compacted.length ? compacted[compacted.length - 1].trim() : '';
    if (trimmed && prev && trimmed === prev) continue;
    compacted.push(line);
  }
  return compacted.join('\n');
}

function repairPolicyGradientExpression(expr) {
  let value = String(expr || '')
    .replace(/[\u200b-\u200f]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
  value = value
    .replace(/\babla_/g, '\\nabla_')
    .replace(/\\?theta_i/g, '\\theta_i')
    .replace(/\bmathbb\{/g, '\\mathbb{')
    .replace(/\\mathbb\{E\}\s*\{\\?tau\s*\\sim\s*\\?pi\{\\theta_i\}\}/g, '\\mathbb{E}_{\\tau \\sim \\pi_{\\theta_i}}')
    .replace(/\\?pi\{\\theta_i\}/g, '\\pi_{\\theta_i}')
    .replace(/\bleft\[/g, '\\left[')
    .replace(/\bright\]/g, '\\right]')
    .replace(/\bleft\(/g, '\\left(')
    .replace(/\bright\)/g, '\\right)')
    .replace(/\bsum_\{/g, '\\sum_{')
    .replace(/\binfty\b/g, '\\infty')
    .replace(/\bgamma\^/g, '\\gamma^')
    .replace(/\blog\s+\\?pi_/g, '\\log \\pi_')
    .replace(/\bcdot\b/g, '\\cdot')
    .replace(/\\?tilde\{r\}_i/g, '\\tilde{r}_i')
    .replace(/J_RUDER/g, 'J_{RUDER}');
  return value;
}

function ensureMarkdownParagraphBreaks(text) {
  return text
    .replace(/([。；;])\s*(#{1,6}\s)/g, '$1\n\n$2')
    .replace(/([。；;])\s*([-*+]\s)/g, '$1\n$2')
    .replace(/([。；;])\s*(\d+\.\s)/g, '$1\n$2')
    .replace(/\s+(Rubric 加权评分明细)/g, '\n\n$1');
}

function cleanupMathArtifacts(text) {
  const cleaned = text
    .replace(/\n\$\$\s*\n+\s*\$\$/g, '\n')
    .replace(/\$\$end\{aligned\}/g, '')
    .replace(/\$end\{aligned\}/g, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
  return repairAlignedMathBlocks(cleaned).replace(/\n{3,}/g, '\n\n').trim();
}

function normalizeControlMathText(text) {
  return text
    .replace(/Π(\d+)=\[([^\]]+)\]\^T/g, (_, n, body) => `$\\Pi_${n}=[${toLatexExpr(body)}]^T$`)
    .replace(/Π(\d+)\^TΠ(\d+)/g, (_, a, b) => `$\\Pi_${a}^T\\Pi_${b}$`)
    .replace(/Ξ_?(\d+)\s*=\s*([^。；\n]+)/g, (_, n, body) => `$\\Xi_${n} = ${toLatexExpr(body)}$`)
    .replace(/\$\\Pi_(\d+)\$\^T\$\\Pi_(\d+)\$/g, (_, a, b) => `$\\Pi_${a}^T\\Pi_${b}$`)
    .replace(/\bN(\d+)Π(\d+)/g, (_, n, p) => `$N_${n}\\Pi_${p}$`)
    .replace(/Π(\d+)/g, (_, n) => `$\\Pi_${n}$`)
    .replace(/Ξ_?(\d+)/g, (_, n) => `$\\Xi_${n}$`)
    .replace(/Ω/g, '$\\Omega$')
    .replace(/\bL_i\b/g, '$L_i$')
    .replace(/\bL(\d+)\^T\b/g, (_, n) => `$L_${n}^{T}$`)
    .replace(/\bL(\d+)\b/g, (_, n) => `$L_${n}$`)
    .replace(/\bN(\d+)\b/g, (_, n) => `$N_${n}$`)
    .replace(/\bR(\d+)\b/g, (_, n) => `$R_${n}$`)
    .replace(/\bS=(\d+(?:\.\d+)?)\b/g, (_, n) => `$S=${n}$`)
    .replace(/\bP=(\d+(?:\.\d+)?)\b/g, (_, n) => `$P=${n}$`);
}

function toLatexExpr(value) {
  return String(value || '')
    .replace(/Π(\d+)/g, (_, n) => `\\Pi_${n}`)
    .replace(/Ξ_?(\d+)/g, (_, n) => `\\Xi_${n}`)
    .replace(/Ω/g, '\\Omega')
    .replace(/\bL_i\b/g, 'L_i')
    .replace(/\bL(\d+)\^T\b/g, (_, n) => `L_${n}^{T}`)
    .replace(/\bL(\d+)\b/g, (_, n) => `L_${n}`)
    .replace(/\bN(\d+)Π(\d+)/g, (_, n, p) => `N_${n}\\Pi_${p}`)
    .replace(/\bN(\d+)\b/g, (_, n) => `N_${n}`)
    .replace(/\bR(\d+)\b/g, (_, n) => `R_${n}`)
    .replace(/\s+/g, ' ')
    .trim();
}

export function parseRubricReason(reason) {
  const text = cleanText(reason);
  const prefix = /^Rubric weighted score:\s*/i;
  if (!prefix.test(text)) return null;
  const body = text.replace(prefix, '');
  const items = body.split(';').map(part => {
    const [rawKey, ...rest] = part.split(':');
    const rawValue = rest.join(':');
    const key = cleanText(rawKey);
    const value = cleanText(rawValue);
    if (!key || !value) return null;
    return {
      key,
      label: rubricLabels[key] || key,
      value,
    };
  }).filter(Boolean);
  if (!items.length) return null;
  return {
    title: '开放设计题采用分项 Rubric 评分',
    items,
  };
}

function translateKey(key) {
  return {
    question: '题目',
    answer: '答案',
    expected_answer: '参考答案',
    model_answer: '模型回答',
    reason: '评分理由',
    score: '评分',
  }[key] || key;
}

function cleanText(value) {
  return String(value || '').trim();
}
