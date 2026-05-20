from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['font.family'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
mpl.rcParams['axes.unicode_minus'] = False

BASE = Path(__file__).resolve().parents[2]
OUTPUT = BASE / "docs/submissions/shared/assets/task2/dual_track_synergy.png"

ASSETS = [
    ("500-question\nBenchmark", "Evaluation Target", "Agent Artifact", "Same Entity\nDifferent Role", "#3498DB"),
    ("9 Models x\n500 Scores", "Leaderboard", "Judge Matrix", "Dual Identity", "#E74C3C"),
    ("28K Chunks,\n362 Docs", "Data Scale Proof", "Embedding Scan", "Same Source\nDifferent View", "#2ECC71"),
    ("QLoRA\nFine-tuning", "Score Improvement", "Counter-intuitive\nDiscovery", "Same Exp.\nDifferent Conclusion", "#F39C12"),
    ("D Data\nFlywheel", "Leaderboard\nExpansion", "6-step\nAutonomous Loop", "Same Process\nDifferent Metric", "#9B59B6"),
    ("31 Retrospective\nDocuments", "Methodology", "Engineering Rigor", "Same Asset\nDifferent Dimension", "#1ABC9C"),
]

def main():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis("off")

    col_labels = ["Asset", "Dataset Role", "Agent Role", "Linkage Type"]

    row_height = 0.10
    header_height = 0.06
    left = 0.06
    right = 0.94
    col_widths = [0.22, 0.24, 0.24, 0.18]
    total_col_w = right - left

    x_positions = [left]
    for cw in col_widths[:-1]:
        x_positions.append(x_positions[-1] + cw * total_col_w)
    x_positions.append(right)

    def draw_cell(ax, x0, y0, x1, y1, text, facecolor="white", textcolor="black",
                  fontsize=8, fontweight="normal", align="center", va="center"):
        rect = mpatches.FancyBboxPatch(
            (x0, y0), x1 - x0, y1 - y0,
            boxstyle="round,pad=0.003", facecolor=facecolor,
            edgecolor="#cccccc", linewidth=0.6
        )
        ax.add_patch(rect)
        ax.text(
            (x0 + x1) / 2, (y0 + y1) / 2, text,
            fontsize=fontsize, color=textcolor, fontweight=fontweight,
            ha=align, va=va, linespacing=1.0
        )

    top = 0.95
    header_color = "#2C3E50"
    for j, (col_name, x0, x1) in enumerate(zip(col_labels, x_positions, x_positions[1:])):
        draw_cell(ax, x0, top - header_height, x1, top, col_name,
                  facecolor=header_color, textcolor="white", fontsize=9, fontweight="bold")

    y0 = top - header_height
    for i, (asset, track1, track2, linkage, linkage_color) in enumerate(ASSETS):
        y1 = y0 - row_height
        row_bg = "#f8f9fa" if i % 2 == 0 else "white"

        draw_cell(ax, x_positions[0], y1, x_positions[1], y0, asset,
                  facecolor=row_bg, fontsize=7.8, fontweight="bold", va="center")
        draw_cell(ax, x_positions[1], y1, x_positions[2], y0, track1,
                  facecolor=row_bg, fontsize=7.2, va="center")
        draw_cell(ax, x_positions[2], y1, x_positions[3], y0, track2,
                  facecolor=row_bg, fontsize=7.2, va="center")

        link_bg = "#eaf2f8"
        if "Dual Identity" in linkage:
            link_bg = "#fdedec"
        elif "Different View" in linkage:
            link_bg = "#e8f8f5"
        elif "Different Conclusion" in linkage:
            link_bg = "#fef5e7"
        elif "Different Metric" in linkage:
            link_bg = "#f4ecf7"
        elif "Different Dimension" in linkage:
            link_bg = "#e8f6f3"

        draw_cell(ax, x_positions[3], y1, x_positions[4], y0, linkage,
                  facecolor=link_bg, fontsize=7.2, fontweight="bold",
                  textcolor=linkage_color, va="center")

        y0 = y1

    ax.text(0.5, 0.02,
            "Dual-track synergy: the same data, experiments, and model artifacts serve complementary roles\n"
            "across dataset construction and agent execution.",
            transform=ax.transAxes, fontsize=8, ha="center", va="bottom",
            color="#555555", linespacing=1.3)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Dual-Track Synergy Matrix: ControlSci Assets Across Two Workflows",
                 fontsize=13, fontweight="bold", pad=12, y=0.98)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout(rect=[0, 0.04, 1, 0.96])
    fig.savefig(OUTPUT, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Output: {OUTPUT}")
    print(f"  Size: {OUTPUT.stat().st_size:,} bytes")
    print("Done.")


if __name__ == "__main__":
    main()
