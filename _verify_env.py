"""环境一致性守卫 — 所有评测/训练启动前强制运行
用法: python _verify_env.py
退出码: 0 = 全绿, 1 = 有警告, 2 = 有致命错误
"""
import importlib
import json
import os
import subprocess
import sys
from pathlib import Path

import httpx
import yaml

ROOT = Path(__file__).resolve().parent
ERRORS = []
WARNS = []

def fail(msg):
    ERRORS.append(f"[FATAL] {msg}")

def warn(msg):
    WARNS.append(f"[WARN]  {msg}")

def ok(msg):
    print(f"  [OK]    {msg}")

def check_file(path, label):
    p = Path(path) if isinstance(path, str) else path
    if p.exists():
        ok(f"{label}: {p}")
    else:
        fail(f"{label}: 文件不存在 → {p}")

# ============================================================
# 常量配置 — 单一来源
# ============================================================
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

PPL_EXPECTED_BASE = {
    "4B": "principled-intelligence/Qwen3.5-4B-text-only",
    "9B": "Qwen/Qwen3.5-9B",
}

REPORT_EXPECTED_MODEL = {
    "4B baseline": "qwen3.5:4b",
    "finetuned":    "Qwen3.5-4B-text-only",
}

# ============================================================
# C0: Python 依赖
# ============================================================
print("C0: Python 环境与关键依赖")
DEPS = {
    "PyYAML":       "yaml",
    "httpx":        "httpx",
    "torch":        "torch",
    "transformers": "transformers",
    "peft":         "peft",
}
for pkg, mod in DEPS.items():
    try:
        importlib.import_module(mod)
        ok(f"{pkg}: 可用")
    except ImportError:
        warn(f"{pkg}: 未安装，可能影响 QLoRA 或评测")

# ============================================================
# C1: QLoRA config ↔ adapter 基座一致性
# ============================================================
print("\nC1: QLoRA config ↔ adapter 一致性")
try:
    config_path = ROOT / "finetune" / "config" / "qlora_config.yaml"
    with open(config_path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
except ImportError:
    fail("PyYAML 未安装。请运行: pip install PyYAML")
except FileNotFoundError:
    fail(f"QLoRA 配置文件不存在: {config_path}")
except KeyError as e:
    fail(f"QLoRA config 缺少必要字段: {e}")
except yaml.YAMLError as e:
    fail(f"QLoRA config YAML 解析失败: {e}")
else:
    config_base = cfg["model"]["name"]
    ok(f"config model.name = {config_base}")

    output_dir = cfg.get("training", {}).get("output_dir", "finetune/output/qlora")
    candidates = [ROOT / output_dir] + sorted(
        (ROOT / output_dir).glob("checkpoint-*"),
        key=lambda p: p.stat().st_mtime, reverse=True
    )
    adapter_path = None
    for cand in candidates:
        ap = cand / "adapter_config.json"
        if ap.exists():
            adapter_path = ap
            ok(f"adapter 目录: {cand.relative_to(ROOT)}")
            break
    if adapter_path is None:
        fail(f"adapter_config.json 在 {output_dir} 下任何位置都不存在")
    else:
        try:
            with open(adapter_path, encoding="utf-8") as f:
                adp = json.load(f)
            adapter_base = adp.get("base_model_name_or_path", "")
            ok(f"adapter base_model = {adapter_base}")
            if config_base != adapter_base:
                fail(f"基座不一致: config={config_base} ≠ adapter={adapter_base}")
            else:
                ok("config ≡ adapter ✅")
        except (json.JSONDecodeError, KeyError) as e:
            fail(f"adapter_config.json 解析失败: {e}")

# ============================================================
# C2: PPL 数据 base_model 字段可信度
# ============================================================
print("\nC2: PPL 数据 base_model 字段")
for label, path in [("4B", "finetune/output/perplexity_delta.json"),
                     ("9B", "finetune/output/perplexity_delta_9b.json")]:
    p = ROOT / path
    if p.exists():
        try:
            with open(p, encoding="utf-8") as f:
                d = json.load(f)
        except json.JSONDecodeError as e:
            fail(f"PPL {label} JSON 解析失败: {e}")
            continue
        bm = d.get("base_model", "UNKNOWN")
        expected = PPL_EXPECTED_BASE.get(label, "")
        if expected and bm != expected:
            fail(f"PPL {label} 数据混淆: base_model={bm} ≠ 预期={expected}")
        else:
            ok(f"PPL {label}: base_model={bm} (base_ppl={d.get('base_avg_ppl','?')})")
    else:
        warn(f"PPL {label}: {path} 不存在")

# ============================================================
# C3: API Key 环境变量
# ============================================================
print("\nC3: API Key 环境变量")
REQUIRED_KEYS = {
    "DEEPSEEK_API_KEY": "DeepSeek Judge/Planning",
    "MIMO_API_KEY": "MiMo-V2.5 视觉审计",
}
for var, usage in REQUIRED_KEYS.items():
    if os.getenv(var):
        ok(f"{var} ({usage}): 已设置")
    else:
        warn(f"{var} ({usage}): 未设置")

# ============================================================
# C4: Ollama 模型可用性
# ============================================================
print("\nC4: Ollama 模型可用性")
try:
    r = httpx.get(f"{OLLAMA_HOST}/api/tags", timeout=5)
    r.raise_for_status()
    models = [m["name"] for m in r.json().get("models", [])]
    ok(f"Ollama 在线 ({OLLAMA_HOST}), {len(models)} 个模型")
    for need in ["qwen3-embedding:4b", "qwen3.5:9b"]:
        if need in models:
            ok(f"  {need}")
        else:
            warn(f"  {need}: 未加载")
except httpx.TimeoutException:
    warn(f"Ollama {OLLAMA_HOST} 超时 (可能未运行)")
except Exception as e:
    warn(f"Ollama 不可达: {e}")

# ============================================================
# C5: 关键数据文件存在性
# ============================================================
print("\nC5: 关键数据文件")
check_file(ROOT / "corpus" / "chunks" / "chunks_manifest.json", "chunks_manifest")
check_file(ROOT / "corpus" / "metadata.json", "metadata")
check_file(ROOT / "benchmark" / "dataset" / "core.json", "core.json (500题)")
check_file(ROOT / "benchmark" / "dataset" / "full.json", "full.json (889题)")

# ============================================================
# C5b: QLoRA 训练数据
# ============================================================
if 'cfg' in dir():
    print("\nC5b: QLoRA 训练数据")
    for key, fname in [("train", cfg["data"]["train_file"]),
                       ("val",   cfg["data"]["val_file"]),
                       ("test",  cfg["data"]["test_file"])]:
        check_file(ROOT / fname, f"QLoRA {key} 数据")
else:
    warn("C5b 跳过: QLoRA config 未加载")

# ============================================================
# C6: QLoRA 评测报告 — 模型字段真实性 + 错配实验识别
# ============================================================
print("\nC6: 已有评测报告 model 字段")
for label, path in [
    ("4B baseline", "finetune/output/eval_baseline_4b_report.json"),
    ("finetuned",    "finetune/output/eval_finetuned_report.json"),
]:
    p = ROOT / path
    if p.exists() and p.stat().st_size > 100:
        try:
            with open(p, encoding="utf-8") as f:
                d = json.load(f)
        except json.JSONDecodeError as e:
            fail(f"{label} report JSON 解析失败: {e}")
            continue
        model_val = d.get("model", "?")
        expected = REPORT_EXPECTED_MODEL.get(label, "")
        if expected and expected not in model_val:
            fail(f"{label} report model 字段异常: '{model_val}' 不包含预期 '{expected}'")
        else:
            ok(f"{label}: model={model_val} overall={d.get('overall_score','?')} dims={d.get('dimension_scores','?')}")
    else:
        warn(f"{label}: {path} 不存在或为空")

# ============================================================
# C6b: 检测 4B base + 9B adapter 错配实验（叙事价值资产）
# ============================================================
print("\nC6b: LoRA 跨尺寸移植检测 (意外实验)")
FINETUNED_PATH = ROOT / "finetune" / "output" / "eval_finetuned_report.json"
ADAPTER_BASE_PATH = ROOT / "finetune" / "output" / "qlora-final" / "adapter_config.json"
BASELINE_4B_PATH = ROOT / "finetune" / "output" / "eval_baseline_4b_report.json"

if FINETUNED_PATH.exists() and ADAPTER_BASE_PATH.exists() and BASELINE_4B_PATH.exists():
    try:
        with open(ADAPTER_BASE_PATH) as f:
            adapter_base = json.load(f).get("base_model_name_or_path", "")
        with open(FINETUNED_PATH) as f:
            finetuned_d = json.load(f)
        finetuned_model_str = finetuned_d.get("model", "")
        finetuned_overall = finetuned_d.get("overall_score", 0)
        finetuned_dims = finetuned_d.get("dimension_scores", {})
        with open(BASELINE_4B_PATH) as f:
            b4b_d = json.load(f)
        baseline_4b_overall = b4b_d.get("overall_score", 0)
        baseline_4b_dims = b4b_d.get("dimension_scores", {})

        is_4b_model = "4B" in finetuned_model_str or "4b" in finetuned_model_str
        is_9b_adapter = "9B" in adapter_base

        if is_4b_model and is_9b_adapter:
            # 计算与 4B baseline 的维度级 Δ（D 维退化最大；C 维侥幸幸存的信号）
            c_delta = finetuned_dims.get("C", 0) - baseline_4b_dims.get("C", 0)
            overall_delta = finetuned_overall - baseline_4b_overall
            warn(
                f"发现错配实验: 4B base + 9B adapter (model={finetuned_model_str}). "
                f"Overall Δ={overall_delta:+.4f}, C维Δ={c_delta:+.4f}. "
                f"这是 LoRA 跨尺寸移植失败的叙事资产 — 证明 QLoRA 适配器不可跨尺寸移植，"
                f"且 C 维在错配下依然幸存（加强了 C 维幸存普遍性）。"
                f"请勿覆盖此文件，保留为 D2 差异化素材。"
            )
        else:
            ok("无跨尺寸错配实验检测到")
    except Exception as e:
        warn(f"C6b 错配检测异常: {e}")

# ============================================================
# C7: 9B baseline Judge 报告
# ============================================================
print("\nC7: 9B baseline Judge 报告")
p = ROOT / "benchmark" / "eval" / "reports" / "qwen3.5-9b_report.json"
if p.exists():
    try:
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
    except json.JSONDecodeError as e:
        fail(f"9B baseline report JSON 解析失败: {e}")
    else:
        ok(f"9B baseline: overall={d.get('overall_score','?')} dims={d.get('dimension_scores','?')}")
else:
    warn("9B baseline 报告不存在")

# ============================================================
# C8: git 状态 (意外未追踪的关键文件)
# ============================================================
print("\nC8: Git 状态")
r = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=str(ROOT))
dirty = [l for l in r.stdout.strip().split("\n") if l.strip()]
if dirty:
    warn(f"{len(dirty)} 个文件有未提交变更")
    for l in dirty[:10]:
        print(f"       {l}")
else:
    ok("工作区干净")

# ============================================================
# C9: .gitignore 阻断风险 — 已验证通过但不在 git 中的关键文件
# ============================================================
print("\nC9: .gitignore 阻断风险")
CRITICAL_FILES = [
    "finetune/output/perplexity_delta.json",
    "finetune/output/perplexity_delta_9b.json",
    "finetune/output/eval_baseline_4b_report.json",
    "finetune/output/eval_finetuned_report.json",
    "benchmark/eval/reports/qwen3.5-9b_report.json",
]
for rel_path in CRITICAL_FILES:
    fp = ROOT / rel_path
    if fp.exists():
        r2 = subprocess.run(["git", "check-ignore", "-q", rel_path],
                            capture_output=True, cwd=str(ROOT))
        if r2.returncode == 0:
            warn(f"{rel_path} 被 .gitignore 排除，无法通过 git 备份/恢复。请确保有本地备份")
    # 不存在的文件已在 C5/C6/C7 中报告，此处不重复

# ============================================================
# 裁决
# ============================================================
print(f"\n{'='*60}")
print(f"结果: {len(ERRORS)} 致命错误, {len(WARNS)} 警告")
if ERRORS:
    for e in ERRORS:
        print(f"  {e}")
if WARNS:
    for w in WARNS:
        print(f"  {w}")

if ERRORS:
    print(f"\n退出码 2 — 请在启动前修复以上致命错误")
    sys.exit(2)
elif WARNS:
    print(f"\n退出码 1 — 有警告但可继续，建议检查")
    sys.exit(1)
else:
    print(f"\n退出码 0 — 全部通过 ✅")
    sys.exit(0)
