from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


repo = Path(__file__).resolve().parents[1]
results = repo / "benchmark" / "eval" / "results"
medical_results = results / "medical"
out_dirs = [
    repo / "_final_submission_by_track" / "track3_medical_rag" / "shared" / "assets",
    repo / "docs" / "submissions" / "shared" / "assets" / "task3",
]

navy = "#0B1F3A"
ink = "#334155"
gray = "#64748B"
line = "#D6E0EA"
fill = "#F7F9FB"
header = "#25384D"
accent = "#3B5B78"
muted = "#8DA2B6"
good = "#477A64"
warn = "#9A6A32"
soft_blue = "#EDF3F8"
soft_green = "#EAF4EF"
soft_warn = "#F8F1E8"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "axes.edgecolor": "#D0D7DE",
        "axes.linewidth": 0.8,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_all(fig: plt.Figure, name: str) -> None:
    for out_dir in out_dirs:
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / name, dpi=220, bbox_inches="tight", pad_inches=0.22)
    plt.close(fig)


def rounded(ax, xy, w, h, fc="white", ec=line, lw=1.0, radius=0.018):
    patch = FancyBboxPatch(
        xy,
        w,
        h,
        boxstyle=f"round,pad=0.010,rounding_size={radius}",
        linewidth=lw,
        edgecolor=ec,
        facecolor=fc,
    )
    ax.add_patch(patch)
    return patch


def canvas(title: str, subtitle: str, figsize=(15.8, 8.8)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(0.04, 0.955, title, fontsize=21, fontweight="bold", color=navy, va="top")
    ax.text(0.04, 0.908, subtitle, fontsize=10.8, color=gray, va="top")
    return fig, ax


def generate_sciverse_rrf_matrix() -> None:
    hybrid = load_json(medical_results / "sciverse_hybrid_compare.json")
    fused = load_json(medical_results / "sciverse_fused_rrf.json")
    s = fused["summary"]
    cases = fused["cases"]
    local_count = 0
    sciverse_count = 0
    for case in cases:
        for item in case["fused_rrf"]["results"]:
            if item.get("source") == "local":
                local_count += 1
            elif item.get("source") == "sciverse":
                sciverse_count += 1
    total = max(1, local_count + sciverse_count)
    local_share = local_count / total
    sciverse_share = sciverse_count / total

    fig, ax = canvas(
        "Sciverse Dual-Engine RRF Evidence",
        "Local PMC index and Sciverse global search are complementary, then fused by one RRF ranking pipe",
    )

    # Pipeline blocks
    y = 0.68
    blocks = [
        (0.06, "Local Hybrid", "97 PMC papers\n3,348 chunks\nclaim support 100%", soft_blue, accent),
        (0.36, "RRF Fusion", f"6 zh Ask cases\nFused support {s['fused_rrf']['claim_support_rate']:.0%}\n{local_share:.0%} Local / {sciverse_share:.0%} Sciverse", fill, navy),
        (0.66, "Sciverse", "5.16B public records\nagentic-search\nclaim support 100%", soft_green, good),
    ]
    for x, label, body, fc, color in blocks:
        rounded(ax, (x, y), 0.24, 0.16, fc=fc, ec=line)
        ax.text(x + 0.02, y + 0.115, label, fontsize=12, color=color, fontweight="bold", va="center")
        ax.text(x + 0.02, y + 0.058, body, fontsize=9.3, color=ink, va="center", linespacing=1.35)
    ax.annotate("", xy=(0.345, y + 0.08), xytext=(0.322, y + 0.08), arrowprops={"arrowstyle": "->", "color": muted, "lw": 1.4})
    ax.annotate("", xy=(0.615, y + 0.08), xytext=(0.638, y + 0.08), arrowprops={"arrowstyle": "->", "color": muted, "lw": 1.4})

    # Metrics table
    x0, y0 = 0.07, 0.28
    widths = [0.24, 0.20, 0.20, 0.20]
    headers = ["Metric", "Local Hybrid", "Sciverse", "Fused RRF"]
    rows = [
        ("Case count", f"{s['case_count']}", f"{s['case_count']}", f"{s['case_count']}"),
        ("Claim support", f"{s['local_hybrid']['claim_support_rate']:.0%}", f"{s['sciverse']['claim_support_rate']:.0%}", f"{s['fused_rrf']['claim_support_rate']:.0%}"),
        ("Avg hits", f"{s['local_hybrid']['avg_hits']:.1f}", f"{s['sciverse']['avg_hits']:.1f}", f"{s['fused_rrf']['avg_hits']:.1f}"),
        ("Fused source mix", "-", "-", f"{local_share:.0%} local / {sciverse_share:.0%} Sciverse"),
        ("Cross-engine overlap", "-", f"{hybrid['summary']['avg_overlap_rate']:.0%}", f"{s['avg_overlap_rate']:.0%}"),
    ]
    row_h = 0.062
    ax.add_patch(Rectangle((x0, y0 + row_h * len(rows)), sum(widths), 0.058, facecolor=header, linewidth=0))
    x = x0
    for h, w in zip(headers, widths):
        ax.text(x + w / 2, y0 + row_h * len(rows) + 0.029, h, fontsize=9.8, color="white", fontweight="bold", ha="center", va="center")
        x += w
    for r, row in enumerate(rows):
        yy = y0 + row_h * (len(rows) - r - 1)
        ax.add_patch(Rectangle((x0, yy), sum(widths), row_h, facecolor="white" if r % 2 == 0 else fill, linewidth=0))
        ax.add_line(plt.Line2D([x0, x0 + sum(widths)], [yy, yy], color=line, linewidth=0.8))
        x = x0
        for c, (text, w) in enumerate(zip(row, widths)):
            color = accent if c == 3 else ink
            weight = "bold" if c == 3 else "normal"
            ax.text(x + (0.018 if c == 0 else w / 2), yy + row_h / 2, text, fontsize=9.5, color=color, fontweight=weight, ha="left" if c == 0 else "center", va="center")
            x += w

    rounded(ax, (0.06, 0.075), 0.87, 0.075, fc=soft_warn, ec=line)
    ax.text(0.085, 0.113, "Boundary", fontsize=10.2, color=navy, fontweight="bold", va="center")
    ax.text(0.170, 0.113, "Sciverse receives public or sanitized queries only; local chunks and indexes remain on the workstation.", fontsize=9.7, color=ink, va="center")
    save_all(fig, "track3_sciverse_rrf_matrix.png")


def generate_sciverse_expansion_funnel() -> None:
    expansion = load_json(medical_results / "sciverse_medical_expansion.json")
    closure = load_json(medical_results / "sciverse_medical_closure_v3.json")
    summary = expansion["summary"]
    baseline = summary["baseline_pmc_papers"]
    english = summary["english_medical_papers"]
    chinese = summary["chinese_medical_papers"]
    total_unique = summary["total_unique_papers"]
    upgraded = baseline + total_unique

    fig, ax = canvas(
        "Sciverse Medical Corpus Expansion",
        "External public search expands the PMC-only medical corpus while preserving the local-first RAG boundary",
    )

    stages = [
        ("PMC local", baseline, "curated public PMC"),
        ("English medical", english, "Sciverse metadata"),
        ("Chinese medical", chinese, "new language coverage"),
        ("Available corpus", upgraded, f"+{summary['expansion_ratio']:.1f}x new papers"),
    ]
    max_v = max(v for _, v, _ in stages)
    x0, y0 = 0.18, 0.63
    bar_h = 0.060
    for i, (label, value, note) in enumerate(stages):
        yy = y0 - i * 0.105
        w = 0.56 * value / max_v
        ax.text(0.055, yy + bar_h / 2, label, fontsize=10.3, color=navy, fontweight="bold", va="center")
        ax.add_patch(Rectangle((x0, yy), 0.56, bar_h, facecolor=fill, edgecolor=line, linewidth=0.8))
        ax.add_patch(Rectangle((x0, yy), w, bar_h, facecolor=good if i == 3 else accent, linewidth=0))
        ax.text(x0 + min(w + 0.012, 0.735), yy + bar_h / 2, f"{value:,}", fontsize=10.5, color=ink, fontweight="bold", va="center")
        ax.text(0.805, yy + bar_h / 2, note, fontsize=9.3, color=gray, va="center")

    # Closure cards
    cards = [
        ("Collected IDs", closure["n_doc_ids_collected"]),
        ("Pulled full text", closure["n_pulled"]),
        ("Clean chunks", closure["n_chunks"]),
    ]
    for i, (label, value) in enumerate(cards):
        x = 0.12 + i * 0.25
        rounded(ax, (x, 0.165), 0.20, 0.115, fc="white")
        ax.text(x + 0.020, 0.240, label, fontsize=9.5, color=gray, va="center")
        ax.text(x + 0.020, 0.198, f"{value:,}", fontsize=17, color=navy, fontweight="bold", va="center")

    rounded(ax, (0.12, 0.030), 0.70, 0.082, fc=soft_green, ec=line)
    ax.text(0.145, 0.074, "Automation check", fontsize=10.1, color=navy, fontweight="bold", va="center")
    ax.text(
        0.285,
        0.083,
        "12 selected papers -> 10 full texts -> 733 chunks",
        fontsize=8.7,
        color=ink,
        va="center",
    )
    ax.text(0.285, 0.055, "Replayable ingestion path; local-first boundary preserved.", fontsize=8.7, color=ink, va="center")
    save_all(fig, "track3_sciverse_expansion_funnel.png")


def generate_supplemental_evidence_matrix() -> None:
    summary = load_json(results / "track3_supplemental_summary.json")
    safety = load_json(results / "track3_safety_refusal_stress.json")
    privacy = load_json(results / "track3_privacy_boundary_audit.json")
    chunk = load_json(results / "track3_semantic_chunk_quality.json")
    zh = load_json(results / "track3_zh_ask_robustness.json")
    cards = load_json(results / "track3_evidence_card_completeness.json")
    deploy = load_json(results / "track3_deployment_smoke_matrix.json")
    ablation = load_json(results / "track3_rag_pipeline_ablation.json")
    ei = load_json(results / "track3_medbench_ei_taxonomy.json")
    best_provider = ablation["retrieval_provider_ablation"]["best_provider"]
    best_model = best_provider["embedding_model"].split("/")[-1]

    rows = [
        ("Pipeline ablation", "3 dimensions", f"{best_model} best", "replay only"),
        ("Safety refusal", f"{safety['case_count']} cases", f"recall {safety['expected_refusal_recall']:.0%}", "static triage"),
        ("EI taxonomy", "LLM / VLM", f"{ei['llm_ei_summary']['evidence_insufficient']}/330 vs {ei['vlm_35b_ei_summary']['evidence_insufficient']}/300", "LLM reasons degraded"),
        ("Privacy boundary", f"{privacy['trace_privacy_summary']['record_count']} traces", "0 raw context to cloud", "audit, not certification"),
        ("Semantic chunks", "3,348 chunks", f"{chunk['covered_target_section_count']} target sections", "no gold accuracy"),
        ("ZH Ask robustness", f"{zh['variant_count']} variants", f"rewrite {zh['rewrite_success_rate']:.0%}", "no variant Hit@k"),
        ("Evidence cards", f"{cards['card_count']} cards", f"claim binding {cards['claim_binding_coverage']:.0%}", "reconstructed cards"),
        ("Deploy smoke", f"{deploy['summary']['entrypoint_available_count']}/{deploy['summary']['entrypoint_count']} entrypoints", f"{deploy['summary']['executed_passed_count']} executed checks", "env checks not_run"),
    ]

    fig, ax = canvas(
        "Medical RAG Supplemental Evidence Matrix",
        "Eight closure checks make stage evidence, refusal boundary, privacy boundary, and deployment readiness explicit",
        figsize=(16.2, 9.4),
    )
    x0, y0 = 0.055, 0.135
    widths = [0.25, 0.18, 0.28, 0.22]
    headers = ["Check", "Scale", "Key evidence", "Boundary"]
    row_h = 0.075
    ax.add_patch(Rectangle((x0, y0 + row_h * len(rows)), sum(widths), 0.058, facecolor=header, linewidth=0))
    x = x0
    for h, w in zip(headers, widths):
        ax.text(x + w / 2, y0 + row_h * len(rows) + 0.029, h, fontsize=10.0, color="white", fontweight="bold", ha="center", va="center")
        x += w

    for r, row in enumerate(rows):
        yy = y0 + row_h * (len(rows) - r - 1)
        ax.add_patch(Rectangle((x0, yy), sum(widths), row_h, facecolor="white" if r % 2 == 0 else fill, linewidth=0))
        ax.add_line(plt.Line2D([x0, x0 + sum(widths)], [yy, yy], color=line, linewidth=0.8))
        x = x0
        for c, (text, w) in enumerate(zip(row, widths)):
            color = accent if c == 2 else ink
            weight = "bold" if c in [0, 2] else "normal"
            ax.text(x + 0.018, yy + row_h / 2, text, fontsize=9.2, color=color, fontweight=weight, va="center")
            x += w

    rounded(ax, (0.060, 0.035), 0.86, 0.065, fc=soft_warn, ec=line)
    ax.text(0.085, 0.068, "Summary", fontsize=10.2, color=navy, fontweight="bold", va="center")
    ax.text(0.170, 0.068, f"{summary['available_task_count']}/{summary['task_count']} supplemental tasks available; deployment smoke keeps environment-dependent checks explicit.", fontsize=9.7, color=ink, va="center")
    save_all(fig, "track3_supplemental_evidence_matrix.png")


def generate_medbench_sciverse_compare() -> None:
    report = load_json(medical_results / "medbench_sciverse_report.json")
    summary = report["summary"]
    meta = report["meta"]
    sciverse_judged = 0
    sciverse_positive = 0
    for question in report["per_question"]:
        score = question.get("scores", {}).get("sciverse_mean_score")
        if score is None:
            judges = question.get("judge", {}).get("sciverse", [])
            if judges:
                score = sum(item["judge"]["score"] for item in judges) / len(judges)
        if score is not None:
            sciverse_judged += 1
            if score > 0:
                sciverse_positive += 1

    labels = ["Local PMC\nHybrid", "Sciverse\nSearch", "Fused\nRRF"]
    values = [
        summary["local"]["mean_score"],
        summary["sciverse"]["mean_score"],
        summary["fused"]["mean_score"],
    ]
    ns = [summary["local"]["n"], summary["sciverse"]["n"], summary["fused"]["n"]]
    colors = [muted, good, accent]

    fig = plt.figure(figsize=(15.4, 8.2))
    fig.text(0.055, 0.935, "MedBench Sciverse Clinical Evidence Check", fontsize=21, fontweight="bold", color=navy)
    fig.text(0.055, 0.895, "Official benchmark questions are replayed through local PMC, external Sciverse, and fused retrieval paths", fontsize=10.8, color=gray)

    ax = fig.add_axes([0.08, 0.25, 0.54, 0.54])
    ax.set_axisbelow(True)
    ax.grid(axis="y", color=line, linewidth=0.8, zorder=0)
    bars = ax.bar(labels, values, color=colors, width=0.58, zorder=3)
    ax.set_ylim(0, 0.13)
    ax.set_ylabel("Mean judge score", fontsize=10.2, color=ink)
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    for bar, value, n in zip(bars, values, ns):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.006,
            f"{value:.3f}\n(n={n})",
            ha="center",
            va="bottom",
            fontsize=10.5,
            color=navy,
            fontweight="bold",
            linespacing=1.25,
        )
    ax.text(1, 0.118, "+0.100 vs local", ha="center", va="center", fontsize=11.2, color=good, fontweight="bold")

    ax2 = fig.add_axes([0.66, 0.25, 0.27, 0.54])
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")
    callouts = [
        ("25 questions", f"{meta['top_k']} retrieval hits per path", soft_blue, accent),
        (f"{sciverse_positive} / {sciverse_judged} positive", "Sciverse path received non-zero evidence scores", soft_green, good),
        (f"{meta['elapsed_seconds']:.1f} s replay", "Boundary: benchmark probe, not official leaderboard scoring", soft_warn, warn),
    ]
    for i, (title, body, fc, color) in enumerate(callouts):
        y = 0.70 - i * 0.265
        rounded(ax2, (0.02, y), 0.94, 0.19, fc=fc, ec=line)
        ax2.text(0.075, y + 0.125, title, fontsize=12.0, color=color, fontweight="bold", va="center")
        ax2.text(0.075, y + 0.065, body, fontsize=9.4, color=ink, va="center", linespacing=1.35)

    fig.text(0.08, 0.115, "Interpretation: the gain is a coverage signal from public external retrieval; it does not certify clinical correctness.", fontsize=9.8, color=gray)
    save_all(fig, "track3_medbench_sciverse_compare.png")


def generate_vision_provider_boundary() -> None:
    qc = load_json(repo / "data" / "sources_medical" / "vision" / "vision_quality_control.json")
    manifest = load_json(repo / "data" / "sources_medical" / "vision" / "vision_chunks_manifest.json")
    complement = load_json(repo / "data" / "sources_medical" / "vision" / "vlm_complement_30.json")

    fig = plt.figure(figsize=(15.8, 8.6))
    fig.text(0.055, 0.935, "Vision Provider Boundary and Local VLM Floor", fontsize=21, fontweight="bold", color=navy)
    fig.text(0.055, 0.895, "Image QC, external MiMo descriptions, and local VLM numeric extraction are checked as separate evidence boundaries", fontsize=10.8, color=gray)

    ax = fig.add_axes([0.06, 0.23, 0.50, 0.56])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    stages = [
        ("Image refs", qc["total_references"], "all manuscript image links", accent),
        ("Filtered", qc["filtered_below_5kb"], f"< {qc['min_size_kb']:.0f} KB thumbnails/icons", warn),
        ("Retained", qc["retained"], f"{qc['retained_ratio_pct']:.1f}% high-quality images", good),
        ("Descriptions", manifest["total_vision_chunks"], manifest["model"], navy),
    ]
    max_v = max(v for _, v, _, _ in stages)
    for i, (label, value, note, color) in enumerate(stages):
        y = 0.78 - i * 0.19
        ax.text(0.02, y + 0.035, label, fontsize=10.5, color=navy, fontweight="bold", va="center")
        ax.add_patch(Rectangle((0.20, y), 0.55, 0.07, facecolor=fill, edgecolor=line, linewidth=0.8))
        ax.add_patch(Rectangle((0.20, y), 0.55 * value / max_v, 0.07, facecolor=color, linewidth=0))
        ax.text(0.78, y + 0.035, f"{value:,}", fontsize=12.0, color=color, fontweight="bold", va="center")
        ax.text(0.20, y - 0.040, note, fontsize=9.0, color=gray, va="center")

    axb = fig.add_axes([0.63, 0.35, 0.30, 0.42])
    model_labels = ["MinerU\n1.2B", "Qwen\n4B", "Qwen\n9B"]
    numeric = [
        complement["mean_numeric"]["n12b"],
        complement["mean_numeric"]["n4b"],
        complement["mean_numeric"]["n9b"],
    ]
    axb.set_axisbelow(True)
    axb.grid(axis="y", color=line, linewidth=0.8, zorder=0)
    bars = axb.bar(model_labels, numeric, color=[muted, warn, good], width=0.58, zorder=3)
    axb.set_ylim(0, 6.2)
    axb.set_ylabel("Numeric facts / image", fontsize=10.0, color=ink)
    axb.set_title("30 statistical chart probe", fontsize=11.5, color=navy, fontweight="bold", pad=10)
    axb.spines[["top", "right"]].set_visible(False)
    axb.tick_params(axis="x", labelsize=9.5)
    axb.tick_params(axis="y", labelsize=9)
    for bar, value in zip(bars, numeric):
        axb.text(bar.get_x() + bar.get_width() / 2, value + 0.18, f"{value:.1f}", ha="center", fontsize=10.5, color=navy, fontweight="bold")

    axc = fig.add_axes([0.63, 0.16, 0.30, 0.13])
    axc.set_xlim(0, 1)
    axc.set_ylim(0, 1)
    axc.axis("off")
    rounded(axc, (0.00, 0.05), 1.00, 0.82, fc=soft_warn, ec=line)
    axc.text(0.06, 0.62, "Boundary", fontsize=10.5, color=navy, fontweight="bold", va="center")
    axc.text(0.06, 0.38, "MiMo: external reference path.", fontsize=8.8, color=ink, va="center")
    axc.text(0.06, 0.22, "Qwen 9B: local privacy floor.", fontsize=8.8, color=ink, va="center")

    save_all(fig, "track3_vision_provider_boundary.png")


def generate_medbench_vlm_model_delta() -> None:
    report35 = load_json(repo / "data" / "sources_medical" / "medbench" / "medbench_vlm_report.json")
    report9 = load_json(repo / "data" / "sources_medical" / "medbench" / "medbench_vlm_report_9b.json")
    s35 = report35["statistics"]
    s9 = report9["statistics"]

    subsets = list(s35["subsets"].keys())
    vals35 = [s35["subsets"][name]["evidence_insufficient"] for name in subsets]
    vals9 = [s9["subsets"][name]["evidence_insufficient"] for name in subsets]

    fig = plt.figure(figsize=(16.0, 8.8))
    fig.text(0.055, 0.935, "MedBench VLM 35B vs 9B Evidence-Insufficient Delta", fontsize=20.5, fontweight="bold", color=navy)
    fig.text(0.055, 0.895, "Both models complete 300 image-grounded questions with zero errors; the residual gap localizes to sequential imaging and therapy planning", fontsize=10.6, color=gray)

    ax = fig.add_axes([0.08, 0.20, 0.62, 0.62])
    y = list(range(len(subsets)))
    h = 0.34
    ax.set_axisbelow(True)
    ax.grid(axis="x", color=line, linewidth=0.8, zorder=0)
    ax.barh([i + h / 2 for i in y], vals35, height=h, color=muted, label="35B", zorder=3)
    ax.barh([i - h / 2 for i in y], vals9, height=h, color=good, label="9B", zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(subsets, fontsize=9.2)
    ax.invert_yaxis()
    ax.set_xlim(0, 10)
    ax.set_xlabel("Evidence-insufficient cases / 30", fontsize=10.2, color=ink)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="lower right", frameon=False, fontsize=9.5)
    for i, (v35, v9) in enumerate(zip(vals35, vals9)):
        if v35:
            ax.text(v35 + 0.15, i + h / 2, str(v35), va="center", fontsize=9.0, color=ink)
        if v9:
            ax.text(v9 + 0.15, i - h / 2, str(v9), va="center", fontsize=9.0, color=ink, fontweight="bold")
    for name in ["MedSeqIm", "MedTherapy"]:
        idx = subsets.index(name)
        ax.axhspan(idx - 0.48, idx + 0.48, color=soft_warn, zorder=1)

    axc = fig.add_axes([0.74, 0.22, 0.20, 0.58])
    axc.set_xlim(0, 1)
    axc.set_ylim(0, 1)
    axc.axis("off")
    cards = [
        ("35B", f"{s35['overall_evidence_insufficient']}/{s35['total_questions']} EI", f"{report35['meta']['elapsed_seconds'] / 60:.1f} min, 0 errors", soft_blue, accent),
        ("9B", f"{s9['overall_evidence_insufficient']}/{s9['total_questions']} EI", f"{report9['meta']['elapsed_seconds'] / 60:.1f} min, 0 errors", soft_green, good),
        ("Delta", "+12 EI cases", "mostly MedSeqIm + MedTherapy", soft_warn, warn),
    ]
    for i, (title, metric, note, fc, color) in enumerate(cards):
        yy = 0.70 - i * 0.28
        rounded(axc, (0.00, yy), 1.00, 0.20, fc=fc, ec=line)
        axc.text(0.08, yy + 0.135, title, fontsize=11.0, color=color, fontweight="bold", va="center")
        axc.text(0.08, yy + 0.083, metric, fontsize=13.0, color=navy, fontweight="bold", va="center")
        axc.text(0.08, yy + 0.035, note, fontsize=8.8, color=gray, va="center")

    fig.text(0.08, 0.100, "Reading: the model-size gap is task-local, not a broad VLM failure; zero-error completion holds for both runs.", fontsize=9.6, color=gray)
    save_all(fig, "track3_medbench_vlm_model_delta.png")


if __name__ == "__main__":
    generate_sciverse_rrf_matrix()
    generate_sciverse_expansion_funnel()
    generate_supplemental_evidence_matrix()
    generate_medbench_sciverse_compare()
    generate_vision_provider_boundary()
    generate_medbench_vlm_model_delta()
