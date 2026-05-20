"""Track3 Medical RAG commands."""

from __future__ import annotations

from typing import Annotated
import json
from pathlib import Path

import typer

from controlsci.cli.common import call_quiet, console, print_json, run_command, current_python, PROJECT_ROOT


app = typer.Typer(help="医学 RAG 索引、检索、问答与评测。")


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


def _eval_path(case_set: str) -> Path:
    if case_set == "zh_ask":
        return PROJECT_ROOT / "benchmark" / "eval" / "results" / "medical_rag_eval_zh_ask.json"
    if case_set == "en":
        return PROJECT_ROOT / "benchmark" / "eval" / "results" / "medical_rag_eval.json"
    raise typer.BadParameter("case-set 只支持 en 或 zh_ask")


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
