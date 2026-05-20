# Track 2 Fallback and Replay Trace

## Purpose

验证 Agent 入口在不执行长任务、不改写产物的前提下，能够解析本地模式、展开依赖 DAG，并定位一键复现入口。

## Commands

```powershell
python benchmark\agent\agent_cli.py --dry-run --local --intents medical_rag,cross_modal_audit,leaderboard_viz --output-log docs\evidence\final_supplemental_experiments\track2_fallback\local_dry_run_trace.json
```

```powershell
python benchmark\agent\agent_cli.py --dry-run --intents reproduce_all --output-log docs\evidence\final_supplemental_experiments\track2_fallback\reproduce_all_dry_run_trace.json
```

## Result

- Local dry-run final status: `completed`
- Dependency DAG expansion: `mineru_parse -> medical_rag -> corpus_parse -> cross_modal_audit -> benchmark_build -> quality_arbitrate -> model_evaluate -> leaderboard_viz`
- Planned steps: `8`
- Execution mutation: none; all steps were dry-run `skipped`
- Replay entrypoint final status: `completed`
- Replay entrypoint resolved step: `reproduce_all (全量复现)` via `run_evaluation.ps1`

## Evidence

- Structured trace: `local_dry_run_trace.json`
- Console log: `local_dry_run_trace.log`
- Replay structured trace: `reproduce_all_dry_run_trace.json`
- Replay console log: `reproduce_all_dry_run_trace.log`

## Notes

该实验用于证明任务规划与复现入口可解析，不声明长任务已在本次 dry-run 中重新执行。完整执行结果仍以主实验日志和提交包中的既有原始记录为准。
