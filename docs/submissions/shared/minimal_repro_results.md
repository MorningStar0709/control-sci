# ControlMind 最小真实闭环复现记录

> 日期：2026-05-15
> 目录：`docs/submissions/`
> 本文件定位：记录三赛道最小真实闭环的执行结果，说明数据校验、Agent、真实小样本评测、Medical RAG 检索与 FastAPI 均可在统一复现路径中跑通。

---

## 1. 复现策略

本项目采用分层复现策略。完整 500 题评测、QLoRA 全量训练和 Medical RAG 全量重建索引均属于报告级或完整离线复现任务，成本高、耗时长；最小真实闭环则用于验证关键路径可执行、可恢复、可审计。

我们采用三层复现策略：

| 层级 | 目标 | 默认命令 | 使用场景 |
|---|---|---|---|
| L1 秒级证据 | 确认三赛道交付物存在且可读 | `conda run --no-capture-output -n myenv python demo/cli/controlscidemo all --quick` | 样例回放 |
| L2 最小真实闭环 | 跑通数据校验、真实 API 小样本评测、leaderboard、Agent 校验、Medical RAG 检索/API | `.\run_minimal_repro.ps1 -Limit 10` | 关键路径复现 |
| L3 完整离线复现 | 500 题评测、QLoRA、索引重建 | `--limit 0 --resume` 或赛道报告附录命令 | 报告级复现 |

本文件记录的是 L2 最小真实闭环结果。

---

## 1.1 实验代码与测试代码边界

为避免把高可用 smoke 验证误读为正式实验结果，项目在代码入口上区分两类运行模式：

| 类别 | 目标 | 典型入口 | 数据与输出原则 |
|---|---|---|---|
| 正式实验 / 报告复现代码 | 复现报告中的完整或报告级结果 | `.\run_agent.ps1 -Profile report`、`python benchmark/eval/run_eval_pipeline.py --profile report`、`python -m controlsci.medical.kb_quality --profile report` | 默认读取并写入项目真实路径，如 `benchmark/dataset/`、`benchmark/eval/results/`、`data/sources_medical/` |
| 最小真实闭环 / 高可用测试代码 | 验证链路可运行、可恢复、可审计，不追求全量覆盖 | `.\run_agent.ps1 -Profile smoke`、`.\run_minimal_repro.ps1 -Limit 10`、`.\run_reviewer_demo.ps1`、`controlscidemo ... --quick` | 默认少量样本、跳过长任务；需要隔离落盘时由测试命令显式传入 `_scratch/...` 输出目录 |
| dry-run / 计划校验代码 | 验证参数、Intent 注册、路径和失败边界，不执行真实长流程 | `agent_cli.py --dry-run --intents reproduce_all`、`tools/mineru_to_md.py --dry-run ...` | 不作为实验分数来源；仅作为工程健康和安全边界证据 |

当前约定：

- `smoke` 是高可用测试 profile：限制样本量，默认跳过 QLoRA、35B Judge、全量索引重建等长任务。
- `report` 是报告级复现 profile：保留完整评测、完整 Judge/分析或报告所需的长流程。
- 正式入口的默认路径应保持为真实项目路径；临时目录只允许作为测试命令的显式参数使用，不能替换源码默认值。
- 最小测试产生的新结果不得覆盖报告已固化数据；需要真实执行时，应显式设置独立输出目录或使用已有 `minimal_repro`/`_scratch` 隔离目录。

因此，本文件中的 L2 结果用于说明系统高可用与闭环真实可执行；报告中的定量结论仍以 L3/报告级产物和 `shared/DATA-TRACE.md` 中的权威源文件为准。

---

## 2. 环境状态

测试时 GPU 与本地模型服务状态：

```text
GPU 初始状态：274 MiB / 24463 MiB, utilization 0%
Ollama：可访问 http://localhost:11434/api/tags
可见模型：qwen3-embedding:4b, qwen3.5:35b, qwen3.5:9b, qwen3.5:4b, qwen3.5:2b, llama3.2:3b, gemma3:4b
```

说明：最小闭环测试会触发本地 embedding 通路。测试结束后显存可能有 Ollama 模型驻留，但 GPU utilization 为 0% 时不代表仍在进行重计算。

---

## 3. Track1 / 评测链路

命令：

```powershell
.\run_minimal_repro.ps1 -Limit 10
```

结果：

```text
ExitCode: 0
总耗时：首次真实评测约 6 分 14 秒；resume 复跑约 23 秒
数据集校验：通过
真实 API 小样本评测：10/10 completed，balanced-mini A/B/C/D 覆盖
overall_score: 0.582
dimension_scores: {"A": 0.5333, "B": 0.4, "C": 1.0, "D": 0.51}
leaderboard.json：生成成功
leaderboard.html：生成成功
核心卫生检查：5/5 passed
Failed: 0
Skipped: 0
```

产物：

```text
benchmark/eval/results/minimal_repro/eval_deepseek-v4-flash.json
benchmark/eval/results/minimal_repro/leaderboard.json
benchmark/eval/results/minimal_repro/leaderboard.html
```

注意：

- `Limit 10 + balanced-mini` 用于验证真实 API/Judge/Resume/Leaderboard 链路可运行，并避免只抽到单一维度。
- balanced-mini 按 A/B/C/D round-robin 抽样；10 题覆盖 A=3、B=3、C=2、D=2。
- 完整 500 题评测支持 `--limit 0 --resume`，属于报告级复现任务。

---

## 4. 数据集校验

命令：

```powershell
python benchmark/eval/validate_dataset.py
```

关键结果：

```text
core.json: 500 questions
A=125 B=125 C=125 D=125
rubric=125/125
duplicate IDs=0
```

备注：

```text
47 C-dim sibling refs missing (expected: siblings span core+full)
```

这是预期 warning：部分 sibling 关系跨 `core.json` 与 `full.json`，不是数据错误。

---

## 5. Track2 Agent 最小闭环

命令：

```powershell
python benchmark/agent/agent_cli.py --dry-run --intents reproduce_all
```

结果：

```text
ExitCode: 0
Task: reproduce_all
Status: completed
步骤: 1
执行方式：dry-run plan generation
```

说明：

- 该命令验证 Agent 能读取 intent registry、生成复现计划、保存结构化日志。
- dry-run 不触发 500 题完整评测，专注于复现计划生成与日志结构校验。

能力注册校验：

```powershell
python benchmark/agent/_validate_capabilities.py
```

结果：

```text
JSON valid
Intents: 14
All deep checks passed
```

---

## 6. Track3 Medical RAG 最小闭环

### 6.1 离线检索 dry-run

命令：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.medical.kb_quality --dry-run
```

结果：

```text
chunks loaded: 3348
FAISS: 33480 KB
BM25: 17134 KB
本地 embedding: 成功
测试查询：primary endpoint
返回结果：3
```

Top-3 检索结果：

| rank | chunk_id | label |
|---:|---|---|
| 1 | `PMC3002358_chunk_012` | `primary_outcome` |
| 2 | `PMC12487728_chunk_007` | `_front_matter_other` |
| 3 | `PMC12574440_chunk_034` | `outcome_measures` |

### 6.2 FastAPI health

命令：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.api.medical_rag --check
```

结果：

```json
{
  "status": "ok",
  "components": {
    "faiss_index": {"available": true, "size_kb": 33480},
    "bm25_index": {"available": true, "size_kb": 17134},
    "chunks_manifest": {"available": true}
  },
  "issues": []
}
```

### 6.3 FastAPI search

临时启动服务：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.api.medical_rag --host 127.0.0.1 --port 17001
```

检索请求：

```powershell
curl http://127.0.0.1:17001/api/evidence/search?q=primary%20endpoint&k=3
```

结果：

```text
health_status=ok
issues=0
search_query=primary endpoint
count=3
vision=False
```

返回结果：

| rank | chunk_id | rrf_score | medical_label |
|---:|---|---:|---|
| 1 | `PMC3002358_chunk_012` | 0.02 | `primary_outcome` |
| 2 | `PMC12487728_chunk_007` | 0.02 | `_front_matter_other` |
| 3 | `PMC12574440_chunk_034` | 0.02 | `outcome_measures` |

---

## 7. 一键 Demo 全赛道验证

在 Medical RAG API 临时启动状态下运行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_reviewer_demo.ps1 -Track All -Quiet -ApiPort 17001
```

结果：

```text
全赛道检查通过
0 skipped
0 failed
```

覆盖：

- Track1 数据集与 leaderboard 资产
- Track2 Agent intent registry 与 dry-run
- Track3 FAISS/BM25/vision index 资产
- Medical RAG API health

---

## 8. 本轮没有运行的内容

| 未运行项 | 原因 | 替代证据 |
|---|---|---|
| 500 题完整评测 | 耗时与 API 成本较高，归入报告级复现 | `Limit 10` 真实评测 + `--limit 0 --resume` 可恢复命令 |
| QLoRA 完整训练 | GPU 长任务，归入完整离线复现 | 微调计划、脚本、PPL/训练产物证据见 Track3 报告 |
| Medical RAG 重建索引 | 已有索引资产存在，重建耗时 | `python -m controlsci.medical.kb_quality --dry-run` + FastAPI search |
| 云端 Demo 部署 | 另行计划，不属于本地最小闭环 | `cloud_demo` profile 隔离验证与 FastAPI 本地验证 |

---

## 9. FastAPI 云端 / 本地 Profile 分离

默认本地 profile：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.api.medical_rag --check
```

结果要点：

```text
profile=local_private
text_full_exposed=true
source_paths_exposed=true
```

云端 demo profile：

```powershell
$env:CONTROLSCI_API_PROFILE="cloud_demo"
conda run --no-capture-output -n myenv python -m controlsci.api.medical_rag --check
```

结果要点：

```text
profile=cloud_demo
status=degraded  # 当前未放置 data/demo_cloud/medical 脱敏演示数据时的预期状态
text_full_exposed=false
source_paths_exposed=false
data_root=medical
issues=data/demo_cloud/medical...
```

云端 search 验证：

```text
source_file=PMC3002358_chunk_012.md
text_full=""
text_preview="# Primary outcome measures"
```

说明：`cloud_demo` 只读取 `data/demo_cloud/medical` 下的脱敏演示资产；如果该目录不存在，服务返回 `degraded`，不会回退读取 `data/sources_medical` 的本地医疗原文。该 profile 隐藏完整 chunk、绝对路径和完整原文，不改变默认 `local_private` 的本地完整能力。

核心卫生检查：

```powershell
python -m controlsci.dev.verify_core_hygiene
```

验证项：

```text
[OK] capability validator
[OK] balanced-mini selection
[OK] report_viz empty input exit
[OK] cloud_demo isolation
[OK] legacy agent wrapper
Core hygiene: 5/5 passed
```

---

## 10. 结论

本轮最小真实闭环说明：

1. 数据集结构是可校验的。
2. Agent 能生成复现计划并通过能力注册校验。
3. 真实 API 小样本评测、Judge、resume、leaderboard 生成链路可运行。
4. Medical RAG 的本地 FAISS/BM25/Ollama embedding 检索链路可运行。
5. FastAPI health/search 可运行。
6. 一键 Demo 在 API 启动时可达到 `16/16 passed`。

因此，本项目采用以下分层复现入口：

```text
L1: controlscidemo all --quick
L2: run_minimal_repro.ps1 -Limit 10
L3: 按需执行完整 500 题 / QLoRA / 索引重建
```
