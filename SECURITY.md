# Security Policy

ControlMind is a research and competition release for scientific document processing, Agent workflows, and source-grounded RAG. It is not a clinical decision system or a production security product.

中文说明：ControlMind 是科学文档处理、Agent 工作流和来源支撑 RAG 的研究工程发布版本，不是临床决策系统，也不是安全产品。

## Supported Scope

Security reports are welcome for:

- Credential leakage in public files or logs.
- Unsafe handling of uploaded files in demos or APIs.
- Path traversal, unsafe archive extraction, or unintended file writes.
- Public/private data boundary mistakes.
- Reproducibility scripts that unexpectedly overwrite audited evidence.

## Out Of Scope

- Medical advice correctness as a standalone claim.
- Failures caused only by missing third-party API keys.
- Denial-of-service against public demos.
- Issues requiring private datasets or credentials not included in the repository.

## Reporting

Please open a GitHub issue with:

- A short description of the issue.
- Reproduction steps using public files whenever possible.
- The affected command, endpoint, or path.
- Whether credentials, local paths, or private data may be exposed.

Do not include live secrets, private medical records, or non-public documents in the issue body.

## Data Boundary

The repository should not contain patient-level private data, live API keys, local `.env` files, or machine-specific absolute paths in committed public artifacts. Large generated caches and indexes are rebuildable artifacts and should be distributed outside normal Git history when needed.
