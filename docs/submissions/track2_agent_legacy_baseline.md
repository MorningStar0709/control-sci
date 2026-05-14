# ControlSci Agent Legacy Baseline

> 日期：2026-05-14
> 位置：`docs/submissions/`
> 用途：说明早期 `benchmark/agent/agent.py` 的工程价值如何被保留下来，并解释为什么正式评审入口统一迁移到 `agent_cli.py`。

---

## 1. 结论

`benchmark/agent/agent.py` 不是废弃成果，而是 ControlSci Agent 的早期工程基座。

它最初承担的是固定流水线 Agent 编排：

```text
benchmark build
  -> quality arbitrate
  -> split dataset
  -> model evaluate
  -> summarize
  -> report visualization
```

随着项目进入三赛道冲刺，系统需求从“固定流程可跑”升级为：

- 自然语言或 intent 驱动
- 14 intent 可组合调度
- API / Ollama / MinerU / Script 四路径资源选择
- 公开/脱敏任务上云，原文/医疗/微调/中间 chunk 留本地
- 失败恢复、verify、自修正、结构化日志
- 云端轻展示与本地私有执行双 profile

因此，正式入口迁移为：

```text
benchmark/agent/agent_cli.py
```

旧入口现在保留为 compatibility wrapper：

```text
benchmark/agent/agent.py
  -> forwards to benchmark/agent/agent_cli.py
```

这样既保留旧路径兼容性，也避免旧实现绕过新的隐私、日志和调度策略。

---

## 2. 架构演进

| 阶段 | 入口 | 核心形态 | 主要价值 | 局限 |
|---|---|---|---|---|
| v1 固定流水线 Agent | `agent.py` | 固定 pipeline 编排 | 证明 benchmark/eval/report 链路可自动串联 | provider、隐私边界和任务组合能力有限 |
| v2 Intent Agent | `agent_cli.py` | intent router + executor | 支持自然语言/intent 序列、dry-run、结构化日志 | 需要更明确的资源策略 |
| v3 隐私感知资源调度 Agent | `agent_cli.py` + `resource_scheduler.py` | intent + data_policy + provider routing | 将“公开/脱敏任务上云，原文/医疗/微调/中间 chunk 留本地”固化到代码 | 当前正式评审入口 |

---

## 3. 旧实现被继承的工程资产

早期 `agent.py` 的价值没有丢失，而是被迁移或升级到新架构中：

| legacy 经验 | 新位置 | 保留价值 |
|---|---|---|
| 固定 pipeline 调用链 | `reproduce_all` intent / `run_evaluation.ps1` | 保留从评测到 leaderboard 的可复现链路 |
| dry-run 思路 | `agent_cli.py --dry-run` | 评委可快速确认计划而不触发长任务 |
| step timeout | `Executor` / 各脚本 timeout | 防止长任务卡死 |
| 执行日志 | `log_schema.py` / `ExecutionLog` / `LogStep` | 所有执行步骤可审计 |
| pipeline summary | `print_summary()` / minimal repro 文档 | 让结果可快速确认 |
| subprocess 编排 | `Executor` dispatch map | 统一封装工具调用 |

---

## 4. 为什么不继续暴露旧实现

旧实现继续作为主入口会带来风险：

- 可能绕过 `resource_scheduler.py` 的 `data_policy`。
- 难以与 `agent_capabilities.json` 的 14 intent 保持一致。
- provider / API key / output 逻辑会出现重复维护。
- 评委运行旧入口时，行为可能和主报告叙事不一致。
- 难以支持 `cloud_demo` / `local_private` 双 profile。

因此，当前选择是：

```text
保留文件名和兼容路径
  但旧实现不再执行
  统一转发到 agent_cli.py
```

这不是浪费，而是风险收敛。

---

## 5. 当前兼容入口行为

命令：

```powershell
python benchmark/agent/agent.py --dry-run --intents reproduce_all
```

行为：

```text
[DEPRECATED] benchmark/agent/agent.py is a compatibility wrapper.
Forwarding to benchmark/agent/agent_cli.py.
```

随后由 `agent_cli.py` 生成正式执行摘要与日志。

---

## 6. 报告叙事用法

建议在 Track2 技术报告中将其表述为：

> `agent.py` 是 ControlSci Agent 的 legacy baseline。它证明了早期固定 pipeline 的可执行性，也沉淀了 dry-run、step timeout、subprocess 编排和 ExecutionLog 等工程经验。随着系统从固定流水线升级为隐私感知 Intent Agent，正式入口统一迁移到 `agent_cli.py`；旧入口保留为 wrapper，以保证历史命令兼容，同时避免绕过新的 data_policy 和 ResourceScheduler。

一句话版本：

> 旧 `agent.py` 的价值不是继续作为主系统运行，而是证明 ControlSci Agent 从固定流水线演进为隐私感知资源调度 Agent 的工程路径。
