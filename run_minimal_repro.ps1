<#
.SYNOPSIS
    ControlSci minimal real-chain reproduction.

.DESCRIPTION
    Runs the review-friendly L2 path:
      - balanced 10-question API/Judge evaluation
      - leaderboard generation in an isolated results dir
      - Agent dry-run
      - Medical RAG offline retrieval dry-run
      - Medical RAG FastAPI health/search
      - one-click demo with API health
#>

param(
    [int]$Limit = 10,
    [string]$ResultsDir = "",
    [int]$ApiPort = 18001,
    [switch]$SkipApiSearch
)

$ErrorActionPreference = "Stop"
$ROOT = $PSScriptRoot
if (-not $ResultsDir) {
    $ResultsDir = Join-Path $ROOT "benchmark\eval\results\minimal_repro"
}

function Step($msg) {
    Write-Host ""
    Write-Host ("=" * 70) -ForegroundColor Cyan
    Write-Host "  $msg" -ForegroundColor Cyan
    Write-Host ("=" * 70) -ForegroundColor Cyan
}

function Run($desc, [scriptblock]$body) {
    Step $desc
    & $body
    if ($LASTEXITCODE -ne 0) {
        throw "Failed: $desc (exit=$LASTEXITCODE)"
    }
}

Push-Location $ROOT
try {
    New-Item -ItemType Directory -Path $ResultsDir -Force | Out-Null

    Run "Balanced mini evaluation + leaderboard" {
        .\run_evaluation.ps1 -Execute -Limit $Limit -BalancedMini -ResultsDir $ResultsDir
    }

    Run "Agent dry-run: reproduce_all" {
        python benchmark\agent\agent_cli.py --dry-run --intents reproduce_all
    }

    Run "Agent capability deep validation" {
        python benchmark\agent\_validate_capabilities.py
    }

    Run "Medical RAG offline retrieval dry-run" {
        conda run --no-capture-output -n myenv python -m controlsci.medical.kb_quality --dry-run
    }

    if (-not $SkipApiSearch) {
        Step "Medical RAG FastAPI health/search + one-click demo"
        $out = Join-Path $env:TEMP "controlsci_medical_api.out.log"
        $err = Join-Path $env:TEMP "controlsci_medical_api.err.log"
        Remove-Item $out,$err -ErrorAction SilentlyContinue
        $healthUrl = "http://127.0.0.1:$ApiPort/api/health"
        $searchUrl = "http://127.0.0.1:$ApiPort/api/evidence/search?q=primary%20endpoint&k=3"
        $p = Start-Process -FilePath "conda" `
            -ArgumentList @("run","--no-capture-output","-n","myenv","python","-m","controlsci.api.medical_rag","--host","127.0.0.1","--port",$ApiPort) `
            -WorkingDirectory $ROOT -WindowStyle Hidden `
            -RedirectStandardOutput $out -RedirectStandardError $err -PassThru
        try {
            $ready = $false
            $health = $null
            for ($i = 0; $i -lt 30; $i++) {
                Start-Sleep -Seconds 1
                $raw = curl.exe -s --max-time 5 $healthUrl
                if ($LASTEXITCODE -eq 0 -and $raw) {
                    try {
                        $health = $raw | ConvertFrom-Json
                        if ($health.profile -eq "local_private") {
                            $ready = $true
                            break
                        }
                    } catch {}
                }
            }
            if (-not $ready) {
                Get-Content $out -ErrorAction SilentlyContinue
                Get-Content $err -ErrorAction SilentlyContinue
                throw "Medical RAG API did not become ready with profile=local_private on port $ApiPort"
            }

            $searchRaw = curl.exe -s --max-time 120 $searchUrl
            if ($LASTEXITCODE -ne 0) { throw "Medical RAG API search failed" }
            $search = $searchRaw | ConvertFrom-Json
            if ([int]$search.count -lt 1) { throw "Medical RAG API search returned no results" }

            .\run_reviewer_demo.ps1 -Track All -Quiet -ApiPort $ApiPort
            if ($LASTEXITCODE -ne 0) { throw "one-click demo failed" }
        } finally {
            Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
        }
    }

    Step "Minimal repro complete"
    Write-Host "  ResultsDir: $ResultsDir" -ForegroundColor Green
    exit 0
} finally {
    Pop-Location
}
