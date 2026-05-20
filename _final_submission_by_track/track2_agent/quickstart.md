# 赛道二快速验证指南

本文件是赛道二独立提交包的快速入口。完整技术说明见 [track2_agent_report.md](track2_agent_report.md)，样例抽查见 [track2_agent_20_cases.md](track2_agent_20_cases.md)。

## 阅读顺序

1. 打开 [README.md](README.md) 了解本包结构。
2. 阅读 [主技术报告](track2_agent_report.md) 的 Agent 定位、执行协议与工程可靠性部分。
3. 抽查 [20 个代表案例](track2_agent_20_cases.md)。
4. 查看 [部署与运行说明](track2_agent_deploy.md)。
5. 需要复核数字时，查看 [DATA-TRACE](shared/DATA-TRACE.md) 与 [证据包](data_trace_bundle/)。

## 核心文件

| 用途 | 文件 |
|:---|:---|
| 主报告 | [track2_agent_report.md](track2_agent_report.md) |
| 案例包 | [track2_agent_20_cases.md](track2_agent_20_cases.md) |
| 部署说明 | [track2_agent_deploy.md](track2_agent_deploy.md) |
| Agent 能力注册表 | [agent/agent_capabilities.json](agent/agent_capabilities.json) |
| 结构化日志样例 | [agent/examples/logs/](agent/examples/logs/) |
| 数据溯源 | [shared/DATA-TRACE.md](shared/DATA-TRACE.md) |

## 最小验证命令

在公开仓库根目录运行：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli track2 validate --artifact all --output _scratch/track2_validate.json
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py --dry-run --local --intents medical_rag,cross_modal_audit,leaderboard_viz --output-log _scratch/agent_local_dag.json
```

`_scratch/` 是本地临时输出目录，可删除、可重建，不属于权威数据源。
