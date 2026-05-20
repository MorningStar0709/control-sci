<#
.SYNOPSIS
    ControlSci Eval Pipeline One-Click Reproduction
    core.json -> leaderboard.json complete call chain

.DESCRIPTION
    Starting from core.json (500-question benchmark), reproduce the full eval pipeline:
      Step 0  -- Prerequisites (conda myenv / API Keys / Ollama)
      Step 1  -- Dataset Validation  (benchmark/eval/validate_dataset.py)
      Step 2  -- Model Evaluation    (benchmark/eval/evaluate.py --mode model)
      Step 3  -- Leaderboard Gen     (summarize_multi.py + report_viz.py)

    Default: DryRun mode (preview only). Use -Execute to actually run.

.PARAMETER Execute
    Actually execute the pipeline (default is DryRun preview).

.PARAMETER TargetModel
    Target model name for evaluation. Default: deepseek-v4-flash.

.PARAMETER JudgeModel
    Judge model name. Default: deepseek-v4-flash.

.PARAMETER Limit
    Max questions to evaluate. Default 10 (quick validation). 0 = all 500.

.PARAMETER Input
    Path to core.json. Default: benchmark/dataset/core.json.

.PARAMETER ResultsDir
    Output directory for results. Default: benchmark/eval/results.

.PARAMETER SkipValidate
    Skip Step 1 dataset validation.

.PARAMETER SkipEvaluate
    Skip Step 2 model evaluation.

.PARAMETER SkipLeaderboard
    Skip Step 3 leaderboard generation.

.PARAMETER Help
    Show full help.

.EXAMPLE
    .\run_evaluation.ps1

.EXAMPLE
    .\run_evaluation.ps1 -Execute -Limit 10

.EXAMPLE
    .\run_evaluation.ps1 -Execute -SkipEvaluate -SkipLeaderboard

.EXAMPLE
    .\run_evaluation.ps1 -Execute -SkipValidate -SkipEvaluate

.NOTES
    Author:  ControlSci Project
    Version: 1.0
    Date:    2026-05-07
    Phase:   6 / Task 1.8b
#>

param(
    [switch]$Execute,
    [string]$TargetModel = "deepseek-v4-flash",
    [string]$JudgeModel = "deepseek-v4-flash",
    [int]$Limit = 10,
    [string]$Input = "",
    [string]$ResultsDir = "",
    [switch]$SkipValidate,
    [switch]$SkipEvaluate,
    [switch]$SkipLeaderboard,
    [switch]$BalancedMini,
    [switch]$Help
)

if ($Help) {
    Get-Help -Detailed $PSCommandPath
    exit 0
}

$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$ROOT = $PSScriptRoot
$PYTHON = "conda"
$ENV_FLAGS = @("run", "--no-capture-output", "-n", "myenv", "python")

if (-not $Input)     { $Input     = Join-Path $ROOT "benchmark\dataset\core.json" }
if (-not $ResultsDir) { $ResultsDir = Join-Path $ROOT "benchmark\eval\results" }

$VALIDATE_SCRIPT = Join-Path $ROOT "benchmark\eval\validate_dataset.py"
$EVALUATE_SCRIPT = Join-Path $ROOT "benchmark\eval\evaluate.py"
$SUMMARIZE_SCRIPT = Join-Path $ROOT "benchmark\eval\summarize_multi.py"
$REPORT_VIZ_SCRIPT = Join-Path $ROOT "benchmark\eval\report_viz.py"

$START_TIME = Get-Date
$FailCount = 0
$SkipCount = 0

# ============================================================
# Helpers
# ============================================================
function Write-Step {
    param([string]$Msg, [int]$Number = 0, [int]$Total = 0)
    $label = if ($Number -gt 0 -and $Total -gt 0) { "[$Number/$Total]" } else { "" }
    Write-Host ("`n" + ("=" * 60)) -ForegroundColor Cyan
    Write-Host "  $label $Msg" -ForegroundColor Cyan
    Write-Host ("=" * 60) -ForegroundColor Cyan
}

function Write-Ok   { param([string]$Msg) Write-Host "  [OK] $Msg" -ForegroundColor Green }
function Write-Warn { param([string]$Msg) Write-Host "  [WARN] $Msg" -ForegroundColor Yellow }
function Write-Err  { param([string]$Msg) Write-Host "  [ERROR] $Msg" -ForegroundColor Red }
function Write-Info { param([string]$Msg) Write-Host "  [INFO] $Msg" -ForegroundColor Gray }

function Get-Elapsed {
    $elapsed = (Get-Date) - $START_TIME
    return "{0:D2}:{1:D2}:{2:D2}" -f $elapsed.Hours, $elapsed.Minutes, $elapsed.Seconds
}

function Invoke-Step {
    param(
        [string[]]$ArgList,
        [string]$Desc = "",
        [boolean]$AllowFail = $false
    )
    $cmdStr = $ArgList -join " "
    if (-not $Execute) {
        Write-Host "  [DRY-RUN] conda run --no-capture-output -n myenv python $cmdStr" -ForegroundColor DarkGray
        return $true
    }
    if ($Desc) { Write-Host "  > $Desc" -ForegroundColor White }
    Write-Info "  $ conda run --no-capture-output -n myenv python $cmdStr"

    $proc = Start-Process -FilePath $PYTHON -ArgumentList ($ENV_FLAGS + $ArgList) `
        -NoNewWindow -Wait -PassThru
    if ($proc.ExitCode -ne 0) {
        Write-Err "Command failed (exit=$($proc.ExitCode))"
        $script:FailCount++
        if (-not $AllowFail) { throw "Pipeline aborted at: $Desc" }
        return $false
    }
    Write-Ok "Done"
    return $true
}

# ============================================================
# Dynamic step count
# ============================================================
$TOTAL_STEPS = 0
if (-not $SkipValidate)     { $TOTAL_STEPS++ }
if (-not $SkipEvaluate)     { $TOTAL_STEPS++ }
if (-not $SkipLeaderboard)  { $TOTAL_STEPS++ }

# ============================================================
# Banner
# ============================================================
Write-Host ""
Write-Host "  +----------------------------------------------------+" -ForegroundColor Cyan
Write-Host "  |   ControlSci Eval Pipeline  One-Click Repro v1.0   |" -ForegroundColor Cyan
Write-Host "  |   core.json -> leaderboard.json                    |" -ForegroundColor Cyan
Write-Host "  |   Start: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')                   |" -ForegroundColor Cyan
Write-Host "  +----------------------------------------------------+" -ForegroundColor Cyan

Write-Host ""
if ($Execute) {
    Write-Host "  Mode: EXECUTE" -ForegroundColor Green
} else {
    Write-Host "  Mode: DRY-RUN (preview only, use -Execute to run)" -ForegroundColor Yellow
}
Write-Host "  Target Model: $TargetModel"
Write-Host "  Judge Model:  $JudgeModel"
$limitLabel = if ($Limit -eq 0) { "ALL (500 questions)" } else { "$Limit questions" }
Write-Host "  Limit:        $limitLabel"
if ($BalancedMini) { Write-Host "  Selection:    balanced-mini (A/B/C/D round-robin)" }
Write-Host "  Input:        $Input"
Write-Host "  Results Dir:  $ResultsDir"
Write-Host "  Steps:        $TOTAL_STEPS (validate + evaluate + leaderboard)"

# ============================================================
# Step 0: Prerequisite Checks
# ============================================================
Write-Step -Number 0 -Total $TOTAL_STEPS -Msg "Step 0: Prerequisite Checks"

$allOk = $true

# Conda env
$condaInfo = conda run -n myenv python --version 2>&1
$condaOk = ($LASTEXITCODE -eq 0) -and $?
if (-not $condaOk) {
    Write-Err "conda myenv not available. Create it: conda create -n myenv python=3.12 -y"
    $allOk = $false
} else {
    Write-Ok "conda (myenv): $condaInfo"
}

# core.json
if (Test-Path $Input) {
    $coreSize = [math]::Round((Get-Item $Input).Length / 1KB, 1)
    Write-Ok "core.json: $coreSize KB"
} else {
    Write-Err "core.json not found: $Input"
    $allOk = $false
}

# API Keys
$dsKey = if ($env:DEEPSEEK_API_KEY) { $env:DEEPSEEK_API_KEY } else { $env:OPENAI_API_KEY }
if ($dsKey) {
    Write-Ok "DEEPSEEK_API_KEY/OPENAI_API_KEY: set (DeepSeek Judge)"
} else {
    Write-Warn "DEEPSEEK_API_KEY/OPENAI_API_KEY not set (required for Judge)"
}

$mimoKey = $env:MIMO_API_KEY
if ($mimoKey) {
    Write-Ok "MIMO_API_KEY: set"
} else {
    Write-Info "MIMO_API_KEY not set (optional, for MiMo eval)"
}

$minimaxKey = $env:MINIMAX_API_KEY
if ($minimaxKey) {
    Write-Ok "MINIMAX_API_KEY: set"
} else {
    Write-Info "MINIMAX_API_KEY not set (optional, for MiniMax eval)"
}

# Ollama (optional, with 5s timeout guard)
$ollamaAvailable = $false
$ollamaJob = Start-Job -ScriptBlock { & ollama list 2>&1; $LASTEXITCODE }
$ollamaJob | Wait-Job -Timeout 5 | Out-Null
if ($ollamaJob.State -eq "Completed") {
    $raw = $ollamaJob | Receive-Job
    $exitCode = @($raw)[-1]
    if ($exitCode -eq 0) {
        Write-Ok "Ollama: running"; $ollamaAvailable = $true
    } else {
        Write-Info "Ollama daemon not running (local Qwen eval unavailable)"
    }
} elseif ($ollamaJob.State -eq "Running") {
    $ollamaJob | Stop-Job | Out-Null
    Write-Info "Ollama daemon not responding within 5s (local Qwen eval unavailable)"
} else {
    Write-Info "Ollama CLI not available (local Qwen eval unavailable)"
}
$ollamaJob | Remove-Job -Force -ErrorAction SilentlyContinue

# ResultsDir
if (-not (Test-Path $ResultsDir)) {
    Write-Info "Creating ResultsDir: $ResultsDir"
    New-Item -ItemType Directory -Path $ResultsDir -Force | Out-Null
    Write-Ok "ResultsDir ready"
} else {
    Write-Ok "ResultsDir exists: $ResultsDir"
}

# Script existence
$scriptChecks = @(
    @{Path=$VALIDATE_SCRIPT; Label="validate_dataset.py"},
    @{Path=$EVALUATE_SCRIPT; Label="evaluate.py"},
    @{Path=$SUMMARIZE_SCRIPT; Label="summarize_multi.py"},
    @{Path=$REPORT_VIZ_SCRIPT; Label="report_viz.py"}
)
foreach ($sc in $scriptChecks) {
    if (Test-Path $sc.Path) {
        Write-Ok "$($sc.Label) ready"
    } else {
        Write-Err "$($sc.Label) missing: $($sc.Path)"
        $allOk = $false
    }
}

if (-not $allOk) {
    Write-Err "Prerequisite checks failed. Fix and retry."
    if (-not $Execute) {
        Write-Info "DryRun mode: errors above are advisory. Use -Execute to enforce."
    } else {
        exit 1
    }
}

# ============================================================
# Step 1: Validate Dataset
# ============================================================
$step = 0
if (-not $SkipValidate) {
    $step++
    Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Step 1: Validate Dataset (core.json integrity)"

    $null = Invoke-Step -ArgList @($VALIDATE_SCRIPT, "--input", $Input) -Desc "validate_dataset.py"

    $t1 = Get-Elapsed
    Write-Info "Step 1 elapsed: $t1"
} else {
    $SkipCount++
    Write-Info "Step 1 skipped (SkipValidate)"
}

# ============================================================
# Step 2: Model Evaluation
# ============================================================
if (-not $SkipEvaluate) {
    $step++
    Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Step 2: Model Evaluation ($TargetModel, limit=$Limit)"

    $evalOutput = Join-Path $ResultsDir "eval_${TargetModel}.json"
    $evalArgs = @(
        $EVALUATE_SCRIPT,
        "--mode", "model",
        "--input", $Input,
        "--output", $evalOutput,
        "--target-model", $TargetModel,
        "--judge-model", $JudgeModel,
        "--limit", $Limit,
        "--resume"
    )
    if ($BalancedMini) {
        $evalArgs += "--balanced-mini"
    }

    $null = Invoke-Step -ArgList $evalArgs -Desc "evaluate.py --mode model --target-model $TargetModel --limit $Limit"
    Write-Info "Output: $evalOutput"

    $t2 = Get-Elapsed
    Write-Info "Step 2 elapsed: $t2"
} else {
    $SkipCount++
    Write-Info "Step 2 skipped (SkipEvaluate)"
}

# ============================================================
# Step 3: Leaderboard Generation
# ============================================================
if (-not $SkipLeaderboard) {
    $step++
    Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Step 3: Leaderboard (summarize + visualize)"

    $leaderJson = Join-Path $ResultsDir "leaderboard.json"
    $leaderHtml = Join-Path $ResultsDir "leaderboard.html"

    Write-Host ""
    Write-Host "  --- 3a: summarize_multi.py -> leaderboard.json ---" -ForegroundColor White
    $summaryArgs = @(
        $SUMMARIZE_SCRIPT,
        "--input", $ResultsDir,
        "--output", $leaderJson
    )
    $summaryOk = Invoke-Step -ArgList $summaryArgs -Desc "summarize_multi.py" -AllowFail $true
    Write-Info "Output: $leaderJson"

    Write-Host ""
    Write-Host "  --- 3b: report_viz.py -> leaderboard.html ---" -ForegroundColor White
    $vizArgs = @(
        $REPORT_VIZ_SCRIPT,
        "--input", $ResultsDir,
        "--output", $leaderHtml
    )
    $vizOk = Invoke-Step -ArgList $vizArgs -Desc "report_viz.py" -AllowFail $true
    Write-Info "Output: $leaderHtml"

    if ($Execute -and (-not $summaryOk -or -not $vizOk)) {
        Write-Warn "Leaderboard step completed with partial outputs. Check errors above."
    }

    $t3 = Get-Elapsed
    Write-Info "Step 3 elapsed: $t3"
} else {
    $SkipCount++
    Write-Info "Step 3 skipped (SkipLeaderboard)"
}

# ============================================================
# Completion Summary
# ============================================================
$totalTime = Get-Elapsed
Write-Host ""
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host "  Eval Pipeline Complete" -ForegroundColor Green
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host "  Elapsed:    $totalTime"
Write-Host "  Target:     $TargetModel"
Write-Host "  Limit:      $(if ($Limit -eq 0) { 'ALL (500)' } else { $Limit })"
Write-Host "  Failed:     $FailCount"
Write-Host "  Skipped:    $SkipCount"
Write-Host ""

if (-not $Execute) {
    Write-Host "  This was a DRY-RUN. To execute:" -ForegroundColor Yellow
    Write-Host "    .\run_evaluation.ps1 -Execute -Limit 10" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  Quick validate only:" -ForegroundColor Gray
    Write-Host "    conda run --no-capture-output -n myenv python benchmark/eval/validate_dataset.py" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Full eval (500 Qs):" -ForegroundColor Gray
    Write-Host "    .\run_evaluation.ps1 -Execute -Limit 0" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Leaderboard from existing results:" -ForegroundColor Gray
    Write-Host "    .\run_evaluation.ps1 -Execute -SkipValidate -SkipEvaluate" -ForegroundColor Gray
}

Write-Host ""
Write-Host "  Output files:" -ForegroundColor Gray
Write-Host "    $ResultsDir\eval_${TargetModel}.json  -- single-model report" -ForegroundColor Gray
Write-Host "    $ResultsDir\leaderboard.json           -- multi-model ranking" -ForegroundColor Gray
Write-Host "    $ResultsDir\leaderboard.html           -- visualization" -ForegroundColor Gray

if ($Execute -and $FailCount -gt 0) {
    exit 1
}
exit 0
