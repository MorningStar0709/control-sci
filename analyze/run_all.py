"""ControlSci 数据集综合分析 — 单次运行产出全部分析结果

使用方法:
    conda run --no-capture-output -n myenv python analyze/run_all.py

产出:
    analyze/outputs/
        01_dim_difficulty.json   四维 × 难度分布矩阵
        02_category.json         子领域覆盖率
        03_reasoning_steps.json  推理步数深度
        04_provider.json         Provider 贡献分析
        05_consistency.json      一致性状态分布
        06_orphan_impact.json    孤儿回收影响模拟
        07_provider_diversity.json 多 Provider diversity 分析
        summary_all.json         汇总数据
        charts/                  PNG + HTML 图表
"""

import json
import sys
import time
import argparse
from concurrent.futures import as_completed, ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass

from analyze import OUTPUT_DIR, CORE_PATH, FULL_PATH
from analyze.analyzers import (
    a1_dim_difficulty,
    a2_control_category,
    a3_reasoning_steps,
    a4_provider,
    b1_consistency,
    c1_orphan_impact,
    c2_provider_diversity,
)
from analyze.charts.render_all import render_all


def load_questions(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("questions", [])


def save_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


ANALYZERS = [
    ("01_dim_difficulty", a1_dim_difficulty.analyze, False),
    ("02_category", a2_control_category.analyze, False),
    ("03_reasoning_steps", a3_reasoning_steps.analyze, False),
    ("04_provider", a4_provider.analyze, False),
    ("05_consistency", b1_consistency.analyze, False),
    ("06_quality_tiers", c1_orphan_impact.analyze, False),
    ("07_provider_diversity", c2_provider_diversity.analyze, False),
]


def parse_args():
    parser = argparse.ArgumentParser(description="Run all ControlSci dataset analyses.")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR), help="Output directory for analysis JSON/charts.")
    parser.add_argument("--dry-run", action="store_true", help="Load inputs and print the planned outputs without writing files.")
    return parser.parse_args()


def main():
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    t0 = time.time()

    print("Loading core.json...", end="", flush=True)
    questions = load_questions(CORE_PATH)
    full_questions = load_questions(FULL_PATH) if FULL_PATH.exists() else []
    print(f" {len(questions)} questions ({len(full_questions)} in full.json)")

    if args.dry_run:
        print("Dry-run analysis plan:")
        for name, _, _ in ANALYZERS:
            print(f"  {name}.json")
        print(f"  summary_all.json")
        print(f"  charts/ under {output_dir}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    results = {}

    with ThreadPoolExecutor(max_workers=4) as pool:
        future_map = {}
        for name, func, needs_full in ANALYZERS:
            if needs_full:
                future = pool.submit(func, questions, full_questions)
            else:
                future = pool.submit(func, questions)
            future_map[future] = name

        for future in as_completed(future_map):
            name = future_map[future]
            try:
                result = future.result()
                results[name] = result
                save_json(output_dir / f"{name}.json", result)
                print(f"  ✅ {name}: {result.get('summary', '')[:80]}")
            except Exception as e:
                print(f"  ❌ {name}: {e}")

    save_json(output_dir / "summary_all.json", {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_questions": len(questions),
        "analysis_count": len(results),
        "summaries": {k: v.get("summary", "") for k, v in results.items()},
    })

    print(f"\nAnalysis complete in {time.time()-t0:.1f}s. Generating charts...")
    render_all(output_dir)
    print(f"\nAll outputs in: {output_dir}")


if __name__ == "__main__":
    main()
