---
language:
- en
- zh
license: cc-by-4.0
task_categories:
- question-answering
- text-generation
configs:
- config_name: core
  data_files: core.json
- config_name: full
  data_files: full.json
tags:
- control-science
- benchmark
- scialign
- llm-evaluation
- structured-corpus
- instruction-tuning
pretty_name: ControlSci Sci-Align Benchmark (Dataset)
---

# ControlSci 数据集 — JSON Schema 与使用说明

> 面向控制科学领域 LLM 跨模态对齐评测的结构化数据集。四维评测体系：概念回溯(A) / 多步推理(B) / 条件敏感性(C) / 开放设计(D)。

---

## 数据文件

| 文件 | 规模 | 维度分布 | 说明 |
|------|:----:|:---------|------|
| `core.json` | 500 题 | A=125 / B=125 / C=125 / D=125 | **核心评测集**：四维完美平衡，推荐评测用此文件 |
| `full.json` | 889 题 | A=185 / B=251 / C=191 / D=262 | **全量可用集**：通过双层仲裁的题目合集 |
| `merged.json` | 1,109 题 | A=224 / B=330 / C=230 / D=325 | **候选池**：含待审/已淘汰题目，含全部生成记录 |
| `schema.json` | — | — | JSON Schema 定义（Draft 2020-12） |
| `manual_review.json` | — | — | 人工审查抽检对照表 |

### 一致性校验状态分布（core.json）

| 状态 | 数量 | 含义 |
|------|:----:|------|
| `auto_passed` | 122 | Embedding 快速通道自动通过 |
| `reviewed_kept` | 378 | LLM 仲裁 + 双轮校验保留 |

---

## 元数据结构

每份 JSON 文件顶层包含 `meta` 和 `questions` 两个字段：

```json
{
  "meta": {
    "project": "ControlSci — 控制科学结构化语料库与 Sci-Align 跨模态对齐评测基准",
    "version": "1.0",
    "updated": "2026-05-05",
    "total_questions": 500,
    "dimensions": { "A": 125, "B": 125, "C": 125, "D": 125 },
    "source": "Split from arbitrated candidate pool (1109 total) — core_500",
    "consistency_status": { "auto_passed": 122, "reviewed_kept": 378 },
    "selection_seed": 42,
    "dimension_target": { "A": 125, "B": 125, "C": 125, "D": 125 },
    "dimension_labels": {
      "A": "概念定义与数学表达",
      "B": "多步推理与计算求解",
      "C": "敏感性分析与方案对比",
      "D": "完整控制方案设计与综合评估"
    }
  },
  "questions": [ ... ]
}
```

| 元字段 | 类型 | 说明 |
|--------|------|------|
| `project` | string | 项目名称 |
| `version` | string | 数据集版本号（full.json/core.json = `1.0`，merged.json = `1.0-candidate`） |
| `updated` | string | 最后更新日期 (ISO 8601，全部为 `2026-05-05`) |
| `total_questions` | int | 题目总数 |
| `dimensions` | object | 各维度题数 `{A,B,C,D}` |
| `source` | string | 数据来源说明 |
| `consistency_status` | object | 一致性校验状态计数（仅 core.json / full.json） |
| `selection_seed` | int | 核心集抽样随机种子（仅 core.json） |
| `dimension_labels` | object | 各维度中文标签（仅 core.json） |

---

## 题目字段 Schema

每道题的结构如下（完整约束见 `schema.json`）：

| 字段 | 类型 | 必需 | 范围/枚举 | 说明 |
|------|------|:----:|-----------|------|
| `id` | string | ✅ | `^CS-EVO-[0-9]{5}$` | 全局唯一标识符 |
| `dimension` | string | ✅ | `A` / `B` / `C` / `D` | 所属评测维度 |
| `difficulty_level` | string | ✅ | `L1` / `L2` / `L3` / `L4` | 难度等级，L1 基础 → L4 挑战 |
| `control_category` | array[string] | ✅ | 见子领域表 | 所属控制子领域标签，1-3 个 |
| `question` | string | ✅ | — | 题目文本（含 LaTeX 行内公式） |
| `answer` | string | ✅ | — | 参考答案（含 LaTeX 行内公式） |
| `reasoning_steps` | array[string] | ✅ | ≥1 条 | 逐步推理过程，均值 5.2 条/题，供 Scorer 参考 |
| `source_ref` | string | ✅ | — | 题目来源：`教材名_chunk_NNN` 或 `arXivID_chunk_NNN` |
| `sensitivity_dimension` | string | *C 维必需* | `parameter` / `environment` / `constraint` / `null` | 条件敏感题目的敏感参数维度 |
| `sibling_id` | string | *C 维必需* | `CS-EVO-xxxxx` / `null` | C 维配对题的原始题 ID |
| `rubric` | object | *D 维必需* | — | 开放设计题的评分标准（含 5 个子维度） |
| `consistency_status` | string | ✅ | `auto_passed` / `needs_review` / `reviewed_kept` / `reviewed_discarded` | 一致性校验状态 |
| `model_source` | string | — | `deepseek` / `mimo` / `minimax` | 生成该题的模型来源 |

### control_category 可选值

核心集 500 题使用以下 10 个细粒度标签（语料库覆盖全部 14 个子领域）：

| 标签 | 子领域 | 标签 | 子领域 |
|------|--------|------|--------|
| `classical` | 经典控制 | `intelligent` | 智能控制 |
| `optimal` | 最优控制 | `mpc` | 模型预测控制 |
| `robust` | 鲁棒控制 | `adaptive` | 自适应控制 |
| `nonlinear` | 非线性控制 | `digital` | 数字控制 |
| `modern` | 现代控制 | `multi_agent` | 多智能体协同 |

### D 维 rubric 字段结构（开放设计专属）

```json
"rubric": {
  "feasibility":   { "max_score": 1, "weight": 0.2, "description": "方案工程可行性" },
  "method_choice": { "max_score": 1, "weight": 0.2, "description": "方法选择合理性" },
  "completeness":  { "max_score": 1, "weight": 0.2, "description": "方案完整度" },
  "innovation":    { "max_score": 1, "weight": 0.2, "description": "设计创新性" },
  "clarity":       { "max_score": 1, "weight": 0.2, "description": "表达清晰度" }
}
```

### 难度等级说明

| 等级 | 考察目标 | 示例 |
|:----:|----------|------|
| L1 | 直接复述教材定义，低检索难度 | "请写出 PID 控制器的传递函数标准形式。" |
| L2 | 需要理解后回答，结合公式与解释 | "解释超前补偿器中参数 α 对系统稳定裕度的影响。" |
| L3 | 跨概念组合，需要逐步推导 | "给定开环传递函数，用根轨迹法设计串联校正网络。" |
| L4 | 综合多知识点，需要深度推理 | "分析多智能体系统中 event-triggered 通信与 Zeno 现象的充要条件。" |

---

## 加载方式

### HuggingFace Datasets（推荐）

```python
from datasets import load_dataset

# 加载核心集
core = load_dataset("MorningStar0709/control-sci-corpus", split="core")
print(f"核心集: {len(core)} 题")

# 查看第一条样本字段
sample = core[0]
print(sample["question"])
print(sample["dimension"], sample["difficulty_level"])
```

### 本地 JSON 直接加载

```python
import json

with open("benchmark/dataset/core.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"核心集: {len(data['questions'])} 题")
print(f"维度分布: {data['meta']['dimensions']}")
```

### 数据筛选示例

```python
# 筛选 C 维敏感性问题
c_questions = [
    q for q in data["questions"]
    if q["dimension"] == "C" and q["sensitivity_dimension"] == "parameter"
]
print(f"参数敏感性 C 维题: {len(c_questions)}")

# 筛选 L4 难度开放设计题
d_l4 = [
    q for q in data["questions"]
    if q["dimension"] == "D" and q["difficulty_level"] == "L4"
]
print(f"L4 开放设计题: {len(d_l4)}")
```

---

## 数据集统计

| 指标 | 数值 |
|------|:----:|
| 语料来源 | 23 本教材 + 339 篇 arXiv 论文 |
| 文档总数 processed | 362 篇 |
| 语义分块数 | 28,514 chunks |
| LaTeX 公式总数 | 253,012 |
| 图片-公式共现 chunks | 4,996 (17.52%) |
| 跨模态可追溯索引 | **500 题 100% 匹配** — 74 题含图片+公式共现 (14.8%) |
| 覆盖子领域 | 14（语料）/ 10（核心集标签） |
| 核心集一致性 | auto_passed 122 + reviewed_kept 378 |
| 平均每道题 reasoning_steps | 均值 5.2 条，范围 1-14 条 |
| 模型生成来源 | DeepSeek 321 / MiMo 86 / MiniMax 93 |
| 许可协议 | CC-BY-4.0 |

---

## 数据用途（三层定位）

ControlSci 数据集遵循"评测 → 微调 → 闭环"三层消费模型，每一层面向不同的 AI 使用场景：

| 层级 | 用途 | 数据文件 | 规模 | 典型消费方式 |
|:---:|------|----------|:----:|-------------|
| **L1 评测** | 评测基准 — LLM 推理能力系统评估 | `core.json` | 500 题 | `evaluate.py` 四维评分；排行榜生成；跨模型对比 |
| **L2 指令微调** | 指令微调 — 领域知识注入 | `full.json` | 889 题 | `load_dataset(..., "full")` → QLoRA/SFT 训练；Colab 零适配Demo |
| **L3 AI 闭环验证** | 自修正轨迹 — 跨模型验证闭环 | self_correction 轨迹 | 3 模型 × 20 题 | 多模型修正轨迹对比；AI 自我纠错能力研究 |

**L1 评测**（`core.json`, 500 题）：面向模型评测，A/B/C/D 四维各 125 题完美平衡，经双层仲裁 + 一致性校验（auto_passed 122 + reviewed_kept 378）。使用 `evaluate.py` 搭配统一 Judge（推荐 deepseek-v4-flash）进行四维评分，产出 leaderboard.json/html。

**L2 指令微调**（`full.json`, 889 题）：面向领域指令微调，包含 core 500 题 + 389 道质量合格但仅通过单轮校验的附加题。更大数据量 + 覆盖更广的子领域分布，适合 QLoRA/SFT 等参数高效微调。每道题含 `question` / `answer` / `reasoning_steps` 三个可组合字段，支持 instruction → response 格式转换。

**L3 AI 闭环验证**（self_correction 轨迹）：面向 AI 自我纠错研究，包含 DeepSeek-v4-flash / MiMo-v2-flash / MiniMax-M2.5 三模型的跨模型自修正轨迹（各 20 题低分题 → 2 轮修正 → Judge 重评）。轨迹记录修正前后的评分变化、推理链演进和最终得分 delta，为 AI 闭环验证研究提供真实数据。

> **三层关系**：L1 定义评测基准 → L2 提供微调数据 → L3 验证闭环效果。三层数据共享统一的 JSON Schema（`schema.json`），确保跨层兼容性。

### HuggingFace Datasets 加载（按层）

```python
from datasets import load_dataset

# L1 评测 — 核心集 500 题
core = load_dataset("MorningStar0709/control-sci-corpus", "core", split="train")
print(f"评测集: {len(core)} 题, 维度分布: A=125 B=125 C=125 D=125")

# L2 指令微调 — 全量集 889 题
full = load_dataset("MorningStar0709/control-sci-corpus", "full", split="train")

# 格式化为 instruction → response
def format_instruction(ex):
    return {"text": f"### 问题\n{ex['question']}\n\n### 参考答案\n{ex['answer']}"}

train_data = full.map(format_instruction)
print(f"微调数据: {len(train_data)} 条")
```

---

## 引用

本项目同时提供 [CITATION.cff](../../CITATION.cff) 标准引用文件（GitHub / Zenodo 双平台自动识别）。

```bibtex
@misc{controlscibenchmark2026,
  title        = {ControlSci: A Structured Corpus and Sci-Align Benchmark
                  for Control Science},
  author       = {{MorningStar}},
  year         = {2026},
  howpublished = {\url{https://github.com/MorningStar0709/control-sci}},
  note         = {CC-BY-4.0 licensed}
}
```

---

## 许可

本数据集采用 **Creative Commons Attribution 4.0 International (CC-BY-4.0)** 许可。详见 [LICENSE](../../LICENSE) 或访问 [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)。
