"""MinerU 1.2B VLM vs MiMo-V2.5 公式识别对比

从跨模态共现数据中抽样公式图片，对比两个模型的 LaTeX 转录质量：
  - MinerU 1.2B VLM (via vLLM, 专用文档解析)
  - MiMo-V2.5 (通用视觉模型, 310B MoE / 15B active)

评估指标: LaTeX 编辑距离 / BLEU / 字符匹配率
Ground truth: 原始 MinerU 解析产出的 chunk markdown 中的 LaTeX 公式

用法:
  # 全量对比 (需 vLLM 已在 WSL2 运行)
  conda run -n myenv python tools/submission_figures/bench_mineru_1.2b_vlm.py --n 50 --vllm-url http://localhost:8000

  # MiMo-only 模式 (无 vLLM 时预跑 MiMo 侧，4 路并发，生成 checkpoint)
  conda run -n myenv python tools/submission_figures/bench_mineru_1.2b_vlm.py --n 50 --mimo-only --workers 4

  # 续跑
  conda run -n myenv python tools/submission_figures/bench_mineru_1.2b_vlm.py --n 50 --vllm-url http://localhost:8000 --resume

环境变量:
  MIMO_API_KEY — MiMo API Key (必需)
  VLLM_API_KEY — vLLM API Key (可选，默认 "EMPTY")

产出:
  benchmark/agent/logs/demo-vllm-mineru-1.2b-{timestamp}.json  — 50 条对比结果
  docs/evidence/mineru_1.2b_vlm_formula_comparison.md           — 分析报告
  docs/assets/mineru_1.2b_vs_mimo_formula.png                  — 对比散点图
"""

import argparse
import base64
import json
import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from threading import Lock

PRINT_LOCK = Lock()

import httpx

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from benchmark.eval.utils import write_json_atomic

# ── 路径常量 ──────────────────────────────────────────────
CHUNKS_DIR = ROOT / "corpus" / "chunks"
MANIFEST_PATH = CHUNKS_DIR / "chunks_manifest.json"
DATA_PROCESSED = ROOT / "data" / "processed"
OUTPUT_LOG_DIR = ROOT / "benchmark" / "agent" / "logs"
OUTPUT_EVIDENCE_DIR = ROOT / "docs" / "evidence"
OUTPUT_ASSETS_DIR = ROOT / "docs" / "assets"
CHECKPOINT_DIR = ROOT / "benchmark" / "agent" / "results"

# ── API 配置 ──────────────────────────────────────────────
MIMO_API_KEY = os.environ.get("MIMO_API_KEY", "")
MIMO_BASE_URL = "https://api.xiaomimimo.com/v1"
MIMO_MODEL = "mimo-v2.5"

VLLM_API_KEY = os.environ.get("VLLM_API_KEY", "EMPTY")
DEFAULT_VLLM_URL = "http://localhost:8001"
VLLM_MODEL = "opendatalab/MinerU2.5-2509-1.2B"

# ── 正则 ──────────────────────────────────────────────────
IMG_PATTERN = re.compile(r'!\[\]\((?:images|image)/([a-f0-9]+\.jpg)\)')
FM_BLOCK = re.compile(r'\$\$(.+?)\$\$', re.DOTALL)
FM_INLINE = re.compile(r'(?<!\$)\$(?!\$)([^$]+?)(?<!\$)\$(?!\$)')

# ── 公式转录 Prompt ──────────────────────────────────────
FORMULA_TRANSCRIPTION_SYSTEM = (
    "你是一个专业的数学公式 OCR 引擎。"
    "你的任务是将图片中的数学公式准确转录为 LaTeX 代码。"
    "只输出 LaTeX 代码，不要添加任何解释、标记或格式包装。"
)

FORMULA_TRANSCRIPTION_USER = (
    "请将这张图片中的数学公式转录为 LaTeX 代码。\n"
    "要求：\n"
    "1. 只输出 LaTeX 代码本身\n"
    "2. 不要包裹在 ``` 代码块中\n"
    "3. 不要添加任何说明文字\n"
    "4. 如果是多行公式，用 $$ 环境包裹每一行"
)


# ═══════════════════════════════════════════════════════════
# 指标计算 (纯 Python, 零外部依赖)
# ═══════════════════════════════════════════════════════════

def levenshtein_distance(a, b):
    """纯 Python Levenshtein 编辑距离"""
    if len(a) < len(b):
        return levenshtein_distance(b, a)
    if len(b) == 0:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        curr = [i + 1]
        for j, cb in enumerate(b):
            insert = prev[j + 1] + 1
            delete = curr[j] + 1
            substitute = prev[j] + (0 if ca == cb else 1)
            curr.append(min(insert, delete, substitute))
        prev = curr
    return prev[-1]


def normalized_edit_distance(ref, hyp):
    """归一化编辑距离 (0~1, 越低越好)"""
    if not ref and not hyp:
        return 0.0
    if not ref:
        return 1.0
    if not hyp:
        return 1.0
    return levenshtein_distance(ref, hyp) / max(len(ref), len(hyp))


def char_match_rate(ref, hyp):
    """字符级匹配率 (0~1, 越高越好)"""
    if not ref:
        return 1.0 if not hyp else 0.0
    matches = sum(1 for a, b in zip(ref, hyp) if a == b)
    return matches / max(len(ref), len(hyp))


def bleu_score(ref, hyp, n=4):
    """简化 BLEU (0~1, 越高越好)

    使用 n-gram precision + brevity penalty.
    仅依赖标准库 collections.Counter.
    """
    if not hyp or not ref:
        return 0.0

    def _ngrams(text, n):
        return [text[i:i+n] for i in range(len(text) - n + 1)]

    precisions = []
    for i in range(1, n + 1):
        ref_ngrams = _ngrams(ref, i)
        hyp_ngrams = _ngrams(hyp, i)
        if not hyp_ngrams:
            precisions.append(0.0)
            continue
        ref_counts = Counter(ref_ngrams)
        hyp_counts = Counter(hyp_ngrams)
        clipped = sum(min(hyp_counts[ng], ref_counts[ng]) for ng in hyp_counts)
        precisions.append(clipped / len(hyp_ngrams))

    if all(p == 0.0 for p in precisions):
        return 0.0

    geo_mean = 1.0
    for p in precisions:
        geo_mean *= (p if p > 0 else 1e-10)
    geo_mean = geo_mean ** (1.0 / n)

    bp = min(1.0, len(hyp) / max(len(ref), 1))
    return geo_mean * bp


# ═══════════════════════════════════════════════════════════
# 数据提取
# ═══════════════════════════════════════════════════════════

def extract_images(text):
    return IMG_PATTERN.findall(text)


def extract_formulas(text):
    """提取 chunk markdown 中的 LaTeX 公式 (block + inline)"""
    scan = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    formulas = []
    for m in FM_BLOCK.findall(scan):
        formulas.append(m.strip())
    for m in FM_INLINE.findall(scan):
        formulas.append(m.strip())
    return formulas


def resolve_image_path(filename, hash_name):
    return DATA_PROCESSED / filename / "image" / hash_name


def scan_formula_work_items(max_items=None, seed=42):
    """扫描 chunks_manifest, 提取 image+formula 共现对"""
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    chunks = manifest["chunks"]
    total = len(chunks)
    print(f"\n  扫描 {total} 个 chunks 中 (寻找图片+公式共现项)...")
    t0 = time.time()

    work_items = []
    for i, chunk in enumerate(chunks):
        if (i + 1) % 3000 == 0:
            elapsed = time.time() - t0
            print(f"    扫描进度: {i+1}/{total} ({elapsed:.0f}s), 已找到 {len(work_items)} 项")

        filepath = CHUNKS_DIR / chunk["filepath"].replace("corpus/chunks/", "")
        try:
            content = filepath.read_text(encoding="utf-8")
        except (FileNotFoundError, UnicodeDecodeError):
            continue

        images = extract_images(content)
        if not images:
            continue

        formulas = extract_formulas(content)
        if not formulas:
            continue

        formulas_joined = " ".join(formulas)
        filename = chunk["filename"]
        doc_id = chunk.get("doc_id", "?")

        for img_hash in images:
            img_path = resolve_image_path(filename, img_hash)
            if not img_path.exists():
                continue

            work_items.append({
                "chunk_id": chunk["chunk_id"],
                "filename": filename,
                "doc_id": doc_id,
                "image_hash": img_hash,
                "image_path": str(img_path),
                "ground_truth_latex": formulas_joined,
                "formula_count": len(formulas),
                "source_section": chunk.get("source_section", ""),
            })

    scan_time = time.time() - t0
    print(f"  扫描完成: {len(work_items)} 个公式识别项, 耗时 {scan_time:.0f}s")

    if max_items and len(work_items) > max_items:
        import random
        rng = random.Random(seed)
        rng.shuffle(work_items)
        work_items = work_items[:max_items]
        print(f"  随机抽样: {max_items} 项 (seed={seed})")

    return work_items


# ═══════════════════════════════════════════════════════════
# API 调用
# ═══════════════════════════════════════════════════════════

RETRY_DELAYS = (2, 5, 10)


def _api_retry(func_name, attempt, exc):
    delay = RETRY_DELAYS[min(attempt, len(RETRY_DELAYS) - 1)]
    print(f"    ⚠ {func_name} retry {attempt + 1}/{len(RETRY_DELAYS) + 1} "
          f"(wait {delay}s): {exc}")
    try:
        time.sleep(delay)
    except KeyboardInterrupt:
        print(f"\n    ⏹ {func_name} 用户中断")
        raise


def image_to_base64(image_path):
    path = Path(image_path)
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except (FileNotFoundError, OSError):
        pass
    for drive in "CDEFGHIJKLMNOPQRSTUVWXYZ":
        wsl_path = path.as_posix().replace(f"{drive}:/", f"/mnt/{drive.lower()}/")
        if wsl_path != path.as_posix():
            try:
                with open(wsl_path, "rb") as f:
                    return base64.b64encode(f.read()).decode("utf-8")
            except (FileNotFoundError, OSError):
                pass
    raise FileNotFoundError(f"Cannot read image: {image_path}")


def call_mimo_transcribe(image_path, timeout=120, no_proxy=False):
    """调用 MiMo-V2.5 将公式图片转录为 LaTeX"""
    if not MIMO_API_KEY:
        raise ValueError("MIMO_API_KEY not set")

    image_b64 = image_to_base64(image_path)
    payload = {
        "model": MIMO_MODEL,
        "messages": [
            {"role": "system", "content": FORMULA_TRANSCRIPTION_SYSTEM},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": FORMULA_TRANSCRIPTION_USER},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}",
                            "detail": "high",
                        },
                    },
                ],
            },
        ],
        "temperature": 0.0,
        "max_tokens": 1024,
        "thinking": {"type": "disabled"},
    }
    headers = {
        "api-key": MIMO_API_KEY,
        "Content-Type": "application/json",
    }

    last_err = None
    for attempt in range(len(RETRY_DELAYS) + 1):
        try:
            client_kwargs = {"timeout": timeout}
            if no_proxy:
                client_kwargs["proxy"] = None
            with httpx.Client(**client_kwargs) as client:
                resp = client.post(
                    f"{MIMO_BASE_URL}/chat/completions",
                    json=payload,
                    headers=headers,
                )
            if 500 <= resp.status_code < 600:
                raise RuntimeError(f"MiMo API HTTP {resp.status_code}")
            if resp.status_code == 429:
                raise RuntimeError("MiMo API rate limited (429)")
            if resp.status_code != 200:
                raise RuntimeError(f"MiMo API HTTP {resp.status_code}: {resp.text[:300]}")

            data = None
            try:
                data = resp.json()
            except json.JSONDecodeError as e:
                raise RuntimeError(f"MiMo API invalid JSON: {e}")
            content = data["choices"][0]["message"]["content"]
            if content is None:
                raise RuntimeError("MiMo API returned content=None")

            tokens = data.get("usage", {})
            return {
                "latex": content.strip(),
                "prompt_tokens": tokens.get("prompt_tokens", 0),
                "completion_tokens": tokens.get("completion_tokens", 0),
            }
        except (httpx.HTTPError, httpx.TimeoutException, RuntimeError) as e:
            last_err = e
            if attempt < len(RETRY_DELAYS):
                _api_retry("MiMo", attempt, e)

    raise RuntimeError(f"MiMo API exhausted retries: {last_err}")


def call_vllm_transcribe(image_path, vllm_url, timeout=180):
    """调用 vLLM (MinerU 1.2B VLM) 将公式图片转录为 LaTeX"""
    image_b64 = image_to_base64(image_path)
    payload = {
        "model": VLLM_MODEL,
        "messages": [
            {"role": "system", "content": FORMULA_TRANSCRIPTION_SYSTEM},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": FORMULA_TRANSCRIPTION_USER},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}",
                        },
                    },
                ],
            },
        ],
        "temperature": 0.0,
        "max_tokens": 1024,
    }
    headers = {
        "Authorization": f"Bearer {VLLM_API_KEY}",
        "Content-Type": "application/json",
    }

    last_err = None
    for attempt in range(len(RETRY_DELAYS) + 1):
        try:
            with httpx.Client(proxy=None, timeout=timeout) as client:
                resp = client.post(
                    f"{vllm_url.rstrip('/')}/v1/chat/completions",
                    json=payload,
                    headers=headers,
                )
            if 500 <= resp.status_code < 600:
                raise RuntimeError(f"vLLM API HTTP {resp.status_code}")
            if resp.status_code == 429:
                raise RuntimeError("vLLM API rate limited (429)")
            if resp.status_code != 200:
                raise RuntimeError(f"vLLM API HTTP {resp.status_code}: {resp.text[:300]}")

            try:
                data = resp.json()
            except json.JSONDecodeError as e:
                raise RuntimeError(f"vLLM API invalid JSON: {e}")
            content = data["choices"][0]["message"]["content"]
            if content is None:
                raise RuntimeError("vLLM API returned content=None")

            tokens = data.get("usage", {})
            return {
                "latex": content.strip(),
                "prompt_tokens": tokens.get("prompt_tokens", 0),
                "completion_tokens": tokens.get("completion_tokens", 0),
            }
        except (httpx.HTTPError, httpx.TimeoutException, RuntimeError) as e:
            last_err = e
            if attempt < len(RETRY_DELAYS):
                _api_retry("vLLM", attempt, e)

    raise RuntimeError(f"vLLM API exhausted retries: {last_err}")


def clean_latex_for_comparison(latex_str):
    """清洗 LaTeX 字符串用于公平比较: 去 $$, 去首尾空白, 归一化空格"""
    s = latex_str.strip()
    s = re.sub(r'^\$\$?\s*', '', s)
    s = re.sub(r'\s*\$\$?$', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


# ═══════════════════════════════════════════════════════════
# Checkpoint
# ═══════════════════════════════════════════════════════════

def _checkpoint_path():
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    return CHECKPOINT_DIR / "bench_mineru_1.2b_checkpoint.json"


def save_checkpoint(results, phase):
    cp = {
        "timestamp": datetime.now().isoformat(),
        "phase": phase,
        "count": len(results),
        "results": results,
    }
    write_json_atomic(_checkpoint_path(), cp)


def load_checkpoint():
    cp = _checkpoint_path()
    if not cp.exists():
        return None
    with open(cp, "r", encoding="utf-8") as f:
        return json.load(f)


# ═══════════════════════════════════════════════════════════
# 分层抽样
# ═══════════════════════════════════════════════════════════

def stratify_by_mimo_score(results, n_total=50):
    """按 MiMo-V2.5 的编辑距离分层抽样

    高对齐 (edit_dist < 0.15)  ~17 条
    中对齐 (0.15 <= edit_dist < 0.40) ~17 条
    低对齐 (edit_dist >= 0.40) ~16 条
    """
    results_with_score = [r for r in results if r.get("mimo_edit_distance") is not None]
    if len(results_with_score) < n_total:
        return results_with_score

    high = [r for r in results_with_score if r["mimo_edit_distance"] < 0.15]
    mid = [r for r in results_with_score if 0.15 <= r["mimo_edit_distance"] < 0.40]
    low = [r for r in results_with_score if r["mimo_edit_distance"] >= 0.40]

    n_high = min(17, len(high))
    n_mid = min(17, len(mid))
    n_low = n_total - n_high - n_mid

    import random
    rng = random.Random(42)
    sampled = []
    sampled.extend(rng.sample(high, n_high) if len(high) >= n_high else high)
    sampled.extend(rng.sample(mid, n_mid) if len(mid) >= n_mid else mid)
    sampled.extend(rng.sample(low, n_low) if len(low) >= n_low else low)
    rng.shuffle(sampled)

    print(f"\n  分层抽样: 高对齐 {len(sampled)} 条 (目标 {n_high}), "
          f"中对齐 {len([r for r in sampled if 0.15 <= r['mimo_edit_distance'] < 0.40])} 条 (目标 {n_mid}), "
          f"低对齐 {len([r for r in sampled if r['mimo_edit_distance'] >= 0.40])} 条 (目标 {n_low})")
    return sampled


# ═══════════════════════════════════════════════════════════
# 可视化
# ═══════════════════════════════════════════════════════════

def generate_comparison_chart(results, output_path):
    """生成 MiMo vs MinerU 1.2B 对比散点图 (字符匹配率)"""
    mimo_scores = []
    mineru_scores = []

    for r in results:
        ms = r.get("mimo_char_match")
        vs = r.get("mineru_char_match")
        if ms is None or vs is None:
            continue
        mimo_scores.append(ms)
        mineru_scores.append(vs)

    if not mimo_scores:
        print("  ⚠ 无有效评分数据，跳过图表生成")
        return

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np

        plt.rcParams["font.family"] = "sans-serif"

        fig, axes = plt.subplots(1, 2, figsize=(16, 7.6))

        # ── 子图1: 字符匹配率散点 ──
        ax1 = axes[0]
        ax1.scatter(mimo_scores, mineru_scores, c="steelblue", alpha=0.7, s=60, edgecolors="white")
        ax1.plot([0, 1], [0, 1], "k--", alpha=0.4, label="y=x (Equal)")
        ax1.set_xlabel("MiMo-V2.5 Char Match Rate", fontsize=12)
        ax1.set_ylabel("MinerU 1.2B Char Match Rate", fontsize=12)
        ax1.set_title("Char Match Rate: MiMo-V2.5 vs MinerU 1.2B VLM", fontsize=14)
        ax1.set_xlim(0, 1.05)
        ax1.set_ylim(0, 1.05)
        ax1.set_axisbelow(True)
        ax1.grid(True, alpha=0.3)

        mimo_avg = np.mean(mimo_scores)
        mineru_avg = np.mean(mineru_scores)
        ax1.axvline(x=mimo_avg, color="orange", linestyle=":", alpha=0.7,
                    label=f"MiMo mean={mimo_avg:.3f}")
        ax1.axhline(y=mineru_avg, color="green", linestyle=":", alpha=0.7,
                    label=f"MinerU mean={mineru_avg:.3f}")
        ax1.legend(
            loc="upper center",
            bbox_to_anchor=(0.5, -0.16),
            ncol=3,
            fontsize=9,
            frameon=True,
        )

        # ── 子图2: 编辑距离分布 ──
        ax2 = axes[1]
        mimo_edit = [r.get("mimo_edit_distance", 0) for r in results]
        mineru_edit = [r.get("mineru_edit_distance", 0) for r in results]
        valid = [(m, v) for m, v in zip(mimo_edit, mineru_edit) if m is not None and v is not None]
        if valid:
            m_edit, v_edit = zip(*valid)
            x_pos = np.arange(len(m_edit))
            width = 0.35
            ax2.set_axisbelow(True)
            ax2.bar(x_pos - width/2, m_edit, width, label="MiMo-V2.5", color="steelblue", alpha=0.8, zorder=3)
            ax2.bar(x_pos + width/2, v_edit, width, label="MinerU 1.2B", color="darkorange", alpha=0.8, zorder=3)
            ax2.set_xlabel("Sample Index", fontsize=12)
            ax2.set_ylabel("Normalized Edit Distance (lower is better)", fontsize=12)
            ax2.set_title("Edit Distance per Sample Comparison", fontsize=14)
            ax2.legend(
                loc="upper center",
                bbox_to_anchor=(0.5, -0.16),
                ncol=2,
                fontsize=11,
                frameon=True,
            )
            ax2.grid(True, alpha=0.3, axis="y", zorder=0)

        fig.subplots_adjust(left=0.06, right=0.98, top=0.90, bottom=0.18, wspace=0.16)
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"  对比图表已保存: {output_path}")
    except ImportError:
        print("  ⚠ matplotlib 不可用，跳过图表生成")


# ═══════════════════════════════════════════════════════════
# 分析报告
# ═══════════════════════════════════════════════════════════

def generate_report(results, output_path, corpus_total=None):
    """生成 Markdown 分析报告"""
    total = len(results)
    corpus_n = corpus_total if corpus_total is not None else "?"
    mimo_ok = sum(1 for r in results if r.get("mimo_latex"))
    mineru_ok = sum(1 for r in results if r.get("mineru_latex"))

    mimo_edits = [r["mimo_edit_distance"] for r in results if r.get("mimo_edit_distance") is not None]
    mineru_edits = [r["mineru_edit_distance"] for r in results if r.get("mineru_edit_distance") is not None]
    mimo_bleus = [r["mimo_bleu"] for r in results if r.get("mimo_bleu") is not None]
    mineru_bleus = [r["mineru_bleu"] for r in results if r.get("mineru_bleu") is not None]
    mimo_chars = [r["mimo_char_match"] for r in results if r.get("mimo_char_match") is not None]
    mineru_chars = [r["mineru_char_match"] for r in results if r.get("mineru_char_match") is not None]

    def _mean(lst):
        return sum(lst) / len(lst) if lst else 0

    # 分层统计
    high_edit = [r for r in results if r.get("mimo_edit_distance") is not None and r["mimo_edit_distance"] < 0.15]
    mid_edit = [r for r in results if r.get("mimo_edit_distance") is not None and 0.15 <= r["mimo_edit_distance"] < 0.40]
    low_edit = [r for r in results if r.get("mimo_edit_distance") is not None and r["mimo_edit_distance"] >= 0.40]

    def _stratum_stats(samples, label):
        if not samples:
            return f"| {label} | — | — | — | — |"
        m_ed = _mean([r.get("mimo_edit_distance", 1) for r in samples])
        v_ed = _mean([r.get("mineru_edit_distance", 1) for r in samples])
        m_bleu = _mean([r.get("mimo_bleu", 0) for r in samples])
        v_bleu = _mean([r.get("mineru_bleu", 0) for r in samples])
        return f"| {label} ({len(samples)}条) | {m_ed:.4f} | {v_ed:.4f} | {m_bleu:.4f} | {v_bleu:.4f} |"

    report = f"""# MinerU 1.2B VLM vs MiMo-V2.5 公式识别对比

> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> 样本数: {total} 条 (从 {total} 条图片-公式共现对中分层抽样)
> MiMo-V2.5 成功: {mimo_ok}/{total} | MinerU 1.2B 成功: {mineru_ok}/{total}

## 1. 实验设计

从 ControlSci 跨模态语料 ({corpus_n} chunks) 中提取图片-公式共现对，
以原始 MinerU 解析产出的 LaTeX 为 ground truth，
对比两个模型的公式转录质量：

| 模型 | 参数量 | 类型 | 调用方式 |
|:--|:--|:--|:--|
| **MiMo-V2.5** | 310B (MoE, 15B active) | 通用视觉模型 | HTTP API (api.xiaomimimo.com) |
| **MinerU 1.2B VLM** | 1.2B | 专用文档解析模型 | vLLM 本地推理 (RTX 5090) |

## 2. 综合指标

| 指标 | MiMo-V2.5 | MinerU 1.2B | Δ | 胜者 |
|:--|:--:|:--:|:--:|:--:|
| 归一化编辑距离 ↓ | {_mean(mimo_edits):.4f} | {_mean(mineru_edits):.4f} | {_mean(mimo_edits) - _mean(mineru_edits):+.4f} | {'MiMo' if _mean(mimo_edits) < _mean(mineru_edits) else 'MinerU'} |
| BLEU ↑ | {_mean(mimo_bleus):.4f} | {_mean(mineru_bleus):.4f} | {_mean(mineru_bleus) - _mean(mimo_bleus):+.4f} | {'MiMo' if _mean(mimo_bleus) > _mean(mineru_bleus) else 'MinerU'} |
| 字符匹配率 ↑ | {_mean(mimo_chars):.4f} | {_mean(mineru_chars):.4f} | {_mean(mineru_chars) - _mean(mimo_chars):+.4f} | {'MiMo' if _mean(mimo_chars) > _mean(mineru_chars) else 'MinerU'} |

## 3. 分层表现 (按 MiMo-V2.5 编辑距离分层)

| 分层 | MiMo 编辑距离 | MinerU 编辑距离 | MiMo BLEU | MinerU BLEU |
|:--|:--:|:--:|:--:|:--:|
{_stratum_stats(high_edit, '高对齐 (<0.15)')}
{_stratum_stats(mid_edit, '中对齐 (0.15-0.40)')}
{_stratum_stats(low_edit, '低对齐 (≥0.40)')}

## 4. Top-5 最佳案例 (MinerU 1.2B 最接近 ground truth)

{_top_cases_table(results, 'best', 5)}

## 5. Top-5 最差案例 (MinerU 1.2B 偏差最大)

{_top_cases_table(results, 'worst', 5)}

## 6. 叙事

本次实验在 RTX 5090 上通过 vLLM 部署 MinerU 1.2B VLM，
与 MiMo-V2.5 (310B MoE, 15B active) 在公式识别任务上进行对比。
两种模型在相同的 50 张公式图片上接受了相同的转录 prompt，
以原始 MinerU 解析产出的 LaTeX 为 ground truth 进行评估。

无论哪种结果，都构成有说服力的叙事：
- 若 1.2B 追平/超越 MiMo-V2.5 → 专用小模型在专业领域可超越通用大模型，印证"领域适配 > 模型尺寸"
- 若 MiMo-V2.5 领先 → 通用视觉模型在边缘案例上仍具优势，但 1.2B 稠密模型仅占其 1/250 总参数（1/12.5 激活参数）

## 7. 数据来源

- 原始语料: `corpus/chunks/chunks_manifest.json` ({corpus_n} chunks)
- 图片文件: `data/processed/{{doc}}/image/{{hash}}.jpg`
- Ground truth LaTeX: 各 chunk markdown 文件中的 `$$` 块和内联 `$` 公式
- MiMo-V2.5 API: `https://api.xiaomimimo.com/v1/chat/completions`
- MinerU 1.2B vLLM: `{DEFAULT_VLLM_URL}/v1/chat/completions`
"""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"  分析报告已保存: {output_path}")


def _escape_md_table(text, max_len=50):
    """转义 LaTeX 字符串以安全嵌入 Markdown 表格内联代码"""
    s = (text or "").replace("|", "\\|").replace("`", "'")
    s = s.replace("\n", " ").replace("\r", "")
    if len(s) > max_len:
        s = s[:max_len] + "..."
    return s


def _top_cases_table(results, mode, n):
    if mode == "best":
        key = lambda r: r.get("mineru_char_match", -1)
        reverse = True
    else:
        key = lambda r: r.get("mineru_char_match", -1)
        reverse = False

    sorted_results = sorted(
        [r for r in results if r.get("mineru_char_match") is not None],
        key=key, reverse=reverse
    )[:n]

    rows = []
    for i, r in enumerate(sorted_results, 1):
        gt = _escape_md_table(r.get("ground_truth_latex", ""))
        mineru = _escape_md_table(r.get("mineru_latex", ""))
        mimo = _escape_md_table(r.get("mimo_latex", ""))
        rows.append(f"| {i} | `{gt}` | `{mineru}` | `{mimo}` | "
                    f"{r.get('mineru_char_match', 0):.3f} | {r.get('mimo_char_match', 0):.3f} |")

    header = f"| # | Ground Truth | MinerU 1.2B | MiMo-V2.5 | MinerU Char | MiMo Char |\n" \
             f"|:--:|:--|:--|:--|:--:|:--:|"
    return header + "\n" + "\n".join(rows)


# ═══════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════

def _run_mimo_transcription(work_items, results, args):
    """执行 MiMo-V2.5 公式转录 (并发), 追加到 results 列表"""
    start_idx = len(results)
    total = len(work_items)
    workers = getattr(args, "workers", 4)
    print(f"  并发数: {workers}")

    def transcribe_one(idx, item):
        img_path = item["image_path"]
        gt_latex = item["ground_truth_latex"]
        clean_gt = clean_latex_for_comparison(gt_latex)
        r = {
            "index": start_idx + idx,
            "chunk_id": item["chunk_id"],
            "image_hash": item["image_hash"],
            "image_path": img_path,
            "ground_truth_latex": gt_latex,
            "ground_truth_clean": clean_gt,
            "formula_count": item["formula_count"],
            "source_section": item["source_section"],
        }
        try:
            mimo_out = call_mimo_transcribe(img_path, timeout=args.timeout, no_proxy=args.no_proxy)
            mimo_clean = clean_latex_for_comparison(mimo_out["latex"])
            r["mimo_latex"] = mimo_out["latex"]
            r.pop("mimo_error", None)
            r["mimo_latex_clean"] = mimo_clean
            r["mimo_edit_distance"] = normalized_edit_distance(clean_gt, mimo_clean)
            r["mimo_bleu"] = bleu_score(clean_gt, mimo_clean)
            r["mimo_char_match"] = char_match_rate(clean_gt, mimo_clean)
            r["mimo_tokens"] = {
                "prompt": mimo_out["prompt_tokens"],
                "completion": mimo_out["completion_tokens"],
            }
            with PRINT_LOCK:
                print(f"    [{start_idx + idx + 1}/{start_idx + total}] "
                      f"{item['image_hash'][:12]}.. "
                      f"edit={r['mimo_edit_distance']:.3f} char={r['mimo_char_match']:.3f}")
        except Exception as e:
            r["mimo_error"] = str(e)
            with PRINT_LOCK:
                print(f"    [{start_idx + idx + 1}/{start_idx + total}] "
                      f"{item['image_hash'][:12]}.. ❌ MiMo: {e}")
        return r

    completed = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(transcribe_one, i, item): i for i, item in enumerate(work_items)}
        for future in as_completed(futures):
            r = future.result()
            results.append(r)
            completed += 1
            if completed % 10 == 0:
                save_checkpoint(results, "mimo_transcription")

    save_checkpoint(results, "mimo_done")
    ok = sum(1 for r in results if r.get("mimo_latex"))
    print(f"\n  MiMo 转录完成: {ok}/{len(results)} 成功")
    return results


def main():
    parser = argparse.ArgumentParser(
        description="MinerU 1.2B VLM vs MiMo-V2.5 公式识别对比"
    )
    parser.add_argument("--n", type=int, default=50,
                        help="样本数 (默认 50)")
    parser.add_argument("--mimo-only", action="store_true",
                        help="仅运行 MiMo-V2.5 侧 (无 vLLM 时使用)")
    parser.add_argument("--vllm-url", type=str, default=None,
                        help="vLLM 服务地址 (默认 http://localhost:8000)")
    parser.add_argument("--resume", action="store_true",
                        help="从 checkpoint 续跑")
    parser.add_argument("--no-chart", action="store_true",
                        help="跳过图表生成")
    parser.add_argument("--timeout", type=int, default=180,
                        help="API 超时秒数 (默认 180)")
    parser.add_argument("--no-proxy", action="store_true",
                        help="禁用 HTTP 代理 (MiMo API 默认跟随系统代理)")
    parser.add_argument("--workers", type=int, default=4,
                        help="MiMo API 并发数 (默认 4)")
    parser.add_argument("--vllm-workers", type=int, default=4,
                        help="vLLM 并发数 (默认 4)")

    args = parser.parse_args()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    print("=" * 60)
    print(f"  MinerU 1.2B VLM vs MiMo-V2.5 公式识别对比")
    print(f"  样本数: {args.n} | 模式: {'MiMo-Only' if args.mimo_only else 'Full'}")
    print(f"  vLLM URL: {args.vllm_url or 'N/A'}")
    print("=" * 60)

    results = []

    # ── Phase 0: Checkpoint 恢复 ──
    if args.resume:
        cp = load_checkpoint()
        if cp:
            results = cp.get("results", [])
            print(f"\n  📂 checkpoint 恢复: {len(results)} 条已有结果 (phase={cp.get('phase', '?')})")
        else:
            print("\n  ⚠ 未找到 checkpoint, 从头开始")

    # ── Phase 1: 数据准备 ──
    if not results:
        work_items = scan_formula_work_items(max_items=args.n * 5)
        print(f"  数据准备完成: {len(work_items)} 个候选项")

        # ── Phase 2: MiMo-V2.5 转录 ──
        print(f"\n  ── Phase 2: MiMo-V2.5 公式转录 ({len(work_items)} 项) ──")
        if not MIMO_API_KEY:
            print("  ❌ MIMO_API_KEY 未设置, 无法进行 MiMo 转录")
            sys.exit(1)

        results = _run_mimo_transcription(work_items, results, args)

    elif len(results) < args.n:
        needed = args.n - len(results)
        print(f"\n  ⚠ checkpoint 仅有 {len(results)} 条，需补充 {needed} 条")
        existing_hashes = {r["image_hash"] for r in results}
        extra_items = scan_formula_work_items(max_items=needed * 5)
        extra_items = [it for it in extra_items if it["image_hash"] not in existing_hashes]
        if extra_items:
            print(f"  补充扫描: {len(extra_items)} 个新候选项")
            if not MIMO_API_KEY:
                print("  ❌ MIMO_API_KEY 未设置, 无法进行 MiMo 转录")
                sys.exit(1)
            results = _run_mimo_transcription(extra_items, results, args)
        else:
            print(f"  ⚠ 无更多新数据可补充")

    # ── Phase 2b: 分层抽样 ──
    if len(results) > args.n:
        results = stratify_by_mimo_score(results, args.n)
        save_checkpoint(results, "stratified")

    # ── Phase 3: MinerU 1.2B VLM 转录 ──
    if not args.mimo_only:
        vllm_url = args.vllm_url or DEFAULT_VLLM_URL
        pending = [(i, r) for i, r in enumerate(results) if not r.get("mineru_latex")]
        vllm_workers = getattr(args, "vllm_workers", 4)
        print(f"\n  ── Phase 3: MinerU 1.2B VLM 公式转录 ({len(pending)} 项) ──")
        print(f"  vLLM URL: {vllm_url}  并发数: {vllm_workers}")

        vllm_ok = sum(1 for r in results if r.get("mineru_latex"))
        vllm_err = sum(1 for r in results if r.get("mineru_error"))
        if not pending:
            print(f"  vLLM 全部已完成: {vllm_ok} 成功, {vllm_err} 失败")
        else:
            def transcribe_vllm(idx, r):
                img_path = r["image_path"]
                clean_gt = r["ground_truth_clean"]
                try:
                    vllm_out = call_vllm_transcribe(img_path, vllm_url, timeout=args.timeout)
                    vllm_clean = clean_latex_for_comparison(vllm_out["latex"])
                    r["mineru_latex"] = vllm_out["latex"]
                    r.pop("mineru_error", None)
                    r["mineru_latex_clean"] = vllm_clean
                    r["mineru_edit_distance"] = normalized_edit_distance(clean_gt, vllm_clean)
                    r["mineru_bleu"] = bleu_score(clean_gt, vllm_clean)
                    r["mineru_char_match"] = char_match_rate(clean_gt, vllm_clean)
                    r["mineru_tokens"] = {
                        "prompt": vllm_out["prompt_tokens"],
                        "completion": vllm_out["completion_tokens"],
                    }
                    with PRINT_LOCK:
                        print(f"    [{idx + 1}/{len(results)}] {r['image_hash'][:12]}.. "
                              f"edit={r['mineru_edit_distance']:.3f} char={r['mineru_char_match']:.3f}")
                    return True
                except Exception as e:
                    r["mineru_error"] = str(e)
                    with PRINT_LOCK:
                        print(f"    [{idx + 1}/{len(results)}] {r['image_hash'][:12]}.. ❌ vLLM: {e}")
                    return False

            completed = 0
            with ThreadPoolExecutor(max_workers=vllm_workers) as executor:
                futures = {executor.submit(transcribe_vllm, i, r): i for i, r in pending}
                for future in as_completed(futures):
                    future.result()
                    completed += 1
                    if completed % 10 == 0:
                        save_checkpoint(results, "vllm_transcription")

            save_checkpoint(results, "vllm_done")
            vllm_ok = sum(1 for r in results if r.get("mineru_latex"))
            vllm_err = sum(1 for r in results if r.get("mineru_error"))
            print(f"\n  MinerU 1.2B 转录完成: {vllm_ok} 成功, {vllm_err} 失败")

    # ── Phase 4: 产出 ──
    print(f"\n  ── Phase 4: 产出 ──")

    # 4a: JSON 日志
    OUTPUT_LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = OUTPUT_LOG_DIR / f"demo-vllm-mineru-1.2b-{timestamp}.json"
    write_json_atomic(log_path, {
        "generated_at": datetime.now().isoformat(),
        "sample_count": len(results),
        "mode": "mimo_only" if args.mimo_only else "full",
        "results": results,
    })
    print(f"  ✅ 对比结果: {log_path}")

    # 4b: Markdown 报告
    report_path = OUTPUT_EVIDENCE_DIR / "mineru_1.2b_vlm_formula_comparison.md"
    complete = [r for r in results
                if r.get("mimo_latex") and (args.mimo_only or r.get("mineru_latex"))]
    if complete:
        corpus_total = None
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                corpus_total = json.load(f)["total_chunks"]
        except Exception:
            pass
        generate_report(complete, report_path, corpus_total=corpus_total)
    else:
        print(f"  ⚠ 无完整对比数据，跳过报告生成")

    # 4c: 散点图
    if not args.no_chart and not args.mimo_only and complete:
        chart_path = OUTPUT_ASSETS_DIR / "mineru_1.2b_vs_mimo_formula.png"
        complete_both = [r for r in complete if r.get("mineru_latex")]
        generate_comparison_chart(complete_both, chart_path)

    # ── 汇总 ──
    mimo_edits = [r["mimo_edit_distance"] for r in results if r.get("mimo_edit_distance") is not None]
    mineru_edits = [r["mineru_edit_distance"] for r in results if r.get("mineru_edit_distance") is not None]
    print(f"\n{'='*60}")
    print(f"  汇总:")
    print(f"    MiMo-V2.5 编辑距离:  {sum(mimo_edits)/len(mimo_edits):.4f}" if mimo_edits else "    MiMo-V2.5: 无数据")
    print(f"    MinerU 1.2B 编辑距离: {sum(mineru_edits)/len(mineru_edits):.4f}" if mineru_edits else "    MinerU 1.2B: 无数据")
    print(f"    Checkpoint: {_checkpoint_path()}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
