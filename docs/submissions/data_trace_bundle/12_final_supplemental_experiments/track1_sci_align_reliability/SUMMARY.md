# Track 1 Sci-Align Reliability Supplemental Experiments

本目录保存 Track 1 Sci-Align 数据集在可消费性、可追溯性、跨模态边界、四维区分度、训练可用性、外部格式兼容和小样本复核一致性上的补充实验产物。实验均复用既有数据与结果，不新增外部 API 调用，不上传数据。

| Task | Scope | Result | Evidence |
|---|---|---|---|
| Task 1 | AI-Ready 消费链路 | core=500、full=889；required fields / reasoning_steps / source_ref 覆盖率均为 1.0 | `track1_ai_ready_smoke.json` |
| Task 2 | 完整性与可追溯审计 | 500 题 unique id、required fields、dimension、source_ref、reasoning_steps 全量通过，issue_count=0 | `track1_sci_align_integrity_audit.json` |
| Task 3 | 跨模态弱点 taxonomy | 20 个 replay 样本覆盖 7 类对齐原因，consistent=10、inconsistent=9、partial=1 | `track1_multimodal_error_taxonomy.json` |
| Task 4 | 四维区分度校准 | 9 模型 × 500 题；range_order=D,C,B,A；A/B range mean=0.117，C/D range mean=0.397 | `track1_dimension_discriminability.json` |
| Task 5 | 训练可用性 Ablation | Sciverse split=785/139；Sciverse-trained 4B PPL delta=-78.3%；4B score delta=-0.0034 | `track1_training_utility_ablation.json` |
| Task 6 | 外部格式兼容 | 50 条分层样本可转换为 4 种结构，关键字段保留率均为 1.0 | `track1_export_format_compatibility.json` |
| Task 7 | 小样本复核一致性 | 30 条样本；mapped_question_count=500；mean bucket agreement=0.7345，dimension agreement=1.0 | `track1_sample_review_consistency.json` |
| Task 8 | Sci-Align / Sci-Evo 范式边界 | 7 项补充实验聚合；明确 Sci-Align 为主范式，Sci-Evo 作为演化轨迹扩展边界 | `track1_supplemental_summary.json` |

## Interpretation

这些实验把 Track 1 的数据资产从“能评测模型”进一步封口到“能被消费、能被追溯、能被迁移格式、能说明边界”。所有对外叙事均应采用“科学对象 / 工程问题 → 实验 → 证据 → 边界”的结构；不得直接复述比赛评分细则。

## Reproduction

```powershell
$env:PYTHONIOENCODING='utf-8'
$env:CONDA_NO_PLUGINS='true'
conda run --no-capture-output -n myenv python -m benchmark.eval.track1_supplemental_summary --input benchmark/eval/results --output benchmark/eval/results/track1_supplemental_summary.json
```

单项实验的复现命令见 `shared/DATA-TRACE.md` #174–#181。
