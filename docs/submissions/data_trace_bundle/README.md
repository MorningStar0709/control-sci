# DATA-TRACE Bundle — ControlSci 公开数据溯源包

本目录包含 ControlSci 项目三份技术报告（Track 1 科学对齐 / Track 2 智能体 / Track 3 医疗 RAG）中所有定量声明的原始数据文件，按报告章节分组组织。评审方可直接在此目录内查找、验证各报告所引用的数据来源。

> 所有文件均从项目仓库复制采集（源文件未移动），SHA-256 校验值见 `manifest.json`。

---

## 快速导航

| 子目录 | 对应报告章节 | 涉及赛道 | 文件数 | 内容概要 |
|:--|:--|:--|--:|:--|
| `01_corpus_scale/` | 语料规模统计 | T1, T2 | 8 | 语料文档数、chunk 数、公式/图片统计、嵌入分析 |
| `02_benchmark/` | Benchmark 数据集 | T1, T2 | 2 | 500 题核心评测集 + 15 题飞轮集 |
| `03_leaderboard/` | 排行榜 & 评测结果 | T1, T2 | 3 | 模型得分排行、9B 逐题评测明细、答案缓存 |
| `04_qlora_ppl/` | QLoRA 微调 & PPL | T1, T2 | 5 | 微调模型评测报告、困惑度对比、训练状态 |
| `05_cross_modal/` | 跨模态对齐审计 | T1 | 1 | 图文共现 chunk 的语义一致性抽样审计 |
| `06_visual_audit/` | MiMo 全量视觉审计 | T2 | 1 | MiMo-V2.5 对 4,996 共现 chunk 的逐条判决 |
| `07_flywheel/` | 数据飞轮 | T2 | 7 | 5 篇 arXiv 原始 PDF + 评测结果 + 进度日志 |
| `08_think_probe/` | Think 模式对照实验 | T1, T2 | 1 | 35B 模型思考模式对评分影响的对照实验 |
| `09_medical_rag/` | Medical RAG | T3 | 7 | 医学 QA、视觉检索、质量控制和速度探针 |
| `10_charts/` | 嵌入分析可视化 | T1, T2 | 4 | PCA / 文档相似度 / Train-Eval 散点图 |

---

## 各子目录详细说明

### `01_corpus_scale/` — 语料规模与嵌入分析

| 文件 | 关键字段 | 说明 |
|:--|:--|:--|
| `metadata.json` | `total_docs`, `textbooks`, `arxiv_papers` | 语料构成：362 文档（23 教材 + 339 arXiv） |
| `corpus_stats.json` | `total_chunks`, `total_formulas`, `total_images`, `total_tokens_estimated` | Chunk 级语料统计（~28K chunks, ~19.7M tokens） |
| `multimodal_chunks.json` | `total_chunks_on_disk`, `chunks_with_image`, `chunks_with_formula`, `chunks_with_both` | 多模态 chunk 统计，含图文共现权威口径 |
| `image_formula_cooccurrence.json` | `has_both`, `has_both_pct`, `subdomains` | 旧口径图文共现率（17.3%）及 14 子领域分布 |
| `a1_global_pca.json` | `pca_variance_explained`, `doc_type_counts`, `control_category_top8`, `centroid_distance_textbook_vs_arxiv` | PCA 嵌入分析：PC1=3.97%, 教材/arXiv 质心距离=0.224 |
| `a2_doc_similarity.json` | `similarity_stats`（textbook_textbook / arxiv_arxiv / cross_type）, `top20_pairs` | 文档间余弦相似度（教材均值为 0.802，远高于 arXiv） |
| `a3_redundancy.json` | `redundant_pairs_total`, `same_doc_redundant`, `cross_doc_redundant`, `top_same_doc_sample` | 冗余检测（cos≥0.95 阈值下 1,013 对），含采样明细 |
| `a4_train_eval.json` | `n_train`, `n_eval`, `split_ratio_actual`, `centroid_cosine`, `mmd_rbf`, `mmd_p_value` | Train/Eval 划分一致性（质心 cos=0.9932, MMD=0.0023） |

### `02_benchmark/` — 评测数据集

| 文件 | 关键字段 | 说明 |
|:--|:--|:--|
| `core.json` | `meta.total_questions`（500）, `questions[]`（含 dimension / difficulty_level / question / answer / reasoning_steps） | 四维（A/B/C/D）各 125 题，难度 L1-L4，含标准答案与推理链 |
| `flywheel_filtered.json` | `[]`（15 个 question 对象） | 从 5 篇 arXiv 论文生成的 15 道飞轮附加题 |

### `03_leaderboard/` — 排行榜与评测结果

| 文件 | 关键字段 | 说明 |
|:--|:--|:--|
| `leaderboard.json` | `models[]`（含 overall_score / dimension_scores / total_questions） | 多模型排行榜，deepseek-v4-flash 在 500 题上得分 0.6431 |
| `qwen3.5_9b_target_eval.json` | `overall_score`, `dimension_scores`, `records[]`（含逐题 score / reason / model_answer / expected_answer） | Qwen3.5-9B 的 500 题逐题评测（overall=0.5991），含完整 answer 与 Judge 理由 |
| `qwen3.5_9b_answers.jsonl` | JSONL 逐行：question_id / model_answer | Qwen3.5-9B 对 500 题的原始回答缓存 |

### `04_qlora_ppl/` — QLoRA 微调与困惑度

| 文件 | 关键字段 | 说明 |
|:--|:--|:--|
| `eval_finetuned_report.json` | `overall_score`, `dimension_scores`, `baseline`, `delta_vs_baseline` | QLoRA 4B 微调后评测（overall=0.4635, Δ=-0.1614 vs 9B baseline） |
| `eval_baseline_4b_report.json` | `overall_score`, `baseline_9b` | 4B 未微调基线评测（overall=0.4669, 与 9B baseline 对照） |
| `perplexity_delta.json` | `base_avg_ppl`（8.4）, `qlora_avg_ppl`（3.9）, `delta_percent`（-53.6%） | QLoRA 4B 微调前后 PPL 变化，含逐题明细 |
| `perplexity_delta_9b.json` | `base_avg_ppl`（6.48）, `qlora_avg_ppl`（4.0）, `delta_percent`（-38.3%） | QLoRA 9B 微调前后 PPL 变化，含逐题明细 |
| `training.status.json` | `status`, `step`, `epoch`, `eval_loss` | QLoRA 训练运行状态（89 steps, eval_loss=0.853） |

### `05_cross_modal/` — 跨模态对齐审计

| 文件 | 关键字段 | 说明 |
|:--|:--|:--|
| `cross_modal_audit_summary.json` | `stats`（consistent=75.9%, alignment_quality=79.3%）, `detailed_results` | MiniMax-VL 对 4,996 图文共现 chunk 的 29 个分层抽样审计结果 |

### `06_visual_audit/` — MiMo 全量视觉审计

| 文件 | 关键字段 | 说明 |
|:--|:--|:--|
| `visual_audit_results.jsonl` | JSONL 逐行：judgment（consistent/inconsistent）, token_usage, chunk_id | MiMo-V2.5 对 4,996 图文共现 chunk 的逐条自动判决（含推理理由 + token 消耗） |

### `07_flywheel/` — 数据飞轮

| 文件 | 说明 |
|:--|:--|
| `flywheel_eval_deepseek.json` | DeepSeek 对 15 道飞轮题的评测结果（overall=0.14），含逐题 score、reason、issues |
| `flywheel_progress_deepseek.jsonl` | JSONL 格式的飞轮评测进度日志 |
| `2605.02370.pdf` 等 5 篇 PDF | 飞轮测试集的 5 篇 arXiv 原始论文（版权归原作者所有） |

### `08_think_probe/` — Think 模式对照实验

| 文件 | 关键字段 | 说明 |
|:--|:--|:--|
| `think_probe_35b_10queries.json` | `summary`（delta_mean=0.195）, `records[]`（含 score / baseline_score / delta / thinking_len） | Qwen3.5-35B 在 10 道题上的 think=true 对比实验，验证开放思考是否影响评分严苛度 |

### `09_medical_rag/` — 赛道三 Medical RAG

| 文件 | 关键字段 | 说明 |
|:--|:--|:--|
| `qa_output.json` | `meta.total_qa_pairs`（11）, `qa_pairs[]`（含 question / output / consistency / sources） | Medical RAG 跨文献证据合成的 QA 格式化输出 |
| `vision_ab_comparison.json` | 8 类医学视觉查询（血糖趋势图/生存曲线/流程图等）的 text / vision / combined 对比 | 纯文本检索 vs 视觉注入检索的 AB 对比，含 top-5 命中详情 |
| `vision_chunks_manifest.json` | `total_vision_chunks`（730） | MiMo-V2.5 视觉描述 FAISS 索引清单 |
| `vision_descriptions.jsonl` | JSONL 逐行：image_id / description | MiniMax-VL 生成的医学图片语义描述 |
| `vision_descriptions_qwen35.jsonl` | JSONL 逐行：image_id / description | Qwen3.5-35B 生成的医学图片语义描述 |
| `vision_quality_control.json` | `total_references`（947）, `filtered_ratio_pct`, `probe_verified_types` | 视觉 chunk 质量控制：947 张参考图，过滤 11.9% 的低质量图片 |
| `medbench_35b_speed_probe.json` | `statistics`（total_questions=3, overall_avg_hits=5.0）, `per_question[]` | MedBench 自评测速度探针（CMB-Clin-extended 子集） |

### `10_charts/` — 嵌入分析可视化

| 文件 | 说明 |
|:--|:--|
| `a1_global_pca.png` | PCA 主成分分析散点图（PC1=3.97%, PC2=3.76%） |
| `a2_doc_similarity.png` | 文档相似度分布图（默认视图） |
| `a2_doc_similarity_full.png` | 文档相似度全量清晰版 |
| `a4_train_eval.png` | Train/Eval 分布一致性散点图（质心 cos=0.9932） |

---

## 排除文件

以下大型衍生文件因可重新生成而未包含在本包中：

| 文件 | 大小 | 重新生成方式 |
|:--|--:|:--|
| `embeddings_cache.npy` | 278 MB | 运行 chunk 嵌入分析脚本 |
| `medical.index` | 33 MB | 重建 Medical RAG 索引 |
| `embeddings_cache.npy`（medical） | 33 MB | 同上 |
| `bm25.pkl` | 17 MB | 同上 |

## 许可

CC-BY-4.0。`07_flywheel/` 中的 arXiv 论文版权归原作者所有。
