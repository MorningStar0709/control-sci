param(
    [int]$Port = 18080
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
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

function Assert-True($Condition, [string]$Message) {
    if (-not $Condition) {
        throw $Message
    }
    Write-Host "[OK] $Message" -ForegroundColor Green
}

Push-Location $Root
try {
    & $Python @PythonPrefix -m py_compile app.py
    Assert-True ($LASTEXITCODE -eq 0) "Python syntax check"

    $base = "http://127.0.0.1:$Port"
    $health = Invoke-RestMethod -Uri "$base/api/health" -TimeoutSec 10
    Assert-True ($health.profile -eq "pure_cloud_demo") "health profile is pure_cloud_demo"
    Assert-True ($health.boundary.forbidden -contains "local_gpu_task") "offline heavy tasks forbidden"

    $runtime = Invoke-RestMethod -Uri "$base/api/runtime" -TimeoutSec 10
    Assert-True ($runtime.mode -eq "pure_cloud_only") "runtime is pure_cloud_only"
    Assert-True ($runtime.local_models.Count -eq 0) "no offline models exposed"
    Assert-True ($runtime.parser_backends[0].id -eq "mineru_official") "MinerU official parser only"

    $quota = Invoke-RestMethod -Uri "$base/api/quota" -TimeoutSec 10
    Assert-True ($quota.limit -ge 1) "quota endpoint works"

    $apiRoot = Invoke-RestMethod -Uri "$base/" -TimeoutSec 10
    Assert-True ($apiRoot.name -eq "ControlMind Pure Cloud Demo API") "API root identifies standalone cloud API"
    Assert-True ($health.components.web_workbench.available -eq $true) "Next workbench is the expected UI surface"

    $askBody = @{ question = "primary endpoint and safety evidence"; context = ""; dry_run = $true } | ConvertTo-Json
    $ask = Invoke-RestMethod -Uri "$base/api/deepseek/ask" -Method Post -Body $askBody -ContentType "application/json" -TimeoutSec 20
    Assert-True ($ask.status -in @("ok", "mock", "dry_run")) "DeepSeek endpoint returns ok, no-key mock, or dry-run"

    $planBody = @{ goal = "convert a public paper into four-axis evaluation questions and a verification summary" } | ConvertTo-Json
    $plan = Invoke-RestMethod -Uri "$base/api/agent/plan" -Method Post -Body $planBody -ContentType "application/json" -TimeoutSec 20
    Assert-True ($plan.dag.Count -ge 1) "agent planning API returns a public DAG"

    $ragBody = @{ question = "does a closed-loop insulin system increase hypoglycemia risk, and what evidence is cited?"; dry_run = $true } | ConvertTo-Json
    $rag = Invoke-RestMethod -Uri "$base/api/medical-rag/ask" -Method Post -Body $ragBody -ContentType "application/json" -TimeoutSec 20
    Assert-True ($rag.retrieved_sources.Count -ge 1) "medical mini RAG retrieves public sources"

    $sourceText = "Public de-identified abstract: the study compares a closed-loop insulin system with usual care, focusing on endpoints, safety events, hypoglycemia risk, and limitations."
    $quizBody = @{ source_text = $sourceText; topic = "safety evidence"; count = 2; dry_run = $true } | ConvertTo-Json
    $quiz = Invoke-RestMethod -Uri "$base/api/quiz/generate" -Method Post -Body $quizBody -ContentType "application/json" -TimeoutSec 20
    Assert-True ($quiz.questions.Count -ge 1) "quiz generation API returns questions"

    $gradeBody = @{
        question = "What evidence boundary should be preserved when interpreting this safety abstract?"
        expected_answer = "The answer should stay within public endpoint and safety evidence and avoid personal medical advice."
        rubric = "10 points: evidence boundary, endpoint/safety mention, and no personal diagnosis."
        student_answer = "The study should be interpreted using endpoints and safety events, and should not be extended into personal medical advice."
        source_text = $sourceText
        dry_run = $true
    } | ConvertTo-Json -Depth 8 -Compress
    $grade = Invoke-RestMethod -Uri "$base/api/quiz/grade" -Method Post -Body $gradeBody -ContentType "application/json" -TimeoutSec 20
    Assert-True ($grade.max_score -eq 10) "quiz grading API returns score payload"

    Write-Host ""
    Write-Host "Pure cloud demo verification passed: $base" -ForegroundColor Cyan
}
finally {
    Pop-Location
}
