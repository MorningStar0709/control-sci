"""Track3 Medical RAG commands."""

from __future__ import annotations

from typing import Annotated
import json
import subprocess
from pathlib import Path

import typer

from controlsci.cli.common import call_quiet, console, print_json, run_command, current_python, PROJECT_ROOT


app = typer.Typer(help="医学 RAG 索引、检索、问答与评测。")
supplemental_app = typer.Typer(help="Track 3 补充实验状态、摘要与复跑入口。")

SUPPLEMENTAL_EXPERIMENTS = {
    "deployment-smoke": {
        "module": "benchmark.eval.track3_deployment_smoke_matrix",
        "output": "benchmark/eval/results/track3_deployment_smoke_matrix.json",
        "summary_output": "benchmark/eval/results/track3_supplemental_summary.json",
    }
}

SUPPLEMENTAL_EVIDENCE_FILES = [
    "benchmark/eval/results/track3_rag_pipeline_ablation.json",
    "benchmark/eval/results/track3_safety_refusal_stress.json",
    "benchmark/eval/results/track3_medbench_ei_taxonomy.json",
    "benchmark/eval/results/track3_privacy_boundary_audit.json",
    "benchmark/eval/results/track3_semantic_chunk_quality.json",
    "benchmark/eval/results/track3_zh_ask_robustness.json",
    "benchmark/eval/results/track3_evidence_card_completeness.json",
    "benchmark/eval/results/track3_deployment_smoke_matrix.json",
    "benchmark/eval/results/track3_supplemental_summary.json",
]

SUPPLEMENTAL_FIGURES = [
    "docs/submissions/shared/assets/task3/track3_sciverse_rrf_matrix.png",
    "docs/submissions/shared/assets/task3/track3_medbench_sciverse_compare.png",
    "docs/submissions/shared/assets/task3/track3_sciverse_expansion_funnel.png",
    "docs/submissions/shared/assets/task3/track3_vision_provider_boundary.png",
    "docs/submissions/shared/assets/task3/track3_medbench_vlm_model_delta.png",
    "docs/submissions/shared/assets/task3/track3_supplemental_evidence_matrix.png",
    "_final_submission_by_track/track3_medical_rag/shared/assets/track3_sciverse_rrf_matrix.png",
    "_final_submission_by_track/track3_medical_rag/shared/assets/track3_medbench_sciverse_compare.png",
    "_final_submission_by_track/track3_medical_rag/shared/assets/track3_sciverse_expansion_funnel.png",
    "_final_submission_by_track/track3_medical_rag/shared/assets/track3_vision_provider_boundary.png",
    "_final_submission_by_track/track3_medical_rag/shared/assets/track3_medbench_vlm_model_delta.png",
    "_final_submission_by_track/track3_medical_rag/shared/assets/track3_supplemental_evidence_matrix.png",
]


@app.command("index")
def index(
    check: Annotated[bool, typer.Option("--check", help="只检查现有索引，不重建。")] = True,
    rebuild: Annotated[bool, typer.Option("--rebuild", help="重建索引。")] = False,
    json_output: Annotated[bool, typer.Option("--json", help="输出 JSON。")] = False,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="将 JSON 以 UTF-8 写入文件。")] = None,
) -> None:
    if rebuild:
        run_command([current_python(), "-m", "controlsci.medical.indexing"], cwd=PROJECT_ROOT)
        return
    from controlsci.api.medical_rag import health as rag_health

    payload = rag_health()
    if json_output or output:
        print_json(payload, output=output)
        return
    console.print(f"Medical RAG 索引状态：{payload.get('status')}")
    for key, value in payload.get("components", {}).items():
        console.print(f"- {key}: {value}")


@app.command("search")
def search_cmd(
    query: Annotated[str, typer.Argument(help="检索问题。")],
    k: Annotated[int, typer.Option("--k", help="返回数量。")] = 5,
    mode: Annotated[str, typer.Option("--mode", help="dense | bm25 | hybrid | vision。")] = "hybrid",
    index_id: Annotated[str, typer.Option("--index", help="qwen | bge_small | bge_m3。")] = "bge_m3",
    json_output: Annotated[bool, typer.Option("--json", help="输出 JSON。")] = False,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="将 JSON 以 UTF-8 写入文件。")] = None,
) -> None:
    from controlsci.api.medical_rag import search

    payload = call_quiet(search, q=query, k=k, mode=mode, vision=(mode == "vision"), index_id=index_id, quiet=json_output)
    if json_output or output:
        print_json(payload, output=output)
        return
    console.print(f"检索查询：{payload.get('search_query')}")
    for item in payload.get("results", []):
        console.print(f"[cyan]#{item['rank']}[/cyan] {item.get('source_file')} · {item.get('text_preview')}")


@app.command("ask")
def ask_cmd(
    question: Annotated[str, typer.Argument(help="用户自然语言问题。")],
    k: Annotated[int, typer.Option("--k", help="检索数量。")] = 3,
    model: Annotated[str, typer.Option("--model", help="本地合成模型。")] = "qwen3.5:9b",
    mode: Annotated[str, typer.Option("--mode", help="dense | bm25 | hybrid | vision。")] = "hybrid",
    index_id: Annotated[str, typer.Option("--index", help="qwen | bge_small | bge_m3。")] = "bge_m3",
    json_output: Annotated[bool, typer.Option("--json", help="输出 JSON。")] = False,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="将 JSON 以 UTF-8 写入文件。")] = None,
) -> None:
    from controlsci.api.medical_rag import AskRequest, ask

    payload = call_quiet(
        ask,
        AskRequest(question=question, k=k, synthesis_model=model, mode=mode, index_id=index_id),
        quiet=json_output,
    )
    if json_output or output:
        print_json(payload, output=output)
        return
    console.print(f"[bold]问题：[/bold]{question}")
    console.print(f"[bold]回答：[/bold]{payload.get('answer')}")
    console.print(f"[dim]引用覆盖率：{payload.get('citation_coverage')} · confidence={payload.get('confidence')}[/dim]")


@app.command("eval")
def eval_cmd(
    case_set: Annotated[str, typer.Option("--case-set", help="en | zh_ask。")] = "zh_ask",
    index_id: Annotated[str, typer.Option("--index", help="默认 index_bge_m3。")] = "index_bge_m3",
    json_output: Annotated[bool, typer.Option("--json", help="输出 JSON。")] = False,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="将 JSON 以 UTF-8 写入文件。")] = None,
) -> None:
    path = _eval_path(case_set)
    if not path.exists():
        raise typer.BadParameter(f"评测结果不存在：{path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    summary = data.get("summary", {})
    selected = summary.get(index_id) or next(iter(summary.values()), {})
    trace_path = Path(data["trace_jsonl"]) if data.get("trace_jsonl") else None
    trace_stats = _trace_stats(trace_path) if trace_path else {}
    payload = {
        "status": "ok" if selected else "degraded",
        "case_set": data.get("case_set"),
        "generated_at": data.get("generated_at"),
        "k": data.get("k"),
        "index": index_id if index_id in summary else next(iter(summary.keys()), ""),
        "summary": selected,
        "trace_jsonl": str(trace_path) if trace_path else "",
        "trace_stats": trace_stats,
        "source": str(path),
    }
    if json_output or output:
        print_json(payload, output=output)
        return
    console.print(f"Track3 RAG Eval: {payload['case_set']} · {payload['index']}")
    console.print(f"Hit@K: {selected.get('hit_at_k')}/{selected.get('cases')} · label_hit_rate={selected.get('label_hit_rate')}")
    if trace_stats:
        console.print(f"Trace: {trace_stats.get('records')} records · claims {trace_stats.get('supported_claims')}/{trace_stats.get('claim_count')} · citation={trace_stats.get('mean_citation_coverage')}")


@supplemental_app.command("status")
def supplemental_status(
    json_output: Annotated[bool, typer.Option("--json", help="输出 JSON。")] = False,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="将 JSON 以 UTF-8 写入文件。")] = None,
) -> None:
    payload = _supplemental_status_payload()
    if json_output or output:
        print_json(payload, output=output)
        return
    console.print(f"Track3 supplemental: {payload['status']}")
    console.print(f"Tasks: {payload['available_task_count']}/{payload['task_count']} available")
    console.print(f"Evidence files: {payload['available_evidence_file_count']}/{payload['evidence_file_count']} available")
    console.print(f"Figures: {payload['available_figure_count']}/{payload['figure_count']} available")
    for task in payload.get("tasks", []):
        console.print(f"- {task['name']}: {task['status']} · {task['path']}")


@supplemental_app.command("summary")
def supplemental_summary_cmd(
    json_output: Annotated[bool, typer.Option("--json", help="输出 JSON。")] = False,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="将 JSON 以 UTF-8 写入文件。")] = None,
) -> None:
    payload = _supplemental_summary_payload()
    if json_output or output:
        print_json(payload, output=output)
        return
    console.print(f"Track3 supplemental summary: {payload['status']}")
    console.print(f"Generated: {payload.get('generated_at')}")
    console.print(f"Tasks: {payload.get('available_task_count')}/{payload.get('task_count')} available")
    console.print(f"Evidence files: {payload.get('available_evidence_file_count')}/{payload.get('evidence_file_count')} available")
    console.print(f"Figures: {payload.get('available_figure_count')}/{payload.get('figure_count')} available")
    smoke = payload.get("deployment_smoke_matrix", {})
    console.print(f"Smoke: {smoke.get('executed_smoke_checks')} executed · {smoke.get('not_run_checks')} not run")


@supplemental_app.command("run")
def supplemental_run(
    task: Annotated[str, typer.Option("--task", help="补充实验任务名，例如 deployment-smoke。")] = "deployment-smoke",
    json_output: Annotated[bool, typer.Option("--json", help="输出 JSON。")] = False,
    output: Annotated[Path | None, typer.Option("--output", "-o", help="将 JSON 以 UTF-8 写入文件。")] = None,
) -> None:
    payload = _run_supplemental_task(task)
    if json_output or output:
        print_json(payload, output=output)
        return
    console.print(f"Supplemental task: {payload['task']} · {payload['status']}")
    console.print(f"Exit code: {payload['exit_code']}")
    for path in payload.get("outputs", []):
        console.print(f"- {path['path']}: {path['status']}")


app.add_typer(supplemental_app, name="supplemental")


def _eval_path(case_set: str) -> Path:
    if case_set == "zh_ask":
        return PROJECT_ROOT / "benchmark" / "eval" / "results" / "medical_rag_eval_zh_ask.json"
    if case_set == "en":
        return PROJECT_ROOT / "benchmark" / "eval" / "results" / "medical_rag_eval.json"
    raise typer.BadParameter("case-set 只支持 en 或 zh_ask")


def _project_path(path_text: str) -> Path:
    return PROJECT_ROOT / Path(path_text)


def _relative_path(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT) if path.is_relative_to(PROJECT_ROOT) else path).replace("\\", "/")


def _read_json_if_exists(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _supplemental_summary_path() -> Path:
    return _project_path(SUPPLEMENTAL_EXPERIMENTS["deployment-smoke"]["summary_output"])


def _supplemental_status_payload() -> dict:
    summary_path = _supplemental_summary_path()
    summary = _read_json_if_exists(summary_path)
    tasks = summary.get("tasks", []) if summary else []
    evidence_files = _path_statuses(SUPPLEMENTAL_EVIDENCE_FILES)
    figures = _path_statuses(SUPPLEMENTAL_FIGURES)
    registered = [
        {
            "name": name,
            "module": config["module"],
            "output": config["output"],
            "summary_output": config["summary_output"],
        }
        for name, config in SUPPLEMENTAL_EXPERIMENTS.items()
    ]
    return {
        "status": summary.get("status", "missing") if summary else "missing",
        "summary_path": _relative_path(summary_path),
        "summary_exists": summary_path.exists(),
        "generated_at": summary.get("generated_at"),
        "task_count": int(summary.get("task_count") or len(tasks)),
        "available_task_count": int(summary.get("available_task_count") or sum(1 for item in tasks if item.get("exists"))),
        "registered_task_count": len(registered),
        "registered_tasks": registered,
        "evidence_file_count": len(evidence_files),
        "available_evidence_file_count": sum(1 for item in evidence_files if item["exists"]),
        "figure_count": len(figures),
        "available_figure_count": sum(1 for item in figures if item["exists"]),
        "tasks": [
            {
                "name": item.get("name"),
                "status": item.get("status", "missing"),
                "exists": bool(item.get("exists")),
                "path": item.get("path"),
                "evaluation_mode": item.get("evaluation_mode"),
            }
            for item in tasks
        ],
        "evidence_files": evidence_files,
        "figures": figures,
        "deployment_smoke_matrix": summary.get("deployment_smoke_matrix", {}),
    }


def _supplemental_summary_payload() -> dict:
    summary_path = _supplemental_summary_path()
    summary = _read_json_if_exists(summary_path)
    evidence_files = _path_statuses(SUPPLEMENTAL_EVIDENCE_FILES)
    figures = _path_statuses(SUPPLEMENTAL_FIGURES)
    if not summary:
        return {
            "status": "missing",
            "summary_path": _relative_path(summary_path),
            "summary_exists": False,
            "task_count": 0,
            "available_task_count": 0,
            "tasks": [],
            "evidence_files": evidence_files,
            "figures": figures,
        }
    return {
        "status": summary.get("status"),
        "summary_path": _relative_path(summary_path),
        "summary_exists": True,
        "generated_at": summary.get("generated_at"),
        "task": summary.get("task"),
        "evaluation_mode": summary.get("evaluation_mode"),
        "task_count": summary.get("task_count"),
        "available_task_count": summary.get("available_task_count"),
        "deployment_smoke_matrix": summary.get("deployment_smoke_matrix", {}),
        "tasks": summary.get("tasks", []),
        "evidence_file_count": len(evidence_files),
        "available_evidence_file_count": sum(1 for item in evidence_files if item["exists"]),
        "figure_count": len(figures),
        "available_figure_count": sum(1 for item in figures if item["exists"]),
        "evidence_files": evidence_files,
        "figures": figures,
        "boundary_notes": summary.get("boundary_notes", []),
        "source": _relative_path(summary_path),
    }


def _path_statuses(paths: list[str]) -> list[dict]:
    items = []
    for path_text in paths:
        path = _project_path(path_text)
        items.append(
            {
                "path": path_text,
                "exists": path.exists(),
                "status": "available" if path.exists() else "missing",
                "size_kb": path.stat().st_size // 1024 if path.exists() and path.is_file() else 0,
            }
        )
    return items


def _run_supplemental_task(task: str) -> dict:
    if task not in SUPPLEMENTAL_EXPERIMENTS:
        raise typer.BadParameter(f"未知 supplemental task：{task}")
    config = SUPPLEMENTAL_EXPERIMENTS[task]
    output_path = _project_path(config["output"])
    summary_path = _project_path(config["summary_output"])
    command = [
        current_python(),
        "-m",
        config["module"],
        "--output",
        str(output_path),
        "--summary-output",
        str(summary_path),
    ]
    completed = subprocess.run(
        command,
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    outputs = [
        {"path": _relative_path(output_path), "exists": output_path.exists(), "status": "available" if output_path.exists() else "missing"},
        {"path": _relative_path(summary_path), "exists": summary_path.exists(), "status": "available" if summary_path.exists() else "missing"},
    ]
    payload = {
        "status": "ok" if completed.returncode == 0 and all(item["exists"] for item in outputs) else "failed",
        "task": task,
        "module": config["module"],
        "command": command,
        "exit_code": completed.returncode,
        "outputs": outputs,
        "stdout_preview": (completed.stdout or "").strip()[:1000],
        "stderr_preview": (completed.stderr or "").strip()[:1000],
    }
    if completed.returncode != 0:
        raise typer.Exit(completed.returncode)
    return payload


def _trace_stats(path: Path) -> dict:
    if not path.exists():
        return {"available": False, "records": 0}
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not rows:
        return {"available": True, "records": 0}
    synthesis_items = [row.get("synthesis", row) for row in rows]
    claim_count = sum(int(item.get("claim_count") or 0) for item in synthesis_items)
    supported_claims = sum(int(item.get("supported_claims") or 0) for item in synthesis_items)
    citation_values = [float(item.get("citation_coverage") or 0) for item in synthesis_items]
    return {
        "available": True,
        "records": len(rows),
        "claim_count": claim_count,
        "supported_claims": supported_claims,
        "mean_citation_coverage": sum(citation_values) / len(citation_values),
    }
