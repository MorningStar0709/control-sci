"""Report completeness commands."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.table import Table

from controlsci.cli.common import PROJECT_ROOT, console, print_json


app = typer.Typer(help="检查报告、图表和提交产物完整性。")


KEY_FIGURE_ITEMS = [
    ("Track1 Sciverse dashboard 图", "docs/submissions/shared/assets/task1/track1_sciverse_validation_dashboard.png", True),
    ("Track1 supplemental matrix 图", "docs/submissions/shared/assets/task1/track1_supplemental_evidence_matrix.png", True),
    ("Track1 training utility 图", "docs/submissions/shared/assets/task1/track1_training_utility_ablation.png", True),
    ("Track2 reliability matrix 图", "docs/submissions/shared/assets/task2/track2_agent_reliability_matrix.png", True),
    ("Track2 failure recovery 图", "docs/submissions/shared/assets/task2/track2_failure_recovery_matrix.png", True),
    ("Track2 source selection 图", "docs/submissions/shared/assets/task2/track2_source_selection_ablation.png", True),
    ("Track2 resource Pareto 图", "docs/submissions/shared/assets/task2/track2_resource_pareto.png", True),
    ("Track2 hard document 图", "docs/submissions/shared/assets/task2/track2_hard_document_stress.png", True),
    ("Track2 Sciverse routing 图", "docs/submissions/shared/assets/task2/track2_sciverse_source_routing.png", True),
    ("Track3 RRF matrix 图", "docs/submissions/shared/assets/task3/track3_sciverse_rrf_matrix.png", True),
    ("Track3 MedBench compare 图", "docs/submissions/shared/assets/task3/track3_medbench_sciverse_compare.png", True),
    ("Track3 expansion funnel 图", "docs/submissions/shared/assets/task3/track3_sciverse_expansion_funnel.png", True),
    ("Track3 vision boundary 图", "docs/submissions/shared/assets/task3/track3_vision_provider_boundary.png", True),
    ("Track3 VLM delta 图", "docs/submissions/shared/assets/task3/track3_medbench_vlm_model_delta.png", True),
    ("Track3 supplemental matrix 图", "docs/submissions/shared/assets/task3/track3_supplemental_evidence_matrix.png", True),
    ("Final Track1 dashboard 图", "_final_submission_by_track/track1_sci_align/shared/assets/track1_sciverse_validation_dashboard.png", True),
    ("Final Track2 resource Pareto 图", "_final_submission_by_track/track2_agent/shared/assets/track2_resource_pareto.png", True),
    ("Final Track3 RRF matrix 图", "_final_submission_by_track/track3_medical_rag/shared/assets/track3_sciverse_rrf_matrix.png", True),
]


REPORT_ITEMS = [
    ("提交包 README", "docs/submissions/README.md", True),
    ("Quickstart", "docs/submissions/quickstart.md", True),
    ("Track1 技术报告", "docs/submissions/track1_sci_align_report.md", True),
    ("Track2 技术报告", "docs/submissions/track2_agent_report.md", True),
    ("Track3 技术报告", "docs/submissions/track3_medical_rag_report.md", True),
    ("DATA-TRACE", "docs/submissions/shared/DATA-TRACE.md", True),
    ("Track1 20 cases", "docs/submissions/shared/track1_sci_align_20_cases.md", True),
    ("Track2 20 cases", "docs/submissions/shared/track2_agent_20_cases.md", True),
    ("Track3 20 cases", "docs/submissions/shared/track3_medical_rag_20_cases.md", True),
    ("验收包 manifest", "docs/submissions/data_trace_bundle/manifest.json", True),
    ("Track3 supplemental summary", "benchmark/eval/results/track3_supplemental_summary.json", True),
    ("Track3 supplemental bundle", "docs/submissions/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental", True),
    ("Track3 final supplemental bundle", "_final_submission_by_track/track3_medical_rag/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental", True),
    ("共享图片目录", "docs/submissions/shared/assets", False),
    ("PPT 素材目录", "_ppt_materials_tracks", False),
    *KEY_FIGURE_ITEMS,
]


def collect_report_status() -> dict:
    items = []
    for label, rel_path, required in REPORT_ITEMS:
        path = PROJECT_ROOT / rel_path
        items.append(
            {
                "label": label,
                "path": rel_path,
                "required": required,
                "available": path.exists(),
                "size_kb": path.stat().st_size // 1024 if path.is_file() else 0,
            }
        )
    return {
        "status": "ok" if all(item["available"] for item in items if item["required"]) else "degraded",
        "items": items,
    }


@app.command("status")
def status(
    json_output: Annotated[bool, typer.Option("--json", help="输出 JSON。")] = False,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="将 JSON 以 UTF-8 写入文件。")] = None,
) -> None:
    payload = collect_report_status()
    if json_output or output:
        print_json(payload, output=output)
        return

    table = Table(title="ControlMind Report Status")
    table.add_column("产物", style="cyan")
    table.add_column("状态")
    table.add_column("路径")
    for item in payload["items"]:
        status_text = "[green]OK[/green]" if item["available"] else ("[red]MISS[/red]" if item["required"] else "[yellow]OPTIONAL[/yellow]")
        table.add_row(item["label"], status_text, item["path"])
    console.print(table)
    console.print(f"整体状态：{payload['status']}")
