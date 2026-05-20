"""LLM-as-Judge scoring for benchmark evaluation.

Supports two dimensions:
  - Dimension A (AScorer): 判断模型回答与标准答案的语义等价性
  - Dimension B (BScorer): 判断模型推理步骤与标准推理链的逻辑一致性
"""

import argparse
import json

from benchmark.eval.client_factory import create_client

# ---------------------------------------------------------------------------
# Shared judge prompts
# ---------------------------------------------------------------------------

A_SYSTEM_PROMPT = """你是一个专业的控制科学答案评分员。你的任务是判断模型给出的答案与标准答案是否语义等价。

## 评分规则
- **1.0 分（完全正确）**：答案核心内容与标准答案一致，关键公式、结论正确。允许同义表达和不同措辞。
- **0.6 分（核心正确但有遗漏）**：核心结论或公式正确，但缺少部分次要细节或解释不够完整。
- **0.3 分（部分正确）**：包含部分正确信息，但存在明显遗漏或错误，无法作为完整答案。
- **0.0 分（错误/空白）**：答案完全错误、无关、或空白。

## 评判原则
- 宽松评判：接受同义表达、不同措辞、不同的叙述顺序
- 只要核心结论和公式正确，即视为语义等价
- 仅在答案明显错误或关键概念错误时才判低分
- 如果模型回答包含标准答案中的正确公式和关键结论，即使表述不同也应判 1.0 分

请严格按照以下 JSON 格式输出，不要输出任何其他内容：
{"score": <分数>, "reason": "<评分理由>", "issues": ["<问题1>", ...]}
分数只能是 0.0、0.3、0.6、1.0 之一。如果没有问题，issues 为空列表 []。"""

A_USER_PROMPT_TEMPLATE = """## 问题
{question}

## 标准答案
{expected_answer}

## 模型回答
{model_answer}

请根据评分规则对模型回答进行评分。"""

B_SYSTEM_PROMPT = """你是一个控制科学推理步骤评分员。你的任务是判断模型给出的推理步骤与标准推理链在逻辑上是否一致。

## 评分规则
- **1.0 分（全部步骤正确）**：推理步骤完整、逻辑清晰，每一步推理都正确，结论正确。
- **0.7 分（步骤完整但结论有错）**：推理链条完整，步骤基本正确，但最终结论出现错误。
- **0.5 分（部分步骤正确，≥50%）**：至少一半以上的推理步骤正确，但存在部分步骤错误或缺失。
- **0.2 分（部分步骤正确，<50%）**：有少量正确步骤，但大部分推理错误或缺失。
- **0.0 分（无有效步骤）**：没有有效的推理步骤，或回答完全无关。

## 评判原则
- 关注推理逻辑的一致性，而非措辞的精确匹配
- 如果模型使用了与标准答案不同的推理路径但逻辑正确，应视为有效步骤
- 宽松评判：只要推理方向正确、关键步骤存在，即视为正确步骤

请严格按照以下 JSON 格式输出，不要输出任何其他内容：
{"score": <分数>, "reason": "<评分理由>", "issues": ["<问题1>", ...]}
分数只能是 0.0、0.2、0.5、0.7、1.0 之一。如果没有问题，issues 为空列表 []。"""

B_USER_PROMPT_TEMPLATE = """## 问题
{question}

## 标准推理步骤
{expected_answer}

## 模型回答的推理步骤
{model_answer}

请根据评分规则对模型回答的推理步骤进行评分。"""

# NOTE: MEDICAL_JUDGE_SYSTEM_PROMPT 和 MEDICAL_USER_PROMPT_TEMPLATE 供后续 MedicalScorer 使用（Track3 Task5）。
# _parse_judge_result 已兼容保留 dimensions 字段，现有 A/B Scorer 不受影响。
MEDICAL_JUDGE_SYSTEM_PROMPT = """你是一位医学文献检索质量评估专家。你的任务是从四个维度评估检索到的医学文献chunk的质量。

## 评分维度（各 0-1 分，总分 0-1）

1. **语义相关性 (Semantic Relevance)**：检索到的 chunk 内容是否与查询意图匹配。医学术语需关注同义词和上下位概念（如 "myocardial infarction" 与 "heart attack" 等价）。
2. **信息完整性 (Information Completeness)**：chunk 是否包含查询所需的关键数据（如基线表数据、结局指标数值、不良事件发生率、统计检验结果等）。
3. **来源可溯性 (Source Traceability)**：chunk 是否包含足够的上下文信息（如章节标题、文献来源、IMRAD 段落标识）以便追溯原始文献。
4. **医学准确性 (Medical Accuracy)**：提取的医学信息是否准确无误，是否存在概念混淆、数值错误或统计报告不当。

## 评分规则
- **1.0 分（完全满足）**：四个维度全部满足，chunk 精确命中查询意图且包含完整数据。
- **0.75 分（基本满足）**：3/4 维度满足，存在一个维度的轻微缺陷（如缺少完整基线表但包含关键结局数据）。
- **0.5 分（部分满足）**：2/4 维度满足，chunk 部分相关但关键数据缺失。
- **0.25 分（勉强相关）**：仅 1/4 维度满足，chunk 主题相关但无可用数据。
- **0.0 分（无关）**：检索结果与查询完全无关，或包含明显医学错误。

## 评判原则
- 医学领域术语宽松匹配：接受同义表达和缩写展开（如 "HTN" ↔ "hypertension"）
- 优先判断是否包含可量化的临床数据（数值、表格、统计量）
- 若 chunk 含 baseline characteristics table 或 primary endpoint 数据，应优先给高分
- 诚实地标注信息来源不完整的情况

请严格按照以下 JSON 格式输出，不要输出任何其他内容：
{"score": <分数>, "reason": "<评分理由>", "dimensions": {"relevance": <0-1>, "completeness": <0-1>, "traceability": <0-1>, "accuracy": <0-1>}, "issues": ["<问题1>", ...]}
分数只能是 0.0、0.25、0.5、0.75、1.0 之一。如果没有问题，issues 为空列表 []。"""

MEDICAL_USER_PROMPT_TEMPLATE = """## 临床查询
{question}

## 检索到的医学文献 Chunk
{chunk_text}

## Chunk 元信息
- 章节标签: {medical_label}
- 父级章节: {medical_parent}

请根据评分规则对检索结果进行评分。"""


# ---------------------------------------------------------------------------
# Scorers
# ---------------------------------------------------------------------------


class AScorer:
    """答案语义等价性评分器 (Dimension A)。"""

    VERSION = "1.1"
    METHOD = "llm_judge"

    @staticmethod
    def judge(question, expected_answer, model_answer, client, model_name):
        """使用 LLM-as-Judge 判断模型回答与标准答案的语义等价性。

        Args:
            question: 原始问题文本
            expected_answer: 标准答案
            model_answer: 模型生成的回答
            client: OpenAI-compatible 客户端实例
            model_name: 使用的模型名称

        Returns:
            dict: {"score": float, "reason": str, "issues": list[str]}
        """
        user_prompt = A_USER_PROMPT_TEMPLATE.format(
            question=question,
            expected_answer=expected_answer,
            model_answer=model_answer,
        )

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": A_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0,
            max_tokens=3000,
        )

        raw = response.choices[0].message.content.strip()
        return _parse_judge_result(raw, valid_scores={0.0, 0.3, 0.6, 1.0})


class BScorer:
    """推理步骤逻辑一致性评分器 (Dimension B)。"""

    VERSION = "1.1"
    METHOD = "llm_judge"

    @staticmethod
    def judge(question, expected_answer, model_answer, client, model_name):
        """使用 LLM-as-Judge 判断模型推理步骤与标准推理链的逻辑一致性。

        Args:
            question: 原始问题文本
            expected_answer: 标准推理步骤
            model_answer: 模型生成的推理步骤
            client: OpenAI-compatible 客户端实例
            model_name: 使用的模型名称

        Returns:
            dict: {"score": float, "reason": str, "issues": list[str]}
        """
        user_prompt = B_USER_PROMPT_TEMPLATE.format(
            question=question,
            expected_answer=expected_answer,
            model_answer=model_answer,
        )

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": B_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0,
            max_tokens=3000,
        )

        raw = response.choices[0].message.content.strip()
        return _parse_judge_result(raw, valid_scores={0.0, 0.2, 0.5, 0.7, 1.0})


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _extract_json_block(text):
    """Extract JSON string from markdown code blocks or raw text."""
    if "```json" in text:
        start = text.index("```json") + 7
        end = text.index("```", start) if "```" in text[start:] else len(text)
        return text[start:end].strip()
    if "```" in text:
        start = text.index("```") + 3
        end = text.index("```", start) if "```" in text[start:] else len(text)
        return text[start:end].strip()
    return text.strip()


def _parse_judge_result(raw, valid_scores):
    """解析 LLM 返回的 JSON 字符串为标准 dict。"""
    json_str = _extract_json_block(raw)

    try:
        result = json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        return {
            "score": 0.0,
            "reason": f"LLM 返回格式异常，无法解析: {raw[:200]}",
            "issues": ["LLM judge response parse failure"],
        }

    score = _coerce_float(result.get("score", 0.0), default=0.0)
    if score not in valid_scores:
        closest = min(valid_scores, key=lambda v: abs(v - score))
        score = closest

    issues = result.get("issues", [])
    if isinstance(issues, str):
        issues = [issues]
    elif not isinstance(issues, list):
        issues = []

    output = {
        "score": score,
        "reason": result.get("reason", ""),
        "issues": issues,
    }
    if "dimensions" in result and isinstance(result["dimensions"], dict):
        output["dimensions"] = result["dimensions"]
    return output


def _coerce_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def create_judge_client(api_key=None, base_url="https://api.deepseek.com", model="deepseek-v4-flash"):
    client, model_name, _ = create_client(api_key, base_url, model)
    return client, model_name


# ---------------------------------------------------------------------------
# Generic LLM-as-Judge (shared by evaluate.py and RubricScorer fallback)
# ---------------------------------------------------------------------------


class GenericScorer:
    """通用 LLM-as-Judge 评分器，用于 C/D 维回退评分。"""

    VERSION = "1.1"
    METHOD = "llm_judge"

    @staticmethod
    def judge(question, expected_answer, model_answer, client, model_name):
        system_prompt = """你是一个控制科学答案评分员。判断模型回答与标准答案是否对应同一结论。
评分规则：
- 1.0: 完全正确，核心结论一致
- 0.75: 基本正确，有少量表述差异
- 0.5: 部分正确，存在明显遗漏
- 0.25: 有正确元素但整体不完整
- 0.0: 错误或空白

输出格式：{"score": <分数>, "reason": "<理由>", "issues": ["<问题>"]}
分数只能是 0.0, 0.25, 0.5, 0.75, 1.0 之一。"""

        user_prompt = f"""## 问题
{question}

## 标准答案
{expected_answer}

## 模型回答
{model_answer}

请评分。"""

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0,
            max_tokens=2000,
        )
        raw = response.choices[0].message.content.strip()
        json_str = _extract_json_block(raw)
        try:
            result = json.loads(json_str)
        except (json.JSONDecodeError, ValueError):
            return {"score": 0.0, "reason": f"Parse error: {raw[:200]}", "issues": ["judge parse failure"]}
        valid = {0.0, 0.25, 0.5, 0.75, 1.0}
        score = _coerce_float(result.get("score", 0.0), default=0.0)
        if score not in valid:
            score = min(valid, key=lambda v: abs(v - score))
        issues = result.get("issues", [])
        if isinstance(issues, str):
            issues = [issues]
        elif not isinstance(issues, list):
            issues = []
        return {"score": score, "reason": result.get("reason", ""), "issues": issues}


# Backward-compatible alias (kept for legacy imports)
generic_judge = GenericScorer.judge


# ---------------------------------------------------------------------------
# Rubric Scorer (Dimension D)
# ---------------------------------------------------------------------------

RUBRIC_BATCH_SYSTEM_PROMPT = """你是一个控制科学开放设计评分员。你需要对模型的回答按多个评分项逐一评分。

每个评分项需要给出 0.0、0.3、0.6、1.0 之一的分值：
- 1.0: 完全覆盖，内容充分且准确
- 0.6: 部分覆盖，有相关内容但不够完整
- 0.3: 轻微提及，只有少量相关内容
- 0.0: 未覆盖，完全没有涉及该评分项

请严格按照以下 JSON 格式输出所有评分项的结果：
{"items": [{"name": "...", "score": 0.0, "reason": "..."}, ...]}"""


def _rubric_judge_batch(question, rubric_items, model_answer, client, model_name):
    """批量 rubric 评分：一次 API 调用评估所有子项。"""
    items_desc = []
    for item in rubric_items:
        items_desc.append(f"- {item['name']} (weight {item['weight']}): {item['description']}")

    user_prompt = f"""## 问题
{question}

## 评分项列表
{chr(10).join(items_desc)}

## 模型回答
{model_answer}

请对每个评分项逐一评分。"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": RUBRIC_BATCH_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
        max_tokens=2000,
    )
    raw = response.choices[0].message.content.strip()
    json_str = _extract_json_block(raw)
    try:
        result = json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        return None

    items = result.get("items", [])
    if not items:
        return None

    valid = {0.0, 0.3, 0.6, 1.0}
    detail_map = {}
    for item in items:
        name = item.get("name", "")
        score = _coerce_float(item.get("score", 0.0), default=0.0)
        if score not in valid:
            score = min(valid, key=lambda v: abs(v - score))
        detail_map[name] = {"score": score, "reason": item.get("reason", "")}
    return detail_map


def _format_rubric_item(item):
    name = item.get("name", "")
    desc = item.get("description", "")
    weight = item.get("weight", 1)
    return f"{name} (weight {weight}): {desc}"


def _rubric_judge_single(question, rubric_item, model_answer, client, model_name):
    """对单个 rubric 子项调用 LLM-as-Judge 评分（降级方案）。"""
    system_prompt = """你是一个控制科学开放设计评分员。你需要判断模型的回答在给定的评分项上是否充分覆盖。
评分规则：
- 1.0: 完全覆盖，内容充分且准确
- 0.6: 部分覆盖，有相关内容但不够完整
- 0.3: 轻微提及，只有少量相关内容
- 0.0: 未覆盖，完全没有涉及该评分项
请严格按照 JSON 格式输出：{"score": <分数>, "reason": "<评分理由>"}"""

    user_prompt = f"""## 问题
{question}

## 评分项
{_format_rubric_item(rubric_item)}

## 模型回答
{model_answer}

请判断模型回答是否充分覆盖了该评分项的内容。"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
        max_tokens=1000,
    )
    raw = response.choices[0].message.content.strip()
    json_str = _extract_json_block(raw)
    try:
        result = json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        return {"score": 0.0, "reason": "Parse error", "weight": rubric_item.get("weight", 1)}
    score = _coerce_float(result.get("score", 0.0), default=0.0)
    valid = {0.0, 0.3, 0.6, 1.0}
    if score not in valid:
        score = min(valid, key=lambda v: abs(v - score))
    return {"score": score, "reason": result.get("reason", ""), "weight": rubric_item.get("weight", 1)}


class RubricScorer:
    """开放性设计评分器 (Dimension D) — 逐 rubric 项加权评分。"""

    VERSION = "1.1"
    METHOD = "llm_judge_rubric"

    @staticmethod
    def judge(question, expected_answer, model_answer, client, model_name, rubric=None):
        if not rubric:
            return generic_judge(question, expected_answer, model_answer, client, model_name)

        rubric_items = []
        for name, item in rubric.items():
            if not isinstance(item, dict):
                continue
            rubric_items.append({
                "name": name,
                "description": item.get("description", ""),
                "weight": float(item.get("weight", 1)),
            })

        batch_result = _rubric_judge_batch(question, rubric_items, model_answer, client, model_name)

        details = []
        total_weight = 0.0
        weighted_sum = 0.0

        if batch_result:
            for item in rubric_items:
                name = item["name"]
                weight = item["weight"]
                detail = batch_result.get(name, {"score": 0.0, "reason": "Not evaluated"})
                score = detail["score"]
                details.append({
                    "name": name,
                    "score": score,
                    "weight": weight,
                    "reason": detail.get("reason", ""),
                })
                total_weight += weight
                weighted_sum += score * weight
        else:
            for item in rubric_items:
                name = item["name"]
                weight = item["weight"]
                result = _rubric_judge_single(question, item, model_answer, client, model_name)
                score = result["score"]
                details.append({
                    "name": name,
                    "score": score,
                    "weight": weight,
                    "reason": result.get("reason", ""),
                })
                total_weight += weight
                weighted_sum += score * weight

        final_score = round(weighted_sum / total_weight, 4) if total_weight > 0 else 0.0

        reasons = [f"{d['name']}: {d['score']}" for d in details]
        return {
            "score": final_score,
            "reason": "Rubric weighted score: " + "; ".join(reasons),
            "issues": [],
            "rubric_details": details,
        }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args():
    parser = argparse.ArgumentParser(
        description="LLM-as-Judge 评分器 — 控制科学基准测试"
    )
    parser.add_argument(
        "--dimension",
        choices=["A", "B"],
        required=True,
        help="评分维度: A=答案语义等价性, B=推理步骤一致性",
    )
    parser.add_argument(
        "--question",
        required=True,
        help="原始问题文本",
    )
    parser.add_argument(
        "--expected",
        required=True,
        help="标准答案（Dimension A）或标准推理步骤（Dimension B）",
    )
    parser.add_argument(
        "--answer",
        required=True,
        help="模型回答（Dimension A）或模型推理步骤（Dimension B）",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="API 密钥，默认按 provider 从环境变量读取；DeepSeek 支持 DEEPSEEK_API_KEY/OPENAI_API_KEY",
    )
    parser.add_argument(
        "--base-url",
        default="https://api.deepseek.com",
        help="API 基础地址 (默认: https://api.deepseek.com)",
    )
    parser.add_argument(
        "--model",
        default="deepseek-v4-flash",
        help="模型名称 (默认: deepseek-v4-flash)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    client, model_name = create_judge_client(
        api_key=args.api_key,
        base_url=args.base_url,
        model=args.model,
    )

    if args.dimension == "A":
        scorer = AScorer()
    else:
        scorer = BScorer()

    result = scorer.judge(
        question=args.question,
        expected_answer=args.expected,
        model_answer=args.answer,
        client=client,
        model_name=model_name,
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
