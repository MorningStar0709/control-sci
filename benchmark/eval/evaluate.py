import argparse
import re
import sys
import time
from collections import Counter
from datetime import datetime, timedelta
from functools import partial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmark.eval.client_factory import create_client, resolve_api_key
from benchmark.eval.judge import GenericScorer
from benchmark.eval.utils import append_jsonl, load_json, write_json_atomic

DEFAULT_INPUT = ROOT / "benchmark" / "dataset" / "sample_questions.json"
DEFAULT_OUTPUT = ROOT / "benchmark" / "dataset" / "sample_report.json"

_FORMULA_PATTERNS = [
    re.compile(r'\$\$'),
    re.compile(r'\\\(|\\\)'),
    re.compile(r'\\\[|\\\]'),
    re.compile(r'\brank\s*\('),
    re.compile(r'\bdet\s*\('),
    re.compile(r'\b[CcGgVvxX]\([a-zA-Z]\)'),
    re.compile(r'\btrace\s*\('),
    re.compile(r'\\begin\{|\\end\{'),
]
CONTROL_TERMS = (
    "传递函数",
    "可控",
    "稳定",
    "Lyapunov",
    "Routh",
    "Riccati",
    "状态空间",
    "反馈",
    "极点",
    "裕度",
)

SCORER_VERSION = "1.1"
SCORER_METHOD = "llm_judge"


def build_model_report(records, target_model, judge_model):
    issues_counter = Counter()
    failure_counter = Counter()
    by_dimension = Counter()
    score_sums = Counter()

    for record in records:
        dimension = record.get("dimension", "?")
        score = float(record.get("score", 0.0) or 0.0)
        by_dimension[dimension] += 1
        score_sums[dimension] += score
        for issue in record.get("issues", []) or []:
            if issue:
                issues_counter[issue] += 1
                issue_text = str(issue).lower()
                if "failure" in issue_text or "error" in issue_text:
                    failure_counter[issue] += 1

    dimension_scores = {
        dimension: round(score_sums[dimension] / count, 4)
        for dimension, count in sorted(by_dimension.items())
        if count
    }
    overall = round(sum(float(record.get("score", 0.0) or 0.0) for record in records) / len(records), 4) if records else 0.0

    return {
        "model": target_model,
        "judge_model": judge_model,
        "scorer_version": SCORER_VERSION,
        "scoring_mode": SCORER_METHOD,
        "total_questions": len(records),
        "overall_score": overall,
        "dimension_scores": dimension_scores,
        "records": records,
        "issues_summary": dict(issues_counter.most_common(20)),
        "failure_summary": dict(failure_counter.most_common()),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def load_existing_records(output_path, selected_ids, retry_failed=False):
    output_path = Path(output_path)
    if not output_path.exists():
        return []
    try:
        existing = load_json(output_path)
    except Exception as exc:
        backup_path = output_path.with_suffix(output_path.suffix + f".corrupt.{int(time.time())}.bak")
        output_path.replace(backup_path)
        print(f"Existing report could not be parsed; moved to {backup_path}: {exc}", flush=True)
        return []

    selected_ids = set(selected_ids)
    records = []
    seen = set()
    for record in existing.get("records", []):
        qid = record.get("id")
        if qid not in selected_ids or qid in seen:
            continue
        issues = [str(issue).lower() for issue in (record.get("issues") or [])]
        failed = any("failure" in issue or "error" in issue for issue in issues)
        if retry_failed and failed:
            continue
        records.append(record)
        seen.add(qid)
    return records


def select_questions(questions, limit=0, balanced_mini=False):
    if not balanced_mini:
        return questions[:limit] if limit > 0 else questions

    if limit <= 0:
        raise SystemExit("--balanced-mini requires --limit > 0")

    buckets = {}
    for q in questions:
        buckets.setdefault(str(q.get("dimension", "?")), []).append(q)

    preferred_dims = [d for d in ("A", "B", "C", "D") if d in buckets]
    preferred_dims.extend(sorted(d for d in buckets if d not in preferred_dims))
    if not preferred_dims:
        return []

    selected = []
    cursor = {d: 0 for d in preferred_dims}
    while len(selected) < limit:
        progressed = False
        for dim in preferred_dims:
            idx = cursor[dim]
            if idx < len(buckets[dim]):
                selected.append(buckets[dim][idx])
                cursor[dim] += 1
                progressed = True
                if len(selected) >= limit:
                    break
        if not progressed:
            break
    return selected


def call_with_retries(label, func, retries=3, base_sleep=2.0):
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as exc:
            last_exc = exc
            if attempt >= retries:
                break
            sleep_s = base_sleep * (2 ** (attempt - 1))
            print(f"  {label} failed attempt {attempt}/{retries}: {exc}; retrying in {sleep_s:.1f}s", flush=True)
            time.sleep(sleep_s)
    raise last_exc


def format_eta(minutes):
    if minutes is None:
        return ""
    return (datetime.now() + timedelta(minutes=minutes)).strftime("%Y-%m-%d %H:%M:%S")


# ── Reference mode (legacy, superseded by LLM-as-Judge model mode) ──


def score_a(question):
    answer = question.get("answer", "")
    has_formula = any(pattern.search(answer) for pattern in _FORMULA_PATTERNS)
    has_control_term = any(term in answer for term in CONTROL_TERMS)
    has_steps = len(question.get("reasoning_steps") or []) >= 2
    if has_formula and has_control_term and has_steps:
        return 1.0
    if (has_formula or has_control_term) and has_steps:
        return 0.7
    return 0.6 if has_steps else 0.3


def score_b(question):
    step_count = len(question.get("reasoning_steps") or [])
    if step_count >= 4:
        return 1.0
    if step_count >= 3:
        return 0.7
    if step_count >= 2:
        return 0.5
    return 0.2


def score_c(question):
    step_count = len(question.get("reasoning_steps") or [])
    has_pair = bool(question.get("sibling_id")) and bool(question.get("sensitivity_dimension"))
    return 0.5 if has_pair and step_count >= 3 else 0.25 if has_pair else 0.0


def score_d(question):
    rubric = question.get("rubric") or {}
    if not rubric:
        return 0.0
    weights = [item.get("weight", 0) for item in rubric.values() if isinstance(item, dict)]
    return round(sum(weights), 4)


def score_question(question):
    dimension = question.get("dimension")
    if dimension == "A":
        score = score_a(question)
    elif dimension == "B":
        score = score_b(question)
    elif dimension == "C":
        score = score_c(question)
    elif dimension == "D":
        score = score_d(question)
    else:
        score = 0.0
    return min(float(score), 1.0)


def evaluate(data, model):
    records = []
    for question in data.get("questions", []):
        score = score_question(question)
        records.append(
            {
                "id": question.get("id"),
                "dimension": question.get("dimension"),
                "difficulty_level": question.get("difficulty_level"),
                "score": score,
                "scoring_mode": "reference_heuristic",
            }
        )

    by_dimension = Counter()
    score_sums = Counter()
    for record in records:
        dimension = record["dimension"]
        by_dimension[dimension] += 1
        score_sums[dimension] += record["score"]

    dimension_scores = {
        dimension: round(score_sums[dimension] / count, 4)
        for dimension, count in sorted(by_dimension.items())
        if count
    }
    overall = round(sum(record["score"] for record in records) / len(records), 4) if records else 0.0

    return {
        "model": model,
        "total_questions": len(records),
        "overall_score": overall,
        "dimension_scores": dimension_scores,
        "records": records,
    }


TARGET_SYSTEM_PROMPT = """你是一个控制科学领域的专家。请回答以下控制科学问题。
如果问题涉及公式推导，请逐步写出推理过程。
如果问题涉及概念解释，请给出精确定义和必要的数学表达式。
回答要准确、专业、完整。"""


def call_target_model(question, client, model_name, provider_kind="openai"):
    """Call the target model to generate an answer for a given question.

    Args:
        question: 问题文本。
        client: Provider 客户端实例。
        model_name: 模型名称。
        provider_kind: Provider 类型标识 ("ollama" | "anthropic" | "openai")。
    """
    if provider_kind == "ollama":
        resp = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": TARGET_SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            temperature=0.3,
            max_tokens=4000,
        )
        return resp.choices[0].message.content.strip()

    if provider_kind == "anthropic":
        resp = client.messages.create(
            model=model_name,
            max_tokens=4000,
            system=TARGET_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": [{"type": "text", "text": question}]}],
        )
        text = ""
        for block in resp.content:
            if hasattr(block, 'text') and block.text:
                text += block.text
        return text.strip()

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": TARGET_SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        temperature=0.3,
        max_tokens=4000,
    )
    message = response.choices[0].message
    content = (message.content or "").strip()
    if content:
        return content
    reasoning_content = getattr(message, "reasoning_content", None)
    return (reasoning_content or "").strip()


def score_model_answer(question, expected, model_answer, dimension, rubric, judge_client, judge_model):
    from benchmark.eval.judge import AScorer, BScorer

    if dimension == "A":
        return AScorer.judge(question, expected, model_answer, judge_client, judge_model)
    if dimension == "B":
        return BScorer.judge(question, expected, model_answer, judge_client, judge_model)
    if dimension == "D" and rubric:
        from benchmark.eval.judge import RubricScorer

        return RubricScorer.judge(question, expected, model_answer, judge_client, judge_model, rubric=rubric)
    if dimension == "C" or dimension == "D":
        return GenericScorer.judge(question, expected, model_answer, judge_client, judge_model)
    return {"score": 0.0, "reason": "Unknown dimension", "issues": ["unknown dimension"]}


def model_evaluate(
    data,
    target_client,
    target_model,
    judge_client,
    judge_model,
    limit=0,
    provider_kind="openai",
    output_path=None,
    resume=False,
    retry_failed=False,
    retries=3,
    max_consecutive_failures=5,
    balanced_mini=False,
):
    questions = data.get("questions", [])
    questions = select_questions(questions, limit=limit, balanced_mini=balanced_mini)

    selected_ids = [q.get("id", f"idx-{i}") for i, q in enumerate(questions)]
    records = load_existing_records(output_path, selected_ids, retry_failed=retry_failed) if (resume and output_path) else []
    completed_ids = {record.get("id") for record in records}
    total = len(questions)
    started_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session_start = time.time()
    initial_completed = len(records)
    status_path = Path(output_path).with_suffix(Path(output_path).suffix + ".status.json") if output_path else None
    progress_path = Path(output_path).with_suffix(Path(output_path).suffix + ".progress.jsonl") if output_path else None
    consecutive_failures = 0
    stopped_early = False

    if records:
        print(f"Resume enabled: loaded {len(records)} existing records from {output_path}", flush=True)

    for i, q in enumerate(questions):
        qid = q.get("id", "?")
        if qid in completed_ids:
            print(f"[{i + 1}/{total}] {qid} already completed; skipping", flush=True)
            continue

        dimension = q.get("dimension", "?")
        difficulty = q.get("difficulty_level", "?")
        question_text = q.get("question", "")
        expected = q.get("answer", "")
        print(f"[{i + 1}/{total}] {qid} ({dimension}, {difficulty}) - calling target model...", flush=True)

        try:
            target_call = partial(call_target_model, question_text, target_client, target_model, provider_kind=provider_kind)
            model_answer = call_with_retries(
                "target",
                target_call,
                retries=retries,
            )
        except Exception as e:
            print(f"  ERROR calling target model after retries: {e}", flush=True)
            model_answer = ""

        print(f"  scoring...", end=" ", flush=True)
        try:
            if model_answer:
                judge_call = partial(
                    score_model_answer,
                    question_text,
                    expected,
                    model_answer,
                    dimension,
                    q.get("rubric"),
                    judge_client,
                    judge_model,
                )
                result = call_with_retries("judge", judge_call, retries=retries)
            else:
                result = {"score": 0.0, "reason": "Target model failed after retries", "issues": ["target failure"]}
        except Exception as e:
            print(f"ERROR scoring after retries: {e}", flush=True)
            result = {"score": 0.0, "reason": f"Scoring error after retries: {e}", "issues": ["scoring failure"]}
            consecutive_failures += 1
        else:
            if result.get("issues") and any("failure" in str(issue).lower() for issue in result.get("issues", [])):
                consecutive_failures += 1
            else:
                consecutive_failures = 0

        print(f"score={result['score']}", flush=True)

        issues = result.get("issues", []) or []
        if not model_answer and "target failure" not in issues:
            issues.append("target failure")

        record = {
            "id": qid,
            "dimension": dimension,
            "difficulty_level": difficulty,
            "score": result["score"],
            "reason": result.get("reason", ""),
            "issues": issues,
            "model_answer": model_answer,
            "expected_answer": expected,
            "scoring_mode": "llm_judge",
            "scorer_version": SCORER_VERSION,
        }
        if "rubric_details" in result:
            record["rubric_details"] = result["rubric_details"]
        records.append(record)
        completed_ids.add(qid)

        if output_path:
            elapsed_sec = max(time.time() - session_start, 0.001)
            session_completed = len(records) - initial_completed
            rate_q_per_min = session_completed / (elapsed_sec / 60) if session_completed > 0 else 0.0
            remaining = max(total - len(records), 0)
            eta_min = remaining / rate_q_per_min if rate_q_per_min > 0 else None
            partial_report = build_model_report(records, target_model, judge_model)
            partial_report["complete"] = len(records) >= total
            partial_report["started_at"] = started_at
            partial_report["run_metrics"] = {
                "session_completed": session_completed,
                "elapsed_sec": round(elapsed_sec, 2),
                "rate_q_per_min": round(rate_q_per_min, 4),
                "eta_min": round(eta_min, 2) if eta_min is not None else None,
                "eta_at": format_eta(eta_min),
            }
            write_json_atomic(output_path, partial_report)
            if status_path:
                status_item = {
                    "model": target_model,
                    "judge_model": judge_model,
                    "status": "running" if len(records) < total else "completed",
                    "completed": len(records),
                    "total": total,
                    "percent": round(len(records) / total * 100, 2) if total else 100.0,
                    "remaining": remaining,
                    "session_completed": session_completed,
                    "elapsed_sec": round(elapsed_sec, 2),
                    "rate_q_per_min": round(rate_q_per_min, 4),
                    "eta_min": round(eta_min, 2) if eta_min is not None else None,
                    "eta_at": format_eta(eta_min),
                    "last_id": qid,
                    "consecutive_failures": consecutive_failures,
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "progress_log": progress_path.name if progress_path else None,
                }
                write_json_atomic(status_path, status_item)
                if progress_path:
                    append_jsonl(progress_path, status_item)

        if consecutive_failures >= max_consecutive_failures:
            stopped_early = True
            print(
                f"Stopping early after {consecutive_failures} consecutive failures. "
                "Use --resume --retry-failed after fixing the issue.",
                flush=True,
            )
            break

    report = build_model_report(records, target_model, judge_model)
    report["complete"] = len(records) >= total
    if not report["complete"]:
        reason = "max_consecutive_failures" if stopped_early else "not_all_questions_completed"
        report["incomplete_reason"] = reason
        report["completed"] = len(records)
        report["total"] = total
    report["started_at"] = started_at
    return report


# ── Report generation (inline md helper, delegates to report.py when available) ──


def render_md_report(report):
    """Quick Markdown rendering of a model evaluation report."""
    from benchmark.eval.report import render_report as rp_render

    meta = {
        "title": "ControlSci Evaluation Report",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target_model": report.get("model", ""),
        "judge_model": report.get("judge_model", ""),
        "scoring_mode": report.get("scoring_mode", ""),
        "overall_score": report.get("overall_score", 0),
    }
    issues_counter = Counter(report.get("issues_summary", {}))
    return rp_render(meta, report.get("records", []), issues_counter)


# ── CLI ──────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a ControlSci benchmark file. Supports reference (data integrity) and model (LLM-as-Judge) modes."
    )
    parser.add_argument("--input", "-i", default=str(DEFAULT_INPUT), help="Benchmark JSON path.")
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT), help="Output report path.")
    parser.add_argument(
        "--mode",
        default="reference",
        choices=["reference", "model"],
        help="Evaluation mode: reference (data integrity check) or model (real LLM evaluation).",
    )

    parser.add_argument("--target-model", default="deepseek-v4-flash", help="Model to evaluate (model mode only).")
    parser.add_argument("--judge-model", default="deepseek-v4-flash", help="Judge model for LLM-as-Judge (model mode only).")
    parser.add_argument("--api-key", default=None, help="API key for model/judge calls (fallback for both target/judge).")
    parser.add_argument("--target-api-key", default=None, help="Override API key for target model.")
    parser.add_argument("--judge-api-key", default=None, help="Override API key for judge model.")
    parser.add_argument("--base-url", default="https://api.deepseek.com", help="API base URL (fallback for both target/judge).")
    parser.add_argument("--target-base-url", default=None, help="Override base URL for target model.")
    parser.add_argument("--judge-base-url", default=None, help="Override base URL for judge model.")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of questions to evaluate (model mode only).")
    parser.add_argument("--balanced-mini", action="store_true",
                        help="With --limit, select questions round-robin across A/B/C/D instead of taking the first N.")
    parser.add_argument("--resume", action="store_true", help="Resume from an existing JSON report and skip completed question IDs.")
    parser.add_argument("--retry-failed", action="store_true", help="When resuming, recompute records marked with failure/error issues.")
    parser.add_argument("--retries", type=int, default=3, help="Retry attempts for target and judge API calls.")
    parser.add_argument("--max-consecutive-failures", type=int, default=5, help="Stop early after this many consecutive failed records.")
    parser.add_argument(
        "--allow-incomplete",
        action="store_true",
        help="Exit 0 even when model-mode evaluation stops before all selected questions complete.",
    )
    parser.add_argument(
        "--format",
        default="json",
        choices=["json", "md"],
        help="Output format: json or md (model mode only).",
    )
    # Reference-mode only backward compat
    parser.add_argument("--model", dest="model_meta", default="reference-heuristic", help="[Reference mode only] Model name for metadata.")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()
    if not input_path.exists():
        raise SystemExit(f"Input not found: {input_path}")

    data = load_json(input_path)

    if args.mode == "reference":
        report = evaluate(data, args.model_meta)
        write_json_atomic(output_path, report)
        print(f"Report saved: {output_path}")
        print(f"Overall score: {report['overall_score']}")
        return

    # ── Model mode ──
    target_base_url = args.target_base_url or args.base_url
    judge_base_url = args.judge_base_url or args.base_url
    target_api_key = resolve_api_key(target_base_url, explicit_key=args.target_api_key, fallback_key=args.api_key)
    judge_api_key = resolve_api_key(judge_base_url, explicit_key=args.judge_api_key, fallback_key=args.api_key)

    print(f"Target model: {args.target_model} @ {target_base_url}")
    print(f"Judge model: {args.judge_model} @ {judge_base_url}")
    print(f"Limit: {args.limit or 'unlimited'}")
    if args.balanced_mini:
        print("Selection: balanced-mini")

    target_client, target_model, target_provider_kind = create_client(target_api_key, target_base_url, args.target_model)
    judge_client, judge_model, _ = create_client(judge_api_key, judge_base_url, args.judge_model)
    state_output_path = output_path
    if args.format == "md" and output_path.suffix.lower() != ".json":
        state_output_path = output_path.with_suffix(".json")

    report = model_evaluate(
        data,
        target_client,
        target_model,
        judge_client,
        judge_model,
        limit=args.limit,
        provider_kind=target_provider_kind,
        output_path=state_output_path,
        resume=args.resume,
        retry_failed=args.retry_failed,
        retries=args.retries,
        max_consecutive_failures=args.max_consecutive_failures,
        balanced_mini=args.balanced_mini,
    )

    if args.format == "md":
        md_content = render_md_report(report)
        output_path = output_path.with_suffix(".md") if output_path.suffix == ".json" else output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(md_content, encoding="utf-8")
        print(f"Markdown report saved: {output_path}")
    else:
        write_json_atomic(output_path, report)
        print(f"JSON report saved: {output_path}")
        print(f"Overall score: {report['overall_score']}")

    if not report.get("complete", False) and not args.allow_incomplete:
        print(
            "Evaluation incomplete: "
            f"{report.get('completed', 0)}/{report.get('total', 0)} completed "
            f"({report.get('incomplete_reason', 'unknown')}). "
            "Use --resume --retry-failed after fixing the issue, or pass --allow-incomplete for exploratory runs.",
            file=sys.stderr,
        )
        raise SystemExit(2)


if __name__ == "__main__":
    main()
