<#
.SYNOPSIS
    Verify the local Task3 Medical RAG demo path.

.DESCRIPTION
    Checks the backend, frontend, saved RAG evaluation artifacts, and the
    Track3 page. If services are not already listening, the script starts them
    through run_frontend.ps1 using the required myenv-backed FastAPI startup.

.EXAMPLE
    .\verify_task3_demo.ps1

.EXAMPLE
    .\verify_task3_demo.ps1 -NoStart
#>

param(
    [int]$FrontendPort = 3000,
    [int]$BackendPort = 17001,
    [switch]$NoStart
)

$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$ROOT = (Resolve-Path $PSScriptRoot).Path
$FRONTEND_URL = "http://localhost:$FrontendPort"
$BACKEND_URL = "http://localhost:$BackendPort"
$EVAL_JSON = Join-Path $ROOT "benchmark\eval\results\medical_rag_eval.json"
$SMOKE_JSON = Join-Path $ROOT "benchmark\eval\results\medical_rag_eval_synthesis_smoke.json"

function Write-Ok { param([string]$Msg) Write-Host "[OK] $Msg" -ForegroundColor Green }
function Write-Warn { param([string]$Msg) Write-Host "[WARN] $Msg" -ForegroundColor Yellow }
function Write-Info { param([string]$Msg) Write-Host "[INFO] $Msg" -ForegroundColor Gray }
function Write-Err { param([string]$Msg) Write-Host "[ERROR] $Msg" -ForegroundColor Red }

function Get-PortProcessIds {
    param([int]$TargetPort)
    $connections = Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue
    if (-not $connections) { return @() }
    return @($connections | Select-Object -ExpandProperty OwningProcess -Unique)
}

function Test-PortListening {
    param([int]$TargetPort)
    return (Get-PortProcessIds -TargetPort $TargetPort).Count -gt 0
}

function Invoke-Check {
    param(
        [string]$Name,
        [scriptblock]$Body
    )
    try {
        & $Body
        Write-Ok $Name
        return $true
    }
    catch {
        Write-Err "$Name failed: $($_.Exception.Message)"
        return $false
    }
}

function Start-Task3ServicesIfNeeded {
    $frontendUp = Test-PortListening -TargetPort $FrontendPort
    $backendUp = Test-PortListening -TargetPort $BackendPort
    if ($frontendUp -and $backendUp) {
        Write-Ok "Services already listening: frontend $FrontendPort, backend $BackendPort"
        return
    }

    if ($NoStart) {
        Write-Warn "Services are not fully up and -NoStart was set."
        return
    }

    Write-Info "Starting Task3 services through run_frontend.ps1..."
    & (Join-Path $ROOT "run_frontend.ps1") -Port $FrontendPort -BackendPort $BackendPort -StartBackend -Background
    Start-Sleep -Seconds 5
}

Start-Task3ServicesIfNeeded

$checks = New-Object System.Collections.Generic.List[bool]

$checks.Add((Invoke-Check "Backend health returns ok/degraded with retrieval indexes" {
    $health = Invoke-RestMethod -Uri "$BACKEND_URL/api/health" -TimeoutSec 20
    if ($health.status -notin @("ok", "degraded")) {
        throw "unexpected health status: $($health.status)"
    }
    $availableIndexes = @($health.components.retrieval_indexes | Where-Object { $_.available })
    if ($availableIndexes.Count -lt 3) {
        throw "expected 3 available retrieval indexes, got $($availableIndexes.Count)"
    }
}))

$checks.Add((Invoke-Check "Medical RAG eval artifact exists and BGE M3 is 8/8" {
    if (-not (Test-Path $EVAL_JSON)) {
        throw "missing $EVAL_JSON"
    }
    $eval = Get-Content $EVAL_JSON -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($eval.cases.Count -ne 8 -or $eval.k -ne 3) {
        throw "expected 8 cases and top-k=3"
    }
    $bgeM3 = $eval.summary.index_bge_m3
    if ($bgeM3.hit_at_k -ne 8 -or $bgeM3.label_hit_at_k -ne 8) {
        throw "expected BGE M3 hit_at_k=8 and label_hit_at_k=8"
    }
}))

$checks.Add((Invoke-Check "Synthesis smoke artifact has full citation coverage" {
    if (-not (Test-Path $SMOKE_JSON)) {
        throw "missing $SMOKE_JSON"
    }
    $smoke = Get-Content $SMOKE_JSON -Raw -Encoding UTF8 | ConvertFrom-Json
    $case = $smoke.results.index_bge_small.primary_endpoint_safety
    if ($case.synthesis.supported_claims -ne $case.synthesis.claim_count) {
        throw "supported claims do not match claim count"
    }
    if ([double]$case.synthesis.citation_coverage -lt 1.0) {
        throw "citation coverage below 1.0"
    }
}))

$checks.Add((Invoke-Check "Eval summary API exposes best index and smoke coverage" {
    $summary = Invoke-RestMethod -Uri "$BACKEND_URL/api/demo/medical-rag/eval-summary" -TimeoutSec 20
    if (-not $summary.available) {
        throw "summary API reports unavailable"
    }
    if ($summary.eval.best_label -ne "index_bge_m3") {
        throw "expected best index index_bge_m3, got $($summary.eval.best_label)"
    }
    if ([double]$summary.smoke_case.citation_coverage -lt 1.0) {
        throw "summary smoke coverage below 1.0"
    }
}))

$checks.Add((Invoke-Check "Frontend Track3 page is reachable" {
    $response = Invoke-WebRequest -Uri "$FRONTEND_URL/track3" -UseBasicParsing -TimeoutSec 20
    if ($response.StatusCode -ne 200) {
        throw "unexpected status code $($response.StatusCode)"
    }
}))

$passed = ($checks | Where-Object { $_ }).Count
$total = $checks.Count
if ($passed -ne $total) {
    Write-Err "Task3 verification failed: $passed/$total checks passed."
    exit 1
}

Write-Ok "Task3 verification passed: $passed/$total checks passed."
Write-Info "Frontend: $FRONTEND_URL/track3"
Write-Info "Backend:  $BACKEND_URL/api/demo/medical-rag/eval-summary"
