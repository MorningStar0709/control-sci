# Data Licenses and Release Boundary

ControlMind combines original project code and reports with derived artifacts from
public third-party literature. The repository-level `LICENSE` applies to the
original ControlMind code, reports, schemas, scripts, and project-authored
materials unless a file or directory states otherwise.

Third-party source documents, parsed text, extracted chunks, images, metadata,
and evidence traces that originate from PMC, arXiv, or other external publishers
retain their original licenses, attribution requirements, and reuse restrictions.
Some source articles may use non-commercial or no-derivatives terms. This
repository does not relicense those third-party materials under the project
license.

## Included Public Data

- `corpus/chunks/`: derived scientific-document chunks used to reproduce the
  benchmark evidence.
- `data/sources_medical/`: public medical-literature working artifacts used by
  the local-first Medical RAG track.
- `data/sources_flywheel/`: public literature artifacts used by the agent
  flywheel demonstrations.
- `docs/submissions/data_trace_bundle/`: curated evidence summaries, scalar
  outputs, representative images, and trace manifests cited by the reports.

These artifacts are included for auditability and reproduction. Before reusing,
redistributing, or publishing a derivative dataset, inspect the original source
license for each document and preserve required attribution.

## Excluded or Untracked Data

The public Git history should not track rebuildable binary indexes, embedding
matrices, local checkpoint caches, credentials, `.env` files, private documents,
patient-level records, dependency folders, build outputs, or local scratch
workspaces. Rebuildable indexes and matrices are generated from the public
pipeline and should be distributed outside normal Git history when needed.

## Privacy Statement

The public release is built from public or sanitized materials. It is not a
patient dataset and should not contain patient-level private records, live API
keys, or local machine credentials. Medical RAG code is designed for local-first
deployment so institutions can substitute their own private corpora without
publishing those materials.
