"""Perplexity probe: compare base vs QLoRA on test.jsonl 89 questions.
Calculates cross-entropy loss on expected answers, lower ppl = better domain fit.
"""
import json
from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

MODEL_ID = "principled-intelligence/Qwen3.5-4B-text-only"
ADAPTER_PATH = Path("finetune/output/qlora-final")
TEST_PATH = Path("finetune/data/test.jsonl")

SYSTEM_PROMPT = "你是控制科学专家。请准确、专业、完整地回答以下问题。涉及公式推导时逐步写出。"

test = [json.loads(l) for l in TEST_PATH.read_text(encoding="utf-8").strip().split("\n")]
print(f"[LOAD] {len(test)} questions")

print("[LOAD] Base model...")
quant_config = BitsAndBytesConfig(
    load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
)
base_model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, quantization_config=quant_config, device_map="auto",
    trust_remote_code=True, attn_implementation="eager", dtype=torch.bfloat16,
).eval()
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def compute_ppl(model, user_msg, expected_answer):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
        {"role": "assistant", "content": expected_answer},
    ]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss.item()
    ppl = torch.exp(torch.tensor(loss)).item()
    return loss, ppl

base_losses = []
base_ppls = []
print("\n[BASE] Computing perplexity...")
for i, item in enumerate(test):
    user_msg = next((m["content"] for m in item.get("messages", []) if m.get("role") == "user"), "")
    assistant_msg = next((m["content"] for m in item.get("messages", []) if m.get("role") == "assistant"), "")
    if not assistant_msg:
        continue
    loss, ppl = compute_ppl(base_model, user_msg, assistant_msg)
    base_losses.append(loss)
    base_ppls.append(ppl)
    if (i + 1) % 10 == 0:
        avg_ppl = sum(base_ppls) / len(base_ppls)
        print(f"  [{i+1}/{len(test)}] avg_ppl={avg_ppl:.1f}", flush=True)

avg_base_ppl = sum(base_ppls) / len(base_ppls) if base_ppls else 0
print(f"[BASE] avg_ppl={avg_base_ppl:.1f}, avg_loss={sum(base_losses)/len(base_losses):.4f}")

del base_model
torch.cuda.empty_cache()

print("\n[LOAD] QLoRA model...")
qlora_model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, quantization_config=quant_config, device_map="auto",
    trust_remote_code=True, attn_implementation="eager", dtype=torch.bfloat16,
).eval()
qlora_model = PeftModel.from_pretrained(qlora_model, str(ADAPTER_PATH))
qlora_model.eval()

qlora_losses = []
qlora_ppls = []
print("\n[QLORA] Computing perplexity...")
for i, item in enumerate(test):
    user_msg = next((m["content"] for m in item.get("messages", []) if m.get("role") == "user"), "")
    assistant_msg = next((m["content"] for m in item.get("messages", []) if m.get("role") == "assistant"), "")
    if not assistant_msg:
        continue
    loss, ppl = compute_ppl(qlora_model, user_msg, assistant_msg)
    qlora_losses.append(loss)
    qlora_ppls.append(ppl)
    if (i + 1) % 10 == 0:
        avg_ppl = sum(qlora_ppls) / len(qlora_ppls)
        print(f"  [{i+1}/{len(test)}] avg_ppl={avg_ppl:.1f}", flush=True)

avg_qlora_ppl = sum(qlora_ppls) / len(qlora_ppls) if qlora_ppls else 0
print(f"[QLORA] avg_ppl={avg_qlora_ppl:.1f}, avg_loss={sum(qlora_losses)/len(qlora_losses):.4f}")

delta_ppl = avg_qlora_ppl - avg_base_ppl
delta_pct = (delta_ppl / avg_base_ppl * 100) if avg_base_ppl else 0

print(f"\n{'='*50}")
print(f"Perplexity Comparison")
print(f"{'='*50}")
print(f"  Base text-only:      avg_ppl={avg_base_ppl:.1f}")
print(f"  QLoRA fine-tuned:    avg_ppl={avg_qlora_ppl:.1f}")
print(f"  Δ ppl:               {delta_ppl:+.1f} ({delta_pct:+.1f}%)")
print(f"\n{'✓ Domain adaptation confirmed' if delta_ppl < 0 else '⚠ Worsened — unexpected'}")

result = {
    "analysis": "perplexity_delta",
    "base_model": MODEL_ID,
    "qlora_adapter": str(ADAPTER_PATH),
    "n_questions": len(test),
    "base_avg_ppl": round(avg_base_ppl, 2),
    "qlora_avg_ppl": round(avg_qlora_ppl, 2),
    "delta_ppl": round(delta_ppl, 2),
    "delta_percent": round(delta_pct, 1),
    "base_ppls": [round(p, 2) for p in base_ppls],
    "qlora_ppls": [round(p, 2) for p in qlora_ppls],
}
Path("finetune/output/perplexity_delta.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nSaved to finetune/output/perplexity_delta.json")
