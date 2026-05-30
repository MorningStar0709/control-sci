# Final Supplemental Experiments

本目录保存一组低成本补充实验的原始日志与摘要。实验均以只读或 dry-run 方式运行，输出仅写入本目录，不覆盖原始语料、索引、评测结果或报告数据。

| Experiment | Scope | Result | Primary evidence |
|---|---|---|---|
| Minimal acceptance | 三赛道一键入口最小验收 | Track 1: 5/5 pass; Track 2: 4/4 pass; Track 3: 6/7 pass, 1 API health check skipped by design | `minimal_acceptance/` |
| Track 3 refusal boundary | 医疗问答高风险边界与证据不足拒答 | 3/3 safety-refusal cases returned without retrieval or cloud context transfer | `track3_refusal/` |
| Track 2 fallback / replay trace | Agent 本地模式、依赖 DAG 与一键复现入口 | dry-run completed; local plan expanded to 8 DAG steps; reproduce_all entrypoint resolved | `track2_fallback/` |
| Track 2 agent reliability | 自然语言规划、故障恢复、多源选择 A/B、资源调度 Pareto、复杂文档覆盖的可复核证据包 | Router 25/25 success; failure injection 18/18 recovered; Agent source-selection accuracy 0.85 vs fixed rule 0.75; resource Pareto 10/12 success; hard-document coverage 15 samples / 6 challenge types | `track2_agent_reliability/` |
| Track 1 local dataset loading | ControlSci 本地 JSON 作为 HuggingFace datasets 输入 | `load_dataset("json")` loaded 500 rows with expected schema | `track1_load/` |

## Interpretation

这些实验不替代主实验结果，只用于补强公开提交包中的工程可靠性、可复现入口和边界控制证据。所有精确数值仍以原始数据包、主评测日志和 `shared/DATA-TRACE.md` 中登记的权威清单为准。
