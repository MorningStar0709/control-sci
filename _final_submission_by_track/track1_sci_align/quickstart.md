# 赛道一快速验证指南

本文件是赛道一独立提交包的快速入口。完整技术说明见 [track1_sci_align_report.md](track1_sci_align_report.md)，样例抽查见 [track1_sci_align_20_cases.md](track1_sci_align_20_cases.md)。

## 阅读顺序

1. 打开 [README.md](README.md) 了解本包结构。
2. 阅读 [主技术报告](track1_sci_align_report.md) 的摘要、数据构建与 AI-ready schema 部分。
3. 抽查 [30 个代表案例](track1_sci_align_20_cases.md)。
4. 需要复核数字时，查看 [DATA-TRACE](shared/DATA-TRACE.md) 与 [证据包](data_trace_bundle/)。

## 核心文件

| 用途 | 文件 |
|:---|:---|
| 主报告 | [track1_sci_align_report.md](track1_sci_align_report.md) |
| 案例包 | [track1_sci_align_20_cases.md](track1_sci_align_20_cases.md) |
| 核心数据集 | [dataset/core.json](dataset/core.json) |
| 全量数据集 | [dataset/full.json](dataset/full.json) |
| Schema | [dataset/schema.json](dataset/schema.json) |
| 数据集说明 | [dataset/README.md](dataset/README.md) |
| 数据溯源 | [shared/DATA-TRACE.md](shared/DATA-TRACE.md) |

## 最小验证命令

在公开仓库根目录运行：

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli track1 validate --sample 4 --output _scratch/track1_validate.json
conda run --no-capture-output -n myenv python demo/cli/controlscidemo track1 --quick
```

`_scratch/` 是本地临时输出目录，可删除、可重建，不属于权威数据源。
