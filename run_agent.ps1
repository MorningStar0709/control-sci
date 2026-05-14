<#
.SYNOPSIS
    ControlSci 终极一键复现 / Ultimate One-Click Reproduction
    语料 Markdown -> 500 题 Benchmark -> 9 模型评测 -> 排行榜 -> 深度分析 -> QLoRA 微调

.DESCRIPTION
    从 MinerU 解析产物出发，一站式复现 ControlSci 评测基准的全部产出：
      Phase A  -- 数据集构建 (metadata -> 题目生成 -> 仲裁 -> 拆分 -> 验证)
      Phase B  -- 模型评测   (DeepSeek + MiniMax + MiMo -> Leaderboard)
      Phase C  -- 深度分析   (7 维分析 + 图表渲染)
      Phase D  -- QLoRA 微调 (训练 + 评测, 可选后台)
      Phase E  -- 本地评测   (Ollama 35B Judge, 可选后台)

    默认 DryRun 模式 (仅预览)。使用 -Execute 实际执行。

.PARAMETER Execute
    实际执行流水线 (默认 DryRun 预览)。

.PARAMETER TargetModels
    目标模型列表，逗号分隔。默认: deepseek,minimax,mimo。

.PARAMETER Limit
    题目生成上限。默认 500。评测阶段默认 0 (=全部)。

.PARAMETER EvalLimit
    评测题目上限。默认 0 (=全部)。与 Limit 独立。

.PARAMETER Input
    core.json 路径。默认: benchmark/dataset/core.json。

.PARAMETER ResultsDir
    评测结果输出目录。默认: benchmark/eval/results。

.PARAMETER SkipDataset
    跳过 Phase A 数据集构建。

.PARAMETER SkipEval
    跳过 Phase B 模型评测。

.PARAMETER SkipAnalysis
    跳过 Phase C 深度分析。

.PARAMETER SkipQlora
    跳过 Phase D QLoRA 微调。

.PARAMETER SkipLocalJudge
    跳过 Phase E 本地 Judge 评测。

.PARAMETER SkipLeaderboard
    跳过 Phase B 中的 Leaderboard 生成。

.PARAMETER DryRun
    打印执行计划而不实际运行。

.PARAMETER Quiet
    静默模式，仅输出摘要。

.PARAMETER BackgroundLong
    QLoRA 训练和 35B Judge 以后台方式启动 (非阻塞)。

.PARAMETER Help
    显示完整帮助。

.EXAMPLE
    .\run_agent.ps1

.EXAMPLE
    .\run_agent.ps1 -Execute -Limit 10

.EXAMPLE
    .\run_agent.ps1 -Execute -SkipDataset -SkipQlora -SkipLocalJudge

.EXAMPLE
    .\run_agent.ps1 -Execute -SkipDataset -TargetModels deepseek

.EXAMPLE
    .\run_agent.ps1 -Execute -BackgroundLong -Limit 500

.NOTES
    Author:  ControlSci Project
    Version: 1.0
    Date:    2026-05-09
    Phase:   7 / Task T3-5
#>

param(
    [switch]$Execute,
    [string]$TargetModels = "deepseek,minimax,mimo",
    [int]$Limit = 500,
    [int]$EvalLimit = 0,
    [string]$Input = "",
    [string]$ResultsDir = "",
    [switch]$SkipDataset,
    [switch]$SkipEval,
    [switch]$SkipAnalysis,
    [switch]$SkipQlora,
    [switch]$SkipLocalJudge,
    [switch]$SkipLeaderboard,
    [switch]$DryRun,
    [switch]$Quiet,
    [switch]$BackgroundLong,
    [switch]$Help
)

if ($Help) {
    Get-Help -Detailed $PSCommandPath
    exit 0
}

$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONUTF8 = '1'
$ROOT = $PSScriptRoot
$PYTHON = "conda"
$ENV_FLAGS = @("run", "--no-capture-output", "-n", "myenv", "python")

if (-not $Input)     { $Input     = Join-Path $ROOT "benchmark\dataset\core.json" }
if (-not $ResultsDir) { $ResultsDir = Join-Path $ROOT "benchmark\eval\results" }

$BENCHMARK_JSON = Join-Path $ROOT "benchmark\dataset\benchmark.json"
$REVIEW_JSON    = Join-Path $ROOT "benchmark\dataset\manual_review.json"
$CORE_JSON      = Join-Path $ROOT "benchmark\dataset\core.json"
$FULL_JSON      = Join-Path $ROOT "benchmark\dataset\full.json"
$MERGED_JSON    = Join-Path $ROOT "benchmark\dataset\merged.json"
$METADATA_JSON  = Join-Path $ROOT "corpus\metadata.json"

$ANALYZE_OUT    = Join-Path $ROOT "analyze\outputs"
$QLORA_DIR      = Join-Path $ROOT "finetune\output\qlora"
$QLORA_FINAL    = Join-Path $ROOT "finetune\output\qlora-final"

$START_TIME = Get-Date

$MODEL_DEFS = @{
    "deepseek" = @{Name="DeepSeek";  Model="deepseek-v4-flash";      BaseUrl="https://api.deepseek.com";            KeyEnv="OPENAI_API_KEY"}
    "minimax"  = @{Name="MiniMax";   Model="MiniMax-M2.7-highspeed"; BaseUrl="https://api.minimaxi.com/anthropic";  KeyEnv="MINIMAX_API_KEY"}
    "mimo"     = @{Name="MiMo";      Model="mimo-v2.5";              BaseUrl="https://api.xiaomimimo.com/v1";       KeyEnv="MIMO_API_KEY"}
}

trap {
    Write-Err "Pipeline terminated: $_"
    exit 2
}

# ============================================================
# Helpers
# ============================================================
function Write-Step {
    param([string]$Msg, [int]$Number = 0, [int]$Total = 0)
    if (-not $Quiet) {
        $label = if ($Number -gt 0 -and $Total -gt 0) { "[$Number/$Total]" } else { "" }
        Write-Host ("`n" + ("=" * 60)) -ForegroundColor Cyan
        Write-Host "  $label $Msg" -ForegroundColor Cyan
        Write-Host ("=" * 60) -ForegroundColor Cyan
    }
}

function Write-Ok   { param([string]$Msg) Write-Host "  [OK] $Msg" -ForegroundColor Green }
function Write-Warn { param([string]$Msg) Write-Host "  [WARN] $Msg" -ForegroundColor Yellow }
function Write-Err  { param([string]$Msg) Write-Host "  [ERROR] $Msg" -ForegroundColor Red }
function Write-Info { param([string]$Msg) if (-not $Quiet) { Write-Host "  [INFO] $Msg" -ForegroundColor Gray } }

function Get-Elapsed {
    $elapsed = (Get-Date) - $START_TIME
    return "{0:D2}:{1:D2}:{2:D2}" -f $elapsed.Hours, $elapsed.Minutes, $elapsed.Seconds
}

function Test-File {
    param([string]$Path, [string]$Label)
    if (Test-Path $Path) {
        Write-Ok "$Label ready: $Path"
        return $true
    }
    Write-Warn "$Label missing: $Path"
    return $false
}

function Invoke-Step {
    param(
        [string[]]$ArgList,
        [string]$Desc = "",
        [switch]$AllowFail,
        [string[]]$MaskTokens = @("--target-api-key", "--judge-api-key", "--api-key", "--hf-token")
    )
    $displayArgs = @()
    $skipNext = $false
    foreach ($a in $ArgList) {
        if ($skipNext) {
            $displayArgs += "***"
            $skipNext = $false
        } elseif ($a -in $MaskTokens) {
            $displayArgs += $a
            $skipNext = $true
        } else {
            $displayArgs += $a
        }
    }
    $cmdStr = $ArgList -join " "
    $displayCmdStr = $displayArgs -join " "
    if (-not $Execute) {
        Write-Host "  [DRY-RUN] conda run --no-capture-output -n myenv python $displayCmdStr" -ForegroundColor DarkGray
        return $true
    }
    if (-not $Quiet -and $Desc) { Write-Host "  > $Desc" -ForegroundColor White }
    Write-Info "  $ conda run --no-capture-output -n myenv python $displayCmdStr"

    $proc = Start-Process -FilePath $PYTHON -ArgumentList ($ENV_FLAGS + $ArgList) `
        -NoNewWindow -Wait -PassThru -WorkingDirectory $ROOT
    if ($proc.ExitCode -ne 0) {
        Write-Err "Command failed (exit=$($proc.ExitCode)): $displayCmdStr"
        if (-not $AllowFail) { throw "Pipeline aborted at: $Desc" }
        return $false
    }
    Write-Ok "Done"
    return $true
}

function Invoke-Background {
    param(
        [string[]]$ArgList,
        [string]$LogFile,
        [string]$ErrFile,
        [string]$Desc = "",
        [string[]]$MaskTokens = @("--target-api-key", "--judge-api-key", "--api-key", "--hf-token")
    )
    $displayArgs = @()
    $skipNext = $false
    foreach ($a in $ArgList) {
        if ($skipNext) {
            $displayArgs += "***"
            $skipNext = $false
        } elseif ($a -in $MaskTokens) {
            $displayArgs += $a
            $skipNext = $true
        } else {
            $displayArgs += $a
        }
    }
    $displayCmdStr = $displayArgs -join " "
    $cmdStr = $ArgList -join " "
    if (-not $Execute) {
        Write-Host "  [DRY-RUN] BACKGROUND: conda run --no-capture-output -n myenv python $displayCmdStr" -ForegroundColor DarkGray
        Write-Host "  [DRY-RUN]   log: $LogFile" -ForegroundColor DarkGray
        return @{Pid=-1; Log=$LogFile}
    }
    if (-not $Quiet -and $Desc) { Write-Host "  > [BACKGROUND] $Desc" -ForegroundColor Magenta }
    Write-Info "  $ conda run --no-capture-output -n myenv python $displayCmdStr"

    $logDir = Split-Path $LogFile -Parent
    if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

    $psArgs = @(
        '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command',
        @"
Set-Location '$ROOT';
`$env:PYTHONIOENCODING='utf-8';
`$env:CONDA_NO_PLUGINS='true';
conda run --no-capture-output -n myenv python $($ArgList -join ' ')
"@
    )

    $p = Start-Process -FilePath 'powershell' `
        -ArgumentList $psArgs `
        -WindowStyle Hidden `
        -RedirectStandardOutput $LogFile `
        -RedirectStandardError $ErrFile `
        -PassThru

    Write-Ok "Background PID=$($p.Id), log=$LogFile"
    Write-Info "  监控: Get-Content -Tail 5 $LogFile"
    return @{Pid=$p.Id; Log=$LogFile; Err=$ErrFile}
}

# ============================================================
# Dynamic step count
# ============================================================
$script:STEP = 0
$TOTAL_STEPS = 0

# Phase A: always runs unless skipped (5 sub-steps)
if (-not $SkipDataset)     { $TOTAL_STEPS += 5 }
# Phase B: eval + leaderboard (2 sub-steps)
if (-not $SkipEval)        { $TOTAL_STEPS++ }
if (-not $SkipLeaderboard -and -not $SkipEval) { $TOTAL_STEPS++ }
# Phase C: analysis (1 step)
if (-not $SkipAnalysis)    { $TOTAL_STEPS++ }
# Phase D: QLoRA training + eval (2 steps)
if (-not $SkipQlora)       { $TOTAL_STEPS += 2 }
# Phase E: local judge (1 step)
if (-not $SkipLocalJudge)  { $TOTAL_STEPS++ }

function Next-Step {
    $script:STEP++
    return $script:STEP
}

# ============================================================
# Banner
# ============================================================
if (-not $Quiet) {
    Write-Host ""
    Write-Host "  +----------------------------------------------------+" -ForegroundColor Cyan
    Write-Host "  |   ControlSci Ultimate One-Click Reproduction v1.0  |" -ForegroundColor Cyan
    Write-Host "  |   语料 Markdown -> Benchmark -> Leaderboard         |" -ForegroundColor Cyan
    Write-Host "  |   Start: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')                   |" -ForegroundColor Cyan
    Write-Host "  +----------------------------------------------------+" -ForegroundColor Cyan
}

Write-Host ""
if ($Execute) {
    Write-Host "  Mode: EXECUTE" -ForegroundColor Green
} else {
    Write-Host "  Mode: DRY-RUN (preview only, use -Execute to run)" -ForegroundColor Yellow
}
Write-Host "  Limit (generation): $Limit questions"
Write-Host "  Eval Limit:         $(if ($EvalLimit -eq 0) { 'ALL' } else { $EvalLimit })"
Write-Host "  Target Models:      $TargetModels"
Write-Host "  Total Steps:        $TOTAL_STEPS"
Write-Host "  Background Long:    $(if ($BackgroundLong) { 'YES' } else { 'NO (synchronous)' })"
Write-Host ""
Write-Host "  Phase A: Dataset   $(if ($SkipDataset) { '[SKIP]' } else { '[RUN]' })" -ForegroundColor $(if ($SkipDataset) { 'DarkGray' } else { 'White' })
Write-Host "  Phase B: Eval      $(if ($SkipEval) { '[SKIP]' } else { '[RUN]' })" -ForegroundColor $(if ($SkipEval) { 'DarkGray' } else { 'White' })
Write-Host "  Phase C: Analysis  $(if ($SkipAnalysis) { '[SKIP]' } else { '[RUN]' })" -ForegroundColor $(if ($SkipAnalysis) { 'DarkGray' } else { 'White' })
Write-Host "  Phase D: QLoRA     $(if ($SkipQlora) { '[SKIP]' } else { '[RUN]' })" -ForegroundColor $(if ($SkipQlora) { 'DarkGray' } else { 'White' })
Write-Host "  Phase E: LocalJudge$(if ($SkipLocalJudge) { '[SKIP]' } else { '[RUN]' })" -ForegroundColor $(if ($SkipLocalJudge) { 'DarkGray' } else { 'White' })

# ============================================================
# Pre-flight: Environment Check (always runs, regardless of Skip* flags)
# ============================================================
if ($Execute) {
    Write-Step -Number 0 -Total $TOTAL_STEPS -Msg "Pre-flight: Environment Check"

    $condaInfo = conda run -n myenv python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Err "conda myenv not available. Create: conda create -n myenv python=3.12 -y"
        exit 1
    }
    Write-Ok "conda (myenv): $condaInfo"
    Write-Info "Pre-flight elapsed: $(Get-Elapsed)"
}

# ============================================================
# Phase A: Dataset Creation
# ============================================================
if (-not $SkipDataset) {

    # --- A0: Prerequisite Checks ---
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase A0: Prerequisite Checks"

    $allOk = $true

    # Key scripts
    $scriptChecks = @(
        @{Path="$ROOT\pipeline\build_metadata_light.py";     Label="build_metadata_light.py"},
        @{Path="$ROOT\benchmark\pipeline\build_benchmark.py"; Label="build_benchmark.py"},
        @{Path="$ROOT\benchmark\pipeline\arbiter.py";         Label="arbiter.py"},
        @{Path="$ROOT\benchmark\pipeline\split_benchmark.py"; Label="split_benchmark.py"},
        @{Path="$ROOT\benchmark\pipeline\validate_benchmark.py"; Label="validate_benchmark.py"}
    )
    foreach ($sc in $scriptChecks) {
        if (-not (Test-Path $sc.Path)) { Write-Err "$($sc.Label) missing: $($sc.Path)"; $allOk = $false }
        else { Write-Ok "$($sc.Label) ready" }
    }

    # MinerU corpus check
    $corpusDir = Join-Path $ROOT "corpus"
    $mdFiles = if (Test-Path $corpusDir) { @(Get-ChildItem -Path $corpusDir -Filter "*.md" -Recurse -ErrorAction SilentlyContinue) } else { @() }
    if ($mdFiles.Count -eq 0) {
        Write-Warn "No corpus Markdown files found under $corpusDir — Phase A2 will fail."
        Write-Warn "  Run MinerU parse first, or create corpus/ directory with .md files."
        if ($Execute) { $allOk = $false }
    } else {
        Write-Ok "Corpus Markdown files: $($mdFiles.Count) found"
    }

    if ((-not $allOk) -and $Execute) {
        Write-Err "Prerequisite checks failed. Fix and retry."
        exit 1
    }
    if ((-not $allOk) -and -not $Execute) {
        Write-Info "DryRun: errors above are advisory."
    }

    # --- A1: Metadata Rebuild ---
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase A1: Metadata Rebuild -> corpus/metadata.json"
    $null = Invoke-Step -ArgList @("pipeline\build_metadata_light.py") -Desc "build_metadata_light.py"
    if (Test-Path $METADATA_JSON) {
        $metaSize = [math]::Round((Get-Item $METADATA_JSON).Length / 1KB, 1)
        Write-Ok "metadata.json: $metaSize KB"
    }

    # --- A2: Question Generation ---
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase A2: Question Generation -> benchmark/dataset/benchmark.json"

    $buildArgList = @("benchmark\pipeline\build_benchmark.py", "--mock")
    $buildArgList += @("--limit", $Limit, "--output", $BENCHMARK_JSON, "--manual-review-output", $REVIEW_JSON)
    $null = Invoke-Step -ArgList $buildArgList -Desc "build_benchmark.py --mock --limit $Limit"

    if (Test-Path $BENCHMARK_JSON) {
        $qCount = (Get-Content $BENCHMARK_JSON -Encoding UTF8 | ConvertFrom-Json).questions.Count
        Write-Ok "benchmark.json: $qCount questions"
    }

    # --- A3: Arbitration ---
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase A3: Arbitration -- resolve needs_review"

    if ((-not (Test-Path $BENCHMARK_JSON)) -or (-not (Test-Path $REVIEW_JSON))) {
        if ($Execute) { Write-Err "benchmark.json or manual_review.json missing."; exit 1 }
        else { Write-Info "DryRun: skipping arbitration dependency check." }
    }

    $arbArgList = @("benchmark\pipeline\build_benchmark.py", "--arbitrate", "--output", $BENCHMARK_JSON, "--manual-review-output", $REVIEW_JSON)
    $null = Invoke-Step -ArgList $arbArgList -Desc "build_benchmark.py --arbitrate"

    if (Test-Path $BENCHMARK_JSON) {
        $arbStats = Get-Content $BENCHMARK_JSON -Encoding UTF8 | ConvertFrom-Json
        $kept = ($arbStats.questions | Where-Object { $_.consistency_status -in @("auto_passed","reviewed_kept") }).Count
        $discarded = ($arbStats.questions | Where-Object { $_.consistency_status -eq "reviewed_discarded" }).Count
        Write-Ok "Post-arbitration: $kept kept, $discarded discarded"
    }

    # --- A4: Split (core.json + full.json) ---
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase A4: Split -> core.json + full.json"

    $splitInput = $BENCHMARK_JSON
    if (Test-Path $MERGED_JSON) {
        $splitInput = $MERGED_JSON
        Write-Info "Using merged.json as split input"
    }

    $splitArgList = @("benchmark\pipeline\split_benchmark.py", "--input", $splitInput, "--core", $CORE_JSON, "--full", $FULL_JSON)
    $null = Invoke-Step -ArgList $splitArgList -Desc "split_benchmark.py -> core + full"

    if (Test-Path $CORE_JSON) {
        $coreData = Get-Content $CORE_JSON -Encoding UTF8 | ConvertFrom-Json
        $dimCounts = $coreData.questions | Group-Object dimension | ForEach-Object { "$($_.Name)=$($_.Count)" }
        Write-Ok "core.json: $($coreData.questions.Count) questions ($($dimCounts -join ', '))"
    }
    if (Test-Path $FULL_JSON) {
        $fullData = Get-Content $FULL_JSON -Encoding UTF8 | ConvertFrom-Json
        Write-Ok "full.json: $($fullData.questions.Count) questions"
    }

    # --- A5: Quality Validation ---
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase A5: Quality Validation"

    $validateTarget = if (Test-Path $CORE_JSON) { $CORE_JSON } else { $BENCHMARK_JSON }
    $null = Invoke-Step -ArgList @("benchmark\pipeline\validate_benchmark.py", "--input", $validateTarget) -Desc "validate_benchmark.py"

    Write-Info "Phase A elapsed: $(Get-Elapsed)"
} else {
    Write-Info "Phase A skipped (SkipDataset)"
}

# ============================================================
# Phase B: Model Evaluation
# ============================================================
if (-not $SkipEval) {

    # --- B0: API Key checks ---
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase B: Model Evaluation (core.json -> eval results)"

    $targetList = $TargetModels -split ',' | ForEach-Object { $_.Trim().ToLower() }
    $activeModels = @()
    foreach ($m in $targetList) {
        $def = $MODEL_DEFS[$m]
        if (-not $def) {
            Write-Warn "Unknown model: $m (skipping)"
            continue
        }
        $key = [Environment]::GetEnvironmentVariable($def.KeyEnv)
        if (-not $key) {
            Write-Warn "$($def.Name) ($($def.KeyEnv)) API key not set — skipping"
            continue
        }
        $masked = $key.Substring(0, [Math]::Min(8, $key.Length)) + "***"
        Write-Ok "$($def.Name): $masked"
        $activeModels += $def
    }

    if ($activeModels.Count -eq 0) {
        Write-Err "No active models with valid API keys. Set env vars and retry."
        if ($Execute) { exit 1 }
    }

    # --- B1: Evaluate each model ---
    if (-not $DryRun -and -not $Execute) {
        Write-Info "DryRun: would evaluate $($activeModels.Count) model(s)"
    }

    $evalInput = if (Test-Path $CORE_JSON) { $CORE_JSON } else { $BENCHMARK_JSON }

    # Use DeepSeek as default judge
    $judgeModel = "deepseek-v4-flash"
    $judgeBaseUrl = "https://api.deepseek.com"
    $judgeApiKey = [Environment]::GetEnvironmentVariable("OPENAI_API_KEY")
    if (-not $judgeApiKey -and $activeModels.Count -gt 0) {
        Write-Warn "OPENAI_API_KEY not set — judge unavailable. Falling back to $($activeModels[0].Name) API key."
        $judgeApiKey = [Environment]::GetEnvironmentVariable($activeModels[0].KeyEnv)
    }

    $evalOk = $true
    foreach ($def in $activeModels) {
        $evalOutput = Join-Path $ResultsDir "eval_$($def.Name.ToLower()).json"
        $targetKey = [Environment]::GetEnvironmentVariable($def.KeyEnv)

        $evalArgs = @(
            "benchmark\eval\evaluate.py",
            "--mode", "model",
            "--input", $evalInput,
            "--output", $evalOutput,
            "--target-model", $def.Model,
            "--target-base-url", $def.BaseUrl,
            "--target-api-key", $targetKey,
            "--judge-model", $judgeModel,
            "--judge-base-url", $judgeBaseUrl,
            "--judge-api-key", $judgeApiKey,
            "--format", "json",
            "--resume"
        )
        if ($EvalLimit -gt 0) {
            $evalArgs += @("--limit", $EvalLimit)
        }

        $ok = Invoke-Step -ArgList $evalArgs -Desc "evaluate.py --mode model --target-model $($def.Name)" -AllowFail
        if (-not $ok) {
            Write-Err "$($def.Name) evaluation incomplete. Continuing with remaining models."
            $evalOk = $false
        } else {
            Write-Ok "$($def.Name): $evalOutput"
        }
    }

    if ((-not $evalOk) -and $Execute) {
        Write-Warn "Some model evaluations failed. Leaderboard may be partial."
    }

    # --- B2: Leaderboard ---
    if (-not $SkipLeaderboard) {
        $n = Next-Step
        Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase B: Leaderboard Generation"

        $leaderJson = Join-Path $ResultsDir "leaderboard.json"
        $leaderHtml = Join-Path $ResultsDir "leaderboard.html"

        $summaryArgs = @(
            "benchmark\eval\summarize_multi.py",
            "--input", $ResultsDir,
            "--output", $leaderJson
        )
        $null = Invoke-Step -ArgList $summaryArgs -Desc "summarize_multi.py -> leaderboard.json" -AllowFail
        Write-Info "Leaderboard JSON: $leaderJson"

        $vizArgs = @(
            "benchmark\eval\report_viz.py",
            "--input", $ResultsDir,
            "--output", $leaderHtml
        )
        $null = Invoke-Step -ArgList $vizArgs -Desc "report_viz.py -> leaderboard.html" -AllowFail
        Write-Info "Leaderboard HTML: $leaderHtml"
    }

    Write-Info "Phase B elapsed: $(Get-Elapsed)"
} else {
    Write-Info "Phase B skipped (SkipEval)"
}

# ============================================================
# Phase C: Comprehensive Analysis
# ============================================================
if (-not $SkipAnalysis) {
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase C: Comprehensive Analysis (7 dimensions + charts)"

    $analysisArgs = @("analyze\run_all.py")
    $ok = Invoke-Step -ArgList $analysisArgs -Desc "analyze/run_all.py" -AllowFail
    if ($ok) {
        if (Test-Path (Join-Path $ANALYZE_OUT "summary_all.json")) {
            Write-Ok "Analysis complete: $ANALYZE_OUT"
        }
    } else {
        Write-Warn "Analysis incomplete. Check $ANALYZE_OUT for partial results."
    }

    Write-Info "Phase C elapsed: $(Get-Elapsed)"
} else {
    Write-Info "Phase C skipped (SkipAnalysis)"
}

# ============================================================
# Phase D: QLoRA Fine-tuning
# ============================================================
if (-not $SkipQlora) {

    # --- D1: QLoRA Training ---
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase D1: QLoRA Training (Qwen3.5-4B-Instruct, ~87min)"

    $qloraLog = Join-Path $QLORA_DIR "train.log"
    $qloraErr = Join-Path $QLORA_DIR "train.err.log"

    if ($BackgroundLong) {
        $bg = Invoke-Background -ArgList @("finetune\scripts\train_qlora.py") `
            -LogFile $qloraLog -ErrFile $qloraErr `
            -Desc "QLoRA training (background)"
        Write-Info "QLoRA training PID=$($bg.Pid). Monitor: Get-Content -Tail 10 $qloraLog"
        Write-Info "Await completion before Phase D2 eval."
    } else {
        $null = Invoke-Step -ArgList @("finetune\scripts\train_qlora.py") `
            -Desc "train_qlora.py (~87min)" -AllowFail
        if (Test-Path (Join-Path $QLORA_FINAL "adapter_config.json")) {
            Write-Ok "QLoRA training complete: $QLORA_FINAL"
        } else {
            Write-Warn "QLoRA training may be incomplete. Check $qloraLog"
        }
    }

    # --- D2: QLoRA Evaluation ---
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase D2: QLoRA Evaluation (Phase 1: generate answers)"

    $evalLog = Join-Path $QLORA_DIR "eval.log"
    $evalErr = Join-Path $QLORA_DIR "eval.err.log"

    if ($BackgroundLong) {
        $bg = Invoke-Background -ArgList @("finetune\scripts\eval_two_phase.py", "--phase", "generate", "--resume") `
            -LogFile $evalLog -ErrFile $evalErr `
            -Desc "QLoRA eval (background)"
        Write-Info "QLoRA eval PID=$($bg.Pid). Monitor: Get-Content -Tail 3 $evalLog"
        Write-Warn "D2 eval launched in background — ensure D1 training completed first or eval will fail (no adapter)."
        Write-Warn "  Check: Test-Path '$QLORA_FINAL\adapter_config.json' before launching D2 manually."
    } else {
        $null = Invoke-Step -ArgList @("finetune\scripts\eval_two_phase.py", "--phase", "generate", "--resume") `
            -Desc "eval_two_phase.py --phase generate" -AllowFail
        if (Test-Path (Join-Path $QLORA_DIR "progress.jsonl")) {
            Write-Ok "QLoRA eval generation started"
        }
    }

    Write-Info "Phase D elapsed: $(Get-Elapsed)"
} else {
    Write-Info "Phase D skipped (SkipQlora)"
}

# ============================================================
# Phase E: Local Judge (Ollama 35B)
# ============================================================
if (-not $SkipLocalJudge) {
    $n = Next-Step
    Write-Step -Number $n -Total $TOTAL_STEPS -Msg "Phase E: Local Judge Evaluation (Ollama qwen3.5:35b)"

    $ollamaAvailable = $false
    $ollamaJob = Start-Job -ScriptBlock { & ollama list 2>&1; $LASTEXITCODE }
    $ollamaJob | Wait-Job -Timeout 5 | Out-Null
    if ($ollamaJob.State -eq "Completed") {
        $raw = $ollamaJob | Receive-Job
        $exitCode = @($raw)[-1]
        if ($exitCode -eq 0) { $ollamaAvailable = $true }
    }
    $ollamaJob | Remove-Job -Force -ErrorAction SilentlyContinue

    if (-not $ollamaAvailable) {
        Write-Warn "Ollama not available — skipping local judge eval."
    } else {
        $localJudgeInput = if (Test-Path $CORE_JSON) { $CORE_JSON } elseif (Test-Path $BENCHMARK_JSON) { $BENCHMARK_JSON } else { $null }

        if (-not $localJudgeInput) {
            Write-Err "No benchmark JSON found (tried core.json, benchmark.json). Run Phase A first."
            if ($Execute) { exit 1 }
        }

        $localJudgeOut = Join-Path $ResultsDir "ollama_judge_35b.json"
        $localJudgeLog = Join-Path $ResultsDir "ollama_judge_35b.log"
        $localJudgeErr = Join-Path $ResultsDir "ollama_judge_35b.err.log"

        $judgeArgs = @(
            "benchmark\eval\evaluate.py",
            "--mode", "model",
            "--input", $localJudgeInput,
            "--output", $localJudgeOut,
            "--target-model", "deepseek-v4-flash",
            "--judge-model", "qwen3.5:35b",
            "--judge-base-url", "http://localhost:11434/v1",
            "--judge-api-key", "ollama",
            "--resume",
            "--max-consecutive-failures", "10"
        )

        if ($BackgroundLong) {
            $bg = Invoke-Background -ArgList $judgeArgs `
                -LogFile $localJudgeLog -ErrFile $localJudgeErr `
                -Desc "35B Judge (background, ~12min for 500 Qs on RTX 5090)"
        } else {
            $null = Invoke-Step -ArgList $judgeArgs `
                -Desc "35B Judge evaluation (500 Qs)" -AllowFail
            if (Test-Path $localJudgeOut) {
                Write-Ok "35B Judge complete: $localJudgeOut"
            }
        }
    }

    Write-Info "Phase E elapsed: $(Get-Elapsed)"
} else {
    Write-Info "Phase E skipped (SkipLocalJudge)"
}

# ============================================================
# Completion Summary
# ============================================================
$totalTime = Get-Elapsed
Write-Host ""
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host "  Pipeline Complete" -ForegroundColor Green
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host "  Elapsed:        $totalTime"
Write-Host "  Mode:           $(if ($Execute) { 'EXECUTE' } else { 'DRY-RUN' })"
Write-Host "  Limit (gen):    $Limit"
Write-Host "  Eval Limit:     $(if ($EvalLimit -eq 0) { 'ALL' } else { $EvalLimit })"

Write-Host ""
Write-Host "  Phase A — Dataset:" -ForegroundColor White
$phaseA_files = @(
    @{Path=$METADATA_JSON; Label="metadata.json"},
    @{Path=$BENCHMARK_JSON; Label="benchmark.json"},
    @{Path=$REVIEW_JSON;    Label="manual_review.json"},
    @{Path=$CORE_JSON;      Label="core.json (500 core set)"},
    @{Path=$FULL_JSON;      Label="full.json (full set)"}
)
foreach ($f in $phaseA_files) {
    if (Test-Path $f.Path) {
        $sz = [math]::Round((Get-Item $f.Path).Length / 1KB, 1)
        Write-Host "    [OK] $($f.Label) ($sz KB)" -ForegroundColor Green
    } else {
        Write-Host "    [$($SkipDataset -or -not $Execute ? 'DRY' : 'MISS')] $($f.Label)" -ForegroundColor $(if ($SkipDataset) { "DarkGray" } else { "Yellow" })
    }
}

Write-Host ""
Write-Host "  Phase B — Eval Results ($ResultsDir):" -ForegroundColor White
$targetList = $TargetModels -split ',' | ForEach-Object { $_.Trim().ToLower() }
foreach ($m in $targetList) {
    $evalFile = Join-Path $ResultsDir "eval_$m.json"
    if (Test-Path $evalFile) {
        $sz = [math]::Round((Get-Item $evalFile).Length / 1KB, 1)
        Write-Host "    [OK] eval_$m.json ($sz KB)" -ForegroundColor Green
    } else {
        $label = if ($SkipEval -or -not $Execute) { "DRY" } else { "MISS" }
        Write-Host "    [$label] eval_$m.json" -ForegroundColor $(if ($SkipEval) { "DarkGray" } else { "Yellow" })
    }
}

$leaderJson = Join-Path $ResultsDir "leaderboard.json"
$leaderHtml = Join-Path $ResultsDir "leaderboard.html"
if (Test-Path $leaderJson) { Write-Host "    [OK] leaderboard.json" -ForegroundColor Green }
else { Write-Host "    [$($SkipEval -or $SkipLeaderboard -or -not $Execute ? 'DRY' : 'MISS')] leaderboard.json" -ForegroundColor $(if ($SkipEval) { "DarkGray" } else { "Yellow" }) }
if (Test-Path $leaderHtml) { Write-Host "    [OK] leaderboard.html" -ForegroundColor Green }
else { Write-Host "    [$($SkipEval -or $SkipLeaderboard -or -not $Execute ? 'DRY' : 'MISS')] leaderboard.html" -ForegroundColor $(if ($SkipEval) { "DarkGray" } else { "Yellow" }) }

Write-Host ""
Write-Host "  Phase C — Analysis ($ANALYZE_OUT):" -ForegroundColor White
if (Test-Path (Join-Path $ANALYZE_OUT "summary_all.json")) {
    Write-Host "    [OK] 7 analysis JSONs + charts" -ForegroundColor Green
} else {
    $label = if ($SkipAnalysis -or -not $Execute) { "DRY" } else { "MISS" }
    Write-Host "    [$label] analysis outputs" -ForegroundColor $(if ($SkipAnalysis) { "DarkGray" } else { "Yellow" })
}

Write-Host ""
Write-Host "  Phase D — QLoRA ($QLORA_FINAL):" -ForegroundColor White
if (Test-Path (Join-Path $QLORA_FINAL "adapter_config.json")) {
    $adapterSize = [math]::Round((Get-ChildItem $QLORA_FINAL -Recurse | Measure-Object -Property Length -Sum).Sum / 1MB, 1)
    Write-Host "    [OK] QLoRA adapter ($adapterSize MB)" -ForegroundColor Green
} else {
    $label = if ($SkipQlora -or -not $Execute) { "DRY" } else { "MISS" }
    Write-Host "    [$label] qlora-final adapter" -ForegroundColor $(if ($SkipQlora) { "DarkGray" } else { "Yellow" })
}

Write-Host ""
Write-Host "  Phase E — Local Judge:" -ForegroundColor White
$localJudgeOut = Join-Path $ResultsDir "ollama_judge_35b.json"
if (Test-Path $localJudgeOut) {
    $sz = [math]::Round((Get-Item $localJudgeOut).Length / 1KB, 1)
    Write-Host "    [OK] ollama_judge_35b.json ($sz KB)" -ForegroundColor Green
} else {
    $label = if ($SkipLocalJudge -or -not $Execute) { "DRY" } else { "MISS" }
    Write-Host "    [$label] ollama_judge_35b.json" -ForegroundColor $(if ($SkipLocalJudge) { "DarkGray" } else { "Yellow" })
}

# Background process summary
if ($BackgroundLong) {
    Write-Host ""
    Write-Host "  Background Processes:" -ForegroundColor Magenta
    if (-not $SkipQlora) {
        Write-Host "    QLoRA Training:  $qloraLog" -ForegroundColor Gray
        Write-Host "    QLoRA Eval:      $evalLog" -ForegroundColor Gray
    }
    if (-not $SkipLocalJudge -and $ollamaAvailable) {
        Write-Host "    35B Judge:       $localJudgeLog" -ForegroundColor Gray
    }
}

if (-not $Execute) {
    Write-Host ""
    Write-Host "  This was a DRY-RUN. To execute:" -ForegroundColor Yellow
    Write-Host "    .\run_agent.ps1 -Execute -Limit 10" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  Minimal validation:" -ForegroundColor Gray
    Write-Host "    .\run_agent.ps1 -Execute -Limit 10 -SkipQlora -SkipLocalJudge" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Full pipeline (500 Qs, all phases):" -ForegroundColor Gray
    Write-Host "    .\run_agent.ps1 -Execute -Limit 0" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Eval only (existing dataset):" -ForegroundColor Gray
    Write-Host "    .\run_agent.ps1 -Execute -SkipDataset -SkipAnalysis -SkipQlora -SkipLocalJudge" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Dataset + Eval only:" -ForegroundColor Gray
    Write-Host "    .\run_agent.ps1 -Execute -SkipAnalysis -SkipQlora -SkipLocalJudge" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Background QLoRA + 35B (overnight):" -ForegroundColor Gray
    Write-Host "    .\run_agent.ps1 -Execute -SkipDataset -SkipEval -SkipAnalysis -BackgroundLong" -ForegroundColor Gray
}

exit 0
