param(
    [int]$ApiPort = 18080,
    [int]$WebPort = 18081,
    [switch]$Force,
    [switch]$OpenBrowser,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$WebRoot = Join-Path $Root "web"

function Get-PortProcessIds([int]$TargetPort) {
    $connections = Get-NetTCPConnection -LocalPort $TargetPort -State Listen -ErrorAction SilentlyContinue
    if (-not $connections) { return @() }
    return @($connections | Select-Object -ExpandProperty OwningProcess -Unique)
}

if ($Force) {
    foreach ($port in @($ApiPort, $WebPort)) {
        foreach ($procId in (Get-PortProcessIds $port)) {
            Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
        }
    }
}

if ($DryRun) {
    Write-Host "Dry-run cloud workbench start plan:" -ForegroundColor Cyan
    Write-Host "  API: .\start.ps1 -Port $ApiPort -Background"
    Write-Host "  Web: next dev -H 127.0.0.1 -p $WebPort"
    Write-Host "  URL: http://127.0.0.1:$WebPort"
    exit 0
}

& (Join-Path $Root "start.ps1") -Port $ApiPort -Background -Force:$Force

$env:CLOUD_DEMO_API_URL = "http://127.0.0.1:$ApiPort"
$env:CONTROLMIND_BACKEND_URL = "http://127.0.0.1:$ApiPort"

$NextBin = Join-Path $WebRoot "node_modules\.bin\next.cmd"
if (-not (Test-Path $NextBin)) {
    $SourceNodeModules = Resolve-Path (Join-Path $Root "..\starboard\node_modules") -ErrorAction SilentlyContinue
    if ($SourceNodeModules -and -not (Test-Path (Join-Path $WebRoot "node_modules"))) {
        cmd /c "mklink /J `"$WebRoot\node_modules`" `"$($SourceNodeModules.Path)`"" | Out-Null
    }
}

if (-not (Test-Path $NextBin)) {
    if (-not (Get-Command pnpm -ErrorAction SilentlyContinue)) {
        Write-Host "node_modules missing under web/, and pnpm was not found. Install pnpm or build with Docker." -ForegroundColor Yellow
        exit 2
    }
    Write-Host "Installing cloud workbench dependencies with pnpm..." -ForegroundColor Cyan
    Push-Location $WebRoot
    try {
        pnpm install
    }
    finally {
        Pop-Location
    }
}

if (-not (Test-Path $NextBin)) {
    Write-Host "Next.js executable still missing after install: $NextBin" -ForegroundColor Yellow
    exit 2
}

$cmd = "`$env:CLOUD_DEMO_API_URL='http://127.0.0.1:$ApiPort'; `$env:CONTROLMIND_BACKEND_URL='http://127.0.0.1:$ApiPort'; & '$NextBin' dev -H 127.0.0.1 -p $WebPort"
Start-Process -FilePath "powershell.exe" `
    -ArgumentList @("-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", $cmd) `
    -WorkingDirectory $WebRoot `
    -WindowStyle Hidden

Start-Sleep -Seconds 5
$url = "http://127.0.0.1:$WebPort"
Write-Host "Started cloud Starboard workbench at $url" -ForegroundColor Green
if ($OpenBrowser) {
    Start-Process $url
}
