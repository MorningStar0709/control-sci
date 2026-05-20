#!/usr/bin/env bash
# reproduce.sh — ControlSci Cross-Modal Alignment Benchmark 一键复现 (WSL2)
# Phase 1-4 Full Pipeline v1.0
# Usage: bash reproduce.sh [options]
set -euo pipefail

# ── Defaults ──
MODE="mock"           # mock | api
PROVIDER="deepseek"
LIMIT=500
CONDA_ENV="${CONDA_ENV:-myenv}"
SKIP_METADATA=0
SKIP_BENCHMARK=0
SKIP_ARBITRATE=0
SKIP_VALIDATE=0
SKIP_SPLIT=0
SKIP_EXPORT=0
DRY_RUN=0
QUIET=0
RESUME=0
SUPPLEMENT=0
PUSH_TO_HUB=""
HF_TOKEN="${HF_TOKEN:-}"

ROOT="$(cd "$(dirname "$0")" && pwd)"
BENCHMARK_JSON="$ROOT/benchmark/dataset/benchmark.json"
REVIEW_JSON="$ROOT/benchmark/dataset/manual_review.json"
CORE_JSON="$ROOT/benchmark/dataset/core.json"
FULL_JSON="$ROOT/benchmark/dataset/full.json"
MERGED_JSON="$ROOT/benchmark/dataset/merged.json"
METADATA_JSON="$ROOT/corpus/metadata.json"

START_TIME=$(date +%s)

# Provider → env var mapping
declare -A PROVIDER_ENV_MAP=(
    ["deepseek"]="DEEPSEEK_API_KEY or OPENAI_API_KEY"
    ["mimo"]="MIMO_API_KEY"
    ["minimax"]="MINIMAX_API_KEY"
)

# ── Color helpers ──
c_cyan='\033[0;36m'
c_green='\033[0;32m'
c_yellow='\033[0;33m'
c_red='\033[0;31m'
c_gray='\033[0;90m'
c_reset='\033[0m'

step_header() {
    local label=""
    if [ "$STEP_NUM" -gt 0 ]; then
        label="[$STEP_NUM/$TOTAL_PHASES]"
    fi
    echo -e "\n${c_cyan}$(printf '=%.0s' {1..60})${c_reset}"
    echo -e "${c_cyan}  $label $*${c_reset}"
    echo -e "${c_cyan}$(printf '=%.0s' {1..60})${c_reset}"
}

ok()    { echo -e "  ${c_green}[OK]${c_reset} $*"; }
warn()  { echo -e "  ${c_yellow}[WARN]${c_reset} $*"; }
err()   { echo -e "  ${c_red}[ERROR]${c_reset} $*"; }
info()  { if [ "$QUIET" -eq 0 ]; then echo -e "  ${c_gray}[INFO]${c_reset} $*"; fi; return 0; }

# ── Args ──
while [ $# -gt 0 ]; do
    case "$1" in
        --mock)            MODE="mock";;
        --api)             MODE="api";;
        --provider)        PROVIDER="$2"; shift;;
        --limit)           LIMIT="$2"; shift;;
        --env)             CONDA_ENV="$2"; shift;;
        --skip-metadata)   SKIP_METADATA=1;;
        --skip-benchmark)  SKIP_BENCHMARK=1;;
        --skip-arbitrate)  SKIP_ARBITRATE=1;;
        --skip-validate)   SKIP_VALIDATE=1;;
        --skip-split)      SKIP_SPLIT=1;;
        --skip-export)     SKIP_EXPORT=1;;
        --dry-run)         DRY_RUN=1;;
        --quiet)           QUIET=1;;
        --resume)          RESUME=1;;
        --supplement)      SUPPLEMENT="$2"; shift;;
        --push-to-hub)     PUSH_TO_HUB="$2"; shift;;
        --hf-token)        HF_TOKEN="$2"; shift;;
        --help|-h)
            echo "Usage: bash reproduce.sh [options]"
            echo ""
            echo "Options:"
            echo "  --mock               Mock mode (deterministic, no API) [default]"
            echo "  --api                API mode (requires Provider key env var)"
            echo "  --provider NAME      Provider: deepseek | minimax | mimo  [default: deepseek]"
            echo "  --limit N            Question limit  [default: 500]"
            echo "  --env NAME           Conda env name  [default: myenv]"
            echo "  --skip-metadata      Skip Phase 2 metadata rebuild"
            echo "  --skip-benchmark     Skip Phase 3 question generation"
            echo "  --skip-arbitrate     Skip Phase 4a arbitration"
            echo "  --skip-split         Skip Phase 4b split"
            echo "  --skip-validate      Skip Phase 4c validation"
            echo "  --skip-export        Skip HF export"
            echo "  --dry-run            Print plan, don't execute"
            echo "  --quiet              Minimal output"
            echo "  --resume             Resume from checkpoint (Phase 3)"
            echo "  --supplement N       Append N questions to existing benchmark.json"
            echo "  --push-to-hub REPO   HF dataset repo name"
            echo "  --hf-token TOKEN     HF write token (or set HF_TOKEN)"
            echo "  -h, --help           Show this help"
            echo ""
            echo "Examples:"
            echo "  bash reproduce.sh                           # Mock 500 questions"
            echo "  bash reproduce.sh --dry-run                 # Preview plan"
            echo "  bash reproduce.sh --api --limit 200         # API mode, 200 questions"
            echo "  bash reproduce.sh --skip-benchmark          # Arbitrate + split only"
            exit 0
            ;;
        *) echo "Unknown option: $1"; exit 1;;
    esac
    shift
done

# ── Dynamic step count ──
TOTAL_PHASES=7
TOTAL_STEPS=1  # Phase 1 always
[ "$SKIP_METADATA"  -eq 0 ] && TOTAL_STEPS=$((TOTAL_STEPS + 1))
[ "$SKIP_BENCHMARK" -eq 0 ] && TOTAL_STEPS=$((TOTAL_STEPS + 1))
[ "$SKIP_ARBITRATE" -eq 0 ] && TOTAL_STEPS=$((TOTAL_STEPS + 1))
[ "$SKIP_SPLIT"     -eq 0 ] && TOTAL_STEPS=$((TOTAL_STEPS + 1))
[ "$SKIP_VALIDATE"  -eq 0 ] && TOTAL_STEPS=$((TOTAL_STEPS + 1))
[ "$SKIP_EXPORT"    -eq 0 ] && TOTAL_STEPS=$((TOTAL_STEPS + 1))

# ── Execute a Python step ──
run_step() {
    local desc="$1"
    shift
    local args=("$@")
    local cmd_str="${args[*]}"

    if [ "$DRY_RUN" -eq 1 ]; then
        echo -e "  ${c_gray}[DRY-RUN]${c_reset} $cmd_str"
        return 0
    fi
    [ "$QUIET" -eq 0 ] && [ -n "$desc" ] && echo "  > $desc"
    info "  \$ $cmd_str"

    if conda run --no-capture-output -n "$CONDA_ENV" python "${args[@]}"; then
        ok "Done"
        return 0
    else
        local rc=$?
        err "Command failed (exit=$rc): $cmd_str"
        return $rc
    fi
}

run_step_allow_fail() {
    run_step "$@" || true
}

elapsed_str() {
    local secs=$(($(date +%s) - START_TIME))
    printf "%02d:%02d:%02d" $((secs/3600)) $(((secs%3600)/60)) $((secs%60))
}

# ══════════════════════════════════════════════════
# Banner
# ══════════════════════════════════════════════════
if [ "$QUIET" -eq 0 ]; then
    echo ""
    echo -e "  ${c_cyan}+----------------------------------------------------+${c_reset}"
    echo -e "  ${c_cyan}|   ControlSci Cross-Modal Alignment Benchmark         |${c_reset}"
    echo -e "  ${c_cyan}|   Phase 1-4 Full Pipeline v1.0  (WSL2)              |${c_reset}"
    echo -e "  ${c_cyan}|   Start: $(date '+%Y-%m-%d %H:%M:%S')                   |${c_reset}"
    echo -e "  ${c_cyan}+----------------------------------------------------+${c_reset}"
fi

echo ""
echo -e "  Mode: $([ "$MODE" = "mock" ] && echo 'Mock (deterministic)' || echo "API ($PROVIDER)")"
echo "  Limit: $LIMIT questions"
echo "  Conda env: $CONDA_ENV"
echo "  Steps: $TOTAL_STEPS active"
[ "$RESUME" -eq 1 ]     && echo "  Resume: YES"
[ "$SUPPLEMENT" -gt 0 ] && echo "  Supplement: +$SUPPLEMENT"
[ "$DRY_RUN" -eq 1 ]    && warn "DRY-RUN mode: printing plan only, not executing."

# ══════════════════════════════════════════════════
# Phase 1: Pre-flight
# ══════════════════════════════════════════════════
STEP_NUM=1
step_header "Phase 1: Pre-flight Checks"

ALL_OK=true

check_file() {
    if [ -f "$1" ]; then
        ok "$2 ready: $1"
    else
        warn "$2 missing: $1"
        ALL_OK=false
    fi
}

check_file "$ROOT/pipeline/build_metadata_light.py"     "Metadata builder"
check_file "$ROOT/benchmark/pipeline/build_benchmark.py"  "Benchmark builder"
check_file "$ROOT/benchmark/pipeline/arbiter.py"          "Arbiter module"
check_file "$ROOT/benchmark/pipeline/split_benchmark.py"  "Splitter"
check_file "$ROOT/benchmark/pipeline/validate_benchmark.py" "Validator"

if conda run -n "$CONDA_ENV" python --version 2>/dev/null; then
    ok "conda ($CONDA_ENV): $(conda run -n "$CONDA_ENV" python --version 2>&1)"
else
    if [ "$DRY_RUN" -eq 1 ]; then
        warn "conda env '$CONDA_ENV' not available in this shell; dry-run continues."
    else
        err "conda env '$CONDA_ENV' not available."
        ALL_OK=false
    fi
fi

if [ "$ALL_OK" = false ] && [ "$DRY_RUN" -eq 0 ]; then
    err "Pre-flight checks failed. Fix and retry."
    exit 1
fi

# ══════════════════════════════════════════════════
# Phase 2: Metadata
# ══════════════════════════════════════════════════
STEP_NUM=$((STEP_NUM + 1))
step_header "Phase 2: Metadata Rebuild -> corpus/metadata.json"

if [ "$SKIP_METADATA" -eq 1 ]; then
    info "Skipped (--skip-metadata)"
    [ ! -f "$METADATA_JSON" ] && warn "metadata.json not found."
else
    run_step "build_metadata_light.py" "pipeline/build_metadata_light.py" || {
        if [ "$DRY_RUN" -eq 0 ]; then
            err "metadata.json not generated."
            exit 1
        fi
    }
    [ -f "$METADATA_JSON" ] && ok "metadata.json generated ($(du -h "$METADATA_JSON" | cut -f1))"
fi

# ══════════════════════════════════════════════════
# Phase 3: Question generation
# ══════════════════════════════════════════════════
STEP_NUM=$((STEP_NUM + 1))
step_header "Phase 3: Question Generation -> benchmark/dataset/benchmark.json"

if [ "$SKIP_BENCHMARK" -eq 1 ]; then
    info "Skipped (--skip-benchmark)"
    [ ! -f "$BENCHMARK_JSON" ] && warn "benchmark.json not found."
else
    BUILD_ARGS=("benchmark/pipeline/build_benchmark.py")

    if [ "$MODE" = "mock" ]; then
        BUILD_ARGS+=("--mock")
    else
        ENV_VAR_NAME="${PROVIDER_ENV_MAP[$PROVIDER]:-UNKNOWN}"
        warn "API mode: will call $PROVIDER to generate $LIMIT questions."
        warn "Ensure env var is set: \$$ENV_VAR_NAME"
        BUILD_ARGS+=("--provider" "$PROVIDER")
    fi

    BUILD_ARGS+=("--limit" "$LIMIT" "--output" "$BENCHMARK_JSON" "--manual-review-output" "$REVIEW_JSON")
    [ "$RESUME" -eq 1 ]     && BUILD_ARGS+=("--resume")
    [ "$SUPPLEMENT" -gt 0 ] && BUILD_ARGS+=("--supplement" "$SUPPLEMENT")

    DESC="build_benchmark.py --$MODE --limit $LIMIT"
    run_step "$DESC" "${BUILD_ARGS[@]}" || {
        if [ "$DRY_RUN" -eq 0 ]; then
            err "benchmark.json not generated."
            [ "$MODE" = "api" ] && [ -f "${BENCHMARK_JSON%.json}.checkpoint.json" ] && \
                info "Checkpoint found -- use --resume to continue."
            exit 1
        fi
    }

    if [ -f "$BENCHMARK_JSON" ]; then
        QCOUNT=$(conda run -n "$CONDA_ENV" python -c "import json;print(len(json.load(open('$BENCHMARK_JSON'))['questions']))" 2>/dev/null || echo "?")
        ok "benchmark.json: $QCOUNT questions"
    fi
fi

# ══════════════════════════════════════════════════
# Phase 4a: Arbitration
# ══════════════════════════════════════════════════
STEP_NUM=$((STEP_NUM + 1))
step_header "Phase 4a: Arbitration -- resolve needs_review"

if [ "$SKIP_ARBITRATE" -eq 1 ]; then
    info "Skipped (--skip-arbitrate)"
else
    if [ ! -f "$BENCHMARK_JSON" ] && [ "$DRY_RUN" -eq 0 ]; then err "benchmark.json missing."; exit 1; fi
    if [ ! -f "$REVIEW_JSON" ]    && [ "$DRY_RUN" -eq 0 ]; then err "manual_review.json missing."; exit 1; fi

    run_step "build_benchmark.py --arbitrate" \
        "benchmark/pipeline/build_benchmark.py" "--arbitrate" \
        "--output" "$BENCHMARK_JSON" "--manual-review-output" "$REVIEW_JSON" || true

    if [ -f "$BENCHMARK_JSON" ]; then
        KEPT=$(conda run -n "$CONDA_ENV" python -c "import json;qs=json.load(open('$BENCHMARK_JSON'))['questions'];print(sum(1 for q in qs if q.get('consistency_status') in ('auto_passed','reviewed_kept')))" 2>/dev/null || echo "?")
        DISCARDED=$(conda run -n "$CONDA_ENV" python -c "import json;qs=json.load(open('$BENCHMARK_JSON'))['questions'];print(sum(1 for q in qs if q.get('consistency_status')=='reviewed_discarded'))" 2>/dev/null || echo "?")
        ok "Post-arbitration: $KEPT kept, $DISCARDED discarded"
    fi
fi

# ══════════════════════════════════════════════════
# Phase 4b: Split
# ══════════════════════════════════════════════════
STEP_NUM=$((STEP_NUM + 1))
step_header "Phase 4b: Split -> core.json (500) + full.json"

if [ "$SKIP_SPLIT" -eq 1 ]; then
    info "Skipped (--skip-split)"
else
    SPLIT_INPUT="$BENCHMARK_JSON"
    if [ -f "$MERGED_JSON" ]; then
        SPLIT_INPUT="$MERGED_JSON"
        info "Using merged.json as split input"
    fi

    [ ! -f "$SPLIT_INPUT" ] && [ "$DRY_RUN" -eq 0 ] && { err "Split input not found: $SPLIT_INPUT"; exit 1; }

    run_step "split_benchmark.py -> core + full" \
        "benchmark/pipeline/split_benchmark.py" \
        "--input" "$SPLIT_INPUT" "--core" "$CORE_JSON" "--full" "$FULL_JSON" || true

    if [ -f "$CORE_JSON" ]; then
        CORE_DIMS=$(conda run -n "$CONDA_ENV" python -c "import json;qs=json.load(open('$CORE_JSON'))['questions'];from collections import Counter;c=Counter(q.get('dimension','?') for q in qs);print(' '.join(f'{k}={v}' for k,v in sorted(c.items())))" 2>/dev/null || echo "?")
        CORE_N=$(conda run -n "$CONDA_ENV" python -c "import json;print(len(json.load(open('$CORE_JSON'))['questions']))" 2>/dev/null || echo "?")
        ok "core.json: $CORE_N questions ($CORE_DIMS)"
    fi
    if [ -f "$FULL_JSON" ]; then
        FULL_N=$(conda run -n "$CONDA_ENV" python -c "import json;print(len(json.load(open('$FULL_JSON'))['questions']))" 2>/dev/null || echo "?")
        ok "full.json: $FULL_N questions"
    fi
fi

# ══════════════════════════════════════════════════
# Phase 4c: Validation
# ══════════════════════════════════════════════════
STEP_NUM=$((STEP_NUM + 1))
step_header "Phase 4c: Quality Validation"

if [ "$SKIP_VALIDATE" -eq 1 ]; then
    info "Skipped (--skip-validate)"
else
    VALIDATE_TARGET="$CORE_JSON"
    [ ! -f "$VALIDATE_TARGET" ] && VALIDATE_TARGET="$BENCHMARK_JSON"
    run_step "validate_benchmark.py" \
        "benchmark/pipeline/validate_benchmark.py" "--input" "$VALIDATE_TARGET" || true
fi

# ══════════════════════════════════════════════════
# Optional: HF Export
# ══════════════════════════════════════════════════
STEP_NUM=$((STEP_NUM + 1))
step_header "Optional: HF JSONL Export"

if [ "$SKIP_EXPORT" -eq 1 ]; then
    info "Skipped (--skip-export)"
else
    EXPORT_INPUT="$CORE_JSON"
    [ ! -f "$EXPORT_INPUT" ] && EXPORT_INPUT="$BENCHMARK_JSON"

    EXPORT_ARGS=("benchmark/pipeline/export_dataset.py" "--input" "$EXPORT_INPUT")

    if [ -n "$PUSH_TO_HUB" ]; then
        TOKEN_VAL="${HF_TOKEN:-}"
        if [ -n "$TOKEN_VAL" ]; then
            export HF_TOKEN="$TOKEN_VAL"
            EXPORT_ARGS+=("--push-to-hub" "$PUSH_TO_HUB")
        else
            warn "PushToHub requires --hf-token or HF_TOKEN env var. Skipping push."
        fi
    fi

    run_step_allow_fail "export_dataset.py -> HF JSONL" "${EXPORT_ARGS[@]}"
fi

# ══════════════════════════════════════════════════
# Completion Summary
# ══════════════════════════════════════════════════
ELAPSED=$(elapsed_str)
echo ""
echo -e "${c_cyan}$(printf '=%.0s' {1..60})${c_reset}"
echo -e "${c_green}  Pipeline Complete${c_reset}"
echo -e "${c_cyan}$(printf '=%.0s' {1..60})${c_reset}"
echo "  Elapsed:    $ELAPSED"
echo -e "  Mode:       $([ "$MODE" = "mock" ] && echo 'Mock' || echo "API ($PROVIDER)")"
echo "  Limit:      $LIMIT"

echo ""
echo "  Outputs:"
for item in "$METADATA_JSON metadata.json" "$BENCHMARK_JSON benchmark.json" \
            "$REVIEW_JSON manual_review.json" "$CORE_JSON core.json (500 core set)" \
            "$FULL_JSON full.json (full set)"; do
    path="${item%% *}"
    label="${item#* }"
    if [ -f "$path" ]; then
        sz=$(du -h "$path" | cut -f1)
        echo -e "    ${c_green}[OK]${c_reset} $label ($sz)"
    else
        echo -e "    ${c_red}[MISS]${c_reset} $label"
    fi
done

echo ""
echo "  Next steps:"
if [ -f "$CORE_JSON" ]; then
    echo "    > Evaluate:  conda run -n $CONDA_ENV python benchmark/eval/evaluate.py --mode model --input $CORE_JSON ..."
    echo "    > Eval Pipe:  conda run -n $CONDA_ENV python benchmark/eval/run_eval_pipeline.py --benchmark $CORE_JSON --limit 10"
    echo "    > Fine-tune:  conda run -n $CONDA_ENV python finetune/scripts/prepare_instruction_data.py"
elif [ -f "$BENCHMARK_JSON" ]; then
    echo "    > Arb+Split:  bash reproduce.sh --skip-metadata --skip-benchmark"
fi

[ "$QUIET" -eq 0 ] && {
    echo ""
    echo -e "  ${c_gray}File locations:${c_reset}"
    echo -e "  ${c_gray}  benchmark/dataset/core.json      - Core set (500 Qs)${c_reset}"
    echo -e "  ${c_gray}  benchmark/dataset/full.json      - Full set (889 Qs)${c_reset}"
    echo -e "  ${c_gray}  benchmark/dataset/benchmark.json - Raw generated${c_reset}"
    echo -e "  ${c_gray}  corpus/metadata.json             - Corpus metadata${c_reset}"
}

exit 0
