"""QLoRA 9B 探针 — 5 分钟验证 base 模型可用性

规则 10.8.2：QLoRA 微调+评测前必须跑此脚本。
base 模型在 chat template 下可能输出 CoT 元分析而非答案，
5 分钟探针可避免 5h 训练浪费。

Usage:
    python -X utf8 _tools/probe_qlora_9b.py --model Qwen/Qwen3.5-9B --num-samples 5
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

COT_PATTERNS = [
    r"让我(?:们)?(?:来)?(?:思考|分析|想想|一步步|仔细)",
    r"我(?:需要|先|来)(?:分析|思考|理解|考虑|梳理)",
    r"首先[，,]",
    r"第一步",
    r"先来",
    r"Let\s+me\s+(think|analyze|consider|break|examine)",
    r"I\s+need\s+to\s+(analyze|think|consider)",
    r"Here.s\s+my\s+(thinking|analysis|thought|reasoning)",
    r"In\s+this\s+(problem|question|case)",
]


def load_sample_questions(n: int = 5):
    core_path = ROOT / "benchmark" / "dataset" / "core.json"
    with open(core_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    records = data if isinstance(data, list) else data.get("records", data.get("questions", []))
    selected = []
    dims_seen = set()
    for r in records:
        dim = r.get("dimension", r.get("dim", "?"))
        if dim not in dims_seen:
            dims_seen.add(dim)
            selected.append(r)
        if len(selected) >= n:
            break
    if len(selected) < n:
        print(f"[WARN] Only {len(selected)} dimensions available, "
              f"requested {n} samples", file=sys.stderr)
    return selected


def load_model(model_name: str):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    t0 = time.time()
    print(f"[MODEL] Loading {model_name} (4bit QLoRA ready)...", flush=True)

    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=quant_config,
        device_map="auto",
        trust_remote_code=True,
    ).eval()
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    elapsed = time.time() - t0
    print(f"   Loaded in {elapsed:.1f}s", flush=True)
    return model, tokenizer


def _detect_cot(answer: str) -> bool:
    answer_lower = answer[:200].lower()
    for pattern in COT_PATTERNS:
        if re.search(pattern, answer_lower):
            return True
    return False


def probe_one(model, tokenizer, record, idx: int, max_new_tokens: int = 512):
    import torch
    question = record.get("question", record.get("user_message", ""))
    dimension = record.get("dimension", record.get("dim", "?"))
    difficulty = record.get("difficulty", record.get("difficulty_level", "?"))

    system_prompt = (
        "你是一位控制科学专家。请用中文回答以下问题，"
        "直接给出答案，不要描述分析过程。"
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    t0 = time.time()
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
        )
    gen_time = time.time() - t0

    generated = outputs[0][inputs.input_ids.shape[1]:]
    answer = tokenizer.decode(generated, skip_special_tokens=True)

    input_tokens = inputs.input_ids.shape[1]
    output_tokens = generated.shape[0]

    cot_risk = _detect_cot(answer)

    print(f"  [{idx}] {dimension} L{difficulty} | {input_tokens}t in -> {output_tokens}t out | {gen_time:.1f}s | CoT_risk={'YES \u26a0\ufe0f' if cot_risk else 'OK'}", flush=True)
    if cot_risk:
        preview = answer[:200].replace("\n", "\\n")
        print(f"       Preview: {preview}...", flush=True)

    return {
        "idx": idx,
        "dimension": dimension,
        "difficulty": difficulty,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "time_s": round(gen_time, 1),
        "cot_risk": cot_risk,
        "answer_preview": answer[:200],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="Qwen/Qwen3.5-9B")
    parser.add_argument("--num-samples", type=int, default=5)
    parser.add_argument("--max-new-tokens", type=int, default=512)
    args = parser.parse_args()

    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 60)
    print(f"QLoRA 9B Probe: {args.model}")
    print(f"  Samples: {args.num_samples} (A/B/C/D 各一 + 额外)")
    print(f"  Max new tokens: {args.max_new_tokens}")
    print("=" * 60, flush=True)

    import torch

    if not torch.cuda.is_available():
        print("[FATAL] CUDA not available \u2014 probe requires GPU")
        sys.exit(1)
    print(f"[GPU] {torch.cuda.get_device_name(0)} "
          f"({torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB)")

    records = load_sample_questions(args.num_samples)
    print(f"[DATA] Loaded {len(records)} questions from core.json")

    model, tokenizer = load_model(args.model)

    print(f"\n[PROBE] Running {len(records)} samples...", flush=True)
    results = []
    cot_count = 0
    total_time = 0

    for i, rec in enumerate(records, 1):
        r = probe_one(model, tokenizer, rec, i, max_new_tokens=args.max_new_tokens)
        results.append(r)
        total_time += r["time_s"]
        if r["cot_risk"]:
            cot_count += 1

    print(f"\n{'='*60}")
    print(f"RESULTS: {len(results)} samples | {total_time:.1f}s total")
    print(f"  CoT risk: {cot_count}/{len(results)}")
    if cot_count == len(results):
        print(f"  VERDICT: \u274c BLOCKED \u2014 base model outputs CoT meta-analysis, NOT answers.")
        print(f"  \u2192 QLoRA fine-tuning is REQUIRED, but pre-training QA is useless.")
        print(f"  \u2192 Adjust strategy: QLoRA is mandatory, don't run pre-training eval.")
        sys.exit(2)
    elif cot_count > 0:
        print(f"  VERDICT: \u26a0\ufe0f PARTIAL \u2014 {cot_count}/{len(results)} samples show CoT patterns.")
        print(f"  \u2192 Run QLoRA fine-tuning BEFORE evaluation. Don't evaluate base model directly.")
        sys.exit(3)
    else:
        print(f"  VERDICT: \u2705 PASS \u2014 all {len(results)} samples produce clean answers.")
        print(f"  \u2192 Base model is instruction-aligned. Can evaluate before/after QLoRA.")
        sys.exit(0)


if __name__ == "__main__":
    main()
