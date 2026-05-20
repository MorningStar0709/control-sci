"""Generate reproducible experiment figures for public submission reports.

The script intentionally writes generated artifacts outside docs/submissions
first, then copies only final PNG files into the public display asset folders.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter, PercentFormatter


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "build" / "submission_experiment_figures"
PUBLIC_ASSET_DIR = ROOT / "docs" / "submissions" / "shared" / "assets"
PUBLIC_TASK1_DIR = PUBLIC_ASSET_DIR / "task1"
PUBLIC_TASK2_DIR = PUBLIC_ASSET_DIR / "task2"
PUBLIC_TASK3_DIR = PUBLIC_ASSET_DIR / "task3"


def setup_style() -> None:
    font_candidates = [
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/msyhbd.ttc"),
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("C:/Windows/Fonts/simsun.ttc"),
    ]
    for font_path in font_candidates:
        if font_path.exists():
            font_manager.fontManager.addfont(str(font_path))
            plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(font_path)).get_name()
            break

    plt.rcParams.update(
        {
            "axes.unicode_minus": False,
            "figure.dpi": 130,
            "savefig.dpi": 220,
            "savefig.bbox": "tight",
            "axes.edgecolor": "#d7dee8",
            "axes.linewidth": 0.9,
            "axes.labelcolor": "#172033",
            "xtick.color": "#35445a",
            "ytick.color": "#35445a",
            "text.color": "#172033",
            "axes.titleweight": "bold",
            "axes.titlesize": 16,
        }
    )


def save(fig: plt.Figure, filename: str, public_dir: Path) -> dict:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    public_dir.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / filename
    public_path = public_dir / filename
    fig.savefig(out_path)
    plt.close(fig)
    shutil.copy2(out_path, public_path)
    return {
        "file": filename,
        "generated": str(out_path.relative_to(ROOT)).replace("\\", "/"),
        "public_copy": str(public_path.relative_to(ROOT)).replace("\\", "/"),
    }


def load_json(path: str) -> dict:
    with (ROOT / path).open("r", encoding="utf-8") as f:
        return json.load(f)


def plot_track1_leaderboard() -> dict:
    data = load_json("benchmark/eval/results/leaderboard_complete.json")
    rows = data["models"]
    names = [r["model"] for r in rows]
    overall = np.array([r["overall_score"] for r in rows]) * 100
    dims = ["A", "B", "C", "D"]
    dim_scores = np.array([[r["dimension_scores"][d] * 100 for d in dims] for r in rows])

    fig, (ax_bar, ax_heat) = plt.subplots(
        1,
        2,
        figsize=(17.2, 7.2),
        gridspec_kw={"width_ratios": [1.0, 1.28], "wspace": 0.50},
    )
    fig.patch.set_facecolor("#f7f9fc")
    for ax in (ax_bar, ax_heat):
        ax.set_facecolor("#ffffff")

    y = np.arange(len(names))
    colors = ["#1f6feb" if i < 3 else "#6b7a90" for i in range(len(names))]
    ax_bar.set_axisbelow(True)
    ax_bar.barh(y, overall, color=colors, height=0.62, zorder=3)
    ax_bar.set_yticks(y, labels=names)
    ax_bar.invert_yaxis()
    ax_bar.set_xlim(0, 75)
    ax_bar.set_xlabel("Overall Score (0-100)")
    ax_bar.set_title("Overall Ranking Across 9 Models")
    ax_bar.grid(axis="x", color="#e8edf5", linewidth=0.8, zorder=0)
    ax_bar.spines[["top", "right", "left"]].set_visible(False)
    for i, value in enumerate(overall):
        ax_bar.text(value + 0.9, i, f"{value:.1f}", va="center", fontsize=10, color="#172033")

    im = ax_heat.imshow(dim_scores, aspect="auto", cmap="YlGnBu", vmin=15, vmax=75)
    ax_heat.set_title("Four-Dimension Capability Profile")
    ax_heat.set_xticks(
        np.arange(len(dims)),
        labels=["A Concepts", "B Reasoning", "C Conditions", "D Design"],
    )
    ax_heat.set_yticks(np.arange(len(names)), labels=names)
    ax_heat.tick_params(axis="y", labelsize=9)
    ax_heat.spines[:].set_visible(False)
    for i in range(dim_scores.shape[0]):
        for j in range(dim_scores.shape[1]):
            value = dim_scores[i, j]
            ax_heat.text(j, i, f"{value:.1f}", ha="center", va="center", fontsize=9, color="#0f172a")
    cbar = fig.colorbar(im, ax=ax_heat, fraction=0.046, pad=0.03)
    cbar.set_label("Dimension Score (0-100)")

    fig.suptitle(
        "ControlMind Sci-Align 500 Benchmark: Overall Ranking and Capability Profile",
        fontsize=18,
        fontweight="bold",
    )
    fig.text(
        0.5,
        0.01,
        "Source: benchmark/eval/results/leaderboard_complete.json; unified judge: DeepSeek-v4-flash; Qwen3.5-9B was evaluated locally via Ollama.",
        ha="center",
        fontsize=10,
        color="#516073",
    )
    return save(fig, "track1_leaderboard_scores.png", PUBLIC_TASK1_DIR)


def plot_track1_mineru_vs_pymupdf() -> dict:
    docs = ["Active Disturbance\nRejection Control", "Automatic Control\nPrinciples", "Nonlinear\nSystems"]
    pages = np.array([381, 635, 530])
    mineru_chars = np.array([478657, 1312750, 1133118])
    pymupdf_chars = np.array([0, 0, 0])
    mineru_formulas = np.array([3036, 9970, 15467])

    fig, (ax1, ax2) = plt.subplots(
        1,
        2,
        figsize=(15.8, 6.3),
        gridspec_kw={"width_ratios": [1.12, 1], "wspace": 0.34},
    )
    fig.patch.set_facecolor("#f7f9fc")
    for ax in (ax1, ax2):
        ax.set_facecolor("#ffffff")
        ax.tick_params(axis="both", labelsize=9)

    x = np.arange(len(docs))
    width = 0.36
    ax1.set_axisbelow(True)
    ax1.bar(x - width / 2, mineru_chars, width, label="MinerU OCR", color="#1f6feb", zorder=3)
    ax1.bar(x + width / 2, pymupdf_chars, width, label="PyMuPDF Text Layer", color="#f59e0b", zorder=3)
    ax1.set_ylim(0, mineru_chars.max() * 1.28)
    ax1.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value / 1_000_000:.1f}M"))
    ax1.set_xticks(x, docs)
    ax1.set_ylabel("Effective Text Characters", fontsize=10)
    ax1.set_title("Scanned Textbooks: Text Extraction Becomes Usable", fontsize=14, pad=8)
    ax1.grid(axis="y", color="#e8edf5", linewidth=0.8, zorder=0)
    ax1.spines[["top", "right"]].set_visible(False)
    ax1.legend(frameon=False, fontsize=10)
    for i, (m, p) in enumerate(zip(mineru_chars, pymupdf_chars)):
        ax1.text(i - width / 2, m + mineru_chars.max() * 0.035, f"{m:,}", ha="center", va="bottom", fontsize=8)
        ax1.text(i + width / 2, mineru_chars.max() * 0.025, f"{p:,}", ha="center", va="bottom", fontsize=8)

    ax2.set_axisbelow(True)
    ax2.barh(docs, mineru_formulas, color="#0f766e", height=0.58, zorder=3)
    ax2.set_xlabel("Structured LaTeX Formula Count", fontsize=10)
    ax2.set_title("Scanned Textbooks: Formula Recovery Requires MinerU", fontsize=14, pad=8)
    ax2.grid(axis="x", color="#e8edf5", linewidth=0.8, zorder=0)
    ax2.spines[["top", "right", "left"]].set_visible(False)
    for i, value in enumerate(mineru_formulas):
        ax2.text(value + 450, i, f"{value:,}", va="center", fontsize=8)

    fig.suptitle("MinerU vs PyMuPDF: Parsing Quality on Scanned Control Textbooks", fontsize=18, fontweight="bold", y=0.98)
    fig.subplots_adjust(top=0.82, bottom=0.18, left=0.07, right=0.98)
    fig.text(
        0.5,
        0.045,
        f"Three scanned textbooks, {pages.sum():,} pages total; MinerU extracted {mineru_chars.sum():,} characters + {mineru_formulas.sum():,} formulas, "
        f"while PyMuPDF extracted {pymupdf_chars.sum():,} text-layer characters. Source: benchmark/pipeline/compare_mineru_vs_pymupdf.py.",
        ha="center",
        fontsize=9,
        color="#516073",
    )
    return save(fig, "track1_mineru_vs_pymupdf_ocr.png", PUBLIC_TASK1_DIR)


def copy_track1_embedding_figures() -> list[dict]:
    copied = []
    sources = {
        "track1_embedding_global_pca.png": "benchmark/eval/results/chunk_embedding/a1_global_pca.png",
        "track1_embedding_train_eval.png": "benchmark/eval/results/chunk_embedding/a4_train_eval.png",
        "track1_benchmark_coverage.png": "benchmark/eval/results/benchmark_quality_viz_1_coverage.png",
        "track1_benchmark_difficulty.png": "benchmark/eval/results/benchmark_quality_viz_2_difficulty.png",
        "track1_benchmark_dimension.png": "benchmark/eval/results/benchmark_quality_viz_3_dimension.png",
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PUBLIC_TASK1_DIR.mkdir(parents=True, exist_ok=True)
    for target_name, source in sources.items():
        source_path = ROOT / source
        generated_path = OUT_DIR / target_name
        public_path = PUBLIC_TASK1_DIR / target_name
        shutil.copy2(source_path, generated_path)
        shutil.copy2(generated_path, public_path)
        copied.append(
            {
                "file": target_name,
                "source": source,
                "generated": str(generated_path.relative_to(ROOT)).replace("\\", "/"),
                "public_copy": str(public_path.relative_to(ROOT)).replace("\\", "/"),
            }
        )
    return copied


def plot_track3_zh_ask_summary() -> dict:
    eval_data = load_json("benchmark/eval/results/medical_rag_eval_zh_ask.json")
    trace_path = ROOT / "benchmark/eval/results/medical_rag_zh_ask_traces.jsonl"
    traces = [json.loads(line) for line in trace_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    summary = eval_data["summary"]["index_bge_m3"]
    total_claims = sum(row["synthesis"]["claim_count"] for row in traces)
    supported_claims = sum(row["synthesis"]["supported_claims"] for row in traces)
    unsupported_claims = sum(row["synthesis"]["unsupported_claims"] for row in traces)
    metrics = [
        ("Hit@3", summary["hit_at_k"], summary["cases"]),
        ("Label Hit@3", summary["label_hit_at_k"], summary["cases"]),
        ("Chinese Bridge", summary["bridged_cases"], summary["cases"]),
        ("Multi-Query", summary["multi_query_cases"], summary["cases"]),
        ("Supported Claims", supported_claims, total_claims),
        ("Unsupported Claims", unsupported_claims, total_claims),
    ]

    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.patch.set_facecolor("#f7f9fc")
    ax.set_facecolor("#ffffff")
    labels = [m[0] for m in metrics]
    values = np.array([m[1] / m[2] if m[2] else 0 for m in metrics])
    colors = ["#1f6feb", "#1f6feb", "#0f766e", "#7c3aed", "#16a34a", "#dc2626"]
    ax.set_axisbelow(True)
    bars = ax.bar(labels, values, color=colors, width=0.62, zorder=3)
    ax.set_ylim(0, 1.12)
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    ax.set_title("Chinese Ask RAG Loop: Retrieval, Bridging, and Citation Support")
    ax.set_ylabel("Share")
    ax.grid(axis="y", color="#e8edf5", linewidth=0.8, zorder=0)
    ax.spines[["top", "right", "left"]].set_visible(False)
    for bar, (_, num, den) in zip(bars, metrics):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.03,
            f"{num}/{den}",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )

    fig.text(
        0.5,
        0.01,
        "Sources: medical_rag_eval_zh_ask.json and medical_rag_zh_ask_traces.jsonl; 6 Chinese queries, BGE M3 index, local qwen3.5:9b synthesis.",
        ha="center",
        fontsize=10,
        color="#516073",
    )
    return save(fig, "zh_ask_rag_trace_summary.png", PUBLIC_TASK3_DIR)


def plot_track3_evidence_boundary() -> dict:
    llm = load_json("data/sources_medical/medbench/medbench_core_subsets_v2_quality.json")["summary"]
    vlm_35b = load_json("data/sources_medical/medbench/medbench_vlm_report.json")["statistics"]
    vlm_9b = load_json("data/sources_medical/medbench/medbench_vlm_report_9b.json")["statistics"]
    labels = ["LLM Text Subset\n35B", "VLM Multimodal Subset\n35B", "VLM Multimodal Subset\n9B"]
    totals = np.array([llm["total_unique"], vlm_35b["total_questions"], vlm_9b["total_questions"]])
    insufficient = np.array(
        [llm["insufficient"], vlm_35b["overall_evidence_insufficient"], vlm_9b["overall_evidence_insufficient"]]
    )
    sufficient = totals - insufficient

    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    fig.patch.set_facecolor("#f7f9fc")
    ax.set_facecolor("#ffffff")
    x = np.arange(len(labels))
    ax.set_axisbelow(True)
    ax.bar(x, sufficient / totals, color="#1f6feb", label="Answerable / evidence-covered", zorder=3)
    ax.bar(
        x,
        insufficient / totals,
        bottom=sufficient / totals,
        color="#f97316",
        label="Evidence-insufficient",
        zorder=3,
    )
    ax.set_xticks(x, labels)
    ax.set_ylim(0, 1.16)
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    ax.set_title("MedBench Evidence Boundary: Text RAG vs Multimodal Evidence")
    ax.set_ylabel("Question Share")
    ax.grid(axis="y", color="#e8edf5", linewidth=0.8, zorder=0)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.legend(
        frameon=False,
        loc="upper left",
        bbox_to_anchor=(1.02, 0.98),
        borderaxespad=0.0,
    )
    for i, (total, ei) in enumerate(zip(totals, insufficient)):
        ax.text(i, 1.045, f"EI {ei}/{total}\n{ei / total:.1%}", ha="center", va="bottom", fontsize=11, fontweight="bold")

    fig.text(
        0.5,
        0.01,
        "Sources: medbench_core_subsets_v2_quality.json, medbench_vlm_report.json, and medbench_vlm_report_9b.json; all are self-evaluations, not official MedBench scores.",
        ha="center",
        fontsize=10,
        color="#516073",
    )
    fig.subplots_adjust(top=0.80, bottom=0.16, left=0.08, right=0.78)
    return save(fig, "medbench_evidence_boundary.png", PUBLIC_TASK3_DIR)


def plot_track2_dual_track_synergy() -> dict:
    columns = ["Asset", "Dataset Role", "Agent Role", "Linkage Type"]
    rows = [
        ["500-question\nBenchmark", "Evaluation Target", "Agent Artifact", "Same Entity\nDifferent Role"],
        ["9 Models x\n500 Scores", "Leaderboard", "Judge Matrix", "Dual Identity"],
        ["28K Chunks,\n362 Docs", "Data Scale Proof", "Embedding Scan", "Same Source\nDifferent View"],
        ["QLoRA\nFine-tuning", "Score Improvement", "Counter-intuitive\nDiscovery", "Same Experiment\nDifferent Conclusion"],
        ["D Data\nFlywheel", "Leaderboard\nExpansion", "6-step\nAutonomous Loop", "Same Process\nDifferent Metric"],
        ["31 Retrospective\nDocuments", "Methodology", "Engineering Rigor", "Same Asset\nDifferent Dimension"],
    ]

    fig, ax = plt.subplots(figsize=(12.5, 6.9))
    fig.patch.set_facecolor("#ffffff")
    ax.axis("off")
    ax.set_title("Dual-Track Synergy Matrix: ControlSci Assets Across Two Workflows", pad=18, fontsize=16)

    table = ax.table(
        cellText=rows,
        colLabels=columns,
        cellLoc="center",
        colLoc="center",
        loc="center",
        bbox=[0.04, 0.16, 0.92, 0.72],
        colWidths=[0.22, 0.24, 0.24, 0.30],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9.2)
    table.scale(1.0, 1.35)

    header_color = "#26384b"
    row_fills = ["#f7f9fb", "#ffffff"]
    asset_fill = "#f1f4f7"
    linkage_fill = "#eef3f7"
    linkage_text = "#243447"
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#d6dce3")
        cell.set_linewidth(0.75)
        if r == 0:
            cell.set_facecolor(header_color)
            cell.get_text().set_color("#ffffff")
            cell.get_text().set_weight("bold")
        else:
            cell.set_facecolor(row_fills[(r - 1) % 2])
            if c == 0:
                cell.set_facecolor(asset_fill)
                cell.get_text().set_weight("bold")
            if c == 3:
                cell.set_facecolor(linkage_fill)
                cell.get_text().set_color(linkage_text)
                cell.get_text().set_weight("bold")

    fig.text(
        0.5,
        0.06,
        "Dual-track synergy: the same data, experiments, and model artifacts serve complementary roles across dataset construction and agent execution.",
        ha="center",
        fontsize=10,
        color="#5b6472",
    )
    return save(fig, "dual_track_synergy.png", PUBLIC_TASK2_DIR)


def main() -> None:
    setup_style()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = {
        "generated_at": "2026-05-17",
        "output_dir": str(OUT_DIR.relative_to(ROOT)).replace("\\", "/"),
        "public_asset_dir": str(PUBLIC_ASSET_DIR.relative_to(ROOT)).replace("\\", "/"),
        "figures": [],
    }
    manifest["figures"].append(plot_track1_leaderboard())
    manifest["figures"].append(plot_track1_mineru_vs_pymupdf())
    manifest["figures"].extend(copy_track1_embedding_figures())
    manifest["figures"].append(plot_track2_dual_track_synergy())
    manifest["figures"].append(plot_track3_zh_ask_summary())
    manifest["figures"].append(plot_track3_evidence_boundary())

    manifest_path = OUT_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {manifest_path.relative_to(ROOT)}")
    for figure in manifest["figures"]:
        print(f"- {figure['public_copy']}")


if __name__ == "__main__":
    main()
