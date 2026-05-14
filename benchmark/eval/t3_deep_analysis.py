"""
T3: 深度分析扩展 — A6~A9
A6: 评分分布 (Score Distribution) — 分布形状/偏度/峰度/双峰检测
A7: 维度 κ (Dimension Agreement) — Kendall's W / ICC / 维度间一致性矩阵
A8: 难度矩阵 (Difficulty Matrix) — 模型×难度热力图/题目难度分析/衰退模式
A9: 长度偏见 (Length Bias) — model_answer 长度与评分相关性

Produce:
  - 7 PNG charts in results/analysis/
  - 4 JSON result files
  - Comprehensive Markdown section in t3_deep_analysis.md
"""

import sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmark.eval.utils import load_json, iter_report_files

import numpy as np
from scipy import stats
from scipy.stats import kurtosis, skew, pearsonr, spearmanr, chi2_contingency

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

CORE_9 = [
    "mimo-v2-flash", "deepseek-v4-flash", "qwen3.5:9b",
    "deepseek-v4-pro", "minimax-m2.5", "minimax-m2.7",
    "mimo-v2.5-pro", "mimo-v2-pro", "mimo-v2.5",
]

_MODEL_ALIASES = {
    "MiniMax-M2.5-highspeed": "minimax-m2.5",
    "MiniMax-M2.7-highspeed": "minimax-m2.7",
}

MODEL_SHORT = {
    "mimo-v2-flash": "MiMo-v2-flash", "deepseek-v4-flash": "DS-v4-flash",
    "qwen3.5:9b": "Qwen3.5:9b", "deepseek-v4-pro": "DS-v4-pro",
    "minimax-m2.5": "MM-m2.5", "minimax-m2.7": "MM-m2.7",
    "mimo-v2.5-pro": "MiMo-v2.5-pro", "mimo-v2-pro": "MiMo-v2-pro",
    "mimo-v2.5": "MiMo-v2.5",
}

MODEL_FAMILY = {
    "mimo-v2-flash": "MiMo", "deepseek-v4-flash": "DeepSeek",
    "qwen3.5:9b": "Qwen", "deepseek-v4-pro": "DeepSeek",
    "minimax-m2.5": "MiniMax", "minimax-m2.7": "MiniMax",
    "mimo-v2.5-pro": "MiMo", "mimo-v2-pro": "MiMo", "mimo-v2.5": "MiMo",
}

FAMILY_COLORS = {"MiMo": "#1f77b4", "DeepSeek": "#ff7f0e", "Qwen": "#2ca02c", "MiniMax": "#d62728"}
DIMENSIONS = ["A", "B", "C", "D"]
DIFFICULTIES = ["L1", "L2", "L3", "L4"]
OUTPUT_DIR = ROOT / "benchmark" / "eval" / "results" / "analysis"

RNG = np.random.RandomState(42)


# ═══════════════════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════════════════

def load_core_9(reports_dir=None):
    if reports_dir is None:
        reports_dir = ROOT / "benchmark" / "eval" / "reports"
    reports_dir = Path(reports_dir)
    data = {}
    for jf in iter_report_files(reports_dir):
        try:
            d = load_json(jf)
            model_raw = d.get("model", "")
            model = _MODEL_ALIASES.get(model_raw, model_raw)
            if model in CORE_9 and d.get("total_questions", 0) >= 400:
                data[model] = d
        except Exception:
            pass
    missing = set(CORE_9) - set(data.keys())
    if missing:
        print(f"  缺失模型报告: {missing}")
    return data


def extract_records(data):
    all_scores = {}
    all_lengths = {}
    all_records = {}
    by_dim = {m: {d: [] for d in DIMENSIONS} for m in data}
    by_diff = {m: {lvl: [] for lvl in DIFFICULTIES} for m in data}
    length_by_dim = {m: {d: [] for d in DIMENSIONS} for m in data}
    dimension_means = {}

    for model, d in data.items():
        scores = []
        lengths = []
        recs_raw = []
        for rec in d.get("records", []):
            dim = rec.get("dimension", "")
            lvl = rec.get("difficulty_level", "")
            sc = rec.get("score", 0.0)
            ma = rec.get("model_answer", "")
            scores.append(sc)
            lengths.append(len(ma))
            recs_raw.append(rec)
            if dim in by_dim[model]:
                by_dim[model][dim].append(sc)
            if lvl in by_diff[model]:
                by_diff[model][lvl].append(sc)
            if dim in length_by_dim[model]:
                length_by_dim[model][dim].append(len(ma))

        all_scores[model] = np.array(scores)
        all_lengths[model] = np.array(lengths)
        all_records[model] = recs_raw
        dimension_means[model] = {
            k: np.mean(v) if v else 0.0 for k, v in by_dim[model].items()
        }

    return all_scores, all_lengths, all_records, by_dim, by_diff, length_by_dim, dimension_means


def _save_fig(fig, name):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / name
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  → {path}")
    return path


def _sig_stars(p):
    if p < 0.001: return "***"
    if p < 0.01: return "**"
    if p < 0.05: return "*"
    if p < 0.10: return "†"
    return "ns"


# ═══════════════════════════════════════════════════════════════════
# A6: Score Distribution
# ═══════════════════════════════════════════════════════════════════

def analysis_a6_distribution(all_scores):
    """A6: 评分分布深度分析 — 直方图/KDE/偏度/峰度/双峰检测"""
    print("\n" + "=" * 60)
    print("A6: 评分分布 (Score Distribution)")
    print("=" * 60)

    models_sorted = sorted(all_scores.keys(), key=lambda m: all_scores[m].mean(), reverse=True)
    names = [MODEL_SHORT[m] for m in models_sorted]
    families = [MODEL_FAMILY[m] for m in models_sorted]
    colors = [FAMILY_COLORS[f] for f in families]

    dist_stats = []
    for m in models_sorted:
        s = all_scores[m]
        sk = float(skew(s))
        ku = float(kurtosis(s, fisher=True))
        qs = np.percentile(s, [25, 50, 75])
        iqr = qs[2] - qs[0]

        # Hartigan's dip test for unimodality
        try:
            from diptest import diptest
            dip_stat, dip_p = diptest(s)
        except ImportError:
            dip_stat, dip_p = None, None

        dist_stats.append({
            "model": m, "name": MODEL_SHORT[m],
            "mean": float(s.mean()), "std": float(s.std(ddof=1)),
            "skewness": round(sk, 4),
            "kurtosis": round(ku, 4),
            "q25": round(float(qs[0]), 4),
            "median": round(float(qs[1]), 4),
            "q75": round(float(qs[2]), 4),
            "iqr": round(float(iqr), 4),
            "dip_stat": round(float(dip_stat), 4) if dip_stat is not None else None,
            "dip_p": round(float(dip_p), 4) if dip_p is not None else None,
            "min": float(s.min()), "max": float(s.max()),
            "n_zeros": int((s == 0).sum()),
            "pct_zeros": round(float((s == 0).mean() * 100), 2),
        })

    # Print summary
    print(f"\n{'Model':<16} {'Mean':>6} {'Skew':>7} {'Kurt':>7} {'Q25':>6} {'Median':>6} {'Q75':>6} {'Zeros%':>7}")
    print("-" * 72)
    for st in dist_stats:
        print(f"{st['name']:<16} {st['mean']:>6.4f} {st['skewness']:>7.2f} {st['kurtosis']:>7.2f} "
              f"{st['q25']:>6.4f} {st['median']:>6.4f} {st['q75']:>6.4f} {st['pct_zeros']:>6.1f}%")

    # ── Chart 1: Density Ridges —──────────────
    print("\n  Chart 1: Density Ridges...")
    fig, ax = plt.subplots(figsize=(12, 8))
    y_offsets = list(range(len(models_sorted)))
    for i, (m, y) in enumerate(zip(models_sorted, y_offsets)):
        s = all_scores[m]
        kde = stats.gaussian_kde(s)
        x_grid = np.linspace(-0.05, 1.05, 300)
        density = kde(x_grid)
        density = density / density.max() * 0.7
        ax.fill_between(x_grid, y + density, y, alpha=0.6, color=colors[i])
        ax.plot(x_grid, y + density, color=colors[i], linewidth=1.2)
        ax.axhline(y, color="gray", linewidth=0.3, alpha=0.4)

    ax.set_yticks(y_offsets)
    ax.set_yticklabels(names, fontsize=10)
    ax.set_xlim(-0.05, 1.05)
    ax.set_xlabel("Score", fontsize=11)
    ax.set_title("A6: Score Distribution Density Ridges (by Model)", fontsize=13, fontweight="bold")
    ax.grid(axis="x", alpha=0.3)
    fig.tight_layout()
    _save_fig(fig, "a6_density_ridges.png")

    # ── Chart 2: Skewness vs Mean —─────────────
    print("  Chart 2: Skewness vs Mean...")
    fig, ax = plt.subplots(figsize=(10, 7))
    means_arr = [st["mean"] for st in dist_stats]
    skews_arr = [st["skewness"] for st in dist_stats]
    for i, m in enumerate(models_sorted):
        ax.scatter(means_arr[i], skews_arr[i], s=120, c=colors[i],
                   edgecolors="black", linewidths=0.5, zorder=5, label=names[i])
        ax.annotate(names[i], (means_arr[i], skews_arr[i]),
                    textcoords="offset points", xytext=(5, 5), fontsize=8)

    ax.axhline(0, color="gray", linestyle="--", alpha=0.4)
    ax.set_xlabel("Mean Score", fontsize=11)
    ax.set_ylabel("Skewness", fontsize=11)
    ax.set_title("A6: Score Skewness vs Mean (by Model)", fontsize=13, fontweight="bold")
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    _save_fig(fig, "a6_skewness_vs_mean.png")

    # ── Chart 3: Quantile Boxen/ECDF —──────────
    print("  Chart 3: ECDF (Cumulative Distribution)...")
    fig, ax = plt.subplots(figsize=(12, 7))
    for i, m in enumerate(models_sorted):
        s = sorted(all_scores[m])
        n = len(s)
        y = np.arange(1, n + 1) / n
        ax.plot(s, y, color=colors[i], linewidth=1.5, label=names[i],
                alpha=0.85)

    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.set_xlabel("Score", fontsize=11)
    ax.set_ylabel("Cumulative Proportion", fontsize=11)
    ax.set_title("A6: ECDF — Empirical Cumulative Distribution (by Model)", fontsize=13, fontweight="bold")
    ax.legend(fontsize=8, loc="lower right", ncol=2)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    _save_fig(fig, "a6_ecdf.png")

    # JSON output
    result_a6 = {
        "analysis": "A6_score_distribution",
        "n_models": len(models_sorted),
        "n_per_model": len(all_scores[models_sorted[0]]),
        "model_stats": dist_stats,
        "interpretation": (
            "负偏态 (skewness < 0) 表示高分集中；正偏态表示低分集中。"
            "峰度 > 0 表示极端值多。双峰 (dip test p<0.05) 暗示能力分化。"
        ),
    }
    json_path = OUTPUT_DIR / "a6_score_distribution.json"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        import json
        json.dump(result_a6, f, ensure_ascii=False, indent=2)
    print(f"  JSON: {json_path}")

    return result_a6


# ═══════════════════════════════════════════════════════════════════
# A7: Dimension Agreement (κ)
# ═══════════════════════════════════════════════════════════════════

def analysis_a7_dimension_kappa(all_scores, by_dim, data):
    """A7: 维度间一致性分析 — Kendall's W / ICC / 维间 Spearman"""
    print("\n" + "=" * 60)
    print("A7: 维度 κ 一致性 (Dimension Agreement)")
    print("=" * 60)

    models_sorted = sorted(data.keys(), key=lambda m: data[m].get("overall_score", 0), reverse=True)
    names = [MODEL_SHORT[m] for m in models_sorted]

    # ── 1. Kendall's W — model rankings across dimensions ──
    n_models = len(models_sorted)
    n_dims = len(DIMENSIONS)

    # Each model (rater) ranks the 4 dimensions → rows are models
    dim_rank_matrix = np.zeros((n_models, n_dims))
    for i, m in enumerate(models_sorted):
        scores_dim = [np.mean(by_dim[m][d]) if by_dim[m][d] else 0 for d in DIMENSIONS]
        ranks = stats.rankdata([-s for s in scores_dim], method="average")
        dim_rank_matrix[i, :] = ranks

    # Kendall's W: sum across raters (models) for each subject (dimension)
    Ri = dim_rank_matrix.sum(axis=0)
    R_mean = Ri.mean()
    S = ((Ri - R_mean) ** 2).sum()
    W_kendall = 12 * S / (n_models ** 2 * (n_dims ** 3 - n_dims))
    W_kendall = min(W_kendall, 1.0)

    # Friedman chi-square test
    friedman_chi2 = n_models * (n_dims - 1) * W_kendall
    friedman_p = 1 - stats.chi2.cdf(friedman_chi2, df=n_dims - 1)
    print(f"  Kendall's W = {W_kendall:.4f} (Friedman χ²={friedman_chi2:.2f}, p={friedman_p:.4f})")
    if W_kendall > 0.7:
        print(f"    → High concordance: models rank consistently across dimensions")
    elif W_kendall > 0.4:
        print(f"    → Moderate concordance")
    else:
        print(f"    → Low concordance: dimension rankings differ substantially")

    # ── 2. Pairwise dimension similarity (model ranks) ──
    dim_pairwise = {}
    for i, d1 in enumerate(DIMENSIONS):
        for j, d2 in enumerate(DIMENSIONS):
            if j <= i:
                continue
            s1 = [np.mean(by_dim[m][d1]) if by_dim[m][d1] else 0 for m in models_sorted]
            s2 = [np.mean(by_dim[m][d2]) if by_dim[m][d2] else 0 for m in models_sorted]
            if len(set(s1)) > 1 and len(set(s2)) > 1:
                r, p = spearmanr(s1, s2)
            else:
                r, p = 0.0, 1.0
            dim_pairwise[f"{d1}↔{d2}"] = {"spearman_rho": round(float(r), 4), "p": round(float(p), 4)}

    print(f"  Dimension pairwise Spearman:")
    for k, v in dim_pairwise.items():
        print(f"    {k}: ρ={v['spearman_rho']:.4f} {_sig_stars(v['p'])}")

    # ── 3. ICC (2,1) for dimension score reliability ──
    icc_matrix = np.zeros((n_models, n_dims))
    for i, m in enumerate(models_sorted):
        for j, d in enumerate(DIMENSIONS):
            icc_matrix[i, j] = np.mean(by_dim[m][d]) if by_dim[m][d] else 0

    ms_between = n_dims * np.var(icc_matrix.mean(axis=1), ddof=1)
    ms_within = np.mean([np.var(icc_matrix[i, :], ddof=1) for i in range(n_models)])
    icc_2_1 = (ms_between - ms_within) / (ms_between + (n_dims - 1) * ms_within) if (ms_between + (n_dims - 1) * ms_within) > 0 else 0
    print(f"  ICC(2,1): {icc_2_1:.4f}")
    if icc_2_1 > 0.75:
        print(f"    → Excellent reliability")
    elif icc_2_1 > 0.5:
        print(f"    → Good reliability")
    else:
        print(f"    → Poor reliability")

    # ── Chart 1: Dimension Ranking Heatmap ──
    print("  Chart 1: Dimension Ranking Heatmap...")
    fig, ax = plt.subplots(figsize=(10, 8))

    rank_pct = np.zeros((n_models, n_dims))
    for j, d in enumerate(DIMENSIONS):
        scores_dim = [np.mean(by_dim[m][d]) if by_dim[m][d] else 0 for m in models_sorted]
        max_s = max(scores_dim) if scores_dim else 1
        for i in range(n_models):
            rank_pct[i, j] = scores_dim[i] / max_s if max_s > 0 else 0

    annot = np.empty_like(rank_pct, dtype=object)
    for i in range(n_models):
        for j in range(n_dims):
            val = np.mean(by_dim[models_sorted[i]][DIMENSIONS[j]]) if by_dim[models_sorted[i]][DIMENSIONS[j]] else 0
            annot[i, j] = f"{val:.4f}"

    sns.heatmap(rank_pct, annot=annot, fmt="", cmap="RdYlGn", vmin=0.5, vmax=1.0,
                xticklabels=DIMENSIONS, yticklabels=names,
                linewidths=0.5, linecolor="white",
                cbar_kws={"label": "Score / Max per Dim"},
                annot_kws={"fontsize": 9}, ax=ax)
    ax.set_title(f"A7: Dimension Score Matrix (Kendall's W={W_kendall:.3f})", fontsize=12, fontweight="bold")
    ax.set_xlabel("Dimension", fontsize=11)
    ax.set_ylabel("Model", fontsize=11)
    fig.tight_layout()
    _save_fig(fig, "a7_dimension_agreement.png")

    # ── Chart 2: Dimension Concordance: Radar of Rankings ──
    print("  Chart 2: Dimension Concordance Radar...")
    angles = np.linspace(0, 2 * np.pi, n_dims, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw={"projection": "polar"})
    for i, m in enumerate(models_sorted):
        vals = [np.mean(by_dim[m][d]) if by_dim[m][d] else 0 for d in DIMENSIONS]
        vals += vals[:1]
        clr = FAMILY_COLORS.get(MODEL_FAMILY[m], "#888")
        ax.plot(angles, vals, color=clr,
                linewidth=1.2, alpha=0.6, label=names[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(DIMENSIONS, fontsize=11)
    ax.set_ylim(0, 0.85)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8])
    ax.set_title(f"A7: Dimension Concordance (W={W_kendall:.3f})", fontsize=13, fontweight="bold", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0), fontsize=8)
    ax.grid(alpha=0.4)
    fig.tight_layout()
    _save_fig(fig, "a7_concordance_radar.png")

    result_a7 = {
        "analysis": "A7_dimension_agreement",
        "n_models": n_models,
        "n_dimensions": n_dims,
        "kendall_W": round(float(W_kendall), 4),
        "friedman_chi2": round(float(friedman_chi2), 2),
        "friedman_p": round(float(friedman_p), 4),
        "icc_2_1": round(float(icc_2_1), 4),
        "dimension_pairwise_spearman": dim_pairwise,
        "interpretation": (
            "Kendall's W 接近 1 说明模型在各维度的排名高度一致；"
            "ICC(2,1) > 0.75 表示维度评分可靠性优秀。"
        ),
    }
    json_path = OUTPUT_DIR / "a7_dimension_agreement.json"
    with open(json_path, "w", encoding="utf-8") as f:
        import json
        json.dump(result_a7, f, ensure_ascii=False, indent=2)
    print(f"  JSON: {json_path}")

    return result_a7


# ═══════════════════════════════════════════════════════════════════
# A8: Difficulty Matrix
# ═══════════════════════════════════════════════════════════════════

def analysis_a8_difficulty_matrix(all_scores, by_diff, by_dim, data):
    """A8: 难度矩阵 — 模型×难度/题目难度分析/衰退模式"""
    print("\n" + "=" * 60)
    print("A8: 难度矩阵 (Difficulty Matrix)")
    print("=" * 60)

    models_sorted = sorted(data.keys(), key=lambda m: data[m].get("overall_score", 0), reverse=True)
    names = [MODEL_SHORT[m] for m in models_sorted]

    # ── 1. Model × Difficulty mean score matrix ──
    diff_matrix = np.zeros((len(models_sorted), len(DIFFICULTIES)))
    for i, m in enumerate(models_sorted):
        for j, lvl in enumerate(DIFFICULTIES):
            vals = by_diff[m].get(lvl, [])
            diff_matrix[i, j] = np.mean(vals) if vals else 0.0

    print(f"\n  Model × Difficulty Mean Score Matrix:")
    header = f"{'Model':<16}" + "".join(f"{lvl:>8}" for lvl in DIFFICULTIES)
    print(f"  {header}")
    print(f"  {'-' * (16 + 8 * len(DIFFICULTIES))}")
    for i, m in enumerate(models_sorted):
        vals = "".join(f"{diff_matrix[i, j]:>8.4f}" for j in range(len(DIFFICULTIES)))
        print(f"  {names[i]:<16}{vals}")

    # ── 2. Item difficulty (p-value) distribution ──
    all_item_scores = []
    for m in models_sorted:
        all_item_scores.append(all_scores[m])
    avg_scores = np.mean(all_item_scores, axis=0)
    difficulty_bins = {
        "very_hard (0.0-0.2)": int((avg_scores < 0.2).sum()),
        "hard (0.2-0.4)": int(((avg_scores >= 0.2) & (avg_scores < 0.4)).sum()),
        "medium (0.4-0.6)": int(((avg_scores >= 0.4) & (avg_scores < 0.6)).sum()),
        "easy (0.6-0.8)": int(((avg_scores >= 0.6) & (avg_scores < 0.8)).sum()),
        "very_easy (0.8-1.0)": int((avg_scores >= 0.8).sum()),
    }
    print(f"\n  Item difficulty (avg score across models):")
    for k, v in difficulty_bins.items():
        print(f"    {k}: {v} items ({v/len(avg_scores)*100:.1f}%)")

    # ── 3. Score deterioration velocity ──
    decay_info = []
    for i, m in enumerate(models_sorted):
        l1_m = diff_matrix[i, 0] if diff_matrix[i, 0] > 0 else 0.001
        l4_m = diff_matrix[i, -1]
        absolute_decay = l1_m - l4_m
        relative_decay = absolute_decay / l1_m
        per_step = absolute_decay / 3
        decay_info.append({
            "model": m, "name": names[i], "L1": float(diff_matrix[i, 0]),
            "L2": float(diff_matrix[i, 1]), "L3": float(diff_matrix[i, 2]),
            "L4": float(diff_matrix[i, 3]),
            "absolute_decay": round(float(absolute_decay), 4),
            "relative_decay": round(float(relative_decay), 4),
            "decay_per_step": round(float(per_step), 4),
        })

    print(f"\n  Score Decay L1→L4:")
    header2 = f"{'Model':<16} {'L1':>7} {'L4':>7} {'AbsΔ':>7} {'RelΔ':>7} {'/step':>7}"
    print(f"  {header2}")
    print(f"  {'-' * (16 + 7 * 5)}")
    for di in decay_info:
        print(f"  {di['name']:<16} {di['L1']:>7.4f} {di['L4']:>7.4f} "
              f"{di['absolute_decay']:>7.4f} {di['relative_decay']:>7.1%} {di['decay_per_step']:>7.4f}")

    # ── Chart 1: Model × Difficulty Heatmap ──
    print("\n  Chart 1: Model × Difficulty Heatmap...")
    fig, ax = plt.subplots(figsize=(10, 8))
    annot = np.empty_like(diff_matrix, dtype=object)
    for i in range(len(models_sorted)):
        for j in range(len(DIFFICULTIES)):
            annot[i, j] = f"{diff_matrix[i, j]:.4f}"
    sns.heatmap(diff_matrix, annot=annot, fmt="", cmap="YlOrRd",
                vmin=0.0, vmax=0.85,
                xticklabels=DIFFICULTIES, yticklabels=names,
                linewidths=0.5, linecolor="white",
                cbar_kws={"label": "Mean Score"},
                annot_kws={"fontsize": 9}, ax=ax)
    ax.set_title("A8: Model × Difficulty Level (Mean Score)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Difficulty Level", fontsize=11)
    ax.set_ylabel("Model", fontsize=11)
    fig.tight_layout()
    _save_fig(fig, "a8_difficulty_matrix.png")

    # ── Chart 2: Decay Curves (model family grouped) ──
    print("  Chart 2: Decay Curves...")
    fig, ax = plt.subplots(figsize=(11, 7))
    for i, m in enumerate(models_sorted):
        family = MODEL_FAMILY.get(m, "Other")
        color = FAMILY_COLORS.get(family, "#888")
        lw = 2.0 if names[i] in ["MiMo-v2-flash", "DS-v4-flash", "Qwen3.5:9b"] else 1.2
        ls = "-" if lw > 1.5 else "--"
        ax.plot(DIFFICULTIES, diff_matrix[i, :], marker="o", label=names[i],
                color=color, linewidth=lw, linestyle=ls, markersize=6 if lw > 1.5 else 4)

    ax.set_ylim(0, 1)
    ax.set_xlabel("Difficulty Level", fontsize=11)
    ax.set_ylabel("Mean Score", fontsize=11)
    ax.set_title("A8: Score Decay Curves (L1→L4)", fontsize=13, fontweight="bold")
    ax.legend(loc="lower left", fontsize=8, ncol=2)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    _save_fig(fig, "a8_decay_curves.png")

    # ── Chart 3: Item Difficulty Histogram ──
    print("  Chart 3: Item Difficulty Histogram...")
    fig, ax = plt.subplots(figsize=(10, 6))
    bins = np.linspace(0, 1, 21)
    ax.hist(avg_scores, bins=bins, color="#3498DB", alpha=0.7, edgecolor="white",
            linewidth=0.5)
    ax.axvline(avg_scores.mean(), color="#E74C3C", linestyle="--", linewidth=2,
               label=f"Mean difficulty={avg_scores.mean():.3f}")
    ax.axvline(0.2, color="gray", linestyle=":", alpha=0.5)
    ax.axvline(0.8, color="gray", linestyle=":", alpha=0.5)
    ax.set_xlabel("Item Difficulty (avg score across 9 models)", fontsize=11)
    ax.set_ylabel("Number of Items", fontsize=11)
    ax.set_title("A8: Item Difficulty Distribution", fontsize=13, fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    _save_fig(fig, "a8_item_difficulty_hist.png")

    result_a8 = {
        "analysis": "A8_difficulty_matrix",
        "n_models": len(models_sorted),
        "n_per_model": len(all_scores[models_sorted[0]]),
        "difficulty_matrix": {
            "models": names,
            "difficulty_levels": DIFFICULTIES,
            "values": [[round(float(diff_matrix[i, j]), 4) for j in range(len(DIFFICULTIES))]
                       for i in range(len(models_sorted))],
        },
        "item_difficulty_bins": difficulty_bins,
        "mean_item_difficulty": round(float(avg_scores.mean()), 4),
        "decay_details": decay_info,
        "most_stable": min(decay_info, key=lambda x: x["absolute_decay"]),
        "most_sensitive": max(decay_info, key=lambda x: x["absolute_decay"]),
        "interpretation": (
            "Item difficulty (p-value) 表示所有模型在该题上的平均得分。"
            "<0.2 为非常困难，>0.8 为非常容易。"
            "Decay 越大表示模型对难度变化越敏感。"
        ),
    }
    json_path = OUTPUT_DIR / "a8_difficulty_matrix.json"
    with open(json_path, "w", encoding="utf-8") as f:
        import json
        json.dump(result_a8, f, ensure_ascii=False, indent=2)
    print(f"  JSON: {json_path}")

    return result_a8


# ═══════════════════════════════════════════════════════════════════
# A9: Length Bias
# ═══════════════════════════════════════════════════════════════════

def analysis_a9_length_bias(all_scores, all_lengths, by_dim, data):
    """A9: 长度偏见分析 — model_answer 长度与评分的相关性"""
    print("\n" + "=" * 60)
    print("A9: 长度偏见 (Length Bias)")
    print("=" * 60)

    models_sorted = sorted(data.keys(), key=lambda m: data[m].get("overall_score", 0), reverse=True)
    names = [MODEL_SHORT[m] for m in models_sorted]
    families = [MODEL_FAMILY[m] for m in models_sorted]
    colors = [FAMILY_COLORS[f] for f in families]

    # ── 1. Per-model length vs score correlation ──
    len_corrs = []
    for idx, m in enumerate(models_sorted):
        lens = all_lengths[m]
        scores = all_scores[m]
        if np.std(lens) > 0 and np.std(scores) > 0:
            r_pearson, p_pearson = pearsonr(lens, scores)
            r_spearman, p_spearman = spearmanr(lens, scores)
        else:
            r_pearson, p_pearson = 0.0, 1.0
            r_spearman, p_spearman = 0.0, 1.0

        len_corrs.append({
            "model": m, "name": names[idx],
            "mean_length": int(lens.mean()),
            "median_length": int(np.median(lens)),
            "std_length": int(lens.std(ddof=1)),
            "min_length": int(lens.min()), "max_length": int(lens.max()),
            "pearson_r": round(float(r_pearson), 4),
            "pearson_p": round(float(p_pearson), 4),
            "spearman_rho": round(float(r_spearman), 4),
            "spearman_p": round(float(p_spearman), 4),
        })

    print(f"\n{'Model':<16} {'AvgLen':>7} {'Pearson r':>10} {'p':>8} {'Spearman ρ':>10} {'p':>8}")
    print("-" * 63)
    for lc in len_corrs:
        print(f"{lc['name']:<16} {lc['mean_length']:>7} {lc['pearson_r']:>10.4f} "
              f"{_sig_stars(lc['pearson_p']):>8} {lc['spearman_rho']:>10.4f} {_sig_stars(lc['spearman_p']):>8}")

    # ── 2. Global length distribution ──
    all_lens_flat = np.concatenate([all_lengths[m] for m in models_sorted])
    all_scores_flat = np.concatenate([all_scores[m] for m in models_sorted])
    global_r, global_p = pearsonr(all_lens_flat, all_scores_flat)
    global_rho, global_rho_p = spearmanr(all_lens_flat, all_scores_flat)
    print(f"\n  Global (all models pooled):")
    print(f"    Pearson r={global_r:.4f} {_sig_stars(global_p)}")
    print(f"    Spearman ρ={global_rho:.4f} {_sig_stars(global_rho_p)}")

    # ── 3. Length × Dimension interaction ──
    dimension_corrs = {}
    print(f"\n  Length-Score correlation by dimension:")
    for d in DIMENSIONS:
        dim_lens = np.concatenate([
            all_lengths[m][[rec.get("dimension", "") == d for rec in data[m].get("records", [])]]
            for m in models_sorted if all_lengths[m].size > 0
        ])
        dim_scores = np.concatenate([
            all_scores[m][[rec.get("dimension", "") == d for rec in data[m].get("records", [])]]
            for m in models_sorted if all_scores[m].size > 0
        ])
        if len(dim_lens) > 1 and np.std(dim_lens) > 0 and np.std(dim_scores) > 0:
            dr, dp = pearsonr(dim_lens, dim_scores)
        else:
            dr, dp = 0.0, 1.0
        dimension_corrs[d] = {"pearson_r": round(float(dr), 4), "p": round(float(dp), 4)}
        print(f"    Dim {d}: r={dr:.4f} {_sig_stars(dp)} (n={len(dim_lens)})")

    # ── Chart 1: Length vs Score Scatter (per model) ──
    print("  Chart 1: Length vs Score Scatter...")
    n_sub = len(models_sorted)
    n_cols = 3
    n_rows = (n_sub + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, 4 * n_rows))
    axes_flat = axes.flatten() if n_sub > 1 else [axes]

    for idx, m in enumerate(models_sorted):
        ax = axes_flat[idx]
        lens = all_lengths[m]
        scores = all_scores[m]
        ax.scatter(lens, scores, c=colors[idx], alpha=0.3, s=8, edgecolors="none")
        if len(lens) > 1:
            z = np.polyfit(lens, scores, 1)
            p_fit = np.poly1d(z)
            x_line = np.linspace(lens.min(), lens.max(), 100)
            ax.plot(x_line, p_fit(x_line), color=colors[idx], linewidth=1.5, linestyle="--")

        lc = len_corrs[idx]
        ax.text(0.95, 0.05, f"r={lc['pearson_r']:.3f}\nρ={lc['spearman_rho']:.3f}",
                transform=ax.transAxes, ha="right", va="bottom",
                fontsize=8, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
        ax.set_xlabel("Answer Length (chars)", fontsize=8)
        ax.set_ylabel("Score", fontsize=8)
        ax.set_title(names[idx], fontsize=9, fontweight="bold")
        ax.set_ylim(-0.05, 1.05)
        ax.grid(alpha=0.3)

    for idx in range(len(models_sorted), len(axes_flat)):
        axes_flat[idx].set_visible(False)

    fig.suptitle("A9: Answer Length vs Score (per Model)", fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    _save_fig(fig, "a9_length_vs_score.png")

    # ── Chart 2: Global Length Distribution ──
    print("  Chart 2: Global Length Distribution...")
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Left: Histogram of lengths by model
    ax = axes[0]
    for i, m in enumerate(models_sorted):
        ax.hist(all_lengths[m], bins=30, alpha=0.4, color=colors[i], label=names[i])
    ax.set_xlabel("Answer Length (chars)", fontsize=11)
    ax.set_ylabel("Frequency", fontsize=11)
    ax.set_title("A9: Answer Length Distribution (by Model)", fontsize=12, fontweight="bold")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(axis="y", alpha=0.3)

    # Right: Length vs Score (grouped bins)
    ax = axes[1]
    length_bins = [0, 500, 1000, 1500, 2000, 3000, 5000, 10000]
    length_labels = ["<500", "500-1k", "1k-1.5k", "1.5k-2k", "2k-3k", "3k-5k", ">5k"]
    bin_means = []
    bin_counts = []
    for i in range(len(length_bins) - 1):
        mask = (all_lens_flat >= length_bins[i]) & (all_lens_flat < length_bins[i + 1])
        bin_means.append(all_scores_flat[mask].mean() if mask.sum() > 0 else 0)
        bin_counts.append(mask.sum())
    bin_means[-1] = all_scores_flat[all_lens_flat >= length_bins[-2]].mean()

    bars = ax.bar(length_labels, bin_means, alpha=0.7, color="#3498DB", edgecolor="white")
    for i, (b, c) in enumerate(zip(bin_means, bin_counts)):
        ax.text(i, b + 0.01, f"n={c}", ha="center", fontsize=8)

    ax.set_xlabel("Answer Length (chars)", fontsize=11)
    ax.set_ylabel("Mean Score", fontsize=11)
    ax.set_title(f"A9: Mean Score by Length Bin (Global r={global_r:.3f})", fontsize=12, fontweight="bold")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    _save_fig(fig, "a9_length_distribution.png")

    # ── Chart 3: Expected vs Actual Length ──
    print("  Chart 3: Expected vs Actual Length Ratio...")
    exp_lens_by_model = {}
    for m in models_sorted:
        exp_lens = []
        for rec in data[m].get("records", []):
            exp_lens.append(len(rec.get("expected_answer", "")))
        exp_lens_by_model[m] = np.array(exp_lens)

    fig, ax = plt.subplots(figsize=(11, 7))
    for i, m in enumerate(models_sorted):
        ratio = all_lengths[m] / np.maximum(exp_lens_by_model[m], 1)
        ratio = np.clip(ratio, 0, 10)
        scores = all_scores[m]
        ax.scatter(ratio, scores, c=colors[i], alpha=0.2, s=5, label=names[i])

    ax.axvline(1.0, color="gray", linestyle="--", alpha=0.5, label="Model=Expected length")
    ax.set_xlabel("Model Answer Length / Expected Answer Length", fontsize=11)
    ax.set_ylabel("Score", fontsize=11)
    ax.set_xlim(0, 8)
    ax.set_ylim(-0.05, 1.05)
    ax.set_title("A9: Length Ratio (Model/Expected) vs Score", fontsize=13, fontweight="bold")
    ax.legend(fontsize=7, ncol=2, loc="upper right")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    _save_fig(fig, "a9_length_ratio.png")

    result_a9 = {
        "analysis": "A9_length_bias",
        "n_models": len(models_sorted),
        "n_per_model": len(all_scores[models_sorted[0]]),
        "global_pearson_r": round(float(global_r), 4),
        "global_pearson_p": round(float(global_p), 4),
        "global_spearman_rho": round(float(global_rho), 4),
        "global_spearman_p": round(float(global_rho_p), 4),
        "per_model": len_corrs,
        "dimension_corrs": dimension_corrs,
        "interpretation": (
            "若 Pearson r 显著为正 → 存在长度偏见（Judge 倾向于给长答案高分）。"
            "若 r ≈ 0 → 无系统性长度偏见。"
        ),
    }
    json_path = OUTPUT_DIR / "a9_length_bias.json"
    with open(json_path, "w", encoding="utf-8") as f:
        import json
        json.dump(result_a9, f, ensure_ascii=False, indent=2)
    print(f"  JSON: {json_path}")

    return result_a9


# ═══════════════════════════════════════════════════════════════════
# Report Generation
# ═══════════════════════════════════════════════════════════════════

def render_markdown(data, a6_result, a7_result, a8_result, a9_result):
    md = []
    md.append("# T3: 深度分析扩展 — A6~A9")
    md.append("")
    md.append(f"**Generated:** 2026-05-09 | **Models:** 9 | **Questions per model:** 500")
    md.append("")
    md.append("---")
    md.append("")

    # ── A6 ──
    md.append("## A6: 评分分布 (Score Distribution)")
    md.append("")
    md.append("| Model | Mean | Std | Skew | Kurt | Q25 | Median | Q75 | IQR | Zeros% |")
    md.append("|-------|------|-----|------|------|-----|--------|-----|-----|--------|")
    for st in a6_result["model_stats"]:
        md.append(f"| {st['name']} | {st['mean']:.4f} | {st['std']:.4f} | "
                  f"{st['skewness']:+.2f} | {st['kurtosis']:+.2f} | {st['q25']:.4f} | "
                  f"{st['median']:.4f} | {st['q75']:.4f} | {st['iqr']:.4f} | {st['pct_zeros']:.1f}% |")
    md.append("")

    md.append("### Distribution Charts")
    md.append("")
    md.append("- **A6 Density Ridges**: `a6_density_ridges.png` — Per-model score density curves")
    md.append("- **A6 Skewness vs Mean**: `a6_skewness_vs_mean.png` — Distribution shape vs central tendency")
    md.append("- **A6 ECDF**: `a6_ecdf.png` — Empirical cumulative distribution functions")
    md.append("")

    # ── A7 ──
    md.append("## A7: 维度 κ 一致性 (Dimension Agreement)")
    md.append("")
    md.append(f"**Kendall's W (Coefficient of Concordance):** {a7_result['kendall_W']:.4f}")
    md.append("")
    md.append(f"- Friedman χ² = {a7_result['friedman_chi2']:.2f}, p = {a7_result['friedman_p']:.4f} {_sig_stars(a7_result['friedman_p'])}")
    md.append(f"- ICC(2,1) = {a7_result['icc_2_1']:.4f}")
    md.append("")
    md.append("### Pairwise Dimension Spearman ρ")
    md.append("")
    md.append("| Dimension Pair | ρ | Significance |")
    md.append("|---------------|----|-------------|")
    for k, v in a7_result["dimension_pairwise_spearman"].items():
        md.append(f"| {k} | {v['spearman_rho']:.4f} | {_sig_stars(v['p'])} |")
    md.append("")
    md.append("### Charts")
    md.append("- **A7 Dimension Agreement**: `a7_dimension_agreement.png` — Score matrix normalized by dimension")
    md.append("- **A7 Concordance Radar**: `a7_concordance_radar.png` — Polar plot of dimension profiles")
    md.append("")

    # ── A8 ──
    md.append("## A8: 难度矩阵 (Difficulty Matrix)")
    md.append("")
    dm = a8_result["difficulty_matrix"]
    md.append("| Model | L1 | L2 | L3 | L4 | AbsΔ | RelΔ |")
    md.append("|-------|----|----|----|----|------|------|")
    for i in range(len(dm["models"])):
        vals = dm["values"][i]
        decay = a8_result["decay_details"][i]
        md.append(f"| {dm['models'][i]} | {vals[0]:.4f} | {vals[1]:.4f} | "
                  f"{vals[2]:.4f} | {vals[3]:.4f} | "
                  f"{decay['absolute_decay']:.4f} | {decay['relative_decay']:.1%} |")
    md.append("")

    md.append(f"**Most stable:** {a8_result['most_stable']['name']} (decay={a8_result['most_stable']['absolute_decay']:.4f})")
    md.append("")
    md.append(f"**Most sensitive:** {a8_result['most_sensitive']['name']} (decay={a8_result['most_sensitive']['absolute_decay']:.4f})")
    md.append("")

    md.append("### Item Difficulty Distribution")
    md.append("")
    md.append(f"Mean item difficulty (all models): **{a8_result['mean_item_difficulty']:.4f}**")
    md.append("")
    md.append("| Category | Count | % |")
    md.append("|----------|-------|---|")
    for k, v in a8_result["item_difficulty_bins"].items():
        md.append(f"| {k} | {v} | {v/500*100:.1f}% |")
    md.append("")

    md.append("### Charts")
    md.append("- **A8 Difficulty Matrix**: `a8_difficulty_matrix.png` — Model × Difficulty level heatmap")
    md.append("- **A8 Decay Curves**: `a8_decay_curves.png` — Score decay L1→L4 per model")
    md.append("- **A8 Item Difficulty Histogram**: `a8_item_difficulty_hist.png` — Distribution of item p-values")
    md.append("")

    # ── A9 ──
    md.append("## A9: 长度偏见 (Length Bias)")
    md.append("")
    md.append(f"**Global Pearson r:** {a9_result['global_pearson_r']:.4f} {_sig_stars(a9_result['global_pearson_p'])}")
    md.append(f"**Global Spearman ρ:** {a9_result['global_spearman_rho']:.4f} {_sig_stars(a9_result['global_spearman_p'])}")
    md.append("")

    md.append("| Model | AvgLen | Min | Max | Pearson r | p | Spearman ρ | p |")
    md.append("|-------|--------|-----|-----|-----------|----|------------|----|")
    for lc in a9_result["per_model"]:
        md.append(f"| {lc['name']} | {lc['mean_length']} | {lc['min_length']} | "
                  f"{lc['max_length']} | {lc['pearson_r']:.4f} | {_sig_stars(lc['pearson_p'])} | "
                  f"{lc['spearman_rho']:.4f} | {_sig_stars(lc['spearman_p'])} |")
    md.append("")

    md.append("### Dimension Breakdown")
    md.append("")
    for d in DIMENSIONS:
        if d in a9_result.get("dimension_corrs", {}):
            dc = a9_result["dimension_corrs"][d]
            md.append(f"- **Dim {d}**: Pearson r = {dc['pearson_r']:.4f} {_sig_stars(dc['p'])}")
    md.append("")
    md.append("### Charts")
    md.append("- **A9 Length vs Score**: `a9_length_vs_score.png` — Scatter plot per model with regression line")
    md.append("- **A9 Length Distribution**: `a9_length_distribution.png` — Histogram + binned mean score")
    md.append("- **A9 Length Ratio**: `a9_length_ratio.png` — Model/Expected length ratio vs score")
    md.append("")

    # ── Methodology ──
    md.append("## Methodology Notes")
    md.append("")
    md.append("- **A6**: Skewness = Fisher-Pearson standardized moment; Kurtosis = Fisher (excess, 0=normal). Dip test requires `scipy.stats` or `diptest` package.")
    md.append("- **A7**: Kendall's W measures rank concordance across dimensions (0=no agreement, 1=perfect). ICC(2,1) = two-way random effects, single rater.")
    md.append("- **A8**: Item difficulty = mean score across all 9 models (classical test theory p-value). Decay = L1 - L4 absolute difference.")
    md.append("- **A9**: Length = len(model_answer) in characters. Both Pearson (linear) and Spearman (monotonic) correlations reported.")
    md.append("")

    return "\n".join(md)


# ═══════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════

def main():
    import argparse
    global OUTPUT_DIR
    parser = argparse.ArgumentParser(description="T3: Deep Analysis Extension — A6~A9")
    parser.add_argument("--reports", default=str(ROOT / "benchmark" / "eval" / "reports"),
                        help="Directory containing *_report.json files")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR),
                        help="Output directory for charts and report")
    parser.add_argument("--skip", nargs="*", choices=["A6", "A7", "A8", "A9"], default=[],
                        help="Skip specific analyses")
    args = parser.parse_args()

    OUTPUT_DIR = Path(args.output_dir)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("T3: 深度分析扩展 — A6~A9")
    print("=" * 60)

    # 1. Load data
    print("\n[1/4] Loading 9 model reports...")
    data = load_core_9(args.reports)
    if len(data) < 3:
        print(f"ERROR: Only {len(data)} models loaded, need ≥ 3. Exiting.")
        return 1
    print(f"  Loaded {len(data)} models: {', '.join(MODEL_SHORT.get(m, m) for m in data)}")

    # 2. Extract records
    print("\n[2/4] Extracting records...")
    all_scores, all_lengths, all_records, by_dim, by_diff, length_by_dim, dimension_means = \
        extract_records(data)

    results = {}

    # 3. A6-A9 analyses
    print("\n[3/4] Running analyses A6~A9...")

    if "A6" not in args.skip:
        print("\n" + "-" * 40)
        results["A6"] = analysis_a6_distribution(all_scores)

    if "A7" not in args.skip:
        print("\n" + "-" * 40)
        results["A7"] = analysis_a7_dimension_kappa(all_scores, by_dim, data)

    if "A8" not in args.skip:
        print("\n" + "-" * 40)
        results["A8"] = analysis_a8_difficulty_matrix(all_scores, by_diff, by_dim, data)

    if "A9" not in args.skip:
        print("\n" + "-" * 40)
        results["A9"] = analysis_a9_length_bias(all_scores, all_lengths, by_dim, data)

    # 4. Report
    print("\n[4/4] Generating Markdown report...")
    md = render_markdown(data,
                         results.get("A6", {"model_stats": []}),
                         results.get("A7", {"kendall_W": 0, "friedman_chi2": 0, "friedman_p": 1,
                                             "icc_2_1": 0, "dimension_pairwise_spearman": {}}),
                         results.get("A8", {"difficulty_matrix": {"models": [], "difficulty_levels": [],
                                                                    "values": []},
                                             "item_difficulty_bins": {}, "mean_item_difficulty": 0,
                                             "decay_details": [], "most_stable": {}, "most_sensitive": {}}),
                         results.get("A9", {"global_pearson_r": 0, "global_pearson_p": 1,
                                             "global_spearman_rho": 0, "global_spearman_p": 1,
                                             "per_model": [], "dimension_corrs": {}}))
    report_path = OUTPUT_DIR / "t3_deep_analysis.md"
    report_path.write_text(md, encoding="utf-8")
    print(f"  Report: {report_path}")

    print(f"\n{'=' * 60}")
    print("T3: A6~A9 analysis complete.")
    lists = [f"benchmark/eval/results/analysis/a{i}_{name}.png"
             for i, name in [("6", "density_ridges"), ("6", "skewness_vs_mean"), ("6", "ecdf"),
                             ("7", "dimension_agreement"), ("7", "concordance_radar"),
                             ("8", "difficulty_matrix"), ("8", "decay_curves"), ("8", "item_difficulty_hist"),
                             ("9", "length_vs_score"), ("9", "length_distribution"), ("9", "length_ratio")]]
    print(f"Charts: {len(lists)} PNGs + 4 JSONs + 1 Markdown")
    print(f"Output: {OUTPUT_DIR}")
    print(f"{'=' * 60}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
