# 赛道二提交包：Data Agent

本目录是赛道二“智能进化 / Agent 能力评测”独立提交包。这里是最终提交副本，权威编辑源仍保留在项目根目录的 `docs/submissions/`。

## 一屏入口

| 用途 | 文件 |
|:---|:---|
| 快速验证指南 | [quickstart.md](quickstart.md) |
| 主技术报告 | [track2_agent_report.md](track2_agent_report.md) |
| 代表案例 | [track2_agent_20_cases.md](track2_agent_20_cases.md) |
| 部署与运行说明 | [track2_agent_deploy.md](track2_agent_deploy.md) |
| Agent 能力注册表 | [agent/agent_capabilities.json](agent/agent_capabilities.json) |
| 结构化日志样例 | [agent/examples/logs/](agent/examples/logs/) |
| 数据溯源 | [shared/DATA-TRACE.md](shared/DATA-TRACE.md) |
| 证据包 | [data_trace_bundle/](data_trace_bundle/) |
| 图表资产 | [assets/task2/](assets/task2/) |
| 演示 PPT 与视频 | [bonus/](bonus/) |
| 可选 npm 启动壳 | [npm/controlmind/](npm/controlmind/) |

> 演示视频（约 114 MB）因超过 GitHub 单文件 100 MB 限制，未上传至 GitHub 仓库。PPT 已在 bonus/ 中。

## 公开入口

| 项目 | 链接 |
|:---|:---|
| GitHub | https://github.com/MorningStar0709/control-sci |
| HuggingFace 数据集 | https://huggingface.co/datasets/MorningStar0709/control-sci-corpus |
| 云端 Demo | https://demo.askiler.com/ |
| Demo 访问码 | `ControlMind@2026` |

## 最小验证命令

克隆公开仓库后，在项目根目录运行：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli track2 validate --artifact all --output _scratch/track2_validate.json
conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py --dry-run --local --intents medical_rag,cross_modal_audit,leaderboard_viz --output-log _scratch/agent_local_dag.json
```

如需使用 Node.js 薄启动壳，可在完整公开仓库根目录或本目录位于公开仓库内时运行：

```powershell
npm install -g ./npm/controlmind
controlmind wrapper-doctor
controlmind track2 validate --artifact all
```

快速查看样例：

```powershell
conda run -n myenv python demo/cli/controlscidemo track2 --quick
.\run_reviewer_demo.ps1 -Track 2
```

## 提交说明

赛道二提交的是科学文档语料生产的 Agent 执行协议：Intent 路由、DAG 规划、资源调度、fallback、产物核验和结构化日志。提交包同时提供人类可读案例和机器可读证据；长耗时在线扩展任务默认不触发，验证命令复用随包产物与已保存日志。

本地运行产物建议写入 `_scratch/`。该目录是临时输出区，可删除、可重建，不属于权威数据源。
