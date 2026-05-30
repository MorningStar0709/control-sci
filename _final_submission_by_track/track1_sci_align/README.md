# 赛道一提交包：Sci-Align

本目录是赛道一“语料筑基 / AGI4S 前沿语料”独立提交包，提供技术报告、数据集副本、30 个代表案例、图表资产与可审计证据索引；完整代码与可执行复现环境见 GitHub 仓库。

## 一屏入口

| 用途 | 文件 |
|:---|:---|
| 快速验证指南 | [quickstart.md](quickstart.md) |
| 主技术报告 | [track1_sci_align_report.md](track1_sci_align_report.md) |
| 30 个代表案例 | [track1_sci_align_20_cases.md](track1_sci_align_20_cases.md) |
| 数据集文件 | [core.json](dataset/core.json)、[full.json](dataset/full.json)、[schema.json](dataset/schema.json) |
| 数据溯源 | [shared/DATA-TRACE.md](shared/DATA-TRACE.md) |
| 证据包 | [data_trace_bundle/](data_trace_bundle/) |
| 图表资产 | [shared/assets/](shared/assets/) |
| 演示 PPT 与视频 | [bonus/](bonus/) |
| 可选 npm 启动壳 | [npm/controlmind/](npm/controlmind/) |

> 本地最终提交包的 `bonus/` 目录包含 PPT 与演示视频。若同步到 GitHub 仓库，视频可能因超过单文件 100 MB 限制而不随仓库上传，评审以本地最终提交包内容为准。

## 公开入口

| 项目 | 链接 |
|:---|:---|
| GitHub | [https://github.com/MorningStar0709/control-sci](https://github.com/MorningStar0709/control-sci) |
| HuggingFace 数据集 | [https://huggingface.co/datasets/MorningStar0709/control-sci-corpus](https://huggingface.co/datasets/MorningStar0709/control-sci-corpus) |
| 云端 Demo | [https://demo.askiler.com/](https://demo.askiler.com/) |
| Demo 访问码 | `ControlMind@2026` |

## 最小验证命令

克隆公开仓库后，在项目根目录运行：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli track1 validate --sample 4 --output _scratch/track1_validate.json
conda run --no-capture-output -n myenv python -m controlsci.cli report status --output _scratch/report_status.json
```

如需使用 Node.js 薄启动壳，可在完整公开仓库根目录或本目录位于公开仓库内时运行：

```powershell
npm install -g ./npm/controlmind
controlmind wrapper-doctor
controlmind track1 validate --sample 4
```

快速查看样例：

```powershell
conda run --no-capture-output -n myenv python demo/cli/controlscidemo track1 --quick
.\run\run_reviewer_demo.ps1 -Track 1
```

## 提交说明

赛道一选择 Sci-Align 数据范式，核心交付物是控制科学领域的 AI-ready 数据集：结构化 schema、source grounding、跨模态证据和九模型排行榜。所有关键定量声明可通过 [shared/DATA-TRACE.md](shared/DATA-TRACE.md) 与 [data_trace_bundle/](data_trace_bundle/) 回到源文件、命令或哈希记录。

本地运行产物建议写入 `_scratch/`。该目录是临时输出区，可删除、可重建，不属于权威数据源。
