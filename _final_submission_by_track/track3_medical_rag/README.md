# 赛道三提交包：Medical RAG

本目录是赛道三“行业应用转化 / 医疗文献 RAG”独立提交包。这里是最终提交副本，权威编辑源仍保留在项目根目录的 `docs/submissions/`。

## 一屏入口

| 用途 | 文件 |
|:---|:---|
| 快速验证指南 | [quickstart.md](quickstart.md) |
| 主技术报告 | [track3_medical_rag_report.md](track3_medical_rag_report.md) |
| 代表案例 | [track3_medical_rag_20_cases.md](track3_medical_rag_20_cases.md) |
| 部署与 API 说明 | [track3_medical_deploy.md](track3_medical_deploy.md) |
| 云端 Demo 导览 | [shared/cloud_demo_walkthrough.md](shared/cloud_demo_walkthrough.md) |
| 公开云端 / 本地私有边界 | [shared/public_cloud_boundary.md](shared/public_cloud_boundary.md) |
| 数据溯源 | [shared/DATA-TRACE.md](shared/DATA-TRACE.md) |
| 证据包 | [data_trace_bundle/](data_trace_bundle/) |
| 图表资产 | [assets/task3/](assets/task3/) |
| Docker 与运行脚本 | [run/](run/) |
| 演示 PPT | [bonus/](bonus/) |
| 可选 npm 启动壳 | [npm/controlmind/](npm/controlmind/) |

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
conda run --no-capture-output -n myenv python -m controlsci.cli track3 search "closed loop insulin hypoglycaemia primary endpoint" --k 3 --mode hybrid --index bge_m3 --output _scratch/track3_search.json
conda run --no-capture-output -n myenv python -m controlsci.cli track3 eval --case-set zh_ask --output _scratch/track3_eval_zh_ask.json
```

如需使用 Node.js 薄启动壳，可在完整公开仓库根目录或本目录位于公开仓库内时运行：

```powershell
npm install -g ./npm/controlmind
controlmind wrapper-doctor
controlmind track3 eval --case-set zh_ask
```

快速查看样例：

```powershell
conda run -n myenv python demo/cli/controlscidemo track3 --quick
.\run_reviewer_demo.ps1 -Track 3
```

## 提交说明

赛道三提交的是一套本地优先的医疗文献证据 RAG：MinerU 解析、医学章节切片、Hybrid 检索、中文 Ask、claim support、拒答边界、视觉证据增强和可部署 API/Demo。最小验证路径使用提交包内已沉淀的公开产物和本地索引；PMC 在线下载保留为语料扩展能力，不作为复现前置条件。

本地运行产物建议写入 `_scratch/`。该目录是临时输出区，可删除、可重建，不属于权威数据源。
