---
name: "mineru-to-md"
description: "Convert supported local documents to Markdown through the local MinerU API in Trae, including PDF, images, DOCX, PPTX, and XLSX, and save the output to a chosen Windows-accessible directory. Use when the user asks to 转 Markdown, 提取 PDF, 解析文档, 图片转 md, 保存为 markdown, batch-convert supported files, check or audit MinerU output quality, 检查转换质量, 统计公式图片数, or 检测扫描版 PDF. Do not use for web pages, plain text rewriting, or summarization tasks without file conversion."
---

# MinerU To Markdown

Use this skill when the user wants to convert local documents into Markdown files
and save the `.md` output to a chosen directory.

This skill is for agent execution, not end-user documentation.

When the user writes in Chinese, ask required follow-up questions and report saved Markdown paths, skipped files, cleanup warnings, and failures in Simplified Chinese. Keep file paths, API URLs, task IDs, command flags, and JSON keys in their original form.

## Runtime assumptions

- MinerU runs inside WSL + Docker.
- The agent runs on the Windows host.
- Windows can reach MinerU at `http://127.0.0.1:8000`.
- Network mode is `mirror`.
- Health check endpoint is `/health` (not `/`).
- GPU power state matters: on battery, GPU utilization drops from ~90% to 5-25%. For documents >100 pages, advise the user to plug in AC power.
- After Docker restart, expect ~60s vLLM cold-start (CPU 100%, GPU idle) before the first document begins. Add `+2min` to time estimates after a restart.
- GPU VRAM fragments over consecutive tasks. After ~6-7 documents, VRAM approaches 22-23GB/24GB and speed degrades 2-4x. Drain the batch first, then suggest `docker restart mineru-api` (42s to healthy, saved files unaffected).

Because of this setup, do **not** use container paths or WSL-internal paths for
API submission. Submit Windows-accessible files directly from the host.

## Invoke when

Invoke this skill when the user asks to:

- convert a PDF to Markdown
- convert an image or scanned document to Markdown
- convert `DOCX`, `PPTX`, or `XLSX` to Markdown
- extract a supported local document into an `.md` file
- save parsed Markdown into a specific directory

Do **not** use this skill for:

- web page to markdown tasks
- plain text rewriting
- general summarization without file conversion
- unsupported file types or remote URLs that are not available as local Windows-accessible files

## Required behavior

Follow these rules exactly:

1. Collect an input source first: 1-2 direct file paths, an input directory, or a UTF-8 list file.
2. Require an output directory.
3. If the user did not specify an output directory, ask before running.
4. For 1-2 simple files, direct file arguments are acceptable, but **must always be wrapped in double quotes** regardless of whether they contain spaces.
5. For more than `2` files, directory conversion, retry batches, or filenames containing smart quotes such as `“”`, use `--input-dir` or `--list-file` so Python collects paths internally. All paths passed to these flags **must also be wrapped in double quotes**.
6. Execute strictly serially.
7. Do not submit multiple parse tasks in parallel.
8. Use the local API at `http://127.0.0.1:8000` unless the user explicitly asks otherwise.
9. Prefer deterministic behavior over convenience.
10. Fail early on invalid paths, unsupported file types, or missing output directory.
11. After successfully saving Markdown on the Windows host, attempt to clean the corresponding container task directory by default.
12. Only keep container-side task artifacts when the user explicitly asks to keep them.
13. Treat per-task cleanup as best effort: report cleanup warnings, but do not treat cleanup failure as conversion failure.
14. Do not create ad hoc batch conversion scripts; use this script's `--input-dir`, `--list-file`, `--dry-run`, `--result-file`, `--failure-list`, and `--skip-existing` options instead.

## Long batch execution

When the batch will run for more than 10 minutes (many documents or large PDFs):

- Start the script through `cmd /c start /b` or a Python `subprocess.Popen` with `CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS` flags. Do **not** use `subprocess.run()` or inline `conda run` for long batches — Trae IDE keyboard events can reach the child process and kill it via `KeyboardInterrupt`.
- If Trae IDE shows a "model loop detected" or "request interrupted" popup during a long batch, check the MinerU `/health` endpoint first — the detached process is likely still running.
- After the batch finishes (all files saved), suggest `docker restart mineru-api` to clear GPU VRAM before the next batch.
- Time estimates for non-detached short runs: report after the fact from JSON output. For pre-run estimates, use this dual model:

| Document size | Estimation | Source |
|---|---|---|
| Pages ≥ 50 | `pages / 60` min (digital) or `pages / 30` min (scanned) | 16-textbook calibration |
| Pages < 50 (batch) | 35-55s per document (file-size tiered) | 342-arXiv calibration |

Estimates carry ~10% error for large docs, ~15% for small-doc batches. Report the estimate as a range.

## Path rules

Accept these path styles:

- normal Windows paths like `D:\docs\a.pdf`
- Windows-accessible `\\wsl$\...` paths
- `/mnt/c/...` style input, which the script can normalize automatically

Do **not** directly execute Linux-only paths like `/home/user/a.pdf`.
If the user gives a Linux-only path, ask them for a Windows-accessible path.

## Supported file types

Only use this skill for these extensions:

- `.pdf`
- `.png`
- `.jpg`
- `.jpeg`
- `.jp2`
- `.webp`
- `.gif`
- `.bmp`
- `.doc`
- `.docx`
- `.ppt`
- `.pptx`
- `.xls`
- `.xlsx`

If the file extension is outside this set, stop and tell the user the file type
is not supported by this skill.

## Preflight checklist

Before running the command, confirm all of the following:

1. Exactly one input mode is used: direct files, `--input-dir`, or `--list-file`.
2. Direct file count is `1` or `2`; larger batches use `--input-dir` or `--list-file`.
3. The output directory is known.
4. The task is truly a document-to-Markdown conversion request.
5. The user is not asking for parallel batch conversion.
6. Every input source is Windows-accessible.
7. For uncertain batches, run `--dry-run` first to preview the exact input set instead of writing a temporary enumeration script.
8. For interrupted or repeated batches, use `--skip-existing` unless the user explicitly wants duplicate versioned output or overwrite.

If any item fails, do not execute the script yet.

## Execution flow

Use this decision flow:

1. Identify the input source.
2. Use direct file arguments only for 1-2 simple paths.
3. Use `--input-dir` for a directory of supported documents.
4. Use `--list-file` when filenames contain shell-sensitive characters or when retrying a saved failure list.
5. Validate that every file path is Windows-accessible and supported.
6. Check whether the user provided an output directory.
7. If missing, ask where to save the Markdown files.
8. Run the Python script directly.
9. Read the JSON result from stdout.
10. Treat stderr as progress/error context, not as the authoritative result.
11. Report saved output paths back to the user.
12. Preserve document images by exporting the container parse directory, not by writing only `md_content`.
13. For long batches, add `--result-file` so the final JSON is available even if terminal output scrolls away.
14. For resume workflows, add `--skip-existing` so already exported Markdown files are not submitted again.

## Command to run

Run the Python script directly with an absolute script path:

```powershell
python ".trae/skills/mineru-to-md/scripts/mineru_to_md.py" `
  --output-dir "D:\target\dir" `
  "D:\input\file.pdf"
```

For two files, still run one command only; the script will submit them serially:

```powershell
python ".trae/skills/mineru-to-md/scripts/mineru_to_md.py" `
  --output-dir "D:\target\dir" `
  "D:\input\a.pdf" `
  "D:\input\b.docx"
```

Use `py -3` instead of `python` only when the Windows environment does not expose
`python` on `PATH`.

For a directory batch, do not pass each filename through the shell. Let Python
enumerate the directory:

```powershell
python ".trae/skills/mineru-to-md/scripts/mineru_to_md.py" `
  --input-dir "D:\input\PDF" `
  --output-dir "D:\target\MD"
```

To preview a directory batch without connecting to MinerU:

```powershell
python ".trae/skills/mineru-to-md/scripts/mineru_to_md.py" `
  --input-dir "D:\input\PDF" `
  --dry-run
```

For recursive directory conversion:

```powershell
python ".trae/skills/mineru-to-md/scripts/mineru_to_md.py" `
  --input-dir "D:\input\documents" `
  --recursive `
  --output-dir "D:\target\MD"
```

For paths with smart quotes or other shell-sensitive characters, write a UTF-8
text file with one path per line, then run:

```powershell
python ".trae/skills/mineru-to-md/scripts/mineru_to_md.py" `
  --list-file "D:\input\files.txt" `
  --output-dir "D:\target\MD"
```

For batch work where failures should be easy to retry, add `--failure-list`:

```powershell
python ".trae/skills/mineru-to-md/scripts/mineru_to_md.py" `
  --input-dir "D:\input\PDF" `
  --output-dir "D:\target\MD" `
  --result-file "D:\target\result.json" `
  --failure-list "D:\target\failed.txt"
```

For interrupted batches or safe reruns, add `--skip-existing`:

```powershell
python ".trae/skills/mineru-to-md/scripts/mineru_to_md.py" `
  --input-dir "D:\input\PDF" `
  --output-dir "D:\target\MD" `
  --skip-existing `
  --result-file "D:\target\result.json"
```

For stats injection alongside conversion, add `--stats`:

```powershell
python ".trae/skills/mineru-to-md/scripts/mineru_to_md.py" `
  --input-dir "D:\input\PDF" `
  --output-dir "D:\target\MD" `
  --stats `
  --result-file "D:\target\result.json"
```

## Default parameters

The script defaults are:

- `base_url=http://127.0.0.1:8000`
- `backend=hybrid-auto-engine`
- `parse_method=auto`
- `lang=ch`
- `return_md=true`
- `timeout=1800`
- `retry_timeout=3600`
- best-effort container task cleanup after success
- stdout JSON is always the primary result; `--result-file` can write a copy to disk
- existing output is not skipped by default; use `--skip-existing` for resume workflows
- `--stats` reads saved Markdown and injects formula/image/table counts + scanned PDF detection into each `saved` entry. **Recommend always using `--stats` for batch conversions** — it eliminates the need for post-conversion grep checks.

Do not override them unless the task clearly requires it.

Large PDFs, scanned documents, and documents with many images may need a longer
first wait. Use `--timeout 3600` when the user mentions large files or prior
timeouts. By default, a task that times out after `1800` seconds is submitted
again once and waited up to `3600` seconds.

## Stability notes

The implementation already performs these checks:

- validates `base_url`
- validates output directory shape
- rejects unsupported file extensions
- rejects missing input files
- supports directory and list-file input without shell-level filename passing
- supports `--dry-run` to preview resolved inputs without contacting MinerU
- reports skipped unsupported files from directory input as `skipped`
- supports `--result-file` for durable JSON output
- can write failed input paths to a UTF-8 failure list for later retry
- supports `--skip-existing` for interrupted batch resume without duplicate `_2` outputs
- rejects suspicious task IDs before container operations
- polls task status serially
- retries transient status/result fetch failures
- retries a timed-out task once with a longer timeout by default
- rejects unknown task states instead of guessing
- writes Markdown via a temporary file before replacing the final `.md`
- attempts to remove `/vllm-workspace/output/<task_id>` after successful host-side save by default
- returns a non-zero exit code only for conversion failures, not cleanup warnings

Rely on these checks, but still do the skill-level preflight before execution.

## Expected script result

On success, stdout is JSON shaped like:

```json
{
  "saved": [
    {
      "input": "D:\\docs\\demo.pdf",
      "output": "D:\\output\\demo\\demo.md",
      "document_dir": "D:\\output\\demo",
      "images_dir": "D:\\output\\demo\\image",
      "container_parse_dir": "/vllm-workspace/output/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/demo",
      "task_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
  ]
}
```

When `--stats` is used, each `saved` entry also contains a `stats` object:

```json
{
  "saved": [
    {
      "input": "D:\\docs\\demo.pdf",
      "output": "D:\\output\\demo\\demo.md",
      "stats": {
        "block_formulas": 45,
        "inline_formulas": 23,
        "details_images": 12,
        "md_images": 3,
        "tables": 7,
        "is_scanned_pdf": false
      }
    }
  ]
}
```

`is_scanned_pdf` is `true` when `block_formulas < 10 AND (details_images + md_images) > 50` — calibrated from 23-textbook dataset.

For directory input, stdout may include unsupported files that were skipped:

```json
{
  "saved": [],
  "skipped": [
    {
      "path": "D:\\docs\\notes.txt",
      "reason": "unsupported_extension"
    }
  ]
}
```

When `--skip-existing` is used, stdout may include already completed files:

```json
{
  "saved": [],
  "skipped_existing": [
    {
      "input": "D:\\docs\\demo.pdf",
      "output": "D:\\output\\demo\\demo.md",
      "reason": "output_exists"
    }
  ]
}
```

If some files fail, stdout may also contain:

```json
{
  "saved": [],
  "errors": [
    {
      "input": "D:\\docs\\bad.pdf",
      "error": "..."
    }
  ]
}
```

Treat non-zero exit codes as failure and summarize the error clearly.
Treat stdout JSON as the source of truth.

## Output shape

For stability, the exported host-side result should look like:

- `D:\target\demo\demo.md`
- `D:\target\demo\image\...`

Treat `--output-dir` as the topic directory. Each input document is exported
into its own document directory so the Markdown and images stay self-contained,
which is better for long-term knowledge base management and later wiki use.

Default reruns create versioned output directories like `demo_2` when `demo`
already exists. Use `--skip-existing` for resume workflows, or `--overwrite`
when the user explicitly wants to replace existing document output.

The script rewrites relative image references from `images/...` or
`./images/...` to `image/...` so the Markdown remains directly usable inside
its document directory on the Windows host.

## Output content reference

After conversion completes, the saved `.md` file contains these machine-readable signals.  The agent can inspect them by reading the `.md` file directly (no external tools needed):

- **Images**: `<details>` blocks with 22 type labels (`line`, `scatter`, `flowchart`, `text_image`, `table`, `bar`, `pie`, `histogram`, `boxplot`, `heatmap`, `network`, `tree`, `mindmap`, `gantt`, `venn`, `radar`, `sankey`, `funnel`, `parallel`, `sunburst`, `waterfall`, `map`).  Also Markdown `![]()` references.
- **Formulas**: `$$` blocks = block-level LaTeX.  `$...$` inline = inline LaTeX.
- **Inline images**: `<image:` blocks embedded in sentence flow.
- **Tables**: Standard Markdown pipe tables (`|---|---|`).

Use `image_dir` from the JSON output to locate extracted image files.  All images are exported alongside the `.md` file, not embedded.

## Known limitations

Report these to the user when the input document type makes them likely:

| Input type | Failure mode | Mitigation |
|---|---|---|
| Scanned PDF / image-based document | Handwritten LaTeX OCR errors; italic/greek symbol confusion | Suggest manual formula audit for formula-dense scanned pages |
| Multi-column academic papers | Column reading order may not match semantic order; inter-column figure placement offset | Preview the first 3 pages before batch production use |
| Complex tables (merged cells, multi-row headers) | Cell boundaries may break; merged cells may be split into disjoint fragments | Flag for manual table review when tables are critical |
| Large matrix formulas | Matrix brackets may be split across lines; alignment lost | Matrices remain semantically valid as LaTeX source, but visual rendering may differ from original |
| Documents with mixed CJK + Latin in math mode | Spacing and font switches may produce artifact characters | Common in Chinese textbooks; usually cosmetic, not semantic loss |

## Quality verification

When the user asks to verify output quality, perform two levels of check.

### Level 1: Automated integrity check (agent-runnable)

If the conversion was run with `--stats`, read the `stats` object from the JSON output directly — skip the grep steps below.

Otherwise, verify these signals by reading the `.md` file. Use the Trae `Grep` tool (`output_mode: "count"`) for each step — do **not** run raw shell `grep` commands:

1. **Formula count**: `Grep` with pattern `\$\$`, `output_mode: "count"` (each pair = 1 block formula). For inline: pattern `\$[^$]+\$`, `output_mode: "count"`.
2. **Bracket pairing**: block `$$` count must be even (no unclosed blocks). If the count is odd, read the file around the unmatched `$$` and report the line number.
3. **Mid-formula breaks**: Read the file with `output_mode: "content"` using pattern `\$\$[\s\S]*?\$\$` (multiline). Flag any block that contains an empty line (`\n\n`) between the `$$` delimiters.
4. **Image count**: `Grep` with pattern `<details>`, `output_mode: "count"`. Then pattern `!\[\]\(`, `output_mode: "count"`.
5. **Table count**: `Grep` with pattern `^\|.*\|.*\|$`, `output_mode: "count"`.

Report findings as:

```text
Formulas: 45 block ($$ pairs √), 23 inline  — 0 unclosed blocks
Images:   12 details blocks, 3 ![]() refs
Tables:   7 pipe tables
Warnings: 1 — matrix block at line 142 has mid-formula line break
```

When `--stats` was not used, also run a **scanned PDF detection** heuristic:

- If block formula count < 10 AND image count > 50, the document is likely a scanned PDF with minimal extractable text. Add `"warning": "scanned_pdf"` to the report and tell the user the output may have limited semantic value.
- Thresholds calibrated from 23-textbook dataset: all scanned PDFs fell below `formula<10 & images>50`, all digital PDFs exceeded both thresholds.

### Level 2: Manual audit (methodology — tell the user)

For visual quality, the user should do a three-column comparison on a few sample pages:

```text
PDF original page → MinerU .md output → PyMuPDF text extraction (baseline)
```

Three audit dimensions:

1. **OCR precision**: Compare characters, especially subscripts/superscripts/greek letters in formula blocks.
2. **Formula integrity**: Check that `$$` blocks are complete and render correctly.
3. **Image association**: Verify that `<details>` blocks appear near their surrounding text context.

For quick spot-checking, the agent can read the first 100 lines of the `.md` and flag any obviously malformed `$$` blocks or `<details>` tags.

Do not audit every conversion automatically. Only run Level 1 when the user asks for quality verification; only suggest Level 2 when the input type matches the known limitations table above.

## Failure handling

If the API cannot be reached:

- tell the user MinerU is not reachable from Windows
- ask them to start or restore the WSL-side service
- suggest running `docker restart mineru-api` and waiting for `/health` to return healthy

If the direct input count is greater than `2`:

- do not run the script
- use `--input-dir` or `--list-file` instead

If the output directory is missing:

- do not run the script
- ask the user where to save the Markdown files

If the path is Linux-only or not Windows-accessible:

- do not run the script
- ask the user for a Windows path or `\\wsl$\...` path

If the extension is unsupported:

- do not run the script
- explain that this skill only handles the supported document/image formats

If filenames contain smart quotes such as `“”`, shell metacharacters, or very
long paths:

- do not pass those paths as direct shell arguments
- use `--input-dir` when all target files are in one directory
- use `--list-file` when the target set is selective

If a batch may need later retry:

- add `--failure-list "D:\target\failed.txt"`
- rerun with `--list-file "D:\target\failed.txt"` after fixing the underlying issue

If a batch was interrupted or might already have completed files:

- add `--skip-existing`
- optionally run `--dry-run --skip-existing --output-dir "D:\target\MD"` first
- use `skipped_existing` to confirm what will not be resubmitted

If the agent needs to inspect the batch before conversion:

- run the same input command with `--dry-run`
- use the JSON `inputs` array as the source of truth
- do not create a temporary Python script just to enumerate files

If the batch is long-running:

- add `--result-file "D:\target\result.json"`
- read that JSON file after completion if stdout is hard to inspect

If stdout is not valid JSON:

- treat the run as failed
- summarize the raw failure signal briefly
- do not guess output paths

If host-side save succeeds but container cleanup fails:

- tell the user the Markdown file was saved successfully
- explicitly report that container artifacts may still remain
- do not claim cleanup succeeded unless the JSON `cleaned` field confirms it
- treat `cleanup_errors` as warnings; the process exit code remains success when all conversions succeeded

## Implementation files

This skill relies on:

- `.trae/skills/mineru-to-md/scripts/mineru_to_md.py`
