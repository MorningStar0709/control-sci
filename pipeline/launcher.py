"""Launch mineru_to_md.py as a completely detached process.
Usage: python pipeline/launcher.py --list-file data/textbook-batch-01.txt

Monitor: python pipeline/_health.py
         Get-Content data/logs/{stem}_stdout.log -Tail 5
"""
import argparse
import os
import subprocess
import sys
from pathlib import Path

# Dynamic project root: pipeline/launcher.py → pipeline/ → project root
WORK_DIR = Path(__file__).resolve().parents[1]

# Default script path: prefer env var, fallback to project-relative path
_DEFAULT_SCRIPT = Path(os.environ.get(
    "MINERU_SCRIPT",
    str(WORK_DIR / "tools" / "mineru_to_md.py"),
))

OUTPUT_DIR = str(WORK_DIR / "data" / "processed")
LOG_DIR = WORK_DIR / "data" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument("--list-file", required=True)
parser.add_argument("--output-dir", default=OUTPUT_DIR)
parser.add_argument("--script-path", default=None,
                    help="Override path to mineru_to_md.py (auto-detected if omitted)")
args = parser.parse_args()

# Resolve script path
if args.script_path:
    SCRIPT = str(Path(args.script_path).resolve())
else:
    script_candidate = _DEFAULT_SCRIPT
    if script_candidate.exists():
        SCRIPT = str(script_candidate.resolve())
    else:
        print(f"Error: default script not found at {script_candidate}", file=sys.stderr)
        print("Use --script-path to specify the correct path.", file=sys.stderr)
        sys.exit(1)

list_file = str(Path(args.list_file).resolve())
output_dir = args.output_dir
stem = Path(list_file).stem
log_file = str(LOG_DIR / f"{stem}_stdout.log")
result_file = str(LOG_DIR / f"{stem}_result.json")
failure_file = str(LOG_DIR / f"{stem}_failed.txt")

cmd = [
    sys.executable, SCRIPT,
    "--list-file", list_file,
    "--output-dir", output_dir,
    "--skip-existing",
    "--result-file", result_file,
    "--failure-list", failure_file,
]

with open(log_file, "w") as f:
    f.write(f"Launching: {' '.join(cmd)}\n")
    f.flush()
    popen_kwargs = {}
    if os.name == "nt":
        popen_kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS

    proc = subprocess.Popen(
        cmd,
        stdout=f,
        stderr=subprocess.STDOUT,
        cwd=str(WORK_DIR),
        **popen_kwargs,
    )
    f.write(f"PID={proc.pid}\n")

print(f"PID={proc.pid}")
print(f"Log: {log_file}")
print(f"Monitor: python -c \"import json,urllib.request;print(json.loads(urllib.request.urlopen('http://127.0.0.1:8000/health').read()))\"")
