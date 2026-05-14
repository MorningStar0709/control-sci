"""
T2: 9-Model Deep Analysis
Statistical inference + visualization for ControlSci Benchmark.

Produces:
  - 6 PNG charts in results/analysis/
  - 1 comprehensive Markdown report

Methods:
  Kruskal-Wallis + Dunn's post-hoc (Bonferroni)
  Cohen's d pairwise effect sizes
  Spearman correlation + hierarchical clustering
  Per-dimension / per-difficulty breakdown
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
import scikit_posthocs as sp

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ── 字体 ──────────────────────────────────────────────────────────
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ── 常量 ──────────────────────────────────────────────────────────
CORE_9 = [
    "mimo-v2-flash",
    "deepseek-v4-flash",
    "qwen3.5:9b",
    "deepseek-v4-pro",
    "minimax-m2.5",
    "minimax-m2.7",
    "mimo-v2.5-pro",
    "mimo-v2-pro",
    "mimo-v2.5",
]

_MODEL_ALIASES = {
    "MiniMax-M2.5-highspeed": "minimax-m2.5",
    "MiniMax-M2.7-highspeed": "minimax-m2.7",
}
DIMENSIONS = ["A", "B", "C", "D"]
DIFFICULTIES = ["L1", "L2", "L3", "L4"]
OUTPUT_DIR = ROOT / "benchmark" / "eval" / "results" / "analysis"

# ── 模型简称 ──────────────────────────────────────────────────────
MODEL_SHORT = {
    "mimo-v2-flash": "MiMo-v2-flash",
    "deepseek-v4-flash": "DS-v4-flash",
    "qwen3.5:9b": "Qwen3.5:9b",
    "deepseek-v4-pro": "DS-v4-pro",
    "minimax-m2.5": "MM-m2.5",
    "minimax-m2.7": "MM-m2.7",
    "mimo-v2.5-pro": "MiMo-v2.5-pro",
    "mimo-v2-pro": "MiMo-v2-pro",
    "mimo-v2.5": "MiMo-v2.5",
}

MODEL_FAMILY = {
    "mimo-v2-flash": "MiMo",
    "deepseek-v4-flash": "DeepSeek",
    "qwen3.5:9b": "Qwen",
    "deepseek-v4-pro": "DeepSeek",
    "minimax-m2.5": "MiniMax",
    "minimax-m2.7": "MiniMax",
    "mimo-v2.5-pro": "MiMo",
    "mimo-v2-pro": "MiMo",
    "mimo-v2.5": "MiMo",
}

FAMILY_COLORS = {
    "MiMo": "#1f77b4",
    "DeepSeek": "#ff7f0e",
    "Qwen": "#2ca02c",
    "MiniMax": "#d62728",
}


# ═══════════════════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════════════════

def load_core_9(reports_dir: Path | str | None = None):
    """Load the 9 core-model full-evaluation reports."""
    if reports_dir is None:
        reports_dir = ROOT / "benchmark" / "eval" / "reports"

    reports_dir = Path(reports_dir)
    if not reports_dir.is_dir():
        raise FileNotFoundError(f"Reports directory not found: {reports_dir}")

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
        print(f"⚠ 缺失模型报告: {missing}")

    return data


def extract_records(data: dict):
    """data[model] = full report → arrays of scores by dimension / difficulty."""
    by_dim = {m: {d: [] for d in DIMENSIONS} for m in data}
    by_diff = {m: {lvl: [] for lvl in DIFFICULTIES} for m in data}
    all_scores = {}
    dimension_means = {}

    for model, d in data.items():
        scores = []
        for rec in d.get("records", []):
            dim = rec.get("dimension", "")
            lvl = rec.get("difficulty_level", "")
            sc = rec.get("score", 0)
            scores.append(sc)
            if dim in by_dim[model]:
                by_dim[model][dim].append(sc)
            if lvl in by_diff[model]:
                by_diff[model][lvl].append(sc)
        all_scores[model] = np.array(scores)
        dimension_means[model] = {k: np.mean(v) if v else 0.0 for k, v in by_dim[model].items()}

    return all_scores, by_dim, by_diff, dimension_means


# ═══════════════════════════════════════════════════════════════════
# Statistical Inference
# ═══════════════════════════════════════════════════════════════════

def kruskal_wallis_test(all_scores: dict, label: str = "Overall"):
    """Kruskal-Wallis H test across all models."""
    groups = [all_scores[m] for m in CORE_9 if m in all_scores]
    if len(groups) < 3:
        return None
    H, p = stats.kruskal(*groups)
    return {"test": "Kruskal-Wallis", "label": label, "H": H, "p": p,
            "df": len(groups) - 1, "n_models": len(groups), "n_total": sum(len(g) for g in groups)}


def dunn_posthoc_test(all_scores: dict):
    """Dunn's post-hoc with Bonferroni correction."""
    models = [m for m in CORE_9 if m in all_scores]
    groups = [all_scores[m] for m in models]
    if len(groups) < 3:
        return None
    df = sp.posthoc_dunn(groups, p_adjust="bonferroni")
    df.index = [MODEL_SHORT.get(m, m) for m in models]
    df.columns = [MODEL_SHORT.get(m, m) for m in models]
    return df


def cohens_d_matrix(all_scores: dict):
    """Pairwise Cohen's d effect sizes."""
    models = sorted(all_scores.keys(), key=lambda m: all_scores[m].mean(), reverse=True)
    n = len(models)
    d_mat = np.zeros((n, n))
    names = [MODEL_SHORT.get(m, m) for m in models]

    for i, mi in enumerate(models):
        for j, mj in enumerate(models):
            if i == j:
                d_mat[i, j] = 0.0
                continue
            s1, s2 = all_scores[mi], all_scores[mj]
            n1, n2 = len(s1), len(s2)
            mean_diff = s1.mean() - s2.mean()
            pooled_std = np.sqrt(((n1 - 1) * s1.var() + (n2 - 1) * s2.var()) / (n1 + n2 - 2))
            d_mat[i, j] = mean_diff / pooled_std if pooled_std > 1e-12 else 0.0

    return d_mat, names, models


def spearman_correlation(all_scores: dict):
    """Spearman rank correlation matrix of per-question scores."""
    models = sorted(all_scores.keys(), key=lambda m: all_scores[m].mean(), reverse=True)
    n = len(models)
    corr = np.zeros((n, n))
    names = [MODEL_SHORT.get(m, m) for m in models]

    for i, mi in enumerate(models):
        for j, mj in enumerate(models):
            if i == j:
                corr[i, j] = 1.0
            elif i < j:
                r, _ = stats.spearmanr(all_scores[mi], all_scores[mj])
                corr[i, j] = corr[j, i] = r

    return corr, names


def per_dimension_kruskal(by_dim: dict):
    """K-W test per dimension."""
    results = {}
    for dim in DIMENSIONS:
        dim_groups = {}
        for m in CORE_9:
            if m in by_dim and by_dim[m].get(dim):
                dim_groups[m] = np.array(by_dim[m][dim])
        if len(dim_groups) >= 3:
            groups = list(dim_groups.values())
            H, p = stats.kruskal(*groups)
            means = {m: s.mean() for m, s in dim_groups.items()}
            best = max(means, key=means.get)
            worst = min(means, key=means.get)
            results[dim] = {
                "H": H, "p": p, "n_models": len(groups),
                "best_model": MODEL_SHORT.get(best, best),
                "best_mean": means[best],
                "worst_model": MODEL_SHORT.get(worst, worst),
                "worst_mean": means[worst],
                "spread": means[best] - means[worst],
            }
    return results


def per_difficulty_kruskal(by_diff: dict):
    """K-W test per difficulty level."""
    results = {}
    for lvl in DIFFICULTIES:
        lvl_groups = {}
        for m in CORE_9:
            if m in by_diff and by_diff[m].get(lvl):
                lvl_groups[m] = np.array(by_diff[m][lvl])
        if len(lvl_groups) >= 3:
            groups = list(lvl_groups.values())
            H, p = stats.kruskal(*groups)
            means = {m: s.mean() for m, s in lvl_groups.items()}
            results[lvl] = {
                "H": H, "p": p,
                "best_model": MODEL_SHORT.get(max(means, key=means.get), ""),
                "worst_model": MODEL_SHORT.get(min(means, key=means.get), ""),
                "spread": max(means.values()) - min(means.values()),
            }
    return results


# ═══════════════════════════════════════════════════════════════════
# Visualization
# ═══════════════════════════════════════════════════════════════════

def _save_fig(fig, name: str):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / name
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  → {path}")
    return path


def fig_overall_bar(all_scores: dict, dunn_df):
    """Fig 1: Overall scores with 95% CI + significance annotations."""
    models = sorted(all_scores.keys(), key=lambda m: all_scores[m].mean(), reverse=True)
    means = [all_scores[m].mean() for m in models]
    ses = [all_scores[m].std(ddof=1) / np.sqrt(len(all_scores[m])) for m in models]
    cis = [1.96 * se for se in ses]
    labels = [MODEL_SHORT.get(m, m) for m in models]
    families = [MODEL_FAMILY.get(m, "Other") for m in models]
    colors = [FAMILY_COLORS.get(f, "#888") for f in families]

    n = len(models)
    fig, ax = plt.subplots(figsize=(12, 6))
    y_pos = range(n)

    bars = ax.barh(y_pos, means, xerr=cis, color=colors, alpha=0.85,
                   capsize=3, edgecolor="white", linewidth=0.8)

    for i, (m, ci) in enumerate(zip(means, cis)):
        ax.text(m + ci + 0.003, i, f"{m:.4f}", va="center", fontsize=9, fontweight="bold")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlim(0, max(means) * 1.18)
    ax.set_xlabel("Overall Score", fontsize=11)
    ax.set_title("ControlSci: 9-Model Overall Scores (95% CI)", fontsize=13, fontweight="bold")
    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.3)

    legend_patches = [plt.Rectangle((0, 0), 1, 1, color=FAMILY_COLORS[f], alpha=0.85, label=f)
                      for f in ["MiMo", "DeepSeek", "Qwen", "MiniMax"]]
    ax.legend(handles=legend_patches, loc="lower right", fontsize=9, title="Family")

    fig.tight_layout()
    return _save_fig(fig, "fig1_overall_bar.png")


def fig_dimension_heatmap(dimension_means: dict, data: dict, per_dim_stats: dict):
    """Fig 2: Model × Dimension heatmap."""
    models = sorted(data.keys(), key=lambda m: data[m].get("overall_score", 0), reverse=True)
    mat = np.zeros((len(models), len(DIMENSIONS)))
    annot = []
    for i, m in enumerate(models):
        row = []
        for j, d in enumerate(DIMENSIONS):
            val = dimension_means[m].get(d, 0)
            mat[i, j] = val
            row.append(f"{val:.4f}")
        annot.append(row)

    labels = [MODEL_SHORT.get(m, m) for m in models]

    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(mat, annot=annot, fmt="", cmap="RdYlGn", vmin=0.15, vmax=0.80,
                xticklabels=DIMENSIONS, yticklabels=labels,
                linewidths=0.5, linecolor="white", cbar_kws={"label": "Score"},
                annot_kws={"fontsize": 9}, ax=ax)

    ax.set_title("Model × Dimension Score Heatmap", fontsize=13, fontweight="bold")
    ax.set_xlabel("Dimension", fontsize=11)
    ax.set_ylabel("Model", fontsize=11)

    for i, m in enumerate(models):
        best_dim = max(dimension_means[m], key=dimension_means[m].get)
        worst_dim = min(dimension_means[m], key=dimension_means[m].get)
        j_best = DIMENSIONS.index(best_dim)
        j_worst = DIMENSIONS.index(worst_dim)
        ax.add_patch(plt.Rectangle((j_best, i), 1, 1, fill=False, edgecolor="blue",
                                     lw=2.5, linestyle="-"))
        ax.add_patch(plt.Rectangle((j_worst, i), 1, 1, fill=False, edgecolor="red",
                                     lw=2.5, linestyle="--"))

    # Significance from per_dim_stats
    sig_notes = []
    for d in DIMENSIONS:
        if d in per_dim_stats:
            s = per_dim_stats[d]
            sig_notes.append(f"{d}: H={s['H']:.1f}, p={s['p']:.4f}")
    if sig_notes:
        fig.text(0.5, -0.02, "K-W: " + " | ".join(sig_notes),
                 ha="center", fontsize=8, style="italic")

    fig.tight_layout()
    return _save_fig(fig, "fig2_dimension_heatmap.png")


def fig_difficulty_boxplot(by_diff: dict, data: dict):
    """Fig 3: Difficulty-level boxplot (all models)."""
    models = sorted(data.keys(), key=lambda m: data[m].get("overall_score", 0), reverse=True)
    labels = [MODEL_SHORT.get(m, m) for m in models]

    n_rows = 3
    n_cols = 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 14), sharey=True)
    fig.suptitle("Score Distribution by Difficulty Level × Model", fontsize=14, fontweight="bold")

    for idx, model in enumerate(models):
        row, col = divmod(idx, n_cols)
        ax = axes[row, col]
        data_list = [by_diff[model].get(lvl, [0]) for lvl in DIFFICULTIES]

        bp = ax.boxplot(data_list, tick_labels=DIFFICULTIES, patch_artist=True,
                         widths=0.5, showmeans=True,
                         meanprops={"marker": "D", "markerfacecolor": "red", "markersize": 5})
        colors = ["#c6dbef", "#6baed6", "#3182bd", "#08519c"]
        for patch, color in zip(bp["boxes"], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        ax.set_title(labels[idx], fontsize=10, fontweight="bold")
        ax.set_ylim(-0.05, 1.1)
        ax.grid(axis="y", alpha=0.3)
        if col == 0:
            ax.set_ylabel("Score", fontsize=9)

    fig.tight_layout()
    return _save_fig(fig, "fig3_difficulty_boxplot.png")


def fig_cohens_d_heatmap(d_mat: np.ndarray, names: list, models: list):
    """Fig 4: Cohen's d pairwise matrix."""
    mask = np.triu(np.ones_like(d_mat, dtype=bool), k=1)

    fig, ax = plt.subplots(figsize=(11, 9))
    annot = np.empty_like(d_mat, dtype=object)
    for i in range(len(names)):
        for j in range(len(names)):
            annot[i, j] = f"{d_mat[i, j]:.3f}" if i != j else "—"

    sns.heatmap(d_mat, annot=annot, fmt="", cmap="RdBu_r", center=0,
                vmin=-0.8, vmax=0.8, mask=mask,
                xticklabels=names, yticklabels=names,
                linewidths=0.3, cbar_kws={"label": "Cohen's d"},
                annot_kws={"fontsize": 8}, ax=ax)

    ax.set_title("Pairwise Cohen's d Effect Sizes (Row > Column = Row wins)",
                 fontsize=12, fontweight="bold")
    ax.tick_params(axis="x", rotation=45)
    ax.tick_params(axis="y", rotation=0)
    fig.tight_layout()
    return _save_fig(fig, "fig4_cohens_d.png")


def fig_correlation_clustermap(corr: np.ndarray, names: list):
    """Fig 5: Spearman correlation + hierarchical clustering."""
    # Use seaborn clustermap for dendrogram
    cg = sns.clustermap(corr, annot=True, fmt=".3f", cmap="coolwarm",
                         vmin=0.6, vmax=1.0, method="average",
                         xticklabels=names, yticklabels=names,
                         figsize=(10, 9), linewidths=0.3,
                         annot_kws={"fontsize": 9},
                         dendrogram_ratio=0.12,
                         cbar_kws={"label": "Spearman ρ"})
    cg.ax_heatmap.set_title("Model Score Correlation + Hierarchical Clustering",
                             fontsize=12, fontweight="bold", pad=20)
    cg.ax_heatmap.tick_params(axis="x", rotation=45)
    cg.fig.tight_layout()
    path = OUTPUT_DIR / "fig5_correlation_cluster.png"
    cg.fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(cg.fig)
    print(f"  → {path}")
    return path


def fig_per_difficulty_line(by_diff: dict, data: dict):
    """Fig 6: Difficulty-sensitivity curves."""
    models = sorted(data.keys(), key=lambda m: data[m].get("overall_score", 0), reverse=True)
    families = [MODEL_FAMILY.get(m, "Other") for m in models]
    labels = [MODEL_SHORT.get(m, m) for m in models]

    fig, ax = plt.subplots(figsize=(11, 7))

    for m, fam, lbl in zip(models, families, labels):
        means = [np.mean(by_diff[m].get(lvl, [0])) for lvl in DIFFICULTIES]
        color = FAMILY_COLORS.get(fam, "#888")
        lw = 2.0 if m in ("mimo-v2-flash", "deepseek-v4-flash", "qwen3.5:9b") else 1.2
        ls = "-" if lw > 1.5 else "--"
        ax.plot(DIFFICULTIES, means, marker="o", label=lbl, color=color,
                linewidth=lw, linestyle=ls, markersize=6 if lw > 1.5 else 4)

    ax.set_ylim(0, 1)
    ax.set_xlabel("Difficulty Level", fontsize=11)
    ax.set_ylabel("Mean Score", fontsize=11)
    ax.set_title("Difficulty-Sensitivity Curves: How Scores Decay with Difficulty",
                 fontsize=12, fontweight="bold")
    ax.legend(loc="lower left", fontsize=8, ncol=2, title="Model", title_fontsize=9)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    return _save_fig(fig, "fig6_difficulty_curves.png")


def fig_model_radar(data: dict):
    """Fig 7: Radar profile for each model (3×3 subplot)."""
    models = sorted(data.keys(), key=lambda m: data[m].get("overall_score", 0), reverse=True)
    labels = [MODEL_SHORT.get(m, m) for m in models]

    angles = np.linspace(0, 2 * np.pi, len(DIMENSIONS), endpoint=False).tolist()
    angles += angles[:1]

    fig, axes = plt.subplots(3, 3, figsize=(15, 15), subplot_kw={"projection": "polar"})
    fig.suptitle("Model Dimension Profiles (Radar)", fontsize=14, fontweight="bold")

    for idx, (model, ax) in enumerate(zip(models, axes.flat)):
        dim_scores = data[model].get("dimension_scores", {})
        values = [dim_scores.get(d, 0) for d in DIMENSIONS]
        values += values[:1]

        family = MODEL_FAMILY.get(model, "Other")
        color = FAMILY_COLORS.get(family, "#888")

        ax.fill(angles, values, alpha=0.25, color=color)
        ax.plot(angles, values, color=color, linewidth=2)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(DIMENSIONS, fontsize=9)
        ax.set_ylim(0, 0.85)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8])
        ax.set_yticklabels(["0.2", "0.4", "0.6", "0.8"], fontsize=7)
        ax.set_title(labels[idx], fontsize=10, fontweight="bold", pad=15)
        ax.grid(alpha=0.4)

    fig.tight_layout()
    return _save_fig(fig, "fig7_model_radar.png")


# ═══════════════════════════════════════════════════════════════════
# Report Generation
# ═══════════════════════════════════════════════════════════════════

def _sig_stars(p: float) -> str:
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    if p < 0.10:
        return "†"
    return "ns"


def _d_interpret(d: float) -> str:
    ad = abs(d)
    if ad < 0.2:
        return "negligible"
    if ad < 0.5:
        return "small"
    if ad < 0.8:
        return "medium"
    return "large"


def _model_rank_desc(rank: int, name: str, overall: float, d_mat, names_all, models_all):
    """Rich model description line."""
    idx = models_all.index(name)
    strengths = d_mat[idx] > 0.3
    weakness = d_mat[idx] < -0.3
    n_beats = int(np.sum(strengths))
    n_beaten = int(np.sum(weakness))
    return f"  beats {n_beats}/8 with d>0.3, loses to {n_beaten}/8"


def render_markdown(data, all_scores, by_dim, by_diff, dimension_means,
                    kw_result, dunn_df, d_mat, names_d, models_d,
                    corr, names_corr, per_dim_kw, per_diff_kw):
    """Generate comprehensive Markdown report."""
    md = []
    md.append("# T2: 9-Model Deep Analysis Report")
    md.append("")
    md.append(f"**Generated:** 2026-05-06 | **Models:** 9 | **Questions per model:** 500")
    md.append("")
    md.append("---")
    md.append("")

    # ── Executive Summary ──
    md.append("## 1. Executive Summary")
    md.append("")

    models_sorted = sorted(data.keys(), key=lambda m: data[m].get("overall_score", 0), reverse=True)

    md.append("| Rank | Model | Overall | A | B | C | D | Family |")
    md.append("|------|-------|---------|----|----|----|----|--------|")
    for rank, m in enumerate(models_sorted, 1):
        d = data[m]
        ov = d.get("overall_score", 0)
        ds = d.get("dimension_scores", {})
        fam = MODEL_FAMILY.get(m, "—")
        md.append(f"| {rank} | {MODEL_SHORT.get(m, m)} | **{ov:.4f}** | "
                  f"{ds.get('A', 0):.4f} | {ds.get('B', 0):.4f} | "
                  f"{ds.get('C', 0):.4f} | {ds.get('D', 0):.4f} | {fam} |")
    md.append("")

    top = models_sorted[0]
    bottom = models_sorted[-1]
    top_ov = data[top].get("overall_score", 0)
    bottom_ov = data[bottom].get("overall_score", 0)
    md.append(f"**Winner:** {MODEL_SHORT[top]} ({top_ov:.4f}) "
              f"— {top_ov - bottom_ov:.4f} ahead of last place ({bottom_ov:.4f}).")
    md.append("")

    # ── Statistical Tests ──
    md.append("## 2. Statistical Inference")
    md.append("")

    if kw_result:
        kw = kw_result
        md.append(f"**Kruskal-Wallis Test** (non-parametric ANOVA):")
        md.append(f"- H = {kw['H']:.2f}, df = {kw['df']}, p = {kw['p']:.6f} {_sig_stars(kw['p'])}")
        md.append(f"- n = {kw['n_models']} models × {kw['n_total'] // kw['n_models']} records = {kw['n_total']} total")
        conclusion = "significant differences exist among models" if kw["p"] < 0.05 else "no significant differences (p ≥ 0.05)"
        md.append(f"- Conclusion: **{conclusion}**.")
        md.append("")

    md.append("### 2.1 Dunn's Post-Hoc (Bonferroni corrected)")
    md.append("")
    if dunn_df is not None:
        md.append("Significant pairwise comparisons (p < 0.05):")
        md.append("")
        md.append("| Comparison | p-value | Significance |")
        md.append("|-----------|---------|-------------|")
        sig_count = 0
        n_models = len(dunn_df)
        for i in range(n_models):
            for j in range(i + 1, n_models):
                p_val = dunn_df.iloc[i, j]
                if p_val < 0.05:
                    sig_count += 1
                    md.append(f"| {dunn_df.index[i]} vs {dunn_df.columns[j]} | {p_val:.6f} | {_sig_stars(p_val)} |")
        md.append("")
        md.append(f"**{sig_count}** significant pairs out of {n_models * (n_models - 1) // 2} total comparisons.")
        md.append("")
    else:
        md.append("*Dunn's test skipped — fewer than 3 models loaded.*")
        md.append("")

    md.append("### 2.2 Cohen's d Effect Sizes (Top vs Others)")
    md.append("")
    md.append(f"Reference model: **{names_d[0]}** (rank 1)")
    md.append("")
    md.append("| vs Model | Cohen's d | Interpretation |")
    md.append("|----------|----------|----------------|")
    for j in range(1, len(names_d)):
        d_val = d_mat[0, j]
        md.append(f"| {names_d[j]} | {d_val:+.3f} | {_d_interpret(d_val)} |")
    md.append("")

    # ── Dimension Analysis ──
    md.append("## 3. Per-Dimension Analysis")
    md.append("")
    md.append("### 3.1 Dimension-wise Kruskal-Wallis")
    md.append("")
    md.append("| Dimension | H | p | Best | Best Mean | Worst | Worst Mean | Spread |")
    md.append("|-----------|----|----|------|-----------|-------|-----------|--------|")
    for d in DIMENSIONS:
        if d in per_dim_kw:
            s = per_dim_kw[d]
            md.append(f"| {d} | {s['H']:.1f} | {s['p']:.4f} {_sig_stars(s['p'])} | "
                      f"{s['best_model']} | {s['best_mean']:.4f} | "
                      f"{s['worst_model']} | {s['worst_mean']:.4f} | {s['spread']:.4f} |")
    md.append("")

    md.append("### 3.2 Model Dimension Profiles")
    md.append("")
    for m in models_sorted:
        ds = data[m].get("dimension_scores", {})
        all_dims = [(d, ds.get(d, 0)) for d in DIMENSIONS]
        best = max(all_dims, key=lambda x: x[1])
        worst = min(all_dims, key=lambda x: x[1])
        md.append(f"- **{MODEL_SHORT[m]}** (Overall: {data[m].get('overall_score', 0):.4f}): "
                  f"Best in {best[0]} ({best[1]:.4f}), weakest in {worst[0]} ({worst[1]:.4f}) "
                  f"| Spread: {best[1] - worst[1]:.4f}")
    md.append("")

    # ── Difficulty Analysis ──
    md.append("## 4. Difficulty-Level Analysis")
    md.append("")
    md.append("### 4.1 Difficulty-wise Kruskal-Wallis")
    md.append("")
    md.append("| Difficulty | H | p | Best | Worst | Spread |")
    md.append("|-----------|----|----|------|-------|--------|")
    for lvl in DIFFICULTIES:
        if lvl in per_diff_kw:
            s = per_diff_kw[lvl]
            md.append(f"| {lvl} | {s['H']:.1f} | {s['p']:.4f} {_sig_stars(s['p'])} | "
                      f"{s['best_model']} | {s['worst_model']} | {s['spread']:.4f} |")
    md.append("")

    md.append("### 4.2 Difficulty Decay Rates")
    md.append("")
    md.append("| Model | L1 Mean | L4 Mean | Decay (L1→L4) | Sensitivity |")
    md.append("|-------|---------|---------|---------------|-------------|")
    decay_rates = []
    for m in models_sorted:
        l1_m = np.mean(by_diff[m].get("L1", [0]))
        l4_m = np.mean(by_diff[m].get("L4", [0]))
        decay = l1_m - l4_m
        sensitivity = decay / l1_m if l1_m > 0 else 0
        decay_rates.append((m, decay, sensitivity))
        md.append(f"| {MODEL_SHORT[m]} | {l1_m:.4f} | {l4_m:.4f} | {decay:+.4f} | {sensitivity:.1%} |")
    md.append("")

    most_stable = min(decay_rates, key=lambda x: x[1])
    most_sensitive = max(decay_rates, key=lambda x: x[1])
    md.append(f"- **Most stable** across difficulty: {MODEL_SHORT[most_stable[0]]} (decay = {most_stable[1]:+.4f})")
    md.append(f"- **Most sensitive** to difficulty: {MODEL_SHORT[most_sensitive[0]]} (decay = {most_sensitive[1]:+.4f})")
    md.append("")

    # ── Correlation ──
    md.append("## 5. Model Score Correlation")
    md.append("")
    md.append(f"Mean pairwise Spearman ρ: **{np.mean(corr[np.triu_indices_from(corr, k=1)]):.4f}**")
    md.append("")
    md.append("| Model Pair | ρ | Strength |")
    md.append("|-----------|------|----------|")
    for i in range(len(names_corr)):
        for j in range(i + 1, len(names_corr)):
            r = corr[i, j]
            strength = "Very Strong" if r > 0.8 else "Strong" if r > 0.6 else "Moderate" if r > 0.4 else "Weak"
            md.append(f"| {names_corr[i]} ↔ {names_corr[j]} | {r:.3f} | {strength} |")
    md.append("")

    # ── Issue Patterns ──
    md.append("## 6. Cross-Model Issue Patterns")
    md.append("")
    all_issues = Counter()
    model_issue_counts = {}
    for m in models_sorted:
        issues = Counter()
        for rec in data[m].get("records", []):
            for iss in (rec.get("issues") or []):
                issues[iss] += 1
        model_issue_counts[m] = issues
        all_issues.update(issues)

    md.append("### 6.1 Top-10 Issues (Aggregated)")
    md.append("")
    md.append("| Rank | Issue | Total Count | Models Affected |")
    md.append("|------|-------|-------------|-----------------|")
    for rank, (iss, cnt) in enumerate(all_issues.most_common(10), 1):
        affected = sum(1 for m in models_sorted if iss in model_issue_counts[m])
        md.append(f"| {rank} | {iss} | {cnt} | {affected}/9 |")
    md.append("")

    # ── Charts ──
    md.append("## 7. Generated Charts")
    md.append("")
    charts = [
        ("Overall Score Bar Chart (95% CI)", "fig1_overall_bar.png"),
        ("Model × Dimension Heatmap", "fig2_dimension_heatmap.png"),
        ("Difficulty-Level Boxplots", "fig3_difficulty_boxplot.png"),
        ("Cohen's d Pairwise Matrix", "fig4_cohens_d.png"),
        ("Score Correlation + Hierarchical Clustering", "fig5_correlation_cluster.png"),
        ("Difficulty-Sensitivity Curves", "fig6_difficulty_curves.png"),
        ("Model Dimension Radar Profiles", "fig7_model_radar.png"),
    ]
    for title, fname in charts:
        md.append(f"- **{title}**: `{fname}`")
    md.append("")

    # ── Methodology ──
    md.append("## 8. Methodology Notes")
    md.append("")
    md.append("- **Kruskal-Wallis**: Non-parametric alternative to one-way ANOVA; does not assume normality.")
    md.append("- **Dunn's Post-hoc**: Multiple comparison correction via Bonferroni; identifies _which_ pairs differ.")
    md.append("- **Cohen's d**: Pooled standard deviation; thresholds: small (0.2), medium (0.5), large (0.8).")
    md.append("- **Spearman ρ**: Rank correlation; robust to non-linear monotonic relationships.")
    md.append("- **Hierarchical Clustering**: Average linkage on (1 − ρ) distance matrix.")
    md.append("- **95% CI**: ±1.96 × SE; assumes asymptotic normality (n=500, CLT applies).")
    md.append("")

    return "\n".join(md)


# ═══════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════

def main():
    import argparse
    global OUTPUT_DIR
    parser = argparse.ArgumentParser(description="T2: 9-Model Deep Analysis")
    parser.add_argument("--reports", default=str(ROOT / "benchmark" / "eval" / "reports"),
                        help="Directory containing *_report.json files")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR),
                        help="Output directory for charts and report")
    parser.add_argument("--no-charts", action="store_true", help="Skip chart generation")
    parser.add_argument("--report-only", action="store_true", help="Only generate the Markdown report")
    args = parser.parse_args()

    OUTPUT_DIR = Path(args.output_dir)

    print("=" * 60)
    print("T2: 9-Model Deep Analysis")
    print("=" * 60)

    # 1. Load data
    print("\n[1/5] Loading 9 model reports...")
    data = load_core_9(args.reports)
    if len(data) < 3:
        print(f"ERROR: Only {len(data)} models loaded, need ≥ 3.  Exiting.")
        return 1
    print(f"  Loaded {len(data)} models: {', '.join(MODEL_SHORT.get(m, m) for m in data)}")

    # 2. Extract records
    print("\n[2/5] Extracting records...")
    all_scores, by_dim, by_diff, dimension_means = extract_records(data)
    for m in sorted(data.keys(), key=lambda x: all_scores[x].mean(), reverse=True):
        print(f"  {MODEL_SHORT[m]}: overall={all_scores[m].mean():.4f}, "
              f"n={len(all_scores[m])}")

    # 3. Statistical tests
    print("\n[3/5] Running statistical tests...")

    kw = kruskal_wallis_test(all_scores)
    if kw:
        print(f"  Kruskal-Wallis: H={kw['H']:.2f}, p={kw['p']:.6f} {_sig_stars(kw['p'])}")

    dunn_df = dunn_posthoc_test(all_scores)
    if dunn_df is not None:
        sig_pairs = 0
        for i in range(len(dunn_df)):
            for j in range(i + 1, len(dunn_df)):
                if dunn_df.iloc[i, j] < 0.05:
                    sig_pairs += 1
        print(f"  Dunn's post-hoc: {sig_pairs} significant pairs (Bonferroni corrected)")

    d_mat, names_d, models_d = cohens_d_matrix(all_scores)
    top_vs_second = abs(d_mat[0, 1])
    print(f"  Cohen's d (top vs #2): {d_mat[0, 1]:+.3f} ({_d_interpret(d_mat[0, 1])})")

    corr, names_corr = spearman_correlation(all_scores)
    mean_corr = np.mean(corr[np.triu_indices_from(corr, k=1)])
    print(f"  Mean Spearman ρ: {mean_corr:.4f}")

    per_dim_kw = per_dimension_kruskal(by_dim)
    for d in DIMENSIONS:
        if d in per_dim_kw:
            s = per_dim_kw[d]
            print(f"  K-W Dim {d}: H={s['H']:.1f}, p={s['p']:.4f} {_sig_stars(s['p'])}, "
                  f"best={s['best_model']}({s['best_mean']:.3f}), spread={s['spread']:.3f}")

    per_diff_kw = per_difficulty_kruskal(by_diff)
    for lvl in DIFFICULTIES:
        if lvl in per_diff_kw:
            s = per_diff_kw[lvl]
            print(f"  K-W {lvl}: H={s['H']:.1f}, p={s['p']:.4f} {_sig_stars(s['p'])}, "
                  f"best={s['best_model']}, spread={s['spread']:.3f}")

    # 4. Visualizations
    if not args.report_only:
        print("\n[4/5] Generating charts...")
        if not args.no_charts:
            fig_overall_bar(all_scores, dunn_df)
            fig_dimension_heatmap(dimension_means, data, per_dim_kw)
            fig_difficulty_boxplot(by_diff, data)
            fig_cohens_d_heatmap(d_mat, names_d, models_d)
            fig_correlation_clustermap(corr, names_corr)
            fig_per_difficulty_line(by_diff, data)
            fig_model_radar(data)
            print("  All 7 charts generated.")
        else:
            print("  Charts skipped (--no-charts).")
    else:
        print("\n[4/5] Charts skipped (--report-only).")

    # 5. Report
    print("\n[5/5] Generating Markdown report...")
    md = render_markdown(data, all_scores, by_dim, by_diff, dimension_means,
                          kw, dunn_df, d_mat, names_d, models_d,
                          corr, names_corr, per_dim_kw, per_diff_kw)
    report_path = OUTPUT_DIR / "t2_deep_analysis.md"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report_path.write_text(md, encoding="utf-8")
    print(f"  Report: {report_path}")

    print(f"\n{'=' * 60}")
    print("T2 analysis complete.")
    print(f"Output: {OUTPUT_DIR}")
    print(f"{'=' * 60}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
