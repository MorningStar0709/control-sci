import argparse
import glob
import hashlib
import json
import os
import random
import re
import time
import yaml
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = ROOT / "finetune" / "config" / "qlora_config.yaml"

CHECKPOINT_PATTERN = re.compile(r"checkpoint-(\d+)")


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def write_status(output_dir, status):
    path = Path(output_dir) / "training.status.json"
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def compute_config_fingerprint(cfg, include_seed=True):
    keys = [
        ("model.name", cfg["model"]["name"]),
        ("model.attn", cfg["model"].get("attn_implementation", "eager")),
        ("lora.r", cfg["lora"]["r"]),
        ("lora.alpha", cfg["lora"]["lora_alpha"]),
        ("lora.target_modules", str(cfg["lora"]["target_modules"])),
        ("train.batch_size", cfg["training"]["per_device_train_batch_size"]),
        ("train.grad_accum", cfg["training"]["gradient_accumulation_steps"]),
        ("train.epochs", cfg["training"]["num_train_epochs"]),
        ("train.lr", cfg["training"]["learning_rate"]),
        ("train.optim", cfg["training"].get("optim", "adamw_torch")),
        ("data.train_file", cfg["data"]["train_file"]),
        ("data.val_file", cfg["data"]["val_file"]),
        ("data.max_seq", cfg["data"].get("max_seq_length", 2048)),
    ]
    if include_seed:
        keys.append(("train.seed", cfg["training"].get("seed", 42)))
    payload = "|".join(f"{k}={v}" for k, v in keys)
    return hashlib.md5(payload.encode()).hexdigest()


def find_latest_checkpoint(output_dir):
    if not os.path.isdir(output_dir):
        return None
    best_step = -1
    best_path = None
    for name in os.listdir(output_dir):
        m = CHECKPOINT_PATTERN.match(name)
        if m:
            step = int(m.group(1))
            if step > best_step:
                best_step = step
                best_path = os.path.join(output_dir, name)
    if best_path is None:
        return None
    trainer_state = os.path.join(best_path, "trainer_state.json")
    if not os.path.exists(trainer_state):
        return None
    return {"path": best_path, "step": best_step, "trainer_state": trainer_state}


def set_reproducibility_seed(seed: int) -> None:
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    try:
        import numpy as np
        np.random.seed(seed)
    except Exception:
        pass
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except Exception:
        pass
    try:
        from transformers import set_seed
        set_seed(seed)
    except Exception:
        pass


def validate_resume(checkpoint_info, cfg):
    trainer_state_path = checkpoint_info["trainer_state"]
    try:
        state = json.loads(Path(trainer_state_path).read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False, "无法读取 trainer_state.json"
    saved_fp = state.get("log_history", [{}])[0].get("config_fingerprint")
    if saved_fp is None:
        return True, "旧版checkpoint（无指纹），信任续传"
    current_fp = compute_config_fingerprint(cfg)
    legacy_fp = compute_config_fingerprint(cfg, include_seed=False)
    if saved_fp not in {current_fp, legacy_fp}:
        return False, f"配置不兼容: checkpoint指纹={saved_fp[:8]}... 当前={current_fp[:8]}..."
    return True, "配置指纹匹配"


def write_run_config(output_dir, cfg, resume_step):
    run_path = Path(output_dir) / "training.run.json"
    tmp = run_path.with_name(run_path.name + ".tmp")
    tmp.write_text(json.dumps({
        "model": cfg["model"]["name"],
        "config_fingerprint": compute_config_fingerprint(cfg),
        "resume_from_step": resume_step,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "config_snapshot": {
            "lora": {k: str(v) for k, v in cfg["lora"].items()},
            "training": {k: str(v) for k, v in cfg["training"].items() if k not in ("output_dir",)},
        },
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(run_path)


def check_env(cfg):
    print("=" * 60, flush=True)
    print("[ENV] 环境检查", flush=True)

    import torch
    cuda_ok = torch.cuda.is_available()
    print(f"  PyTorch: {torch.__version__}", flush=True)
    print(f"  CUDA available: {cuda_ok}", flush=True)
    if cuda_ok:
        print(f"  CUDA version: {torch.version.cuda}", flush=True)
        for i in range(torch.cuda.device_count()):
            mem_gb = torch.cuda.get_device_properties(i).total_memory / 1024**3
            print(f"  GPU[{i}]: {torch.cuda.get_device_name(i)} ({mem_gb:.1f} GB)", flush=True)
    else:
        print("[WARN] CUDA 不可用，将在 CPU 上运行（极慢）", flush=True)

    bf16_supported = cuda_ok and torch.cuda.is_bf16_supported()
    if cfg["training"].get("bf16") and not bf16_supported:
        print("[WARN] bf16 不可用，回退为 fp16", flush=True)
        cfg["training"]["bf16"] = False
        cfg["training"]["fp16"] = True
        cfg["bitsandbytes"]["bnb_4bit_compute_dtype"] = "float16"
    print(f"  bf16: {bf16_supported}, fp16: {cuda_ok}", flush=True)

    try:
        import bitsandbytes as bnb
        print(f"  bitsandbytes: {bnb.__version__}", flush=True)
    except ImportError:
        raise SystemExit("[FATAL] bitsandbytes 未安装，请先 pip install bitsandbytes>=0.43")

    try:
        import transformers
        import peft
        import trl
        print(f"  transformers: {transformers.__version__}", flush=True)
        print(f"  peft: {peft.__version__}", flush=True)
        print(f"  trl: {trl.__version__}", flush=True)
    except ImportError as e:
        raise SystemExit(f"[FATAL] 缺少依赖: {e}")

    print("=" * 60, flush=True)
    return cuda_ok


def setup_model_and_tokenizer(cfg, cuda_ok):
    print("[MODEL] 加载基座模型 + Tokenizer...", flush=True)

    import torch
    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        BitsAndBytesConfig,
    )

    model_name = cfg["model"]["name"]
    print(f"  模型: {model_name}", flush=True)

    bnb_cfg = cfg["bitsandbytes"]
    compute_dtype = getattr(torch, bnb_cfg["bnb_4bit_compute_dtype"])
    torch_dtype = torch.bfloat16 if cuda_ok and torch.cuda.is_bf16_supported() else torch.float16
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=bnb_cfg["load_in_4bit"],
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_quant_type=bnb_cfg["bnb_4bit_quant_type"],
        bnb_4bit_use_double_quant=bnb_cfg.get("bnb_4bit_use_double_quant", False),
        bnb_4bit_quant_storage=compute_dtype,
    )

    attn_impl = cfg["model"].get("attn_implementation", "eager")
    print(f"  目标 attn: {attn_impl}", flush=True)

    try:
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            quantization_config=quantization_config,
            device_map="auto",
            trust_remote_code=cfg["model"].get("trust_remote_code", False),
            attn_implementation=attn_impl,
            dtype=torch_dtype,
        )
        print(f"  attn_implementation: {attn_impl}", flush=True)
    except (ImportError, ValueError, OSError) as e:
        print(f"  [WARN] {attn_impl} 加载失败 ({e})，回退 eager", flush=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            quantization_config=quantization_config,
            device_map="auto",
            trust_remote_code=cfg["model"].get("trust_remote_code", False),
            attn_implementation="eager",
            dtype=torch_dtype,
        )
        print(f"  attn_implementation: eager (fallback)", flush=True)

    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=cfg["model"].get("trust_remote_code", False),
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    print(f"  词表大小: {len(tokenizer)}", flush=True)
    return model, tokenizer


def apply_lora(model, cfg):
    print("[LORA] 应用 LoRA 适配器...", flush=True)

    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

    model = prepare_model_for_kbit_training(model)

    lora_cfg = cfg["lora"]
    peft_config = LoraConfig(
        r=lora_cfg["r"],
        lora_alpha=lora_cfg["lora_alpha"],
        target_modules=lora_cfg["target_modules"],
        lora_dropout=lora_cfg["lora_dropout"],
        bias=lora_cfg["bias"],
        task_type=lora_cfg["task_type"],
        init_lora_weights=lora_cfg.get("init_lora_weights", "gaussian"),
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()
    return model


def load_datasets(cfg, tokenizer):
    print("[DATA] 加载训练数据...", flush=True)

    from datasets import load_dataset

    data_cfg = cfg["data"]
    train_path = str(ROOT / data_cfg["train_file"])
    val_path = str(ROOT / data_cfg["val_file"])

    for label, p in [("train", train_path), ("val", val_path)]:
        if not Path(p).exists():
            raise SystemExit(f"[FATAL] {label} 数据文件不存在: {p}")

    dataset = load_dataset("json", data_files={
        "train": train_path,
        "validation": val_path,
    })

    print(f"  train: {len(dataset['train'])} 条", flush=True)
    print(f"  val:   {len(dataset['validation'])} 条", flush=True)

    def format_messages(examples):
        texts = []
        for msgs in examples["messages"]:
            texts.append(tokenizer.apply_chat_template(
                msgs,
                tokenize=False,
                add_generation_prompt=False,
            ))
        return {"text": texts}

    dataset = dataset.map(format_messages, batched=True, remove_columns=dataset["train"].column_names)
    return dataset


def train(cfg, model, tokenizer, dataset, resume_from_checkpoint=None, resumed=False):
    if resumed:
        print("[RESUME] 从 checkpoint 续传...", flush=True)
        print(f"  checkpoint: {resume_from_checkpoint}", flush=True)
    else:
        print("[TRAIN] 开始 QLoRA 训练...", flush=True)

    from transformers import TrainingArguments, TrainerCallback
    from trl import SFTTrainer

    t_cfg = cfg["training"]
    seed = int(t_cfg.get("seed", 42))
    output_dir = str(ROOT / t_cfg["output_dir"])
    os.makedirs(output_dir, exist_ok=True)

    effective_bs = t_cfg["per_device_train_batch_size"] * t_cfg["gradient_accumulation_steps"]
    steps_per_epoch = max(1, len(dataset["train"]) // effective_bs)
    total_steps = steps_per_epoch * t_cfg["num_train_epochs"]
    warmup_steps = int(total_steps * t_cfg["warmup_ratio"])

    log_dir = str(ROOT / t_cfg["output_dir"] / "logs")
    os.environ["TENSORBOARD_LOGGING_DIR"] = log_dir

    training_args = TrainingArguments(
        output_dir=output_dir,
        per_device_train_batch_size=t_cfg["per_device_train_batch_size"],
        gradient_accumulation_steps=t_cfg["gradient_accumulation_steps"],
        num_train_epochs=t_cfg["num_train_epochs"],
        learning_rate=t_cfg["learning_rate"],
        logging_steps=t_cfg["logging_steps"],
        save_steps=t_cfg["save_steps"],
        eval_steps=t_cfg["eval_steps"],
        save_total_limit=t_cfg["save_total_limit"],
        warmup_steps=warmup_steps,
        lr_scheduler_type=t_cfg["lr_scheduler_type"],
        bf16=t_cfg.get("bf16", False),
        fp16=t_cfg.get("fp16", False),
        gradient_checkpointing=t_cfg.get("gradient_checkpointing", False),
        gradient_checkpointing_kwargs=t_cfg.get("gradient_checkpointing_kwargs", {"use_reentrant": True}),
        dataloader_num_workers=t_cfg.get("dataloader_num_workers", 0),
        remove_unused_columns=t_cfg.get("remove_unused_columns", False),
        max_grad_norm=t_cfg.get("max_grad_norm", 1.0),
        optim=t_cfg.get("optim", "adamw_torch"),
        seed=seed,
        data_seed=seed,
        eval_strategy="steps",
        save_strategy="steps",
        load_best_model_at_end=False,
        report_to="none",
    )

    config_fp = compute_config_fingerprint(cfg)

    class StatusCallback(TrainerCallback):
        def __init__(self, output_dir, total_steps, t0, resumed):
            self.output_dir = output_dir
            self.total_steps = total_steps
            self.t0 = t0
            self.step_times = []
            self.resumed = resumed
            self._fp_written = False

        def on_step_begin(self, args, state, control, **kwargs):
            if not self._fp_written and state.global_step > 0:
                self._fp_written = True
                write_status(self.output_dir, {
                    "status": "training",
                    "resumed": self.resumed,
                    "step": state.global_step,
                    "total_steps": self.total_steps,
                    "seed": seed,
                    "config_fingerprint": config_fp,
                    "elapsed_min": round((time.time() - self.t0) / 60, 1),
                    "updated_at": datetime.now(timezone.utc).isoformat(),
                })

        def on_log(self, args, state, control, logs=None, **kwargs):
            elapsed = time.time() - self.t0
            self.step_times.append((state.global_step, elapsed))
            recent_rate = 0
            if len(self.step_times) >= 2:
                recent = self.step_times[-5:] if len(self.step_times) >= 5 else self.step_times
                d_steps = recent[-1][0] - recent[0][0]
                d_time = recent[-1][1] - recent[0][1]
                recent_rate = d_steps / d_time * 60 if d_time > 0 else 0

            remaining = self.total_steps - state.global_step
            eta_min = remaining / recent_rate if recent_rate > 0 else 0

            write_status(self.output_dir, {
                "status": "training",
                "resumed": self.resumed,
                "step": state.global_step,
                "total_steps": self.total_steps,
                "epoch": round(state.epoch, 2) if state.epoch else 0,
                "loss": logs.get("loss") if logs else None,
                "eval_loss": logs.get("eval_loss") if logs else None,
                "learning_rate": logs.get("learning_rate") if logs else None,
                "elapsed_min": round(elapsed / 60, 1),
                "rate_steps_per_min": round(recent_rate, 1),
                "eta_min": round(eta_min, 0),
                "config_fingerprint": config_fp,
                "updated_at": datetime.now(timezone.utc).isoformat(),
            })

    status_cb = StatusCallback(output_dir, total_steps, time.time(), resumed)

    data_cfg = cfg["data"]
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"],
        processing_class=tokenizer,
        callbacks=[status_cb],
    )

    use_compile = t_cfg.get("torch_compile", False)
    if use_compile:
        import torch
        model = torch.compile(model, mode="reduce-overhead")
        print("  torch.compile: reduce-overhead", flush=True)

    print(f"  有效 batch size: {t_cfg['per_device_train_batch_size']} × {t_cfg['gradient_accumulation_steps']} = {effective_bs}", flush=True)
    print(f"  epoch: {t_cfg['num_train_epochs']}", flush=True)
    print(f"  lr: {t_cfg['learning_rate']}", flush=True)
    print(f"  warmup steps: {warmup_steps} / {total_steps}", flush=True)
    print(f"  save steps: {t_cfg['save_steps']}", flush=True)
    print(f"  配置指纹: {config_fp[:8]}...", flush=True)
    print()

    train_result = trainer.train(resume_from_checkpoint=resume_from_checkpoint)
    elapsed = time.time() - status_cb.t0

    write_status(output_dir, {
        "status": "completed",
        "step": train_result.global_step,
        "total_steps": total_steps,
        "training_loss": round(train_result.training_loss, 4) if train_result.training_loss else None,
        "elapsed_min": round(elapsed / 60, 1),
        "seed": seed,
        "config_fingerprint": config_fp,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    })

    print(f"\n[DONE] 训练完成，耗时 {elapsed/60:.1f} min ({elapsed:.0f} s)", flush=True)
    print(f"  总步数: {train_result.global_step}", flush=True)
    print(f"  训练损失: {train_result.training_loss:.4f}", flush=True)

    final_dir = str(Path(output_dir).parent / (Path(output_dir).name + "-final"))
    trainer.save_model(final_dir)
    tokenizer.save_pretrained(final_dir)
    print(f"  模型保存到: {final_dir}", flush=True)

    eval_results = trainer.evaluate()
    print(f"  验证损失: {eval_results.get('eval_loss', 'N/A')}", flush=True)

    return final_dir


def estimate_tokens(dataset, tokenizer, max_seq_length, train_cfg):
    print("[EST] 估算 Token 量...", flush=True)
    sample_count = min(len(dataset["train"]), 20)
    import random
    rng = random.Random(42)
    indices = rng.sample(range(len(dataset["train"])), sample_count)
    lengths = []
    for idx in indices:
        tokens = len(tokenizer.encode(dataset["train"][idx]["text"], add_special_tokens=False))
        lengths.append(min(tokens, max_seq_length))
    avg_len = sum(lengths) / len(lengths)
    total_est = avg_len * len(dataset["train"])
    print(f"  采样 {sample_count} 条, 平均长度: {avg_len:.0f} tokens", flush=True)
    print(f"  train 总 token 估算: {total_est:.0f}", flush=True)
    effective_bs = train_cfg["per_device_train_batch_size"] * train_cfg["gradient_accumulation_steps"]
    steps_per_epoch = int(len(dataset["train"]) / effective_bs)
    print(f"  估计 steps/epoch: ~{steps_per_epoch}", flush=True)


def main():
    parser = argparse.ArgumentParser(description="QLoRA 指令微调 — ControlSci")
    parser.add_argument("--config", type=str, default=str(DEFAULT_CONFIG), help="YAML 配置文件路径")
    parser.add_argument("--dry-run", action="store_true", help="仅检查环境，不启动训练")
    parser.add_argument("--resume", action="store_true", help="强制从最新checkpoint续传")
    parser.add_argument("--force", action="store_true", help="忽略已有checkpoint，从头训练")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        raise SystemExit(f"配置文件不存在: {config_path}")

    cfg = load_config(config_path)
    seed = int(cfg.get("training", {}).get("seed", 42))
    set_reproducibility_seed(seed)
    print(f"[CONFIG] {config_path}", flush=True)
    print(f"  model: {cfg['model']['name']}", flush=True)
    print(f"  lora r={cfg['lora']['r']}, alpha={cfg['lora']['lora_alpha']}", flush=True)
    print(f"  seed={seed}", flush=True)
    print()

    cuda_ok = check_env(cfg)

    if args.dry_run:
        print("[DRY-RUN] 环境检查通过", flush=True)
        print("[DRY-RUN] 验证模型加载（首次会下载 ~8GB，后续缓存）...", flush=True)
        model, tokenizer = setup_model_and_tokenizer(cfg, cuda_ok)
        total_params = sum(p.numel() for p in model.parameters())
        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print(f"[DRY-RUN] 模型加载成功: {total_params/1e6:.0f}M params ({trainable_params/total_params*100:.1f}% trainable)", flush=True)
        print("[DRY-RUN] 全部检查通过，未启动训练", flush=True)
        return

    if not cuda_ok:
        print("[WARN] 继续在 CPU 上训练（将非常缓慢）", flush=True)

    output_dir = str(ROOT / cfg["training"]["output_dir"])
    resumed = False
    resume_from_checkpoint = None
    checkpoint_info = find_latest_checkpoint(output_dir)

    if checkpoint_info and not args.force:
        if args.resume:
            ok, msg = validate_resume(checkpoint_info, cfg)
            if not ok:
                raise SystemExit(f"[FATAL] 续传校验失败: {msg}\n  如需从头训练，请加 --force 或删除 {output_dir}/")
            print(f"[DETECT] 发现 checkpoint-{checkpoint_info['step']} — {msg}", flush=True)
            print(f"  路径: {checkpoint_info['path']}", flush=True)
            print(f"  将从此 checkpoint 续传", flush=True)
            print()
            resumed = True
            resume_from_checkpoint = checkpoint_info["path"]
        else:
            print(f"[DETECT] 发现 checkpoint-{checkpoint_info['step']}", flush=True)
            print(f"  路径: {checkpoint_info['path']}", flush=True)
            print(f"  将自动续传...", flush=True)
            ok, msg = validate_resume(checkpoint_info, cfg)
            if not ok:
                raise SystemExit(f"[FATAL] 续传校验失败: {msg}\n  如需从头训练，请加 --force 或删除 {output_dir}/")
            print(f"  校验: {msg}", flush=True)
            print()
            resumed = True
            resume_from_checkpoint = checkpoint_info["path"]
    elif checkpoint_info and args.force:
        print(f"[FORCE] 忽略已有 checkpoint-{checkpoint_info['step']}，从头训练", flush=True)
        print()
    else:
        if checkpoint_info:
            print(f"[NOTE] checkpoint存在但 --force 生效，从头训练", flush=True)
        print("[FRESH] 未检测到checkpoint，从头训练", flush=True)
        print()

    model, tokenizer = setup_model_and_tokenizer(cfg, cuda_ok)
    model = apply_lora(model, cfg)
    dataset = load_datasets(cfg, tokenizer)

    estimate_tokens(dataset, tokenizer, cfg["data"].get("max_seq_length", 2048), cfg["training"])
    print()

    os.makedirs(output_dir, exist_ok=True)
    write_run_config(output_dir, cfg, checkpoint_info["step"] if resumed else 0)

    final_dir = train(cfg, model, tokenizer, dataset,
                      resume_from_checkpoint=resume_from_checkpoint,
                      resumed=resumed)

    print()
    print("=" * 60, flush=True)
    print(f"[OUTPUT] 微调适配器: {final_dir}", flush=True)
    print("=" * 60, flush=True)


if __name__ == "__main__":
    main()
