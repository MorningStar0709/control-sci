"""S1.5 两阶段评测 — 按后台进程监控规范，每题原子写入 + status + progress + 续传

Phase 1: 批量推理 89 题 (GPU 100%)
  - torch.compile 加速
  - 每题原子写入 eval_answers.json
  - 每题写 eval_answers.status.json (step/rate/eta/updated_at)
  - 每题追加 eval_answers.progress.jsonl
  - --resume 跳过已完成 ID

Phase 2: DeepSeek API 评分 (无 GPU, 可前台跑)
  - 每题原子写入 eval_finetuned_report.json
  - status + progress 同 Phase 1 pattern
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from benchmark.eval.utils import load_json, write_json_atomic

DEFAULT_CONFIG = ROOT / "finetune" / "config" / "qlora_config.yaml"
DEFAULT_ADAPTER = ROOT / "finetune" / "output" / "qlora-final"
DEFAULT_TEST = ROOT / "finetune" / "data" / "test.jsonl"
DEFAULT_ANSWERS = ROOT / "finetune" / "output" / "eval_answers.json"
DEFAULT_BENCHMARK = ROOT / "benchmark" / "dataset" / "core.json"
DEFAULT_OUTPUT = ROOT / "finetune" / "output" / "eval_finetuned_report.json"

BASELINE = {
    "model": "qwen3.5:9b (baseline, 无微调)",
    "overall_score": 0.6249,
    "dimension_scores": {"A": 0.5688, "B": 0.6104, "C": 0.6620, "D": 0.6586},
}

DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY", "")
TARGET_SYSTEM_PROMPT = "你是控制科学专家。请准确、专业、完整地回答以下问题。涉及公式推导时逐步写出。"


def append_jsonl(path, line):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")


def write_status_checkpoint(base_path, data):
    path = Path(str(base_path) + ".status.json")
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def load_peft_model(config_path, adapter_path, attn_impl=None):
    import yaml, torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    from peft import PeftModel

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    model_name = cfg["model"]["name"]
    bnb_cfg = cfg["bitsandbytes"]
    compute_dtype = getattr(torch, bnb_cfg["bnb_4bit_compute_dtype"])
    torch_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=bnb_cfg["load_in_4bit"],
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_quant_type=bnb_cfg["bnb_4bit_quant_type"],
        bnb_4bit_use_double_quant=bnb_cfg.get("bnb_4bit_use_double_quant", False),
        bnb_4bit_quant_storage=torch_dtype,
    )

    _attn = attn_impl or "sdpa"
    print(f"[MODEL] 加载基座: {model_name}  (attn={_attn})")
    model = AutoModelForCausalLM.from_pretrained(
        model_name, quantization_config=quantization_config,
        device_map="auto", trust_remote_code=cfg["model"].get("trust_remote_code", False),
        attn_implementation=_attn,
        dtype=torch_dtype,
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=cfg["model"].get("trust_remote_code", False))
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    print(f"[ADAPTER] 加载 LoRA: {adapter_path}")
    model = PeftModel.from_pretrained(model, str(adapter_path))
    model.eval()
    return model, tokenizer, cfg


def load_base_model(config_path, model_name_override=None):
    import yaml, torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    model_name = model_name_override or cfg["model"]["name"]
    bnb_cfg = cfg["bitsandbytes"]
    compute_dtype = getattr(torch, bnb_cfg["bnb_4bit_compute_dtype"])
    torch_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=bnb_cfg["load_in_4bit"],
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_quant_type=bnb_cfg["bnb_4bit_quant_type"],
        bnb_4bit_use_double_quant=bnb_cfg.get("bnb_4bit_use_double_quant", False),
        bnb_4bit_quant_storage=torch_dtype,
    )

    print(f"[MODEL] 加载基座（裸模型）: {model_name}")
    model = AutoModelForCausalLM.from_pretrained(
        model_name, quantization_config=quantization_config,
        device_map="auto", trust_remote_code=cfg["model"].get("trust_remote_code", False),
        attn_implementation="sdpa",
        dtype=torch_dtype,
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=cfg["model"].get("trust_remote_code", False))
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"
    model.eval()
    return model, tokenizer, cfg


def generate_batch(model, tokenizer, questions):
    import torch
    texts = []
    for q in questions:
        msgs = [{"role": "system", "content": TARGET_SYSTEM_PROMPT}, {"role": "user", "content": q}]
        texts.append(tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True))
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True).to(model.device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=512, do_sample=False,
                                 pad_token_id=tokenizer.pad_token_id, eos_token_id=tokenizer.eos_token_id,
                                 cache_implementation="static")
    input_len = inputs["input_ids"].shape[1]
    return [tokenizer.decode(outputs[i][input_len:], skip_special_tokens=True).strip() for i in range(len(questions))]


def phase1_generate(model, tokenizer, test_questions, output_path, resume=False, batch_size=4):
    total = len(test_questions)
    answers = {}
    completed_ids = set()
    t0 = time.time()

    if resume and output_path.exists():
        try:
            existing = load_json(output_path)
            answers = existing.get("answers", {})
            completed_ids = set(answers.keys())
            print(f"[RESUME] Phase 1: {len(completed_ids)}/{total} 已完成", flush=True)
        except Exception:
            pass

    pending = [(i, tq) for i, tq in enumerate(test_questions) if tq["_id"] not in completed_ids]
    if not pending:
        print("Phase 1: 全部完成", flush=True)
        return answers

    batches = [pending[i:i+batch_size] for i in range(0, len(pending), batch_size)]
    print(f"Phase 1: {len(pending)} 题待推理 batch={batch_size} → {len(batches)} batches", flush=True)

    for bi, batch in enumerate(batches):
        qids = [tq["_id"] for _, tq in batch]
        dims = [tq["_dimension"] for _, tq in batch]
        questions = [next((m["content"] for m in tq.get("messages", []) if m.get("role") == "user"), "") for _, tq in batch]

        t_start = time.time()
        batch_answers = generate_batch(model, tokenizer, questions)
        dt = time.time() - t_start

        for ki in range(len(batch)):
            qid, dim, ans = qids[ki], dims[ki], batch_answers[ki]
            answers[qid] = ans
            completed_ids.add(qid)
            print(f"  [{len(answers)}/{total}] {qid} ({dim}) {len(ans)} chars", flush=True)

        elapsed = time.time() - t0
        avg_rate = len(answers) / (elapsed / 60) if elapsed > 0 else 0
        eta_min = (total - len(answers)) / avg_rate if avg_rate > 0 else 0

        write_json_atomic(output_path, {"answers": answers, "total": total, "completed": len(answers), "elapsed_sec": round(elapsed, 1)})
        write_status_checkpoint(output_path, {
            "status": "running", "completed": len(answers), "total": total,
            "percent": round(len(answers)/total*100, 1), "elapsed_min": round(elapsed/60, 1),
            "rate_q_per_min": round(avg_rate, 1), "eta_min": round(eta_min, 0),
            "batch_size": batch_size, "updated_at": datetime.now(timezone.utc).isoformat(),
        })
        for ki in range(len(batch)):
            append_jsonl(str(output_path) + ".progress.jsonl", {"qid": qids[ki], "dimension": dims[ki],
                "chars": len(batch_answers[ki]), "elapsed_sec": round(elapsed, 1), "completed": len(answers)})

        print(f"  [batch {bi+1}/{len(batches)}] {len(answers)}/{total} {dt:.1f}s/batch ({dt/len(batch):.1f}s/题) rate={avg_rate:.1f} q/min eta={eta_min:.0f} min", flush=True)

    elapsed = time.time() - t0
    write_json_atomic(output_path, {"answers": answers, "total": total, "completed": total, "elapsed_sec": round(elapsed, 1)})
    write_status_checkpoint(output_path, {"status": "completed", "completed": total, "total": total, "percent": 100.0,
        "elapsed_min": round(elapsed/60, 1), "updated_at": datetime.now(timezone.utc).isoformat()})
    avg = elapsed / total if total > 0 else 0
    print(f"\n✅ Phase 1 完成: {output_path}")
    print(f"   {total} 题, {elapsed/60:.1f} min, {avg:.1f}s/题  (batch={batch_size})")
    return answers


def score_with_judge(question, expected, model_answer, dimension, rubric, client, judge_model):
    from benchmark.eval.judge import AScorer, BScorer
    if dimension == "A":
        return AScorer.judge(question, expected, model_answer, client, judge_model)
    if dimension == "B":
        return BScorer.judge(question, expected, model_answer, client, judge_model)
    if dimension == "C" or (dimension == "D" and not rubric):
        from benchmark.eval.judge import GenericScorer
        return GenericScorer.judge(question, expected, model_answer, client, judge_model)
    if dimension == "D" and rubric:
        from benchmark.eval.judge import RubricScorer
        return RubricScorer.judge(question, expected, model_answer, client, judge_model, rubric=rubric)
    return {"score": 0.0, "reason": "Unknown dimension", "issues": ["unknown dimension"]}


def phase2_judge(answers, test_questions, judge_model, api_key, output_path, resume=False):
    from openai import OpenAI, DefaultHttpxClient
    total = len(test_questions)
    judge_client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com",
                          timeout=120, max_retries=0, http_client=DefaultHttpxClient(proxy=None))

    records = []
    completed_ids = set()
    t0 = time.time()
    step_times = []

    if resume and output_path.exists():
        try:
            existing = load_json(output_path)
            records = existing.get("records", [])
            completed_ids = {r["id"] for r in records}
            print(f"[RESUME] Phase 2: 已加载 {len(completed_ids)} 条已完成评分", flush=True)
        except Exception:
            pass

    for i, tq in enumerate(test_questions):
        qid = tq["_id"]
        if qid in completed_ids:
            continue

        dim = tq["_dimension"]
        diff = tq["_difficulty"]
        question_text = next((m["content"] for m in tq.get("messages", []) if m.get("role") == "user"), "")
        expected = tq["_expected_answer"]
        rubric = tq.get("_rubric")
        model_answer = answers.get(qid, "")

        completed_now = i + 1
        print(f"[{completed_now}/{total}] {qid} ({dim}) — 评分中...", flush=True)
        try:
            result = score_with_judge(question_text, expected, model_answer, dim, rubric, judge_client, judge_model)
        except Exception as e:
            result = {"score": 0.0, "reason": str(e), "issues": ["scoring error"]}

        record = {"id": qid, "dimension": dim, "difficulty_level": diff, "score": result["score"],
                  "reason": result.get("reason", ""), "issues": result.get("issues", []),
                  "model_answer": model_answer, "expected_answer": expected}
        records.append(record)
        completed_ids.add(qid)
        step_times.append((len(records), time.time() - t0))
        print(f"  score={result['score']}", flush=True)

        completed = len(records)
        elapsed = time.time() - t0
        recent_rate = 0
        if len(step_times) >= 2:
            recent = step_times[-5:] if len(step_times) >= 5 else step_times
            d_cnt = recent[-1][0] - recent[0][0]
            d_sec = recent[-1][1] - recent[0][1]
            recent_rate = d_cnt / (d_sec / 60) if d_sec > 0 else 0
        remaining = total - completed
        eta_min = remaining / recent_rate if recent_rate > 0 else 0

        scores = [r["score"] for r in records]
        dim_scores = {}
        for r in records:
            d = r.get("dimension", "?")
            dim_scores.setdefault(d, []).append(r["score"])

        partial = {
            "model": "qlora-finetuned-Qwen3.5-4B-text-only", "judge_model": judge_model,
            "total_questions": total, "overall_score": round(sum(scores) / len(scores), 4),
            "dimension_scores": {d: round(sum(v) / len(v), 4) for d, v in dim_scores.items()},
            "baseline": BASELINE,
            "delta_vs_baseline": round((sum(scores) / len(scores) - BASELINE["overall_score"]), 4),
            "records": records,
            "complete": completed >= total,
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        write_json_atomic(output_path, partial)
        write_status_checkpoint(output_path, {
            "status": "running" if completed < total else "completed",
            "completed": completed, "total": total,
            "percent": round(completed / total * 100, 1),
            "current_qid": qid, "current_dimension": dim,
            "last_score": result.get("score", 0),
            "overall_sofar": round(sum(scores) / len(scores), 4),
            "elapsed_min": round(elapsed / 60, 1),
            "rate_q_per_min": round(recent_rate, 1),
            "eta_min": round(eta_min, 0),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        })

        append_jsonl(str(output_path) + ".progress.jsonl", {
            "qid": qid, "dimension": dim, "score": result["score"],
            "elapsed_sec": round(elapsed, 1), "completed": completed,
        })

        avg_rate = completed / (elapsed / 60) if elapsed > 0 else 0
        print(f"  [{completed}/{total}] recent_rate={recent_rate:.1f} q/min, eta={eta_min:.0f} min", flush=True)

    elapsed = time.time() - t0
    scores = [r["score"] for r in records]
    dim_scores = {}
    for r in records:
        d = r.get("dimension", "?")
        dim_scores.setdefault(d, []).append(r["score"])

    report = {
        "model": "qlora-finetuned-Qwen3.5-4B-text-only", "judge_model": judge_model,
        "total_questions": total, "overall_score": round(sum(scores) / len(scores), 4),
        "dimension_scores": {d: round(sum(v) / len(v), 4) for d, v in dim_scores.items()},
        "baseline": BASELINE,
        "delta_vs_baseline": round((sum(scores) / len(scores) - BASELINE["overall_score"]), 4),
        "run_metrics": {"total_time_sec": round(elapsed, 1)},
        "records": records, "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    write_json_atomic(output_path, report)
    write_status_checkpoint(output_path, {"status": "completed", "completed": total, "total": total,
                                           "percent": 100.0, "overall_score": report["overall_score"],
                                           "dimension_scores": report["dimension_scores"],
                                           "delta_vs_baseline": report["delta_vs_baseline"],
                                           "elapsed_min": round(elapsed / 60, 1),
                                           "updated_at": datetime.now(timezone.utc).isoformat()})
    print(f"\n✅ Phase 2 完成: overall={report['overall_score']}, Δ={report['delta_vs_baseline']}")
    return report


def load_test_questions(test_path, benchmark_path=None):
    import re as _re
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=["generate", "judge", "both"], default="both")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--adapter", default=str(DEFAULT_ADAPTER))
    parser.add_argument("--test", default=str(DEFAULT_TEST))
    parser.add_argument("--answers", default=str(DEFAULT_ANSWERS))
    parser.add_argument("--benchmark", default=str(DEFAULT_BENCHMARK))
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--judge-model", default="deepseek-v4-flash")
    parser.add_argument("--resume", action="store_true", help="断点续传 — 跳过已完成题")
    parser.add_argument("--no-compile", action="store_true")
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--base", default=None, help="裸模型 HF ID（跳过 LoRA，用于基线评测）")
    parser.add_argument("--no-adapter", action="store_true", help="不加载 LoRA 适配器")
    args = parser.parse_args()

    test_questions = load_test_questions(args.test, args.benchmark)
    print(f"[DATA] test 集: {len(test_questions)} 题")

    if args.phase in ("generate", "both"):
        if args.no_adapter or args.base:
            model, tokenizer, cfg = load_base_model(args.config, args.base)
        else:
            model, tokenizer, cfg = load_peft_model(args.config, args.adapter)
        import torch
        if args.no_compile:
            print("  torch.compile: disabled", flush=True)
        else:
            model = torch.compile(model, mode="reduce-overhead")
            print("  torch.compile: reduce-overhead", flush=True)
        answers = phase1_generate(model, tokenizer, test_questions, Path(args.answers), resume=args.resume, batch_size=args.batch_size)
        if args.phase == "generate":
            print("Phase 1 完成。运行 --phase judge --resume 进行评分。")
            return

    if args.phase in ("judge", "both"):
        if args.phase == "judge":
            if not Path(args.answers).exists():
                raise SystemExit(f"答案文件不存在: {args.answers}，请先运行 --phase generate")
            with open(args.answers, encoding="utf-8") as f:
                answers = json.load(f)["answers"]
        phase2_judge(answers, test_questions, args.judge_model, DEEPSEEK_KEY, Path(args.output), resume=args.resume)


if __name__ == "__main__":
    main()
