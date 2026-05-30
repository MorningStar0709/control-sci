# ControlMind CLI Quickstart

ControlMind CLI is the product-facing command line entrypoint for the local workbench, three-track validation, Medical RAG, and DATA-TRACE artifacts.

The internal Python package remains `controlsci` for compatibility. The public command name is `controlmind`.

## Install

```powershell
conda run --no-capture-output -n myenv pip install -e .
```

Without installation:

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli --help
```

FastAPI-backed commands should run in `myenv`:

```powershell
conda run --no-capture-output -n myenv python -m controlsci.cli health --output _scratch/health.json
```

## Python CLI

ControlMind exposes a Python console script through `pyproject.toml`. The command below installs the local Python entrypoint and keeps the implementation inside `controlsci`.

```powershell
conda run --no-capture-output -n myenv pip install -e .
controlmind --help
controlmind doctor
controlmind run acceptance
```

Without installation, run the same commands through `conda run --no-capture-output -n myenv python -m controlsci.cli`.

## npm Launcher

ControlMind also provides a lightweight npm launcher for demos and reproducible handoff. It does not reimplement the Python core; it locates the project, selects a Python/Conda runtime, and forwards commands to `conda run --no-capture-output -n myenv python -m controlsci.cli`.

```powershell
npm install -g ./npm/controlmind
controlmind --help
controlmind wrapper-doctor
controlmind run acceptance
```

Runtime resolution order: `CONTROLMIND_PYTHON`, `conda run --no-capture-output -n myenv python`, then system `python3/python`. Set `CONTROLMIND_HOME` when running from outside the repository.

## Core Commands

```powershell
controlmind health
controlmind doctor
controlmind config show
controlmind demo status
controlmind demo start
controlmind demo restart
```

## Track Validation

```powershell
controlmind track1 validate --sample 4
controlmind track2 validate --artifact all
controlmind track3 index --check
controlmind track3 search "closed loop insulin hypoglycaemia" --k 2
controlmind track3 eval --case-set zh_ask
```

## Unified Acceptance

```powershell
controlmind run acceptance
controlmind run acceptance --output _scratch/acceptance.json
```

This command checks workbench health, Track1 validation, Track2 artifact validation, Track3 index health, and report completeness.

When saving machine-readable results on Windows, prefer `--output/-o` over shell redirection. The CLI writes UTF-8 JSON directly, so the file can be parsed consistently across PowerShell, conda, and CI.

## Trace Artifacts

```powershell
controlmind trace bundle
controlmind report status
```

## Boundary

- `controlmind` is the public product interface.
- `controlsci` is the legacy internal runtime package.
- Local-first remains the default policy.
- Cloud paths must be explicitly selected through runtime configuration.
- Long-running tasks are not triggered by default from validation commands; they validate saved artifacts and show the command required for full regeneration.
- `_scratch/` is the local temporary output area. It is ignored by git and can be rebuilt without changing audited evidence files.
- arXiv/PMC online download commands are corpus expansion utilities. Minimal validation uses packaged artifacts to avoid public-service rate limits or browser-cookie prerequisites.
