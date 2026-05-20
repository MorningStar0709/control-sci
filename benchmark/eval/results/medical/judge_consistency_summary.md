# Judge 一致性分析摘要

生成时间: 2026-05-11  
输入报告: `benchmark/eval/results/medical/kb_quality_report.json`  
输出数据: `benchmark/eval/results/medical/judge_consistency.json`

## 数据规模

- 评分矩阵: 14 Judges x 75 entry-level retrieval judgements = 1050 条潜在评分记录
- 覆盖结构: 25 queries x top-3 chunks = 75 entries
- Judge 来源: 8 API + 6 local
- 有效 overall score: 851 / 1050
- 有效四维 dimension score: 751 / 1050

注: local sample judges 覆盖 41-42 entries，API judges 覆盖 75 entries；因此一致性分析保留缺失值，并按 Krippendorff's alpha 的 missing-rating 语义计算。

## Krippendorff's Alpha

| Model group | Overall alpha | Relevance | Completeness | Traceability | Accuracy |
|:--|--:|--:|--:|--:|--:|
| all 14 judges | 0.4616 | 0.6813 | 0.6441 | 0.4581 | 0.5040 |
| API 8 judges | 0.5487 | 0.8421 | 0.7546 | 0.4702 | 0.6175 |
| local 6 judges | 0.4292 | 0.6087 | 0.5837 | 0.5140 | 0.5277 |

结论: API 组一致性最高，尤其 relevance alpha=0.8421、completeness alpha=0.7546；全体 14 源在 relevance/completeness 上具备较强一致性，在 traceability 上分歧最大。

## Dimension Correlation

| Dimension pair | Pearson | Spearman | n |
|:--|--:|--:|--:|
| relevance vs completeness | 0.6872 | 0.7020 | 751 |
| relevance vs traceability | 0.6418 | 0.6762 | 751 |
| relevance vs accuracy | 0.7346 | 0.7311 | 751 |
| completeness vs traceability | 0.5700 | 0.5938 | 751 |
| completeness vs accuracy | 0.5814 | 0.6012 | 751 |
| traceability vs accuracy | 0.7638 | 0.7821 | 751 |

结论: traceability 与 accuracy 相关最高，说明引用可溯性和事实准确性在 Judge 判断中高度同向；completeness 与 traceability 的相关最低，说明完整性和证据链覆盖仍是两个可区分维度。

## Bootstrap Overall Ranking CI

Bootstrap: 10000 resamples, 95% CI, rank 1 = best.

| Rank | Judge | Mean score | 95% rank CI |
|--:|:--|--:|:--|
| 1 | gemma3:4b | 0.5119 | [1.0, 1.0] |
| 2 | llama3.2:3b | 0.3690 | [2.0, 7.0] |
| 3 | qwen3.5:35b | 0.3049 | [2.0, 8.0] |
| 4 | mimo-v2.5 | 0.3033 | [2.0, 6.0] |
| 5 | mm-m2.5 | 0.2967 | [2.0, 7.0] |
| 6 | mm-m2.7 | 0.2867 | [3.0, 8.0] |
| 7 | mimo-v2-pro | 0.2633 | [5.0, 9.0] |
| 8 | mimo-v2.5-pro | 0.2400 | [6.0, 11.0] |
| 9 | qwen3.5:9b | 0.2202 | [5.0, 13.0] |
| 10 | qwen3.5:4b | 0.2083 | [7.0, 13.0] |
| 11 | mimo-v2-flash | 0.2033 | [9.0, 13.0] |
| 12 | qwen3.5:2b | 0.1905 | [7.0, 13.0] |
| 13 | ds-v4-flash | 0.1633 | [9.0, 13.0] |
| 14 | ds-v4-pro | 0.0400 | [14.0, 14.0] |

结论: gemma3:4b 在当前 scoring scale 下排名稳定第一；第 2-6 名置信区间重叠明显，报告中应描述为第二梯队而非硬性单点排序。
