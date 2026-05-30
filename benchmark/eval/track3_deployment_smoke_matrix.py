"""Build Track 3 deployment smoke matrix and supplemental summary."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


SUPPLEMENTAL_RESULTS = [
    ("task1_pipeline_ablation", ROOT / "benchmark" / "eval" / "results" / "track3_rag_pipeline_ablation.json"),
    ("task2_safety_refusal_stress", ROOT / "benchmark" / "eval" / "results" / "track3_safety_refusal_stress.json"),
    ("task3_medbench_ei_taxonomy", ROOT / "benchmark" / "eval" / "results" / "track3_medbench_ei_taxonomy.json"),
    ("task4_privacy_boundary_audit", ROOT / "benchmark" / "eval" / "results" / "track3_privacy_boundary_audit.json"),
    ("task5_semantic_chunk_quality", ROOT / "benchmark" / "eval" / "results" / "track3_semantic_chunk_quality.json"),
    ("task6_zh_ask_robustness", ROOT / "benchmark" / "eval" / "results" / "track3_zh_ask_robustness.json"),
    ("task7_evidence_card_completeness", ROOT / "benchmark" / "eval" / "results" / "track3_evidence_card_completeness.json"),
]

ENTRYPOINTS = [
    ("cli_track3", ROOT / "controlsci" / "cli" / "track3.py", "CLI track3 index/search/ask/eval commands"),
    ("cli_app", ROOT / "controlsci" / "cli" / "app.py", "Main CLI app entrypoint"),
    ("rest_api", ROOT / "controlsci" / "api" / "medical_rag.py", "Medical RAG FastAPI/functional API"),
    ("frontend_launcher", ROOT / "_final_submission_by_track" / "track3_medical_rag" / "run" / "run_frontend.ps1", "Frontend launcher in final bundle"),
    ("dockerfile", ROOT / "_final_submission_by_track" / "track3_medical_rag" / "run" / "Dockerfile", "Container build file"),
    ("docker_compose", ROOT / "_final_submission_by_track" / "track3_medical_rag" / "run" / "docker-compose.yml", "Docker compose runtime"),
    ("npm_launcher", ROOT / "_final_submission_by_track" / "track3_medical_rag" / "npm" / "controlmind" / "bin" / "controlmind.js", "NPM CLI launcher"),
    ("rag_flywheel", ROOT / "_final_submission_by_track" / "track3_medical_rag" / "run" / "run_task3_rag_flywheel.ps1", "RAG flywheel reproducibility script"),
    ("demo_verify", ROOT / "_final_submission_by_track" / "track3_medical_rag" / "run" / "verify_task3_demo.ps1", "Demo verification script"),
]


def path_text(path: Path) -> str:
    return str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path).replace("\\", "/")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def entrypoint_matrix() -> list[dict[str, Any]]:
    return [
        {
            "entrypoint": name,
            "path": path_text(path),
            "exists": path.exists(),
            "size_bytes": path.stat().st_size if path.exists() else 0,
            "purpose": purpose,
        }
        for name, path, purpose in ENTRYPOINTS
    ]


def run_smoke(name: str, command: list[str], timeout_seconds: int = 45) -> dict[str, Any]:
    started = datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout_seconds,
        )
        stdout = (completed.stdout or "").strip()
        stderr = (completed.stderr or "").strip()
        return {
            "name": name,
            "status": "passed" if completed.returncode == 0 else "failed",
            "command": command,
            "exit_code": completed.returncode,
            "started_at": started,
            "stdout_preview": stdout[:1000],
            "stderr_preview": stderr[:1000],
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "name": name,
            "status": "timeout",
            "command": command,
            "exit_code": None,
            "started_at": started,
            "stdout_preview": (exc.stdout or "")[:1000] if isinstance(exc.stdout, str) else "",
            "stderr_preview": (exc.stderr or "")[:1000] if isinstance(exc.stderr, str) else "",
        }


def smoke_checks() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    checks = [
        run_smoke("track3_eval_zh_ask_cli", [sys.executable, "-m", "controlsci.cli", "track3", "eval", "--case-set", "zh_ask", "--json"]),
        run_smoke("track3_supplemental_status_cli", [sys.executable, "-m", "controlsci.cli", "track3", "supplemental", "status", "--json"]),
    ]
    not_run = [
        {
            "name": "track3_index_check_cli",
            "status": "not_run_environment_dependency",
            "command": [sys.executable, "-m", "controlsci.cli", "track3", "index", "--check", "--json"],
            "reason": "Health check imports the full Medical RAG API stack and local index/model dependencies; Task 8 records static readiness instead of risking a long environment-bound check.",
        },
        {
            "name": "docker_compose_up",
            "status": "not_run_environment_dependency",
            "command": ["docker", "compose", "up"],
            "reason": "Docker daemon and service ports are environment dependent; compose files are included in static readiness matrix.",
        },
        {
            "name": "frontend_demo_launch",
            "status": "not_run_environment_dependency",
            "command": ["powershell", "-File", "run/run_frontend.ps1"],
            "reason": "Frontend smoke is a long-running service launch; static launcher presence is audited here.",
        },
    ]
    return checks, not_run


def summarize_task(name: str, path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"name": name, "path": path_text(path), "exists": False, "status": "missing"}
    data = load_json(path)
    summary = {"name": name, "path": path_text(path), "exists": True, "status": data.get("status"), "task": data.get("task"), "evaluation_mode": data.get("evaluation_mode")}
    for key in [
        "case_count",
        "base_case_count",
        "variant_count",
        "card_count",
        "covered_target_section_count",
        "rewrite_success_rate",
        "intent_consistency_rate",
        "privacy_local_only_rate",
        "claim_binding_coverage",
        "citation_whitelist_pass_rate",
    ]:
        if key in data:
            summary[key] = data[key]
    if "acceptance_check" in data:
        summary["acceptance_check"] = data["acceptance_check"]
    return summary


def supplemental_summary(smoke_matrix: dict[str, Any]) -> dict[str, Any]:
    tasks = [summarize_task(name, path) for name, path in SUPPLEMENTAL_RESULTS]
    return {
        "status": "available" if all(task.get("exists") for task in tasks) else "partial",
        "generated_at": datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z"),
        "task": "Track 3 Supplemental Experiments Summary",
        "evaluation_mode": "existing_task_json_aggregation",
        "task_count": len(tasks),
        "available_task_count": sum(1 for task in tasks if task.get("exists")),
        "tasks": tasks,
        "deployment_smoke_matrix": {
            "path": "benchmark/eval/results/track3_deployment_smoke_matrix.json",
            "entrypoints": len(smoke_matrix.get("entrypoint_matrix", [])),
            "entrypoints_available": sum(1 for item in smoke_matrix.get("entrypoint_matrix", []) if item.get("exists")),
            "executed_smoke_checks": len(smoke_matrix.get("executed_smoke_checks", [])),
            "not_run_checks": len(smoke_matrix.get("not_run_checks", [])),
        },
        "boundary_notes": [
            "Summary aggregates Task 1-7 JSON evidence and Task 8 deployment readiness; it does not add new model inference.",
            "Deployment checks distinguish executed smoke checks from environment-dependent checks that were not run.",
        ],
    }


def build_result() -> dict[str, Any]:
    executed, not_run = smoke_checks()
    matrix = entrypoint_matrix()
    return {
        "status": "available",
        "generated_at": datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z"),
        "task": "Track 3 Task 8 - Deployment Smoke Matrix and Final Packaging",
        "evaluation_mode": "static_readiness_plus_light_cli_smoke",
        "entrypoint_matrix": matrix,
        "executed_smoke_checks": executed,
        "not_run_checks": not_run,
        "summary": {
            "entrypoint_count": len(matrix),
            "entrypoint_available_count": sum(1 for item in matrix if item["exists"]),
            "executed_passed_count": sum(1 for item in executed if item["status"] == "passed"),
            "executed_failed_count": sum(1 for item in executed if item["status"] not in {"passed"}),
            "not_run_count": len(not_run),
        },
        "boundary_notes": [
            "This smoke matrix is a deployment readiness and light CLI verification record, not a full Docker/frontend runtime certification.",
            "Environment-dependent checks are explicitly listed as not_run_environment_dependency rather than reported as success.",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Track 3 deployment smoke matrix and supplemental summary.")
    parser.add_argument("--output", required=True, help="Output deployment smoke matrix JSON path")
    parser.add_argument("--summary-output", default="benchmark/eval/results/track3_supplemental_summary.json", help="Output supplemental summary JSON path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = supplemental_summary(result)
    summary_output = Path(args.summary_output)
    summary_output.parent.mkdir(parents=True, exist_ok=True)
    summary_output.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[Track3 Task8] wrote {output}")
    print(f"[Track3 Task8] wrote {summary_output}")


if __name__ == "__main__":
    main()
