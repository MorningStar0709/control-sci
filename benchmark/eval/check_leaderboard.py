"""Verify leaderboard data integrity.

Usage:
    conda run --no-capture-output -n myenv python benchmark/eval/check_leaderboard.py
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEADERBOARD_PATH = ROOT / "benchmark" / "eval" / "reports" / "leaderboard.json"

if not LEADERBOARD_PATH.exists():
    print(f"Leaderboard not found: {LEADERBOARD_PATH}")
    print("Run summarize_multi.py first to generate it.")
    sys.exit(1)

data = json.loads(LEADERBOARD_PATH.read_text(encoding="utf-8"))
models = data.get("models", [])

print(f"Models in leaderboard: {len(models)}")
print()
print(f"| Rank | Model | Overall | A | B | C | D | Questions | Complete |")
print(f"|------|-------|---------|---|---|---|---|-----------|----------|")

errors = []
for i, m in enumerate(sorted(models, key=lambda x: -x.get("overall_score", 0)), 1):
    name = m.get("model", "?")
    overall = m.get("overall_score", -1)
    ds = m.get("dimension_scores", {})
    a = ds.get("A", "-")
    b = ds.get("B", "-")
    c = ds.get("C", "-")
    d = ds.get("D", "-")
    n = m.get("total_questions", 0)
    ok = "yes" if m.get("complete") else "no"
    
    print(f"| {i} | {name} | {overall:.4f} | {a} | {b} | {c} | {d} | {n} | {ok} |")
    
    if not isinstance(overall, (int, float)) or overall < 0 or overall > 1:
        errors.append(f"  ❌ {name}: overall_score={overall} out of range [0,1]")

print()
if errors:
    for e in errors:
        print(e)
    print(f"\n❌ {len(errors)} error(s) found")
    sys.exit(1)
else:
    print(f"✅ All {len(models)} models valid, scores in [0,1] range")
