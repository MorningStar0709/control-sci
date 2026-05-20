"""Report completeness commands."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.table import Table

from controlsci.cli.common import PROJECT_ROOT, console, print_json


app = typer.Typer(help="检查报告、图表和提交产物完整性。")


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
    ("共享图片目录", "docs/submissions/shared/assets", False),
    ("PPT 素材目录", "_ppt_materials_tracks", False),
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
