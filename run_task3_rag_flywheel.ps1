<#
.SYNOPSIS
    Task3 Medical RAG reproducible flywheel.

.DESCRIPTION
    Runs the stable, local-only Medical RAG loop on the curated corpus:
      1. fixed retrieval evaluation across Qwen / BGE Small / BGE M3 indexes
      2. local answer-synthesis smoke test on one evidence query
      3. Chinese Ask reproducibility trace
      4. optional demo/API verification
      5. supplemental deployment smoke matrix and summary refresh

    PMC online download is intentionally out of this main loop because it
    depends on short-lived browser PoW cookies. Keep download experiments in
    _tools/ as corpus expansion utilities, not as a reproducibility prerequisite.

.EXAMPLE
    .\run_task3_rag_flywheel.ps1

.EXAMPLE
    .\run_task3_rag_flywheel.ps1 -DryRun

.EXAMPLE
    .\run_task3_rag_flywheel.ps1 -SkipSynthesis -SkipDemoVerify

.EXAMPLE
    .\run_task3_rag_flywheel.ps1 -SynthesisModel qwen3.5:9b -NoStartServices
#>

param(
    [int]$TopK = 3,
    [string]$SynthesisModel = "qwen3.5:9b",
    [switch]$SkipRetrieval,
    [switch]$SkipSynthesis,
    [switch]$SkipZhAsk,
    [switch]$SkipDemoVerify,
    [switch]$SkipSupplemental,
    [switch]$NoStartServices,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"

$ROOT = (Resolve-Path $PSScriptRoot).Path
$MyEnvPython = if ($env:CONTROLMIND_PYTHON) { $env:CONTROLMIND_PYTHON } elseif ($env:CONTROLSCI_PYTHON) { $env:CONTROLSCI_PYTHON } else { "" }
$EvalScript = Join-Path $ROOT "benchmark\eval\medical_rag_eval.py"
$EvalJson = Join-Path $ROOT "benchmark\eval\results\medical_rag_eval.json"
$SmokeJson = Join-Path $ROOT "benchmark\eval\results\medical_rag_eval_synthesis_smoke.json"
$ZhAskJson = Join-Path $ROOT "benchmark\eval\results\medical_rag_eval_zh_ask.json"
$ZhAskTrace = Join-Path $ROOT "benchmark\eval\results\medical_rag_zh_ask_traces.jsonl"
$SupplementalMatrixJson = Join-Path $ROOT "benchmark\eval\results\track3_deployment_smoke_matrix.json"
$SupplementalSummaryJson = Join-Path $ROOT "benchmark\eval\results\track3_supplemental_summary.json"
$VerifyScript = Join-Path $ROOT "verify_task3_demo.ps1"
$ChunksManifest = Join-Path $ROOT "data\sources_medical\chunks\chunks_manifest.json"
$PublicEvidenceManifest = Join-Path $ROOT "docs\submissions\data_trace_bundle\manifest.json"

function Write-Step {
    param([string]$Message)
    Write-Host ""
    Write-Host ("=" * 72) -ForegroundColor Cyan
    Write-Host "  $Message" -ForegroundColor Cyan
    Write-Host ("=" * 72) -ForegroundColor Cyan
}

function Write-Ok { param([string]$Message) Write-Host "[OK] $Message" -ForegroundColor Green }
function Write-Warn { param([string]$Message) Write-Host "[WARN] $Message" -ForegroundColor Yellow }
function Write-Info { param([string]$Message) Write-Host "[INFO] $Message" -ForegroundColor Gray }

function Invoke-MyEnvPython {
    param([string[]]$ArgsList)
    if ($MyEnvPython -and (Test-Path $MyEnvPython)) {
        & $MyEnvPython @ArgsList
        return
    }
    Write-Warn "CONTROLMIND_PYTHON/CONTROLSCI_PYTHON not set; falling back to conda run -n myenv."
    & conda run --no-capture-output -n myenv python @ArgsList
}

function Assert-File {
    param([string]$Path, [string]$Label)
    if (-not (Test-Path $Path)) {
        throw "$Label missing: $Path"
    }
    Write-Ok "$Label ready: $Path"
}

function Read-Json {
    param([string]$Path)
    return Get-Content $Path -Raw -Encoding UTF8 | ConvertFrom-Json
}

function Read-JsonLines {
    param([string]$Path)
    return Get-Content $Path -Encoding UTF8 | Where-Object { $_.Trim() } | ForEach-Object { $_ | ConvertFrom-Json }
}

Write-Host ""
Write-Host "Task3 Medical RAG Flywheel" -ForegroundColor Cyan
Write-Info "Root: $ROOT"
Write-Info "TopK: $TopK"
Write-Info "Synthesis model: $SynthesisModel"
Write-Info "Main path: existing local corpus -> fixed eval -> local synthesis smoke -> Chinese Ask trace -> demo verification"
Write-Info "PMC download is excluded from this reproducible loop."

if ($DryRun) {
    Write-Step "Dry-run plan"
    Write-Info "Would check RAG eval script: $EvalScript"
    Write-Info "Would check medical chunks manifest: $ChunksManifest"
    Write-Info "Would check BGE M3 FAISS/BM25 indexes under data\\sources_medical\\index_bge_m3"
    if (-not $SkipRetrieval) {
        Write-Info "Would run retrieval eval -> $EvalJson"
    } else {
        Write-Warn "Retrieval eval skipped by -SkipRetrieval."
    }
    if (-not $SkipSynthesis) {
        Write-Info "Would run local synthesis smoke with $SynthesisModel -> $SmokeJson"
    } else {
        Write-Warn "Synthesis smoke skipped by -SkipSynthesis."
    }
    if (-not $SkipZhAsk) {
        Write-Info "Would run Chinese Ask bridge and trace eval -> $ZhAskJson / $ZhAskTrace"
    } else {
        Write-Warn "Chinese Ask eval skipped by -SkipZhAsk."
    }
    if (-not $SkipDemoVerify) {
        Write-Info "Would run demo/API verifier: $VerifyScript"
    } else {
        Write-Warn "Demo verification skipped by -SkipDemoVerify."
    }
    if (-not $SkipSupplemental) {
        Write-Info "Would refresh supplemental deployment smoke matrix -> $SupplementalMatrixJson / $SupplementalSummaryJson"
    } else {
        Write-Warn "Supplemental refresh skipped by -SkipSupplemental."
    }
    Write-Ok "Dry-run finished without touching evaluation artifacts."
    exit 0
}

Assert-File -Path $EvalScript -Label "RAG eval script"
if (-not ($SkipRetrieval -and $SkipSynthesis -and $SkipZhAsk)) {
    Assert-File -Path $ChunksManifest -Label "Medical chunks manifest"
} else {
    Write-Warn "Skipping retrieval/synthesis/ZhAsk; Medical chunks manifest check skipped."
}
if (-not ($SkipRetrieval -and $SkipSynthesis -and $SkipZhAsk)) {
    Assert-File -Path (Join-Path $ROOT "data\sources_medical\index_bge_m3\medical.index") -Label "BGE M3 FAISS index"
    Assert-File -Path (Join-Path $ROOT "data\sources_medical\index_bge_m3\bm25.pkl") -Label "BGE M3 BM25 index"
} elseif (Test-Path $PublicEvidenceManifest) {
    Write-Warn "Skipping live RAG steps; using public evidence bundle as the traceability boundary."
} else {
    Write-Warn "Skipping live RAG steps; no public evidence manifest found."
}

if (-not $SkipRetrieval) {
    Write-Step "Step 1/5: fixed multi-index retrieval evaluation"
    Invoke-MyEnvPython -ArgsList @(
        $EvalScript,
        "--k", "$TopK",
        "--indexes", "qwen", "bge_small", "bge_m3",
        "--output", $EvalJson
    )
    Assert-File -Path $EvalJson -Label "Retrieval eval JSON"

    $eval = Read-Json -Path $EvalJson
    $bgeM3 = $eval.summary.index_bge_m3
    if ($bgeM3.hit_at_k -ne 8 -or $bgeM3.label_hit_at_k -ne 8) {
        throw "BGE M3 expected Hit@$TopK=8/8 and Label Hit@$TopK=8/8, got $($bgeM3.hit_at_k)/$($bgeM3.label_hit_at_k)"
    }
    Write-Ok "BGE M3 retrieval remains closed-loop: Hit@$TopK=8/8, Label Hit@$TopK=8/8"
} else {
    Write-Warn "Skipping retrieval eval."
}

if (-not $SkipSynthesis) {
    Write-Step "Step 2/5: local evidence-bounded synthesis smoke"
    Invoke-MyEnvPython -ArgsList @(
        $EvalScript,
        "--k", "$TopK",
        "--indexes", "bge_small",
        "--with-synthesis",
        "--synthesis-model", $SynthesisModel,
        "--limit-cases", "1",
        "--output", $SmokeJson
    )
    Assert-File -Path $SmokeJson -Label "Synthesis smoke JSON"

    $smoke = Read-Json -Path $SmokeJson
    $case = $smoke.results.index_bge_small.primary_endpoint_safety
    if ($case.synthesis.supported_claims -ne $case.synthesis.claim_count) {
        throw "Synthesis smoke has unsupported claims: $($case.synthesis.supported_claims)/$($case.synthesis.claim_count)"
    }
    if ([double]$case.synthesis.citation_coverage -lt 1.0) {
        throw "Synthesis smoke citation coverage below 1.0"
    }
    Write-Ok "Synthesis smoke remains evidence-bounded: $($case.synthesis.supported_claims)/$($case.synthesis.claim_count) claims, citation coverage $($case.synthesis.citation_coverage)"
} else {
    Write-Warn "Skipping synthesis smoke."
}

if (-not $SkipZhAsk) {
    Write-Step "Step 3/5: Chinese Ask bridge and trace evaluation"
    Invoke-MyEnvPython -ArgsList @(
        $EvalScript,
        "--k", "$TopK",
        "--indexes", "bge_m3",
        "--case-set", "zh_ask",
        "--with-synthesis",
        "--synthesis-model", $SynthesisModel,
        "--output", $ZhAskJson,
        "--trace-jsonl", $ZhAskTrace
    )
    Assert-File -Path $ZhAskJson -Label "Chinese Ask eval JSON"
    Assert-File -Path $ZhAskTrace -Label "Chinese Ask trace JSONL"

    $zhAsk = Read-Json -Path $ZhAskJson
    $zhSummary = $zhAsk.summary.index_bge_m3
    if ($zhSummary.hit_at_k -ne 6 -or $zhSummary.label_hit_at_k -ne 6) {
        throw "Chinese Ask expected Hit@$TopK=6/6 and Label Hit@$TopK=6/6, got $($zhSummary.hit_at_k)/$($zhSummary.label_hit_at_k)"
    }
    if ($zhSummary.bridged_cases -ne 6) {
        throw "Chinese Ask expected 6 bridged cases, got $($zhSummary.bridged_cases)"
    }
    $zhTraces = @(Read-JsonLines -Path $ZhAskTrace)
    $claimCount = 0
    $supportedClaims = 0
    $coverageTotal = 0.0
    foreach ($trace in $zhTraces) {
        $claimCount += [int]$trace.synthesis.claim_count
        $supportedClaims += [int]$trace.synthesis.supported_claims
        $coverageTotal += [double]$trace.synthesis.citation_coverage
    }
    if ($claimCount -le 0 -or $supportedClaims -ne $claimCount) {
        throw "Chinese Ask traces have unsupported claims: $supportedClaims/$claimCount"
    }
    $meanCoverage = [math]::Round($coverageTotal / [math]::Max(1, $zhTraces.Count), 3)
    Write-Ok "Chinese Ask bridge remains closed-loop: Hit@$TopK=6/6, Label Hit@$TopK=6/6, bridged=6/6, multi-query=$($zhSummary.multi_query_cases)/6"
    Write-Ok "Chinese Ask synthesis remains evidence-bounded: $supportedClaims/$claimCount claims, mean citation coverage $meanCoverage"
} else {
    Write-Warn "Skipping Chinese Ask trace eval."
}

if (-not $SkipDemoVerify) {
    Write-Step "Step 4/5: demo/API verification"
    Assert-File -Path $VerifyScript -Label "Task3 demo verifier"
    $verifyArgs = @()
    if ($NoStartServices) {
        $verifyArgs += "-NoStart"
    }
    & $VerifyScript @verifyArgs
    Write-Ok "Demo verification completed."
} else {
    Write-Warn "Skipping demo verification."
}

if (-not $SkipSupplemental) {
    Write-Step "Step 5/5: supplemental deployment smoke matrix refresh"
    Invoke-MyEnvPython -ArgsList @(
        "-m", "benchmark.eval.track3_deployment_smoke_matrix",
        "--output", $SupplementalMatrixJson,
        "--summary-output", $SupplementalSummaryJson
    )
    Assert-File -Path $SupplementalMatrixJson -Label "Track3 supplemental deployment smoke matrix"
    Assert-File -Path $SupplementalSummaryJson -Label "Track3 supplemental summary"
    Write-Ok "Supplemental deployment smoke matrix refreshed."
} else {
    Write-Warn "Skipping supplemental refresh."
}

Write-Step "Summary"
Write-Ok "Task3 RAG flywheel finished."
Write-Info "Retrieval artifact: benchmark\eval\results\medical_rag_eval.json"
Write-Info "Synthesis artifact: benchmark\eval\results\medical_rag_eval_synthesis_smoke.json"
Write-Info "Chinese Ask artifact: benchmark\eval\results\medical_rag_eval_zh_ask.json"
Write-Info "Chinese Ask trace: benchmark\eval\results\medical_rag_zh_ask_traces.jsonl"
Write-Info "Supplemental deployment matrix: benchmark\eval\results\track3_deployment_smoke_matrix.json"
Write-Info "Supplemental summary: benchmark\eval\results\track3_supplemental_summary.json"
Write-Info "Traceability docs: docs\submissions\shared\DATA-TRACE.md and docs\submissions\track3_medical_rag_report.md"
