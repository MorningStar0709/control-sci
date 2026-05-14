# Public Release Manifest

This branch is the clean public/reviewer release of ControlSci. It is intentionally smaller than the private research branch: the goal is to make the core code, submission reports, and traceable public evidence easy to inspect without exposing raw private corpora or heavy generated artifacts.

## Included

- `controlsci/`: production-ish Python package for shared paths, Medical RAG API, indexing, quality checks, and visualization helpers.
- `benchmark/agent/`: agent runtime, CLI, capability registry, log schema, and small dry-run examples.
- `benchmark/eval/`: evaluation, reporting, validation, and analysis code needed to understand or rerun the public workflows.
- `benchmark/dataset/`: public benchmark datasets and schemas used by the reviewer demo.
- `demo/cli/`: lightweight terminal demo entrypoint.
- `docs/submissions/`: final public reports, reviewer quickstart, shared diagrams, 20-case appendices, and the curated `data_trace_bundle`.
- Root scripts and environment files: `run_reviewer_demo.ps1`, `run_minimal_repro.ps1`, `run_agent.ps1`, `run_evaluation.ps1`, `run_medical_agent.ps1`, `reproduce.sh`, `Dockerfile`, `docker-compose.yml`, and `requirements.txt`.

## Excluded

- Raw corpora and parsed full-text sources under `data/`, `corpus/`, and related caches.
- Private medical indexes, embeddings, intermediate chunks, and local-only RAG assets.
- Model weights, LoRA/finetune outputs, checkpoint caches, and large generated matrices.
- Internal planning notes, scratch experiments, legacy `_tools/` and `_scratch/` workspaces, and slide/presentation work materials.
- Full benchmark result directories where the same public evidence has been copied into `docs/submissions/data_trace_bundle/`.

## Evidence Boundary

The public evidence boundary is `docs/submissions/data_trace_bundle/`. Files in that directory are curated copies of the scalar results, JSON summaries, representative images, medical RAG samples, and trace manifests cited by the reports. When a report references a heavier private source path such as `benchmark/eval/results/...`, the public reviewer should first look for the corresponding copied artifact in `docs/submissions/data_trace_bundle/manifest.json`.

## Privacy Principle

ControlSci keeps public or desensitized tasks cloud-runnable, while original text, medical data, finetuning data, embeddings, and intermediate chunks remain local/private. This is part of the project design, not an omission: the release is meant to prove the engineering surface and evidence chain without publishing sensitive or copyrighted working material.
