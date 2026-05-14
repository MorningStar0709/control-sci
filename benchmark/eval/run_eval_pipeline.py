"""Orchestrate the full evaluation pipeline after Phase C generation completes.

NOTE: This pipeline evaluates only 3 models (DeepSeek, MiniMax, MiMo) for
quick verification. For the full 9-model evaluation, use evaluate.py directly.

Usage:
    python benchmark/eval/run_eval_pipeline.py --benchmark benchmark/dataset/benchmark.json

Steps: arbitrate (1/4) → evaluate 3 models (2/4) → summary (3/4) → export (4/4)
"""
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable

# Model definitions for evaluation
# WARNING: This pipeline evaluates only 3 models (subset).
# The full ControlSci Benchmark evaluates 9 models total.
# Use benchmark/eval/evaluate.py directly for multi-model runs.
TARGET_MODELS = [
    {"name": "DeepSeek",   "model": "deepseek-v4-flash",      "base_url": "https://api.deepseek.com",            "api_key_env": "OPENAI_API_KEY"},
    {"name": "MiniMax",    "model": "MiniMax-M2.7-highspeed", "base_url": "https://api.minimaxi.com/anthropic",  "api_key_env": "MINIMAX_API_KEY"},
    {"name": "MiMo",       "model": "mimo-v2.5-pro",          "base_url": "https://api.xiaomimimo.com/v1",       "api_key_env": "MIMO_API_KEY"},
]

JUDGE_CONFIG = {
    "model": "deepseek-v4-flash",
    "base_url": "https://api.deepseek.com",
    "api_key_env": "OPENAI_API_KEY",
}


def step(msg):
    print(f"\n{'='*60}")
    print(f"  {msg}")
    print(f"{'='*60}")


def run(cmd, cwd=None, env_extra=None):
    print(f"  $ {cmd}", flush=True)
    full_env = os.environ.copy()
    if env_extra:
        full_env.update(env_extra)
    result = subprocess.run(cmd, shell=True, cwd=cwd or str(ROOT), capture_output=True, text=True, env=full_env)
    for line in result.stdout.strip().split("\n"):
        if line.strip():
            print(f"  {line}", flush=True)
    if result.returncode != 0:
        for line in result.stderr.strip().split("\n"):
            if line.strip():
                print(f"  ! {line}", flush=True)
        print(f"  ❌ Failed (exit={result.returncode})", flush=True)
    else:
        print(f"  ✅ OK", flush=True)
    return result.returncode


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Evaluation pipeline: arbitrate → evaluate 3 models → summary → export.")
    parser.add_argument("--benchmark", default=str(ROOT / "benchmark" / "dataset" / "benchmark.json"), help="Benchmark JSON path.")
    parser.add_argument("--review", default=str(ROOT / "benchmark" / "dataset" / "manual_review.json"), help="Manual review JSON path.")
    parser.add_argument("--output-dir", default=str(ROOT / "benchmark" / "eval_output"), help="Output directory for reports.")
    parser.add_argument("--skip-arbitrate", action="store_true", help="Skip arbitration step.")
    parser.add_argument("--skip-eval", action="store_true", help="Skip model evaluation step.")
    parser.add_argument("--skip-export", action="store_true", help="Skip HF export step.")
    parser.add_argument("--limit", type=int, default=0, help="Limit questions per evaluation (for testing).")
    parser.add_argument("--push-to-hub", default=None, help="HF dataset repo name for export.")
    parser.add_argument("--hf-token", default=None, help="HF token for export.")
    parser.add_argument("--supplement-target", type=int, default=500, help="Target question count after arbitration (default: 500).")
    args = parser.parse_args()

    benchmark_path = Path(args.benchmark).resolve()
    review_path = Path(args.review).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    start_time = time.time()

    # ── Step 0: Validate inputs ──
    if not benchmark_path.exists():
        raise SystemExit(f"Benchmark not found: {benchmark_path}")

    # ── Step 1: Arbitration ──
    if not args.skip_arbitrate:
        step("Step 1/4: Arbitration")
        rc = run(f'{PYTHON} benchmark/pipeline/build_benchmark.py --arbitrate --output "{benchmark_path}" --manual-review-output "{review_path}"')
        if rc != 0:
            print("Arbitration failed. Continuing with un-arbitrated benchmark.", flush=True)

        post_count = len(load_json(str(benchmark_path)).get("questions", []))
        print(f"  Post-arbitration question count: {post_count}", flush=True)
    else:
        print("⏩ Skipping arbitration.", flush=True)

    # ── Step 2: Evaluate each target model ──
    if not args.skip_eval:
        limit_opt = f" --limit {args.limit}" if args.limit > 0 else ""
        for model_def in TARGET_MODELS:
            step(f"Step 2/4: Evaluate {model_def['name']}")
            output_path = output_dir / f"report_{model_def['name'].lower()}.json"
            target_api_key = os.environ.get(model_def["api_key_env"], "")
            if not target_api_key:
                print(f"  ⚠️ No API key for {model_def['name']} ({model_def['api_key_env']}), skipping...", flush=True)
                continue

            judge_api_key = os.environ.get(JUDGE_CONFIG["api_key_env"], "")
            cmd = (
                f'{PYTHON} benchmark/eval/evaluate.py --mode model'
                f' --input "{benchmark_path}"'
                f' --output "{output_path}"'
                f' --target-model "{model_def["model"]}"'
                f' --target-base-url "{model_def["base_url"]}"'
                f' --judge-model "{JUDGE_CONFIG["model"]}"'
                f' --judge-base-url "{JUDGE_CONFIG["base_url"]}"'
                f'{limit_opt}'
                f' --format json'
            )
            env_extra = {}
            env_extra[model_def["api_key_env"]] = target_api_key
            if JUDGE_CONFIG["api_key_env"] not in env_extra:
                env_extra[JUDGE_CONFIG["api_key_env"]] = judge_api_key
            rc = run(cmd, env_extra=env_extra)
            if rc == 0:
                print(f"  Report saved: {output_path}", flush=True)
            else:
                print(f"  ❌ {model_def['name']} evaluation failed, continuing...", flush=True)
    else:
        print("⏩ Skipping model evaluation.", flush=True)

    # ── Step 3: Generate comparison summary ──
    if not args.skip_eval:
        step("Step 3/4: Generate comparison summary")
        summary = {
            "pipeline_start": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)),
            "benchmark_source": str(benchmark_path),
            "models_evaluated": [],
        }
        for model_def in TARGET_MODELS:
            json_path = output_dir / f"report_{model_def['name'].lower()}.json"
            if json_path.exists():
                report = load_json(str(json_path))
                summary["models_evaluated"].append({
                    "name": model_def["name"],
                    "overall_score": report.get("overall_score", 0),
                    "total_questions": report.get("total_questions", 0),
                    "dimension_scores": report.get("dimension_scores", {}),
                })
        summary_path = output_dir / "summary.json"
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        print(f"  Summary: {summary_path}", flush=True)
        for m in summary["models_evaluated"]:
            print(f"    {m['name']:>8s}: overall={m['overall_score']:.2f}, n={m['total_questions']}", flush=True)

    # ── Step 4: Export to HuggingFace ──
    if args.push_to_hub:
        step("Step 4/4: Export to HuggingFace Hub")
        hf_token = args.hf_token or os.environ.get("HF_TOKEN", "")
        hf_flag = f' --push-to-hub "{args.push_to_hub}"' if args.push_to_hub else ""
        hf_token_flag = f' --hf-token "{hf_token}"' if hf_token else ""
        rc = run(
            f'{PYTHON} benchmark/pipeline/export_dataset.py'
            f' --input "{benchmark_path}"'
            f' --output "{output_dir / "hf_export"}"'
            f'{hf_flag}{hf_token_flag}'
        )
    else:
        print("⏩ Skipping HF export. Pass --push-to-hub <repo> to enable.", flush=True)

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"  Pipeline complete in {elapsed:.0f}s ({elapsed/60:.1f}min)")
    print(f"  Output: {output_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
