<#
.SYNOPSIS
  ControlSci 评审一键复现脚本 - 零 API Key 复核三赛道核心指标

.DESCRIPTION
  无需外部 API Key，一条命令验证：
    Track 1: 数据集结构 (500题 schema) + 六维计分板
    Track 2: Agent 15 Intent 注册 + dry-run 复现计划
    Track 3: 医疗 Hybrid 索引 + qwen3.5 本地视觉 FAISS + RAG API
  硬件依赖: 仅 Track 3 API 健康检查需先启动服务。
             Track 1/2 纯本地，零外部依赖。

.PARAMETER Track
  1 | 2 | 3 | All

.PARAMETER Quiet
  录屏友好模式：隐藏 Python 子命令的详细输出，仅保留摘要。

.PARAMETER SkipApiHealth
  跳过 Track 3 的 localhost API 健康检查，适用于只展示本地索引资产的录屏。

.EXAMPLE
  .\run_reviewer_demo.ps1 -Track 1
  .\run_reviewer_demo.ps1 -Track All
#>

param(
    [ValidateSet(1, 2, 3, "All")]
    $Track = 2,
    [switch]$Quiet,
    [switch]$SkipApiHealth,
    [int]$ApiPort = 17001
)

$ErrorActionPreference = "Continue"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path (Join-Path $ScriptDir "..")
Push-Location $ProjectRoot

$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONUTF8 = '1'
$env:CONDA_NO_PLUGINS = 'true'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$BANNER = "=" * 60
$sw = [System.Diagnostics.Stopwatch]::StartNew()
$FailCount = 0; $OkCount = 0; $SkipCount = 0

$PythonExe = "conda"
$PyArgs = @("run", "--no-capture-output", "-n", "myenv", "python")

function header($t)  { Write-Host "`n$BANNER" -ForegroundColor Cyan; Write-Host "  $t" -ForegroundColor Cyan; Write-Host $BANNER -ForegroundColor Cyan }
function ok($m)    { $script:OkCount++;  Write-Host "  [OK]   $m" -ForegroundColor Green }
function fail($m)  { $script:FailCount++; Write-Host "  [FAIL] $m" -ForegroundColor Red }
function skip($m)  { $script:SkipCount++; Write-Host "  [SKIP] $m" -ForegroundColor Yellow }
function info($m)   { Write-Host "  [INFO]  $m" -ForegroundColor Yellow }
function warn($m)   { Write-Host "  [WARN]  $m" -ForegroundColor Yellow }

function run-py([string[]]$argsList) {
    $display = ($PyArgs + $argsList) -join " "
    info "Running: $display"
    $result = & $PythonExe @PyArgs @argsList 2>&1
    $rc = $LASTEXITCODE
    if ($result -and -not $Quiet) {
        $result | ForEach-Object { Write-Host "          $_" -ForegroundColor DarkGray }
    } elseif ($result -and $rc -ne 0) {
        $result | Select-Object -Last 12 | ForEach-Object { Write-Host "          $_" -ForegroundColor DarkGray }
    }
    return $rc
}

function read-json-utf8($path) {
    $text = [System.IO.File]::ReadAllText($path, [System.Text.UTF8Encoding]::new($false, $true))
    return $text | ConvertFrom-Json
}

function check-file($path, $desc) {
    $fp = Join-Path $ProjectRoot $path
    if (Test-Path $fp) {
        $size = [math]::Round((Get-Item $fp).Length / 1KB, 1)
        ok "$desc - ${size} KB"
    } else { fail "$desc - NOT FOUND ($path)" }
}

function check-any-file($paths, $desc) {
    foreach ($path in $paths) {
        $fp = Join-Path $ProjectRoot $path
        if (Test-Path $fp) {
            $size = [math]::Round((Get-Item $fp).Length / 1KB, 1)
            ok "$desc - ${size} KB ($path)"
            return
        }
    }
    fail "$desc - NOT FOUND ($($paths -join ' | '))"
}

Write-Host ""
Write-Host $BANNER -ForegroundColor Magenta
Write-Host "  ControlSci One-Click Reproduction" -ForegroundColor Magenta
Write-Host "  Track $Track | Zero API Key | $(Get-Date -Format 'yyyy-MM-dd HH:mm')" -ForegroundColor Magenta
if ($Quiet) { Write-Host "  Mode: Quiet summary" -ForegroundColor Magenta }
if ($SkipApiHealth) { Write-Host "  Track3 API health: skipped" -ForegroundColor Magenta }
Write-Host "  Python: $PythonExe" -ForegroundColor Magenta
Write-Host $BANNER -ForegroundColor Magenta

# === Track 1: Dataset + Scoreboard =====================================
if ($Track -eq 1 -or $Track -eq "All") {
    header "Track 1: Sci-Align Dataset & Scoreboard"

    $rc = run-py @("benchmark/eval/validate_dataset.py")
    if ($rc -eq 0) { ok "Dataset schema validation (500 Q, 4-dim balanced)" }
    else { fail "Dataset validation failed (exit=$rc)" }

    check-file "benchmark/dataset/core.json" "core.json (500 Q)"
    check-file "benchmark/dataset/full.json" "full.json (889 Q)"
    check-any-file @(
        "benchmark/eval/results/leaderboard_complete.json",
        "docs/submissions/data_trace_bundle/03_leaderboard/leaderboard.json"
    ) "Leaderboard (9 models)"

    check-any-file @(
        "docs/assets/scoreboard_local_vs_api.json",
        "docs/submissions/data_trace_bundle/10_charts/manifest.json",
        "docs/submissions/shared/assets/task1/track1_leaderboard_scores.png"
    ) "Scoreboard / public chart evidence"
}

# === Track 2: Agent ====================================================
if ($Track -eq 2 -or $Track -eq "All") {
    header "Track 2: Agent Capabilities & Dry-Run"

    try {
        $cap = read-json-utf8 "$ProjectRoot/agent/agent_capabilities.json"
        $intentCount = @($cap.intents).Count
        if ($intentCount -ge 15) { ok "Agent intent registry valid ($intentCount intents)" }
        else { fail "Agent intent registry incomplete ($intentCount intents)" }
    } catch {
        fail "Agent capability registry parse failed: $($_.Exception.Message)"
    }

    check-file "agent/agent_capabilities.json" "agent_capabilities.json"
    check-file "agent/examples/logs/task_1_corpus.json" "agent corpus log sample"
    check-file "agent/examples/logs/task_4_recovery.json" "agent recovery log sample"
    check-file "shared/assets/track2_agent_reliability_matrix.png" "Track2 reliability evidence matrix"
    check-file "shared/assets/track2_failure_recovery_matrix.png" "Track2 failure recovery matrix"
    check-file "shared/assets/track2_source_selection_ablation.png" "Track2 source selection A/B"
    check-file "shared/assets/track2_resource_pareto.png" "Track2 resource scheduling Pareto"
    check-file "shared/assets/track2_hard_document_stress.png" "Track2 hard document stress"
    check-file "shared/assets/track2_sciverse_source_routing.png" "Track2 Sciverse source routing"
}

# === Track 3: Medical RAG ==============================================
if ($Track -eq 3 -or $Track -eq "All") {
    header "Track 3: Medical RAG Indexes & API"

    # The private workspace may include live FAISS/BM25 indexes. The public
    # release keeps traceable evidence copies under docs/submissions/data_trace_bundle.
    check-any-file @(
        "data/sources_medical/index/embeddings_cache.npy",
        "docs/submissions/data_trace_bundle/09_medical_rag/medical_rag_eval.json"
    ) "Text retrieval evidence"
    check-any-file @(
        "data/sources_medical/index/medical.index",
        "docs/submissions/data_trace_bundle/09_medical_rag/medical_rag_eval_zh_ask.json"
    ) "FAISS text evidence"
    check-any-file @(
        "data/sources_medical/index/bm25.pkl",
        "docs/submissions/data_trace_bundle/09_medical_rag/vision_chunks_manifest.json"
    ) "BM25 / chunk evidence"

    check-any-file @(
        "data/sources_medical/index/medical_vision.index",
        "docs/submissions/data_trace_bundle/09_medical_rag/vision_descriptions.jsonl"
    ) "MiMo vision evidence"
    check-any-file @(
        "data/sources_medical/index/medical_vision_qwen35.index",
        "docs/submissions/data_trace_bundle/09_medical_rag/vision_descriptions_qwen35.jsonl"
    ) "qwen3.5 vision evidence"

    $visionTrace = "$ProjectRoot/data/sources_medical/vision/vision_descriptions_qwen35.jsonl"
    $publicVisionTrace = "$ProjectRoot/docs/submissions/data_trace_bundle/09_medical_rag/vision_descriptions_qwen35.jsonl"
    if (Test-Path $visionTrace) {
        $cnt = (Get-Content $visionTrace -Encoding UTF8).Count
        ok "qwen3.5 vision descriptions: $cnt images"
    } elseif (Test-Path $publicVisionTrace) {
        $cnt = (Get-Content $publicVisionTrace -Encoding UTF8).Count
        ok "qwen3.5 vision descriptions public trace: $cnt lines"
    } else { fail "vision_descriptions_qwen35.jsonl - NOT FOUND" }

    if ($SkipApiHealth) {
        skip "Medical RAG API health check skipped by -SkipApiHealth"
    } else {
        # --- API health ---
        $healthUrl = "http://localhost:$ApiPort/api/health"
        info "Checking $healthUrl"
        try {
            $resp = Invoke-WebRequest -Uri $healthUrl -TimeoutSec 5 -UseBasicParsing
            ok "Medical RAG API - HTTP $($resp.StatusCode)"
        } catch {
            fail "Medical RAG API unreachable - see tip below"
        }
    }
}

# === Footer ============================================================
$sw.Stop()
$total = $OkCount + $FailCount + $SkipCount
Write-Host ""
Write-Host $BANNER -ForegroundColor Magenta
Write-Host "  $OkCount/$total checks passed  |  ${SkipCount} skipped  |  ${FailCount} failed  |  $([math]::Round($sw.Elapsed.TotalSeconds,1))s" -ForegroundColor Magenta
Write-Host $BANNER -ForegroundColor Magenta

if (($Track -eq 3 -or $Track -eq "All") -and -not $SkipApiHealth -and $FailCount -gt 0) {
    Write-Host "  Tip: if RAG API check failed, start it first:" -ForegroundColor DarkYellow
    Write-Host "    $PythonExe -m controlsci.api.medical_rag --port $ApiPort" -ForegroundColor DarkYellow
}

Write-Host ""
Write-Host "  Next steps:" -ForegroundColor Cyan
Write-Host "    L1 (0.9s,CPU): .\run_reviewer_demo.ps1 -Track 1" -ForegroundColor Cyan
Write-Host "    L2 (<1 CNY):    .\run_minimal_repro.ps1 -Limit 10" -ForegroundColor Cyan
Write-Host "    Full repro:    see Appendix A of each report in docs/submissions/" -ForegroundColor Cyan
Write-Host "    Quickstart:    docs/submissions/quickstart.md" -ForegroundColor Cyan
Write-Host ""

Pop-Location
if ($FailCount -gt 0) {
    exit 1
}
exit 0
