# Track 2 Agent Reliability Evidence

本目录保存赛道二补充实验的可复核证据包。实验目标不是新增功能，而是用批量、结构化结果回答五个工程问题：Agent 是否能稳定规划、是否能处理故障、是否能在多源任务中做出比固定规则更可靠的选择、是否能暴露资源调度边界、是否具备复杂文档挑战覆盖证据。

## Evidence Files

| 文件 | 来源 | 内容 |
|---|---|---|
| `agent_router_robustness.json` | `benchmark/eval/results/agent_router_robustness.json` | 25 条自然语言任务变体的 Router baseline 结果 |
| `agent_router_robustness.freeze.json` | `benchmark/eval/results/agent_router_robustness.freeze.json` | Task 1 baseline 冻结清单与 SHA-256 |
| `agent_failure_injection_matrix.json` | `benchmark/eval/results/agent_failure_injection_matrix.json` | 6 类故障 × 3 次的恢复矩阵 |
| `agent_source_selection_ablation.json` | `benchmark/eval/results/agent_source_selection_ablation.json` | 20 条查询的 Fixed Rule / Agent Router / Oracle A/B 对比 |
| `agent_resource_pareto.json` | `benchmark/eval/results/agent_resource_pareto.json` | 4 类任务 × auto / local / replay 的资源调度 Pareto 探针 |
| `agent_hard_document_stress.json` | `benchmark/eval/results/agent_hard_document_stress.json` | 6 类复杂文档挑战的仓库内样本覆盖压力测试 |

## Key Findings

| 工程问题 | 关键结果 | 权威源 |
|---|---:|---|
| 自然语言任务能否进入可执行链路 | 25/25 success, dry_run_success_rate=1.0 | `agent_router_robustness.json` summary |
| 常见故障是否能留下结构化恢复证据 | 18/18 recovered, recovery_success_rate=1.0 | `agent_failure_injection_matrix.json` summary |
| Agent 选择是否优于固定规则 | Agent accuracy=0.85, fixed rule=0.75 | `agent_source_selection_ablation.json` summary |
| 隐私边界是否被外部检索误触发 | Agent privacy violation=0, fixed rule=1 | `agent_source_selection_ablation.json` summary |
| 资源调度是否暴露真实可用性边界 | 12 records, 10 success, 2 unavailable, error_records=0 | `agent_resource_pareto.json` summary |
| 复杂文档挑战是否有可复核覆盖 | 15 samples, 6 challenge types, coverage_rate=1.0 | `agent_hard_document_stress.json` summary |

## Boundary Notes

- `agent_router_robustness.json` 是 baseline，不包含 few-shot 或 prompt 改进，后续优化必须与冻结清单对照。
- `agent_failure_injection_matrix.json` 使用 mock、临时环境变量和本地 timeout，不停止真实服务，不修改真实 API key。
- `agent_source_selection_ablation.json` 只评估 source / intent selection，不依赖 Sciverse 实时检索，因此不包含平均 hits。
- `agent_resource_pareto.json` 只记录 health probe、call count、latency、本地 / 远端分类和 replay 基线；没有可交叉审计账单或 token 来源时不写成本金额。
- `agent_hard_document_stress.json` 使用仓库内文件和既有审计产物；`standard_spec` 是结构规范覆盖，不等价于行业标准 PDF。
- 对外报告建议采用“工程问题 → 实验 → 证据 → 边界”的叙事，不直接复刻比赛评分细则。

## Reproduction Commands

```powershell
$env:PYTHONIOENCODING='utf-8'
$env:CONDA_NO_PLUGINS='true'
conda run --no-capture-output -n myenv python -m benchmark.agent.router_robustness_eval --output benchmark/eval/results/agent_router_robustness.json
conda run --no-capture-output -n myenv python -m benchmark.agent.failure_injection_eval --output benchmark/eval/results/agent_failure_injection_matrix.json
conda run --no-capture-output -n myenv python -m benchmark.agent.source_selection_ablation --output benchmark/eval/results/agent_source_selection_ablation.json
conda run --no-capture-output -n myenv python -m benchmark.agent.resource_pareto_eval --output benchmark/eval/results/agent_resource_pareto.json
conda run --no-capture-output -n myenv python -m benchmark.agent.hard_document_stress_eval --output benchmark/eval/results/agent_hard_document_stress.json
```
