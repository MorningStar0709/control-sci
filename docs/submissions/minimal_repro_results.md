# ControlSci 最小真实闭环复现结果

> 日期：2026-05-14
> 目录：`docs/submissions/`
> 用途：给评委快速确认“不是只看静态报告”，而是数据校验、Agent、真实小样本评测、Medical RAG 检索与 FastAPI 都已跑通。

---

## 1. 复现策略

本项目不建议评委现场运行完整 500 题评测、QLoRA 全量训练或 Medical RAG 全量重建索引。原因不是链路不可运行，而是这些任务成本高、耗时长，且不适合作为评审现场默认入口。

我们采用三层复现策略：

| 层级 | 目标 | 默认命令 | 适合场景 |
|---|---|---|---|
| L1 秒级证据 | 快速确认三赛道交付物存在且可读 | `python demo/cli/controlscidemo all --quick` | 3 分钟初筛 |
| L2 最小真实闭环 | 跑通数据校验、真实 API 小样本评测、leaderboard、Agent 校验、Medical RAG 检索/API | `.\run_minimal_repro.ps1 -Limit 10` | 10-20 分钟深度抽查 |
| L3 完整离线复现 | 500 题评测、QLoRA、索引重建 | `--limit 0 --resume` 或赛道报告附录命令 | 需要完整审计时 |

本文件记录的是 L2 最小真实闭环结果。

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

- `Limit 10 + balanced-mini` 用于证明真实 API/Judge/Resume/Leaderboard 链路可运行，并避免只抽到单一维度。
- balanced-mini 按 A/B/C/D round-robin 抽样；10 题覆盖 A=3、B=3、C=2、D=2。
- 完整 500 题评测支持 `--limit 0 --resume`，但不建议作为评审现场默认命令。

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
- dry-run 不触发 500 题完整评测，避免评审现场等待。

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
conda run --no-capture-output -n myenv python -m controlsci.api.medical_rag --host 127.0.0.1 --port 18001
```

请求：

```powershell
curl http://127.0.0.1:18001/api/evidence/search?q=primary%20endpoint&k=3
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
.\run_reviewer_demo.ps1 -Track All -Quiet -ApiPort 18001
```

结果：

```text
16/16 checks passed
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
| 500 题完整评测 | 评审现场耗时与 API 成本较高 | `Limit 10` 真实评测 + `--limit 0 --resume` 可恢复命令 |
| QLoRA 完整训练 | GPU 长任务，不适合最小验证 | 微调计划、脚本、PPL/训练产物证据见 Track3 报告 |
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

核心卫生脚本：

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

本轮最小真实闭环证明：

1. 数据集结构是可校验的。
2. Agent 能生成复现计划并通过能力注册校验。
3. 真实 API 小样本评测、Judge、resume、leaderboard 生成链路可运行。
4. Medical RAG 的本地 FAISS/BM25/Ollama embedding 检索链路可运行。
5. FastAPI health/search 可运行。
6. 一键 Demo 在 API 启动时可达到 `16/16 passed`。

因此，本项目的评审建议入口不是完整全量重跑，而是：

```text
L1: controlscidemo all --quick
L2: run_minimal_repro.ps1 -Limit 10
L3: 按需执行完整 500 题 / QLoRA / 索引重建
```
