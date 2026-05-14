"""S2* 多Judge交叉验证 — Fleiss' Kappa 评分者间信度

选取已完成评测报告的样本，用 3 个不同 Judge 模型重新评分，
计算 Fleiss' Kappa 以量化 Judge 选择对评分一致性的影响。

Judge 模型 (默认):
  - deepseek-v4-flash (主 Judge，DeepSeek API)
  - deepseek-v4-pro   (第二 Judge，DeepSeek API)
  - minimax-m2.5       (第三 Judge，MiniMax Anthropic API)

产出:
  - benchmark/eval/reports/cross_judge_kappa.json
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from benchmark.eval.utils import load_json, write_json_atomic
from benchmark.eval.judge import A_SYSTEM_PROMPT, B_SYSTEM_PROMPT, \
    A_USER_PROMPT_TEMPLATE, B_USER_PROMPT_TEMPLATE

DEFAULT_REPORTS_DIR = ROOT / "benchmark" / "eval" / "reports"
DEFAULT_OUTPUT = ROOT / "benchmark" / "eval" / "reports" / "cross_judge_kappa.json"
DEFAULT_SAMPLE_SIZE = 30

DEFAULT_JUDGES = [
    {"name": "deepseek-v4-flash", "base_url": "https://api.deepseek.com", "key_env": "DEEPSEEK_API_KEY"},
    {"name": "deepseek-v4-pro",   "base_url": "https://api.deepseek.com", "key_env": "DEEPSEEK_API_KEY"},
    {"name": "minimax-m2.5",      "base_url": "https://api.minimaxi.com/anthropic", "key_env": "MINIMAX_API_KEY"},
]

DEEPSEEK_API_KEY_DEFAULT = os.getenv("DEEPSEEK_API_KEY", "")


def _resolve_key(judge_cfg):
    key = os.environ.get(judge_cfg["key_env"], "")
    if not key and "deepseek" in judge_cfg["base_url"]:
        key = DEEPSEEK_API_KEY_DEFAULT
    return key


def _create_client(judge_cfg, api_key):
    from openai import OpenAI, DefaultHttpxClient

    is_anthropic = "minimax" in judge_cfg["base_url"].lower()
    if is_anthropic:
        from anthropic import Anthropic
        import httpx
        return Anthropic(
            api_key=api_key, base_url=judge_cfg["base_url"],
            timeout=120, http_client=httpx.Client(proxy=None),
        ), "anthropic"
    return (
        OpenAI(
            api_key=api_key, base_url=judge_cfg["base_url"],
            timeout=120, max_retries=0,
            http_client=DefaultHttpxClient(proxy=None),
        ),
        "openai",
    )


def _judge_one(client, client_type, judge_name, question, expected, model_answer, dimension, rubric):
    from benchmark.eval.evaluate import score_model_answer
    from benchmark.eval.judge import AScorer, BScorer
    try:
        if client_type == "anthropic":
            result = _judge_anthropic(client, judge_name, question, expected, model_answer, dimension, rubric)
        else:
            result = score_model_answer(
                question, expected, model_answer, dimension, rubric, client, judge_name,
            )
        return {"score": result.get("score", 0.0), "reason": result.get("reason", ""), "judge": judge_name, "error": None}
    except Exception as e:
        return {"score": -1.0, "reason": str(e), "judge": judge_name, "error": str(e)}


def _judge_anthropic(client, judge_name, question, expected, model_answer, dimension, rubric):
    if dimension == "A":
        system_prompt = A_SYSTEM_PROMPT
        user_prompt = A_USER_PROMPT_TEMPLATE.format(
            question=question, expected_answer=expected, model_answer=model_answer,
        )
    elif dimension == "B":
        system_prompt = B_SYSTEM_PROMPT
        user_prompt = B_USER_PROMPT_TEMPLATE.format(
            question=question, expected_answer=expected, model_answer=model_answer,
        )
    else:
        system_prompt = "你是控制科学评分员。对综合方案进行评分。输出: {\"score\": <0.0-1.0>, \"reason\": \"...\", \"issues\": [...]}"
        rubric_hint = ""
        if rubric:
            rubric_hint = f"\n\n## 评分量规\n{json.dumps(rubric, ensure_ascii=False)}"
        user_prompt = f"""## 问题
{question}

## 标准答案
{expected}

## 模型回答
{model_answer}{rubric_hint}

请对模型回答评分。"""
    resp = client.messages.create(
        model=judge_name,
        max_tokens=3000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    text = ""
    for block in resp.content:
        if hasattr(block, "text") and block.text:
            text += block.text
    from benchmark.eval.judge import _parse_judge_result
    valid_scores = {0.0, 0.3, 0.6, 1.0} if dimension in ("A", "D") else {0.0, 0.2, 0.5, 0.7, 1.0}
    return _parse_judge_result(text.strip(), valid_scores)


def load_report_records(report_path):
    data = load_json(report_path)
    return data.get("records", []), data.get("model", "")


def sample_records(records, n, seed=42):
    import random
    rng = random.Random(seed)
    records = [r for r in records if r.get("model_answer") and r.get("model_answer", "").strip()]
    if len(records) <= n:
        return records
    return rng.sample(records, n)


def score_all_judges(records, judges, question_map=None):
    scored = []
    for judge_cfg in judges:
        api_key = _resolve_key(judge_cfg)
        if not api_key:
            print(f"[SKIP] Judge {judge_cfg['name']}: 无 API Key")
            continue
        client, client_type = _create_client(judge_cfg, api_key)
        print(f"[JUDGE] {judge_cfg['name']} ({client_type}) — 评分 {len(records)} 条...")
        for i, r in enumerate(records):
            qid = r.get("id", f"Q{i}")
            core_q = question_map.get(qid, {}) if question_map else {}
            question_text = core_q.get("question", "")
            expected = r.get("expected_answer", "")
            res = _judge_one(
                client, client_type, judge_cfg["name"],
                question_text,
                expected,
                r.get("model_answer", ""),
                r.get("dimension", "A"),
                r.get("rubric_details"),
            )
            res["question_id"] = qid
            res["dimension"] = r.get("dimension", "")
            scored.append(res)
            if (i + 1) % 10 == 0:
                print(f"  {judge_cfg['name']}: {i + 1}/{len(records)}")
        print(f"  {judge_cfg['name']}: {len(records)}/{len(records)} 完成")
    return scored


def compute_fleiss_kappa(scored, threshold=0.5):
    by_q = {}
    for s in scored:
        qid = s["question_id"]
        if qid not in by_q:
            by_q[qid] = []
        score = s.get("score", -1)
        if score < 0:
            continue
        by_q[qid].append(1.0 if score >= threshold else 0.0)

    n_questions = len([v for v in by_q.values() if len(v) >= 2])
    if n_questions < 2:
        return {"kappa": None, "error": f"不足 2 题有 ≥2 位有效 Judge ({n_questions})"}

    n_raters = max(len(v) for v in by_q.values())
    categories = [0.0, 1.0]

    n_matrix = []
    for qid, scores in by_q.items():
        if len(scores) < 2:
            continue
        row = [scores.count(cat) for cat in categories]
        n_matrix.append(row)

    N = len(n_matrix)
    k = len(categories)
    n = n_raters
    if N == 0 or n <= 1:
        return {"kappa": None, "error": "数据不足"}

    p_j = []
    for j in range(k):
        col_sum = sum(row[j] for row in n_matrix)
        p_j.append(col_sum / (N * n))

    P_i = []
    for row in n_matrix:
        sum_sq = sum(x * (x - 1) for x in row)
        P_i.append(sum_sq / (n * (n - 1)))

    P_bar = sum(P_i) / N
    P_e_bar = sum(pj * pj for pj in p_j)
    if abs(1 - P_e_bar) < 1e-10:
        return {"kappa": 1.0, "n_questions": N, "n_raters": n, "P_bar": P_bar, "P_e_bar": P_e_bar}

    kappa = (P_bar - P_e_bar) / (1 - P_e_bar)
    return {
        "kappa": round(kappa, 4),
        "interpretation": _interpret_kappa(kappa),
        "n_questions": N,
        "n_raters": n,
        "categories": categories,
        "threshold": threshold,
        "P_bar": round(P_bar, 4),
        "P_e_bar": round(P_e_bar, 4),
    }


def _interpret_kappa(kappa):
    if kappa < 0:
        return "poor (低于随机)"
    if kappa < 0.2:
        return "slight"
    if kappa < 0.4:
        return "fair"
    if kappa < 0.6:
        return "moderate"
    if kappa < 0.8:
        return "substantial"
    return "almost perfect"


def main():
    parser = argparse.ArgumentParser(description="多Judge交叉验证 — Fleiss' Kappa 评分者间信度")
    parser.add_argument("--report", "-r", default=None, help="单个评测报告 JSON 路径 (优先于sample)")
    parser.add_argument("--sample-size", "-n", type=int, default=DEFAULT_SAMPLE_SIZE, help="采样题数")
    parser.add_argument("--seed", type=int, default=42, help="采样种子")
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT), help="输出路径")
    parser.add_argument("--judges", nargs="+", default=None, help="Judge 模型名 (覆盖默认)")
    parser.add_argument("--threshold", type=float, default=0.5, help="Fleiss' Kappa 二值化阈值")
    args = parser.parse_args()

    if args.report:
        report_path = Path(args.report)
        if not report_path.exists():
            raise SystemExit(f"评测报告不存在: {report_path}")
        records, model_name = load_report_records(report_path)
    else:
        report_dir = Path(DEFAULT_REPORTS_DIR)
        report_files = sorted(report_dir.glob("*_report.json"))
        report_files = [f for f in report_files if "kappa" not in f.name and "status" not in f.suffix]
        if not report_files:
            report_files = sorted(report_dir.glob("*_report.json.progress.jsonl"))
            if not report_files:
                raise SystemExit(f"未找到评测报告: {report_dir}")
            print(f"[WARN] 无完整 JSON 报告，将使用进度文件中的记录 (实验性)")
        records, model_name = [], ""
        for rf in report_files[:1]:
            try:
                records, model_name = load_report_records(rf)
                break
            except Exception:
                continue

    if not records:
        raise SystemExit("未能加载任何记录")

    core_data = load_json(ROOT / "benchmark" / "dataset" / "core.json")
    question_map = {q["id"]: q for q in core_data.get("questions", [])}
    print(f"已加载 core.json 题目索引: {len(question_map)} 题")

    print(f"已加载 {len(records)} 条记录 (来源: {model_name or 'unknown'})")
    records = sample_records(records, args.sample_size, args.seed)
    print(f"采样 {len(records)} 条有效记录 (含非空 model_answer)")

    judges = DEFAULT_JUDGES
    if args.judges:
        judges = [{"name": j, "base_url": "https://api.deepseek.com", "key_env": "DEEPSEEK_API_KEY"} for j in args.judges]

    scored = score_all_judges(records, judges, question_map=question_map)
    kappa_result = compute_fleiss_kappa(scored, args.threshold)

    output = {
        "meta": {
            "project": "ControlSci S2* 多Judge交叉验证",
            "method": "Fleiss' Kappa",
            "threshold": args.threshold,
            "sample_size": len(records),
            "source_model": model_name,
        },
        "judges": [j["name"] for j in judges],
        "kappa": kappa_result,
        "per_judge_summary": _compute_judge_summary(scored),
        "records": scored,
    }

    write_json_atomic(args.output, output)
    print(f"\n[OK] 交叉验证报告已写入: {args.output}")
    print(f"  Fleiss' Kappa: {kappa_result.get('kappa', 'N/A')} ({kappa_result.get('interpretation', '')})")
    print(f"  题目数: {kappa_result.get('n_questions', 'N/A')}")
    print(f"  Rater数: {kappa_result.get('n_raters', 'N/A')}")


def _compute_judge_summary(scored):
    by_judge = {}
    for s in scored:
        j = s["judge"]
        if j not in by_judge:
            by_judge[j] = {"scores": [], "errors": 0, "count": 0}
        by_judge[j]["count"] += 1
        if s.get("error"):
            by_judge[j]["errors"] += 1
        elif s.get("score", -1) >= 0:
            by_judge[j]["scores"].append(s["score"])
    summary = {}
    for j, data in by_judge.items():
        valid = data["scores"]
        summary[j] = {
            "count": data["count"],
            "errors": data["errors"],
            "mean": round(sum(valid) / len(valid), 4) if valid else None,
            "std": round(_std(valid), 4) if len(valid) >= 2 else None,
        }
    return summary


def _std(values):
    mean = sum(values) / len(values)
    return (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5


if __name__ == "__main__":
    main()
