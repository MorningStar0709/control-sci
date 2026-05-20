import json
import sys
from pathlib import Path
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import FancyBboxPatch

mpl.rcParams['font.family'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
mpl.rcParams['axes.unicode_minus'] = False

BASE = Path(__file__).resolve().parents[2]
ANSWER_PATH = BASE / "benchmark/eval/results/leaderboard_complete.json"
JUDGE_API_PATH = BASE / "benchmark/eval/results/judge_matrix/api_8judge_consolidated.json"
JUDGE_LOCAL_PATH = BASE / "benchmark/eval/results/judge_matrix/local_6judge_consolidated.json"
OUTPUT = BASE / "docs/assets/dual_role_matrix.png"


FAMILY_COLORS = {
    "DeepSeek": "#1A5276",
    "MiniMax": "#1E8449",
    "MiMo": "#B9770E",
    "Qwen": "#C0392B",
}
FAMILY_MARKERS = {
    "DeepSeek": "o",
    "MiniMax": "^",
    "MiMo": "s",
    "Qwen": "D",
}


def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def normalize(name):
    return name.lower().replace("-", "").replace("_", "").replace(".", "").replace(":", "")


def detect_family(display_name):
    for fam in ["DeepSeek", "MiniMax", "MiMo", "Qwen"]:
        if display_name.lower().startswith(fam.lower()):
            return fam
    return "Other"


def shorten_name(name):
    return name.replace("-highspeed", "").replace("deepseek", "DS", 1).replace(
        "DeepSeek", "DS").replace("MiniMax", "MM").replace("MiMo", "MiMo")


def main():
    answer_data = load_json(ANSWER_PATH)
    judge_api = load_json(JUDGE_API_PATH)
    judge_local = load_json(JUDGE_LOCAL_PATH)

    answer_map = {}
    for m in answer_data["models"]:
        key = normalize(m["model"])
        answer_map[key] = m

    judge_map = {}
    for mname in judge_api["models"]:
        key = normalize(mname)
        judge_map[key] = {
            "display": mname,
            "mean": judge_api["summary_statistics"][mname]["mean"]
        }

    overlaps = []
    answer_only = []
    for norm_name, m in answer_map.items():
        if norm_name in judge_map:
            overlaps.append({
                "display": m["model"],
                "answer_score": m["overall_score"],
                "judge_mean": judge_map[norm_name]["mean"],
                "family": detect_family(m["model"]),
            })
        else:
            answer_only.append(m)

    overlaps.sort(key=lambda x: x["answer_score"], reverse=True)

    print(f"Overlapping models (Answerer ∩ Judge): {len(overlaps)}")
    for o in overlaps:
        print(f"  {o['display']:30s}  family={o['family']:8s}  "
              f"answer={o['answer_score']:.4f}  judge={o['judge_mean']:.4f}")
    print(f"\nAnswerer-only models: {len(answer_only)}")
    for m in answer_only:
        print(f"  {m['model']:30s}  answer={m['overall_score']:.4f}  (no API judge data)")

    local_judge_map = {}
    for jname in judge_local["judges"]:
        lk = normalize(jname)
        local_judge_map[lk] = judge_local["overall_scores"][jname]

    fig = plt.figure(figsize=(12.5, 11.4))
    gs = fig.add_gridspec(2, 1, height_ratios=[4.7, 2.45], hspace=0.14)
    ax_scatter = fig.add_subplot(gs[0])
    ax_table = fig.add_subplot(gs[1])
    ax_table.axis("off")

    seen_families = set()
    for o in overlaps:
        fam = o["family"]
        color = FAMILY_COLORS.get(fam, "#2E86AB")
        marker = FAMILY_MARKERS.get(fam, "o")
        show_label = fam if fam not in seen_families else ""
        seen_families.add(fam)
        ax_scatter.scatter(
            o["answer_score"], o["judge_mean"],
            s=160, c=color, marker=marker, zorder=5,
            edgecolors="white", linewidths=0.8, alpha=0.9,
            label=show_label
        )

    label_overrides = {
        "MiMo-v2-flash": {"xytext": (-10, 8), "ha": "right"},
        "MiMo-v2-pro": {"xytext": (8, -14), "ha": "left"},
        "MiMo-v2.5": {"xytext": (8, -14), "ha": "left"},
        "DeepSeek-v4-flash": {"xytext": (10, -10), "ha": "left", "va": "top"},
        "DeepSeek-v4-pro": {"xytext": (-10, 8), "ha": "right", "va": "bottom"},
    }

    for o in overlaps:
        fam = o["family"]
        offset_map = {
            "DeepSeek": (8, 6),
            "MiniMax": (8, -14),
            "MiMo": (-6, 8),
        }
        dx, dy = offset_map.get(fam, (8, 6))
        ha = "left"
        if o["display"] in ("MiMo-v2-flash", "MiMo-v2-pro", "MiMo-v2.5-pro"):
            dx, dy = (-8, 8) if o["display"] == "MiMo-v2-flash" else (8, -14)

        if o["display"] in label_overrides:
            override = label_overrides[o["display"]]
            dx, dy = override["xytext"]
            ha = override["ha"]
            va = override.get("va", "center")
        else:
            va = "center"

        ax_scatter.annotate(
            shorten_name(o["display"]),
            (o["answer_score"], o["judge_mean"]),
            xytext=(dx, dy),
            textcoords="offset points",
            fontsize=9.6,
            color="#1a1a1a",
            fontweight="bold",
            ha=ha,
            va=va,
            zorder=8,
            bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor="none", alpha=0.88),
        )

    xs = np.array([o["answer_score"] for o in overlaps])
    ys = np.array([o["judge_mean"] for o in overlaps])

    lim_min = min(xs.min(), ys.min()) - 0.045
    lim_max = max(xs.max(), ys.max()) + 0.065

    diag = np.linspace(lim_min, lim_max, 100)
    ax_scatter.plot(diag, diag, "--", color="#888888",
                    linewidth=1.2, alpha=0.7, label="y=x (Perfect Agreement)")

    r, p = stats.pearsonr(xs, ys)
    print(f"\nPearson r = {r:.6f}, p = {p:.2e}")
    stat_text = rf"Pearson $r = {r:.6f}$"
    if p < 0.001:
        stat_text += r" ($p < 0.001$)"
    else:
        stat_text += f" ($p = {p:.4f}$)"

    ax_scatter.text(0.97, 0.04, stat_text, transform=ax_scatter.transAxes,
                    fontsize=10, ha="right", va="bottom",
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.85))

    qwen_norm = normalize("Qwen3.5-9B")
    if qwen_norm in local_judge_map and qwen_norm in answer_map:
        qwen_answer = answer_map[qwen_norm]["overall_score"]
        qwen_judge_local = local_judge_map[qwen_norm]
        gap = qwen_answer - qwen_judge_local

        ax_scatter.scatter(qwen_answer, qwen_judge_local, s=160,
                           c="#C0392B", zorder=6, edgecolors="white",
                           linewidths=0.8, marker="D",
                           label="Qwen3.5-9B (Local Judge)")

        ax_scatter.annotate(
            "Qwen3.5-9B\n(Local Judge)",
            (qwen_answer, qwen_judge_local),
            xytext=(10, -20),
            textcoords="offset points",
            fontsize=9.6,
            color="#C0392B",
            fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#C0392B", lw=0.8)
        )

        ax_scatter.plot([qwen_answer, qwen_answer], [qwen_judge_local, qwen_answer],
                        ":", color="#C0392B", linewidth=0.8, alpha=0.5)

        gap_x = qwen_answer + 0.008
        gap_y = (qwen_answer + qwen_judge_local) / 2
        ax_scatter.annotate(
            rf"$\Delta = {gap:.4f}$",
            (gap_x, gap_y),
            fontsize=9,
            color="#C0392B",
            fontweight="bold",
            rotation=90,
            ha="left", va="center"
        )

    ax_scatter.set_xlabel("Answerer Score", fontsize=11, fontweight="bold", labelpad=8)
    ax_scatter.set_ylabel("Judge Mean Score", fontsize=11, fontweight="bold")
    ax_scatter.set_title("Dual Role Matrix: Answerer vs Judge",
                         fontsize=13, fontweight="bold", pad=12)

    ax_scatter.set_xlim(lim_min, lim_max)
    ax_scatter.set_ylim(lim_min, lim_max)
    ax_scatter.set_aspect("equal")
    ax_scatter.grid(True, alpha=0.25, linestyle=":")

    handles, labels = ax_scatter.get_legend_handles_labels()
    unique = dict(zip(labels, handles))
    ax_scatter.legend(
        unique.values(),
        unique.keys(),
        fontsize=9.4,
        loc="upper left",
        framealpha=0.82,
        edgecolor="#cccccc",
        borderpad=0.72,
        labelspacing=0.72,
        handletextpad=0.72,
        handlelength=1.7,
        markerscale=1.05,
    )

    headers = ["Model", "Answer Score", "Judge Mean", "Δ", "Family", "Role"]
    cell_data = []
    for o in overlaps:
        diff = abs(o["answer_score"] - o["judge_mean"])
        cell_data.append([
            o["display"],
            f"{o['answer_score']:.4f}",
            f"{o['judge_mean']:.4f}",
            f"{diff:.5f}",
            o["family"],
            "Answerer + Judge"
        ])

    cell_data.append([
        "Qwen3.5-9B",
        f"{answer_map[qwen_norm]['overall_score']:.4f}",
        f"{local_judge_map[qwen_norm]:.4f}",
        f"{answer_map[qwen_norm]['overall_score'] - local_judge_map[qwen_norm]:.4f}",
        "Qwen",
        "Answerer Only\n(Local Judge)"
    ])

    col_widths = [0.22, 0.10, 0.12, 0.10, 0.10, 0.14]
    total_w = sum(col_widths)
    col_widths = [w / total_w for w in col_widths]

    table = ax_table.table(
        cellText=cell_data,
        colLabels=headers,
        cellLoc="center",
        loc="center",
        bbox=[0.0, 0.01, 1.0, 0.98],
        colWidths=col_widths,
    )

    table.auto_set_font_size(False)
    table.set_fontsize(8.6)
    table.scale(1, 1.22)

    for (i, j), cell in table.get_celld().items():
        if i == 0:
            cell.set_text_props(fontweight="bold", color="white", fontsize=8.8)
            cell.set_facecolor("#2C3E50")
        elif i % 2 == 0:
            cell.set_facecolor("#f5f5f5")
        else:
            cell.set_facecolor("white")
        cell.set_edgecolor("#cccccc")
        cell.set_height(0.125)

    last_row_idx = len(cell_data)
    for j in range(len(headers)):
        cell = table[last_row_idx, j]
        cell.set_facecolor("#FDEDEC")
        kwargs = {}
        if j == 0:
            kwargs["fontweight"] = "bold"
        if j in (1, 2, 3):
            kwargs["color"] = "#C0392B"
        if kwargs:
            cell.set_text_props(**kwargs)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(left=0.07, right=0.96, top=0.95, bottom=0.045)
    fig.savefig(OUTPUT, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"\nOutput: {OUTPUT}")
    print(f"  Size: {OUTPUT.stat().st_size:,} bytes")
    print("Done.")


if __name__ == "__main__":
    main()
