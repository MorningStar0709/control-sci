# Track 2 DATA-TRACE Bundle — Data Agent Evidence Index

本目录是 Track 2 Data Agent final package 的赛道裁剪证据包。文件均为提交包内真实存在的副本，完整清单与 SHA-256 见 `manifest.json`。

## Included

| 子目录 | 内容 |
|:--|:--|
| `01_corpus_scale/` | 语料规模与文档结构统计 |
| `02_benchmark/` | 与 Agent 任务复用的 Sci-Align 数据入口 |
| `03_leaderboard/` | Agent 评测链路引用的排行榜与 scorecard evidence |
| `04_qlora_ppl/` | 训练 / PPL 探针引用证据 |
| `05_cross_modal/` | 跨模态审计摘要 |
| `06_visual_audit/` | 视觉审计结果 |
| `07_flywheel/` | Agent 飞轮公开论文、日志与能力配置 |
| `08_think_probe/` | Think 模式探针结果 |
| `10_charts/` | 提交报告图表与 chart manifest |
| `11_throughput/` | 吞吐短测 |
| `12_final_supplemental_experiments/` | Track 2 reliability 与跨赛道 sanity evidence |
| `13_sciverse_integration/` | SciVerse 集成 readiness evidence |

## Excluded

| 目录 | 原因 |
|:--|:--|
| `09_medical_rag/`、`09_medical_rag_large/` | 属于 Track 3 Medical RAG final package |
| `10_charts_large/` | 大型 embedding cache 不随 Track 2 裁剪包分发 |

## Supplemental Focus

Track 2 的新增补充实验证据位于 `12_final_supplemental_experiments/track2_agent_reliability/`，覆盖 router robustness、failure injection、source-selection ablation、resource Pareto 与 hard-document stress。

Agent 相关入口另见 final package 根目录的 `agent/`、`run/`、`track2_agent_20_cases.md` 与 `track2_agent_deploy.md`。

## Evidence Boundary

| 类型 | 目录 | 用途 |
|:--|:--|:--|
| Track 2 primary evidence | `07_flywheel/`、`08_think_probe/`、`12_final_supplemental_experiments/track2_agent_reliability/`、`12_final_supplemental_experiments/track2_fallback/` | 支撑 Intent Router、DAG 执行、失败恢复、source selection、资源调度与 Agent dry-run 复核结论 |
| Shared data / evaluation evidence | `01_corpus_scale/`、`02_benchmark/`、`03_leaderboard/`、`04_qlora_ppl/`、`05_cross_modal/`、`06_visual_audit/`、`11_throughput/` | Agent 复用的科学数据、排行榜、训练与跨模态审计底座，不单独替代 Track 1 主证据 |
| Shared acceptance evidence | `12_final_supplemental_experiments/minimal_acceptance/`、`12_final_supplemental_experiments/track1_load/`、`12_final_supplemental_experiments/track3_refusal/` | 用于说明三赛道统一验收入口与边界控制，不作为 Track 2 主结论证据 |
| Cross-track integration evidence | `13_sciverse_integration/` | 用于说明 Sciverse intent 与三赛道集成链路；具体 Agent 结论以本表 primary evidence 为准 |

## License

CC-BY-4.0。飞轮 arXiv 论文版权归原作者所有。
