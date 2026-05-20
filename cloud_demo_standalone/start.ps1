param(
    [int]$Port = 18080,
    [switch]$Background,
    [switch]$Force,
    [switch]$OpenBrowser
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path (Join-Path $Root "..")
$Python = if ($env:CONTROLMIND_PYTHON) { $env:CONTROLMIND_PYTHON } elseif ($env:CONTROLSCI_PYTHON) { $env:CONTROLSCI_PYTHON } else { "" }
$PythonPrefix = @()
if ($Python -and (Test-Path $Python)) {
    $PythonPrefix = @()
}
elseif (Get-Command conda -ErrorAction SilentlyContinue) {
    $Python = "conda"
    $PythonPrefix = @("run", "--no-capture-output", "-n", "myenv", "python")
}
else {
    $Python = "python"
    $PythonPrefix = @()
}

function Get-PortProcessIds([int]$TargetPort) {
    $connections = Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue
    if (-not $connections) { return @() }
    return @($connections | Select-Object -ExpandProperty OwningProcess -Unique)
}

if ($Force) {
    foreach ($procId in (Get-PortProcessIds $Port)) {
        Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
    }
}
elseif ((Get-PortProcessIds $Port).Count -gt 0) {
    Write-Host "Port $Port is already in use. Use -Force to stop the existing listener." -ForegroundColor Yellow
    exit 2
}

$env:CLOUD_DEMO_PORT = "$Port"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
if (-not $env:DEMO_ACCESS_CODE -and -not $env:DEMO_ALLOW_DRY_RUN_WITHOUT_CODE) {
    $env:DEMO_ALLOW_DRY_RUN_WITHOUT_CODE = "1"
}

if ($Background) {
    $OutLog = Join-Path $Root "server.log"
    $ErrLog = Join-Path $Root "server.err.log"
    $process = Start-Process -FilePath $Python `
        -ArgumentList ($PythonPrefix + @("-m", "uvicorn", "app:app", "--host", "127.0.0.1", "--port", "$Port")) `
        -WorkingDirectory $Root `
        -RedirectStandardOutput $OutLog `
        -RedirectStandardError $ErrLog `
        -WindowStyle Hidden `
        -PassThru
    Start-Sleep -Seconds 3
    Write-Host "Started pure cloud demo at http://127.0.0.1:$Port (PID $($process.Id))" -ForegroundColor Green
    if ($OpenBrowser) {
        Start-Process "http://127.0.0.1:$Port"
    }
    exit 0
}

if ($OpenBrowser) {
    Start-Process "http://127.0.0.1:$Port"
}

Push-Location $Root
try {
    & $Python @PythonPrefix -m uvicorn app:app --host 127.0.0.1 --port $Port
}
finally {
    Pop-Location
}
