"""S1.5 微调模型评测 — 加载 LoRA 适配器 + 在 test 集上评测

加载体 QLoRA 微调后的 PEFT 模型，在 test.jsonl 上逐题推理，
用 DeepSeek API 作为 Judge 评分，最终与 baseline (qwen3.5:9b, overall=0.6249) 对比。

前置条件: S1.4 QLoRA 训练已完成，产出 finetune/output/qlora-final/

产出:
  - finetune/output/eval_finetuned_report.json  微调模型评测报告
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
DEFAULT_OUTPUT = ROOT / "finetune" / "output" / "eval_finetuned_report.json"
DEFAULT_BENCHMARK = ROOT / "benchmark" / "dataset" / "core.json"

BASELINE = {
    "model": "qwen3.5:9b (baseline, 无微调)",
    "overall_score": 0.6249,
    "dimension_scores": {"A": 0.5688, "B": 0.6104, "C": 0.6620, "D": 0.6586},
}

DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY", "")

TARGET_SYSTEM_PROMPT = "你是控制科学专家。请准确、专业、完整地回答以下问题。涉及公式推导时逐步写出。"


def load_peft_model(config_path, adapter_path):
    import yaml
    import torch
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
    )

    print(f"[MODEL] 加载基座: {model_name}")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=quantization_config,
        device_map="auto",
        trust_remote_code=cfg["model"].get("trust_remote_code", False),
        attn_implementation=cfg["model"].get("attn_implementation", "eager"),
        dtype=torch_dtype,
    )

    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=cfg["model"].get("trust_remote_code", False),
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    adapter_path = Path(adapter_path)
    if not adapter_path.exists():
        available = sorted(ROOT.glob("finetune/output/qlora*/"))
        msg = f"适配器路径不存在: {adapter_path}"
        if available:
            msg += f"\n  可用路径: {[str(a) for a in available]}"
        raise SystemExit(msg)

    print(f"[ADAPTER] 加载 LoRA: {adapter_path}")
    model = PeftModel.from_pretrained(model, str(adapter_path))
    model.eval()
    return model, tokenizer, cfg


def generate_answer(model, tokenizer, question, max_new_tokens=2048, temperature=0.0):
    import torch
    messages = [
        {"role": "system", "content": TARGET_SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            do_sample=(temperature > 0),
            top_p=0.9,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    generated = outputs[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(generated, skip_special_tokens=True).strip()


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


def load_test_questions(test_path, benchmark_path=None):
    import re as _re
    test_questions = []
    with open(test_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                test_questions.append(json.loads(line))

    core_map = {}
    if benchmark_path:
        bp = Path(benchmark_path)
        if bp.exists():
            core = load_json(bp)
            core_map = {q["id"]: q for q in core.get("questions", [])}
        else:
            print(f"[WARN] benchmark 文件不存在: {bp}，将使用 JSONL 自带答案")

    for tq in test_questions:
        msgs = tq.get("messages", [])
        user_msg = next((m["content"] for m in msgs if m.get("role") == "user"), "")
        assistant_msg = next((m["content"] for m in msgs if m.get("role") == "assistant"), "")
        qid = _extract_qid(user_msg)

        tq["_id"] = qid or f"test-{hash(user_msg) % 10000}"
        tq["_dimension"] = "?"
        tq["_difficulty"] = "?"
        tq["_rubric"] = None
        tq["_expected_answer"] = assistant_msg

        if qid and qid in core_map:
            core_q = core_map[qid]
            tq["_dimension"] = core_q.get("dimension", "?")
            tq["_difficulty"] = core_q.get("difficulty_level", "?")
            tq["_rubric"] = core_q.get("rubric")
            tq["_expected_answer"] = core_q.get("answer", assistant_msg)

        if tq["_dimension"] == "?" and user_msg:
            dm = _re.search(r"\[维度:\s*([A-D])\]", user_msg)
            if dm:
                tq["_dimension"] = dm.group(1)

    return test_questions


def _extract_qid(user_msg):
    import re
    m = re.search(r"(CS-EVO-\d{5})", user_msg)
    return m.group(1) if m else None


def build_report(records, model_name, judge_model):
    scores = [r["score"] for r in records]
    dim_scores = {}
    for r in records:
        d = r.get("dimension", "?")
        if d not in dim_scores:
            dim_scores[d] = []
        dim_scores[d].append(r["score"])

    return {
        "model": model_name,
        "judge_model": judge_model,
        "scorer_version": "1.1",
        "scoring_mode": "llm_judge",
        "total_questions": len(records),
        "overall_score": round(sum(scores) / len(scores), 4) if scores else 0.0,
        "dimension_scores": {d: round(sum(v) / len(v), 4) for d, v in dim_scores.items()},
        "baseline": BASELINE,
        "delta_vs_baseline": round((sum(scores) / len(scores) - BASELINE["overall_score"]), 4) if scores else None,
        "records": records,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def write_status(output_path, status):
    path = Path(str(output_path) + ".status.json")
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def main():
    parser = argparse.ArgumentParser(description="S1.5 微调模型评测 — 加载 LoRA 适配器 + test 集评测")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="QLoRA 训练配置")
    parser.add_argument("--adapter", default=str(DEFAULT_ADAPTER), help="LoRA 适配器路径")
    parser.add_argument("--test", default=str(DEFAULT_TEST), help="test.jsonl 路径")
    parser.add_argument("--benchmark", default=str(DEFAULT_BENCHMARK), help="core.json 路径 (提取 rubric 等字段)")
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT), help="输出报告路径")
    parser.add_argument("--limit", type=int, default=0, help="限制评测题数 (0=全部)")
    parser.add_argument("--judge-model", default="deepseek-v4-flash", help="Judge 模型名")
    parser.add_argument("--api-key", default=None, help="DeepSeek API Key")
    parser.add_argument("--temperature", type=float, default=0.0, help="生成温度 (0=确定性/贪婪)")
    parser.add_argument("--resume", action="store_true", help="断点续传")
    args = parser.parse_args()

    test_path = Path(args.test)
    if not test_path.exists():
        raise SystemExit(f"test.jsonl 不存在: {test_path}")

    print("[S1.5] 微调模型评测开始")
    model, tokenizer, cfg = load_peft_model(args.config, args.adapter)

    test_questions = load_test_questions(test_path, args.benchmark)
    if args.limit and args.limit > 0:
        test_questions = test_questions[:args.limit]
    total = len(test_questions)
    print(f"[DATA] test 集: {total} 题")

    api_key = args.api_key or os.environ.get("DEEPSEEK_API_KEY") or DEEPSEEK_KEY
    from openai import OpenAI, DefaultHttpxClient
    judge_client = OpenAI(
        api_key=api_key, base_url="https://api.deepseek.com",
        timeout=120, max_retries=0,
        http_client=DefaultHttpxClient(proxy=None),
    )

    records = []
    completed_ids = set()
    if args.resume and Path(args.output).exists():
        try:
            existing = load_json(args.output)
            records = existing.get("records", [])
            completed_ids = {r["id"] for r in records}
            print(f"[RESUME] 已加载 {len(records)} 条已完成记录")
        except Exception as e:
            print(f"[WARN] 续传加载失败: {e}，重新开始")

    t0 = time.time()
    for i, tq in enumerate(test_questions):
        qid = tq["_id"]
        dim = tq["_dimension"]
        diff = tq["_difficulty"]
        question_text = next((m["content"] for m in tq.get("messages", []) if m.get("role") == "user"), "")
        expected = tq["_expected_answer"]
        rubric = tq.get("_rubric")

        if qid in completed_ids:
            print(f"[{i + 1}/{total}] {qid} ({dim}, {diff}) — 已完成，跳过", flush=True)
            continue

        print(f"[{i + 1}/{total}] {qid} ({dim}, {diff}) — 推理中...", flush=True)
        t_infer = time.time()
        try:
            model_answer = generate_answer(model, tokenizer, question_text, temperature=args.temperature)
        except Exception as e:
            print(f"  ERROR 推理: {e}", flush=True)
            model_answer = ""
        infer_time = time.time() - t_infer

        t_score = time.time()
        try:
            if model_answer:
                result = score_with_judge(
                    question_text, expected, model_answer, dim, rubric,
                    judge_client, args.judge_model,
                )
            else:
                result = {"score": 0.0, "reason": "Inference failed", "issues": ["inference failure"]}
        except Exception as e:
            print(f"  ERROR 评分: {e}", flush=True)
            result = {"score": 0.0, "reason": str(e), "issues": ["scoring error"]}
        score_time = time.time() - t_score

        record = {
            "id": qid,
            "dimension": dim,
            "difficulty_level": diff,
            "score": result["score"],
            "reason": result.get("reason", ""),
            "issues": result.get("issues", []),
            "model_answer": model_answer,
            "expected_answer": expected,
            "infer_time_sec": round(infer_time, 2),
            "score_time_sec": round(score_time, 2),
        }
        records.append(record)
        completed_ids.add(qid)
        print(f"  score={result['score']} (infer={infer_time:.1f}s, judge={score_time:.1f}s)", flush=True)

        partial_report = build_report(records, f"qlora-finetuned-{cfg['model']['name'].split('/')[-1]}", args.judge_model)
        partial_report["complete"] = len(records) >= total
        write_json_atomic(args.output, partial_report)

        elapsed = time.time() - t0
        completed = len(records)
        rate = completed / (elapsed / 60) if elapsed > 0 else 0
        remaining = total - completed
        eta_min = remaining / rate if rate > 0 else 0
        write_status(args.output, {
            "status": "running" if not partial_report["complete"] else "completed",
            "step": completed,
            "total": total,
            "percent": round(completed / total * 100, 1),
            "current_qid": qid,
            "current_dimension": dim,
            "last_score": record.get("score", 0),
            "elapsed_min": round(elapsed / 60, 1),
            "rate_q_per_min": round(rate, 1),
            "eta_min": round(eta_min, 0),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        })

    elapsed = time.time() - t0
    report = build_report(records, f"qlora-finetuned-{cfg['model']['name'].split('/')[-1]}", args.judge_model)
    report["run_metrics"] = {
        "total_time_sec": round(elapsed, 1),
        "avg_infer_sec": round(sum(r.get("infer_time_sec", 0) for r in records) / max(len(records), 1), 1),
        "avg_score_sec": round(sum(r.get("score_time_sec", 0) for r in records) / max(len(records), 1), 1),
    }

    write_json_atomic(args.output, report)
    write_status(args.output, {
        "status": "completed",
        "step": len(records),
        "total": total,
        "percent": 100.0,
        "overall_score": report["overall_score"],
        "dimension_scores": report["dimension_scores"],
        "delta_vs_baseline": report["delta_vs_baseline"],
        "elapsed_min": round(elapsed / 60, 1),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    })
    print(f"\n{'=' * 60}")
    print(f"[OK] 评测完成: {args.output}")
    print(f"  Overall: {report['overall_score']} (baseline: {BASELINE['overall_score']}, Δ={report['delta_vs_baseline']})")
    print(f"  Dimension scores: {report['dimension_scores']}")
    print(f"  总耗时: {elapsed / 60:.1f} min")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
