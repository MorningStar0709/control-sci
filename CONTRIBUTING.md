# Contributing

Thank you for helping improve ControlMind. This repository is prepared as a public research and competition release, so contributions should keep reproducibility, traceability, and data provenance intact.

中文说明：本仓库是面向公开复现与比赛审查的研究工程版本。任何贡献都应优先保持复现路径、数据溯源和公开边界清晰。

## What To Contribute

- Reproducibility fixes for CLI, scripts, demos, and documentation.
- Bug fixes in benchmark evaluation, Agent orchestration, and Medical RAG utilities.
- Clear documentation improvements that reduce setup or audit ambiguity.
- Small public sample data that improves verification without adding private or restricted material.

## Before Opening A Pull Request

Run the lightweight checks that match your change:

```powershell
conda run -n myenv python demo/cli/controlscidemo all --quick
conda run --no-capture-output -n myenv python -m controlsci.cli doctor --output _scratch/doctor.json
```

For Agent or RAG changes:

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli track2 validate --artifact all --output _scratch/track2_validate.json
conda run --no-capture-output -n myenv python -m controlsci.cli track3 eval --case-set zh_ask --output _scratch/track3_eval_zh_ask.json
```

## Data Rules

- Do not commit credentials, private documents, patient-level data, or local absolute paths.
- Put temporary outputs under `_scratch/`.
- Keep report numbers traceable to public files, scripts, commands, or manifest hashes.
- Use Git LFS, release assets, or dataset hosting for large binary artifacts instead of normal Git history.

## Pull Request Style

- Explain the user-facing or reproducibility impact.
- List the commands you ran.
- Mention any external API, GPU, or network dependency that affects repeatability.

## 中文简要规则

- 不提交密钥、私有文档、患者级数据和本机绝对路径。
- 临时产物写入 `_scratch/`。
- 报告中的新增数字必须能追溯到公开文件、脚本、命令或 manifest。
- 大体积二进制文件不要直接进入 Git 历史。
