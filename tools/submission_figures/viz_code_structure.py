from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches
import numpy as np

mpl.rcParams['font.family'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
mpl.rcParams['axes.unicode_minus'] = False

BASE = Path(__file__).resolve().parents[2]
OUTPUT = BASE / "docs/assets/code_structure.png"

COLORS = {
    "bg": "#F7F9FC",
    "text_primary": "#1B2A4A",
    "text_secondary": "#5A6B80",
    "text_light": "#8899AA",
    "shadow": "#00000010",
    "edge_default": "#B0BCC8",
    "edge_highlight": "#7B8FA3",
}

LAYER_CONFIG = [
    {"y": 8.3, "label": "Entry", "tag": "CLI / API Gateway",
     "color": "#2C3E50", "band": "#E8EDF5", "band_end": "#DDE4EF"},
    {"y": 6.7, "label": "Core", "tag": "Agent Brain + Scheduler",
     "color": "#3498DB", "band": "#E8F0FB", "band_end": "#DAE9F7"},
    {"y": 4.8, "label": "Eval", "tag": "Benchmark + Judge",
     "color": "#27AE60", "band": "#E8F8ED", "band_end": "#D6F2DD"},
    {"y": 3.0, "label": "Tools", "tag": "Deep Analysis + Audit",
     "color": "#8E44AD", "band": "#F0EAF6", "band_end": "#E6DCF0"},
    {"y": 1.5, "label": "Orch", "tag": "Orchestration + Visualization",
     "color": "#E67E22", "band": "#FDF3E8", "band_end": "#FAE8D0"},
]

MODULES = [
    ("agent_cli.py", 5.5, 8.3, 1503, 0, "Entry"),

    ("resource_scheduler.py", 3.0, 7.0, 662, 1, "Core"),
    ("visual_audit.py", 8.0, 7.0, 520, 1, "Core"),
    ("agent.py", 5.5, 6.2, 211, 1, "Core"),

    ("evaluate.py", 1.8, 5.0, 569, 2, "Eval"),
    ("judge.py", 4.2, 5.0, 451, 2, "Eval"),
    ("cross_judge.py", 6.8, 5.0, 289, 2, "Eval"),
    ("chunk_embedding\n_analysis.py", 9.3, 5.0, 697, 2, "Eval"),

    ("t3_deep_analysis.py", 1.2, 3.2, 878, 3, "Tools"),
    ("audit_anti_scaling\n_law.py", 3.8, 3.2, 653, 3, "Tools"),
    ("bench_mineru_1.2b\n_vlm.py", 6.6, 3.2, 795, 3, "Tools"),
    ("embedding_analysis.py", 9.3, 3.2, 450, 3, "Tools"),

    ("build_corpus.py", 2.0, 1.5, 254, 4, "Orch"),
    ("benchmark_quality\n_viz.py", 5.0, 1.5, 320, 4, "Orch"),
    ("model_parallel.py", 8.0, 1.5, 478, 4, "Orch"),
]

EDGES = [
    ("agent_cli.py", "resource_scheduler.py"),
    ("agent_cli.py", "visual_audit.py"),
    ("agent_cli.py", "agent.py"),
    ("resource_scheduler.py", "evaluate.py"),
    ("resource_scheduler.py", "judge.py"),
    ("agent.py", "cross_judge.py"),
    ("agent.py", "chunk_embedding\n_analysis.py"),
    ("evaluate.py", "t3_deep_analysis.py"),
    ("judge.py", "audit_anti_scaling\n_law.py"),
    ("visual_audit.py", "bench_mineru_1.2b\n_vlm.py"),
    ("chunk_embedding\n_analysis.py", "embedding_analysis.py"),
    ("evaluate.py", "model_parallel.py"),
    ("judge.py", "benchmark_quality\n_viz.py"),
    ("agent.py", "build_corpus.py"),
]

EDGE_COLORS = {
    ("Entry", "Core"): "#3D5A80",
    ("Core", "Eval"): "#2E86AB",
    ("Core", "Tools"): "#A06CD5",
    ("Core", "Orch"): "#D4933B",
    ("Eval", "Tools"): "#6BAF6B",
    ("Eval", "Orch"): "#C78C4E",
    ("Tools", "Orch"): "#B875C9",
}


def gradient_band(ax, y_center, height, color_top, color_bot, alpha=0.3):
    y0 = y_center - height / 2
    y1 = y_center + height / 2
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack([gradient] * 2)
    ax.imshow(gradient, aspect='auto', origin='lower',
              extent=[0.3, 11.5, y0, y1], alpha=alpha,
              cmap=mpl.colors.LinearSegmentedColormap.from_list(
                  'gb', [color_top, color_bot]))


def draw_shadow_box(ax, x, y, w, h, facecolor, edgecolor=None, lw=1.2, r=0.08):
    shadow = FancyBboxPatch((x - w/2 + 0.03, y - h/2 - 0.03), w, h,
                            boxstyle=f"round,pad={r}", facecolor=COLORS["shadow"],
                            edgecolor="none", linewidth=0, zorder=1)
    ax.add_patch(shadow)
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle=f"round,pad={r}", facecolor=facecolor,
                         edgecolor=edgecolor or facecolor, linewidth=lw, zorder=3)
    ax.add_patch(box)
    return box


def main():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 9.5)
    ax.set_facecolor(COLORS["bg"])
    fig.patch.set_facecolor(COLORS["bg"])
    ax.axis("off")

    for layer in LAYER_CONFIG:
        gradient_band(ax, layer["y"], 1.1, layer["band"], layer["band_end"], alpha=0.35)
        ax.text(0.5, layer["y"], layer["label"],
                fontsize=8, color=layer["color"], fontweight="bold",
                ha="center", va="center", rotation=90, alpha=0.6,
                bbox=dict(boxstyle="round,pad=0.12", facecolor="white",
                          edgecolor=layer["color"], alpha=0.4, linewidth=0.5),
                zorder=2)

    node_info = {}
    for name, x, y, lines, layer_idx, group in MODULES:
        cfg = LAYER_CONFIG[layer_idx]
        color = cfg["color"]
        size_factor = lines / 1500.0
        nh = 0.38 + size_factor * 0.22
        nw = min(2.1, max(1.5, 1.1 + size_factor * 0.9))

        node_info[name] = (x, y, nw, nh, group, color)

    for src, dst in EDGES:
        if src in node_info and dst in node_info:
            sx, sy, sw, sh, sg, sc = node_info[src]
            dx, dy, dw, dh, dg, dc = node_info[dst]
            sy_bot = sy - sh / 2
            dy_top = dy + dh / 2

            if sy_bot > dy_top:
                ec = EDGE_COLORS.get((sg, dg), COLORS["edge_default"])
                ax.annotate("", xy=(dx, dy_top), xytext=(sx, sy_bot),
                            arrowprops=dict(arrowstyle="-|>", color=ec, lw=1.3,
                                            connectionstyle="arc3,rad=0.05",
                                            alpha=0.7),
                            zorder=2)

    for name, x, y, lines, layer_idx, group in MODULES:
        color = node_info[name][5]
        nw = node_info[name][2]
        nh = node_info[name][3]

        draw_shadow_box(ax, x, y, nw, nh, facecolor=color, edgecolor=color, lw=0.8, r=0.06)

        display_name = name.replace("\n", " ")
        ax.text(x, y + 0.03, display_name,
                fontsize=7, color="white", fontweight="bold",
                ha="center", va="center", zorder=5)
        ax.text(x, y - nh/2 + 0.055, f"{lines} L",
                fontsize=6, color="#D0D8E8", ha="center", va="bottom",
                style="italic", zorder=5)

    for cfg in LAYER_CONFIG:
        layer_idx = LAYER_CONFIG.index(cfg)
        layer_modules = [(m[0], m[3]) for m in MODULES if m[4] == layer_idx]
        total_lines = sum(l for _, l in layer_modules)
        count = len(layer_modules)
        ax.text(11.0, cfg["y"] + 0.35, cfg["label"],
                fontsize=9, color=cfg["color"], fontweight="bold",
                ha="right", va="center", zorder=5)
        ax.text(11.0, cfg["y"] + 0.1, cfg["tag"],
                fontsize=6.5, color=COLORS["text_light"],
                ha="right", va="center", style="italic", zorder=5)
        ax.text(11.0, cfg["y"] - 0.12, f"{count} files  ·  {total_lines:,} lines",
                fontsize=6, color=COLORS["text_secondary"],
                ha="right", va="center", zorder=5)

    ax.text(5.75, 9.2, "ControlSci Code Structure — Module Dependency Graph",
            fontsize=16, fontweight="bold", ha="center", va="bottom",
            color=COLORS["text_primary"], zorder=5)

    total_lines = sum(m[3] for m in MODULES)
    total_files = len(MODULES)
    total_edges = len(EDGES)
    ax.text(5.75, 8.9,
            f"{total_files} key modules  ·  {total_lines:,} total lines  ·  {total_edges} dependency edges  ·  5-layer architecture",
            fontsize=8, ha="center", va="bottom", color=COLORS["text_secondary"], zorder=5)

    panel_x, panel_y = 0.55, 0.4
    draw_shadow_box(ax, panel_x + 1.8, panel_y, 3.6, 0.55,
                    facecolor="white", edgecolor="#D0D8E8", lw=0.6, r=0.08)
    stats = f"Total: {total_files} files  |  {total_lines:,} lines  |  {total_edges} edges  |  5 layers"
    ax.text(panel_x + 1.8, panel_y + 0.12, stats,
            fontsize=7.5, color=COLORS["text_primary"], fontweight="bold",
            ha="center", va="center", zorder=5)
    ax.text(panel_x + 1.8, panel_y - 0.1,
            "Node size ∝ code volume  |  Edge color = source→target layer",
            fontsize=6.5, color=COLORS["text_light"],
            ha="center", va="center", style="italic", zorder=5)

    legend_handles = []
    for cfg in LAYER_CONFIG:
        legend_handles.append(
            mpatches.Patch(facecolor=cfg["color"], edgecolor=cfg["color"],
                           linewidth=0.8, label=f"{cfg['label']}: {cfg['tag']}"))
    leg = ax.legend(handles=legend_handles, loc="lower center",
                    fontsize=7.5, ncol=5, framealpha=0.95,
                    edgecolor="#D0D8E8", bbox_to_anchor=(0.55, -0.01),
                    handletextpad=0.4, columnspacing=1.2)
    leg.get_frame().set_linewidth(0.5)
    leg.get_frame().set_facecolor("white")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=220, bbox_inches="tight",
                facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    print(f"Output: {OUTPUT}")
    print(f"  Size: {OUTPUT.stat().st_size:,} bytes")
    print("Done.")


if __name__ == "__main__":
    main()
