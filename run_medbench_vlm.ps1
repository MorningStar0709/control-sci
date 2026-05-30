
<#
  MedBench VLM 一键续跑 / 启动脚本
  用法: 在项目根目录打开 PowerShell, 执行 .\_tools\run_medbench_vlm.ps1
  日志输出到 _scratch/medbench_vlm_run.log
  中断后重新运行此脚本即可自动 --resume
#>

$ErrorActionPreference = "Continue"

$env:PYTHONIOENCODING = 'utf-8'
$env:CONDA_NO_PLUGINS = 'true'

$LOG = "_scratch/medbench_vlm_run.log"
$FULL = "_scratch/medbench_vlm_full.log"

Write-Host "========================================"
Write-Host "  MedBench VLM 评测"
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host "  日志: $LOG"
Write-Host "========================================"
Write-Host ""

$ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
"[$ts] START" | Out-File $FULL -Encoding UTF8
"[$ts] START" | Out-File $LOG -Encoding UTF8

$proc = Start-Process -FilePath "conda" `
    -ArgumentList "run --no-capture-output -n myenv python _scratch/medbench_vlm_test.py --resume --report-every 10" `
    -NoNewWindow -Wait -RedirectStandardOutput $FULL -RedirectStandardError $FULL -PassThru

$ts_done = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Write-Host ""
Write-Host "========================================"
Write-Host "  完成时间: $ts_done"
Write-Host "  退出码: $($proc.ExitCode)"
Write-Host "  报告: data/sources_medical/medbench/medbench_vlm_report.json"
Write-Host "========================================"

# 从 FULL 日志提取关键行（去掉 embed 噪音）
if (Test-Path $FULL) {
    Get-Content $FULL | Where-Object { $_ -notmatch '^  \[embed\]' -and $_ -notmatch 'accomplished' } | Out-File $LOG -Encoding UTF8
}

# 最终状态
$status = Get-Content "data/sources_medical/medbench/medbench_vlm_report.json.status.json" -ErrorAction SilentlyContinue | ConvertFrom-Json -ErrorAction SilentlyContinue
if ($status) {
    Write-Host "  状态: $($status.state) | 完成: $($status.completed)/300"
}
