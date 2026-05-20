# DATA-TRACE: ControlSci 全量数字可追溯索引

> **用途**：三份赛道技术报告中每个定量声明的单一权威源 + 可复现命令。
> **共享**：`docs/submissions/track1_sci_align_report.md` / `track2_agent_report.md` / `track3_medical_rag_report.md`
> **规范**：每个数字只指向一个权威源文件，若多个源文件有同一字段则优先使用权威口径。
> **更新**：2026-05-17 | **审计**：✅ 已修复 10 项不可验证条目；新增 Task3 多索引 RAG 评测与合成闭环溯源；补充 Track1 中间报告回源条目；新增补充验收记录

### DATA-TRACE 条目准入规则

1. 每个条目必须有一个可定位到磁盘的源文件
2. 每个数字必须在源文件中可直接读取（不能是"源文件里没有，我算出来的"——如果确需计算，源文件必须包含所有计算因子）
3. 禁止"合计估算"——如果数字是多个子项的和，每个子项必须各自有源文件
4. 工程 meta 数据（commit 数、审查轮次、人力消耗）不进入 DATA-TRACE
5. Markdown 分析报告、截图和 PNG 图表只能作为导航或展示产物；若报告中出现具体数值，DATA-TRACE 必须指向其背后的 JSON/JSONL、原始 PDF/Markdown、运行日志或可复算脚本。
6. 带 `~`、`约`、`<`、`≈` 的工程成本/耗时/token 可以作为估算项进入清单，但必须保留估算符号，并写明公式、因子或逐条日志；不得把估算项改写为精确实验观测。
7. 非核心过程指标（如工程耗时、成本、token、人工记录的 CLI 输出）若为当次实测但 stdout/stderr 未单独归档，可标为“工程实测记录值”；应写明记录来源与可交叉验证产物。只有数值本身无法定位时，才移出权威清单或改为非定量描述。

---

## 一、语料规模（赛道一 §2 / 赛道二 §2）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 1 | §2.1 文档总数 | 362 | `corpus/metadata.json` L5 | `conda run -n myenv python -c "import json; print(json.load(open(r'corpus/metadata.json',encoding='utf-8'))['total_docs'])"` | ✅ |
| 2 | §2.1 教材数 | 23 | `corpus/metadata.json` L6 | `conda run -n myenv python -c "import json; print(json.load(open(r'corpus/metadata.json',encoding='utf-8'))['textbooks'])"` | ✅ |
| 3 | §2.1 arXiv 论文数 | 339 | `corpus/metadata.json` L7 | `conda run -n myenv python -c "import json; print(json.load(open(r'corpus/metadata.json',encoding='utf-8'))['arxiv_papers'])"` | ✅ |
| 4 | §2.2 磁盘 glob chunk 数 | 28,514 | `benchmark/eval/results/multimodal_chunks.json` L8 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/multimodal_chunks.json',encoding='utf-8'))['total_chunks_on_disk'])"` | ✅ |
| 5 | §2.2 manifest chunk 数 | 28,475 | `corpus/stats/corpus_stats.json` L8 | `conda run -n myenv python -c "import json; print(json.load(open(r'corpus/stats/corpus_stats.json',encoding='utf-8'))['total_chunks'])"` | ✅ |
| 6 | §2.2 train/eval split (manifest) | 22,635 / 5,840 | `benchmark/eval/results/chunk_embedding/a4_train_eval.json` L3-L4 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a4_train_eval.json')); print('train:', d['n_train'], 'eval:', d['n_eval'])"` | ✅ |
| 7 | §2.2 chunks w/ image | 6,204 | `benchmark/eval/results/multimodal_chunks.json` L9 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/multimodal_chunks.json',encoding='utf-8'))['chunks_with_image'])"` | ✅ |
| 8 | §2.2 chunks w/ formula | 19,748 | `benchmark/eval/results/multimodal_chunks.json` L10 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/multimodal_chunks.json',encoding='utf-8'))['chunks_with_formula'])"` | ✅ |
| 9 | §2.2 chunks w/ both (权威口径) | 4,996 (17.52%) | `benchmark/eval/results/multimodal_chunks.json` L11-L12 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/multimodal_chunks.json',encoding='utf-8')); print(d['chunks_with_both'], d['both_pct'])"` | ✅ |
| 10 | §2.2 chunks w/ both (旧口径) | 4,935 | `benchmark/eval/results/image_formula_cooccurrence.json` | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/image_formula_cooccurrence.json',encoding='utf-8'))['has_both'])"` | ✅ |
| 11 | §2.2 总公式数 | 253,012 | `corpus/stats/corpus_stats.json` L3 | `conda run -n myenv python -c "import json; print(json.load(open(r'corpus/stats/corpus_stats.json',encoding='utf-8'))['total_formulas'])"` | ✅ |
| 12 | §2.2 行内/块级公式 | 196,127 / 56,885 | `corpus/stats/corpus_stats.json` L4-L5 | `conda run -n myenv python -c "import json; d=json.load(open(r'corpus/stats/corpus_stats.json',encoding='utf-8')); print(d['total_inline_formulas'], d['total_block_formulas'])"` | ✅ |
| 13 | §2.2 总图片数 | 11,554 | `corpus/stats/corpus_stats.json` L6 | `conda run -n myenv python -c "import json; print(json.load(open(r'corpus/stats/corpus_stats.json',encoding='utf-8'))['total_images'])"` | ✅ |
| 14 | §2.2 估计 token 数 | 19,671,465 | `corpus/stats/corpus_stats.json` L9 | `conda run -n myenv python -c "import json; print(json.load(open(r'corpus/stats/corpus_stats.json',encoding='utf-8'))['total_tokens_estimated'])"` | ✅ |
| 15 | §2.2 Top-1 学科 chunk 数 | 最优控制 5,375 | `benchmark/eval/results/chunk_embedding/a1_global_pca.json` 第12行起 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a1_global_pca.json')); print(d['control_category_top8'][0]['category'], d['control_category_top8'][0]['count'])"` | ✅ |
| 16 | §2.2 教材 chunk / arXiv chunk | 13,759 / 14,716 | `benchmark/eval/results/chunk_embedding/a1_global_pca.json` L9-L11 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a1_global_pca.json')); print(d['doc_type_counts'])"` | ✅ |

---

## 二、Benchmark 设计（赛道一 §3 / 赛道二 §2）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 17 | §3.1 总题数 | 500 | `benchmark/dataset/core.json` meta.total_questions | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/dataset/core.json',encoding='utf-8'))['meta']['total_questions'])"` | ✅ |
| 18 | §3.1 四维各 125 题 | A=125, B=125, C=125, D=125 | `benchmark/dataset/core.json` questions[].dimension | `conda run -n myenv python -c "import json; from collections import Counter; d=json.load(open(r'benchmark/dataset/core.json',encoding='utf-8')); print(Counter(q['dimension'] for q in d['questions']))"` | ✅ |
| 19 | §3.1 难度分布 | L1=40, L2=153, L3=163, L4=144 | `benchmark/dataset/core.json` questions[].difficulty_level | `conda run -n myenv python -c "import json; from collections import Counter; d=json.load(open(r'benchmark/dataset/core.json',encoding='utf-8')); print(dict(Counter(q['difficulty_level'] for q in d['questions'])))"` | ✅ |
| 20 | §3.3 飞轮题数 | 15 | `benchmark/dataset/flywheel_filtered.json` | `conda run -n myenv python -c "import json; print(len(json.load(open(r'benchmark/dataset/flywheel_filtered.json',encoding='utf-8'))))"` | ✅ |
| 21 | §3.3 合并总题数 | 515 | `benchmark/eval/results/leaderboard.json` models[-1].total_questions | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/leaderboard.json')); print(d['models'][-1]['total_questions'])"` | ✅ |
| 22 | §3.3 飞轮 arXiv 论文来源 | 5 篇 | `data/sources_flywheel/` 目录 | `powershell -c "(Get-ChildItem data/sources_flywheel/*.pdf).Count"` | ✅ |
| 23 | §3.3 飞轮 chunk 数 | 47 | `data/sources_flywheel/md/*.md` + `data/sources_flywheel/run_flywheel.py::chunk_papers` | `conda run -n myenv python data/sources_flywheel/run_flywheel.py --dry-run --skip-gen --skip-filter --skip-eval` | ✅ |

---

## 三、嵌入分析 A1-A4（赛道一 §2 / 赛道二 §2）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 24 | A1 PC1 解释方差 | 3.97% | `benchmark/eval/results/chunk_embedding/a1_global_pca.json` L6 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a1_global_pca.json')); print('PC1:', d['pca_variance_explained'][0], 'PC2:', d['pca_variance_explained'][1])"` | ✅ |
| 25 | A1 PC1+PC2 | 7.73% | `benchmark/eval/results/chunk_embedding/a1_global_pca.json` L6 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a1_global_pca.json')); print('PC1+PC2:', sum(d['pca_variance_explained']))"` | ✅ |
| 26 | A1 textbook↔arxiv 质心距离 | 0.224 | `benchmark/eval/results/chunk_embedding/a1_global_pca.json` L47 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/chunk_embedding/a1_global_pca.json'))['centroid_distance_textbook_vs_arxiv'])"` | ✅ |
| 27 | A2 textbook-textbook mean cos | 0.8022 | `benchmark/eval/results/chunk_embedding/a2_doc_similarity.json` L6 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a2_doc_similarity.json')); print(d['similarity_stats']['textbook_textbook']['mean'])"` | ✅ |
| 28 | A2 arxiv-arxiv mean cos | 0.5872 | `benchmark/eval/results/chunk_embedding/a2_doc_similarity.json` L12 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a2_doc_similarity.json')); print(d['similarity_stats']['arxiv_arxiv']['mean'])"` | ✅ |
| 29 | A2 cross-type mean cos | 0.6214 | `benchmark/eval/results/chunk_embedding/a2_doc_similarity.json` L18 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a2_doc_similarity.json')); print(d['similarity_stats']['cross_type']['mean'])"` | ✅ |
| 30 | A2 Top-1 论文对 cos | 0.9819 | `benchmark/eval/results/chunk_embedding/a2_doc_similarity.json` L32 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a2_doc_similarity.json')); print(d['top20_pairs'][0]['cosine_similarity'])"` | ✅ |
| 31 | A3 冗余对总数 (cos≥0.95) | 1,013 | `benchmark/eval/results/chunk_embedding/a3_redundancy.json` L7 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/chunk_embedding/a3_redundancy.json'))['redundant_pairs_total'])"` | ✅ |
| 32 | A3 同文档冗余 | 248 | `benchmark/eval/results/chunk_embedding/a3_redundancy.json` L8 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/chunk_embedding/a3_redundancy.json'))['same_doc_redundant'])"` | ✅ |
| 33 | A3 跨文档冗余 | 765 | `benchmark/eval/results/chunk_embedding/a3_redundancy.json` L9 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/chunk_embedding/a3_redundancy.json'))['cross_doc_redundant'])"` | ✅ |
| 34 | A3 cos=1.000 完全重复对 | 抽样确认 | `benchmark/eval/results/chunk_embedding/a3_redundancy.json` top-10 samples | 全量精确计数需重跑语义查重；10 对完全重复为抽样核查结论，不作为精确总数声明 | ⚠️ 抽样结论，不作权威总数 |
| 35 | A4 Train 质心 cos | 0.9932 | `benchmark/eval/results/chunk_embedding/a4_train_eval.json` L6 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/chunk_embedding/a4_train_eval.json'))['centroid_cosine'])"` | ✅ |
| 36 | A4 MMD | 0.0018 (rbf) / p=0.0 | `benchmark/eval/results/chunk_embedding/a4_train_eval.json` | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/chunk_embedding/a4_train_eval.json')); print('mmd_rbf:', d['mmd_rbf'], 'mmd_p_value:', d['mmd_p_value'])"` | ✅ |
| 37 | A4 split ratio | 0.7949 (79.5%) | `benchmark/eval/results/chunk_embedding/a4_train_eval.json` L5 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/chunk_embedding/a4_train_eval.json'))['split_ratio_actual'])"` | ✅ |

---

## 四、赛道一 Leaderboard & Judge（赛道一 §4 / 赛道二 §4）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 38 | §4.1 deepseek-v4-flash 500题 | 0.6431 | `benchmark/eval/results/leaderboard.json` models[2].overall_score | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/leaderboard.json')); print(d['models'][2]['overall_score'])"` | ✅ |
| 39 | §4.1 deepseek-v4-flash 维度分 | A=0.7104, B=0.5984, C=0.622, D=0.6414 | `benchmark/eval/results/leaderboard.json` models[2].dimension_scores | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/leaderboard.json')); print(d['models'][2]['dimension_scores'])"` | ✅ |
| 40 | §4.1 deepseek-v4-flash 飞轮 15 题 | 0.1400 | `benchmark/eval/results/leaderboard.json` models[4].overall_score | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/leaderboard.json')); print(d['models'][4]['overall_score'])"` | ✅ |
| 41 | §4.1 合并 500+15 | 0.6284 (515题) | `benchmark/eval/results/leaderboard.json` models[5].overall_score | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/leaderboard.json')); print(d['models'][-1]['overall_score'], d['models'][-1]['total_questions'])"` | ✅ |
| 42 | §4.1 飞轮 vs 基准差距 | 4.6× (0.14 vs 0.6431) | `benchmark/eval/results/leaderboard.json` models[2] vs models[4] | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/leaderboard.json')); print(round(d['models'][2]['overall_score']/d['models'][4]['overall_score'],1))"` | ✅ |

---

---

## 五、QLoRA & PPL（赛道一 §4 / 赛道二 §4）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 47 | §5.1 QLoRA 4B 评测题数 | 89 | `finetune/output/eval_finetuned_report.json` L4 | `conda run -n myenv python -c "import json; d=json.load(open(r'finetune/output/eval_finetuned_report.json')); print(d['total_questions'])"` | ✅ |
| 48 | §5.1 QLoRA 4B overall | 0.4635 | `finetune/output/eval_finetuned_report.json` L5 | `conda run -n myenv python -c "import json; d=json.load(open(r'finetune/output/eval_finetuned_report.json')); print(d['overall_score'])"` | ✅ |
| 49 | §5.1 baseline 9B overall | 0.6249 | `finetune/output/eval_finetuned_report.json` L15 | `conda run -n myenv python -c "import json; d=json.load(open(r'finetune/output/eval_finetuned_report.json')); print(d['baseline']['overall_score'])"` | ✅ |
| 50 | §5.1 Δ vs baseline | -0.1614 | `finetune/output/eval_finetuned_report.json` L22 | `conda run -n myenv python -c "import json; print(json.load(open(r'finetune/output/eval_finetuned_report.json'))['delta_vs_baseline'])"` | ✅ |
| 51 | §5.2 Base avg PPL | 8.4 | `finetune/output/perplexity_delta.json` L7 | `conda run -n myenv python -c "import json; print(json.load(open(r'finetune/output/perplexity_delta.json'))['base_avg_ppl'])"` | ✅ |
| 52 | §5.2 QLoRA avg PPL | 3.9 | `finetune/output/perplexity_delta.json` L8 | `conda run -n myenv python -c "import json; print(json.load(open(r'finetune/output/perplexity_delta.json'))['qlora_avg_ppl'])"` | ✅ |
| 53 | §5.2 PPL 降幅 (4B) | -53.6% | `finetune/output/perplexity_delta.json` L9 | `conda run -n myenv python -c "import json; print(json.load(open(r'finetune/output/perplexity_delta.json'))['delta_percent'])"` | ✅ |
| 53b | §5.2 PPL 降幅 (9B) | -38.3% | `finetune/output/perplexity_delta_9b.json` L8 | `conda run -n myenv python -c "import json; print(json.load(open(r'finetune/output/perplexity_delta_9b.json'))['delta_percent'])"` | ✅ |
| 54 | §5.3 C 维 QLoRA-4B 幸存 | ΔC=+0.0000（四维中最佳） | `finetune/output/eval_baseline_4b_report.json` + `finetune/output/eval_finetuned_report.json` | `conda run -n myenv python -c "import json; d4b=json.load(open(r'finetune/output/eval_baseline_4b_report.json')); dft=json.load(open(r'finetune/output/eval_finetuned_report.json')); deltas={k:round(dft['dimension_scores'][k]-d4b['dimension_scores'][k],4) for k in d4b['dimension_scores']}; print(min(deltas,key=lambda k:abs(deltas[k])), deltas)"` | ✅ |

---
## 五-B、Qwen3.5-9B 补充重跑（赛道一 §6.5 追踪）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 106 | §6.5 补充重跑 overall | 0.5991 (500题, vs 原始 0.6250 Δ=-0.0259) | `benchmark/eval/results/qwen3.5_9b_target_eval.json` | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/qwen3.5_9b_target_eval.json')); print('overall:', d['overall_score'], 'A:', d['dimension_scores']['A'], 'B:', d['dimension_scores']['B'], 'C:', d['dimension_scores']['C'], 'D:', d['dimension_scores']['D'])"` | ✅ |
| 107 | §6.5 补充重跑参数 | num_ctx=3072, max_tokens=2500, judge=deepseek-v4-flash | `benchmark/eval/results/qwen3.5_9b_target_eval.json` metadata | 见 #106 | ✅ |
| 108 | §6.5 补充重跑原始答案 | 500 题逐题答案 jsonl | `benchmark/eval/results/qwen3.5_9b_answers.jsonl` | `powershell -c "(Get-Content benchmark/eval/results/qwen3.5_9b_answers.jsonl \| Measure-Object -Line).Lines"` | ✅ |

---

## 六、跨模态对齐审计（赛道一 §3.5 / 赛道二 §2）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 55 | §3.5 抽样群体 | 4,996 | `benchmark/eval/results/cross_modal_audit_summary.json` L6 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/cross_modal_audit_summary.json'))['config']['population'])"` | ✅ |
| 56 | §3.5 一致率 (consistent) | 75.9% | `benchmark/eval/results/cross_modal_audit_summary.json` L12 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/cross_modal_audit_summary.json'))['stats']['consistent_pct'])"` | ✅ |
| 57 | §3.5 综合对齐质量 | 79.3% | `benchmark/eval/results/cross_modal_audit_summary.json` L18 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/cross_modal_audit_summary.json'))['stats']['alignment_quality'])"` | ✅ |
| 58 | §3.5 不一致率 | 20.7% | `benchmark/eval/results/cross_modal_audit_summary.json` L15 | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/cross_modal_audit_summary.json'))['stats']['inconsistent_pct'])"` | ✅ |

---

## 七、D 数据飞轮（赛道一 §4 / 赛道二 §3）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 59 | §3.3 飞轮耗时 | 391s | `benchmark/agent/agent_report.md §3.4` 与 `docs/submissions/shared/track2_agent_20_cases.md` 记录该值来自 CLI 输出；`benchmark/agent/logs/demo-data-flywheel.json`、`benchmark/dataset/flywheel_filtered.json`、`benchmark/eval/results/flywheel_eval_deepseek.json` 可交叉验证执行产物完整 | `select-string benchmark/agent/agent_report.md -Pattern "391 秒"`；另核 `benchmark/agent/logs/*.json` 无 380-402s 结构化 wall-time 字段 | ✅ 工程实测记录值；stdout/stderr 未单独归档 |
| 60 | §3.3 飞轮 5 PDF 论文 ID | 2605.02370, 2605.03662, 2605.05182, 2605.05575, 2605.06630 | `data/sources_flywheel/` 目录 | `powershell -c "Get-ChildItem data/sources_flywheel/*.pdf \| Select-Object Name"` | ✅ |
| 61 | §3.3 飞轮 15 题各维度分 | A=0.15, B=0.05, C=0.25, D=0.1875 | `benchmark/eval/results/leaderboard.json` models[4].dimension_scores | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/leaderboard.json')); print(d['models'][4]['dimension_scores'])"` | ✅ |
| 62 | §3.3 飞轮 empty_answer | 3 | `benchmark/eval/results/leaderboard.json` models[4].failure_summary | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/leaderboard.json')); print(d['models'][4]['failure_summary'])"` | ✅ |
| 63 | §3.3 飞轮 wrong_core_concept | 12 | `benchmark/eval/results/leaderboard.json` models[4].failure_summary | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/leaderboard.json')); print(d['models'][4]['failure_summary'])"` | ✅ |
| 64 | §3.3 飞轮空回答题数 | 4 | `benchmark/eval/results/flywheel_eval_deepseek.json` | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/flywheel_eval_deepseek.json')); empties=[r['question_id'] for r in d['results'] if r['answer'].strip()=='']; print('count:', len(empties), 'ids:', empties)"` | ✅ |

---

## 八、工程纪实（赛道二 §5）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 65 | §5.1 agent_cli.py 行数 | 1,464 | `benchmark/agent/agent_cli.py` | `conda run -n myenv powershell -c "(Get-Content benchmark/agent/agent_cli.py \| Measure-Object -Line).Lines"` | ✅ (实测 1,464) |
| 66 | §5.1 resource_scheduler.py 行数 | 662 | `benchmark/agent/resource_scheduler.py` | `conda run -n myenv powershell -c "(Get-Content benchmark/agent/resource_scheduler.py \| Measure-Object -Line).Lines"` | ✅ (实测 662) |
| 67 | §5.1 visual_audit.py 行数 | 520 | `benchmark/agent/visual_audit.py` | `conda run -n myenv powershell -c "(Get-Content benchmark/agent/visual_audit.py \| Measure-Object -Line).Lines"` | ✅ (实测 520) |
| 68 | §5.1 chunk_embedding_analysis.py 行数 | 697 | `benchmark/eval/chunk_embedding_analysis.py` | `conda run -n myenv powershell -c "(Get-Content benchmark/eval/chunk_embedding_analysis.py \| Measure-Object -Line).Lines"` | ✅ (实测 697) |
| 69 | §5.1 Git commits | 78 | git log | `git log --oneline \| measure-object \| % { $_.Count }` | 🚫 工程 meta，按准入规则不进入权威数字 |
| 70 | §5.1 API Token — DeepSeek 评测 | ~450K | evaluate 管线日志 + checkpoint 累计 | 逐次评测累计 | ✅ 估算/累计口径，正文需保留 `~` |
| 71 | §5.1 API Token — MiMo 视觉审计 | ~11.1M (9,227 images) | `benchmark/agent/results/visual_audit_results.jsonl` token_usage 逐行求和 | `conda run -n myenv python -c "import json; lines=[l for l in open(r'benchmark/agent/results/visual_audit_results.jsonl',encoding='utf-8') if l.strip()]; total=sum(json.loads(l).get('token_usage',{}).get('prompt_tokens',0)+json.loads(l).get('token_usage',{}).get('completion_tokens',0)+json.loads(l).get('token_usage',{}).get('image_tokens',0) for l in lines); print('records:',len(lines),'tokens:',total)"` | ✅ |
| 72 | §5.1 GPU — QLoRA 4B 训练 | ~23min | `finetune/output/qlora-qwen4b-cross/training.status.json` elapsed_min | `conda run -n myenv python -c "import json; print(json.load(open(r'finetune/output/qlora-qwen4b-cross/training.status.json',encoding='utf-8'))['elapsed_min'],'min')"` | ✅ |
| 73 | §5.1 GPU — 嵌入分析 | 已删除（无运行时日志） | — | — | — |
| 74 | §5.1 GPU — 本地 Judge 评测 | ~6h | Ollama 评测进度日志 | Judge 矩阵评估日志累计 | ✅ 估算/日志累计口径，正文需保留 `~` |
| 75 | §4.2.2 think 模式对照实验：10 题 B/D 维开思考后 Δ=+0.195 | baseline→think=true Δ_mean=0.195 | `benchmark/eval/results/think_probe_35b_10queries.json` summary.delta_mean | `conda run -n myenv python benchmark/eval/think_probe.py` | ✅ |

---

## 九、嵌入分析运行指标

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 76 | 嵌入矩阵维度 | 28,475 × 2,560 float32 | `embeddings_cache.npy` + a1_global_pca.json | `conda run -n myenv python -c "import numpy as np; e=np.load(r'benchmark/eval/results/chunk_embedding/embeddings_cache.npy'); print(e.shape, e.dtype)"` | ✅ |
| 77 | 嵌入缓存大小 | ~278 MB | `embeddings_cache.npy` | `conda run -n myenv powershell -c "(Get-Item benchmark/eval/results/chunk_embedding/embeddings_cache.npy).Length / 1MB"` | ✅ |

---

## 十、嵌入分析产出文件清单

| # | 文件 | 路径 | 状态 |
|:-:|:--|:--|:--:|
| 79 | A1 PCA 图 | `benchmark/eval/results/chunk_embedding/a1_global_pca.png` | ✅ |
| 80 | A1 PCA JSON | `benchmark/eval/results/chunk_embedding/a1_global_pca.json` | ✅ |
| 81 | A2 文档相似度图 | `benchmark/eval/results/chunk_embedding/a2_doc_similarity.png` | ✅ |
| 82 | A2 文档相似度全图 | `benchmark/eval/results/chunk_embedding/a2_doc_similarity_full.png` | ✅ |
| 83 | A2 文档相似度 JSON | `benchmark/eval/results/chunk_embedding/a2_doc_similarity.json` | ✅ |
| 84 | A3 冗余检测 JSON | `benchmark/eval/results/chunk_embedding/a3_redundancy.json` | ✅ |
| 85 | A4 Train/Eval 图 | `benchmark/eval/results/chunk_embedding/a4_train_eval.png` | ✅ |
| 86 | A4 Train/Eval JSON | `benchmark/eval/results/chunk_embedding/a4_train_eval.json` | ✅ |
| 87 | 嵌入缓存 | `benchmark/eval/results/chunk_embedding/embeddings_cache.npy` (278MB) | ✅ |

---

---

## 十一、赛道三 Medical RAG（赛道三 §2-§4）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|---:|:--|:--|:--:|
| 88 | §2 医学文献数 | 98 | `data/sources_medical/md/` 子目录数 | `powershell -c "(Get-ChildItem data/sources_medical/md -Directory).Count"` | ✅ |
| 89 | §2 医学 chunk 数 | 3,348 | `data/sources_medical/index/embeddings_cache.npy` shape | `conda run -n myenv python -c "import numpy as np; e=np.load(r'data/sources_medical/index/embeddings_cache.npy'); print(e.shape[0])"` | ✅ |
| 90 | §2 嵌入维度 | 2,560 | `data/sources_medical/index/embeddings_cache.npy` shape | `conda run -n myenv python -c "import numpy as np; e=np.load(r'data/sources_medical/index/embeddings_cache.npy'); print(e.shape[1])"` | ✅ |
| 91 | §2 嵌入模型 | qwen3-embedding:4b | `benchmark/eval/chunk_embedding_analysis.py` 嵌入配置 | 查阅配置文件 | ✅ |
| 92 | §2 QA 数据集 | 11 对 | `data/sources_medical/qa/qa_output.json` meta.total_qa_pairs | `conda run -n myenv python -c "import json; print(json.load(open(r'data/sources_medical/qa/qa_output.json'))['meta']['total_qa_pairs'])"` | ✅ |
| 93 | §3 混合索引 — FAISS | 3,348 × 2,560 (33 MB) | `data/sources_medical/index/medical.index` | `powershell -c "[math]::Round((Get-Item data/sources_medical/index/medical.index).Length/1MB,0)"` | ✅ |
| 94 | §3 混合索引 — BM25 | 17 MB | `data/sources_medical/index/bm25.pkl` | `powershell -c "[math]::Round((Get-Item data/sources_medical/index/bm25.pkl).Length/1MB,0)"` | ✅ |
| 95 | §3 视觉索引 — MiMo-V2.5 | 730 × 2,560 (7 MB) | `data/sources_medical/vision/vision_chunks_manifest.json` total_vision_chunks | `conda run -n myenv python -c "import json; print(json.load(open(r'data/sources_medical/vision/vision_chunks_manifest.json'))['total_vision_chunks'])"` | ✅ |
| 96 | §3 视觉描述质量控制 — 原始引用 | 947 | `data/sources_medical/vision/vision_quality_control.json` total_references | `conda run -n myenv python -c "import json; print(json.load(open(r'data/sources_medical/vision/vision_quality_control.json'))['total_references'])"` | ✅ |
| 97 | §3 视觉描述质量控制 — 过滤 <5KB | 113 (11.9%) | `data/sources_medical/vision/vision_quality_control.json` filtered_below_5kb + filtered_ratio_pct | `conda run -n myenv python -c "import json; d=json.load(open(r'data/sources_medical/vision/vision_quality_control.json')); print(d['filtered_below_5kb'], d['filtered_ratio_pct'])"` | ✅ |
| 98 | §3 视觉描述质量控制 — 保留 | 721 (76.1%) | `data/sources_medical/vision/vision_quality_control.json` retained + retained_ratio_pct | `conda run -n myenv python -c "import json; d=json.load(open(r'data/sources_medical/vision/vision_quality_control.json')); print(d['retained'], d['retained_ratio_pct'])"` | ✅ |
| 99 | §3 视觉描述生成耗时 | ~14.6 min (4线程) | `data/sources_medical/vision/vision_descriptions.jsonl` ts 逐条落盘；manifest generated_at | `conda run -n myenv python -c "import json; from datetime import datetime; rows=[json.loads(l) for l in open(r'data/sources_medical/vision/vision_descriptions.jsonl',encoding='utf-8') if l.strip()]; ts=[datetime.fromisoformat(r['ts']) for r in rows if r.get('ts')]; print(len(rows), round((max(ts)-min(ts)).total_seconds()/60,2), min(ts).isoformat(), max(ts).isoformat())"` | ✅ 估算/运行口径；逐条 ts 已落盘，正文需保留 `~` |
| 100 | §3 视觉描述 token 消耗 | ~543K (含图像输入) | `data/sources_medical/vision/vision_descriptions.jsonl` token_usage 逐条落盘 | `conda run -n myenv python -c "import json; rows=[json.loads(l) for l in open(r'data/sources_medical/vision/vision_descriptions.jsonl',encoding='utf-8') if l.strip()]; prompt=sum((r.get('token_usage') or {}).get('prompt_tokens',0) for r in rows); comp=sum((r.get('token_usage') or {}).get('completion_tokens',0) for r in rows); img=sum((r.get('token_usage') or {}).get('image_tokens',0) for r in rows); print(len(rows), prompt, comp, img, prompt+comp, prompt+comp+img)"` | ✅ 估算/分项 token_usage 已落盘；正文需保留 `~` 并说明口径 |
| 101 | §4 视觉注入 AB 对比 — 查询数 | 8 | `benchmark/eval/results/medical/vision_ab_comparison.json` key count | `conda run -n myenv python -c "import json; print(len(json.load(open(r'benchmark/eval/results/medical/vision_ab_comparison.json',encoding='utf-8'))))"` | ✅ |
| 102 | §4 视觉注入 AB 对比 — text-only top-5 含视觉 | 0/8 (0%) | `benchmark/eval/results/medical/vision_ab_comparison.json` vision_in_text_top5 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/medical/vision_ab_comparison.json')); print(sum(1 for v in d.values() if v['vision_in_text_top5']) ,'/', len(d))"` | ✅ |
| 103 | §4 视觉注入 AB 对比 — 融合后 top-3 含视觉 | 8/8 (100%) | `benchmark/eval/results/medical/vision_ab_comparison.json` combined_top5 含 vision_ 前缀 | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/medical/vision_ab_comparison.json')); print(sum(1 for q in d.values() if any('vision_' in c[0] for c in q['combined_top5'][:3])) ,'/', len(d))"` | ✅ |
| 104 | §3 MiMo 视觉描述模型 | mimo-v2.5 | `data/sources_medical/vision/vision_chunks_manifest.json` model | `conda run -n myenv python -c "import json; print(json.load(open(r'data/sources_medical/vision/vision_chunks_manifest.json'))['model'])"` | ✅ |
| 105 | §3 MedBench 自评测 — 35B 速度 | 52.8s / 3 题 | `data/sources_medical/medbench/medbench_35b_speed_probe.json` meta.elapsed_seconds | `conda run -n myenv python -c "import json; print(json.load(open(r'data/sources_medical/medbench/medbench_35b_speed_probe.json'))['meta']['elapsed_seconds'])"` | ✅ |
| 109 | §4.4 多索引 RAG 固定题集规模 | 8 queries, top-k=3 | `benchmark/eval/results/medical_rag_eval.json` cases + k | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/medical_rag_eval.json',encoding='utf-8')); print(len(d['cases']), d['k'])"` | ✅ |
| 110 | §4.4 Qwen3 Embedding Hit@3 / Label Hit@3 | 8/8, 7/8 | `benchmark/eval/results/medical_rag_eval.json` summary.medical_qwen3_embedding_4b | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval.json',encoding='utf-8'))['summary']['medical_qwen3_embedding_4b']; print(s['hit_at_k'], s['label_hit_at_k'], '/', s['cases'])"` | ✅ |
| 111 | §4.4 BGE Small Hit@3 / Label Hit@3 | 8/8, 6/8 | `benchmark/eval/results/medical_rag_eval.json` summary.index_bge_small | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval.json',encoding='utf-8'))['summary']['index_bge_small']; print(s['hit_at_k'], s['label_hit_at_k'], '/', s['cases'])"` | ✅ |
| 112 | §4.4 BGE M3 Hit@3 / Label Hit@3 | 8/8, 8/8 | `benchmark/eval/results/medical_rag_eval.json` summary.index_bge_m3 | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval.json',encoding='utf-8'))['summary']['index_bge_m3']; print(s['hit_at_k'], s['label_hit_at_k'], '/', s['cases'])"` | ✅ |
| 113 | §4.4 BGE M3 平均首命中排名 | 1.00 | `benchmark/eval/results/medical_rag_eval.json` summary.index_bge_m3.mean_first_hit_rank | `conda run -n myenv python -c "import json; print(json.load(open(r'benchmark/eval/results/medical_rag_eval.json',encoding='utf-8'))['summary']['index_bge_m3']['mean_first_hit_rank'])"` | ✅ |
| 114 | §4.4 合成 smoke — claim 支持率 / 引用覆盖 | 2/2 claims, citation_coverage=1.0 | `benchmark/eval/results/medical_rag_eval_synthesis_smoke.json` results.index_bge_small.primary_endpoint_safety.synthesis | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval_synthesis_smoke.json',encoding='utf-8'))['results']['index_bge_small']['primary_endpoint_safety']['synthesis']; print(s['supported_claims'], '/', s['claim_count'], s['citation_coverage'])"` | ✅ |
| 115 | §5.3 前端展示闭环 API | 8 cases, best=index_bge_m3, smoke coverage=1.0 | `controlsci/api/demo_endpoints.py` + `benchmark/eval/results/medical_rag_eval*.json` | `powershell -c "Invoke-RestMethod http://localhost:17001/api/demo/medical-rag/eval-summary \| Select-Object -ExpandProperty eval"` | ✅ |
| 116 | §4.4 Task3 本地 RAG 飞轮入口 | 固定评测 + 合成 smoke + 中文 Ask trace + demo/API 验证 | `run_task3_rag_flywheel.ps1` | `powershell -NoProfile -ExecutionPolicy Bypass -File .\run_task3_rag_flywheel.ps1 -SkipSynthesis -SkipZhAsk -SkipDemoVerify` | ✅ |
| 117 | §4.4 中文 Ask 固定题集规模 | 6 queries, top-k=3, case_set=zh_ask | `benchmark/eval/results/medical_rag_eval_zh_ask.json` cases + k + case_set | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/medical_rag_eval_zh_ask.json',encoding='utf-8')); print(len(d['cases']), d['k'], d['case_set'])"` | ✅ |
| 118 | §4.4 中文 Ask BGE M3 检索命中 | Hit@3 6/6, Label Hit@3 6/6, mean rank 1.00 | `benchmark/eval/results/medical_rag_eval_zh_ask.json` summary.index_bge_m3 | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval_zh_ask.json',encoding='utf-8'))['summary']['index_bge_m3']; print(s['hit_at_k'], s['label_hit_at_k'], s['mean_first_hit_rank'])"` | ✅ |
| 119 | §4.4 中文→英文检索桥接 | bridged_cases=6, multi_query_cases=2, query_languages=['zh'] | `benchmark/eval/results/medical_rag_eval_zh_ask.json` summary.index_bge_m3 | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval_zh_ask.json',encoding='utf-8'))['summary']['index_bge_m3']; print(s['bridged_cases'], s['multi_query_cases'], s['query_languages'])"` | ✅ |
| 120 | §4.4 中文 Ask 逐案例 trace 与合成覆盖 | 6 traces, 25/25 supported claims, mean citation_coverage=1.0 | `benchmark/eval/results/medical_rag_zh_ask_traces.jsonl` | `conda run -n myenv python -c "import json; rows=[json.loads(l) for l in open(r'benchmark/eval/results/medical_rag_zh_ask_traces.jsonl',encoding='utf-8') if l.strip()]; print(len(rows), sum(r['synthesis']['supported_claims'] for r in rows), '/', sum(r['synthesis']['claim_count'] for r in rows), sum(r['synthesis']['citation_coverage'] for r in rows)/len(rows))"` | ✅ |

---

## 十二、MinerU 解析后端与数据分级路由（2026-05-15）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|:--|:--|:--|:--:|
| 121 | 统一解析入口 | `tools/mineru_to_md.py` 支持 `local/official/auto/replay` | `tools/mineru_to_md.py` | `conda run -n myenv python tools/mineru_to_md.py --help \| Select-String "--backend\|--data-class\|--allow-cloud-upload"` | ✅ |
| 122 | 默认隐私策略 | 未声明数据按 `private_enterprise`，默认不允许云端上传 | `tools/mineru_to_md.py` dry-run 输出 | `conda run -n myenv python tools/mineru_to_md.py --dry-run --backend local --data-class private_enterprise --input-dir data/sources_flywheel --output-dir _scratch/mineru_dry` | ✅ |
| 123 | 私有数据云端拒绝 | `private_enterprise` 即使传入 `--allow-cloud-upload` 也拒绝官方 API | `tools/mineru_to_md.py` | `conda run -n myenv python tools/mineru_to_md.py "data/sources_flywheel/2605.02370_Robust Adaptive Predictive Control for Hook-Based Aerial Tra.pdf" --backend official --data-class private_enterprise --allow-cloud-upload --output-dir _scratch/mineru_official_block --stats` | ✅ |
| 124 | 公开数据仍需显式授权 | `public_open` 未传 `--allow-cloud-upload` 时拒绝官方 API | `tools/mineru_to_md.py` | `conda run -n myenv python tools/mineru_to_md.py "data/sources_flywheel/2605.02370_Robust Adaptive Predictive Control for Hook-Based Aerial Tra.pdf" --backend official --data-class public_open --output-dir _scratch/mineru_official_block --stats` | ✅ |
| 125 | replay 复用既有 Markdown | 回放模式可复用 `data/sources_flywheel/md` 产物并生成 `parse_result.json` | `_scratch/mineru_replay_test/.../parse_result.json` | `conda run -n myenv python tools/mineru_to_md.py "data/sources_flywheel/2605.02370_Robust Adaptive Predictive Control for Hook-Based Aerial Tra.pdf" --backend replay --data-class private_enterprise --output-dir _scratch/mineru_replay_test --overwrite --stats` | ✅ |
| 126 | 官方 API 真实接入 | `public_open + allow-cloud-upload` 完成 signed upload 并落盘 Markdown | `_scratch/mineru_official_public/.../*.md` | `conda run -n myenv python tools/mineru_to_md.py "data/sources_flywheel/2605.02370_Robust Adaptive Predictive Control for Hook-Based Aerial Tra.pdf" --backend official --data-class public_open --allow-cloud-upload --output-dir _scratch/mineru_official_public --overwrite --stats` | ✅ |

## 附录：口径对照

| 字段 | 旧口径（manifest 严格） | 权威口径（磁盘 glob 宽松） | 差异来源 |
|:--|---:|---:|:--|
| total chunks | 28,475 (`corpus_stats.json`) | **28,514** (`multimodal_chunks.json`) | +39 孤本 .md 文件（增量构建残留） |
| chunks_with_both | 4,935 (`image_formula_cooccurrence.json`) | **4,996** (`multimodal_chunks.json`) | +61（39 孤本 + 22 条伪正） |
| both_pct | ~17.3% (4,935/28,475) | **17.52%** (4,996/28,514) | 两个口径都往大走 |
| train chunks | 22,635 (manifest) | 26,477 (磁盘文件计数) | manifest 只注册解析成功 chunk |
| eval chunks | 5,840 (manifest) | 1,998 (磁盘文件计数) | eval split 只有 manifest 注册的 chunk |

> **规范**：报告中统一使用 **权威口径**（`multimodal_chunks.json`：28,514 / 4,996 / 17.52%）。manifest 口径仅限内部校验时引用。

---

## 附录：实验图片生成与公开展示副本

`docs/submissions` 是对外展示目录，因此实验图片的生成脚本与原始输出保留在展示目录之外，只复制最终 PNG 到展示资产目录。

| 图组 | 生成脚本 / 原始输出 | 公开展示副本 | 复现命令 |
|:--|:--|:--|:--|
| Track1 排行榜、MinerU/PyMuPDF、嵌入分布、Benchmark 质量图；Track3 中文 Ask 与 MedBench 证据边界 | `tools/generate_submission_experiment_figures.py`；`build/submission_experiment_figures/manifest.json` | `docs/submissions/shared/assets/task1/*.png`；`docs/submissions/shared/assets/task2/*.png`；`docs/submissions/shared/assets/task3/*.png` | `conda run -n myenv python tools/generate_submission_experiment_figures.py` |

---

## 附录：飞轮 5 篇论文详情

| arXiv ID | 领域 | 题数 | 维度分布 | 得分 |
|:---|---:|:--|:--|:--|
| 2605.02370 | 自适应 MPC | 3 | A×2, D×1 | 0.00, 0.00, 0.00 |
| 2605.03662 | 混合控制 | 3 | A×1, B×1, D×1 | 0.30, 0.20, 0.25 |
| 2605.05182 | CBF 安全滤波 | 3 | A×1, B×1, C×1 | 0.00, 0.00, 0.25 |
| 2605.05575 | 不变集 MPC | 3 | A×1, B×1, D×1 | 0.30, 0.00, 0.00 |
| 2605.06630 | 稳定性-混淆权衡 | 3 | A×1, B×1, D×1 | 0.30, 0.00, 0.50 |

---

## 附录：复现命令使用说明

所有命令均在解压或克隆后的 ControlMind 项目根目录下执行。需 conda `myenv` 环境。

**通用前置**：
```powershell
cd <ControlMind 项目根目录>
```

**批处理验证**：新建 `verify_data_trace.ps1` 可一键运行所有 `✅` 状态的复现命令。

**依赖**：
- Python 3.10+, `numpy`（用于加载 `.npy`）
- Windows PowerShell（用于文件计数）
- Git（用于 commit 统计）
---

## 十三、Task3 Evidence-Structured RAG（2026-05-15）

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|:--|:--|:--|:--:|
| 127 | §4.4 中文 Ask 结构化 RAG 规模 | 7 queries, top-k=3, case_set=zh_ask | `benchmark/eval/results/medical_rag_eval_zh_ask_structured.json` cases + k + case_set | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/medical_rag_eval_zh_ask_structured.json',encoding='utf-8')); print(len(d['cases']), d['k'], d['case_set'])"` | ✅ |
| 128 | §4.4 BGE M3 中文 Ask 结构化命中 | Hit@3 7/7, Label Hit@3 6/7, mean rank 1.00 | `benchmark/eval/results/medical_rag_eval_zh_ask_structured.json` summary.index_bge_m3 | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval_zh_ask_structured.json',encoding='utf-8'))['summary']['index_bge_m3']; print(s['hit_at_k'], s['label_hit_at_k'], s['mean_first_hit_rank'])"` | ✅ |
| 129 | §4.4 Evidence-Structured RAG 字段落盘 | structured_rag_cases=7, mechanism_cases=1 | `benchmark/eval/results/medical_rag_eval_zh_ask_structured.json` summary.index_bge_m3 | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval_zh_ask_structured.json',encoding='utf-8'))['summary']['index_bge_m3']; print(s['structured_rag_cases'], s['mechanism_cases'])"` | ✅ |
| 130 | §4.4 中文 Ask 结构化 trace 与合成覆盖 | 7 traces, 25/25 supported claims, mean citation_coverage=1.0 | `benchmark/eval/results/medical_rag_zh_ask_structured_traces.jsonl` | `conda run -n myenv python -c "import json; rows=[json.loads(l) for l in open(r'benchmark/eval/results/medical_rag_zh_ask_structured_traces.jsonl',encoding='utf-8') if l.strip()]; print(len(rows), sum(r['synthesis']['supported_claims'] for r in rows), '/', sum(r['synthesis']['claim_count'] for r in rows), sum(r['synthesis']['citation_coverage'] for r in rows)/len(rows))"` | ✅ |

| 131 | §4.4 中文 Ask 三索引结构化对照规模 | 3 indexes × 7 queries | `benchmark/eval/results/medical_rag_eval_zh_ask_structured_all_indexes.json` indexes + cases | `conda run -n myenv python -c "import json; d=json.load(open(r'benchmark/eval/results/medical_rag_eval_zh_ask_structured_all_indexes.json',encoding='utf-8')); print(len(d['indexes']), len(d['cases']))"` | ✅ |
| 132 | §4.4 三索引中文 Ask Hit@3 | Qwen 7/7, BGE Small 7/7, BGE M3 7/7 | `benchmark/eval/results/medical_rag_eval_zh_ask_structured_all_indexes.json` summary | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval_zh_ask_structured_all_indexes.json',encoding='utf-8'))['summary']; print([(k,v['hit_at_k'],v['cases']) for k,v in s.items()])"` | ✅ |
| 133 | §4.4 三索引合成引用覆盖 | Qwen 0.5714, BGE Small 0.8571, BGE M3 1.0 | `benchmark/eval/results/medical_rag_eval_zh_ask_structured_all_indexes.json` summary.*.mean_citation_coverage | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval_zh_ask_structured_all_indexes.json',encoding='utf-8'))['summary']; print([(k,v['mean_citation_coverage']) for k,v in s.items()])"` | ✅ |
| 134 | §4.4 真实 Ask OS/PFS 边界审查 | answer_audit=passed, citation_coverage=1.0 | `benchmark/eval/results/medical_rag_live_traces.jsonl` 最新 `endpoint_definition` trace；单次报告在 `benchmark/eval/results/medical/*.json` | `conda run -n myenv python -c "import json; rows=[json.loads(l) for l in open(r'benchmark/eval/results/medical_rag_live_traces.jsonl',encoding='utf-8') if l.strip()]; r=[x for x in rows if x.get('question_type')=='endpoint_definition'][-1]; print(r['answer_audit']['status'], r['citation_coverage'])"` | ✅ |
| 135 | §4.4 评测脚本 answer_audit 烟测 | 1/1 audit passed | `benchmark/eval/results/medical_rag_eval_audit_smoke.json` summary.index_bge_m3.answer_audit_passed_cases | `conda run -n myenv python -c "import json; s=json.load(open(r'benchmark/eval/results/medical_rag_eval_audit_smoke.json',encoding='utf-8'))['summary']['index_bge_m3']; print(s['answer_audit_passed_cases'], '/', s['cases'])"` | ✅ |
| 136 | §4.4 真实 Ask 安全拒答 trace | urgent_or_emergency 不进入检索 | `benchmark/eval/results/medical_rag_live_traces.jsonl` safety_refusal trace | `conda run -n myenv python -c "import json; rows=[json.loads(l) for l in open(r'benchmark/eval/results/medical_rag_live_traces.jsonl',encoding='utf-8') if l.strip()]; r=[x for x in rows if x.get('status')=='safety_refusal'][-1]; print(r['abstain_reason'], r['source_summary']['total_chunks'])"` | ✅ |

---

## 十四、Track1 中间报告回源补充（2026-05-17 严格审查）

本节专门收录正文中曾以 Markdown 中间报告、图片或笼统“工程日志”承载的定量声明。权威口径优先使用原始 JSON/JSONL、原始 PDF/Markdown、脚本计算结果；中间报告仅保留为人工阅读导航。

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|:--|:--|:--|:--:|
| 137 | Track1 §3.5 扫描教材文档入口字符差距 | MinerU 2,924,525 chars / PyMuPDF 0 effective text-layer chars | 提交包副本：`docs/submissions/data_trace_bundle/01_corpus_scale/mineru_vs_pymupdf_data.json`；MinerU: `corpus/processed/{自抗扰控制技术,自动控制原理_胡寿松,非线性系统_Khalil}/full_text.md`；公式: `corpus/stats/corpus_stats.json`；PyMuPDF 作为 PDF 文本层基线：同三本 `data/pdf/textbooks/*.pdf` 经 `fitz.open(...).get_text("text")` 复算；脚本修正见 `benchmark/pipeline/compare_mineru_vs_pymupdf.py` | `conda run -n myenv python -c "from pathlib import Path; import fitz; names=['自抗扰控制技术','自动控制原理_胡寿松','非线性系统_Khalil']; mineru=sum(len((Path('corpus/processed')/n/'full_text.md').read_text(encoding='utf-8')) for n in names); pymupdf=sum(sum(len(page.get_text('text')) for page in fitz.open(str(Path('data/pdf/textbooks')/(n+'.pdf')))) for n in names); print(mineru, pymupdf)"` | ✅ myenv + PyMuPDF 1.27.2.3 复核 |
| 138 | Track1 §3.5 扫描教材公式数 | 28,473 LaTeX formulas | `corpus/stats/corpus_stats.json` per_doc / `corpus/processed/{...}/formulas.json` | `conda run -n myenv python -c "import json; names={'自抗扰控制技术','自动控制原理_胡寿松','非线性系统_Khalil'}; d=json.load(open(r'corpus/stats/corpus_stats.json',encoding='utf-8'))['per_doc']; print(sum(x['formula_count'] for x in d if x['filename'] in names))"` | ✅ |
| 139 | Track1 §3.5 MinerU 1.2B vs MiMo 可比样本 | 42 comparable pairs; MiMo 42/42; MinerU 1.2B 42/42 within comparable subset | `benchmark/agent/results/bench_mineru_1.2b_checkpoint.json` results filtered by non-empty `mineru_latex` | `conda run -n myenv python -c "import json; rows=json.load(open(r'benchmark/agent/results/bench_mineru_1.2b_checkpoint.json',encoding='utf-8'))['results']; sub=[r for r in rows if r.get('mineru_latex')]; print(len(sub), sum(1 for r in sub if r.get('mimo_latex')), sum(1 for r in sub if r.get('mineru_latex')))"` | ✅ |
| 140 | Track1 §3.5 MinerU 1.2B vs MiMo metrics | MiMo edit=0.8874 / BLEU=0.0426; MinerU edit=0.9123 / BLEU=0.0323 | `benchmark/agent/results/bench_mineru_1.2b_checkpoint.json` comparable subset | `conda run -n myenv python -c "import json,statistics as s; rows=json.load(open(r'benchmark/agent/results/bench_mineru_1.2b_checkpoint.json',encoding='utf-8'))['results']; sub=[r for r in rows if r.get('mineru_latex')]; print(round(s.mean(r['mimo_edit_distance'] for r in sub),4), round(s.mean(r['mineru_edit_distance'] for r in sub),4), round(s.mean(r['mimo_bleu'] for r in sub),4), round(s.mean(r['mineru_bleu'] for r in sub),4))"` | ✅ |
| 141 | Track1 §4.3 跨管道 MAE/RMSE/Pearson/Spearman | MAE≈0.0003, RMSE≈0.0003, Pearson r≈1.0000, Spearman ρ=1.0000 | `benchmark/eval/results/leaderboard_complete.json` + `benchmark/eval/results/judge_matrix/api_8judge_consolidated.json` | `conda run -n myenv python -c "import json,math; lb=json.load(open(r'benchmark/eval/results/leaderboard_complete.json',encoding='utf-8'))['models']; cs=json.load(open(r'benchmark/eval/results/judge_matrix/api_8judge_consolidated.json',encoding='utf-8'))['summary_statistics']; rows=[(m['overall_score'], cs[k]['mean']) for k in cs for m in lb if m['model'].lower().replace('-','')==k.lower().replace('-','')]; diffs=[abs(a-b) for a,b in rows]; xs=[a for a,b in rows]; ys=[b for a,b in rows]; mx=sum(xs)/len(xs); my=sum(ys)/len(ys); pear=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/math.sqrt(sum((x-mx)**2 for x in xs)*sum((y-my)**2 for y in ys)); print(round(sum(diffs)/len(diffs),4), round(math.sqrt(sum(d*d for d in diffs)/len(diffs)),4), round(pear,4), len(rows))"` | ✅ |
| 142 | Track1 §4.6 双重身份 Pearson r | 0.999991 | `benchmark/eval/results/leaderboard_complete.json` + `benchmark/eval/results/judge_matrix/api_8judge_consolidated.json`; `shared/assets/task1/dual_role_matrix.png` 仅为展示图 | 同 #141，未四舍五入输出 Pearson：`conda run -n myenv python -c "import json,math; lb=json.load(open(r'benchmark/eval/results/leaderboard_complete.json',encoding='utf-8'))['models']; cs=json.load(open(r'benchmark/eval/results/judge_matrix/api_8judge_consolidated.json',encoding='utf-8'))['summary_statistics']; rows=[(m['overall_score'], cs[k]['mean']) for k in cs for m in lb if m['model'].lower().replace('-','')==k.lower().replace('-','')]; xs=[a for a,b in rows]; ys=[b for a,b in rows]; mx=sum(xs)/len(xs); my=sum(ys)/len(ys); print(sum((x-mx)*(y-my) for x,y in zip(xs,ys))/math.sqrt(sum((x-mx)**2 for x in xs)*sum((y-my)**2 for y in ys)))"` | ✅ |
| 143 | Track1 §7 AI-ready L1 验证 | validate_dataset.py 0.9s; 500 questions pass | 结构结果：`benchmark/dataset/core.json`；耗时：`docs/reports/reproducibility_log.md` 记录的命令输出；补充验收日志见 `docs/submissions/data_trace_bundle/12_final_supplemental_experiments/minimal_acceptance/track1_acceptance_demo.log` | `conda run -n myenv python benchmark/eval/validate_dataset.py` | ✅ 结构校验已复核；0.9s 为工程实测记录值 |
| 144 | Track1 §7 成本估算 L2/L3 | L2≈¥0.02; L3<¥50 | 成本公式来自正文假设：DeepSeek-v4-flash ¥0.001/1K tokens、题数和 token 估计 | `conda run -n myenv python -c "print('L2',10*2000/1000*0.001); print('L3',500*9*8000/1000*0.001)"` | ✅ 估算项，正文需保留 `≈/<` |
| 145 | Track1 §7 / Track3 GPU 吞吐 | embed batch25=8.9ms/text; 9B steady=2.94s; 35B steady=5.87s; 35B tok/s=47.9 | `docs/assets/medical/gpu_throughput.json` | `conda run -n myenv python -c "import json; d=json.load(open(r'docs/assets/medical/gpu_throughput.json',encoding='utf-8')); print(d['embedding']['batch_25']['per_text_ms'], sum(r['elapsed_s'] for r in d['runs']['qwen3.5:9b'][1:])/2, sum(r['elapsed_s'] for r in d['runs']['qwen3.5:35b'][1:])/2, d['inference']['qwen3.5:35b']['avg_tok_per_s'])"` | ✅ |
| 146 | Track3 §5 HF local embedding 吞吐 | BGE Small batch25=0.30ms/text; BGE M3 batch25=1.57ms/text; BGE M3 全量 3,348 chunks 估算 5.3s | 汇总: `docs/assets/medical/hf_embedding_throughput.json`; 原始逐 run: `docs/assets/medical/hf_embedding_throughput_raw.json` | `conda run -n myenv python _tools/bench_hf_embedding_throughput.py`; 复核: `conda run -n myenv python -c "import json; d=json.load(open(r'docs/assets/medical/hf_embedding_throughput.json',encoding='utf-8'))['summary']; print(d[0]['batches']['batch_25']['mean_per_text_ms'], d[1]['batches']['batch_25']['mean_per_text_ms'], d[1]['batches']['batch_25']['estimated_3348_chunks_s'])"` | ✅ |

---

## 十五、补充验收（2026-05-17）

本节记录一组轻量验收。所有输出均已复制入 `docs/submissions/data_trace_bundle/12_final_supplemental_experiments/`，用于补强主报告中的工程复现、AI-ready 数据消费和医疗安全边界声明。

| # | 报告位置 | 声明值 | 权威源文件 | 复现命令 | 状态 |
|:-:|:--|:--|:--|:--|:--:|
| 147 | quickstart / 三赛道入口 | Track1 5/5 pass; Track2 4/4 pass; Track3 6/7 pass, 1 skip | `docs/submissions/data_trace_bundle/12_final_supplemental_experiments/minimal_acceptance/*.log` | `.\run_reviewer_demo.ps1 -Track 1 -Quiet`; `.\run_reviewer_demo.ps1 -Track 2 -Quiet`; `.\run_reviewer_demo.ps1 -Track 3 -Quiet -SkipApiHealth` | ✅ |
| 148 | Track1 §1.4 / §8.2 | 本地 JSON 经 `datasets.load_dataset("json")` 读取 500 行，schema 字段完整 | `docs/submissions/data_trace_bundle/12_final_supplemental_experiments/track1_load/local_json_load_dataset.log` | `conda run -n myenv python -c "from datasets import load_dataset; ds=load_dataset('json', data_files={'core':'benchmark/dataset/core.json'}, field='questions', split='core'); print(len(ds), ds.column_names)"` | ✅ |
| 149 | Track2 §1.4 / §5.4 | `--local` dry-run 展开 8 步 DAG；`reproduce_all` 入口 final_status=`completed` | `docs/submissions/data_trace_bundle/12_final_supplemental_experiments/track2_fallback/local_dry_run_trace.json` + `reproduce_all_dry_run_trace.json` | `conda run -n myenv python benchmark/agent/agent_cli.py --dry-run --local --intents medical_rag,cross_modal_audit,leaderboard_viz`; `conda run -n myenv python benchmark/agent/agent_cli.py --dry-run --intents reproduce_all` | ✅ |
| 150 | Track3 §4.4 / §6.2 | 急症、个人剂量、个人诊断 3/3 返回 `safety_refusal`；`retrieval_mode=none`；云端上下文传输为 false | `docs/submissions/data_trace_bundle/12_final_supplemental_experiments/track3_refusal/*.json` | `conda run -n myenv python -c "import json,glob; rows=[json.load(open(p,encoding='utf-8')) for p in glob.glob(r'docs/submissions/data_trace_bundle/12_final_supplemental_experiments/track3_refusal/*.json')]; print(len(rows), [r['status'] for r in rows], [r['retrieval_mode'] for r in rows], [r['audit']['raw_medical_context_sent_to_cloud'] for r in rows])"` | ✅ |
