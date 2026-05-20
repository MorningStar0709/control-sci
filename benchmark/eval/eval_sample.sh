#!/usr/bin/env bash
set -euo pipefail

echo "=========================================="
echo "  ControlSci Benchmark Evaluation Samples"
echo "=========================================="
echo ""

if command -v conda >/dev/null 2>&1; then
  CONDA_CMD=(conda)
elif command -v conda.exe >/dev/null 2>&1; then
  CONDA_CMD=(conda.exe)
else
  echo "WARN: conda not found in this shell; printing examples only."
  CONDA_CMD=()
fi

# ── Example 1: Reference mode (default) ─────────────────────
echo "1. Reference mode (benchmark data integrity check):"
echo "   (default, no --model argument needed)"
if [ "${#CONDA_CMD[@]}" -gt 0 ]; then
  "${CONDA_CMD[@]}" run --no-capture-output -n myenv python benchmark/eval/evaluate.py \
    --mode reference \
    --input benchmark/dataset/sample_questions.json \
    --output benchmark/dataset/sample_report.json
else
  echo "   skipped: conda unavailable"
fi
echo ""

# ── Example 2: Model mode with 3-question limit ─────────────
echo "2. Model mode (LLM-as-Judge, limited to 3 questions):"
echo "   Make sure OPENAI_API_KEY is set in your environment."
echo ""
echo "   conda run --no-capture-output -n myenv python benchmark/eval/evaluate.py \\"
echo "     --mode model \\"
echo "     --input benchmark/dataset/sample_questions.json \\"
echo "     --target-model deepseek-v4-flash \\"
echo "     --judge-model deepseek-v4-flash \\"
echo "     --limit 3 \\"
echo "     --output benchmark/dataset/model_eval_report.json"
echo ""

# ── Example 3: Model mode with Markdown output ─────────────
echo "3. Model mode with Markdown report:"
echo ""
echo "   conda run --no-capture-output -n myenv python benchmark/eval/evaluate.py \\"
echo "     --mode model \\"
echo "     --input benchmark/dataset/sample_questions.json \\"
echo "     --target-model deepseek-v4-flash \\"
echo "     --judge-model deepseek-v4-flash \\"
echo "     --limit 3 \\"
echo "     --format md \\"
echo "     --output benchmark/dataset/eval_report.md"
echo ""

# ── Example 4: Standalone judge.py usage ───────────────────
echo "4. Standalone LLM-as-Judge (Dimension A):"
echo ""
echo "   conda run --no-capture-output -n myenv python benchmark/eval/judge.py \\"
echo "     --dimension A \\"
echo "     --question \"What is a PID controller?\" \\"
echo "     --expected \"PID controller has three parameters: Kp, Ki, Kd\" \\"
echo "     --answer \"A PID controller consists of proportional, integral, and derivative terms: Kp, Ki, and Kd.\" \\"
echo "     --model deepseek-v4-flash"
echo ""

# ── Example 5: report.py standalone usage ──────────────────
echo "5. Generate Markdown report from existing JSON result:"
echo ""
echo "   conda run --no-capture-output -n myenv python benchmark/eval/report.py \\"
echo "     --input benchmark/dataset/sample_report.json \\"
echo "     --format md \\"
echo "     --output benchmark/dataset/sample_report.md"
echo ""
