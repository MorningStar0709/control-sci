"""Medical Perplexity Probe: Base vs QLoRA on 3,348 chunks, stratified by medical_label.
Two modes:
  --mode raw:     compute PPL on raw chunk text (measures format specialization cost)
  --mode chatml:  wrap chunk in ChatML template to match training distribution (measures domain adaptation)
Delta across medical sections quantifies domain adaptation per section type.
"""
import argparse
import json
import sys
import os
import time
from pathlib import Path
from collections import defaultdict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

BASE_MODEL_ID = "principled-intelligence/Qwen3.5-4B-text-only"
ADAPTER_PATH = Path("finetune/output/qlora-medical/checkpoint-259")
MANIFEST_PATH = Path("data/sources_medical/chunks/chunks_manifest.json")
OUTPUT_DIR = Path("finetune/output/eval_medical_ppl")
MAX_SEQ_LENGTH = 2048
MIN_CHUNKS_PER_LABEL = 5

MEDICAL_SYSTEM_PROMPT = "你是一位临床医学研究专家，精通循证医学文献的解读与分析。请基于医学文献内容回答以下问题。"
MEDICAL_USER_QUERY = "请详细阅读并理解以下医学内容，提供完整的分析和解读。"


def load_chunks(manifest_path):
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    chunks = data["chunks"]
    print(f"[LOAD] {len(chunks)} chunks from manifest (train={data['train_chunks']}, eval={data['eval_chunks']})")
    return chunks


def read_chunk_text(chunk, base_dir="data/sources_medical/chunks"):
    filepath = chunk.get("filepath", "")
    if not filepath:
        return None
    full_path = Path(base_dir).parent.parent / filepath if not Path(filepath).exists() else Path(filepath)
    alt_path = Path(base_dir) / chunk.get("set", "train") / f"{chunk['chunk_id']}.md"
    for p in [Path(filepath), full_path, alt_path]:
        if p.exists():
            try:
                return p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                return None
    return None


def wrap_chatml(chunk_text):
    messages = [
        {"role": "system", "content": MEDICAL_SYSTEM_PROMPT},
        {"role": "user", "content": MEDICAL_USER_QUERY},
        {"role": "assistant", "content": chunk_text},
    ]
    return messages


def apply_chat_template(tokenizer, messages):
    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)


def compute_ppl_on_text(model, tokenizer, text, max_length=MAX_SEQ_LENGTH, mode="raw"):
    if not text or not text.strip():
        return None, None
    if mode == "chatml":
        messages = wrap_chatml(text)
        text = apply_chat_template(tokenizer, messages)
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=max_length,
    ).to(model.device)
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss.item()
    ppl = torch.exp(torch.tensor(loss)).item()
    return loss, ppl


def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_ID, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    return tokenizer


def load_base_model():
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_ID, quantization_config=quant_config, device_map="auto",
        trust_remote_code=True, attn_implementation="eager", dtype=torch.bfloat16,
    ).eval()
    return model


def load_qlora_model():
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_ID, quantization_config=quant_config, device_map="auto",
        trust_remote_code=True, attn_implementation="eager", dtype=torch.bfloat16,
    ).eval()
    model = PeftModel.from_pretrained(model, str(ADAPTER_PATH))
    model.eval()
    return model


def stratify_results(chunks, base_ppls, qlora_ppls):
    by_label = defaultdict(lambda: {"n": 0, "base_ppls": [], "qlora_ppls": []})
    by_parent = defaultdict(lambda: {"n": 0, "base_ppls": [], "qlora_ppls": []})

    for chunk, bp, qp in zip(chunks, base_ppls, qlora_ppls):
        if bp is None or qp is None:
            continue
        label = chunk.get("medical_label", "unknown") or "unknown"
        parent = chunk.get("medical_parent") or "root"
        by_label[label]["n"] += 1
        by_label[label]["base_ppls"].append(bp)
        by_label[label]["qlora_ppls"].append(qp)
        by_parent[parent]["n"] += 1
        by_parent[parent]["base_ppls"].append(bp)
        by_parent[parent]["qlora_ppls"].append(qp)

    def summarize(group, min_n=MIN_CHUNKS_PER_LABEL):
        result = {}
        for key, g in sorted(group.items()):
            if g["n"] < min_n:
                continue
            base_avg = sum(g["base_ppls"]) / g["n"]
            qlora_avg = sum(g["qlora_ppls"]) / g["n"]
            delta = qlora_avg - base_avg
            delta_pct = (delta / base_avg * 100) if base_avg else 0
            result[key] = {
                "n": g["n"],
                "base_avg_ppl": round(base_avg, 2),
                "qlora_avg_ppl": round(qlora_avg, 2),
                "delta_ppl": round(delta, 2),
                "delta_percent": round(delta_pct, 1),
            }
        return result

    return summarize(by_label), summarize(by_parent)


def run():
    parser = argparse.ArgumentParser(description="Medical Perplexity Probe")
    parser.add_argument("--mode", choices=["raw", "chatml"], default="chatml",
                        help="raw: raw text; chatml: wrap in ChatML template")
    args = parser.parse_args()
    mode = args.mode

    output_suffix = "_raw" if mode == "raw" else "_chatml"
    OUTPUT_PATH = OUTPUT_DIR / f"perplexity_medical{output_suffix}.json"
    PER_CHUNK_PATH = OUTPUT_DIR / f"per_chunk_ppls{output_suffix}.json"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    chunks = load_chunks(MANIFEST_PATH)
    print(f"[INFO] Mode: {mode}")
    print(f"[INFO] Using adapter: {ADAPTER_PATH}")
    print(f"[INFO] Max seq length: {MAX_SEQ_LENGTH}")
    print(f"[INFO] Min chunks per label: {MIN_CHUNKS_PER_LABEL}")

    tokenizer = load_tokenizer()

    chunk_texts = []
    valid_chunks = []
    for i, ch in enumerate(chunks):
        text = read_chunk_text(ch)
        if text and text.strip():
            chunk_texts.append(text)
            valid_chunks.append(ch)
        if (i + 1) % 500 == 0:
            print(f"  [LOAD TEXT] {i+1}/{len(chunks)} loaded, {len(valid_chunks)} valid")

    n = len(valid_chunks)
    print(f"[LOAD TEXT] Done: {n}/{len(chunks)} chunks have valid text")
    if n == 0:
        print("[FATAL] No valid chunks — aborting.")
        sys.exit(1)

    base_ppls = [None] * n
    base_losses = [None] * n

    print("\n[BASE] Loading base model...")
    t0 = time.time()
    base_model = load_base_model()
    print(f"  Loaded in {time.time()-t0:.0f}s")

    print(f"\n[BASE] Computing perplexity on {n} chunks ({mode})...")
    t_start = time.time()
    for i in range(n):
        loss, ppl = compute_ppl_on_text(base_model, tokenizer, chunk_texts[i], mode=mode)
        if loss is not None:
            base_losses[i] = loss
            base_ppls[i] = ppl
        if (i + 1) % 200 == 0 or (i + 1) == n:
            valid = sum(1 for p in base_ppls[:i+1] if p is not None)
            elapsed = time.time() - t_start
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            print(f"  [{i+1}/{n}] valid={valid}, elapsed={elapsed:.0f}s, rate={rate:.1f}chunk/s")

    valid_base = [p for p in base_ppls if p is not None]
    avg_base_ppl = sum(valid_base) / len(valid_base) if valid_base else 0
    print(f"[BASE] Done: {len(valid_base)}/{n} valid, avg_ppl={avg_base_ppl:.2f}, "
          f"elapsed={time.time()-t_start:.0f}s")

    del base_model
    torch.cuda.empty_cache()

    qlora_ppls = [None] * n
    qlora_losses = [None] * n

    print("\n[QLORA] Loading QLoRA model...")
    t0 = time.time()
    qlora_model = load_qlora_model()
    print(f"  Loaded in {time.time()-t0:.0f}s")

    print(f"\n[QLORA] Computing perplexity on {n} chunks ({mode})...")
    t_start = time.time()
    for i in range(n):
        loss, ppl = compute_ppl_on_text(qlora_model, tokenizer, chunk_texts[i], mode=mode)
        if loss is not None:
            qlora_losses[i] = loss
            qlora_ppls[i] = ppl
        if (i + 1) % 200 == 0 or (i + 1) == n:
            valid = sum(1 for p in qlora_ppls[:i+1] if p is not None)
            elapsed = time.time() - t_start
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            print(f"  [{i+1}/{n}] valid={valid}, elapsed={elapsed:.0f}s, rate={rate:.1f}chunk/s")

    valid_qlora = [p for p in qlora_ppls if p is not None]
    avg_qlora_ppl = sum(valid_qlora) / len(valid_qlora) if valid_qlora else 0
    print(f"[QLORA] Done: {len(valid_qlora)}/{n} valid, avg_ppl={avg_qlora_ppl:.2f}, "
          f"elapsed={time.time()-t_start:.0f}s")

    del qlora_model
    torch.cuda.empty_cache()

    both_valid = [(i, bp, qp) for i, (bp, qp) in enumerate(zip(base_ppls, qlora_ppls))
                  if bp is not None and qp is not None]
    n_valid = len(both_valid)
    base_vals = [bp for _, bp, _ in both_valid]
    qlora_vals = [qp for _, _, qp in both_valid]

    avg_base = sum(base_vals) / n_valid if n_valid else 0
    avg_qlora = sum(qlora_vals) / n_valid if n_valid else 0
    delta = avg_qlora - avg_base
    delta_pct = (delta / avg_base * 100) if avg_base else 0

    label_mode = "Raw Text" if mode == "raw" else "ChatML"
    print(f"\n{'='*60}")
    print(f"  Medical Perplexity Comparison [{label_mode}] ({n_valid} chunks)")
    print(f"{'='*60}")
    print(f"  Base text-only:      avg_ppl={avg_base:.2f}")
    print(f"  QLoRA fine-tuned:    avg_ppl={avg_qlora:.2f}")
    print(f"  Δ ppl:               {delta:+.2f} ({delta_pct:+.1f}%)")
    suffix = "✓ Domain adaptation confirmed" if delta < 0 else "╳ Format specialization cost"
    print(f"  {suffix}")
    print(f"{'='*60}")

    by_label, by_parent = stratify_results(
        valid_chunks, base_ppls, qlora_ppls)

    print(f"\n── By medical_label (top-level, n>={MIN_CHUNKS_PER_LABEL}) ──")
    print(f"  {'Label':<30s} {'n':>5s} {'Base PPL':>9s} {'QLoRA PPL':>10s} {'Δ%':>8s}")
    print(f"  {'-'*30} {'-'*5} {'-'*9} {'-'*10} {'-'*8}")
    for label, s in sorted(by_label.items(), key=lambda x: -x[1]["n"]):
        print(f"  {label:<30s} {s['n']:>5d} {s['base_avg_ppl']:>9.2f} "
              f"{s['qlora_avg_ppl']:>10.2f} {s['delta_percent']:>+7.1f}%")

    print(f"\n── By medical_parent (n>={MIN_CHUNKS_PER_LABEL}) ──")
    print(f"  {'Parent':<30s} {'n':>5s} {'Base PPL':>9s} {'QLoRA PPL':>10s} {'Δ%':>8s}")
    print(f"  {'-'*30} {'-'*5} {'-'*9} {'-'*10} {'-'*8}")
    for parent, s in sorted(by_parent.items(), key=lambda x: -x[1]["n"]):
        label = parent if parent != "root" else "(top-level)"
        print(f"  {label:<30s} {s['n']:>5d} {s['base_avg_ppl']:>9.2f} "
              f"{s['qlora_avg_ppl']:>10.2f} {s['delta_percent']:>+7.1f}%")

    report = {
        "analysis": f"medical_perplexity_delta_{mode}",
        "mode": mode,
        "label_mode": label_mode,
        "base_model": BASE_MODEL_ID,
        "qlora_adapter": str(ADAPTER_PATH),
        "total_chunks_in_manifest": len(chunks),
        "valid_chunks": n,
        "both_valid_pairs": n_valid,
        "overall": {
            "base_avg_ppl": round(avg_base, 2),
            "qlora_avg_ppl": round(avg_qlora, 2),
            "delta_ppl": round(delta, 2),
            "delta_percent": round(delta_pct, 1),
            "base_avg_loss": round(sum(bp for _, bp, _ in both_valid) / n_valid, 4) if n_valid else 0,
            "qlora_avg_loss": round(sum(qp for _, _, qp in both_valid) / n_valid, 4) if n_valid else 0,
        },
        "by_label": by_label,
        "by_parent": by_parent,
    }

    OUTPUT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[SAVE] Report: {OUTPUT_PATH}")

    per_chunk = []
    for i, (base_p, qlora_p) in enumerate(zip(base_ppls, qlora_ppls)):
        if base_p is not None and qlora_p is not None:
            per_chunk.append({
                "chunk_id": valid_chunks[i]["chunk_id"],
                "set": valid_chunks[i].get("set", ""),
                "medical_label": valid_chunks[i].get("medical_label", ""),
                "medical_parent": valid_chunks[i].get("medical_parent"),
                "estimated_tokens": valid_chunks[i].get("estimated_tokens", 0),
                "base_ppl": round(base_p, 2),
                "qlora_ppl": round(qlora_p, 2),
            })
    PER_CHUNK_PATH.write_text(
        json.dumps(per_chunk, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[SAVE] Per-chunk data: {PER_CHUNK_PATH} ({len(per_chunk)} entries)")


if __name__ == "__main__":
    os.environ["PYTHONUTF8"] = "1"
    run()
