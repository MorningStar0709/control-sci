# Public Release Manifest

This branch is the public/reviewer release of ControlSci. It is intentionally broad: the goal is to keep the public code, reports, evidence bundle, reproducibility scripts, open medical corpus derivatives, indexes, and benchmark outputs close to the local project state, while still excluding credentials, dependency caches, generated runtime folders, and private model/checkpoint material.

## Included

- `controlsci/`: production-ish Python package for shared paths, Medical RAG API, indexing, quality checks, and visualization helpers.
- `benchmark/agent/`: agent runtime, CLI, capability registry, log schema, and small dry-run examples.
- `benchmark/agent/logs/` and `benchmark/agent/results/`: public execution records and task outputs used to support the Agent track.
- `benchmark/eval/`: evaluation, reporting, validation, and analysis code needed to understand or rerun the public workflows.
- `benchmark/eval/results/`: public benchmark outputs, medical RAG results, traces, figures, and result summaries used by the reports.
- `benchmark/dataset/`: public benchmark datasets and schemas used by the reviewer demo.
- `data/sources_medical/`: public/open medical RAG working set, including parsed Markdown, chunks, indexes, QA artifacts, MedBench probe outputs, and source metadata.
- `demo/cli/`: lightweight terminal demo entrypoint.
- `docs/submissions/`: final public reports, reviewer quickstart, shared diagrams, 20-case appendices, and the curated `data_trace_bundle`.
- `tools/`, `scripts/`, `pipeline/`, and `notebooks/`: reproducibility utilities and analysis helpers.
- `npm/controlmind/`: optional Node.js launcher that locates the repository and forwards commands to the Python CLI.
- `starboard/`: frontend source for the local workbench, excluding dependency/build folders.
- `cloud_demo_standalone/`: isolated cloud-demo source package, excluding runtime uploads, logs, dependency folders, and build folders.
- Root scripts and environment files: `run_reviewer_demo.ps1`, `run_minimal_repro.ps1`, `run_agent.ps1`, `run_evaluation.ps1`, `run_medical_agent.ps1`, `run_task3_rag_flywheel.ps1`, `run_frontend.ps1`, `verify_task3_demo.ps1`, `reproduce.sh`, `Dockerfile`, `docker-compose.yml`, `pyproject.toml`, and `requirements.txt`.
- Public repository guidance: `README.md`, `README.zh.md`, `REPRODUCIBILITY.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `LICENSE`, and `CITATION.cff`.

## Excluded

- Dependency and build caches such as `node_modules/`, `.next/`, `.next-build/`, `__pycache__/`, `.pytest_cache/`, and generated upload folders.
- Local runtime logs that are not part of benchmark evidence.
- Credentials, `.env` files with live values, personal machine paths, and user-specific interpreter paths.
- Model weights, LoRA/finetune outputs, checkpoint caches, and non-public large generated matrices.
- Per-track final submission packages, slide-production folders, build outputs, internal planning notes, scratch experiments, legacy `_tools/` and `_scratch/` workspaces, and non-public presentation work materials.

## Evidence Boundary

The primary citation boundary remains `docs/submissions/data_trace_bundle/`. Files in that directory are curated copies of the scalar results, JSON summaries, representative images, medical RAG samples, and trace manifests cited by the reports. The broader release also includes the underlying public working artifacts in `benchmark/eval/results/`, `benchmark/agent/logs/`, and `data/sources_medical/` so that reproduction can stay close to the local project.

## Privacy Principle

ControlSci keeps public or desensitized workflows cloud-runnable and publishes the open evidence needed to inspect the three tracks. What remains outside the release is limited to credentials, local caches, dependency installs, private scratch work, and model/checkpoint assets that are either too heavy or not required for public reproduction.
