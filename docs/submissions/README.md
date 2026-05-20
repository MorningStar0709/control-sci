# ControlMind 三赛道提交包

本目录是 2026 MinerU 生态挑战赛三赛道提交入口。三份主报告相互独立，可分别阅读；共享材料用于统一承载快速验证、样例抽查、数据溯源和本地复现。

## 第一入口

| 类型 | 入口 |
|:---|:---|
| 快速验证指南 | [quickstart.md](quickstart.md) |
| 云端 Demo | [https://demo.askiler.com/](https://demo.askiler.com/) |
| 前端访问码 | `ControlMind@2026` |
| GitHub | [MorningStar0709/ControlMind](https://github.com/MorningStar0709/ControlMind) |
| HuggingFace 数据集 | [MorningStar0709/control-sci-corpus](https://huggingface.co/datasets/MorningStar0709/control-sci-corpus) |

## 三份主报告

| 赛道 | 主报告 | 核心命题 | 快速证据 |
|:---|:---|:---|:---|
| Track1 Sci-Align | [track1_sci_align_report.md](track1_sci_align_report.md) | 控制科学结构化语料库与 Sci-Align 评测基准 | 500 题、AI-Ready schema、九模型排行榜、DATA-TRACE |
| Track2 Data Agent | [track2_agent_report.md](track2_agent_report.md) | 面向科学文档生产的 Agent 执行协议 | 14 Intent、资源调度器、LogStep、391 秒数据飞轮 replay |
| Track3 Medical RAG | [track3_medical_rag_report.md](track3_medical_rag_report.md) | 医疗文献来源支撑 RAG 与私有部署边界 | 证据不足拒答、中文 Ask、claim support、endpoint 边界 |

## 样例与溯源

| 材料 | 作用 |
|:---|:---|
| [shared/track1_sci_align_20_cases.md](shared/track1_sci_align_20_cases.md) | Track1 科学表达、跨模态 grounding 与题目样例抽查 |
| [shared/track2_agent_20_cases.md](shared/track2_agent_20_cases.md) | Track2 Agent 规划、执行、失败恢复和日志样例抽查 |
| [shared/track3_medical_rag_20_cases.md](shared/track3_medical_rag_20_cases.md) | Track3 医疗 RAG、拒答、中文 Ask 和来源支撑样例抽查 |
| [shared/DATA-TRACE.md](shared/DATA-TRACE.md) | 三赛道关键数字、图表、日志和原始文件来源索引 |
| [data_trace_bundle/manifest.json](data_trace_bundle/manifest.json) | 提交包内原始数据与证据文件清单，含 SHA-256 |
| [shared/minimal_repro_results.md](shared/minimal_repro_results.md) | 最小真实闭环复现记录 |
| [data_trace_bundle/12_final_supplemental_experiments/README.md](data_trace_bundle/12_final_supplemental_experiments/README.md) | 补充验收：三赛道最小入口、Track1 本地 JSON 加载、Track2 本地 DAG dry-run、Track3 拒答边界 |
| [shared/verifiable_source_matrix.md](shared/verifiable_source_matrix.md) | 三赛道来源与证据矩阵 |

## Demo 与部署

| 材料 | 作用 |
|:---|:---|
| [shared/cloud_demo_walkthrough.md](shared/cloud_demo_walkthrough.md) | 云端 Demo 页面、功能和边界导览 |
| [shared/public_cloud_boundary.md](shared/public_cloud_boundary.md) | 公开云端与本地私有资料的边界说明 |
| [shared/track2_agent_deploy.md](shared/track2_agent_deploy.md) | Track2 Agent 部署、依赖与运行边界 |
| [shared/track3_medical_deploy.md](shared/track3_medical_deploy.md) | Track3 医疗 RAG API、Docker 与本地索引部署 |

## 本地运行命令

在解压或克隆后的 ControlMind 项目根目录下运行：

```powershell
python demo/cli/controlscidemo all --quick
python demo/cli/controlscidemo track1 --quick
python demo/cli/controlscidemo track2 --quick
python demo/cli/controlscidemo track3 --quick
```

进一步复核三赛道：

```powershell
.\run_reviewer_demo.ps1 -Track All
```

Conda 环境可使用：

```powershell
conda run -n myenv python demo/cli/controlscidemo all --quick
```

推荐的最小验收命令如下。所有 JSON 产物写入 `_scratch/`，不会覆盖报告中已经固化的数据或证据文件：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli run acceptance --output _scratch/acceptance.json
conda run --no-capture-output -n myenv python -m controlsci.cli track2 validate --artifact flywheel --output _scratch/track2_flywheel.json
conda run --no-capture-output -n myenv python -m controlsci.cli track3 search "closed loop insulin hypoglycaemia primary endpoint" --k 3 --mode hybrid --index bge_m3 --output _scratch/track3_search.json
```

`_scratch/` 是本地临时运行目录，可删除、可重建，不属于权威数据源。最小验收默认使用提交包内已沉淀的公开 PDF、Markdown、题库、索引和 evidence；arXiv/PMC 在线下载保留为语料扩展能力，不作为提交包复现的前置条件。


