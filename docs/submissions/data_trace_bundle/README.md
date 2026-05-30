# DATA-TRACE Bundle — 可复现溯源资产集中导航

本目录是 [DATA-TRACE.md](../shared/DATA-TRACE.md) 的配套数据包。
所有文件均从项目仓库中以**复制**方式采集（源文件未移动），按报告章节分组。

## 结构

| 子目录 | DATA-TRACE 章节 | 内容 |
|:--|:--|:--|
| `01_corpus_scale/` | 一 / 十四 | 语料规模统计与 MinerU/PyMuPDF 扫描教材文档入口对比 (#1-16, #137) |
| `02_benchmark/` | 二 | Benchmark 数据集与跨模态索引 (#17-23) |
| `03_leaderboard/` | 四 | 排行榜、评测结果与修订清单 (#38-42, #106-108) |
| `04_qlora_ppl/` | 五 | QLoRA 微调 & PPL (#47-54) |
| `05_cross_modal/` | 六 | 跨模态对齐审计 (#55-58) |
| `06_visual_audit/` | 八 | MiMo 全量视觉审计 (#71) |
| `07_flywheel/` | 七 | Agent 能力配置、飞轮日志与原始文献 (#22, #59-64) |
| `08_think_probe/` | 八 | Think 模式对照实验 (#75) |
| `09_medical_rag/` | 十一 | 赛道三 Medical RAG 与合成 smoke (#88-105, #117-120) |
| `09_medical_rag_large/` | 十一 | 医疗 RAG 原始索引与检索缓存 |
| `10_charts/` | 十 | 嵌入分析 PNG 图表与提交插图 manifest (#79-86) |
| `10_charts_large/` | 十 | 语料嵌入矩阵缓存 |
| `11_throughput/` | 十一 / 附录性能 | GPU 吞吐与 HF embedding 短测 (#145-146) |
| `12_final_supplemental_experiments/` | 附录补充验收 | 三赛道最小入口、Track1 本地 JSON 加载、Track2 本地 DAG dry-run、Track3 安全拒答边界 |
| `13_sciverse_integration/` | 十六 | Sciverse 覆盖、检索、跨源评测、医学闭环、排行榜与 Agent 飞轮 (#151-168) |

## 完整清单

`manifest.json` 是本数据包的文件完整性清单：记录生成时间、复制策略、总大小、每个文件的原始路径、包内路径、size 与 SHA-256。当前全量导航包由 `scripts/build_data_trace_bundle.py` 于 `2026-05-24T16:22:20` 生成，`total_size_mb=400.96`。

Manifest 只回答“证据文件是否存在且内容未漂移”，不替代实验数字的权威来源。报告中的精确数值仍以 [DATA-TRACE.md](../shared/DATA-TRACE.md) 登记的 JSON / JSONL / log 及对应复现命令为准；三赛道 final bundle 下的 manifest 另按赛道裁剪，评审应优先核验各自包内 manifest 与实体文件是否一致。

字段语义如下：`bundle_path` 表示当前数据包内的相对路径；`source_path` 表示该文件在项目仓库中的原始来源路径；`size_bytes` / `size_mb` / `sha256` 表示复制后的包内文件状态。赛道级 final bundle 继承同一语义，但只覆盖对应包内实际存在的裁剪文件。

## 排除文件

无。三份主报告和 DATA-TRACE 中引用的可定位数据源文件均已复制入本包；报告、脚本、命令、git log 等非数据源不重复复制。赛道级 final bundle 会按 Track 1 / Track 2 / Track 3 裁剪本包内容，因此其 `data_trace_bundle/README.md` 与 `manifest.json` 只描述对应赛道的 included / excluded 范围。

## 许可

CC-BY-4.0。飞轮 arXiv 论文版权归原作者所有。
