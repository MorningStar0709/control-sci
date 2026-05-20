# ControlMind

ControlMind is a MinerU-based scientific document intelligence project for the 2026 MinerU Data Intelligence Challenge. It connects three independent tracks into one auditable chain: scientific corpus construction, autonomous data processing, and source-grounded RAG.

[Chinese version](README.zh.md)

```text
Track 1: Sci-Align dataset and benchmark
Track 2: Data Agent execution protocol
Track 3: Medical literature RAG
```

The project uses MinerU to turn scientific PDFs into structured text, formulas, tables, figures, chunks, indexes, benchmark questions, Agent traces, and RAG evidence cards.

## Public Entry Points

| Item | Link |
|:---|:---|
| Cloud demo | [https://demo.askiler.com/](https://demo.askiler.com/) |
| Demo access code | `ControlMind@2026` |
| GitHub | [MorningStar0709/ControlMind](https://github.com/MorningStar0709/ControlMind) |
| HuggingFace dataset | [MorningStar0709/control-sci-corpus](https://huggingface.co/datasets/MorningStar0709/control-sci-corpus) |
| Submission quickstart | [docs/submissions/quickstart.md](docs/submissions/quickstart.md) |
| Submission README | [docs/submissions/README.md](docs/submissions/README.md) |
| Data trace | [docs/submissions/shared/DATA-TRACE.md](docs/submissions/shared/DATA-TRACE.md) |
| Reproducibility | [REPRODUCIBILITY.md](REPRODUCIBILITY.md) |

## What Is Included

| Track | Main artifact | Start here |
|:---|:---|:---|
| Track 1: Sci-Align | 500-question control-science benchmark with AI-ready schema | [track1_sci_align_report.md](docs/submissions/track1_sci_align_report.md) |
| Track 2: Data Agent | 14-intent Agent protocol with scheduling, logs, fallback, replay, and validation | [track2_agent_report.md](docs/submissions/track2_agent_report.md) |
| Track 3: Medical RAG | Source-grounded medical literature RAG with Chinese Ask, claim support, refusal boundary, and local deployment | [track3_medical_rag_report.md](docs/submissions/track3_medical_rag_report.md) |

Representative sample packs:

- [Track 1 20 cases](docs/submissions/shared/track1_sci_align_20_cases.md)
- [Track 2 20 cases](docs/submissions/shared/track2_agent_20_cases.md)
- [Track 3 20 cases](docs/submissions/shared/track3_medical_rag_20_cases.md)

## Key Results

| Area | Result |
|:---|:---|
| Scientific corpus | 362 control-science documents, 253,012 LaTeX formulas, 28K-level chunks |
| Track 1 benchmark | 500 balanced questions, A/B/C/D = 125 each, 9-model leaderboard |
| Cross-modal traceability | 500/500 questions linked to source chunks; image/formula statistics preserved |
| Track 2 Agent | 14 intents, ResourceScheduler, LogStep schema, artifact validation, 391-second flywheel replay |
| Track 3 Medical RAG | 97 parsed PMC papers, 3,348 medical chunks, FAISS/BM25/vision indexes |
| Chinese Ask | BGE-M3 fixed trace with full claim support and citation coverage in saved evaluation |
| Local-first boundary | Medical chunks, indexes, QLoRA data, and RAG context stay local by default |

All quantitative claims in the submission reports point back to files, commands, or hashes in [DATA-TRACE.md](docs/submissions/shared/DATA-TRACE.md).

## Quick Start

Use an existing `myenv` environment when available.

```powershell
conda run -n myenv python demo/cli/controlscidemo all --quick
```

Run per-track quick views:

```powershell
conda run -n myenv python demo/cli/controlscidemo track1 --quick
conda run -n myenv python demo/cli/controlscidemo track2 --quick
conda run -n myenv python demo/cli/controlscidemo track3 --quick
```

Run reviewer-oriented minimal verification:

```powershell
.\run_reviewer_demo.ps1 -Track All -SkipApiHealth
```

Run JSON-oriented checks. Use `--output` when saving files on Windows; it lets the Python CLI write UTF-8 JSON directly and avoids shell redirection encoding issues.

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli doctor --output _scratch/doctor.json
conda run --no-capture-output -n myenv python -m controlsci.cli track2 validate --artifact all --output _scratch/track2_validate.json
conda run --no-capture-output -n myenv python -m controlsci.cli track3 eval --case-set zh_ask --output _scratch/track3_eval_zh_ask.json
```

Install the public CLI wrapper locally:

```powershell
pip install -e .
controlmind doctor
controlmind track2 validate --artifact all
controlmind track3 eval --case-set zh_ask
```

Optional Node.js launcher:

```powershell
npm install -g ./npm/controlmind
controlmind wrapper-doctor
controlmind track2 validate --artifact all
```

The npm package is only a thin launcher. It locates the repository, selects `CONTROLMIND_PYTHON`, `conda run -n myenv python`, or system Python, and forwards commands to `python -m controlsci.cli`.

## Load The Sci-Align Dataset

```python
from datasets import load_dataset

core = load_dataset("MorningStar0709/control-sci-corpus", "core", split="train")
print(len(core))
print(core[0]["question"])

full = load_dataset("json", data_files="benchmark/dataset/full.json", field="questions", split="train")
```

Local JSON files:

```text
benchmark/dataset/core.json
benchmark/dataset/full.json
benchmark/dataset/schema.json
```

Dataset documentation:

- [benchmark/dataset/README.md](benchmark/dataset/README.md)
- [HuggingFace dataset card](https://huggingface.co/datasets/MorningStar0709/control-sci-corpus)

## Local Demo And Deployment

Start the local frontend/backend workbench:

```powershell
.\run_frontend.ps1 -StartBackend
```

Run the RAG API-backed reviewer check after the local API is available:

```powershell
.\run_reviewer_demo.ps1 -Track All -ApiPort 17001
```

Track-specific deployment notes:

- [Track 2 Agent deploy notes](docs/submissions/shared/track2_agent_deploy.md)
- [Track 3 Medical RAG deploy notes](docs/submissions/shared/track3_medical_deploy.md)
- [Cloud demo boundary](docs/submissions/shared/public_cloud_boundary.md)

The public cloud demo is for public or sanitized examples. Private documents, medical chunks, indexes, model adapters, and RAG contexts are handled through local/private paths.

## Reproducibility Boundary

The recommended verification path uses packaged public artifacts and local indexes. arXiv/PMC online downloading remains available as a corpus expansion capability, but it is intentionally not a prerequisite for minimal validation because public services may apply rate limits, browser checks, or short-lived cookies. Local run outputs should go under `_scratch/`; that directory is ignored and can be deleted or regenerated without affecting the audited source data.

For the full layered policy, see [REPRODUCIBILITY.md](REPRODUCIBILITY.md). In short: smoke checks and minimal real-chain validation are designed for a public checkout; report-level conclusions are auditable through `docs/submissions/data_trace_bundle/`; full-scale rebuilds may require GPU, network access, and external model/API credentials.

## Repository Map

```text
benchmark/                    Track 1 benchmark and Track 2 Agent artifacts
benchmark/dataset/            ControlSci core/full/schema JSON files
benchmark/eval/               evaluation, leaderboard, medical RAG eval scripts
controlsci/                   Python package and controlmind CLI
npm/controlmind/              optional Node.js launcher for the Python CLI
data/sources_medical/         Track 3 medical corpus, chunks, indexes, vision artifacts
docs/submissions/             public submission reports, quickstart, evidence bundle
starboard/                    local/cloud demo frontend
tools/                        MinerU and utility scripts
```

## License And Data Boundary

- The ControlSci dataset is released under **CC-BY-4.0**. See [LICENSE](LICENSE).
- Public PMC/arXiv/source documents retain their original licenses and attribution requirements.
- Patient-level private data is not included in this repository or submission package.
- Cloud demo inputs are limited to public or sanitized materials; private RAG assets are local-first.

## Citation

```bibtex
@misc{controlmind2026,
  title        = {ControlMind: MinerU-based Scientific Document Intelligence for Sci-Align, Data Agent, and Medical RAG},
  author       = {MorningStar},
  year         = {2026},
  howpublished = {\url{https://github.com/MorningStar0709/ControlMind}},
  note         = {ControlSci dataset released under CC-BY-4.0}
}
```
