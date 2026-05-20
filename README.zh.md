# ControlMind

ControlMind 是一个基于 MinerU 的科学文档智能项目，面向 2026 MinerU 数据智能与前沿语料挑战赛。项目将科学语料构建、自主化数据处理和来源支撑 RAG 三个独立赛道连接成一条可复核的工程链条。

[English version](README.md)

```text
赛道一：Sci-Align 数据集与评测基准
赛道二：Data Agent 执行协议
赛道三：医疗文献来源支撑 RAG
```

项目使用 MinerU 将科学 PDF 转化为结构化文本、公式、表格、图片、chunk、索引、评测题、Agent trace 和 RAG 来源卡片。

## 公开入口

| 项目 | 链接 |
|:---|:---|
| 云端 Demo | [https://demo.askiler.com/](https://demo.askiler.com/) |
| Demo 访问码 | `ControlMind@2026` |
| GitHub | [MorningStar0709/ControlMind](https://github.com/MorningStar0709/ControlMind) |
| HuggingFace 数据集 | [MorningStar0709/control-sci-corpus](https://huggingface.co/datasets/MorningStar0709/control-sci-corpus) |
| 提交包快速指南 | [docs/submissions/quickstart.md](docs/submissions/quickstart.md) |
| 提交包首页 | [docs/submissions/README.md](docs/submissions/README.md) |
| 数据溯源 | [docs/submissions/shared/DATA-TRACE.md](docs/submissions/shared/DATA-TRACE.md) |
| 复现说明 | [REPRODUCIBILITY.md](REPRODUCIBILITY.md) |

## 项目内容

| 赛道 | 主要产物 | 优先查看 |
|:---|:---|:---|
| 赛道一：Sci-Align | 500 题控制科学评测集与 AI-ready schema | [track1_sci_align_report.md](docs/submissions/track1_sci_align_report.md) |
| 赛道二：Data Agent | 14 Intent Agent 协议，含调度、日志、降级、回放与验收 | [track2_agent_report.md](docs/submissions/track2_agent_report.md) |
| 赛道三：Medical RAG | 医疗文献来源支撑 RAG，含中文 Ask、claim support、拒答边界与本地部署 | [track3_medical_rag_report.md](docs/submissions/track3_medical_rag_report.md) |

代表案例包：

- [赛道一 20 个案例](docs/submissions/shared/track1_sci_align_20_cases.md)
- [赛道二 20 个案例](docs/submissions/shared/track2_agent_20_cases.md)
- [赛道三 20 个案例](docs/submissions/shared/track3_medical_rag_20_cases.md)

## 关键结果

| 领域 | 结果 |
|:---|:---|
| 科学语料 | 362 篇控制科学文档、253,012 条 LaTeX 公式、28K 级 chunk |
| 赛道一评测集 | 500 道均衡题，A/B/C/D 各 125，九模型排行榜 |
| 跨模态溯源 | 500/500 题可追溯到源 chunk，并保留图片/公式统计 |
| 赛道二 Agent | 14 Intent、资源调度、LogStep、产物验收、391 秒数据飞轮 replay |
| 赛道三医疗 RAG | 97 篇 PMC 文献、3,348 个医学 chunk、FAISS/BM25/视觉索引 |
| 中文 Ask | 固化评测中 BGE-M3 中文 Ask trace 达到完整 claim support 与 citation coverage |
| 本地优先边界 | 医疗 chunk、索引、QLoRA 数据和 RAG 上下文默认留在本地 |

三份提交报告中的关键定量声明均可回到 [DATA-TRACE.md](docs/submissions/shared/DATA-TRACE.md) 中的源文件、命令或哈希记录。

## 快速开始

如果已有 `myenv` 环境，建议直接使用该环境运行：

```powershell
conda run -n myenv python demo/cli/controlscidemo all --quick
```

分赛道快速查看：

```powershell
conda run -n myenv python demo/cli/controlscidemo track1 --quick
conda run -n myenv python demo/cli/controlscidemo track2 --quick
conda run -n myenv python demo/cli/controlscidemo track3 --quick
```

运行面向审查的最小验证：

```powershell
.\run_reviewer_demo.ps1 -Track All -SkipApiHealth
```

运行 JSON 输出的检查命令。Windows 下如需保存文件，建议使用 `--output`，由 Python CLI 直接写入 UTF-8 JSON，避免 PowerShell 重定向带来的编码问题。

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli doctor --output _scratch/doctor.json
conda run --no-capture-output -n myenv python -m controlsci.cli track2 validate --artifact all --output _scratch/track2_validate.json
conda run --no-capture-output -n myenv python -m controlsci.cli track3 eval --case-set zh_ask --output _scratch/track3_eval_zh_ask.json
```

本地安装公开 CLI 入口：

```powershell
pip install -e .
controlmind doctor
controlmind track2 validate --artifact all
controlmind track3 eval --case-set zh_ask
```

可选 Node.js 启动壳：

```powershell
npm install -g ./npm/controlmind
controlmind wrapper-doctor
controlmind track2 validate --artifact all
```

npm 包只是薄启动壳：它定位仓库，选择 `CONTROLMIND_PYTHON`、`conda run -n myenv python` 或系统 Python，然后转发到 `python -m controlsci.cli`。

## 加载 Sci-Align 数据集

```python
from datasets import load_dataset

core = load_dataset("MorningStar0709/control-sci-corpus", "core", split="train")
print(len(core))
print(core[0]["question"])

full = load_dataset("json", data_files="benchmark/dataset/full.json", field="questions", split="train")
```

本地 JSON 文件：

```text
benchmark/dataset/core.json
benchmark/dataset/full.json
benchmark/dataset/schema.json
```

数据集文档：

- [benchmark/dataset/README.md](benchmark/dataset/README.md)
- [HuggingFace 数据集卡片](https://huggingface.co/datasets/MorningStar0709/control-sci-corpus)

## 本地 Demo 与部署

启动本地前后端工作台：

```powershell
.\run_frontend.ps1 -StartBackend
```

本地 API 启动后，可运行包含 RAG API 健康检查的一键验证：

```powershell
.\run_reviewer_demo.ps1 -Track All -ApiPort 17001
```

分赛道部署说明：

- [赛道二 Agent 部署说明](docs/submissions/shared/track2_agent_deploy.md)
- [赛道三医疗 RAG 部署说明](docs/submissions/shared/track3_medical_deploy.md)
- [云端 Demo 边界](docs/submissions/shared/public_cloud_boundary.md)

云端 Demo 仅用于公开或脱敏样例。私有文档、医疗 chunk、索引、模型 adapter 和 RAG 上下文默认通过本地/私有路径处理。

## 复现边界

推荐验收路径使用随包公开产物和本地索引。arXiv/PMC 在线下载仍作为语料扩展能力保留，但不作为最小验证前置条件，因为公共服务可能存在限流、浏览器校验或短时效 cookie。所有本地运行产物建议写入 `_scratch/`；该目录已被忽略，可删除、可重建，不影响已经审计的源数据。

完整分层复现策略见 [REPRODUCIBILITY.md](REPRODUCIBILITY.md)。简而言之：smoke check 与最小真实链路面向公开检出环境；报告结论通过 `docs/submissions/data_trace_bundle/` 审计；完整大规模重建可能需要 GPU、网络和外部模型/API 凭证。

## 仓库结构

```text
benchmark/                    赛道一评测与赛道二 Agent 产物
benchmark/dataset/            ControlSci core/full/schema 数据文件
benchmark/eval/               评测、排行榜与医疗 RAG 评测脚本
controlsci/                   Python 包与 controlmind CLI
npm/controlmind/              Python CLI 的可选 Node.js 启动壳
data/sources_medical/         赛道三医学语料、chunk、索引和视觉产物
docs/submissions/             公开提交报告、快速指南和证据包
starboard/                    本地与云端 Demo 前端
tools/                        MinerU 与工具脚本
```

## 许可与数据边界

- ControlSci 数据集采用 **CC-BY-4.0** 许可，详见 [LICENSE](LICENSE)。
- PMC、arXiv 等公开来源文档仍遵循其原始许可和署名要求。
- 本仓库和提交包不包含患者级私有数据。
- 云端 Demo 输入限定为公开或脱敏材料；私有 RAG 资产默认本地优先。

## 引用

```bibtex
@misc{controlmind2026,
  title        = {ControlMind: MinerU-based Scientific Document Intelligence for Sci-Align, Data Agent, and Medical RAG},
  author       = {MorningStar},
  year         = {2026},
  howpublished = {\url{https://github.com/MorningStar0709/ControlMind}},
  note         = {ControlSci dataset released under CC-BY-4.0}
}
```
