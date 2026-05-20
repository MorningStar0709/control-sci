param(
    [int]$Chunks = 4,
    [switch]$DryRun
)

$projectRoot = Split-Path $PSScriptRoot -Parent
$script = "pipeline\complete_metadata.py"
$totalDocs = 362
if ($Chunks -lt 1) {
    throw "Chunks must be >= 1"
}
$chunkSize = [math]::Ceiling($totalDocs / $Chunks)

Write-Host "=== T1 Parallel Launch ($Chunks workers) ===" -ForegroundColor Cyan
Write-Host "Total: $totalDocs, Per chunk: $chunkSize" -ForegroundColor Cyan

$pids = @()

for ($i = 0; $i -lt $Chunks; $i++) {
    $offset = $i * $chunkSize
    $limit = [math]::Min($chunkSize, $totalDocs - $offset)
    $cpPath = "pipeline\complete_metadata.checkpoint.chunk_$i.json"
    $logFile = "pipeline\t1_chunk_$i.log"
    $errFile = "pipeline\t1_chunk_$i.err.log"

    $env:PYTHONIOENCODING = "utf-8"
    $env:CONDA_NO_PLUGINS = "true"
    $argsList = @(
        "run", "--no-capture-output", "-n", "myenv", "python",
        $script,
        "--offset", "$offset",
        "--limit", "$limit",
        "--checkpoint-path", $cpPath,
        "--skip-arxiv",
        "--skip-cross"
    )

    if ($DryRun) {
        Write-Host "[DRY-RUN] conda $($argsList -join ' ')" -ForegroundColor DarkGray
        continue
    }

    $p = Start-Process -FilePath "conda" `
        -ArgumentList $argsList `
        -WorkingDirectory $projectRoot `
        -RedirectStandardOutput (Join-Path $projectRoot $logFile) `
        -RedirectStandardError (Join-Path $projectRoot $errFile) `
        -PassThru -WindowStyle Hidden
    $pids += $p.Id

    Write-Host "[Chunk $i] PID=$($p.Id) offset=$offset limit=$limit cp=$cpPath" -ForegroundColor Green
}

if ($DryRun) {
    Write-Host "`nDry-run validated: $Chunks chunk launch commands." -ForegroundColor Green
    exit 0
}

Write-Host "`n$($pids.Count) processes launched (hidden)" -ForegroundColor Yellow
Write-Host "Logs: pipeline\t1_chunk_*.log" -ForegroundColor Yellow
Write-Host "`nCheck progress:" -ForegroundColor Cyan
Write-Host "  Get-Content pipeline\t1_chunk_0.log -Tail 5" -ForegroundColor Gray
Write-Host "  Get-Content pipeline\t1_chunk_1.log -Tail 5" -ForegroundColor Gray
Write-Host "  Get-Content pipeline\t1_chunk_2.log -Tail 5" -ForegroundColor Gray
Write-Host "  Get-Content pipeline\t1_chunk_3.log -Tail 5" -ForegroundColor Gray
