"""4B 裸模型 baseline 评测 — Ollama 推理 + DeepSeek 评分

与 S1.5 微调版形成公平对比（同基座、同数据、同 prompt、同 judge），
唯一变量：加不加 LoRA。

Usage:
    python finetune/scripts/eval_4b_baseline.py                # 全新跑
    python finetune/scripts/eval_4b_baseline.py --resume       # 续传
    python finetune/scripts/eval_4b_baseline.py --compare-only # 仅做对比报告
"""
import argparse
import hashlib
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
DEFAULT_OUTPUT = ROOT / "finetune" / "output" / "eval_baseline_4b_report.json"
FINETUNED_REPORT = ROOT / "finetune" / "output" / "eval_finetuned_report.json"

OLLAMA_URL = "http://localhost:11434/v1"
OLLAMA_MODEL = "qwen3.5:4b"
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY", "")
JUDGE_MODEL = "deepseek-v4-flash"

SYSTEM_PROMPT = "你是控制科学专家。请准确、专业、完整地回答以下问题。涉及公式推导时逐步写出。"

BASELINE_9B = {
    "model": "qwen3.5:9b (baseline, 无微调)",
    "overall_score": 0.6249,
    "dimension_scores": {"A": 0.5688, "B": 0.6104, "C": 0.6620, "D": 0.6586},
}

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
        qid = qid.group(1) if qid else "test-" + hashlib.md5(user_msg.encode()).hexdigest()[:4]
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


def _get_ollama_client():
    client = getattr(_thread_local, "ollama_client", None)
    if client is None:
        from openai import OpenAI, DefaultHttpxClient
        client = OpenAI(base_url=OLLAMA_URL, api_key="ollama",
                        timeout=300, max_retries=1,
                        http_client=DefaultHttpxClient(proxy=None))
        _thread_local.ollama_client = client
    return client


def _get_judge_client():
    client = getattr(_thread_local, "judge_client", None)
    if client is None:
        from openai import OpenAI, DefaultHttpxClient
        client = OpenAI(api_key=DEEPSEEK_KEY, base_url="https://api.deepseek.com",
                        timeout=120, max_retries=1,
                        http_client=DefaultHttpxClient(proxy=None))
        _thread_local.judge_client = client
    return client


def infer_one(question):
    client = _get_ollama_client()
    try:
        resp = client.chat.completions.create(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question["_user_message"]},
            ],
            temperature=0,
            max_tokens=4096,
            extra_body={"reasoning_effort": "none"},
        )
        return resp.choices[0].message.content or ""
    except Exception as e:
        print(f"  [OLLAMA ERR] {question['_id']}: {e}", flush=True)
        return ""


def score_one(question, model_answer):
    from benchmark.eval.judge import AScorer, BScorer
    client = _get_judge_client()

    dim = question["_dimension"]
    q_text = question["_user_message"]
    expected = question["_expected_answer"]
    rubric = question.get("_rubric")

    try:
        if dim == "A":
            result = AScorer.judge(q_text, expected, model_answer, client, JUDGE_MODEL)
        elif dim == "B":
            result = BScorer.judge(q_text, expected, model_answer, client, JUDGE_MODEL)
        elif dim == "C" or (dim == "D" and not rubric):
            from benchmark.eval.judge import GenericScorer
            result = GenericScorer.judge(q_text, expected, model_answer, client, JUDGE_MODEL)
        elif dim == "D" and rubric:
            from benchmark.eval.judge import RubricScorer
            result = RubricScorer.judge(q_text, expected, model_answer, client, JUDGE_MODEL, rubric=rubric)
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


def flush_report(output_path, records, total):
    scores = [r["score"] for r in records]
    dim_scores = {}
    for r in records:
        d = r.get("dimension", "?")
        dim_scores.setdefault(d, []).append(r["score"])

    complete = len(records) >= total
    report = {
        "model": "qwen3.5:4b (Ollama, 无微调)",
        "judge_model": JUDGE_MODEL,
        "total_questions": total,
        "overall_score": round(sum(scores) / len(scores), 4) if scores else 0,
        "dimension_scores": {d: round(sum(v) / len(v), 4) for d, v in dim_scores.items()},
        "baseline_9b": BASELINE_9B,
        "complete": complete,
        "records": records,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    if FINETUNED_REPORT.exists():
        try:
            ft = load_json(FINETUNED_REPORT)
            report["finetuned_4b"] = {
                "model": "qwen3.5:4b + QLoRA",
                "overall_score": ft.get("overall_score"),
                "dimension_scores": ft.get("dimension_scores", {}),
            }
            delta = round((sum(scores) / len(scores) - ft.get("overall_score", 0)), 4) if scores else 0
            report["delta_vs_finetuned"] = delta
        except Exception:
            pass
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
        "overall_sofar": round(sum(scores) / len(scores), 4) if scores else 0,
        "elapsed_min": round(elapsed / 60, 1),
        "rate_q_per_min": round(rate, 1),
        "eta_min": round(eta_min, 0),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    })

    return complete


def run_parallel(test_questions, output_path, max_workers=2, resume=False):
    global _start_time
    _start_time = time.time()

    records = []
    completed_ids = set()

    if resume and output_path.exists():
        try:
            existing = load_json(output_path)
            records = existing.get("records", [])
            completed_ids = {r["id"] for r in records}
            print(f"[RESUME] 已加载 {len(completed_ids)} 条已完成", flush=True)
        except Exception:
            pass

    pending = [q for q in test_questions if q["_id"] not in completed_ids]
    total = len(test_questions)
    print(f"[BASELINE] 待评测: {len(pending)}/{total} | workers={max_workers} | model={OLLAMA_MODEL}", flush=True)

    if not pending:
        print("[BASELINE] 全部已完成", flush=True)
        flush_report(output_path, records, total)
        return records

    pending_idx = 0
    pending_lock = threading.Lock()

    def next_task():
        nonlocal pending_idx
        with pending_lock:
            if pending_idx >= len(pending):
                return None
            idx = pending_idx
            pending_idx += 1
        return pending[idx]

    def worker():
        while True:
            question = next_task()
            if question is None:
                return

            qid = question["_id"]
            dim = question["_dimension"]
            t_start = time.time()
            model_answer = infer_one(question)
            dt_infer = time.time() - t_start

            t_score = time.time()
            record = score_one(question, model_answer)
            dt_score = time.time() - t_score

            with _lock:
                records.append(record)
                completed_ids.add(qid)
                completed = len(records)
                elapsed = time.time() - _start_time
                rate = completed / (elapsed / 60) if elapsed > 0 else 0
                remaining = total - completed
                eta_min = remaining / rate if rate > 0 else 0

                flush_report(output_path, records, total)

                append_jsonl(str(output_path) + ".progress.jsonl", {
                    "qid": qid, "dimension": dim, "score": record["score"],
                    "infer_sec": round(dt_infer, 1),
                    "judge_sec": round(dt_score, 1),
                    "elapsed_sec": round(elapsed, 1), "completed": completed,
                })

                print(f"  [{completed}/{total}] {qid} ({dim}) score={record['score']:.2f} "
                      f"infer={dt_infer:.1f}s judge={dt_score:.1f}s "
                      f"rate={rate:.1f}q/m eta={eta_min:.0f}m", flush=True)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(worker) for _ in range(max_workers)]
        for f in as_completed(futures):
            f.result()

    elapsed = time.time() - _start_time
    complete = flush_report(output_path, records, total)
    rate = len(records) / (elapsed / 60) if elapsed > 0 else 0
    print(f"\n[DONE] {len(records)}/{total} | {elapsed:.1f}s | ~{rate:.1f} q/min", flush=True)

    scores = [r["score"] for r in records]
    dim_scores = {}
    for r in records:
        d = r.get("dimension", "?")
        dim_scores.setdefault(d, []).append(r["score"])
    overall = sum(scores) / len(scores) if scores else 0
    print(f"  overall={overall:.4f}", flush=True)
    for d in sorted(dim_scores):
        avg = sum(dim_scores[d]) / len(dim_scores[d])
        print(f"  dim={d}: {avg:.4f}", flush=True)

    if FINETUNED_REPORT.exists():
        try:
            ft = load_json(FINETUNED_REPORT)
            ft_overall = ft.get("overall_score", 0)
            delta = overall - ft_overall
            print(f"\n  Δ vs 微调版: {delta:+.4f}  (微调={ft_overall:.4f})", flush=True)
        except Exception:
            pass

    return records


def main():
    parser = argparse.ArgumentParser(description="4B 裸模型 baseline 评测")
    parser.add_argument("--test", default=str(DEFAULT_TEST))
    parser.add_argument("--benchmark", default=str(DEFAULT_BENCHMARK))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--workers", type=int, default=1, help="Ollama 并发数 (GPU 密集，建议 1)")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--compare-only", action="store_true", help="仅输出对比报告")
    args = parser.parse_args()

    test_path = Path(args.test)
    benchmark_path = Path(args.benchmark)
    output_path = Path(args.output)

    if args.compare_only:
        print("[COMPARE-ONLY]", flush=True)
        if not output_path.exists():
            raise SystemExit(f"No baseline report yet: {output_path}")
    else:
        print(f"[LOAD] 加载题目: {test_path}")
        test_questions = load_test_questions(test_path, benchmark_path)
        print(f"[LOAD] {len(test_questions)} 题")

        run_parallel(test_questions, output_path,
                     max_workers=args.workers, resume=args.resume)

    if not output_path.exists():
        return

    report = load_json(output_path)
    print(f"\n{'='*60}")
    print("  4B Baseline vs 微调 vs 9B Reference")
    print(f"{'='*60}")
    print()

    baseline_4b = {
        "label": "4B 未微调",
        "overall": report.get("overall_score", 0),
        "dims": report.get("dimension_scores", {}),
    }
    print_model(baseline_4b)

    ft_data = report.get("finetuned_4b", {})
    if ft_data:
        ft = {
            "label": "4B + QLoRA",
            "overall": ft_data.get("overall_score", 0),
            "dims": ft_data.get("dimension_scores", {}),
        }
        print_model(ft)

        delta_ov = ft["overall"] - baseline_4b["overall"]
        print(f"\n  微调增益 Δ overall = {delta_ov:+.4f}")
        for d in ["A", "B", "C", "D"]:
            df = ft["dims"].get(d, 0)
            db = baseline_4b["dims"].get(d, 0)
            print(f"    Δ {d} = {df - db:+.4f}  ({db:.4f} → {df:.4f})")

    print()
    print_model({"label": "9B 参考", "overall": BASELINE_9B["overall_score"], "dims": BASELINE_9B["dimension_scores"]})


def print_model(m):
    print(f"  {m['label']:12s}  overall={m['overall']:.4f}  "
          f"A={m['dims'].get('A', '-'):.4f}  B={m['dims'].get('B', '-'):.4f}  "
          f"C={m['dims'].get('C', '-'):.4f}  D={m['dims'].get('D', '-'):.4f}")


if __name__ == "__main__":
    main()
