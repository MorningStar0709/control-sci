# ControlSci Benchmark — 跨模态对齐评测基准

ControlSci 评测基准的代码与数据集。

## 目录结构

```
benchmark/
├── dataset/             # 评测数据集 JSON
│   ├── core.json        # 核心集（500题，A/B/C/D各125）
│   ├── full.json        # 全量可用集（889题）
│   ├── merged.json      # 候选池（1109题，含待审）
│   ├── schema.json      # 数据 Schema 定义
│   └── manual_review.json  # 人工审查对照
├── pipeline/            # 数据生成管线
│   ├── build_benchmark.py        # 从语料库生成评测题
│   ├── merge_benchmarks.py       # 合并多路生成产出
│   ├── split_benchmark.py        # 拆分为 core + full 子集
│   ├── arbiter.py                # 两轮答案仲裁
│   ├── orphan_judge.py           # 孤儿题自动回收
│   ├── validate_benchmark.py     # 数据集校验
│   ├── export_dataset.py         # HuggingFace 导出
│   └── compare_mineru_vs_pymupdf.py  # 工具对比实验
├── eval/                # 模型评测
│   ├── evaluate.py               # 评测入口
│   ├── judge.py                  # 评分器
│   ├── report.py                 # 报告渲染
│   ├── report_viz.py             # 可视化报告
│   ├── summarize_multi.py        # 多模型汇总
│   ├── run_eval_pipeline.py      # 全自动评测管线
│   ├── run_eval_multi.ps1        # 批量评测脚本
│   └── eval_sample.sh            # 评测示例
├── generator/           # 生成器子包（被 pipeline 引用）
│   ├── api.py            # LLM 调用层
│   ├── prompts.py        # Prompt 模板
│   ├── distribution.py   # 维度/难度分布控制
│   └── quality.py        # 质量监控
├── archive/             # 中间产物归档（gitignored）
│   ├── raw_json/         # 各 Provider 原始 JSON
│   ├── manual_review/    # 审查数据
│   ├── checkpoint/       # 生成/仲裁中间检查点
│   ├── backup/           # 易地备份
│   └── candidate/        # 合并候选池产物
└── logs/                # 日志归档（gitignored）
    ├── generation/
    ├── diag/
    ├── arbitration/
    └── orphan_judge/
```

## 核心数据

| 文件 | 题数 | 说明 |
|------|:----:|------|
| `dataset/core.json` | 500 | 核心集：A/B/C/D 各 125 完美平衡 |
| `dataset/full.json` | 889 | 全量可用：通过仲裁的题目 |
| `dataset/merged.json` | 1,109 | 候选池：含待审和已淘汰题目 |

## 快速使用

### 拆分数据集

```bash
python pipeline/split_benchmark.py --seed 42
```

### HuggingFace 导出

```bash
python pipeline/export_dataset.py --input dataset/core.json --output ../huggingface/control-sci-corpus
```

### 模型评测

```bash
python eval/evaluate.py \
  --mode model \
  --input dataset/core.json \
  --target-model deepseek-v4-flash \
  --judge-model deepseek-v4-flash \
  --output eval_report.json
```
