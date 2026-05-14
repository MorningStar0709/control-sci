# ControlSci Data Agent 部署指南

> **版本**：v4.0 | **更新日期**：2026-05-10
> **适用环境**：Windows 10/11 + Conda + Python 3.12+ | 可选：Ollama（本地模型）、vLLM WSL2（1.2B VLM 文档解析）、RTX 5090 24GB（QLoRA 微调 + 35B 推理）
> **架构**：13 intent × LLM Intent Router × 三轨资源调度 (API/MiMo-V2.5 视觉/Ollama 本地/MinerU/vLLM)

---

## 1. 系统概述

ControlSci Data Agent 是面向 AGI4S 的科学文档跨模态语料智能体。它能自主理解科学文档处理需求、规划多步执行路径、调用三轨推理引擎（轨道 1：API DeepSeek/MiMo/MiniMax 含 MiMo-V2.5 原生视觉；轨道 2：Ollama 本地 9B/35B；轨道 3：vLLM WSL2 MinerU-1.2B VLM 公式识别）+ MinerU 文档解析，完成从原始 PDF 到结构化跨模态评测数据集的全链路自主生产。

### 1.1 核心能力

| 能力 | 说明 |
|------|------|
| **13 intent × LLM Intent Router** | 自然语言 → few-shot 拆解为多步 plan → 自动调度执行路径 → Verify 闭环 |
| **三轨推理引擎** | 轨道 1（API：DeepSeek/MiMo/MiniMax）、轨道 2（Ollama 本地：9B/35B）、轨道 3（vLLM WSL2：MinerU-1.2B VLM 文档解析） → ResourceScheduler 按任务类型自动路由 |
| **跨模态对齐审计** | MiMo-V2.5 原生全模态视觉模型（~4.7s/图），6,204 含图 chunk × 11,554 张图片全量扫描，断点续跑 |
| **三 Provider 并行生成** | DeepSeek / MiMo / MiniMax 三路同时生成评测题 |
| **数据飞轮闭环** | arxiv_search → mineru_parse → benchmark_build → quality_arbitrate → model_evaluate → leaderboard_viz：从论文检索到排行榜更新的全自动 6-step |
| **多格式文档解析** | 支持 PDF/PPTX/HTML/扫描件图片四种格式统一解析，chunk 数/公式提取率/图片保留率 三维度对比 |
| **LLM-as-Judge 仲裁** | 两层仲裁（Embedding 快速通道 + LLM 深度评审）筛选高质量题目 |
| **隐私双路径** | `--local` 模式：Resource Scheduler 降级至 Ollama（Intent Router 仍用 DeepSeek） |
| **多 Judge 一致性** | API 8 Judge + 本地 6 Judge → Fleiss' κ 三角验证 + 评分者反规模定律 |
| **QLoRA 领域微调** | 单卡 24GB 极限微调，Perplexity 探针验证语料信息密度 |
| **结构化执行日志** | JSON 格式记录每步输入/输出/状态/耗时/错误/验证结果 |

### 1.2 系统架构

```
用户自然语言输入: "审计这批 arXiv 论文的公式-图片跨模态对齐质量"
  │
  ▼
┌─ Layer 1: Intent Router (agent_cli.py — LLM few-shot)
│  DeepSeek v4-flash 将自然语言 → intent 序列:
│  [cross_modal_audit → corpus_quality_report]
│  每步标注: tool / resource_type / depends_on
│
├─ Layer 2: Resource Scheduler (resource_scheduler.py)
│  三轨决策 (优先级: 可复现性 > 隐私 > 成本):
│  ├─ 轨道 1 (API) → DeepSeek/MiMo/MiniMax — 文本/Judge + MiMo-V2.5 视觉
│  ├─ 轨道 2 (Ollama) → qwen3.5:9b/35b — 本地推理 + Judge
│  └─ 轨道 3 (vLLM WSL2) → MinerU-1.2B VLM — 公式识别专用
│  可选 --local: Layer 2 降级至 Ollama/MinerU（Layer 1 Intent Router 仍用 DeepSeek）
│
├─ Layer 3: Executor + Verifier
│  for each step:
│    execute → capture LogStep → verify (LLM)
│    ├─ ✅ pass → next step
│    ├─ ❌ fail → auto-fallback (switch provider / retry)
│    └─ ⚠️ partial → append correction step
│
└─ Output: execution_log.json + artifacts
```

### 1.3 13 intent 概览

| # | intent_id | 功能 | 工具链 | 资源类型 |
|:--:|------|------|------|:--------:|
| 0 | `arxiv_search` | arXiv 论文检索 — 控制科学前沿论文检索+下载 | searching-arxiv-papers Skill + arXiv API | script |
| 1 | `mineru_parse` | 文档解析 — PDF/PPTX 原始文档 → 结构化 Markdown | mineru-to-md Skill + MinerU API | local_api |
| 2 | `corpus_parse` | 语料解析 — 科学文档批量解析，含公式/图片/表格提取 | MinerU API + mineru-to-md Skill | local_api |
| 3 | `cross_modal_audit` | 跨模态对齐审计 — 图片×公式语义一致性 | visual_audit.py + MiMo-V2.5 原生视觉 | api |
| 4 | `corpus_quality_report` | 语料质量报告 — 全维度质量分析 | DeepSeek + 统计脚本 | api |
| 5 | `benchmark_build` | 评测数据集构建 — 500 题四维度覆盖 | build_benchmark.py + 三 Provider | api |
| 6 | `quality_arbitrate` | 质量仲裁 — 双层 LLM 一致性筛选 | arbiter.py + DeepSeek + Ollama | api |
| 7 | `model_evaluate` | 模型评测 — 统一接口评测任意模型 | evaluate.py + 自动选 Judge | api |
| 8 | `multi_judge_compare` | 多 Judge 对比 — API vs 本地双榜 | evaluate.py (API + Ollama 双路径) | api |
| 9 | `leaderboard_viz` | 排行榜可视化 — 表格+柱状图+热力图 | summarize_multi.py + report_viz.py | script |
| 10 | `local_finetune` | 本地微调 — QLoRA + Perplexity 验证 | train_qlora.py + Ollama | local_gpu |
| 11 | `reproduce_all` | 全量复现 — 一键端到端全链路 | run_agent.ps1 全链路 | script |
| 12 | `multi_format_parse` | 多格式文档解析 — PPTX/HTML/扫描件 → Markdown 质量对比 | MinerU API + tools/mineru_to_md.py | local_api |

---

## 2. 环境准备

### 2.1 硬件要求

| 资源 | 最低配置 | 推荐配置 |
|------|---------|---------|
| 内存 | 8 GB | 16 GB+（Ollama 35B 建议 64 GB） |
| 磁盘 | 10 GB（语料 + 中间产物） | 20 GB+ |
| GPU | 不需要（纯 API 调用） | RTX 5090 24GB（QLoRA + Ollama 35B） |
| 网络 | 稳定互联网（API 调用） | 无代理直连（降低延迟） |

### 2.2 软件依赖

| 组件 | 版本要求 | 用途 |
|------|---------|------|
| Python | ≥ 3.10（推荐 3.12） | 主运行时 |
| Conda | 任意版本 | 环境管理 |
| MinerU | ≥ 1.0 | PDF/论文解析 |
| Ollama | ≥ 0.6 | 可选：本地模型推理 + Judge |
| OpenAI Python SDK | ≥ 1.68 | DeepSeek / MiMo 文本调用 |
| Anthropic Python SDK | ≥ 0.97 | MiniMax 兼容调用 |
| httpx | ≥ 0.28 | MiMo-V2.5 视觉 API 调用 |

### 2.3 Python 包依赖

```powershell
conda run --no-capture-output -n myenv pip install openai anthropic httpx tqdm requests pyarrow
```

**版本参考（已验证可用）**：

| 包 | 版本 | 用途 |
|----|------|------|
| openai | ≥ 1.68 | DeepSeek / MiMo 文本 / Ollama 兼容口 |
| anthropic | ≥ 0.97.0 | MiniMax Anthropic 兼容接口 |
| httpx | ≥ 0.28.1 | MiMo-V2.5 视觉 raw httpx 调用 |
| tqdm | ≥ 4.67.3 | 进度展示 |
| requests | ≥ 2.32+ | 通用 HTTP |
| pyarrow | ≥ 15.0+ | HF 数据集导出 |

### 2.4 API 密钥配置

ControlSci Data Agent 支持四类 API 密钥，需配置以下环境变量：

```powershell
# DeepSeek（Intent Router + 生成 + Judge 主引擎）
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-your-deepseek-key", "User")

# MiMo-V2.5 视觉 + MiMo 文本（跨模态审计 + 补充生成）
[System.Environment]::SetEnvironmentVariable("MIMO_API_KEY", "your-mimo-key", "User")

# MiniMax（补充生成）
[System.Environment]::SetEnvironmentVariable("MINIMAX_API_KEY", "your-minimax-key", "User")

# MinerU API（语料解析）
[System.Environment]::SetEnvironmentVariable("MINERU_API_BASE", "http://localhost:8000", "User")
```

> **注意**：
> - 环境变量设置后需重启终端生效
> - DeepSeek 通过 `OPENAI_API_KEY` 传递（OpenAI 兼容接口）
> - MiMo-V2.5 视觉调用使用 `api-key` header 认证，不走 OpenAI SDK（详见 §3.1 五 Provider 认证方式表）
> - Agent 启动时自动执行 `_check_env()` 验证全部 Provider Key

### 2.5 Ollama 本地模型（轨道 2）

Ollama 提供零成本本地推理能力，支持两种通信模式：

- **原生 API** (`/api/chat`，推荐)：设置 `think:false` 避免推理链占用 max_tokens
- **OpenAI 兼容 API** (`/v1/chat/completions`)：非思考场景使用

```powershell
# 安装 Ollama 后拉取模型
ollama pull qwen3.5:9b       # 本地 Judge + 评测目标模型
ollama pull qwen3-embedding:4b  # Embedding 快速通道
ollama pull qwen3.5:35b      # 可选：6 Judge 一致性升级 + 弹性伸缩实验

# 验证运行状态
ollama list
```

Ollama 默认监听 `http://localhost:11434`。可通过 `OLLAMA_HOST` 环境变量自定义地址。

> **性能参考**：9B 模型 ~1s/题，4B 模型 ~0.5s/题，35B 模型 ~1.5s/题（RTX 5090）。35B 是 thinking model，必须用 `/api/chat` + `think:false`，不可用 `/v1/chat/completions`。

### 2.6 vLLM 本地 VLM（轨道 3 — WSL2 可选）

轨道 3 通过 vLLM 在 WSL2 容器内部署 MinerU-1.2B VLM，提供专用文档解析能力。实验表明，1.2B 稠密模型在公式识别任务上的表现与 310B 通用视觉模型（MiMo-V2.5 MoE，15B 激活参数）可比——印证了"领域适配 > 模型尺寸"的工程结论。

#### 2.6.1 前置条件

- Windows 11 + WSL2 + Ubuntu 22.04+（Windows 10 21H2+ 亦可）
- WSL2 内 Conda 环境已配置
- 宿主机 RTX 5090 24GB（vLLM 自动识别 GPU）

#### 2.6.2 安装与启动

```bash
# WSL 内
conda activate myenv
pip install vllm
vllm serve opendatalab/MinerU2.5-2509-1.2B --port 8000 --gpu-memory-utilization 0.3
```

> 1.2B 模型仅 ~3GB，`--gpu-memory-utilization 0.3` 即可。如需和 Ollama 共享 GPU，可降至 0.2。

#### 2.6.3 验证部署

```bash
curl -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "opendatalab/MinerU2.5-2509-1.2B", "prompt": "Hello", "max_tokens": 10}'
```

#### 2.6.4 与 MinerU 的区别

| 维度 | MinerU API | vLLM MinerU-1.2B VLM |
|:--|:--|:--|
| 用途 | PDF → Markdown 结构化解析 | 公式图片 → LaTeX 跨模态对齐 |
| 部署位置 | 宿主机（Windows） | WSL2 容器 |
| 模型尺寸 | 大模型（>10B OCR） | 1.2B 稠密模型 |
| 推理速度 | ~42s/篇（PDF 解析） | ~1.5s/图（公式识别） |
| 依赖 | MinerU 服务 | vLLM + PyTorch CUDA |

---

## 3. 三轨资源调度器部署

`resource_scheduler.py`（`benchmark/agent/resource_scheduler.py`）是系统的 Layer 2 核心组件。它负责：

- **健康检查**：8 路独立探活，零密钥泄露
- **Provider 参数管理**：从 `agent_capabilities.json` 加载各 Provider 的模型/端点/温度/超时配置
- **客户端工厂**：每 Provider 独立客户端实例
- **自动降级**：按 resource_type 级联回退

### 3.1 三轨五 Provider 决策

| 轨道 | Provider | 用途 | 认证方式 |
|:----:|----------|------|----------|
| 1 | **DeepSeek API** | Intent Router / Judge / 文本生成 | `OPENAI_API_KEY` → `Authorization: Bearer` |
| 1 | **MiMo-V2.5 原生视觉** | 跨模态审计 — 图片→公式语义判决 | `MIMO_API_KEY` → `api-key` header (raw httpx) |
| 1 | **MiMo / MiniMax 文本** | 补充题目生成 | `MIMO_API_KEY` / `MINIMAX_API_KEY` |
| 2 | **Ollama 本地** | 本地 Judge / 本地评测 / --local 模式 | 无密钥 |
| 3 | **vLLM WSL2** | MinerU-1.2B VLM 公式识别 | 无密钥（本机端口） |
| — | **MinerU 本地 API** | 科学文档 PDF/PPTX/HTML 解析 | `MINERU_API_BASE` |

### 3.2 健康检查验证

Agent 启动时自动执行 8 路健康检查：

```powershell
conda run -n myenv python -c "
from benchmark.agent.resource_scheduler import get_global_scheduler
s = get_global_scheduler()
status = s.check_health()
print(status.summary)
"
```

**健康检查输出示例**：
```
ResourceStatus @ 2026-05-10T09:30:00
  ✅ deepseek          available     连通正常
  ✅ mimo_vision       available     连通正常
  ✅ mimo_text         available     连通正常
  ✅ minimax           available     连通正常
  ✅ ollama_chat       available     连通正常
  ✅ ollama_compat     available     连通正常
  ❌ mineru            unavailable   MinerU API 未启动
  ❓ gpu               unknown       GPU 检测超时
```

每种 Provider 有独立的超时（5s）和 TTL（30s，缓存避免频繁探活）。

### 3.3 Provider 参数映射

`agent_capabilities.json` 的 `resource_scheduler_config.provider_parameter_map` 定义了各 Provider 的精确调用参数。关键配置：

| Provider | 子类型 | 模型 | base_url | client_type | 特殊说明 |
|----------|:------:|------|----------|:-----------:|----------|
| deepseek | chat | deepseek-v4-flash | `https://api.deepseek.com` | openai | `proxy=None` |
| mimo | vision | mimo-v2.5 | `https://api.xiaomimimo.com/v1` | raw_httpx | `thinking:disabled`, `api-key header` |
| mimo | text | mimo-v2-flash | `https://api.xiaomimimo.com/v1` | openai | — |
| minimax | chat | minimax-2.5 | `https://api.minimaxi.com/anthropic` | anthropic | Anthropic 兼容接口 |
| ollama | chat | qwen3.5:9b | `http://localhost:11434` | raw_httpx | `/api/chat` + `think:false` |
| ollama | completions | qwen3.5:9b | `http://localhost:11434` | openai | `/v1/chat/completions` |
| vllm | vision | MinerU2.5-2509-1.2B | `http://localhost:8000` | raw_httpx | WSL2 容器，`/v1/completions`，非默认注册 |

### 3.4 验证调度器

```powershell
# 验证调度器能正确解析所有 12 个 intent 的资源需求
conda run -n myenv python -c "
from benchmark.agent.resource_scheduler import get_global_scheduler
s = get_global_scheduler()
for intent_id in ['arxiv_search','mineru_parse','corpus_parse','cross_modal_audit',
                   'corpus_quality_report','benchmark_build','quality_arbitrate',
                   'model_evaluate','multi_judge_compare','leaderboard_viz',
                   'local_finetune','reproduce_all','multi_format_parse']:
    r = s.resolve(intent_id)
    print(f'{intent_id:25s} → {r.provider:12s} {r.sub_type:10s} {r.model}')
"
```

---

## 4. 跨模态审计引擎部署

`visual_audit.py`（`benchmark/agent/visual_audit.py`）是赛道二核心差异化武器。它使用 MiMo-V2.5 原生全模态视觉模型，对语料中的科学图片和 LaTeX 公式进行语义一致性审计。

### 4.1 核心特性

| 特性 | 规格 |
|------|------|
| 视觉引擎 | MiMo-V2.5 (mimo-v2.5) — 原生全模态，40 图像 token |
| 兜底引擎 | MiniMax (MiniMax-M2.5-highspeed) — 综合对齐质量 79.3% |
| 推理速度 | ~4.7s/图（MiMo）、~8.8s/图（MiniMax） |
| 并发 | 5 线程 ThreadPoolExecutor |
| 断点续跑 | checkpoint 每 50 条原子写入 |
| 图片来源 | 6,204 含图 chunk（23 教材 + 339 arXiv），11,554 张图片 |
| 审计指标 | `alignment_pass_rate`, `per_image_judgment`, `failure_reasons` |

### 4.2 Provider 选择

通过环境变量 `VISION_PROVIDER` 切换：

```powershell
# 默认：MiMo-V2.5（更严格、更快）
$env:VISION_PROVIDER = "mimo"

# 兜底：MiniMax（交叉验证用）
$env:VISION_PROVIDER = "minimax"
```

### 4.3 执行审计

```powershell
# 全量扫描（默认 5 线程，断点续跑）
conda run -n myenv python benchmark/agent/visual_audit.py --workers 5 --resume

# 限量调试（审计前 100 张图片）
conda run -n myenv python benchmark/agent/visual_audit.py --max-items 100

# 单图测试验证 MiMo 识别能力
conda run -n myenv python benchmark/agent/visual_audit.py --test

> `--resume` 本身就会自动跳过已完成条目，无需单独的 `--retry-failed` 参数。

### 4.4 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--workers` | 5 | 并发线程数（建议 5-8） |
| `--max-items` | None（全量） | 最大审计图片数（调试用，None=全量） |
| `--resume` | false | 从 checkpoint 恢复（自动跳过已完成条目） |
| `--test` | false | 单图测试模式 |
| `--provider` | 环境变量 `VISION_PROVIDER` | 覆盖视觉 Provider：`mimo` 或 `minimax` |

### 4.5 审计产出

| 文件 | 格式 | 说明 |
|------|------|------|
| `visual_audit_results.jsonl` | JSONL | 逐条审计结果（图片引用+对应公式+语义判决） |
| `visual_audit_checkpoint.json` | JSON | 断点续跑 checkpoint |
| `visual_audit_report.json` | JSON | 汇总统计报告（通过率/失败原因分布） |

### 4.6 与 Intent Router 集成

跨模态审计在 agent_cli.py 中通过 intent `cross_modal_audit` 自动调度：

```powershell
# 自然语言触发
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    "审计这批 arXiv 论文的公式-图片跨模态对齐质量"

# 手动指定 intent 序列
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents corpus_parse,cross_modal_audit,corpus_quality_report
```

---

## 5. Agent CLI — 13 intent × LLM Intent Router

`agent_cli.py`（`benchmark/agent/agent_cli.py`）是系统的 Layer 1+3 核心入口。它将用户的自然语言请求通过 LLM few-shot 拆解为可执行的 intent 序列，然后逐步执行并验证。

### 5.1 基本用法

```powershell
# 自然语言驱动（DeepSeek v4-flash 自动拆解）
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    "全量复现整个评测流程"

# 指定 intent 序列（跳过 Intent Router）
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents corpus_parse,benchmark_build,quality_arbitrate,model_evaluate,leaderboard_viz

# dry-run 验证计划（不实际执行）
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --dry-run "评测 deepseek-v4-flash 模型"
```

### 5.2 完整参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `input` | 无（必填之一） | 自然语言任务描述 |
| `--intents` / `-i` | 无 | 手动指定 intent 序列，逗号分隔 |
| `--dry-run` / `-n` | false | 干跑模式：仅生成计划不执行 |
| `--local` / `-l` | false | 本地模式：Resource Scheduler 降级至 Ollama/MinerU（Intent Router 仍用 DeepSeek） |
| `--max-retries` | 2 | 每步最大重试次数 |
| `--no-verify` | false | 禁用 LLM 验证 |
| `--output-log` / `-o` | `logs/{task_id}.json` | 执行日志 JSON 输出路径 |
| `--list-intents` | false | 列出所有可用 intent |
| `--version` / `-V` | false | 显示版本号 |

### 5.3 本地降级模式（--local）

`--local` 模式是赛道二的隐私双路径核心特性。启用后 Resource Scheduler 将 API 类 intent 的 Provider 降级至本地：

```powershell
# 本地模式：Resource Scheduler 降级至 Ollama（Intent Router 仍用 DeepSeek）
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --local "生成语料质量报告"

# 本地模式指定 intent
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --local --intents corpus_parse,corpus_quality_report
```

`--local` 模式下，Resource Scheduler 将 API 类 intent 的 provider 降级至 Ollama 或 script，详情见下表：

| 原路径 | `--local` 降级至 | 说明 |
|--------|-----------------|------|
| DeepSeek API | Ollama qwen3.5:9b | `_resolve_local` 将各 intent 映射至 `ollama` |
| MiMo-V2.5 视觉 | 由 `VISION_PROVIDER` 控制 | resolve 降级至 `ollama`，但 Executor 执行 `visual_audit.py` 时视觉引擎由 `VISION_PROVIDER` 环境变量决定（默认 MiMo） |
| MiniMax API | Ollama qwen3.5:9b | 同上 |
| MinerU API | 本地 MinerU | corpus_parse 映射至 `mineru` |
| vLLM WSL2 | 不可降级（WSL2 内无备选） | vLLM 仅用于公式识别对比实验，非核心路径 |

> **注意**：`--local` 仅影响 Resource Scheduler 的 resolve 策略。**Intent Router（Layer 1）始终调用 DeepSeek v4-flash**，不受 local_mode 影响。

### 5.4 Intent 序列示例

**intent 0 — arXiv 论文检索（数据飞轮起点）**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents arxiv_search
```

**intent 1 — 文档解析（原始 PDF→Markdown）**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents mineru_parse
```

**intent 2 — 语料解析**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents corpus_parse
```

**intent 3 — 跨模态审计**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents cross_modal_audit
```

**intent 4 — 语料质量报告**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents corpus_quality_report
```

**intent 5 — 评测数据集构建**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents benchmark_build
```

**intent 6 — 质量仲裁**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents quality_arbitrate
```

**intent 7 — 模型评测**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents model_evaluate
```

**intent 8 — 多 Judge 对比**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents multi_judge_compare
```

**intent 9 — 排行榜可视化**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents leaderboard_viz
```

**intent 10 — 本地微调**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents local_finetune
```

**intent 11 — 全量复现**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents reproduce_all
```

**intent 12 — 多格式文档解析（PPTX/HTML/扫描件）**
```powershell
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents multi_format_parse
```

### 5.5 执行日志

Agent 每次执行自动生成结构化 JSON 日志，保存至 `benchmark/agent/logs/`（可通过 `--output-log` 自定义路径）：

```json
{
  "schema_version": "1.0",
  "task_id": "agent-20260508-153000",
  "task_name": "审计这批 arXiv 论文的跨模态对齐质量",
  "steps": [
    {
      "schema_version": "1.0",
      "step_id": 1,
      "step_name": "cross_modal_audit (跨模态对齐审计)",
      "tool": "visual_audit.py + MiMo-V2.5 原生视觉",
      "input_summary": "{\"source\": \"corpus/chunks/\", \"concurrency\": 5, \"resume\": true}",
      "output_summary": "✅ Audit complete: 4935 images, 79.3% alignment pass rate",
      "status": "success",
      "duration_ms": 1080000,
      "timestamp": "2026-05-08 15:30:45",
      "error": null
    }
  ],
  "total_duration_ms": 1080000,
  "final_status": "completed",
  "created_at": "2026-05-08 15:12:45"
}
```

---

## 6. 故障恢复矩阵

系统设计了四层容错机制，覆盖 Provider 不可用、API 超时、JSON 解析失败、Ollama 熔断等常见故障。

### 6.1 故障恢复路线图

```
故障发生
    │
    ▼
┌─ HealthCheck 检测 ─────────────────────┐
│  ● Provider 不可用 → 标记 UNAVAILABLE  │
│  ● 超时/限流 → 标记 DEGRADED          │
│  ● TTL 30s 缓存，避免频繁探活          │
└────────────────────────────────────────┘
    │
    ▼
┌─ Resource Scheduler 解析 ─────────────┐
│  ● resolve(intent_id) 硬编码映射，     │
│    不检查健康状态                      │
│  ● --local 模式降级至 Ollama/script  │
│  ● 执行层超时 → 进入 fallback           │
└────────────────────────────────────────┘
    │
    ▼
┌─ Executor 执行 ───────────────────────┐
│  ● _run_subprocess timeout 保护       │
│  ● 规则 10.2.2: 每步原子写入 LogStep  │
└────────────────────────────────────────┘
    │
    ▼
┌─ Verifier 验证 → score<0.5? ──────┐
│  ├─ ✅ pass → 进入下一步             │
│  ├─ ❌ fail, 有重试机会 → 🔄 retry  │
│  │     → get_fallback() → script  │
│  │     → 切换 Provider 重试          │
│  └─ ❌ fail, 无重试机会 → 记录失败    │
└──────────────────────────────────────┘
```

### 6.2 Provider 级降级

> **重要说明**：`resolve()` 是硬编码映射，不检查健康状态。真正的 fallback 发生在 **Executor 层超时后**，由 `get_fallback()` 执行。所有 Provider 的 fallback 目标均为 `script`（本地脚本），不是另一个 Provider。

| 故障模式 | 检测层 | 降级策略（代码实际行为） |
|----------|---------|--------------------------|
| DeepSeek API 执行超时 | Executor `_run_subprocess` | `get_fallback()` → script（本 intent 以本地脚本执行） |
| MiMo-V2.5 视觉 404 | Executor 执行报错 | `get_fallback()` → script（本 intent 以本地脚本执行） |
| MiniMax 限流 429 | Executor 执行报错 | `get_fallback()` → script |
| Ollama 服务未启动 | Executor 执行报错 | `get_fallback()` → script |
| MinerU API 未监听 | Executor 执行报错 | `get_fallback()` → script |
| vLLM WSL2 未启动 | Executor 执行报错 | 无 fallback（对比实验可选，跳过不影响核心链路） |
| Ollama Judge 熔断 | `--max-consecutive-failures` 阈值 | API Judge = 5, Ollama Judge ≥ 10 |
| JSON 解析失败 | `_extract_json_block()` 两层回退 | 修复 JSON (尾逗号清理) → 重试 |

### 6.3 Resource Type 级降级

定义于 `agent_capabilities.json` 的 `resource_scheduler_config.fallback_order`：

| 资源类型 | 允许降级至 | 超时 |
|:--------:|:-----------:|:----:|
| api | script | 120s |
| local_api | script | 300s |
| local_gpu | script | 3600s |
| script | 不降级 | 600s |

### 6.4 重试 + 验证闭环

每步执行自动经历 `Execute → LLM Verify → Auto-fallback` 闭环：

```
Step 失败 ── 首次自动重试 (provider 不变)
  ├── 成功 → ✅ 继续
  └── 失败 → 🔄 二次重试 (降级 provider)
       ├── 成功 → ✅ 继续
       └── 失败 → ❌ 记录失败，继续下一步
```

- 最大重试次数：`--max-retries 2`（默认）
- Verify 失败判定：`score < 0.5`
- 降级检测：`scheduler.get_fallback(resolved)` 返回备选 Provider

### 6.5 隐私双路径

| 模式 | API 依赖 | 适用场景 |
|:----:|:--------:|----------|
| **默认** | DeepSeek + MiMo + MinerU + vLLM（可选） | 全功能模式 |
| **--local** | 仍有 DeepSeek（Intent Router） | 减少 API 调用量，适合轻度规划场景 |

`--local` 模式下：
- **Intent Router（Layer 1）始终调用 DeepSeek**，不受 local_mode 影响
- Resource Scheduler（Layer 2）将 API 类 intent 降级至 Ollama（`_resolve_local` 映射）
- cross_modal_audit 映射至 `ollama`，但 Executor 仍执行 `visual_audit.py`（视觉由 MiMo/MiniMax 提供）
- `--local` 不等于零 API，仅减少了执行层的外部 API 依赖

### 6.6 断点续跑

系统在多个层面支持断点续跑：

| 组件 | 恢复机制 | 粒度 |
|------|---------|:----:|
| visual_audit.py | `--resume` + checkpoint (每 50 条) | 逐条 |
| evaluate.py | `--resume` + `--retry-failed` | 逐题 |
| build_benchmark.py | `--resume` + checkpoint (每 15 题) | 逐题 |
| agent_cli.py | 重新运行跳过已完成步骤 | 按 step |
| reproduce_all | `skip_existing=True` 检测已有产出 | 按 intent |

---

## 7. 语料准备

### 7.1 语料来源

ControlSci 语料库包含两类来源：

| 来源 | 数量 | 格式 | 存储位置 |
|------|:----:|:----:|---------|
| 控制科学教材 | 23 本 | PDF | `data/pdf/textbooks/` |
| arXiv 论文 | 339 篇 | PDF | `data/pdf/arXiv/` |

### 7.2 语料解析（MinerU）

对应 intent `corpus_parse`，或直接使用 MinerU 命令行：

```powershell
# 批量解析教材
conda run --no-capture-output -n myenv magic-pdf -p data/pdf/textbooks/ -o corpus/parsed/textbooks/ -m auto

# 批量解析 arXiv 论文
conda run --no-capture-output -n myenv magic-pdf -p data/pdf/arXiv/ -o corpus/parsed/arxiv/ -m auto
```

> **性能参考**：arXiv 论文平均解析速度约 42 秒/篇（62% 固定开销），教材约 60 页/分钟。

### 7.3 多格式解析测试素材

对应 intent `multi_format_parse`，需准备以下三类测试文件：

| 格式 | 建议来源 | 存储位置 |
|:----:|---------|---------|
| PPTX | 控制科学课件（教材配套幻灯片） | `benchmark/agent/test_materials/` |
| HTML | arXiv 论文页面（保存为 .html） | `benchmark/agent/test_materials/` |
| 扫描件图片 | 公式密集页（教材截图） | `benchmark/agent/test_materials/` |

```powershell
# 多格式解析：指定文件列表
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py `
    --intents multi_format_parse

# 直接调用 mineru_to_md.py（跳过 Agent 编排）
conda run --no-capture-output -n myenv python tools/mineru_to_md.py `
    --input benchmark/agent/test_materials/ --output benchmark/agent/test_materials/md/ `
    --skip-existing --stats
```

产出的 `parse_result_*.md` 文件按 chunk 数/公式提取率/图片保留率三维度对比各格式的解析质量差异。

---

## 8. 题目生成

### 8.1 三 Provider 并行生成

对应 intent `benchmark_build`，或直接使用 `build_benchmark.py`：

```powershell
# DeepSeek 生成（默认）
conda run --no-capture-output -n myenv python benchmark/pipeline/build_benchmark.py `
  --corpus corpus --provider deepseek --limit 50 `
  --output benchmark/dataset/benchmark.json `
  --manual-review-output benchmark/dataset/manual_review.json

# MiniMax 生成
conda run --no-capture-output -n myenv python benchmark/pipeline/build_benchmark.py `
  --corpus corpus --provider minimax --limit 50 `
  --output benchmark/dataset/benchmark_minimax.json `
  --manual-review-output benchmark/dataset/manual_review_minimax.json

# MiMo 生成
conda run --no-capture-output -n myenv python benchmark/pipeline/build_benchmark.py `
  --corpus corpus --provider mimo --limit 50 `
  --output benchmark/dataset/benchmark_mimo.json `
  --manual-review-output benchmark/dataset/manual_review_mimo.json
```

### 8.2 关键参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--corpus` | `corpus/` | 语料库根目录 |
| `--provider` | `deepseek` | Provider：`deepseek` / `minimax` / `mimo` |
| `--limit` | 10 | 生成题目数量 |
| `--output` | `benchmark/dataset/benchmark.json` | 输出 JSON 路径 |
| `--resume` | false | 从 checkpoint 恢复 |
| `--supplement` | 0 | 追加生成 N 题到已有 benchmark.json |
| `--reset-every` | 15 | 每 N 题重建 OpenAI 客户端 |

### 8.3 Checkpoint 机制

生成过程自动保存 checkpoint 到 `benchmark/archive/checkpoint/`。若生成中断：

```powershell
conda run --no-capture-output -n myenv python benchmark/pipeline/build_benchmark.py `
  --corpus corpus --provider deepseek --limit 50 --resume `
  --output benchmark/dataset/benchmark.json `
  --manual-review-output benchmark/dataset/manual_review.json
```

---

## 9. 质量仲裁

### 9.1 双层 LLM 仲裁

对应 intent `quality_arbitrate`，使用 DeepSeek 进行 Embedding 快速通道 + LLM 深度评审：

```powershell
conda run --no-capture-output -n myenv python benchmark/pipeline/build_benchmark.py `
  --arbitrate --output benchmark/dataset/benchmark.json `
  --manual-review-output benchmark/dataset/manual_review.json
```

### 9.2 仲裁参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--arbitrate-workers` | 3 | 并行仲裁 API 调用数 |
| `--arbitrate-max-tokens` | 1024 | 单次仲裁响应最大 token 数 |

### 9.3 仲裁状态流转

```
生成 → needs_review → [Embedding 快速通道] → auto_passed
                   └→ [LLM 深度评审] → reviewed_kept / reviewed_discarded
```

### 9.4 孤儿回收

```powershell
conda run --no-capture-output -n myenv python benchmark/pipeline/orphan_judge.py
```

> 孤儿回收使用 DeepSeek API，单轮调用，185 题约 9 分钟完成，通过率约 61.6%。

---

## 10. 数据集构建 + 评测 + 报告

### 10.1 数据集拆分

```powershell
conda run --no-capture-output -n myenv python benchmark/pipeline/split_benchmark.py `
  --input benchmark/dataset/merged.json --seed 42
```

| 文件 | 题数 | 说明 |
|------|:----:|------|
| `benchmark/dataset/core.json` | 500 | 核心集：A/B/C/D 各 125 |
| `benchmark/dataset/full.json` | 889 | 全量可用集 |
| `benchmark/dataset/merged.json` | 1,109 | 候选池 |

### 10.2 模型评测

对应 intent `model_evaluate`，支持 API / Ollama 双模式：

```powershell
# API 模型评测（DeepSeek）
conda run --no-capture-output -n myenv python benchmark/eval/evaluate.py `
  --mode model --input benchmark/dataset/core.json `
  --target-model deepseek-v4-flash --judge-model deepseek-v4-flash `
  --base-url https://api.deepseek.com `
  --output benchmark/eval/reports/deepseek-v4-flash_report.json `
  --resume --retries 3 --max-consecutive-failures 5

# 本地模型评测（Ollama qwen3.5:9b）
conda run --no-capture-output -n myenv python benchmark/eval/evaluate.py `
  --mode model --input benchmark/dataset/core.json `
  --target-model qwen3.5:9b --target-base-url http://localhost:11434/v1 `
  --target-api-key ollama `
  --judge-model deepseek-v4-flash --judge-base-url https://api.deepseek.com `
  --output benchmark/eval/reports/qwen3.5-9b_report.json `
  --resume --retries 3 --max-consecutive-failures 10
```

> **关键**：Ollama Judge 的 `--max-consecutive-failures` 必须设为 **10** 而非默认 5（规则 10.8.3）。C/D 维低分易被误判为失败。

### 10.3 排行榜 + 可视化

对应 intent `leaderboard_viz`：

```powershell
# 生成排行榜 JSON
conda run --no-capture-output -n myenv python benchmark/eval/summarize_multi.py `
  --input benchmark/eval/reports --output benchmark/eval/reports/leaderboard.json

# 生成可视化 HTML + PNG
conda run --no-capture-output -n myenv python benchmark/eval/report_viz.py `
  --input benchmark/eval/reports/leaderboard.json `
  --output benchmark/eval/reports/leaderboard.html
```

### 10.4 HuggingFace 导出

```powershell
conda run --no-capture-output -n myenv python benchmark/pipeline/export_dataset.py `
  --input benchmark/dataset/core.json --output huggingface/control-sci-corpus

# 推送到 HuggingFace Hub
conda run --no-capture-output -n myenv python benchmark/pipeline/export_dataset.py `
  --input benchmark/dataset/core.json --output huggingface/control-sci-corpus `
  --push-to-hub "your-username/control-sci-benchmark" --hf-token "hf_xxx"
```

---

## 11. 目录结构

```
MinerU/
├── benchmark/
│   ├── agent/                    # Data Agent 核心层
│   │   ├── __init__.py
│   │   ├── agent_cli.py          # Layer 1+3: Intent Router + Executor + Verifier
│   │   ├── agent_capabilities.json  # 13 intent 能力注册表
│   │   ├── resource_scheduler.py # Layer 2: 三轨资源调度器
│   │   ├── visual_audit.py       # 跨模态审计引擎（MiMo-V2.5 原生视觉）
│   │   ├── log_schema.py         # 日志 Schema 定义
│   │   ├── agent.py              # 原 v1 ControlSciAgent（向后兼容）
│   │   ├── _validate_capabilities.py  # capabilities.json 校验
│   │   ├── _verify_10_intents.py      # 13 intent 验收脚本
│   │   ├── test_materials/       # 多格式解析测试素材（PPTX/HTML/图片）
│   │   ├── logs/                 # 执行日志 JSON
│   │   ├── results/              # visual_audit 审计产出
│   │   └── examples/             # 12 个示例脚本
│   │       ├── run_task_1_corpus.py
│   │       ├── run_task_2_arbitrate.py
│   │       ├── run_task_3_eval.py
│   │       ├── run_task_4_recovery.py
│   │       ├── run_task_5_transfer.py
│   │       └── logs/             # 示例执行日志
│   ├── dataset/                  # 数据集 JSON
│   │   ├── core.json             # 核心集（500 题）
│   │   ├── full.json             # 全量集（889 题）
│   │   └── schema.json           # 数据 Schema
│   ├── pipeline/                 # 数据生成管线
│   │   ├── build_benchmark.py    # 题目生成 + 仲裁入口
│   │   ├── split_benchmark.py    # core/full 拆分
│   │   ├── merge_benchmarks.py   # 多路合并
│   │   ├── orphan_judge.py       # 孤儿题回收
│   │   ├── validate_benchmark.py # 数据校验
│   │   └── export_dataset.py     # HuggingFace 导出
│   └── eval/                     # 评测引擎
│       ├── evaluate.py           # 评测入口
│       ├── judge.py              # LLM-as-Judge 评分器
│       ├── summarize_multi.py    # 多模型排行榜
│       ├── report_viz.py         # 可视化
│       └── reports/              # 评测报告输出
├── corpus/                       # 语料解析产物（chunk、元数据、统计）
├── data/                         # 原始数据源
│   ├── pdf/textbooks/            # 23 本控制科学教材 PDF
│   ├── pdf/arXiv/                # 339 篇 arXiv 论文 PDF
│   └── sources_flywheel/         # 数据飞轮论文 PDF
├── tools/                        # 辅助工具
│   └── mineru_to_md.py           # MinerU 解析封装（多格式支持）
├── docs/
│   └── agent/
│       ├── deploy.md             # 本文档
│       └── agent_report.md       # 技术报告
└── finetune/                     # QLoRA 微调模块
    ├── train_qlora.py
    └── data/                     # 微调数据集
```

---

## 12. 快速验证清单

完成部署后，按以下顺序验证各组件是否正常工作：

```powershell
# 1. 环境检查
conda run -n myenv python -c "import openai; import anthropic; import httpx; print('deps OK')"

# 2. Provider 健康检查（8 路）
conda run -n myenv python -c "
from benchmark.agent.resource_scheduler import get_global_scheduler
s = get_global_scheduler()
print(s.check_health().summary)
"

# 3. Agent CLI 模块 import
conda run -n myenv python -c "
from benchmark.agent.agent_cli import ControlSciAgentCLI, IntentRegistry, IntentRouter, Executor, Verifier
print('agent OK')
"

# 4. 13 intent 能力注册表验证
conda run -n myenv python benchmark/agent/_validate_capabilities.py

# 5. 13 intent dry-run 验收
conda run --no-capture-output -n myenv python benchmark/agent/_verify_10_intents.py

# 6. agent_cli.py dry-run（自然语言）
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py --dry-run "审计跨模态对齐质量"

# 7. agent_cli.py dry-run（--local 模式）
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py --dry-run --local "生成语料质量报告"

# 8. visual_audit 单图测试
conda run -n myenv python benchmark/agent/visual_audit.py --test

# 9. 数据校验
conda run --no-capture-output -n myenv python benchmark/pipeline/validate_benchmark.py --input benchmark/dataset/core.json

# 10. Reference 评测测试
conda run --no-capture-output -n myenv python benchmark/eval/evaluate.py --mode reference --input benchmark/dataset/core.json --output test_ref.json
Remove-Item test_ref.json -ErrorAction SilentlyContinue

# 11. Mock 生成测试
conda run --no-capture-output -n myenv python benchmark/pipeline/build_benchmark.py --mock --limit 3 --output test_mock.json --manual-review-output test_review.json
Remove-Item test_mock.json, test_review.json -ErrorAction SilentlyContinue

# 12. (可选) vLLM WSL2 独立连通性（非 HealthCheck 内置，需单独验证）
conda run -n myenv python -c "
import httpx
r = httpx.get('http://localhost:8000/v1/models', timeout=5)
print(f'vLLM: {r.status_code}')
"

# 13. (可选) 多格式解析 dry-run
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py --dry-run "把 PPTX 课件转成结构化文本"
```

全部通过即部署成功。

---

## 13. 常见问题排查

### 13.1 MiMo-V2.5 视觉 API 返回 404

**症状**：visual_audit.py 返回 HTTP 404。

**原因**：使用了 `mimo-v2.5-pro` 模型（长推理模型，不支持图像输入）。视觉模型必须是 `mimo-v2.5`（原生全模态）。

**解决**：
- 确认 `agent_capabilities.json` 中 `mimo.vision.model` 为 `mimo-v2.5`
- MiMo 视觉调用必须使用 **raw httpx** + `api-key` header，严禁 OpenAI SDK
- 必须设置 `thinking:disabled`

### 13.2 Ollama Judge 熔断误杀

**症状**：Ollama Judge 评测到一半进程退出，日志显示 "max consecutive failures reached"。

**原因**：C/D 维低分被误判为失败，默认 `--max-consecutive-failures 5` 过激。

**解决**：Ollama Judge 必须使用 `--max-consecutive-failures 10`，与 API Judge (5) 区分。

### 13.3 Ollama 推理链占用过多 token

**症状**：Qwen 3.5 评测时 `content` 字段为空，max_tokens 被推理链耗尽。

**解决**：
- `/api/chat`（原生，推荐）：设置 `think:false`
- `/v1/chat/completions`（兼容）：设置 `reasoning_effort='none'`

### 13.4 Import 路径错误

**症状**：`ModuleNotFoundError: No module named 'benchmark'`。

**解决**：确保从项目根目录运行脚本。`:file_path` 模块已在 `agent_cli.py` 和 `resource_scheduler.py` 中自动处理：

```python
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
```

### 13.5 Conda 编码崩溃

**症状**：`UnicodeDecodeError: 'gbk' codec can't decode byte`。

**解决**：所有子进程调用必须使用：
```powershell
$env:PYTHONIOENCODING='utf-8'
$env:CONDA_NO_PLUGINS='true'
conda run --no-capture-output -n myenv python ...
```

### 13.6 MiniMax 限流

**症状**：MiniMax API 返回 429 错误。

**解决**：MiniMax 限流阈值约 40 题/路。使用 `--limit` 分批生成，或降低 `--arbitrate-workers`。

### 13.7 DeepSeek v4 系列 JSON 截断

**症状**：Intent Router 返回的 JSON 计划不完整（被截断）。

**解决**：中文 JSON 输出场景 `max_tokens` 至少 4096（当前默认值）。`agent_cli.py` 和 `resource_scheduler.py` 中已统一设置为 4096。

### 13.8 Checkpoint 文件损坏

**症状**：`--resume` 后数据异常。

**解决**：删除对应 checkpoint 文件后重新运行：

```powershell
Remove-Item benchmark/archive/checkpoint/*.checkpoint.json
Remove-Item benchmark/agent/results/visual_audit_checkpoint.json
```

### 13.9 vLLM WSL2 连通失败

**症状**：vLLM 调用超时或端口不可达。

**原因**：WSL2 未启动 / vLLM 服务未运行 / 端口冲突。

**解决**：
1. 确认 WSL2 已启动：`wsl --list --verbose`
2. WSL 内确认 vLLM 进程运行：`ps aux | grep vllm`
3. 检查端口占用：WSL 内 `ss -tlnp | grep 8000`
4. 宿主机 → WSL 端口转发：`netsh interface portproxy show v4tov4`
5. 如端口被占，改用 `--port 8001` 并更新 `agent_capabilities.json` 的 `vllm.base_url`

> vLLM 是可选组件（仅用于 MinerU-1.2B VLM 公式识别对比实验），不影响核心评测链路。启动失败时跳过即可。
