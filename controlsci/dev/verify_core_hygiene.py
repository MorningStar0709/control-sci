"""Core hygiene checks for review-facing ControlSci code paths.

This is intentionally lightweight: it checks policy/entrypoint invariants
without running long API, GPU, or training jobs.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


from controlsci.core.paths import PROJECT_ROOT


ROOT = PROJECT_ROOT
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _run(args, **kwargs):
    return subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        **kwargs,
    )


def _ok(label):
    print(f"[OK] {label}")


def _fail(label, detail):
    print(f"[FAIL] {label}: {detail}")
    return False


def check_capabilities():
    proc = _run([sys.executable, "benchmark/agent/_validate_capabilities.py"], timeout=30)
    if proc.returncode != 0:
        return _fail("capability validator", proc.stdout + proc.stderr)
    _ok("capability validator")
    return True


def check_balanced_selection():
    from benchmark.eval.evaluate import select_questions

    data = json.loads((ROOT / "benchmark/dataset/core.json").read_text(encoding="utf-8"))
    selected = select_questions(data["questions"], limit=10, balanced_mini=True)
    dims = [q.get("dimension") for q in selected]
    expected = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
    if dims != expected:
        return _fail("balanced-mini selection", f"{dims} != {expected}")
    _ok("balanced-mini selection")
    return True


def check_report_empty_exit():
    with tempfile.TemporaryDirectory() as tmp:
        proc = _run([sys.executable, "benchmark/eval/report_viz.py", "--input", tmp, "--output", str(Path(tmp) / "x.html")], timeout=30)
    if proc.returncode == 0:
        return _fail("report_viz empty input exit", "expected non-zero exit")
    _ok("report_viz empty input exit")
    return True


def check_cloud_demo_isolation():
    code = (
        "import json, os; "
        "os.environ['CONTROLSCI_API_PROFILE']='cloud_demo'; "
        "import controlsci.api.medical_rag as api; "
        "print(json.dumps(api.health(), ensure_ascii=False))"
    )
    proc = _run(["conda", "run", "--no-capture-output", "-n", "myenv", "python", "-c", code], timeout=60)
    if proc.returncode != 0:
        return _fail("cloud_demo isolation", proc.stdout + proc.stderr)
    health = json.loads(proc.stdout.strip().splitlines()[-1])
    if health["profile"] != "cloud_demo":
        return _fail("cloud_demo health profile", health)
    if health["components"]["privacy_boundary"]["text_full_exposed"]:
        return _fail("cloud_demo text exposure", health["components"]["privacy_boundary"])
    if "sources_medical" in str(health) or str(ROOT) in str(health):
        return _fail("cloud_demo health path leak", health)
    _ok("cloud_demo isolation")
    return True


def check_legacy_wrapper():
    proc = _run([sys.executable, "benchmark/agent/agent.py", "--dry-run", "--intents", "reproduce_all"], timeout=60)
    if proc.returncode != 0:
        return _fail("legacy agent wrapper", proc.stdout + proc.stderr)
    if "compatibility wrapper" not in proc.stderr:
        return _fail("legacy agent wrapper", "missing deprecation forwarding message")
    _ok("legacy agent wrapper")
    return True


def main():
    checks = [
        check_capabilities,
        check_balanced_selection,
        check_report_empty_exit,
        check_cloud_demo_isolation,
        check_legacy_wrapper,
    ]
    results = [check() for check in checks]
    failed = len([r for r in results if not r])
    print(f"\nCore hygiene: {len(results) - failed}/{len(results)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
