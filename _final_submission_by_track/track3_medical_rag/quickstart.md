# 赛道三快速验证指南

本文件是赛道三独立提交包的快速入口。完整技术说明见 [track3_medical_rag_report.md](track3_medical_rag_report.md)，样例抽查见 [track3_medical_rag_20_cases.md](track3_medical_rag_20_cases.md)。

## 阅读顺序

1. 打开 [README.md](README.md) 了解本包结构。
2. 阅读 [主技术报告](track3_medical_rag_report.md) 的业务价值、证据 RAG 和本地部署边界部分。
3. 抽查 [26 个代表案例](track3_medical_rag_20_cases.md)。
4. 查看 [部署与 API 说明](track3_medical_deploy.md)、[云端 Demo 导览](shared/cloud_demo_walkthrough.md) 和 [公开云端 / 本地私有边界](shared/public_cloud_boundary.md)。
5. 需要复核数字时，查看 [DATA-TRACE](shared/DATA-TRACE.md) 与 [证据包](data_trace_bundle/)。

## 核心文件

| 用途 | 文件 |
|:---|:---|
| 主报告 | [track3_medical_rag_report.md](track3_medical_rag_report.md) |
| 26 个案例包 | [track3_medical_rag_20_cases.md](track3_medical_rag_20_cases.md) |
| 部署说明 | [track3_medical_deploy.md](track3_medical_deploy.md) |
| 云端 Demo 导览 | [shared/cloud_demo_walkthrough.md](shared/cloud_demo_walkthrough.md) |
| 私有部署边界 | [shared/public_cloud_boundary.md](shared/public_cloud_boundary.md) |
| 数据溯源 | [shared/DATA-TRACE.md](shared/DATA-TRACE.md) |

## 最小验证命令

如果只拿到本目录这个独立提交包，推荐先运行 evidence-only 检查。该模式只验证已提交证据包，不启动本地 RAG 服务，也不要求 `benchmark/`、`controlsci/` 或 `starboard/` 源码目录存在：

```powershell
.\run\run_task3_rag_flywheel.ps1 -EvidenceOnly
.\run\verify_task3_demo.ps1 -EvidenceOnly
```

在公开仓库根目录运行：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli track3 search "closed loop insulin hypoglycaemia primary endpoint" --k 3 --mode hybrid --index bge_m3 --output _scratch/track3_search.json
conda run --no-capture-output -n myenv python -m controlsci.cli track3 eval --case-set zh_ask --output _scratch/track3_eval_zh_ask.json
```

`_scratch/` 是本地临时输出目录，可删除、可重建，不属于权威数据源。PMC 在线下载保留为语料扩展能力，不作为复现前置条件。
