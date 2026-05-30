<#
.SYNOPSIS
    Medical Data Agent 一键复现 / One-Click Reproduction
    医疗 RAG 全流程: 切片→索引→检索→自评测→QA格式化→可视化

.DESCRIPTION
    从 MinerU 解析的 97 篇 PMC 医疗文献 Markdown 出发，一键复现：
      Step 1 -- 医疗章节本体切片 (层级语义树)
      Step 2 -- QLoRA 医疗 4B 微调 (可选)
      Step 3 -- Hybrid 索引构建 (FAISS Dense + BM25 Sparse)
      Step 4-5 -- 知识库自评测 (smoke 默认轻量 Judge；report 为 14 源评分矩阵)
      Step 6 -- 跨文献证据合成 + QA 格式化
      Step 7 -- 可视化 (可选)

    默认 DryRun 模式 (仅预览)。使用 -Execute 实际执行。

.PARAMETER Execute
    实际执行流水线 (默认 DryRun 预览)。

.PARAMETER Quiet
    静默模式，仅输出摘要。

.PARAMETER SkipTrain
    跳过 QLoRA 微调 (当 adapter 已就绪时)。

.PARAMETER SkipViz
    跳过可视化图表生成。

.PARAMETER Profile
    运行策略: smoke 为高可用最小真实测试，report 为报告级完整评估。

.PARAMETER Help
    显示完整帮助信息。

.EXAMPLE
    # 预览执行计划
    .\run_medical_agent.ps1

.EXAMPLE
    # 执行全流程
    .\run_medical_agent.ps1 -Execute

.EXAMPLE
    # 跳过微调和可视化
    .\run_medical_agent.ps1 -Execute -SkipTrain -SkipViz

.NOTES
    Author:  ControlSci Project
    Version: 1.0
    Date:    2026-05-11
    Phase:   7 / Task 7
#>

param(
    [switch]$Execute,
    [switch]$Quiet,
    [switch]$SkipTrain,
    [switch]$SkipViz,
    [ValidateSet("smoke", "report")]
    [string]$Profile = "smoke",
    [switch]$Help
)

if ($Help) {
    Get-Help -Detailed $PSCommandPath
    exit 0
}

$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONUTF8 = '1'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$ROOT = (Resolve-Path $PSScriptRoot).Path
$PYTHON = "conda"
$ENV_FLAGS = @("run", "--no-capture-output", "-n", "myenv", "python")

trap {
    Write-Err "Pipeline terminated: $_"
    exit 2
}

$MEDICAL_DIR   = Join-Path $ROOT "data\sources_medical"
$MD_DIR        = Join-Path $MEDICAL_DIR "md"
$CHUNKS_DIR    = Join-Path $MEDICAL_DIR "chunks"
$INDEX_DIR     = Join-Path $MEDICAL_DIR "index"
$QA_DIR        = Join-Path $MEDICAL_DIR "qa"
$MANIFEST_PATH = Join-Path $CHUNKS_DIR "chunks_manifest.json"
$RESULTS_DIR   = Join-Path $ROOT "benchmark\eval\results\medical"
$ASSETS_DIR    = Join-Path $ROOT "docs\assets\medical"
$QLORA_ADAPTER = Join-Path $ROOT "finetune\output\qlora-medical\adapter_config.json"

$AGENT_CLI     = Join-Path $ROOT "benchmark\agent\agent_cli.py"
$RAG_HANDLER   = Join-Path $ROOT "benchmark\agent\medical_rag_handler.py"
$BUILD_IDX     = Join-Path $ROOT "controlsci\medical\indexing.py"
$EVAL_KB       = Join-Path $ROOT "controlsci\medical\kb_quality.py"
$QA_FORMATTER  = Join-Path $ROOT "controlsci\medical\qa_formatter.py"
$VIZ_SCRIPT    = Join-Path $ROOT "controlsci\medical\visualization.py"

$START_TIME = Get-Date
$pipelineOk = $false

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

function Test-Dir {
    param([string]$Path, [string]$Label)
    if (Test-Path $Path) {
        $count = @(Get-ChildItem -Path $Path -ErrorAction SilentlyContinue).Count
        Write-Ok "$Label exists ($count items): $Path"
        return $true
    }
    Write-Warn "$Label missing: $Path"
    return $false
}

# ============================================================
# Banner
# ============================================================
if (-not $Quiet) {
    Write-Host ""
    Write-Host "  +----------------------------------------------------+" -ForegroundColor Cyan
    Write-Host "  |   Medical Data Agent  One-Click Repro v1.0         |" -ForegroundColor Cyan
    Write-Host "  |   医疗 RAG 全流程: 切片 -> 索引 -> 评测 -> QA      |" -ForegroundColor Cyan
    Write-Host "  |   Start: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')                   |" -ForegroundColor Cyan
    Write-Host "  +----------------------------------------------------+" -ForegroundColor Cyan
}

Write-Host ""
if ($Execute) {
    Write-Host "  Mode: EXECUTE" -ForegroundColor Green
} else {
    Write-Host "  Mode: DRY-RUN (preview only, use -Execute to run)" -ForegroundColor Yellow
}
Write-Host "  Skip QLoRA:  $(if ($SkipTrain) { 'YES' } else { 'NO' })"
Write-Host "  Skip Viz:    $(if ($SkipViz) { 'YES' } else { 'NO' })"
Write-Host "  Profile:     $Profile"
Write-Host "  Root:        $ROOT"
Write-Host ""

# ============================================================
# Step 0: Prerequisite Checks
# ============================================================
Write-Step -Number 0 -Total 7 -Msg "Step 0: Prerequisite Checks"

$allOk = $true

# Conda env
$condaInfo = conda run -n myenv python --version 2>&1
if (($LASTEXITCODE -ne 0) -or -not $?) {
    Write-Err "conda myenv not available. Create: conda create -n myenv python=3.12 -y"
    $allOk = $false
} else {
    Write-Ok "conda (myenv): $condaInfo"
}

# Medical data: md/
if (-not (Test-Dir -Path $MD_DIR -Label "MD directory")) { $allOk = $false }

# Medical data: chunks manifest
if (Test-File -Path $MANIFEST_PATH -Label "chunks manifest") {
    try {
        $manifestData = Get-Content $MANIFEST_PATH -Encoding UTF8 | ConvertFrom-Json
        $totalChunks = if ($manifestData.metadata.total_chunks) { $manifestData.metadata.total_chunks } else { $manifestData.total_chunks }
        $trainChunks = if ($manifestData.metadata.train_count) { $manifestData.metadata.train_count } else { $manifestData.train_chunks }
        $evalChunks = if ($manifestData.metadata.eval_count) { $manifestData.metadata.eval_count } else { $manifestData.eval_chunks }
        Write-Ok "chunks: $totalChunks chunks, $trainChunks train / $evalChunks eval"
    } catch {
        Write-Warn "chunks manifest JSON 解析失败: $_"
        $allOk = $false
    }
} else { $allOk = $false }

# Medical data: index
$null = Test-File -Path (Join-Path $INDEX_DIR "medical.index") -Label "FAISS index"
$null = Test-File -Path (Join-Path $INDEX_DIR "bm25.pkl") -Label "BM25 index"

# QLoRA adapter
if (-not $SkipTrain) {
    $null = Test-File -Path $QLORA_ADAPTER -Label "QLoRA adapter"
}

# API Keys
$dsKey = if ($env:DEEPSEEK_API_KEY) { $env:DEEPSEEK_API_KEY } else { $env:OPENAI_API_KEY }
if ($dsKey) {
    Write-Ok "DEEPSEEK_API_KEY/OPENAI_API_KEY: set (DeepSeek Judge)"
} else {
    Write-Warn "DEEPSEEK_API_KEY/OPENAI_API_KEY not set (required for Judge scoring)"
}

$mimoKey = $env:MIMO_API_KEY
if ($mimoKey) {
    Write-Ok "MIMO_API_KEY: set"
} else {
    Write-Info "MIMO_API_KEY not set (optional)"
}

$minimaxKey = $env:MINIMAX_API_KEY
if ($minimaxKey) {
    Write-Ok "MINIMAX_API_KEY: set"
} else {
    Write-Info "MINIMAX_API_KEY not set (optional)"
}

# Ollama (with 5s timeout guard)
$ollamaAvailable = $false
try {
    $ollamaJob = Start-Job -ScriptBlock { & ollama list *>$null; $LASTEXITCODE }
    $ollamaJob | Wait-Job -Timeout 5 | Out-Null
    if ($ollamaJob.State -eq "Completed") {
        $raw = $ollamaJob | Receive-Job
        $ollamaAvailable = ($raw.Count -gt 0 -and $raw[$raw.Count - 1] -is [int] -and $raw[$raw.Count - 1] -eq 0)
    } elseif ($ollamaJob.State -eq "Running") {
        $ollamaJob | Stop-Job | Out-Null
    }
    $ollamaJob | Remove-Job -Force -ErrorAction SilentlyContinue
} catch {
    $ollamaJob | Remove-Job -Force -ErrorAction SilentlyContinue
}
if ($ollamaAvailable) {
    Write-Ok "Ollama: running"
} else {
    Write-Info "Ollama daemon not available (Hybrid retrieval requires qwen3-embedding:4b)"
}

# Key scripts
$scriptChecks = @(
    @{Path=$AGENT_CLI;    Label="agent_cli.py"},
    @{Path=$RAG_HANDLER;  Label="medical_rag_handler.py"},
    @{Path=$BUILD_IDX;    Label="build_medical_index.py"},
    @{Path=$EVAL_KB;      Label="eval_kb_quality.py"},
    @{Path=$QA_FORMATTER; Label="medical_qa_formatter.py"},
    @{Path=$VIZ_SCRIPT;   Label="viz_medical_rag.py"}
)
foreach ($sc in $scriptChecks) {
    if (Test-Path $sc.Path) {
        Write-Ok "$($sc.Label) ready"
    } else {
        Write-Warn "$($sc.Label) not found: $($sc.Path) — step will be skipped"
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
# Pipeline — delegate to agent_cli.py
# ============================================================
Write-Step -Number 1 -Total 7 -Msg "Medical RAG Pipeline: 切片 → 微调 → 索引 → 评测 → QA → Viz"

Write-Info "Delegating to agent_cli.py --intents medical_rag"

$medicalParams = @{ profile = $Profile }
if ($SkipTrain) { $medicalParams["skip_train"] = $true }
if ($SkipViz)   { $medicalParams["skip_viz"]   = $true }

$agentArgs = @(
    $AGENT_CLI,
    "--intents", "medical_rag",
    "--no-expand-deps"
)
if ($medicalParams.Count -gt 0) {
    $wrapped = @{ medical_rag = $medicalParams }
    $paramsJson = ($wrapped | ConvertTo-Json -Compress)
    $agentArgs += @("--intent-params", $paramsJson)
    Write-Info "intent-params: $paramsJson"
}

if ($Execute) {
    Write-Host ""
    Write-Host "  ╔═══════════════════════════════════════════════════╗" -ForegroundColor Magenta
    Write-Host "  ║  Medical Data Agent Pipeline Starting...          ║" -ForegroundColor Magenta
    Write-Host "  ║  (full output below from medical_rag_handler.py)  ║" -ForegroundColor Magenta
    Write-Host "  ╚═══════════════════════════════════════════════════╝" -ForegroundColor Magenta
    Write-Host ""

    $proc = Start-Process -FilePath $PYTHON -ArgumentList ($ENV_FLAGS + $agentArgs) `
        -NoNewWindow -Wait -PassThru -WorkingDirectory $ROOT

    $pipelineOk = ($proc.ExitCode -eq 0)
    if ($pipelineOk) {
        Write-Ok "Medical RAG pipeline complete"
    } else {
        Write-Err "Medical RAG pipeline failed (exit=$($proc.ExitCode))"
    }
} else {
    Write-Host ""
    Write-Host "  [DRY-RUN] Would execute:" -ForegroundColor DarkGray
    $dryCmd = "conda run --no-capture-output -n myenv python $($agentArgs -join ' ')"
    Write-Host "    $dryCmd" -ForegroundColor DarkGray
    Write-Host ""
    Write-Host "  Pipeline steps (via medical_rag_handler.py):" -ForegroundColor DarkGray
    Write-Host "    1. 医疗章节本体切片 (层级语义树)" -ForegroundColor DarkGray
    Write-Host "    2. QLoRA 微调 $(if ($SkipTrain) { '[SKIP]' } else { '' })" -ForegroundColor DarkGray
    Write-Host "    3. Hybrid 索引构建 (FAISS + BM25)" -ForegroundColor DarkGray
    if ($Profile -eq "smoke") {
        Write-Host "    4. 知识库自评测 (smoke: 1 query / 1 local judge)" -ForegroundColor DarkGray
    } else {
        Write-Host "    4. 知识库自评测 (report: 14 源评分矩阵)" -ForegroundColor DarkGray
    }
    Write-Host "    5. QA 格式化 (官方格式封装)" -ForegroundColor DarkGray
    Write-Host "    6. 可视化 $(if ($SkipViz) { '[SKIP]' } else { '' })" -ForegroundColor DarkGray
    $pipelineOk = $true
}

# ============================================================
# Completion Summary
# ============================================================
$totalTime = Get-Elapsed
Write-Host ""
Write-Host ("=" * 60) -ForegroundColor Cyan
if ($pipelineOk) {
    Write-Host "  Medical Data Agent Pipeline Complete" -ForegroundColor Green
} else {
    Write-Host "  Medical Data Agent Pipeline FAILED" -ForegroundColor Red
}
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host "  Elapsed:    $totalTime"
Write-Host "  Mode:       $(if ($Execute) { 'EXECUTE' } else { 'DRY-RUN' })"
Write-Host "  Profile:    $Profile"
Write-Host "  Skip Train: $(if ($SkipTrain) { 'YES' } else { 'NO' })"
Write-Host "  Skip Viz:   $(if ($SkipViz) { 'YES' } else { 'NO' })"
Write-Host ""

Write-Host "  Input Assets:" -ForegroundColor White
if (Test-Path $MANIFEST_PATH) { Write-Host "    [OK] chunks manifest" -ForegroundColor Green } else { Write-Host "    [MISS] chunks manifest" -ForegroundColor DarkGray }
if (Test-Path (Join-Path $INDEX_DIR "medical.index")) { Write-Host "    [OK] FAISS index" -ForegroundColor Green } else { Write-Host "    [MISS] FAISS index" -ForegroundColor DarkGray }
if (Test-Path (Join-Path $INDEX_DIR "bm25.pkl")) { Write-Host "    [OK] BM25 index" -ForegroundColor Green } else { Write-Host "    [MISS] BM25 index" -ForegroundColor DarkGray }
if (-not $SkipTrain) {
    if (Test-Path $QLORA_ADAPTER) { Write-Host "    [OK] QLoRA adapter" -ForegroundColor Green } else { Write-Host "    [MISS] QLoRA adapter" -ForegroundColor DarkGray }
}

Write-Host ""
Write-Host "  Output Files:" -ForegroundColor White
$pipelineReport = Join-Path $RESULTS_DIR "pipeline_summary.json"
$kbQualityReport = Join-Path $RESULTS_DIR "kb_quality_report.json"
if (Test-Path $pipelineReport) {
    $sz = [math]::Round((Get-Item $pipelineReport).Length / 1KB, 1)
    Write-Host "    [OK] pipeline_summary.json ($sz KB)" -ForegroundColor Green
} else {
    Write-Host "    [$(if ($Execute) { 'MISS' } else { 'DRY' })] pipeline_summary.json (not yet generated)" -ForegroundColor $(if ($Execute) { 'Yellow' } else { 'DarkGray' })
}
if (Test-Path $kbQualityReport) {
    $sz = [math]::Round((Get-Item $kbQualityReport).Length / 1KB, 1)
    Write-Host "    [OK] kb_quality_report.json ($sz KB)" -ForegroundColor Green
} else {
    Write-Host "    [$(if ($Execute) { 'MISS' } else { 'DRY' })] kb_quality_report.json (not yet generated)" -ForegroundColor $(if ($Execute) { 'Yellow' } else { 'DarkGray' })
}

Write-Host ""
Write-Host "  Directory Tree:" -ForegroundColor White
Write-Host "    data/sources_medical/" -ForegroundColor Gray
Write-Host "      md/     — MinerU 解析产物 (97 .md)" -ForegroundColor Gray
Write-Host "      chunks/ — 语义切片 (3,348 chunks)" -ForegroundColor Gray
Write-Host "      index/  — Hybrid 索引 (FAISS + BM25)" -ForegroundColor Gray
Write-Host "      qa/     — 官方 QA 格式输出" -ForegroundColor Gray
Write-Host "    benchmark/eval/results/medical/ — 评估报告" -ForegroundColor Gray
Write-Host "    docs/assets/medical/            — 可视化图表" -ForegroundColor Gray

if (-not $Execute) {
    Write-Host ""
    Write-Host "  This was a DRY-RUN. To execute:" -ForegroundColor Yellow
    Write-Host "    .\run_medical_agent.ps1 -Execute" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  Skip training (existing adapter):" -ForegroundColor Gray
    Write-Host "    .\run_medical_agent.ps1 -Execute -SkipTrain -SkipViz -Profile smoke" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Report-level full evaluation:" -ForegroundColor Gray
    Write-Host "    .\run_medical_agent.ps1 -Execute -Profile report" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Or call handler directly:" -ForegroundColor Gray
    Write-Host "    conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py --intents medical_rag" -ForegroundColor Gray
}

exit $(if ($pipelineOk) { 0 } else { 1 })
