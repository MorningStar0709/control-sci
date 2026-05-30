# ControlMind npm launcher

This package is a thin Node.js launcher for the Python-based ControlMind CLI.

It does not reimplement the scientific pipeline. It locates the repository,
selects a Python runtime, and forwards commands to:

```bash
python -m controlsci.cli
```

## Local install

From the repository root:

```bash
npm install -g ./npm/controlmind
controlmind --help
controlmind wrapper-doctor
```

## Runtime selection

The launcher resolves Python in this order:

1. `CONTROLMIND_PYTHON`
2. `conda run --no-capture-output -n myenv python`
3. `python3` / `python` on `PATH`

Set `CONTROLMIND_HOME` when running from outside the repository.
