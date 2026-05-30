from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


repo = Path(__file__).resolve().parents[1]
out_dirs = [
    repo / "docs" / "submissions" / "shared" / "assets" / "task1",
    repo / "_final_submission_by_track" / "track1_sci_align" / "shared" / "assets",
]

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "axes.edgecolor": "#D0D7DE",
        "axes.linewidth": 0.8,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)

navy = "#0B1F3A"
blue = "#2563EB"
cyan = "#0891B2"
green = "#059669"
orange = "#D97706"
red = "#DC2626"
gray = "#64748B"
light = "#F8FAFC"
line = "#D6E0EA"
academic_accent = "#3B5B78"
academic_muted = "#8DA2B6"
academic_good = "#477A64"
academic_warn = "#9A6A32"
academic_red = "#9B3A3A"
academic_fill = "#F7F9FB"


def save_all(fig, name):
    for out_dir in out_dirs:
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / name, dpi=220, bbox_inches="tight", pad_inches=0.22)
    plt.close(fig)


def title(ax, text, subtitle):
    ax.text(0.03, 0.96, text, fontsize=22, fontweight="bold", color=navy, va="top")
    ax.text(0.03, 0.915, subtitle, fontsize=11, color=gray, va="top")


def row_box(ax, y, number, label, metric, evidence, boundary, color):
    row_h = 0.066
    ax.add_patch(
        FancyBboxPatch(
            (0.045, y),
            0.91,
            row_h,
            boxstyle="round,pad=0.006,rounding_size=0.014",
            linewidth=1,
            edgecolor=line,
            facecolor="white",
        )
    )
    ax.add_patch(Rectangle((0.045, y), 0.006, row_h, linewidth=0, facecolor=color, alpha=0.75))
    mid_y = y + row_h / 2
    ax.text(0.075, mid_y, f"{number:02d}", fontsize=12.5, fontweight="bold", color=academic_accent, va="center")
    ax.text(0.135, mid_y, label, fontsize=11.4, fontweight="bold", color=navy, va="center")
    ax.text(0.355, mid_y, metric, fontsize=14.0, fontweight="bold", color=academic_accent, va="center")
    ax.text(0.515, mid_y, evidence, fontsize=9.8, color="#334155", va="center")
    ax.text(0.745, mid_y, boundary, fontsize=9.0, color=gray, va="center")


def generate_sciverse_dashboard():
    fig, ax = plt.subplots(figsize=(15.5, 9.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    title(ax, "Sciverse External Validation Summary", "External-source stress test with fixed schema, audit rubric, and evaluation entry")

    ax.text(0.075, 0.810, "Stage", fontsize=10, fontweight="bold", color=gray)
    ax.text(0.360, 0.810, "Metric", fontsize=10, fontweight="bold", color=gray)
    ax.text(0.520, 0.810, "Evidence", fontsize=10, fontweight="bold", color=gray)
    ax.text(0.750, 0.810, "Boundary", fontsize=10, fontweight="bold", color=gray)

    rows = [
        ("Coverage", "14/14", "Control subfields covered", "minimum > 3.5M records", academic_accent),
        ("Search Relevance", "10/10", "Agentic-search probes", "average score 0.978", academic_muted),
        ("Full-Text Parsing", "14/14", "1,417 formulas; 46 image refs", "sampled full-text pull", academic_good),
        ("Image Audit", "90.3%", "84/93 images consistent", "MiMo visual audit", academic_warn),
        ("Cross-Source Evaluation", "+0.108", "Sciverse vs arXiv judge delta", "content effect, not bias claim", academic_accent),
        ("Leaderboard Consistency", "order kept", "35B > 9B > 4B", "30 Sciverse questions", academic_muted),
        ("Training Utility", "PPL -78.3%", "Sciverse QLoRA ablation", "not reasoning gain", academic_good),
    ]
    y = 0.720
    for i, (label, metric, evidence, boundary, color) in enumerate(rows, start=1):
        row_box(ax, y, i, label, metric, evidence, boundary, color)
        y -= 0.083

    ax.add_patch(
        FancyBboxPatch(
            (0.06, 0.055),
            0.88,
            0.065,
            boxstyle="round,pad=0.014,rounding_size=0.018",
            linewidth=1,
            edgecolor=line,
            facecolor=academic_fill,
        )
    )
    ax.text(0.085, 0.088, "Note", fontsize=10.8, fontweight="bold", color=navy, va="center")
    ax.text(0.145, 0.088, "Evidence only; not a reasoning-improvement claim.", fontsize=10.0, color=academic_red, va="center", fontweight="bold")
    save_all(fig, "track1_sciverse_validation_dashboard.png")


def generate_supplemental_matrix():
    fig, ax = plt.subplots(figsize=(15.5, 9.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    title(ax, "Track 1 Supplemental Evidence Matrix", "Seven closure checks for consumability, traceability, conversion, training utility, and review boundaries")

    ax.add_patch(Rectangle((0.045, 0.825), 0.91, 0.045, linewidth=0, facecolor="#25384D"))
    ax.text(0.075, 0.848, "Check", fontsize=10, fontweight="bold", color="white", va="center")
    ax.text(0.300, 0.848, "Key Result", fontsize=10, fontweight="bold", color="white", va="center")
    ax.text(0.520, 0.848, "Evidence", fontsize=10, fontweight="bold", color="white", va="center")
    ax.text(0.750, 0.848, "Boundary", fontsize=10, fontweight="bold", color="white", va="center")

    rows = [
        ("AI-Ready Consumption", "500 core; 889 full", "required fields coverage = 1.0", "local JSON smoke only", academic_accent),
        ("Integrity & Traceability", "0 issues", "all required fields and refs pass", "local index resolution only", academic_good),
        ("Multimodal Taxonomy", "20 samples; 7 causes", "consistent 10; inconsistent 9; partial 1", "replay audit; no new VLM calls", academic_warn),
        ("Dimension Discriminability", "D/C > A/B", "dimension range separates hard tasks", "aggregate range; no item-level test", academic_muted),
        ("Training Utility Boundary", "PPL -78.3%", "Base 19.8 -> QLoRA 4.3", "reasoning delta tracked separately", academic_good),
        ("Export Format Compatibility", "4 formats; fields=100%", "OpenAI/HF/QA/ChatML", "compatibility, not certification", academic_accent),
        ("Sample Review Consistency", "30 samples; bucket .7345", "judge replay", "small replay; no human review", academic_good),
    ]
    y = 0.735
    for idx, (label, metric, evidence, boundary, color) in enumerate(rows, start=1):
        fill = "white" if idx % 2 else academic_fill
        ax.add_patch(Rectangle((0.045, y), 0.91, 0.073, linewidth=0, facecolor=fill))
        ax.add_patch(Rectangle((0.045, y), 0.005, 0.073, linewidth=0, facecolor=color, alpha=0.75))
        ax.text(0.075, y + 0.037, label, fontsize=10.7, fontweight="bold", color=navy, va="center")
        metric_size = 11.0 if label == "Sample Review Consistency" else 12.4
        ax.text(0.300, y + 0.037, metric, fontsize=metric_size, fontweight="bold", color=academic_accent, va="center")
        ax.text(0.520, y + 0.037, evidence, fontsize=9.7, color="#334155", va="center")
        ax.text(0.750, y + 0.037, boundary, fontsize=9.2, color=gray, va="center")
        ax.add_line(plt.Line2D([0.045, 0.955], [y, y], color=line, linewidth=0.8))
        y -= 0.078
    ax.add_line(plt.Line2D([0.045, 0.955], [y + 0.078, y + 0.078], color=line, linewidth=0.8))

    ax.add_patch(
        FancyBboxPatch(
            (0.06, 0.075),
            0.88,
            0.105,
            boxstyle="round,pad=0.014,rounding_size=0.018",
            linewidth=1,
            edgecolor=line,
            facecolor=academic_fill,
        )
    )
    ax.text(0.085, 0.135, "Closure Principle", fontsize=11.5, fontweight="bold", color=navy, va="center")
    ax.text(0.230, 0.135, "Each row validates one delivery property and records one explicit boundary.", fontsize=10.2, color="#334155", va="center")
    ax.text(0.230, 0.100, "Boundaries are evidence, not caveats to hide.", fontsize=10.2, color=academic_red, va="center", fontweight="bold")
    save_all(fig, "track1_supplemental_evidence_matrix.png")


def generate_training_ablation():
    fig = plt.figure(figsize=(13.4, 7.2))
    fig.text(0.06, 0.930, "Training Utility Boundary Check", fontsize=20, color=navy, fontweight="bold", va="top")
    fig.text(0.06, 0.875, "Language-model fit and reasoning score are reported as separate evidence channels", fontsize=11, color=gray, va="top")

    fig.text(0.08, 0.790, "PPL fit probe", fontsize=13, color=navy, fontweight="bold", va="top")
    fig.text(0.08, 0.750, "139 Sciverse validation segments; lower is better", fontsize=9.5, color=gray, va="top")
    fig.text(0.08, 0.718, "Observed PPL: 19.8 -> 4.3  (delta -15.5; -78.3%)", fontsize=9.8, color="#334155", va="top")
    fig.text(0.595, 0.790, "Reasoning score check", fontsize=13, color=navy, fontweight="bold", va="top")
    fig.text(0.595, 0.750, "89 QA hold-out items; observed delta -0.0034", fontsize=9.5, color=gray, va="top")

    ppl_ax = fig.add_axes([0.08, 0.265, 0.42, 0.400])
    score_ax = fig.add_axes([0.595, 0.315, 0.32, 0.310])
    note_ax = fig.add_axes([0.06, 0.070, 0.88, 0.120])
    note_ax.axis("off")

    labels = ["Base 4B", "Sciverse-QLoRA 4B"]
    values = [19.8, 4.3]
    colors = ["#94A3B8", green]
    bars = ppl_ax.bar(labels, values, color=colors, width=0.58, edgecolor="white", linewidth=1.5)
    ppl_ax.set_ylabel("Perplexity", fontsize=10.5, color="#334155")
    ppl_ax.set_ylim(0, 22)
    ppl_ax.grid(axis="y", color="#E2E8F0", linewidth=1)
    ppl_ax.set_axisbelow(True)
    for spine in ["top", "right"]:
        ppl_ax.spines[spine].set_visible(False)
    for bar, value in zip(bars, values):
        ppl_ax.text(bar.get_x() + bar.get_width() / 2, value + 0.55, f"{value:.1f}", ha="center", va="bottom", fontsize=12.5, fontweight="bold", color=navy)
    score_labels = ["Baseline judge", "QLoRA judge"]
    score_values = [0.4669, 0.4635]
    score_colors = ["#94A3B8", "#FCA5A5"]
    score_ax.barh(score_labels, score_values, color=score_colors, height=0.42, edgecolor="white", linewidth=1.4)
    score_ax.set_xlim(0, 1.0)
    score_ax.set_xticks([0.0, 0.5, 1.0])
    score_ax.grid(axis="x", color="#E2E8F0", linewidth=1)
    score_ax.set_axisbelow(True)
    score_ax.invert_yaxis()
    for spine in ["top", "right", "left"]:
        score_ax.spines[spine].set_visible(False)
    score_ax.tick_params(axis="y", length=0)
    for y_pos, value in enumerate(score_values):
        score_ax.text(value + 0.018, y_pos, f"{value:.4f}", va="center", fontsize=10.5, color=navy, fontweight="bold")
    note_ax.add_patch(
        FancyBboxPatch(
            (0, 0),
            1,
            1,
            transform=note_ax.transAxes,
            boxstyle="round,pad=0.014,rounding_size=0.025",
            linewidth=1.0,
            edgecolor=line,
            facecolor=light,
        )
    )
    note_ax.text(0.035, 0.62, "Supported claim", transform=note_ax.transAxes, fontsize=10.8, color=navy, fontweight="bold", va="center")
    note_ax.text(0.180, 0.62, "Sciverse paragraphs are trainable and reduce in-domain PPL.", transform=note_ax.transAxes, fontsize=10.2, color="#334155", va="center")
    note_ax.text(0.035, 0.32, "Boundary", transform=note_ax.transAxes, fontsize=10.8, color=red, fontweight="bold", va="center")
    note_ax.text(0.180, 0.32, "Do not infer general reasoning improvement from PPL; judge score is tracked separately.", transform=note_ax.transAxes, fontsize=10.2, color="#334155", va="center")
    save_all(fig, "track1_training_utility_ablation.png")


if __name__ == "__main__":
    generate_sciverse_dashboard()
    generate_supplemental_matrix()
    generate_training_ablation()
