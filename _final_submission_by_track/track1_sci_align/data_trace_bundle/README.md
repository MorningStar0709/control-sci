# Track 1 DATA-TRACE Bundle — Sci-Align Evidence Index

本目录是 Track 1 Sci-Align final package 的赛道裁剪证据包。文件均为提交包内真实存在的副本，完整清单与 SHA-256 见 `manifest.json`。

## Included

| 子目录 | 内容 |
|:--|:--|
| `01_corpus_scale/` | 语料规模、PCA、文档相似度、MinerU/PyMuPDF 对照等统计 |
| `02_benchmark/` | Sci-Align core 数据集、飞轮样本与图文索引；full 数据集见 `../dataset/full.json` |
| `03_leaderboard/` | 排行榜、评测结果与 scorecard evidence |
| `04_qlora_ppl/` | QLoRA、PPL 与训练可用性相关 evidence |
| `05_cross_modal/` | 跨模态对齐审计摘要 |
| `06_visual_audit/` | MiMo 视觉审计结果 |
| `07_flywheel/` | Agent 飞轮公开论文、日志与能力配置 |
| `08_think_probe/` | Think 模式探针结果 |
| `10_charts/` | 提交报告图表与 chart manifest |
| `11_throughput/` | GPU / HF embedding 吞吐短测 |
| `12_final_supplemental_experiments/` | Track 1 reliability 与跨赛道 sanity evidence |
| `13_sciverse_integration/` | SciVerse 集成与 submission readiness evidence |

## Excluded

| 目录 | 原因 |
|:--|:--|
| `09_medical_rag/`、`09_medical_rag_large/` | 属于 Track 3 Medical RAG final package |
| `10_charts_large/` | 大型 embedding cache 不随 Track 1 裁剪包分发 |

## Supplemental Focus

Track 1 的新增补充实验证据位于 `12_final_supplemental_experiments/track1_sci_align_reliability/`，覆盖数据可消费性、完整性、跨模态 taxonomy、四维区分度、训练可用性、外部格式兼容与小样本复核一致性。

## Evidence Boundary

| 类型 | 目录 | 用途 |
|:--|:--|:--|
| Track 1 primary evidence | `02_benchmark/`、`03_leaderboard/`、`04_qlora_ppl/`、`05_cross_modal/`、`06_visual_audit/`、`12_final_supplemental_experiments/track1_sci_align_reliability/` | 支撑 Sci-Align 数据集、排行榜、训练可用性、跨模态审计与补充可靠性结论 |
| Shared acceptance evidence | `12_final_supplemental_experiments/minimal_acceptance/`、`12_final_supplemental_experiments/track1_load/`、`12_final_supplemental_experiments/track2_fallback/`、`12_final_supplemental_experiments/track3_refusal/` | 用于说明三赛道统一验收入口与边界控制，不作为 Track 1 主结论证据 |
| Cross-track integration evidence | `13_sciverse_integration/`、`07_flywheel/`、`11_throughput/` | 用于说明 ControlMind / Sciverse 统一集成链路；具体赛道结论以本表 primary evidence 为准 |

## License

CC-BY-4.0。飞轮 arXiv 论文版权归原作者所有。
