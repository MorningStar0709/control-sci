# Reproducibility

ControlMind uses a layered reproducibility model. The default path is designed to be runnable on a fresh public checkout without private credentials or local absolute paths; full-scale rebuilds remain available when GPU, network, and external model/API access are present.

中文说明：本仓库采用分层复现策略。默认路径用于公开检出后的最小真实验证；完整大规模重建需要额外的 GPU、网络和外部模型/API 条件。

## Level 1: Smoke Check

Purpose: verify that the public code, packaged evidence, CLI, and local artifact readers are usable.

```powershell
conda run -n myenv python demo/cli/controlscidemo all --quick
.\run_reviewer_demo.ps1 -Track All -SkipApiHealth
```

Recommended JSON checks:

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli doctor --output _scratch/doctor.json
conda run --no-capture-output -n myenv python -m controlsci.cli track2 validate --artifact all --output _scratch/track2_validate.json
conda run --no-capture-output -n myenv python -m controlsci.cli track3 eval --case-set zh_ask --output _scratch/track3_eval_zh_ask.json
```

Expected boundary: commands should read public artifacts and write only to `_scratch/` or explicitly supplied result folders.

If the local Medical RAG API is already running, the API-backed check can be run with:

```powershell
.\run_reviewer_demo.ps1 -Track All -ApiPort 17001
```

Optional Node.js launcher:

```powershell
npm install -g ./npm/controlmind
controlmind wrapper-doctor
controlmind run acceptance
```

This launcher does not reimplement the pipeline. It forwards commands to `python -m controlsci.cli`.

## Level 2: Minimal Real Chain

Purpose: run a compact but real evaluation chain across the three tracks.

```powershell
.\run_minimal_repro.ps1 -Limit 10 -SkipApiSearch
```

This path covers:

- Track 1 balanced mini evaluation and leaderboard generation.
- Track 2 Agent dry-run, capability validation, and artifact checks.
- Track 3 offline Medical RAG retrieval quality check.

To include the local Medical RAG API health/search path:

```powershell
.\run_minimal_repro.ps1 -Limit 10
```

## Level 3: Evidence Audit

Purpose: inspect the data used by the public reports without rerunning expensive jobs.

Primary files:

- `docs/submissions/quickstart.md`
- `docs/submissions/shared/DATA-TRACE.md`
- `docs/submissions/data_trace_bundle/manifest.json`
- `docs/submissions/data_trace_bundle/README.md`
- `benchmark/dataset/core.json`
- `benchmark/dataset/full.json`

The public reports cite curated evidence under `docs/submissions/data_trace_bundle/`. Large derived indexes and embedding caches are intentionally treated as rebuildable artifacts and may be distributed through release packages or dataset hosting rather than normal Git history.

## Level 4: Full Rebuild

Purpose: regenerate large corpora, indexes, multi-model evaluation outputs, and GPU throughput records.

This level may require:

- Stable access to public paper sources such as arXiv or PMC.
- API keys for external model providers when running remote judge/model evaluations.
- Local GPU/runtime setup for Ollama, HuggingFace embeddings, or vision model paths.
- Additional time for full PDF parsing, indexing, and batch evaluation.

The full rebuild path is documented through the root scripts and per-track submission notes. Public services can rate-limit downloads, so packaged evidence remains the authoritative audit trail for the submitted results.

## Output Hygiene

Use `_scratch/` for local experiments:

```powershell
New-Item -ItemType Directory -Force _scratch
```

Do not commit:

- `.env` or credential files.
- Dependency caches such as `node_modules/`, `.next/`, and `__pycache__/`.
- Large generated matrices, FAISS indexes, or embedding caches.
- Local machine paths from runtime logs.

## Short Chinese Guide

推荐复现顺序：

1. 先运行 `controlscidemo all --quick` 与 `run_reviewer_demo.ps1 -Track All -SkipApiHealth`，确认公开入口可用。
2. 再运行 `run_minimal_repro.ps1 -Limit 10 -SkipApiSearch`，验证三赛道最小真实链路。
3. 对照 `DATA-TRACE.md` 与 `data_trace_bundle/manifest.json` 复核报告中的关键数据。
4. 只有在具备 GPU、网络和外部 API 条件时，再执行完整重建。

公开承诺边界：核心结论可复核，最小链路可复现，完整大规模实验可重建但受外部环境影响。
