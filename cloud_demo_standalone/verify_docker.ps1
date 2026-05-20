param(
    [int]$Port = 18080,
    [switch]$ConfigOnly
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path

function Invoke-Checked([scriptblock]$Command, [string]$Label) {
    & $Command
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed with exit code $LASTEXITCODE"
    }
    Write-Host "[OK] $Label" -ForegroundColor Green
}

Push-Location $Root
try {
    Invoke-Checked { docker compose config | Out-Null } "docker compose config"
    if ($ConfigOnly) {
        Write-Host "Docker compose config verified. Build skipped by -ConfigOnly." -ForegroundColor Cyan
        exit 0
    }
    Invoke-Checked { docker compose build } "docker compose build for API and Next workbench"

    Write-Host "Docker image verified. To run:" -ForegroundColor Cyan
    Write-Host "  docker compose up -d" -ForegroundColor Cyan
    Write-Host "  curl http://127.0.0.1:$Port/api/demo/health" -ForegroundColor Cyan
}
finally {
    Pop-Location
}
