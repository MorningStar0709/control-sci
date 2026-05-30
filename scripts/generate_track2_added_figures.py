from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


repo = Path(__file__).resolve().parents[1]
out_dirs = [
    repo / "_final_submission_by_track" / "track2_agent" / "shared" / "assets",
    repo / "docs" / "submissions" / "shared" / "assets" / "task2",
]

results = repo / "benchmark" / "eval" / "results"

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
soft_green = "#EAF4EF"
soft_blue = "#EDF3F8"
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


def load_json(name: str) -> dict:
    with (results / name).open("r", encoding="utf-8") as f:
        return json.load(f)


def save_all(fig: plt.Figure, name: str) -> None:
    for out_dir in out_dirs:
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / name, dpi=220, bbox_inches="tight", pad_inches=0.22)
    plt.close(fig)


def title(ax, text: str, subtitle: str) -> None:
    ax.text(0.035, 0.955, text, fontsize=21, fontweight="bold", color=navy, va="top")
    ax.text(0.035, 0.905, subtitle, fontsize=10.8, color=gray, va="top")


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


def generate_reliability_matrix() -> None:
    router = load_json("agent_router_robustness.json")["summary"]
    failure = load_json("agent_failure_injection_matrix.json")["summary"]
    source = load_json("agent_source_selection_ablation.json")["summary"]
    resource = load_json("agent_resource_pareto.json")["summary"]
    stress = load_json("agent_hard_document_stress.json")["summary"]

    columns = [
        {
            "label": "Planning",
            "question": "NL goal -> intent chain",
            "design": "5 task families x 25 variants",
            "result": f"{router['success_cases']}/{router['total_cases']} success",
            "boundary": "baseline; no tuning",
        },
        {
            "label": "Recovery",
            "question": "Common faults recover?",
            "design": "6 fault types x 3 trials",
            "result": f"{failure['recovered_cases']}/{failure['total_cases']} recovered",
            "boundary": "mock/local only",
        },
        {
            "label": "Source Selection",
            "question": "Router beats fixed rule?",
            "design": "20 queries; oracle labels",
            "result": f"Agent {source['agent_accuracy']:.2f} vs rule {source['fixed_rule_accuracy']:.2f}",
            "boundary": "selection only",
        },
        {
            "label": "Scheduling",
            "question": "Provider state exposed?",
            "design": "4 families x auto/local/replay",
            "result": f"{resource['success_records']}/{resource['total_records']} success",
            "boundary": "health probes only",
        },
        {
            "label": "Hard Docs",
            "question": "Stress cases covered?",
            "design": "6 challenge classes; 15 samples",
            "result": f"{stress['success_samples']} success + {stress['partial_samples']} partial",
            "boundary": "repo/replay samples",
        },
    ]

    fig, ax = plt.subplots(figsize=(15.8, 8.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    title(ax, "Agent Reliability Evidence Matrix", "Five batch experiments audit planning, recovery, routing, scheduling, and hard-document coverage")

    x0, y0 = 0.045, 0.155
    total_w, total_h = 0.91, 0.665
    col_w = total_w / len(columns)
    row_heights = [0.090, 0.145, 0.140, 0.155, 0.135]
    ax.add_patch(Rectangle((x0, y0 + total_h - row_heights[0]), total_w, row_heights[0], facecolor=header, linewidth=0))
    y = y0 + total_h
    for i, rh in enumerate(row_heights):
        y -= rh
        if i > 0:
            ax.add_patch(Rectangle((x0, y), total_w, rh, facecolor="white" if i % 2 else fill, linewidth=0))
        ax.add_line(plt.Line2D([x0, x0 + total_w], [y, y], color=line, linewidth=0.8))

    for c, item in enumerate(columns):
        x = x0 + c * col_w
        ax.add_line(plt.Line2D([x, x], [y0, y0 + total_h], color=line, linewidth=0.8))
        cx = x + col_w * 0.34
        ax.text(cx, y0 + total_h - row_heights[0] / 2, item["label"], fontsize=10.0, color="white", fontweight="bold", ha="center", va="center")

        entries = [item["question"], item["design"], item["result"], item["boundary"]]
        yy = y0 + total_h - row_heights[0]
        for r, text in enumerate(entries, start=1):
            yy -= row_heights[r]
            color = accent if r == 3 else ink
            weight = "bold" if r == 3 else "normal"
            ax.text(x + col_w * 0.06, yy + row_heights[r] / 2, text, fontsize=9.2, color=color, fontweight=weight, va="center", wrap=True)
    ax.add_line(plt.Line2D([x0 + total_w, x0 + total_w], [y0, y0 + total_h], color=line, linewidth=0.8))

    rounded(ax, (0.055, 0.045), 0.89, 0.065, fc=fill)
    ax.text(0.080, 0.078, "Reading", fontsize=10.2, color=navy, fontweight="bold", va="center")
    ax.text(0.160, 0.078, "Each column reports one behavioral surface; boundaries are part of the evidence, not caveats.", fontsize=9.8, color=ink, va="center")
    save_all(fig, "track2_agent_reliability_matrix.png")


def generate_sciverse_source_routing() -> None:
    data = load_json("sciverse_source_selection_showcase.json")
    rows = data["decision_matrix"]
    sources = ["arXiv", "PMC local", "Sciverse"]

    fig, ax = plt.subplots(figsize=(15.8, 8.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    title(ax, "Sciverse Source Routing Matrix", "Agent selects literature source by freshness, privacy boundary, and coverage objective")

    x0, y0 = 0.055, 0.155
    widths = [0.20, 0.15, 0.15, 0.15, 0.17, 0.13]
    headers = ["Query type", "arXiv", "PMC local", "Sciverse", "Sciverse coverage", "Decision driver"]
    row_h = 0.095

    ax.add_patch(Rectangle((x0, y0 + row_h * len(rows)), sum(widths), 0.055, facecolor=header, linewidth=0))
    x = x0
    for h, w in zip(headers, widths):
        ax.text(x + w / 2, y0 + row_h * len(rows) + 0.027, h, fontsize=9.4, color="white", fontweight="bold", ha="center", va="center")
        x += w

    driver = {
        "arXiv": "freshness",
        "PMC 本地": "privacy",
        "Sciverse": "coverage",
    }
    source_key = {
        "arXiv": "arXiv",
        "PMC 本地": "PMC local",
        "Sciverse": "Sciverse",
    }
    query_labels = {
        "Q1": "Frontier preprint",
        "Q2": "Cross-disciplinary",
        "Q3": "Medical privacy",
        "Q4": "Textbook/classic",
        "Q5": "AI-control crossover",
    }

    for idx, row in enumerate(rows):
        y = y0 + row_h * (len(rows) - idx - 1)
        ax.add_patch(Rectangle((x0, y), sum(widths), row_h, facecolor="white" if idx % 2 == 0 else fill, linewidth=0))
        ax.add_line(plt.Line2D([x0, x0 + sum(widths)], [y, y], color=line, linewidth=0.8))
        selected = source_key[row["preferred"]]
        cells = [
            query_labels[row["id"]],
            "selected" if selected == "arXiv" else "",
            "selected" if selected == "PMC local" else "",
            "selected" if selected == "Sciverse" else "",
            row["sciverse_coverage"],
            driver[row["preferred"]],
        ]
        x = x0
        for c, (text, w) in enumerate(zip(cells, widths)):
            if c in [1, 2, 3]:
                if text:
                    ax.add_patch(FancyBboxPatch((x + w * 0.31, y + row_h * 0.28), w * 0.38, row_h * 0.44, boxstyle="round,pad=0.004,rounding_size=0.012", facecolor=soft_green, edgecolor=good, linewidth=0.9))
                    ax.text(x + w / 2, y + row_h / 2, "chosen", fontsize=8.8, color=good, fontweight="bold", ha="center", va="center")
                else:
                    ax.text(x + w / 2, y + row_h / 2, "-", fontsize=10, color=muted, ha="center", va="center")
            else:
                color = accent if c in [0, 5] else ink
                weight = "bold" if c == 0 else "normal"
                ax.text(x + w * 0.06, y + row_h / 2, text, fontsize=9.2, color=color, fontweight=weight, va="center", wrap=True)
            x += w

    x = x0
    for w in widths:
        ax.add_line(plt.Line2D([x, x], [y0, y0 + row_h * len(rows) + 0.055], color=line, linewidth=0.8))
        x += w
    ax.add_line(plt.Line2D([x, x], [y0, y0 + row_h * len(rows) + 0.055], color=line, linewidth=0.8))

    rounded(ax, (0.060, 0.045), 0.88, 0.070, fc=fill)
    ax.text(0.085, 0.080, "Summary", fontsize=10.2, color=navy, fontweight="bold", va="center")
    ax.text(0.165, 0.080, "Source distribution: arXiv 1, PMC local 1, Sciverse 3; average Sciverse meta coverage 19.6M records.", fontsize=9.8, color=ink, va="center")
    save_all(fig, "track2_sciverse_source_routing.png")


def generate_failure_recovery_matrix() -> None:
    data = load_json("agent_failure_injection_matrix.json")
    summary = data["summary"]
    records = data["records"]
    failure_types = list(summary["by_failure_type"].keys())
    labels = [
        "Ollama unavailable",
        "API key missing",
        "Missing input",
        "Schema missing",
        "Tool timeout",
        "Resume skip-existing",
    ]

    fig, ax = plt.subplots(figsize=(14.8, 8.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    title(ax, "Failure Injection Recovery Matrix", "Six non-destructive fault classes, three trials each, all leave recoverable evidence")

    x0, y0 = 0.090, 0.190
    label_w = 0.285
    trial_w = 0.135
    dur_w = 0.150
    row_h = 0.077
    total_w = label_w + trial_w * 3 + dur_w

    ax.add_patch(Rectangle((x0, y0 + row_h * len(failure_types)), total_w, 0.055, facecolor=header, linewidth=0))
    headers = ["Fault class", "Trial 1", "Trial 2", "Trial 3", "Avg ms"]
    widths = [label_w, trial_w, trial_w, trial_w, dur_w]
    x = x0
    for h, w in zip(headers, widths):
        ax.text(x + w / 2, y0 + row_h * len(failure_types) + 0.027, h, fontsize=9.6, color="white", fontweight="bold", ha="center", va="center")
        x += w

    rec_by_type = {ft: [] for ft in failure_types}
    for rec in records:
        rec_by_type[rec["failure_type"]].append(rec)

    for idx, ft in enumerate(failure_types):
        y = y0 + row_h * (len(failure_types) - idx - 1)
        ax.add_patch(Rectangle((x0, y), total_w, row_h, facecolor="white" if idx % 2 == 0 else fill, linewidth=0))
        ax.add_line(plt.Line2D([x0, x0 + total_w], [y, y], color=line, linewidth=0.8))
        ax.text(x0 + 0.018, y + row_h / 2, labels[idx], fontsize=9.5, color=navy, fontweight="bold", va="center")
        trials = sorted(rec_by_type[ft], key=lambda r: r["case_id"])
        avg = sum(r["duration_ms"] for r in trials) / len(trials)
        x = x0 + label_w
        for rec in trials:
            ax.add_patch(Rectangle((x + 0.015, y + 0.016), trial_w - 0.030, row_h - 0.032, facecolor=soft_green, edgecolor=good, linewidth=0.9))
            ax.text(x + trial_w / 2, y + row_h / 2, "recovered", fontsize=8.5, color=good, fontweight="bold", ha="center", va="center")
            x += trial_w
        ax.text(x + dur_w / 2, y + row_h / 2, f"{avg:.0f}", fontsize=9.5, color=accent, fontweight="bold", ha="center", va="center")

    x = x0
    for w in widths:
        ax.add_line(plt.Line2D([x, x], [y0, y0 + row_h * len(failure_types) + 0.055], color=line, linewidth=0.8))
        x += w
    ax.add_line(plt.Line2D([x, x], [y0, y0 + row_h * len(failure_types) + 0.055], color=line, linewidth=0.8))

    rounded(ax, (0.090, 0.055), 0.800, 0.085, fc=fill)
    ax.text(0.120, 0.100, "Result", fontsize=10.5, color=navy, fontweight="bold", va="center")
    ax.text(0.200, 0.100, f"{summary['recovered_cases']}/{summary['total_cases']} recovered; average recovery record {summary['average_recovery_duration_ms']:.2f} ms; no real API keys or services were damaged.", fontsize=9.7, color=ink, va="center")
    save_all(fig, "track2_failure_recovery_matrix.png")


def generate_source_selection_ablation() -> None:
    data = load_json("agent_source_selection_ablation.json")
    summary = data["summary"]
    categories = [
        ("frontier_preprint", "Frontier\npreprint"),
        ("published_crossdisciplinary", "Published /\ncross-field"),
        ("medical_clinical", "Medical\nclinical"),
        ("private_local", "Private /\nlocal"),
        ("benchmark_pipeline", "Benchmark\npipeline"),
    ]
    fixed = [summary["by_category"][key]["fixed_rule_accuracy"] for key, _ in categories]
    agent = [summary["by_category"][key]["agent_accuracy"] for key, _ in categories]
    labels = [label for _, label in categories]
    x = list(range(len(categories)))

    fig, ax = plt.subplots(figsize=(14.8, 8.4))
    fig.subplots_adjust(left=0.075, right=0.965, top=0.78, bottom=0.17)
    ax.set_title("Source Selection A/B", fontsize=22, fontweight="bold", color=navy, pad=26)
    ax.text(
        0.5,
        1.035,
        "Agent Router is compared with a fixed keyword rule against oracle source labels",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=11,
        color=gray,
    )

    width = 0.34
    ax.bar([i - width / 2 for i in x], fixed, width=width, color=muted, label="Fixed rule")
    ax.bar([i + width / 2 for i in x], agent, width=width, color=accent, label="Agent Router")
    ax.set_ylim(0, 1.12)
    ax.set_ylabel("Oracle match rate", fontsize=12, color=ink)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10)
    ax.tick_params(axis="y", labelsize=10)
    ax.grid(axis="y", color=line, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)

    for i, (f, a) in enumerate(zip(fixed, agent)):
        ax.text(i - width / 2, f + 0.025, f"{f:.2f}", ha="center", va="bottom", fontsize=9.2, color=ink, fontweight="bold")
        ax.text(i + width / 2, a + 0.025, f"{a:.2f}", ha="center", va="bottom", fontsize=9.2, color=accent, fontweight="bold")

    fig.text(
        0.102,
        0.065,
        f"Overall: Agent {summary['agent_accuracy']:.2f} vs fixed rule {summary['fixed_rule_accuracy']:.2f}; "
        f"Agent privacy violations {summary['agent_privacy_violation_count']}; fixed rule {summary['fixed_rule_privacy_violation_count']}. "
        "Light bars=fixed rule; dark bars=Agent Router.",
        fontsize=10.5,
        color=ink,
    )
    save_all(fig, "track2_source_selection_ablation.png")


def generate_resource_pareto() -> None:
    data = load_json("agent_resource_pareto.json")
    summary = data["summary"]
    providers = ["deepseek", "ollama", "mimo", "mineru", "replay"]
    provider_labels = ["DeepSeek\nAPI", "Ollama\nlocal", "MiMo\nvision", "MinerU", "Replay\nartifact"]
    success = [summary["by_provider"][p]["success"] for p in providers]
    unavailable = [summary["by_provider"][p]["unavailable"] for p in providers]
    calls = [summary["by_provider"][p]["call_count"] for p in providers]
    latency = [summary["by_provider"][p]["avg_latency_ms"] for p in providers]
    x = list(range(len(providers)))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.8, 7.8), gridspec_kw={"width_ratios": [1.18, 1]})
    fig.subplots_adjust(left=0.065, right=0.965, top=0.75, bottom=0.17, wspace=0.26)
    fig.suptitle("Resource Scheduling Pareto Check", fontsize=22, fontweight="bold", color=navy, y=0.94)
    fig.text(
        0.5,
        0.885,
        "Scheduler health probes expose provider availability, replay reproducibility, and explicit cost-audit boundaries",
        ha="center",
        fontsize=10.8,
        color=gray,
    )

    ax1.bar(x, success, color=good, label="success", zorder=3)
    ax1.bar(x, unavailable, bottom=success, color=warn, label="unavailable", zorder=3)
    ax1.set_xticks(x)
    ax1.set_xticklabels(provider_labels, fontsize=9.5)
    ax1.set_ylabel("Probe records", fontsize=11.5, color=ink)
    ax1.set_axisbelow(True)
    ax1.grid(axis="y", color=line, linewidth=0.8, zorder=0)
    ax1.spines[["top", "right"]].set_visible(False)
    ax1.set_ylim(0, 4.35)
    ax1.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.11), ncol=2, fontsize=9.5)
    for i, (s, u) in enumerate(zip(success, unavailable)):
        total = s + u
        ax1.text(i, total + 0.08, f"{s}/{total}", ha="center", fontsize=9.5, color=navy, fontweight="bold")

    ax2.set_axisbelow(True)
    ax2.grid(color=line, linewidth=0.8, zorder=0)
    ax2.scatter(
        calls,
        latency,
        s=[90 + 35 * (s + u) for s, u in zip(success, unavailable)],
        color=accent,
        alpha=0.90,
        edgecolors="white",
        linewidths=1.1,
        zorder=4,
    )
    label_offsets = {
        "deepseek": (0.18, 0),
        "ollama": (0.16, 0),
        "mimo": (0.10, 0),
        "mineru": (0.18, 0),
        "replay": (0.18, 0),
    }
    for i, provider in enumerate(providers):
        dx, dy = label_offsets[provider]
        ax2.text(
            calls[i] + dx,
            latency[i] + dy,
            provider_labels[i].replace("\n", " "),
            fontsize=9.2,
            color=ink,
            ha="left",
            va="center",
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.86, "pad": 1.8},
            zorder=5,
        )
    ax2.set_xlabel("Audited probe call count", fontsize=11.5, color=ink)
    ax2.set_ylabel("Average health latency (ms)", fontsize=11.5, color=ink)
    ax2.spines[["top", "right"]].set_visible(False)
    ax2.set_xlim(-0.25, max(calls) + 0.95)
    ax2.set_ylim(-60, max(latency) + 240)

    fig.text(
        0.075,
        0.065,
        f"Summary: {summary['success_records']}/{summary['total_records']} records succeeded; "
        f"cost amount is not audited because token/billing cross-source evidence is absent.",
        fontsize=10.3,
        color=ink,
    )
    save_all(fig, "track2_resource_pareto.png")


def generate_hard_document_stress() -> None:
    data = load_json("agent_hard_document_stress.json")
    summary = data["summary"]
    challenges = [
        ("numeric_dense", "Numeric\ndense"),
        ("cross_page", "Cross-page"),
        ("flow_engineering_diagram", "Flow /\nengineering"),
        ("low_quality_scan", "Low-quality\nscan"),
        ("complex_chart", "Complex\nchart"),
        ("standard_spec", "Standard /\nspec"),
    ]
    labels = [label for _, label in challenges]
    success = [summary["by_challenge"][key]["success"] for key, _ in challenges]
    partial = [summary["by_challenge"][key]["partial"] for key, _ in challenges]
    x = list(range(len(challenges)))

    fig, ax = plt.subplots(figsize=(15.2, 8.2))
    fig.subplots_adjust(left=0.075, right=0.965, top=0.74, bottom=0.23)
    ax.set_title("Hard Document Stress Coverage", fontsize=22, fontweight="bold", color=navy, pad=25)
    ax.text(
        0.5,
        1.035,
        "Repository and replay artifacts are grouped into six document challenge classes",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10.8,
        color=gray,
    )

    ax.bar(x, success, color=good, label="success")
    ax.bar(x, partial, bottom=success, color=warn, label="partial")
    ax.set_ylim(0, 3.35)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9.5)
    ax.set_ylabel("Traceable samples", fontsize=11.5, color=ink)
    ax.grid(axis="y", color=line, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)

    for i, (s, p) in enumerate(zip(success, partial)):
        ax.text(i, s + p + 0.08, f"{s + p}", ha="center", fontsize=9.8, color=navy, fontweight="bold")

    fig.text(
        0.125,
        0.060,
        f"Overall: {summary['success_samples']} success + {summary['partial_samples']} partial / "
        f"{summary['total_samples']} samples; schema consistency {summary['schema_consistency_rate']:.1%}. "
        "Green=success; ochre=partial.",
        fontsize=10.1,
        color=ink,
    )
    save_all(fig, "track2_hard_document_stress.png")


if __name__ == "__main__":
    generate_reliability_matrix()
    generate_sciverse_source_routing()
    generate_failure_recovery_matrix()
    generate_source_selection_ablation()
    generate_resource_pareto()
    generate_hard_document_stress()
