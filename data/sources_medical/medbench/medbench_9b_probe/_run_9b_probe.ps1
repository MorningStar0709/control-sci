param(
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$projectRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")
Set-Location -LiteralPath $projectRoot
$env:PYTHONUTF8 = "1"
$env:PYTHONUNBUFFERED = "1"
$jobs = '[{"n":15,"subset":"MedExam"},{"n":10,"subset":"MedReportQC"},{"n":10,"subset":"MedRxPlan"},{"n":5,"subset":"MedDiag"},{"n":5,"subset":"MedTreat"},{"n":5,"subset":"MedLitQA"}]' | ConvertFrom-Json
$statusPath = "data\sources_medical\medbench\medbench_9b_probe\_aggregate.status.json"
$model = "qwen3.5:9b"
$topK = "5"
$resume = $true
$dryRun = [bool]($DryRun -or $env:MEDBENCH_PROBE_DRY_RUN -eq "1")
$started = Get-Date
$completed = 0
$failed = 0

foreach ($job in $jobs) {
    $subset = [string]$job.subset
    $n = [int]$job.n
    $out = Join-Path "data\sources_medical\medbench\medbench_9b_probe" ("medbench_9b_probe_" + $subset + ".json")
    $progress = "$out.progress.jsonl"
    $status = "$out.status.json"
    $argsList = @(
        "run", "--no-capture-output", "-n", "myenv", "python",
        "_tools/eval_medbench.py",
        "--model", $model,
        "--top-k", $topK,
        "--subset", $subset,
        "--max-questions", $n,
        "--output", $out,
        "--progress", $progress,
        "--status", $status,
        "--report-every", "5"
    )
    if ($resume) { $argsList += "--resume" }

    if ($dryRun) {
        Write-Host "[DRY-RUN] conda $($argsList -join ' ')" -ForegroundColor DarkGray
        continue
    }

    @{
        state = "running"
        model = $model
        current_subset = $subset
        current_max_questions = $n
        completed_subsets = $completed
        failed_subsets = $failed
        total_subsets = $jobs.Count
        elapsed_seconds = [math]::Round(((Get-Date) - $started).TotalSeconds, 1)
        updated_at = (Get-Date).ToString("s")
        output_dir = "data\sources_medical\medbench\medbench_9b_probe"
    } | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $statusPath -Encoding UTF8

    try {
        & conda @argsList
        if ($LASTEXITCODE -ne 0) { throw "conda exited with code $LASTEXITCODE" }
        $completed += 1
    } catch {
        $failed += 1
        Write-Error ("Subset " + $subset + " failed: " + $_.Exception.Message)
    }
}

if ($dryRun) {
    Write-Host "[DRY-RUN] medbench 9B probe plan validated." -ForegroundColor Green
    exit 0
}

@{
    state = $(if ($failed -eq 0) { "completed" } else { "completed_with_errors" })
    model = $model
    completed_subsets = $completed
    failed_subsets = $failed
    total_subsets = $jobs.Count
    elapsed_seconds = [math]::Round(((Get-Date) - $started).TotalSeconds, 1)
    updated_at = (Get-Date).ToString("s")
    output_dir = "data\sources_medical\medbench\medbench_9b_probe"
} | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $statusPath -Encoding UTF8

