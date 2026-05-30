"""S1.5 Phase 2 并行评分 — ThreadPoolExecutor 4路并发 API 调用

读取 eval_answers.json, 用 DeepSeek API 并行评分 89 题,
输出 eval_finetuned_report.json (含 overall_score + 四维分数 + delta vs baseline)

Usage:
    python finetune/scripts/judge_parallel.py               # 全新跑
    python finetune/scripts/judge_parallel.py --resume      # 续传 (跳过已评分ID)
    python finetune/scripts/judge_parallel.py --workers 6   # 6路并发
"""
import argparse
import json
import re as _re
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from benchmark.eval.utils import load_json, write_json_atomic

DEFAULT_TEST = ROOT / "finetune" / "data" / "test.jsonl"
DEFAULT_BENCHMARK = ROOT / "benchmark" / "dataset" / "core.json"
DEFAULT_ANSWERS = ROOT / "finetune" / "output" / "eval_answers.json"
DEFAULT_OUTPUT = ROOT / "finetune" / "output" / "eval_finetuned_report.json"

BASELINE = {
    "model": "qwen3.5:9b (baseline, 无微调)",
    "overall_score": 0.6249,
    "dimension_scores": {"A": 0.5688, "B": 0.6104, "C": 0.6620, "D": 0.6586},
}

DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY", "")

_lock = threading.Lock()
_thread_local = threading.local()
_start_time = None


def append_jsonl(path, line):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")


def write_status(base_path, data):
    path = Path(str(base_path) + ".status.json")
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def load_test_questions(test_path, benchmark_path=None):
    if not Path(test_path).exists():
        raise SystemExit(f"评测数据不存在: {test_path}")
    test_questions = []
    with open(test_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                test_questions.append(json.loads(line))

    core_map = {}
    if benchmark_path and Path(benchmark_path).exists():
        core = load_json(benchmark_path)
        core_map = {q["id"]: q for q in core.get("questions", [])}

    for tq in test_questions:
        msgs = tq.get("messages", [])
        user_msg = next((m["content"] for m in msgs if m.get("role") == "user"), "")
        assistant_msg = next((m["content"] for m in msgs if m.get("role") == "assistant"), "")
        qid = _re.search(r"(CS-EVO-\d{5})", user_msg)
        qid = qid.group(1) if qid else f"test-{hash(user_msg) % 10000}"
        dim = "?"
        if qid in core_map:
            cq = core_map[qid]
            dim = cq.get("dimension", "?")
        if dim == "?":
            dm = _re.search(r"\[维度:\s*([A-D])\]", user_msg)
            if dm:
                dim = dm.group(1)
        expected = core_map.get(qid, {}).get("answer", assistant_msg) if qid in core_map else assistant_msg
        rubric = core_map.get(qid, {}).get("rubric") if qid in core_map else None
        diff = core_map.get(qid, {}).get("difficulty_level", "?") if qid in core_map else "?"

        tq["_id"] = qid
        tq["_dimension"] = dim
        tq["_difficulty"] = diff
        tq["_rubric"] = rubric
        tq["_expected_answer"] = expected
        tq["_user_message"] = user_msg
    return test_questions


def _get_client(api_key):
    client = getattr(_thread_local, "client", None)
    if client is None:
        from openai import OpenAI, DefaultHttpxClient
        client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com",
                        timeout=120, max_retries=1,
                        http_client=DefaultHttpxClient(proxy=None))
        _thread_local.client = client
    return client


def score_one(question, model_answer, judge_model, api_key):
    from benchmark.eval.judge import AScorer, BScorer
    client = _get_client(api_key)

    dim = question["_dimension"]
    q_text = question["_user_message"]
    expected = question["_expected_answer"]
    rubric = question.get("_rubric")

    try:
        if dim == "A":
            result = AScorer.judge(q_text, expected, model_answer, client, judge_model)
        elif dim == "B":
            result = BScorer.judge(q_text, expected, model_answer, client, judge_model)
        elif dim == "C" or (dim == "D" and not rubric):
            from benchmark.eval.judge import GenericScorer
            result = GenericScorer.judge(q_text, expected, model_answer, client, judge_model)
        elif dim == "D" and rubric:
            from benchmark.eval.judge import RubricScorer
            result = RubricScorer.judge(q_text, expected, model_answer, client, judge_model, rubric=rubric)
        else:
            result = {"score": 0.0, "reason": "Unknown dimension", "issues": ["unknown dimension"]}
    except Exception as e:
        result = {"score": 0.0, "reason": str(e), "issues": ["scoring error"]}

    return {
        "id": question["_id"],
        "dimension": dim,
        "difficulty_level": question["_difficulty"],
        "score": result["score"],
        "reason": result.get("reason", ""),
        "issues": result.get("issues", []),
        "model_answer": model_answer,
        "expected_answer": expected,
    }


def flush_report(output_path, records, total, judge_model):
    scores = [r["score"] for r in records]
    dim_scores = {}
    for r in records:
        d = r.get("dimension", "?")
        dim_scores.setdefault(d, []).append(r["score"])

    complete = len(records) >= total
    report = {
        "model": "qlora-finetuned-Qwen3.5-4B-text-only",
        "judge_model": judge_model,
        "total_questions": total,
        "overall_score": round(sum(scores) / len(scores), 4),
        "dimension_scores": {d: round(sum(v) / len(v), 4) for d, v in dim_scores.items()},
        "baseline": BASELINE,
        "delta_vs_baseline": round((sum(scores) / len(scores) - BASELINE["overall_score"]), 4),
        "complete": complete,
        "records": records,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    write_json_atomic(output_path, report)

    elapsed = time.time() - _start_time if _start_time else 0
    completed = len(records)
    rate = completed / (elapsed / 60) if elapsed > 0 else 0
    remaining = total - completed
    eta_min = remaining / rate if rate > 0 else 0

    write_status(output_path, {
        "status": "completed" if complete else "running",
        "completed": completed, "total": total,
        "percent": round(completed / total * 100, 1),
        "overall_sofar": round(sum(scores) / len(scores), 4),
        "elapsed_min": round(elapsed / 60, 1),
        "rate_q_per_min": round(rate, 1),
        "eta_min": round(eta_min, 0),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    })

    return complete


def run_parallel(answers, test_questions, judge_model, api_key, output_path,
                 max_workers=4, resume=False):
    global _start_time
    _start_time = time.time()

    records = []
    completed_ids = set()

    if resume and output_path.exists():
        try:
            existing = load_json(output_path)
            records = existing.get("records", [])
            completed_ids = {r["id"] for r in records}
            print(f"[RESUME] 已加载 {len(completed_ids)} 条已完成评分", flush=True)
        except Exception:
            pass

    answer_vals = list(answers.values())
    pending = []
    for i, q in enumerate(test_questions):
        if q["_id"] in completed_ids:
            continue
        model_ans = answers.get(q["_id"], "") or (answer_vals[i] if i < len(answer_vals) else "")
        pending.append((q, model_ans))
    total = len(test_questions)
    print(f"[JUDGE] 待评分: {len(pending)}/{total} | workers={max_workers} | model={judge_model}", flush=True)

    if not pending:
        print("[JUDGE] 全部已完成", flush=True)
        flush_report(output_path, records, total, judge_model)
        return records

    pending_idx = 0
    pending_lock = threading.Lock()

    def submit_all():
        nonlocal pending_idx
        while True:
            with pending_lock:
                if pending_idx >= len(pending):
                    return None, None
                idx = pending_idx
                pending_idx += 1
            return pending[idx][0], pending[idx][1]

    def worker():
        while True:
            question, model_answer = submit_all()
            if question is None:
                return

            qid = question["_id"]
            dim = question["_dimension"]
            t_start = time.time()
            record = score_one(question, model_answer, judge_model, api_key)
            dt = time.time() - t_start

            with _lock:
                records.append(record)
                completed_ids.add(qid)
                completed = len(records)
                elapsed = time.time() - _start_time
                rate = completed / (elapsed / 60) if elapsed > 0 else 0
                remaining = total - completed
                eta_min = remaining / rate if rate > 0 else 0

                flush_report(output_path, records, total, judge_model)

                append_jsonl(str(output_path) + ".progress.jsonl", {
                    "qid": qid, "dimension": dim, "score": record["score"],
                    "time_sec": round(dt, 1),
                    "elapsed_sec": round(elapsed, 1), "completed": completed,
                })

                print(f"  [{completed}/{total}] {qid} ({dim}) score={record['score']:.2f} "
                      f"t={dt:.1f}s rate={rate:.1f}q/m eta={eta_min:.0f}m", flush=True)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(worker) for _ in range(max_workers)]
        for f in as_completed(futures):
            f.result()

    elapsed = time.time() - _start_time
    complete = flush_report(output_path, records, total, judge_model)
    rate = len(records) / (elapsed / 60) if elapsed > 0 else 0
    print(f"\n[DONE] {len(records)}/{total} | {elapsed:.1f}s | ~{rate:.1f} q/min", flush=True)

    scores = [r["score"] for r in records]
    dim_scores = {}
    for r in records:
        d = r.get("dimension", "?")
        dim_scores.setdefault(d, []).append(r["score"])
    overall = sum(scores) / len(scores) if scores else 0
    delta = overall - BASELINE["overall_score"]
    print(f"  overall={overall:.4f}  delta={delta:+.4f}", flush=True)
    for d in sorted(dim_scores):
        avg = sum(dim_scores[d]) / len(dim_scores[d])
        base = BASELINE["dimension_scores"].get(d, 0)
        print(f"  dim={d}: {avg:.4f}  (baseline={base:.4f}, delta={avg-base:+.4f})", flush=True)

    return records


def main():
    parser = argparse.ArgumentParser(description="Phase 2 并行评分")
    parser.add_argument("--test", default=str(DEFAULT_TEST))
    parser.add_argument("--benchmark", default=str(DEFAULT_BENCHMARK))
    parser.add_argument("--answers", default=str(DEFAULT_ANSWERS))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--judge-model", default="deepseek-v4-flash")
    parser.add_argument("--api-key", default=DEEPSEEK_KEY)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    test_path = Path(args.test)
    benchmark_path = Path(args.benchmark)
    answers_path = Path(args.answers)
    output_path = Path(args.output)

    if not answers_path.exists():
        raise SystemExit(f"答案文件不存在: {answers_path}，请先运行 --phase generate")

    print(f"[LOAD] 加载题目: {test_path}")
    test_questions = load_test_questions(test_path, benchmark_path)
    print(f"[LOAD] {len(test_questions)} 题")

    print(f"[LOAD] 加载答案: {answers_path}")
    answers_data = load_json(answers_path)
    answers = answers_data.get("answers", {})
    if not answers:
        raise SystemExit("eval_answers.json 中无答案数据")
    print(f"[LOAD] {len(answers)} 条答案")

    run_parallel(answers, test_questions, args.judge_model, args.api_key,
                 output_path, max_workers=args.workers, resume=args.resume)


if __name__ == "__main__":
    main()
