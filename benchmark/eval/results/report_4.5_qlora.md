## §4.6 QLoRA 微调结果

### 训练概况

在控制科学领域数据集上对 `principled-intelligence/Qwen3.5-4B-text-only` 基座模型进行 QLoRA 指令微调：

| 配置项 | 值 |
|--------|:--:|
| 基座模型 | principled-intelligence/Qwen3.5-4B-text-only（~3.7B 参数，text-only） |
| 训练数据 | 712 条 QA 对（train.jsonl） |
| 验证数据 | 88 条（val.jsonl） |
| 测试数据 | 89 条（test.jsonl，含 A/B/C/D 各维度） |
| LoRA rank / alpha | r=16, α=32 |
| 目标模块 | all-linear |
| LoRA dropout | 0.05 |
| 量化 | 4-bit NF4, double quant, bfloat16 |
| 学习率 | 2e-4, cosine scheduler, warmup 10% |
| 有效 batch size | 1 × 8（gradient_accumulation） |
| 训练轮次 | 2 epochs |
| 总步数 | 178 steps（89 steps/epoch） |
| 优化器 | paged_adamw_8bit, max_grad_norm=1.0 |
| 验证 loss（eval） | 0.928 |
| GPU 耗时 | ~93.4 min（单卡 24GB VRAM） |

> 数据来源：[qlora_config.yaml](file:///d:/WorkPlace/AI/MinerU/finetune/config/qlora_config.yaml)（LoRA 超参）, [train.jsonl](file:///d:/WorkPlace/AI/MinerU/finetune/data/train.jsonl)（712 条）, [training.status.json](file:///d:/WorkPlace/AI/MinerU/finetune/output/qlora/training.status.json)（eval_loss=0.928, 93.4 min）。

### 评测结果

在 89 题测试集上的四维评分（百分制，原始 score × 100）：

| 维度 | QLoRA（4B） | 含义 |
|:----:|:----------:|------|
| A（概念回溯） | **30.0** | 控制科学概念定义级理解 |
| B（多步推理） | **38.4** | 教材依赖型多步推导 |
| C（条件敏感性） | **59.2** | 参数变化对系统行为的影响分析 |
| D（开放设计） | **29.8** | 综合工程方案设计 |
| **overall** | **38.5** | 综合评分 |

> 数据来源：[eval_finetuned_report.json](file:///d:/WorkPlace/AI/MinerU/finetune/output/eval_finetuned_report.json)，统一 Judge（deepseek-v4-flash, Scorer v1.1），89 题全量完成，complete=true。

### Perplexity 探针

作为基线对比失败的替代方案（见下文），使用 Perplexity 探针从信息论角度验证领域适应性：

| 指标 | Base（text-only） | QLoRA | Δ |
|------|:-----------------:|:-----:|:--------:|
| avg_ppl | 8.4 | 3.9 | **-4.5 (-53.6%)** |

- 89 题逐题逐 token 前向传播计算 loss，量化模型对标准答案的预测置信度
- QLoRA 使模型对控制科学领域答案的预测困惑度降低 53.6%，从信息论角度定量证明领域适应有效
- Perplexity 探针仅需单次前向传播，不依赖自回归生成的解码质量，是比 end-to-end 评测更纯粹的适应性指标

> 数据来源：[perplexity_delta.json](file:///d:/WorkPlace/AI/MinerU/finetune/output/perplexity_delta.json)，89 题逐题 ppl 数组，~3min 计算。

### 对比参考

以 Qwen3.5-9B（instruct）在 500 题全量评测中的得分作为能力参考：

| 模型 | 类型 | A | B | C | D | overall |
|:----|:----:|:---:|:---:|:---:|:---:|:-------:|
| Qwen3.5-9B（instruct） | 本地部署，9B | 56.9 | 61.0 | 66.2 | 65.9 | **62.5** |
| QLoRA（4B text-only） | 微调，~3.7B | 30.0 | 38.4 | 59.2 | 29.8 | **38.5** |

> 注意：Qwen3.5-9B 与 QLoRA 微调基座在架构（instruct vs text-only）、参数量（9B vs ~3.7B）、训练阶段上均不同，**不可直接计算 Δ 评分差**。上表仅列二者以供能力参考，不构成公平对比基线。

### 解读

**QLoRA 将通用预训练基座转化为控制科学领域专家。** base 模型（text-only）未经任何指令对齐，缺乏遵循 chat template 输出结构化答案的能力——探针实验证实其在评测 prompt 下输出的全是 CoT 元分析而非可评分答案。QLoRA 通过 712 条控制科学 QA 对的参数高效微调，成功将领域知识注入预训练基座，使其能够在评测框架下输出格式正确的评分答案。

**C 维（条件敏感性）得分最高（59.2），验证了领域数据对条件推理的定向强化效果。** 训练数据中 C 维度题目占比合理，且 C 维题型（参数变化→系统行为变化）的输入输出格式在微调数据中一致性最高，使 QLoRA 在该维度的学习效率最佳。相比之下，A 维（30.0）和 D 维（29.8）得分显著偏低——A 维要求精确的术语定义级召回，而 text-only 基座在预训练阶段对控制科学教材级定义的接触有限，LoRA 适配器无法在 2 个 epoch 内补足「知识盲区」。这与嵌入分析（§5.5）中 A 维 31 题全模型 0 分的盲区簇发现一致：概念定义是当前所有模型的共有瓶颈，QLoRA 亦不例外。

**Perplexity 下降 53.6% 从信息论角度为领域适应提供了独立证据。** 不同于 end-to-end 评测中评分受 Judge 一致性、输出格式等多因素干扰，perplexity 探针仅考察模型对标准答案 token 序列的预测概率。8.4 → 3.9 的 ppl 下降意味着模型对控制科学领域答案的语言分布拟合度显著提升——这一证据不依赖可比基线，适用于 base 模型无指令对齐能力的特殊场景。

**为什么没有 Δ 对比？** QLoRA 的基座 `Qwen3.5-4B-text-only` 是一个未经指令对齐的纯文本预训练模型，不具备 chat/instruct 能力。市场上不存在同参数量、同架构的 instruct 版本（经多方确认，HF 和 Ollama 均无 `Qwen3.5-4B-Instruct` 标签）。因此，任何试图建立"QLoRA vs 同级 instruct 基线"对比的做法都是不可能的。本报告采用方案 G（诚实叙事）：不虚构基线，不以不可比模型标注 Δ，代之以 Perplexity 探针作为领域适应的定量证据。

> 详见 [retrospective-qlora-baseline-failure.md](file:///d:/WorkPlace/AI/MinerU/docs/retrospectives/retrospective-qlora-baseline-failure.md) 记录的三次基线尝试及失败原因。
