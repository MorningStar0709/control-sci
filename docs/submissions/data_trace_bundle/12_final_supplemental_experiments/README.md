# Final Supplemental Experiments

本目录保存一组低成本补充实验的原始日志与摘要。实验均以只读或 dry-run 方式运行，输出仅写入本目录，不覆盖原始语料、索引、评测结果或报告数据。

| Experiment | Scope | Result | Primary evidence |
|---|---|---|---|
| Minimal acceptance | 三赛道一键入口最小验收 | Track 1: 5/5 pass; Track 2: 4/4 pass; Track 3: 6/7 pass, 1 API health check skipped by design | `minimal_acceptance/` |
| Track 3 refusal boundary | 医疗问答高风险边界与证据不足拒答 | 3/3 safety-refusal cases returned without retrieval or cloud context transfer | `track3_refusal/` |
| Track 2 fallback / replay trace | Agent 本地模式、依赖 DAG 与一键复现入口 | dry-run completed; local plan expanded to 8 DAG steps; reproduce_all entrypoint resolved | `track2_fallback/` |
| Track 2 agent reliability | 自然语言规划、故障恢复、多源选择 A/B、资源调度 Pareto、复杂文档覆盖的可复核证据包 | Router 25/25 success; failure injection 18/18 recovered; Agent source-selection accuracy 0.85 vs fixed rule 0.75; resource Pareto 10/12 success; hard-document coverage 15 samples / 6 challenge types | `track2_agent_reliability/` |
| Track 1 local dataset loading | ControlSci 本地 JSON 作为 HuggingFace datasets 输入 | `load_dataset("json")` loaded 500 rows with expected schema | `track1_load/` |
| Track 1 Sci-Align reliability | 数据集可消费性、完整性、跨模态 taxonomy、四维区分度、训练可用性、外部格式兼容与小样本复核一致性 | core=500 / full=889；source_ref_resolved_rate=1.0；C/D range mean=0.397 > A/B 0.117；4 formats preserved key fields；sample review bucket agreement=0.7345 | `track1_sci_align_reliability/` |
| Track 3 Medical RAG supplemental | 阶段消融、安全拒答、EI taxonomy、隐私边界、语义切片、中文 Ask 鲁棒性、Evidence Card 与部署 smoke matrix | 9 个 JSON evidence files；deployment smoke executed_passed_count=2，not_run_count=3；supplemental summary status=available | `track3_medical_rag_supplemental/` |

## Interpretation

这些实验不替代主实验结果，只用于补强公开提交包中的工程可靠性、可复现入口和边界控制证据。所有精确数值仍以原始数据包、主评测日志和 `shared/DATA-TRACE.md` 中登记的权威清单为准。Track3 supplemental 已同步进入 Track3 final bundle；final bundle 的 manifest 用于验证包内文件完整性，不替代本目录的实验语义说明。
