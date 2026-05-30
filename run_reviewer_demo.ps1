<#
.SYNOPSIS
  ControlSci 评委一键复现脚本 - 零 API Key 验证三赛道核心指标

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
  .\run_reviewer_demo.ps1 -Track All -SkipApiHealth
#>

param(
    [ValidateSet(1, 2, 3, "All")]
    $Track = 1,
    [switch]$Quiet,
    [switch]$SkipApiHealth,
    [int]$ApiPort = 17001
)

$ErrorActionPreference = "Continue"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path $ScriptDir
Push-Location $ProjectRoot

$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONUTF8 = '1'
$env:CONDA_NO_PLUGINS = 'true'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$BANNER = "=" * 60
$sw = [System.Diagnostics.Stopwatch]::StartNew()
$FailCount = 0; $OkCount = 0; $SkipCount = 0

$PythonCandidates = @(
    $env:CONTROLSCI_PYTHON,
    (Join-Path $ProjectRoot ".venv\Scripts\python.exe")
) | Where-Object { $_ -and $_.Trim() }
$PythonExe = "conda run --no-capture-output -n myenv python"
foreach ($candidate in $PythonCandidates) {
    if (Test-Path $candidate) {
        $PythonExe = $candidate
        break
    }
}

function header($t)  { Write-Host "`n$BANNER" -ForegroundColor Cyan; Write-Host "  $t" -ForegroundColor Cyan; Write-Host $BANNER -ForegroundColor Cyan }
function ok($m)    { $script:OkCount++;  Write-Host "  [OK]   $m" -ForegroundColor Green }
function fail($m)  { $script:FailCount++; Write-Host "  [FAIL] $m" -ForegroundColor Red }
function skip($m)  { $script:SkipCount++; Write-Host "  [SKIP] $m" -ForegroundColor Yellow }
function info($m)   { Write-Host "  [INFO]  $m" -ForegroundColor Yellow }
function warn($m)   { Write-Host "  [WARN]  $m" -ForegroundColor Yellow }

function run-py([string[]]$argsList) {
    $display = $argsList -join " "
    info "Running: $PythonExe $display"
    if ($PythonExe -eq "conda run --no-capture-output -n myenv python") {
        $result = & conda run --no-capture-output -n myenv python @argsList 2>&1
    } else {
        $result = & $PythonExe @argsList 2>&1
    }
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

function check-track3-supplemental-consistency($matrixPath, $summaryPath, $desc) {
    $matrixFile = Join-Path $ProjectRoot $matrixPath
    $summaryFile = Join-Path $ProjectRoot $summaryPath
    if (-not (Test-Path $matrixFile)) {
        fail "$desc - deployment matrix NOT FOUND ($matrixPath)"
        return
    }
    if (-not (Test-Path $summaryFile)) {
        fail "$desc - summary NOT FOUND ($summaryPath)"
        return
    }
    try {
        $matrix = read-json-utf8 $matrixFile
        $summary = read-json-utf8 $summaryFile
        $executed = @($matrix.executed_smoke_checks)
        $notRun = @($matrix.not_run_checks)
        $supplementalPassed = @($executed | Where-Object { $_.name -eq "track3_supplemental_status_cli" -and $_.status -eq "passed" }).Count -gt 0
        $unexpectedNotRun = @($notRun | Where-Object { $_.status -ne "not_run_environment_dependency" }).Count
        if ($summary.status -notin @("available", "ok")) {
            fail "$desc - summary status unexpected: $($summary.status)"
        } elseif (-not $supplementalPassed) {
            fail "$desc - supplemental status CLI smoke missing or not passed"
        } elseif ($unexpectedNotRun -gt 0) {
            fail "$desc - environment-dependent checks have unexpected status"
        } elseif ([int]$summary.deployment_smoke_matrix.executed_smoke_checks -ne $executed.Count) {
            fail "$desc - executed smoke count mismatch"
        } elseif ([int]$summary.deployment_smoke_matrix.not_run_checks -ne $notRun.Count) {
            fail "$desc - not-run smoke count mismatch"
        } else {
            ok "$desc - deployment matrix and summary consistent"
        }
    } catch {
        fail "$desc - consistency check failed: $($_.Exception.Message)"
    }
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
    header "Track 1: Sci-Evo Dataset & Scoreboard"

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
    check-file "docs/submissions/shared/assets/task1/track1_sciverse_validation_dashboard.png" "Track1 Sciverse validation dashboard"
    check-file "docs/submissions/shared/assets/task1/track1_supplemental_evidence_matrix.png" "Track1 supplemental evidence matrix"
    check-file "docs/submissions/shared/assets/task1/track1_training_utility_ablation.png" "Track1 training utility ablation"
}

# === Track 2: Agent ====================================================
if ($Track -eq 2 -or $Track -eq "All") {
    header "Track 2: Agent Capabilities & Dry-Run"

    try {
        $cap = read-json-utf8 "$ProjectRoot/benchmark/agent/agent_capabilities.json"
        $intentCount = @($cap.intents).Count
        if ($intentCount -ge 15) { ok "Agent intent registry valid ($intentCount intents)" }
        else { fail "Agent intent registry incomplete ($intentCount intents)" }
    } catch {
        fail "Agent capability registry parse failed: $($_.Exception.Message)"
    }

    $rc = run-py @("benchmark/agent/agent_cli.py", "--dry-run", "--intents", "reproduce_all")
    if ($rc -eq 0) { ok "Agent dry-run: reproduce_all plan generated" }
    else { fail "Agent dry-run failed (exit=$rc)" }

    check-file "benchmark/agent/agent_capabilities.json" "agent_capabilities.json"
    if (Test-Path "$ProjectRoot/benchmark/agent/agent_cli.py") {
        ok "agent_cli.py ($([math]::Round((Get-Item "$ProjectRoot/benchmark/agent/agent_cli.py").Length/1KB,1)) KB)"
    } else { fail "agent_cli.py - NOT FOUND" }
    check-file "docs/submissions/shared/assets/task2/track2_agent_reliability_matrix.png" "Track2 reliability evidence matrix"
    check-file "docs/submissions/shared/assets/task2/track2_failure_recovery_matrix.png" "Track2 failure recovery matrix"
    check-file "docs/submissions/shared/assets/task2/track2_source_selection_ablation.png" "Track2 source selection A/B"
    check-file "docs/submissions/shared/assets/task2/track2_resource_pareto.png" "Track2 resource scheduling Pareto"
    check-file "docs/submissions/shared/assets/task2/track2_hard_document_stress.png" "Track2 hard document stress"
    check-file "docs/submissions/shared/assets/task2/track2_sciverse_source_routing.png" "Track2 Sciverse source routing"
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
    check-file "benchmark/eval/results/track3_supplemental_summary.json" "Track3 supplemental summary"
    check-file "benchmark/eval/results/track3_deployment_smoke_matrix.json" "Track3 deployment smoke matrix"
    check-file "docs/submissions/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental/track3_supplemental_summary.json" "Track3 supplemental bundle summary"
    check-file "docs/submissions/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental/track3_deployment_smoke_matrix.json" "Track3 supplemental bundle deployment matrix"
    check-file "_final_submission_by_track/track3_medical_rag/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental/track3_supplemental_summary.json" "Track3 final supplemental bundle summary"
    check-file "_final_submission_by_track/track3_medical_rag/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental/track3_deployment_smoke_matrix.json" "Track3 final supplemental bundle deployment matrix"
    check-track3-supplemental-consistency "benchmark/eval/results/track3_deployment_smoke_matrix.json" "benchmark/eval/results/track3_supplemental_summary.json" "Track3 local supplemental consistency"
    check-track3-supplemental-consistency "docs/submissions/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental/track3_deployment_smoke_matrix.json" "docs/submissions/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental/track3_supplemental_summary.json" "Track3 public supplemental consistency"
    check-track3-supplemental-consistency "_final_submission_by_track/track3_medical_rag/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental/track3_deployment_smoke_matrix.json" "_final_submission_by_track/track3_medical_rag/data_trace_bundle/12_final_supplemental_experiments/track3_medical_rag_supplemental/track3_supplemental_summary.json" "Track3 final supplemental consistency"
    check-file "docs/submissions/shared/assets/task3/track3_sciverse_rrf_matrix.png" "Track3 Sciverse RRF matrix"
    check-file "docs/submissions/shared/assets/task3/track3_medbench_sciverse_compare.png" "Track3 MedBench Sciverse compare"
    check-file "docs/submissions/shared/assets/task3/track3_sciverse_expansion_funnel.png" "Track3 Sciverse expansion funnel"
    check-file "docs/submissions/shared/assets/task3/track3_vision_provider_boundary.png" "Track3 vision provider boundary"
    check-file "docs/submissions/shared/assets/task3/track3_medbench_vlm_model_delta.png" "Track3 MedBench VLM model delta"
    check-file "docs/submissions/shared/assets/task3/track3_supplemental_evidence_matrix.png" "Track3 supplemental evidence matrix"

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
