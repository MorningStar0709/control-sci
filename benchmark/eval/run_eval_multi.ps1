# PowerShell batch evaluation script.
# Usage: .\run_eval_multi.ps1 -models "deepseek-v4-flash,mimo-v2.5" -input benchmark/dataset/core.json
# Multi-provider example: .\run_eval_multi.ps1 -models "mimo-v2.5-pro" -judge_model "deepseek-v4-flash" -target_base_url "https://api.xiaomimimo.com/v1" -judge_base_url "https://api.deepseek.com" -resume

param(
    [string]$models = "deepseek-v4-flash",
    [Alias("input")]
    [string]$benchmark_input = "benchmark/dataset/core.json",
    [string]$api_key = "",
    [string]$target_api_key = "",
    [string]$judge_api_key = "",
    [string]$base_url = "https://api.deepseek.com",
    [string]$target_base_url = "",
    [string]$judge_base_url = "",
    [string]$judge_model = "deepseek-v4-flash",
    [int]$limit = 0,
    [string]$output_dir = "benchmark/eval/reports",
    [switch]$dry_run,
    [switch]$resume,
    [switch]$retry_failed,
    [int]$retries = 3,
    [int]$max_consecutive_failures = 5
)

if (-not (Test-Path $output_dir)) {
    New-Item -ItemType Directory -Path $output_dir -Force | Out-Null
}

function Get-MaskedArgs {
    param([string[]]$ArgsList)
    $maskNext = $false
    $masked = @()
    foreach ($arg in $ArgsList) {
        if ($maskNext) {
            $masked += "***"
            $maskNext = $false
        } elseif ($arg -in @("--api-key", "--target-api-key", "--judge-api-key", "--hf-token")) {
            $masked += $arg
            $maskNext = $true
        } else {
            $masked += $arg
        }
    }
    return $masked
}

$modelList = $models -split ","

foreach ($model in $modelList) {
    $model = $model.Trim()
    Write-Host "`n===== Evaluating model: $model =====" -ForegroundColor Green

    $safeModel = $model -replace "[:/\\]", "-"
    $outputFile = Join-Path $output_dir "$safeModel`_report.json"

    $evaluateArgs = @(
        "run", "--no-capture-output", "-n", "myenv", "python", "benchmark/eval/evaluate.py"
        "--mode", "model"
        "--input", $benchmark_input
        "--output", $outputFile
        "--target-model", $model
        "--judge-model", $judge_model
        "--base-url", $base_url
        "--retries", $retries.ToString()
        "--max-consecutive-failures", $max_consecutive_failures.ToString()
    )

    if ($target_base_url) { $evaluateArgs += "--target-base-url"; $evaluateArgs += $target_base_url }
    if ($judge_base_url) { $evaluateArgs += "--judge-base-url"; $evaluateArgs += $judge_base_url }
    if ($api_key) { $evaluateArgs += "--api-key"; $evaluateArgs += $api_key }
    if ($target_api_key) { $evaluateArgs += "--target-api-key"; $evaluateArgs += $target_api_key }
    if ($judge_api_key) { $evaluateArgs += "--judge-api-key"; $evaluateArgs += $judge_api_key }
    if ($limit -gt 0) { $evaluateArgs += "--limit"; $evaluateArgs += $limit.ToString() }
    if ($resume) { $evaluateArgs += "--resume" }
    if ($retry_failed) { $evaluateArgs += "--retry-failed" }

    $displayArgs = Get-MaskedArgs -ArgsList $evaluateArgs
    Write-Host "Running: conda $($displayArgs -join ' ')" -ForegroundColor Yellow
    if ($dry_run) {
        Write-Host "Dry-run: command not executed; output would be $outputFile" -ForegroundColor DarkGray
        continue
    }
    & "conda" $evaluateArgs

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Model $model completed: $outputFile" -ForegroundColor Green
    } else {
        Write-Host "Model $model failed (exit code: $LASTEXITCODE)" -ForegroundColor Red
    }
}
