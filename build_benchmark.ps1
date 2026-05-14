<#
.SYNOPSIS
    ControlSci Cross-Modal Alignment Benchmark 一键复现 / One-Click Reproduction
    Phase 1-4 Full Pipeline: 校验 -> 元数据 -> 题目生成 -> 仲裁 -> 拆分 -> 验证

.DESCRIPTION
    从语料 Markdown 出发，完整复现 ControlSci 评测基准数据集：
      Phase 1  -- 前置校验 (MinerU 产物就绪检查)
      Phase 2  -- 元数据重建 (corpus/metadata.json)
      Phase 3  -- 题目生成   (benchmark/dataset/benchmark.json)
      Phase 4  -- 仲裁拆分验证 (core.json + full.json)
      可选     -- 格式导出 / 评测启动

    默认使用 Mock 模式 (确定性输出，零 API 调用)。
    API 模式需配置 Provider Key 环境变量。

.PARAMETER Mock
    使用 Mock 模式生成题目 (确定性，无 API 调用)。默认开启。

.PARAMETER Api
    API 模式：由 LLM 实时生成题目 (需配置 Provider Key 环境变量)。

.PARAMETER Provider
    API 模式下使用的 Provider: deepseek / minimax / mimo。默认 deepseek。

.PARAMETER Limit
    生成题目数量上限。默认 500。

.PARAMETER SkipMetadata
    跳过 Phase 2 元数据重建。

.PARAMETER SkipBenchmark
    跳过 Phase 3 题目生成。

.PARAMETER SkipArbitrate
    跳过 Phase 4 仲裁步骤。

.PARAMETER SkipValidate
    跳过 Phase 4 验证步骤。

.PARAMETER SkipSplit
    跳过 Phase 4 拆分步骤 (不生成 core.json / full.json)。

.PARAMETER SkipExport
    跳过格式导出步骤。

.PARAMETER DryRun
    打印执行计划而不实际运行任何命令。

.PARAMETER Quiet
    静默模式，仅输出摘要。

.PARAMETER Resume
    断点续跑：从已有 checkpoint 恢复 Phase 3 题目生成。

.PARAMETER Supplement
    向已有 benchmark.json 追加 N 道题目。

.PARAMETER PushToHub
    HuggingFace 数据集仓库名。传入则启用在导出阶段推送到 HF Hub。

.PARAMETER HfToken
    HuggingFace write token。也可通过 HF_TOKEN 环境变量传入。

.PARAMETER Help
    显示完整帮助信息。

.EXAMPLE
    # 默认：Mock 模式完整复现 (500 题)
    .\build_benchmark.ps1

.EXAMPLE
    # 仅预览执行计划
    .\build_benchmark.ps1 -DryRun

.EXAMPLE
    # API 模式 DeepSeek 生成 200 题
    .\build_benchmark.ps1 -Api -Provider deepseek -Limit 200

.EXAMPLE
    # 跳过重新生成，仅运行仲裁+拆分+验证
    .\build_benchmark.ps1 -SkipBenchmark

.EXAMPLE
    # 断点续跑 + 仅验证
    .\build_benchmark.ps1 -Resume -SkipArbitrate -SkipSplit -SkipExport

.NOTES
    Author:  ControlSci Project
    Version: 1.1
    Date:    2026-05-05
    Phase:   5 / Task C1
    Changelog:
      v1.1 - 数组传参消除空格截断 / HF Token 环境变量 / 动态阶段计数器 / trap 清理
      v1.0 - 初始交付
#>

param(
    [switch]$Mock,
    [switch]$Api,
    [Alias("Provider")]
    [ValidateSet("deepseek", "mimo", "minimax")]
    [string]$ModelProvider = "deepseek",
    [int]$Limit = 500,
    [switch]$SkipMetadata,
    [switch]$SkipBenchmark,
    [switch]$SkipArbitrate,
    [switch]$SkipValidate,
    [switch]$SkipSplit,
    [switch]$SkipExport,
    [switch]$DryRun,
    [switch]$Quiet,
    [switch]$Resume,
    [int]$Supplement = 0,
    [string]$PushToHub = "",
    [string]$HfToken = "",
    [switch]$Help
)

if ($Help) {
    Get-Help -Detailed $PSCommandPath
    exit 0
}

$ErrorActionPreference = "Stop"
$ROOT = $PSScriptRoot
$PYTHON = "conda"
$ENV_FLAGS = @("run", "--no-capture-output", "-n", "myenv", "python")

$BENCHMARK_JSON = Join-Path $ROOT "benchmark\dataset\benchmark.json"
$REVIEW_JSON    = Join-Path $ROOT "benchmark\dataset\manual_review.json"
$CORE_JSON      = Join-Path $ROOT "benchmark\dataset\core.json"
$FULL_JSON      = Join-Path $ROOT "benchmark\dataset\full.json"
$MERGED_JSON    = Join-Path $ROOT "benchmark\dataset\merged.json"
$METADATA_JSON  = Join-Path $ROOT "corpus\metadata.json"

$START_TIME = Get-Date

$PROVIDER_ENV_MAP = @{
    "deepseek" = "OPENAI_API_KEY"
    "mimo"     = "MIMO_API_KEY"
    "minimax"  = "MINIMAX_API_KEY"
}

trap {
    Write-Err "Pipeline terminated: $_"
    exit 2
}

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

function Invoke-Step {
    param(
        [string[]]$ArgList,
        [string]$Desc = "",
        [switch]$AllowFail,
        [string[]]$MaskTokens = @()
    )
    $displayArgs = $ArgList
    if ($MaskTokens.Count -gt 0) {
        $displayArgs = @()
        $skipNext = $false
        foreach ($a in $ArgList) {
            if ($skipNext) { $displayArgs += "***"; $skipNext = $false }
            elseif ($a -in $MaskTokens) { $displayArgs += $a; $skipNext = $true }
            else { $displayArgs += $a }
        }
    }
    $cmdStr = $displayArgs -join " "

    if ($DryRun) {
        Write-Host "  [DRY-RUN] $cmdStr" -ForegroundColor DarkGray
        return $true
    }
    if (-not $Quiet -and $Desc) { Write-Host "  > $Desc" -ForegroundColor White }
    Write-Info "  $ $cmdStr"

    $proc = Start-Process -FilePath $PYTHON -ArgumentList ($ENV_FLAGS + $ArgList) `
        -NoNewWindow -Wait -PassThru
    if ($proc.ExitCode -ne 0) {
        Write-Err "Command failed (exit=$($proc.ExitCode)): $cmdStr"
        if (-not $AllowFail) { throw "Pipeline aborted at: $Desc" }
        return $false
    }
    Write-Ok "Done"
    return $true
}

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

# ============================================================
# Dynamic step count
# ============================================================
$TOTAL_STEPS = 1  # Phase 1 always runs
if (-not $SkipMetadata)  { $TOTAL_STEPS++ }
if (-not $SkipBenchmark) { $TOTAL_STEPS++ }
if (-not $SkipArbitrate) { $TOTAL_STEPS++ }
if (-not $SkipSplit)     { $TOTAL_STEPS++ }
if (-not $SkipValidate)  { $TOTAL_STEPS++ }
if (-not $SkipExport)    { $TOTAL_STEPS++ }

# ============================================================
# Banner
# ============================================================
if (-not $Quiet) {
    Write-Host ""
    Write-Host "  +----------------------------------------------------+" -ForegroundColor Cyan
    Write-Host "  |   ControlSci Cross-Modal Alignment Benchmark         |" -ForegroundColor Cyan
    Write-Host "  |   Phase 1-4 Full Pipeline v1.1                      |" -ForegroundColor Cyan
    Write-Host "  |   Start: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')                   |" -ForegroundColor Cyan
    Write-Host "  +----------------------------------------------------+" -ForegroundColor Cyan
}

$UseApi = $Api
$UseMock = -not $UseApi
if ($Mock) { $UseApi = $false; $UseMock = $true }

Write-Host ""
Write-Host "  Mode: $(if ($UseMock) { 'Mock (deterministic)' } else { "API ($ModelProvider)" })" -ForegroundColor White
Write-Host "  Limit: $Limit questions"
Write-Host "  Env: conda run -n myenv python"
Write-Host "  Steps: $TOTAL_STEPS active"
if ($Resume)       { Write-Host "  Resume: YES" }
if ($Supplement -gt 0) { Write-Host "  Supplement: +$Supplement" }
if ($DryRun)       { Write-Warn "DRY-RUN mode: printing plan only, not executing." }

# ============================================================
# Phase 1: Pre-flight checks
# ============================================================
$step = 0
$step++
Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Phase 1: Pre-flight Checks"

$prechecks = @(
    @{Path="$ROOT\pipeline\build_metadata_light.py";    Label="Metadata builder"},
    @{Path="$ROOT\benchmark\pipeline\build_benchmark.py"; Label="Benchmark builder"},
    @{Path="$ROOT\benchmark\pipeline\arbiter.py";        Label="Arbiter module"},
    @{Path="$ROOT\benchmark\pipeline\split_benchmark.py"; Label="Splitter"},
    @{Path="$ROOT\benchmark\pipeline\validate_benchmark.py"; Label="Validator"}
)
$allOk = $true
foreach ($item in $prechecks) {
    if (-not (Test-File -Path $item.Path -Label $item.Label)) { $allOk = $false }
}

$condaInfo = conda run -n myenv python --version 2>&1
$condaOk = ($LASTEXITCODE -eq 0) -and $?
if (-not $condaOk) {
    Write-Err "conda myenv not available. Create it: conda create -n myenv python=3.12 -y"
    $allOk = $false
} else {
    Write-Ok "conda (myenv): $condaInfo"
}

if (-not $allOk -and -not $DryRun) {
    Write-Err "Pre-flight checks failed. Fix and retry."
    exit 1
}

# ============================================================
# Phase 2: Metadata rebuild
# ============================================================
$step++
Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Phase 2: Metadata Rebuild -> corpus/metadata.json"

if ($SkipMetadata) {
    Write-Info "Skipped (--SkipMetadata)"
    if (-not (Test-Path $METADATA_JSON)) {
        Write-Warn "metadata.json not found, downstream steps may fail."
    }
} else {
    $null = Invoke-Step -ArgList @("pipeline\build_metadata_light.py") -Desc "build_metadata_light.py"
    if (Test-Path $METADATA_JSON) {
        $metaSize = (Get-Item $METADATA_JSON).Length
        Write-Ok "metadata.json generated ($([math]::Round($metaSize / 1KB, 1)) KB)"
    } elseif (-not $DryRun) {
        Write-Err "metadata.json not generated."
        exit 1
    }
}

# ============================================================
# Phase 3: Question generation
# ============================================================
$step++
Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Phase 3: Question Generation -> benchmark/dataset/benchmark.json"

if ($SkipBenchmark) {
    Write-Info "Skipped (--SkipBenchmark)"
    if (-not (Test-Path $BENCHMARK_JSON)) {
        Write-Warn "benchmark.json not found. Ensure a benchmark file exists."
    }
} else {
    $buildArgList = @("benchmark\pipeline\build_benchmark.py")
    if ($UseMock) {
        $buildArgList += @("--mock")
    } else {
        $envVarName = $PROVIDER_ENV_MAP[$ModelProvider]
        Write-Warn "API mode: will call $ModelProvider to generate $Limit questions."
        Write-Warn "Ensure env var is set: `$$envVarName"
        $buildArgList += @("--provider", $ModelProvider)
    }
    $buildArgList += @("--limit", $Limit, "--output", $BENCHMARK_JSON, "--manual-review-output", $REVIEW_JSON)
    if ($Resume) { $buildArgList += "--resume" }
    if ($Supplement -gt 0) { $buildArgList += @("--supplement", $Supplement) }

    $label = if ($UseMock) { "build_benchmark.py --mock --limit $Limit" }
             else { "build_benchmark.py --provider $ModelProvider --limit $Limit" }
    $null = Invoke-Step -ArgList $buildArgList -Desc $label

    if (Test-Path $BENCHMARK_JSON) {
        $stats = Get-Content $BENCHMARK_JSON -Encoding UTF8 | ConvertFrom-Json
        Write-Ok "benchmark.json: $($stats.questions.Count) questions"
    } elseif (-not $DryRun) {
        Write-Err "benchmark.json not generated."
        if (-not $UseMock -and (Test-Path ($BENCHMARK_JSON -replace '\.json$', '.checkpoint.json'))) {
            Write-Info "Checkpoint found -- use -Resume to continue."
        }
        exit 1
    }
}

# ============================================================
# Phase 4a: Arbitration
# ============================================================
$step++
Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Phase 4a: Arbitration -- resolve needs_review"

if ($SkipArbitrate) {
    Write-Info "Skipped (--SkipArbitrate)"
} else {
    if (-not (Test-Path $BENCHMARK_JSON) -and -not $DryRun) { Write-Err "benchmark.json missing."; exit 1 }
    if (-not (Test-Path $REVIEW_JSON) -and -not $DryRun)    { Write-Err "manual_review.json missing."; exit 1 }

    $arbArgList = @("benchmark\pipeline\build_benchmark.py", "--arbitrate", "--output", $BENCHMARK_JSON, "--manual-review-output", $REVIEW_JSON)
    $null = Invoke-Step -ArgList $arbArgList -Desc "build_benchmark.py --arbitrate"

    if (Test-Path $BENCHMARK_JSON) {
        $arbStats = Get-Content $BENCHMARK_JSON -Encoding UTF8 | ConvertFrom-Json
        $kept = ($arbStats.questions | Where-Object { $_.consistency_status -in @("auto_passed","reviewed_kept") }).Count
        $discarded = ($arbStats.questions | Where-Object { $_.consistency_status -eq "reviewed_discarded" }).Count
        Write-Ok "Post-arbitration: $kept kept, $discarded discarded"
    }
}

# ============================================================
# Phase 4b: Split (core.json + full.json)
# ============================================================
$step++
Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Phase 4b: Split -> core.json (500) + full.json"

if ($SkipSplit) {
    Write-Info "Skipped (--SkipSplit)"
} else {
    $splitInput = $BENCHMARK_JSON
    if (Test-Path $MERGED_JSON) {
        $splitInput = $MERGED_JSON
        Write-Info "Using merged.json as split input"
    }
    if (-not (Test-Path $splitInput) -and -not $DryRun) { Write-Err "Split input not found: $splitInput"; exit 1 }

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
}

# ============================================================
# Phase 4c: Quality validation
# ============================================================
$step++
Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Phase 4c: Quality Validation"

if ($SkipValidate) {
    Write-Info "Skipped (--SkipValidate)"
} else {
    $validateTarget = if (Test-Path $CORE_JSON) { $CORE_JSON } else { $BENCHMARK_JSON }
    $valArgList = @("benchmark\pipeline\validate_benchmark.py", "--input", $validateTarget)
    $null = Invoke-Step -ArgList $valArgList -Desc "validate_benchmark.py"
}

# ============================================================
# Optional: HF Export
# ============================================================
$step++
Write-Step -Number $step -Total $TOTAL_STEPS -Msg "Optional: HF JSONL Export"

if ($SkipExport) {
    Write-Info "Skipped (--SkipExport)"
} else {
    $exportInput = if (Test-Path $CORE_JSON) { $CORE_JSON } else { $BENCHMARK_JSON }
    $exportArgList = @("benchmark\pipeline\export_dataset.py", "--input", $exportInput)

    if ($PushToHub) {
        $hfTokenValue = if ($HfToken) { $HfToken } else { $env:HF_TOKEN }
        if ($hfTokenValue) {
            $env:HF_TOKEN = $hfTokenValue
            $exportArgList += @("--push-to-hub", $PushToHub)
        } else {
            Write-Warn "PushToHub requires --hf-token or HF_TOKEN env var. Skipping push."
        }
    }
    $null = Invoke-Step -ArgList $exportArgList -Desc "export_dataset.py -> HF JSONL" -AllowFail
}

# ============================================================
# Completion Summary
# ============================================================
$totalTime = Get-Elapsed
Write-Host ""
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host "  Pipeline Complete" -ForegroundColor Green
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host "  Elapsed:    $totalTime"
Write-Host "  Mode:       $(if ($UseMock) { 'Mock' } else { "API ($ModelProvider)" })"
Write-Host "  Limit:      $Limit"

$outputs = @(
    @{Path=$METADATA_JSON; Label="metadata.json"},
    @{Path=$BENCHMARK_JSON; Label="benchmark.json"},
    @{Path=$REVIEW_JSON;    Label="manual_review.json"},
    @{Path=$CORE_JSON;      Label="core.json (500 core set)"},
    @{Path=$FULL_JSON;      Label="full.json (full set)"}
)

Write-Host ""
Write-Host "  Outputs:"
foreach ($out in $outputs) {
    if (Test-Path $out.Path) {
        $sz = [math]::Round((Get-Item $out.Path).Length / 1KB, 1)
        Write-Host "    [OK] $($out.Label) ($sz KB)" -ForegroundColor Green
    } else {
        Write-Host "    [MISS] $($out.Label)" -ForegroundColor $(if ($DryRun) { "DarkGray" } else { "Red" })
    }
}

Write-Host ""
Write-Host "  Next steps:"
if (Test-Path $CORE_JSON) {
    Write-Host "    > Evaluate:  conda run -n myenv python benchmark/eval/evaluate.py --mode model --input $CORE_JSON ..."
    Write-Host "    > Eval Pipe:  conda run -n myenv python benchmark/eval/run_eval_pipeline.py --benchmark $CORE_JSON --limit 10"
    Write-Host "    > Fine-tune:  conda run -n myenv python finetune/scripts/prepare_instruction_data.py"
} elseif (Test-Path $BENCHMARK_JSON) {
    Write-Host "    > Arb+Split:  .\build_benchmark.ps1 -SkipMetadata -SkipBenchmark"
}

if (-not $DryRun -and -not $Quiet) {
    Write-Host ""
    Write-Host "  File locations:" -ForegroundColor Gray
    Write-Host "    benchmark/dataset/core.json      - Core set (500 Qs)" -ForegroundColor Gray
    Write-Host "    benchmark/dataset/full.json      - Full set (889 Qs)" -ForegroundColor Gray
    Write-Host "    benchmark/dataset/benchmark.json - Raw generated" -ForegroundColor Gray
    Write-Host "    corpus/metadata.json             - Corpus metadata" -ForegroundColor Gray
}

exit 0
