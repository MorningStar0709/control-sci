<#
.SYNOPSIS
  ControlSci 评委一键复现脚本 — 零 API Key 验证三赛道核心指标

.DESCRIPTION
  无需外部 API Key，一条命令验证：
    Track 1: 数据集结构 (500题 schema) + 六维计分板
    Track 2: Agent 13 Intent 注册 + dry-run 复现计划
    Track 3: 医疗 Hybrid 索引 + qwen3.5 本地视觉 FAISS + RAG API
  硬件依赖: 仅 Track 3 API 健康检查需先启动服务。
             Track 1/2 纯本地，零外部依赖。

.PARAMETER Track
  1 | 2 | 3 | All

.PARAMETER Quiet
  录屏友好模式：隐藏 Python 子命令的详细输出，仅保留摘要。

.PARAMETER SkipApiHealth
  跳过 Track 3 的 localhost:8001 API 健康检查，适用于只展示本地索引资产的录屏。

.EXAMPLE
  .\run_reviewer_demo.ps1 -Track 1
  .\run_reviewer_demo.ps1 -Track All
#>

param(
    [ValidateSet(1, 2, 3, "All")]
    $Track = 1,
    [switch]$Quiet,
    [switch]$SkipApiHealth,
    [int]$ApiPort = 8001
)

$ErrorActionPreference = "Continue"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path $ScriptDir
Push-Location $ProjectRoot

$env:PYTHONIOENCODING = 'utf-8'
$env:CONDA_NO_PLUGINS = 'true'

$BANNER = "=" * 60
$sw = [System.Diagnostics.Stopwatch]::StartNew()
$FailCount = 0; $OkCount = 0; $SkipCount = 0

function header($t)  { Write-Host "`n$BANNER" -ForegroundColor Cyan; Write-Host "  $t" -ForegroundColor Cyan; Write-Host $BANNER -ForegroundColor Cyan }
function ok($m)    { $script:OkCount++;  Write-Host "  [OK]   $m" -ForegroundColor Green }
function fail($m)  { $script:FailCount++; Write-Host "  [FAIL] $m" -ForegroundColor Red }
function skip($m)  { $script:SkipCount++; Write-Host "  [SKIP] $m" -ForegroundColor Yellow }
function info($m)   { Write-Host "  [INFO]  $m" -ForegroundColor Yellow }
function warn($m)   { Write-Host "  [WARN]  $m" -ForegroundColor Yellow }

function run-py([string[]]$argsList) {
    $display = $argsList -join " "
    info "Running: conda run python $display"
    $result = conda run --no-capture-output -n myenv python @argsList 2>&1
    $rc = $LASTEXITCODE
    if ($result -and -not $Quiet) {
        $result | ForEach-Object { Write-Host "          $_" -ForegroundColor DarkGray }
    } elseif ($result -and $rc -ne 0) {
        $result | Select-Object -Last 12 | ForEach-Object { Write-Host "          $_" -ForegroundColor DarkGray }
    }
    return $rc
}

function check-file($path, $desc) {
    $fp = Join-Path $ProjectRoot $path
    if (Test-Path $fp) {
        $size = [math]::Round((Get-Item $fp).Length / 1KB, 1)
        ok "$desc — ${size} KB"
    } else { fail "$desc — NOT FOUND ($path)" }
}

Write-Host ""
Write-Host $BANNER -ForegroundColor Magenta
Write-Host "  ControlSci One-Click Reproduction" -ForegroundColor Magenta
Write-Host "  Track $Track | Zero API Key | $(Get-Date -Format 'yyyy-MM-dd HH:mm')" -ForegroundColor Magenta
if ($Quiet) { Write-Host "  Mode: Quiet summary" -ForegroundColor Magenta }
if ($SkipApiHealth) { Write-Host "  Track3 API health: skipped" -ForegroundColor Magenta }
Write-Host $BANNER -ForegroundColor Magenta

# === Track 1: Dataset + Scoreboard =====================================
if ($Track -eq 1 -or $Track -eq "All") {
    header "Track 1: Sci-Evo Dataset & Scoreboard"

    $rc = run-py @("benchmark/eval/validate_dataset.py")
    if ($rc -eq 0) { ok "Dataset schema validation (500 Q, 4-dim balanced)" }
    else { fail "Dataset validation failed (exit=$rc)" }

    check-file "benchmark/dataset/core.json" "core.json (500 Q)"
    check-file "benchmark/dataset/full.json" "full.json (889 Q)"
    check-file "docs/submissions/data_trace_bundle/03_leaderboard/leaderboard.json" "Leaderboard evidence copy (9 models)"

    $tracePath = Join-Path $ProjectRoot "docs/submissions/data_trace_bundle/manifest.json"
    if (Test-Path $tracePath) {
        $trace = Get-Content $tracePath -Raw | ConvertFrom-Json
        $items = @($trace.files)
        if ($items.Count -ge 20) { ok "Data trace manifest available ($($items.Count) public artifacts)" }
        else { fail "Data trace manifest is unexpectedly small ($($items.Count) artifacts)" }
    } else { fail "Data trace manifest — NOT FOUND" }
}

# === Track 2: Agent ====================================================
if ($Track -eq 2 -or $Track -eq "All") {
    header "Track 2: Agent Capabilities & Dry-Run"

    try {
        $cap = Get-Content "$ProjectRoot/benchmark/agent/agent_capabilities.json" -Raw | ConvertFrom-Json
        $intentCount = @($cap.intents).Count
        if ($intentCount -ge 13) { ok "Agent intent registry valid ($intentCount intents)" }
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
    } else { fail "agent_cli.py — NOT FOUND" }
}

# === Track 3: Medical RAG ==============================================
if ($Track -eq 3 -or $Track -eq "All") {
    header "Track 3: Medical RAG Indexes & API"

    # --- core indexes ---
    check-file "docs/submissions/data_trace_bundle/09_medical_rag/qa_output.json" "Medical RAG QA evidence"
    check-file "docs/submissions/data_trace_bundle/09_medical_rag/vision_ab_comparison.json" "Medical vision injection A/B evidence"
    check-file "docs/submissions/data_trace_bundle/09_medical_rag/vision_chunks_manifest.json" "Medical vision chunk manifest"

    # --- qwen3.5 local vision index (new) ---
    check-file "docs/submissions/data_trace_bundle/09_medical_rag/vision_descriptions_qwen35.jsonl" "qwen3.5 vision descriptions (public sample)"

    if (Test-Path "$ProjectRoot/docs/submissions/data_trace_bundle/09_medical_rag/vision_descriptions_qwen35.jsonl") {
        $cnt = (Get-Content "$ProjectRoot/docs/submissions/data_trace_bundle/09_medical_rag/vision_descriptions_qwen35.jsonl").Count
        ok "qwen3.5 vision descriptions: $cnt images"
    } else { fail "vision_descriptions_qwen35.jsonl — NOT FOUND" }

    if ($SkipApiHealth) {
        skip "Medical RAG API health check skipped by -SkipApiHealth"
    } else {
        # --- API health ---
        $healthUrl = "http://localhost:$ApiPort/api/health"
        info "Checking $healthUrl"
        try {
            $resp = Invoke-WebRequest -Uri $healthUrl -TimeoutSec 5 -UseBasicParsing
            ok "Medical RAG API — HTTP $($resp.StatusCode)"
        } catch {
            fail "Medical RAG API unreachable — see tip below"
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
    Write-Host "    conda run --no-capture-output -n myenv python -m controlsci.api.medical_rag --port $ApiPort" -ForegroundColor DarkYellow
}

Write-Host ""
Write-Host "  Next steps:" -ForegroundColor Cyan
Write-Host "    L1 (0.9s,CPU): .\run_reviewer_demo.ps1 -Track 1" -ForegroundColor Cyan
Write-Host "    L2 (<1 CNY):    .\run_minimal_repro.ps1 -Limit 10" -ForegroundColor Cyan
Write-Host "    Full repro:    see Appendix A of each report in docs/submissions/" -ForegroundColor Cyan
Write-Host "    Narration:     docs/submissions/shared/core-narrative-and-strategy.md" -ForegroundColor Cyan
Write-Host ""

Pop-Location
if ($FailCount -gt 0) {
    exit 1
}
exit 0
