# Track 3 DATA-TRACE Bundle — Medical RAG Evidence Index

本目录是 Track 3 Medical RAG final package 的赛道裁剪证据包。文件均为提交包内真实存在的副本，完整清单与 SHA-256 见 `manifest.json`。

## Included

| 子目录 | 内容 |
|:--|:--|
| `01_corpus_scale/` | MinerU/PyMuPDF 入口对照 |
| `09_medical_rag/` | Medical RAG 评测、视觉注入、MedBench 与 QA evidence |
| `09_medical_rag_large/` | 医学 RAG 索引与检索缓存 |
| `10_charts/` | 提交报告图表与 chart manifest |
| `10_charts_large/` | embedding cache |
| `11_throughput/` | GPU / HF embedding 吞吐短测 |
| `12_final_supplemental_experiments/` | Track 3 supplemental experiments 与跨赛道 sanity evidence |
| `13_sciverse_integration/` | SciVerse 集成 readiness evidence |

## Excluded

| 目录 | 原因 |
|:--|:--|
| `02_benchmark/`、`03_leaderboard/`、`04_qlora_ppl/`、`05_cross_modal/`、`06_visual_audit/`、`07_flywheel/`、`08_think_probe/` | 属于 Track 1 / Track 2 通用科学评测与 Agent 证据包 |

## Supplemental Focus

Track 3 的新增补充实验证据位于 `12_final_supplemental_experiments/track3_medical_rag_supplemental/`（阶段消融、安全拒答压力、EI taxonomy、隐私边界、语义切片、中文 Ask 鲁棒性、Evidence Card 完整性与 deployment smoke matrix）。安全拒答独立证据见 `12_final_supplemental_experiments/track3_refusal/`（3/3 safety_refusal，retrieval_mode=none，云端上下文传输 false）。

## Evidence Boundary

| 类型 | 目录 | 用途 |
|:--|:--|:--|
| Track 3 primary evidence | `09_medical_rag/`、`09_medical_rag_large/`、`10_charts_large/`、`12_final_supplemental_experiments/track3_medical_rag_supplemental/`、`12_final_supplemental_experiments/track3_refusal/` | 支撑 Medical RAG 检索、中文 Ask、视觉增强、医学索引、安全拒答与补充实验结论 |
| Shared acceptance evidence | `12_final_supplemental_experiments/minimal_acceptance/`、`12_final_supplemental_experiments/track1_load/`、`12_final_supplemental_experiments/track2_fallback/` | 用于说明三赛道统一验收入口与复现边界，不作为 Track 3 主结论证据 |
| Cross-track integration evidence | `13_sciverse_integration/`、`11_throughput/` | 用于说明 Sciverse 医学扩展与统一吞吐基准；具体医疗 RAG 结论以本表 primary evidence 为准 |

## License

CC-BY-4.0。医学公开数据版权归原始来源所有。
