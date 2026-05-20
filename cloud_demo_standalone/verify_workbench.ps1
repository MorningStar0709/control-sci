param(
    [int]$WebPort = 18081
)

$ErrorActionPreference = "Stop"

function Assert-True($Condition, [string]$Message) {
    if (-not $Condition) {
        throw $Message
    }
    Write-Host "[OK] $Message" -ForegroundColor Green
}

$base = "http://127.0.0.1:$WebPort"

$health = Invoke-RestMethod -Uri "$base/api/demo/health" -TimeoutSec 15
Assert-True ($health.profile -eq "pure_cloud_demo") "workbench API proxy reaches pure cloud API"
Assert-True ($health.components.web_workbench.available -eq $true) "workbench health advertises Next shell"

$runtime = Invoke-RestMethod -Uri "$base/api/demo/runtime/options" -TimeoutSec 15
Assert-True ($runtime.mode -eq "pure_cloud_only") "workbench runtime is pure_cloud_only"
Assert-True ($runtime.local_models.Count -eq 0) "workbench exposes no local models"
Assert-True ($runtime.local_indexes.Count -eq 0) "workbench exposes no local indexes"

$demo = Invoke-WebRequest -Uri "$base/demo" -TimeoutSec 20 -UseBasicParsing
Assert-True ($demo.StatusCode -eq 200) "Next demo page loads"
Assert-True ($demo.Content -match "ControlMind") "page title aligns with local workbench"

$sourceText = "Public de-identified abstract: Track1 backend needs MinerU parsing, DeepSeek question generation, and DeepSeek grading, returning questions, expected answers, and grading reasons."
$quizBody = @{ source_text = $sourceText; topic = "Track1 acceptance"; count = 1; dry_run = $true } | ConvertTo-Json
$quiz = Invoke-RestMethod -Uri "$base/api/demo/quiz/generate" -Method Post -Body $quizBody -ContentType "application/json" -TimeoutSec 20
Assert-True ($quiz.questions.Count -eq 1) "workbench proxy exposes quiz generation API"

$gradeBody = @{
    question = "Which backend capabilities are demonstrated by this public abstract?"
    expected_answer = "The backend demonstrates parsing, question generation, grading, and public/de-identified material boundaries."
    rubric = "10 points: mention parsing, question generation, grading, and public-data boundary."
    student_answer = "The backend includes parsing, question-generation, and grading APIs, and only uses public de-identified material."
    source_text = $sourceText
    dry_run = $true
} | ConvertTo-Json -Depth 8 -Compress
$grade = Invoke-RestMethod -Uri "$base/api/demo/quiz/grade" -Method Post -Body $gradeBody -ContentType "application/json" -TimeoutSec 20
Assert-True ($grade.max_score -eq 10) "workbench proxy exposes quiz grading API"

$planBody = @{ goal = "convert a public paper into four-axis evaluation questions and a verification summary" } | ConvertTo-Json
$plan = Invoke-RestMethod -Uri "$base/api/demo/agent/plan" -Method Post -Body $planBody -ContentType "application/json" -TimeoutSec 20
Assert-True ($plan.dag.Count -ge 1) "workbench proxy exposes agent planning API"

$ragBody = @{ question = "does a closed-loop insulin system increase hypoglycemia risk, and what evidence is cited?"; dry_run = $true } | ConvertTo-Json
$rag = Invoke-RestMethod -Uri "$base/api/demo/medical-rag/ask" -Method Post -Body $ragBody -ContentType "application/json" -TimeoutSec 20
Assert-True ($rag.retrieved_sources.Count -ge 1) "workbench proxy exposes medical mini RAG API"

Write-Host ""
Write-Host "Cloud workbench verification passed: $base/demo" -ForegroundColor Cyan
