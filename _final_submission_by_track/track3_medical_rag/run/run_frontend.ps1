<#
.SYNOPSIS
    Start the ControlMind / ControlSci frontend workbench.

.DESCRIPTION
    Starts the Next.js frontend under starboard. By default, the server runs
    in the current terminal so startup errors are visible. Use -Background for
    demo recording or long-lived local use.
    In the standalone final bundle, use -EvidenceOnly to validate submitted
    evidence JSON without requiring frontend/backend source files.

.PARAMETER Port
    Frontend port. Defaults to 3000.

.PARAMETER Background
    Start Next.js in a hidden background process and write logs to
    starboard\next-server.log.

.PARAMETER OpenBrowser
    Open the frontend URL in the default browser after startup.

.PARAMETER StartBackend
    Start the FastAPI backend first using the myenv Python interpreter.

.PARAMETER BackendPort
    FastAPI backend port. Defaults to 17001.

.PARAMETER Install
    Run pnpm install before starting if node_modules is missing.

.PARAMETER Force
    Stop existing node/next processes listening on the selected port.

.PARAMETER Help
    Show detailed help.

.EXAMPLE
    .\run_frontend.ps1

.EXAMPLE
    .\run_frontend.ps1 -Background -OpenBrowser

.EXAMPLE
    .\run_frontend.ps1 -Port 3001 -Install

.EXAMPLE
    .\run_frontend.ps1 -StartBackend -Background -OpenBrowser
#>

param(
    [int]$Port = 3000,
    [int]$BackendPort = 17001,
    [switch]$Background,
    [switch]$OpenBrowser,
    [switch]$StartBackend,
    [switch]$Install,
    [switch]$Force,
    [switch]$EvidenceOnly,
    [switch]$Help
)

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

if ($Help) {
    Get-Help -Detailed $PSCommandPath
    exit 0
}

$ErrorActionPreference = "Stop"
$BUNDLE_ROOT = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ROOT = $BUNDLE_ROOT
$FRONTEND_DIR = Join-Path $ROOT "starboard"
$LOG_PATH = Join-Path $FRONTEND_DIR "next-server.log"
$ERR_LOG_PATH = Join-Path $FRONTEND_DIR "next-server.err.log"
$BACKEND_LOG_PATH = Join-Path $ROOT "api-server.log"
$BACKEND_ERR_LOG_PATH = Join-Path $ROOT "api-server.err.log"
$MYENV_PYTHON = if ($env:CONTROLMIND_PYTHON) { $env:CONTROLMIND_PYTHON } elseif ($env:CONTROLSCI_PYTHON) { $env:CONTROLSCI_PYTHON } else { "" }
$NEXT_BIN = Join-Path $FRONTEND_DIR "node_modules\.bin\next.cmd"
$URL = "http://localhost:$Port"
$BACKEND_URL = "http://127.0.0.1:$BackendPort"
$EVIDENCE_EVAL_JSON = Join-Path $BUNDLE_ROOT "data_trace_bundle\09_medical_rag\medical_rag_eval.json"
$EVIDENCE_ZH_ASK_JSON = Join-Path $BUNDLE_ROOT "data_trace_bundle\09_medical_rag\medical_rag_eval_zh_ask.json"
$EVIDENCE_DEPLOYMENT_SMOKE_MATRIX_JSON = Join-Path $BUNDLE_ROOT "data_trace_bundle\12_final_supplemental_experiments\track3_medical_rag_supplemental\track3_deployment_smoke_matrix.json"
$EVIDENCE_SUPPLEMENTAL_SUMMARY_JSON = Join-Path $BUNDLE_ROOT "data_trace_bundle\12_final_supplemental_experiments\track3_medical_rag_supplemental\track3_supplemental_summary.json"

function Write-Ok { param([string]$Msg) Write-Host "[OK] $Msg" -ForegroundColor Green }
function Write-Warn { param([string]$Msg) Write-Host "[WARN] $Msg" -ForegroundColor Yellow }
function Write-Info { param([string]$Msg) Write-Host "[INFO] $Msg" -ForegroundColor Gray }
function Write-Err { param([string]$Msg) Write-Host "[ERROR] $Msg" -ForegroundColor Red }

function Assert-File {
    param([string]$Path, [string]$Label)
    if (-not (Test-Path $Path)) {
        throw "$Label missing: $Path"
    }
    Write-Ok "$Label ready: $Path"
}

function Invoke-EvidenceOnlyCheck {
    Assert-File -Path $EVIDENCE_EVAL_JSON -Label "Track3 retrieval evidence JSON"
    Assert-File -Path $EVIDENCE_ZH_ASK_JSON -Label "Track3 Chinese Ask evidence JSON"
    Assert-File -Path $EVIDENCE_DEPLOYMENT_SMOKE_MATRIX_JSON -Label "Track3 deployment smoke matrix evidence JSON"
    Assert-File -Path $EVIDENCE_SUPPLEMENTAL_SUMMARY_JSON -Label "Track3 supplemental summary evidence JSON"
    $matrix = Get-Content $EVIDENCE_DEPLOYMENT_SMOKE_MATRIX_JSON -Raw -Encoding UTF8 | ConvertFrom-Json
    $summary = Get-Content $EVIDENCE_SUPPLEMENTAL_SUMMARY_JSON -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($summary.status -notin @("available", "ok")) {
        throw "Track3 supplemental summary status is not available: $($summary.status)"
    }
    $executed = @($matrix.executed_smoke_checks)
    $notRun = @($matrix.not_run_checks)
    if (-not ($executed | Where-Object { $_.name -eq "track3_supplemental_status_cli" -and $_.status -eq "passed" })) {
        throw "Track3 supplemental status CLI smoke is missing or not passed."
    }
    if (($notRun | Where-Object { $_.status -ne "not_run_environment_dependency" }).Count -gt 0) {
        throw "Deployment matrix has environment-dependent checks reported with an unexpected status."
    }
    if ([int]$summary.deployment_smoke_matrix.executed_smoke_checks -ne $executed.Count) {
        throw "Supplemental summary executed smoke count does not match deployment matrix."
    }
    if ([int]$summary.deployment_smoke_matrix.not_run_checks -ne $notRun.Count) {
        throw "Supplemental summary not-run count does not match deployment matrix."
    }
    Write-Ok "Final bundle evidence-only validation passed."
}

if ($EvidenceOnly -or -not (Test-Path $FRONTEND_DIR)) {
    if (-not $EvidenceOnly) {
        Write-Warn "Frontend source is not present in this final bundle; switching to evidence-only validation."
    }
    Invoke-EvidenceOnlyCheck
    exit 0
}

function Test-Command {
    param([string]$Name)
    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Get-PortProcessIds {
    param([int]$TargetPort)

    $connections = Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue
    if (-not $connections) {
        return @()
    }

    return @($connections | Select-Object -ExpandProperty OwningProcess -Unique)
}

function Stop-PortProcesses {
    param([int]$TargetPort)

    $pids = Get-PortProcessIds -TargetPort $TargetPort
    foreach ($pidValue in $pids) {
        $process = Get-Process -Id $pidValue -ErrorAction SilentlyContinue
        if ($process) {
            Write-Warn "Stopping process on port ${TargetPort}: $($process.ProcessName) ($pidValue)"
            Stop-Process -Id $pidValue -Force
            Wait-Process -Id $pidValue -Timeout 5 -ErrorAction SilentlyContinue
        }
    }
}

function Start-Backend {
    $backendPids = Get-PortProcessIds -TargetPort $BackendPort
    if ($backendPids.Count -gt 0) {
        if ($Force) {
            Stop-PortProcesses -TargetPort $BackendPort
        }
        else {
            Write-Ok "FastAPI backend already listening at $BACKEND_URL"
            return
        }
    }

    $backendFile = if ($MYENV_PYTHON) { $MYENV_PYTHON } else { "python" }
    $backendArgs = @("-m", "controlsci.api.medical_rag", "--port", "$BackendPort")
    if ($MYENV_PYTHON -and -not (Test-Path $backendFile)) {
        Write-Warn "Configured Python not found: $MYENV_PYTHON"
    }
    if (-not $MYENV_PYTHON -and (Test-Command "conda")) {
        Write-Info "No explicit Python configured; using conda run -n myenv."
        $backendFile = "conda"
        $backendArgs = @("run", "--no-capture-output", "-n", "myenv", "python") + $backendArgs
    }
    elseif ($MYENV_PYTHON -and -not (Test-Path $MYENV_PYTHON)) {
        if (Test-Command "conda") {
            Write-Warn "Falling back to conda run -n myenv."
            $backendFile = "conda"
            $backendArgs = @("run", "--no-capture-output", "-n", "myenv", "python") + $backendArgs
        }
        else {
            Write-Err "Configured Python not found and conda is unavailable: $MYENV_PYTHON"
            Write-Info "Set CONTROLMIND_PYTHON or CONTROLSCI_PYTHON to the Python executable for this project."
            exit 2
        }
    }

    foreach ($path in @($BACKEND_LOG_PATH, $BACKEND_ERR_LOG_PATH)) {
        if (Test-Path $path) {
            try {
                Remove-Item -LiteralPath $path -Force
            }
            catch {
                Write-Warn "Could not clear locked log file: $path"
            }
        }
    }

    Write-Info "Starting FastAPI backend with myenv Python..."
    Write-Info "Backend log: $BACKEND_LOG_PATH"

    $env:PYTHONUTF8 = "1"
    $env:PYTHONIOENCODING = "utf-8"
    if (-not $env:CONTROLSCI_API_PROFILE) {
        $env:CONTROLSCI_API_PROFILE = if ($env:CONTROLMIND_PROFILE) { $env:CONTROLMIND_PROFILE } elseif ($env:PROFILE) { $env:PROFILE } else { "cloud_demo" }
    }

    $process = Start-Process `
        -FilePath $backendFile `
        -ArgumentList $backendArgs `
        -WorkingDirectory $ROOT `
        -RedirectStandardOutput $BACKEND_LOG_PATH `
        -RedirectStandardError $BACKEND_ERR_LOG_PATH `
        -WindowStyle Hidden `
        -PassThru

    Start-Sleep -Seconds 5
    $backendPids = Get-PortProcessIds -TargetPort $BackendPort
    if ($backendPids.Count -gt 0) {
        Write-Ok "Started FastAPI backend at $BACKEND_URL. PID: $($process.Id)"
    }
    else {
        Write-Warn "Backend process was started, but port $BackendPort is not listening yet."
        Write-Info "Check log: $BACKEND_LOG_PATH"
        Write-Info "Check error log: $BACKEND_ERR_LOG_PATH"
    }
}

if (-not (Test-Path $FRONTEND_DIR)) {
    Write-Err "Frontend directory not found: $FRONTEND_DIR"
    exit 2
}

if (-not (Test-Path (Join-Path $FRONTEND_DIR "package.json"))) {
    Write-Err "package.json not found under: $FRONTEND_DIR"
    exit 2
}

if (-not (Test-Command "pnpm")) {
    Write-Err "pnpm is required but was not found in PATH."
    Write-Info "Install pnpm or enable it through Corepack, then rerun this script."
    exit 2
}

$nodeModules = Join-Path $FRONTEND_DIR "node_modules"
if ((-not (Test-Path $nodeModules)) -and (-not $Install)) {
    Write-Warn "node_modules is missing. Rerun with -Install to install dependencies first."
    exit 2
}

if ($Install) {
    Write-Info "Installing frontend dependencies..."
    Push-Location $FRONTEND_DIR
    try {
        pnpm install
    }
    finally {
        Pop-Location
    }
}

if (-not (Test-Path $NEXT_BIN)) {
    Write-Err "Next.js executable not found: $NEXT_BIN"
    Write-Info "Run this script with -Install after approving any pnpm build-script prompts if needed."
    exit 2
}

$existingPids = Get-PortProcessIds -TargetPort $Port
if ($existingPids.Count -gt 0) {
    if ($Force) {
        Stop-PortProcesses -TargetPort $Port
    }
    else {
        Write-Warn "Port $Port is already in use by process id(s): $($existingPids -join ', ')"
        Write-Info "Use -Port <port> to choose another port, or -Force to stop the existing listener."
        exit 2
    }
}

if ($StartBackend) {
    Start-Backend
}
else {
    $backendPids = Get-PortProcessIds -TargetPort $BackendPort
    if ($backendPids.Count -gt 0) {
        Write-Ok "FastAPI backend detected at $BACKEND_URL"
    }
    else {
        Write-Warn "FastAPI backend is not listening at $BACKEND_URL"
        Write-Info "Use -StartBackend to launch it with myenv, or start it separately before using live demo modes."
    }
}

Write-Ok "Frontend directory: $FRONTEND_DIR"
Write-Ok "Frontend URL: $URL"

if ($Background) {
    foreach ($path in @($LOG_PATH, $ERR_LOG_PATH)) {
        if (Test-Path $path) {
            try {
                Remove-Item -LiteralPath $path -Force
            }
            catch {
                Write-Warn "Could not clear locked log file: $path"
            }
        }
    }

    $arguments = @("/c", "`"$NEXT_BIN`"", "dev", "-p", "$Port")
    $process = Start-Process `
        -FilePath "cmd.exe" `
        -ArgumentList $arguments `
        -WorkingDirectory $FRONTEND_DIR `
        -RedirectStandardOutput $LOG_PATH `
        -RedirectStandardError $ERR_LOG_PATH `
        -WindowStyle Hidden `
        -PassThru

    Start-Sleep -Seconds 3
    Write-Ok "Started frontend in background. PID: $($process.Id)"
    Write-Info "Log: $LOG_PATH"
    Write-Info "Error log: $ERR_LOG_PATH"

    if ($OpenBrowser) {
        Start-Process $URL
    }

    exit 0
}

if ($OpenBrowser) {
    Start-Process $URL
}

Write-Info "Starting Next.js in the current terminal. Press Ctrl+C to stop."
Push-Location $FRONTEND_DIR
try {
    & $NEXT_BIN dev -p $Port
}
finally {
    Pop-Location
}
