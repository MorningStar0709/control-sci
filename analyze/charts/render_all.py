import json
from pathlib import Path

def render_all(output_dir):
    output_dir = Path(output_dir)
    chart_dir = output_dir / "charts"
    chart_dir.mkdir(parents=True, exist_ok=True)

    results = {}
    for f in output_dir.glob("*.json"):
        if f.name == "summary_all.json":
            continue
        results[f.stem] = json.loads(f.read_text(encoding="utf-8"))

    # ── 1. 四维×难度热力图 ──
    if "01_dim_difficulty" in results:
        data = results["01_dim_difficulty"]["data"]
        matrix = data["matrix"]
        dims = ["A", "B", "C", "D"]
        levels = ["L1", "L2", "L3", "L4"]
        import matplotlib.pyplot as plt
        import numpy as np

        arr = np.array([[matrix[d][l] for l in levels] for d in dims])
        fig, ax = plt.subplots(figsize=(6, 4))
        im = ax.imshow(arr, cmap="YlOrRd", aspect="auto", vmin=0, vmax=40)
        ax.set_xticks(range(len(levels)))
        ax.set_xticklabels(levels)
        ax.set_yticks(range(len(dims)))
        ax.set_yticklabels(dims)
        for i in range(len(dims)):
            for j in range(len(levels)):
                ax.text(j, i, str(arr[i, j]), ha="center", va="center", fontsize=11, fontweight="bold")
        ax.set_xlabel("Difficulty Level")
        ax.set_ylabel("Dimension")
        fig.colorbar(im, ax=ax, fraction=0.046)
        fig.suptitle("Dimension × Difficulty Matrix", fontsize=13)
        fig.tight_layout()
        fig.savefig(chart_dir / "heatmap_dim_diff.png", dpi=180, bbox_inches="tight")
        plt.close(fig)
        print("  ✅ heatmap_dim_diff.png")

        # HTML fallback
        _write_html_table(chart_dir / "heatmap_dim_diff.html",
            ["Dimension"] + levels,
            [[d] + [str(matrix[d][l]) for l in levels] for d in dims],
            "Dimension × Difficulty Matrix")

    # ── 2. 子领域覆盖率柱状图 ──
    if "02_category" in results:
        cats = results["02_category"]["data"]["categories"]
        items = sorted(cats.items(), key=lambda x: -x[1])[:15]
        labels, values = zip(*items) if items else ([], [])
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, max(4, len(labels) * 0.35)))
        ax.barh(labels[::-1], values[::-1], color="#2f6f8f")
        ax.set_xlabel("Question Count")
        ax.set_title("Top Control Sub-domain Coverage")
        fig.tight_layout()
        fig.savefig(chart_dir / "category_bar.png", dpi=180, bbox_inches="tight")
        plt.close(fig)
        print("  ✅ category_bar.png")

        _write_html_table(chart_dir / "category_bar.html",
            ["Sub-domain", "Count"],
            [[c, str(n)] for c, n in items],
            "Top Control Sub-domain Coverage")

    # ── 3. 推理步数箱线图 ──
    if "03_reasoning_steps" in results:
        stats = results["03_reasoning_steps"]["data"]
        dims = ["A", "B", "C", "D"]
        # Generate approximate box data from stats
        _write_html_table(chart_dir / "steps_boxplot.html",
            ["Dimension", "Count", "Mean", "Median", "Q25", "Q75", "Min", "Max"],
            [[d,
              str(stats[d]["count"]),
              str(stats[d]["mean"]),
              str(stats[d]["median"]),
              str(stats[d]["q25"]),
              str(stats[d]["q75"]),
              str(stats[d]["min"]),
              str(stats[d]["max"])] for d in dims if stats[d]["count"] > 0],
            "Reasoning Step Depth by Dimension")
        print("  ✅ steps_boxplot.html (table)")

    # ── 4. Provider 饼图 ──
    if "04_provider" in results:
        prov = results["04_provider"]["data"]["provider_counts"]
        labels, values = zip(*prov.items()) if prov else ([], [])
        import matplotlib.pyplot as plt
        colors = ["#2f6f8f", "#d98c3e", "#5a9e6f", "#8f5a9e"]
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(values, labels=labels, autopct="%1.1f%%", colors=colors[:len(labels)],
               startangle=90, textprops={"fontsize": 10})
        ax.set_title("Provider Contribution")
        fig.tight_layout()
        fig.savefig(chart_dir / "provider_pie.png", dpi=180, bbox_inches="tight")
        plt.close(fig)
        print("  ✅ provider_pie.png")

    # ── 5. 一致性状态饼图 ──
    if "05_consistency" in results:
        status = results["05_consistency"]["data"]["status_counts"]
        labels, values = zip(*status.items()) if status else ([], [])
        label_map = {"auto_passed": "Auto Passed", "reviewed_kept": "Reviewed Kept"}
        labels_display = [label_map.get(l, l) for l in labels]
        import matplotlib.pyplot as plt
        colors = ["#5a9e6f", "#2f6f8f", "#d98c3e"]
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(values, labels=labels_display, autopct="%1.1f%%", colors=colors[:len(labels)],
               startangle=90, textprops={"fontsize": 10})
        ax.set_title("Consistency Status Distribution")
        fig.tight_layout()
        fig.savefig(chart_dir / "consistency_pie.png", dpi=180, bbox_inches="tight")
        plt.close(fig)
        print("  ✅ consistency_pie.png")

    # ── 6. 质量分层对比图 ──
    if "06_quality_tiers" in results:
        data = results["06_quality_tiers"]["data"]
        dims = ["A", "B", "C", "D"]
        auto_d = [data["auto_passed"]["dim_dist"][d] for d in dims]
        rev_d = [data["reviewed_kept"]["dim_dist"][d] for d in dims]
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.arange(len(dims))
        w = 0.35
        fig, ax = plt.subplots(figsize=(8, 5))
        bars1 = ax.bar(x - w/2, auto_d, w, label="Auto Passed", color="#5a9e6f")
        bars2 = ax.bar(x + w/2, rev_d, w, label="Reviewed Kept", color="#2f6f8f")
        ax.set_xticks(x)
        ax.set_xticklabels(dims)
        ax.set_ylabel("Question Count")
        ax.set_title("Quality Tier Distribution by Dimension")
        ax.legend()
        for bar in bars1:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    str(int(bar.get_height())), ha="center", va="bottom", fontsize=9)
        for bar in bars2:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    str(int(bar.get_height())), ha="center", va="bottom", fontsize=9)
        fig.tight_layout()
        fig.savefig(chart_dir / "quality_tiers.png", dpi=180, bbox_inches="tight")
        plt.close(fig)
        print("  ✅ quality_tiers.png")

        _write_html_table(chart_dir / "quality_tiers.html",
            ["Metric", "Auto Passed", "Reviewed Kept"],
            [["Count", str(data["auto_passed"]["count"]), str(data["reviewed_kept"]["count"])],
             ["Pct", str(data["auto_passed"]["pct"])+"%", str(data["reviewed_kept"]["pct"])+"%"],
             ["Mean Steps", str(data["auto_passed"]["mean_reasoning_steps"]), str(data["reviewed_kept"]["mean_reasoning_steps"])]],
            "Quality Tier Comparison")

    print(f"\nAll charts saved to: {chart_dir}")


def _write_html_table(path, headers, rows, title):
    lines = ["<!DOCTYPE html><html><head><meta charset='utf-8'>"
             f"<title>{title}</title>"
             "<style>body{font-family:sans-serif;margin:20px}"
             "table{border-collapse:collapse;width:100%}"
             "th,td{border:1px solid #ddd;padding:8px;text-align:center}"
             "th{background:#2f6f8f;color:#fff}"
             "tr:nth-child(even){background:#f5f5f5}</style></head><body>"
             f"<h2>{title}</h2><table><tr>"]
    for h in headers:
        lines.append(f"<th>{h}</th>")
    lines.append("</tr>")
    for row in rows:
        lines.append("<tr>")
        for cell in row:
            lines.append(f"<td>{cell}</td>")
        lines.append("</tr>")
    lines.append("</table></body></html>")
    path.write_text("\n".join(lines), encoding="utf-8")
