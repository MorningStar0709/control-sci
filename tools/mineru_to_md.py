#!/usr/bin/env python3
# Copy of mineru-to-md Skill script for Agent-driven document parsing.
# Original: .trae/skills/mineru-to-md/scripts/mineru_to_md.py
# This standalone copy is referenced by _exec_mineru_parse handler in agent_cli.py.
"""MinerU-to-MD: call local MinerU API to convert documents to Markdown."""
import argparse
import json
import os
import posixpath
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse
from typing import Any

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from controlsci.api.mineru_official import parse_mineru_official_upload
from controlsci.api.mineru_formats import (
    extensions_for_backend,
    format_label,
    is_supported_path,
)


DEFAULT_BASE_URL = "http://127.0.0.1:8000"
DEFAULT_BACKEND = "hybrid-auto-engine"
DEFAULT_PARSE_METHOD = "auto"
DEFAULT_LANG = "ch"
DEFAULT_TIMEOUT = 1800
DEFAULT_RETRY_TIMEOUT = 3600
DEFAULT_POLL_INTERVAL = 2.0
MAX_FILES = 2
STATUS_RETRY_COUNT = 3
RESULT_RETRY_COUNT = 3
DEFAULT_CONTAINER_NAME = "mineru-api"
DEFAULT_CONTAINER_OUTPUT_ROOT = "/vllm-workspace/output"
PARSER_BACKENDS = {"local", "official", "auto", "replay"}
DATA_CLASSES = {
    "public_open",
    "public_but_regulated",
    "private_enterprise",
    "private_medical",
    "confidential_defense",
    "derived_sensitive",
}
CLOUD_ALLOWED_DATA_CLASSES = {"public_open", "public_but_regulated"}
TASK_ID_PATTERN = re.compile(r"^[0-9a-fA-F-]{8,}$")
IMAGE_REF_PATTERN = re.compile(r"(?P<prefix>[\(\"'=])(?:\./)?images/")
STATS_BLOCK_FORMULA = re.compile(r"\$\$")
STATS_INLINE_FORMULA = re.compile(r"\$[^$]+\$")
STATS_DETAILS_IMAGE = re.compile(r"<details>")
STATS_MD_IMAGE = re.compile(r"!\[\]\(image/")
STATS_TABLE = re.compile(r"^\|.*\|.*\|$", re.MULTILINE)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def parse_args():
    parser = argparse.ArgumentParser(description="Convert documents to Markdown via MinerU API.")
    parser.add_argument("files", nargs="*", help="Files to convert (max 2 for direct mode)")
    parser.add_argument("--input-dir", help="Directory of files to convert (batch mode)")
    parser.add_argument("--recursive", action="store_true", help="Recurse into subdirectories")
    parser.add_argument("--output-dir", help="Output directory for Markdown files")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help=f"API base URL (default: {DEFAULT_BASE_URL})")
    parser.add_argument("--mineru-backend", "--local-backend", dest="mineru_backend", default=DEFAULT_BACKEND)
    parser.add_argument(
        "--backend",
        "--parser-backend",
        "--backend-mode",
        dest="parser_backend",
        choices=sorted(PARSER_BACKENDS),
        default="local",
        help="Parser backend: local(default), official, auto, or replay.",
    )
    parser.add_argument(
        "--data-class",
        choices=sorted(DATA_CLASSES),
        default="private_enterprise",
        help="Data sensitivity class used to decide whether cloud upload is allowed.",
    )
    parser.add_argument(
        "--allow-cloud-upload",
        action="store_true",
        help="Explicitly allow uploading the current file to MinerU official API when data-class permits it.",
    )
    parser.add_argument("--official-base-url", default=os.environ.get("MINERU_OFFICIAL_BASE_URL", "https://mineru.net"))
    parser.add_argument("--official-model-version", default="vlm")
    parser.add_argument("--parse-method", default=DEFAULT_PARSE_METHOD)
    parser.add_argument("--lang", default=DEFAULT_LANG)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--retry-timeout", type=int, default=DEFAULT_RETRY_TIMEOUT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-existing", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--result-file")
    parser.add_argument("--failure-list")
    parser.add_argument("--list-file")
    parser.add_argument("--max-files", type=int, default=0, help="Limit number of collected input files after filtering.")
    parser.add_argument("--no-cleanup", action="store_true")
    return parser.parse_args()


def cloud_upload_allowed(args):
    return args.data_class in CLOUD_ALLOWED_DATA_CLASSES and args.allow_cloud_upload


def cloud_upload_refusal(args):
    if args.data_class not in CLOUD_ALLOWED_DATA_CLASSES:
        return (
            f"Refusing cloud upload: data_class={args.data_class} is local-only. "
            "Use --backend local for private or sensitive documents."
        )
    if not args.allow_cloud_upload:
        return (
            "Refusing cloud upload: official MinerU API requires --allow-cloud-upload "
            "and data_class in [public_open, public_but_regulated]."
        )
    if not os.environ.get("MINERU_API_TOKEN") and not os.environ.get("MINERU_OFFICIAL_TOKEN"):
        return "Refusing cloud upload: MINERU_API_TOKEN or MINERU_OFFICIAL_TOKEN is not configured."
    return ""


def normalize_base_url(url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"http://{url}"
    return url.rstrip("/")


def collect_input_files(args):
    skipped = []
    files = []
    supported_backend = "local" if args.parser_backend == "auto" else args.parser_backend
    supported = extensions_for_backend(supported_backend)

    def append_if_supported(path: Path):
        if is_supported_path(path, supported_backend):
            files.append(path)
        else:
            skipped.append({
                "path": str(path),
                "reason": "unsupported_extension",
                "backend": supported_backend,
                "supported": sorted(supported),
            })

    if args.list_file:
        for line in Path(args.list_file).read_text(encoding="utf-8-sig").splitlines():
            line = line.strip()
            if not line:
                continue
            append_if_supported(Path(line))
    elif args.input_dir:
        pattern = "**/*" if args.recursive else "*"
        for p in sorted(Path(args.input_dir).glob(pattern)):
            if p.is_file():
                append_if_supported(p)
    elif args.files:
        for f in args.files:
            append_if_supported(Path(f))
    if args.max_files > 0:
        files = files[:args.max_files]
    return files, skipped


def validate_input_files(files):
    if not files:
        raise ValueError("No supported input files found.")
    invalid = [f for f in files if not f.exists()]
    if invalid:
        raise ValueError(f"Files not found: {', '.join(str(f) for f in invalid)}")
    if len(files) > MAX_FILES and not hasattr(parse_args(), 'input_dir'):
        pass


def ensure_service_available(base_url):
    try:
        req = urllib.request.Request(f"{base_url}/health")
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("status") != "healthy":
                raise RuntimeError(f"MinerU API unhealthy: {data}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Cannot reach MinerU API at {base_url}: {e}")


def submit_task(base_url, file_path, args):
    curl_cmd = [
        "curl", "-s", "-X", "POST", f"{base_url}/tasks",
        "-F", f"files=@{file_path}",
        "-F", f"backend={args.mineru_backend}",
        "-F", f"parse_method={args.parse_method}",
        "-F", f"lang_list={args.lang}",
        "-F", "return_md=true",
    ]
    try:
        result = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            raise RuntimeError(f"curl failed: {result.stderr[:200]}")
        data = json.loads(result.stdout)
        task_id = data.get("task_id") or data.get("id") or data.get("data", {}).get("task_id")
        if not task_id:
            raise RuntimeError(f"No task_id in response: {result.stdout[:200]}")
        return task_id
    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON from API: {result.stdout[:200]}")
    except FileNotFoundError:
        raise RuntimeError("curl command not found. Is curl installed?")


def poll_task(base_url, task_id, timeout_seconds, poll_interval=DEFAULT_POLL_INTERVAL):
    deadline = time.time() + timeout_seconds
    status_url = f"{base_url}/tasks/{task_id}"

    for _ in range(STATUS_RETRY_COUNT):
        try:
            while time.time() < deadline:
                req = urllib.request.Request(status_url)
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                status = data.get("status") or data.get("data", {}).get("status")
                if status in ("completed", "done", "success"):
                    return "completed"
                if status in ("failed", "error"):
                    raise RuntimeError(f"Task failed: {data}")
                time.sleep(poll_interval)
            raise TimeoutError(f"Task {task_id} timed out after {timeout_seconds}s")
        except (urllib.error.URLError, ConnectionError):
            time.sleep(5)
    raise RuntimeError(f"Failed to poll status for task {task_id}")


def get_task_result(base_url, task_id):
    result_url = f"{base_url}/tasks/{task_id}/result"
    for _ in range(RESULT_RETRY_COUNT):
        try:
            req = urllib.request.Request(result_url)
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, ConnectionError):
            time.sleep(5)
    raise RuntimeError(f"Failed to fetch result for task {task_id}")


def export_from_container(task_id, output_dir, doc_stem):
    container_output = f"{DEFAULT_CONTAINER_OUTPUT_ROOT}/{task_id}/{doc_stem}/hybrid_auto"
    doc_dir = Path(output_dir) / doc_stem
    doc_dir.mkdir(parents=True, exist_ok=True)

    export_cmd = ["docker", "cp", f"{DEFAULT_CONTAINER_NAME}:{container_output}/.", str(doc_dir)]
    result = subprocess.run(export_cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        raise RuntimeError(f"docker cp failed: {result.stderr[:200]}")


    for md_file in doc_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        content = IMAGE_REF_PATTERN.sub(r"\1image/", content)
        md_file.write_text(content, encoding="utf-8", newline="\n")


    images_dir = doc_dir / "image"
    if not images_dir.exists() and (doc_dir / "image").exists():
        (doc_dir / "image").rename(images_dir)


def cleanup_container(task_id):
    try:
        subprocess.run(
            ["docker", "exec", DEFAULT_CONTAINER_NAME, "rm", "-rf",
             f"{DEFAULT_CONTAINER_OUTPUT_ROOT}/{task_id}"],
            capture_output=True, timeout=10,
        )
        return True, None
    except Exception as e:
        return False, str(e)[:200]


def compute_stats(md_path):
    text = Path(md_path).read_text(encoding="utf-8")
    block_formulas = len(STATS_BLOCK_FORMULA.findall(text)) // 2
    inline_formulas = len(STATS_INLINE_FORMULA.findall(text))
    details_images = len(STATS_DETAILS_IMAGE.findall(text))
    md_images = len(STATS_MD_IMAGE.findall(text))
    tables = len(STATS_TABLE.findall(text))
    is_scanned = block_formulas < 10 and (details_images + md_images) > 50
    return {
        "block_formulas": block_formulas,
        "inline_formulas": inline_formulas,
        "details_images": details_images,
        "md_images": md_images,
        "tables": tables,
        "is_scanned_pdf": is_scanned,
    }


def write_parse_result(doc_dir, entry, backend, args, status="ok", detail=""):
    payload = {
        "status": status,
        "backend": backend,
        "data_class": args.data_class,
        "cloud_upload": backend == "official",
        "detail": detail,
        **entry,
    }
    result_path = Path(doc_dir) / "parse_result.json"
    result_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(result_path)


def extract_pdf_markdown_fallback(file_path, limit_pages=8):
    if Path(file_path).suffix.lower() != ".pdf":
        return ""
    try:
        from pypdf import PdfReader
    except Exception:
        return ""
    try:
        reader = PdfReader(str(file_path))
        parts = [f"# {Path(file_path).stem}", "", f"> 本地轻量 replay：pypdf 提取前 {min(len(reader.pages), limit_pages)} 页文本。", ""]
        for idx, page in enumerate(reader.pages[:limit_pages], start=1):
            text = page.extract_text() or ""
            if text.strip():
                parts.append(f"## Page {idx}")
                parts.append(text.strip())
                parts.append("")
        return "\n".join(parts).strip()
    except Exception:
        return ""


def find_existing_replay_markdown(file_path):
    file_path = Path(file_path)
    doc_stem = file_path.stem
    candidates = [
        file_path.parent / "md" / doc_stem / f"{doc_stem}.md",
        file_path.parent / "md" / f"{doc_stem}.md",
        file_path.with_suffix(".md"),
    ]
    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def convert_one_file(args, base_url, output_dir, file_path, timeout_seconds):
    eprint(f"  Submitting: {file_path}")

    doc_stem = file_path.stem
    doc_dir = Path(output_dir) / doc_stem
    doc_dir.mkdir(parents=True, exist_ok=True)
    saved_md_path = doc_dir / f"{doc_stem}.md"

    task_id = submit_task(base_url, file_path, args)
    eprint(f"  Task ID: {task_id}, waiting up to {timeout_seconds}s")

    try:
        poll_task(base_url, task_id, timeout_seconds)
    except TimeoutError:
        raise

    result_data = get_task_result(base_url, task_id)
    file_key = file_path.stem
    file_result = result_data.get("results", {}).get(file_key, {})
    md_content = file_result.get("md_content", "")
    if md_content:
        saved_md_path.write_text(md_content, encoding="utf-8")
        eprint(f"  Saved: {saved_md_path}")
    else:
        raise RuntimeError(f"No md_content in result for {file_key}")

    images_dir = doc_dir / "image"
    try:
        container_task_root = f"{DEFAULT_CONTAINER_OUTPUT_ROOT}/{task_id}"
        find_cmd = ["docker", "exec", DEFAULT_CONTAINER_NAME, "find",
                     container_task_root, "-type", "d", "-name", "images"]
        r = subprocess.run(find_cmd, capture_output=True, text=True, timeout=10)
        container_images_dir = r.stdout.strip().splitlines()
        if container_images_dir:
            src = container_images_dir[0].strip()
            if src:
                docker_cp = ["docker", "cp", f"{DEFAULT_CONTAINER_NAME}:{src}/.", str(images_dir)]
                subprocess.run(docker_cp, capture_output=True, text=True, timeout=120)
                md_content = IMAGE_REF_PATTERN.sub(r"\1image/", md_content)
                saved_md_path.write_text(md_content, encoding="utf-8")
                eprint(f"  Images: {len(list(images_dir.iterdir()))} exported to {images_dir}")
    except Exception as e:
        eprint(f"  Warning: image export failed: {e}")

    saved_entry = {
        "input": str(file_path),
        "output": str(saved_md_path),
        "document_dir": str(doc_dir),
        "images_dir": str(images_dir),
        "task_id": task_id,
        "backend": "local",
        "data_class": args.data_class,
        "cloud_upload": False,
    }

    if args.stats:
        saved_entry["stats"] = compute_stats(saved_md_path)

    saved_entry["parse_result"] = write_parse_result(doc_dir, saved_entry, "local", args, status="ok", detail="MinerU local parse completed")

    if not args.no_cleanup:
        ok, err = cleanup_container(task_id)
        if ok:
            return saved_entry, {"container": DEFAULT_CONTAINER_NAME, "path": f"{DEFAULT_CONTAINER_OUTPUT_ROOT}/{task_id}", "task_id": task_id}, None
        else:
            return saved_entry, None, err

    return saved_entry, None, None


def convert_one_file_official(args, output_dir, file_path, timeout_seconds):
    refusal = cloud_upload_refusal(args)
    if refusal:
        raise RuntimeError(refusal)

    doc_stem = file_path.stem
    doc_dir = Path(output_dir) / doc_stem
    doc_dir.mkdir(parents=True, exist_ok=True)
    token = os.environ.get("MINERU_API_TOKEN", os.environ.get("MINERU_OFFICIAL_TOKEN", "")).strip()
    result = parse_mineru_official_upload(
        file_path,
        token=token,
        base_url=args.official_base_url,
        model_version=args.official_model_version,
        language=args.lang,
        timeout=timeout_seconds,
        output_dir=doc_dir,
    )
    if not result.parse_ok:
        raise RuntimeError(result.detail)

    md_path = Path(result.artifacts.get("markdown_path") or (doc_dir / f"{doc_stem}.md"))
    if not md_path.exists() and result.markdown:
        md_path.write_text(result.markdown, encoding="utf-8")
    images_dir = doc_dir / "image"
    saved_entry = {
        "input": str(file_path),
        "output": str(md_path),
        "document_dir": str(doc_dir),
        "images_dir": str(images_dir),
        "task_id": result.task_id,
        "backend": "official",
        "data_class": args.data_class,
        "cloud_upload": True,
        "official_base_url": args.official_base_url,
        "model_version": args.official_model_version,
        "artifacts": result.artifacts,
    }
    if args.stats and md_path.exists():
        saved_entry["stats"] = compute_stats(md_path)
    saved_entry["parse_result"] = write_parse_result(doc_dir, saved_entry, "official", args, status=result.status, detail=result.detail)
    return saved_entry, None, None


def convert_one_file_replay(args, output_dir, file_path):
    doc_stem = file_path.stem
    doc_dir = Path(output_dir) / doc_stem
    doc_dir.mkdir(parents=True, exist_ok=True)
    saved_md_path = doc_dir / f"{doc_stem}.md"
    if saved_md_path.exists() and not args.overwrite:
        detail = "Replay existing markdown"
    else:
        existing_md = find_existing_replay_markdown(file_path)
        if existing_md:
            md = existing_md.read_text(encoding="utf-8", errors="replace")
            detail = f"Replay copied existing markdown from {existing_md}"
        else:
            md = extract_pdf_markdown_fallback(file_path)
            detail = "Replay fallback markdown generated by pypdf"
        if not md:
            raise RuntimeError("Replay backend requires existing markdown or PDF text fallback")
        saved_md_path.write_text(md, encoding="utf-8")
    saved_entry = {
        "input": str(file_path),
        "output": str(saved_md_path),
        "document_dir": str(doc_dir),
        "images_dir": str(doc_dir / "image"),
        "task_id": "",
        "backend": "replay",
        "data_class": args.data_class,
        "cloud_upload": False,
    }
    if args.stats:
        saved_entry["stats"] = compute_stats(saved_md_path)
    saved_entry["parse_result"] = write_parse_result(doc_dir, saved_entry, "replay", args, status="replay", detail=detail)
    return saved_entry, None, None


def main():
    args = parse_args()

    base_url = normalize_base_url(args.base_url)
    input_files, skipped = collect_input_files(args)

    if args.dry_run:
        cloud_refusal = cloud_upload_refusal(args) if args.parser_backend in {"official", "auto"} else ""
        result = {
            "dry_run": True,
            "count": len(input_files),
            "inputs": [str(f) for f in input_files],
            "backend": args.parser_backend,
            "data_class": args.data_class,
            "cloud_upload_allowed": cloud_upload_allowed(args),
            "cloud_refusal": cloud_refusal,
            "supported_formats": format_label(extensions_for_backend(args.parser_backend)),
        }
        if skipped:
            result["skipped"] = skipped
        print(json.dumps(result, ensure_ascii=False))
        return 0

    if not args.output_dir:
        eprint("Error: --output-dir is required")
        return 2

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.parser_backend == "official":
        refusal = cloud_upload_refusal(args)
        if refusal:
            eprint(f"Error: {refusal}")
            return 3

    if args.parser_backend in {"local", "auto"}:
        try:
            ensure_service_available(base_url)
            local_available = True
        except RuntimeError as e:
            local_available = False
            if args.parser_backend == "local":
                eprint(f"Error: {e}")
                return 3
            eprint(f"Warning: local MinerU unavailable, evaluating auto fallback: {e}")
    else:
        local_available = False

    saved = []
    errors = []
    cleaned = []
    cleanup_errors = []
    total = len(input_files)

    for idx, file_path in enumerate(input_files, 1):
        doc_dir = output_dir / file_path.stem
        saved_md_path = doc_dir / f"{file_path.stem}.md"
        if args.skip_existing and saved_md_path.exists() and not args.overwrite:
            skipped_entry = {"input": str(file_path), "output": str(saved_md_path), "reason": "skip_existing"}
            saved.append(skipped_entry)
            eprint(f"[{idx}/{total}] Skipped existing: {saved_md_path}")
            continue
        try:
            if args.parser_backend == "local":
                saved_item, cleanup_info, cleanup_err = convert_one_file(args, base_url, output_dir, file_path, args.timeout)
            elif args.parser_backend == "official":
                saved_item, cleanup_info, cleanup_err = convert_one_file_official(args, output_dir, file_path, args.timeout)
            elif args.parser_backend == "replay":
                saved_item, cleanup_info, cleanup_err = convert_one_file_replay(args, output_dir, file_path)
            elif args.parser_backend == "auto":
                if local_available:
                    try:
                        saved_item, cleanup_info, cleanup_err = convert_one_file(args, base_url, output_dir, file_path, args.timeout)
                    except Exception as local_exc:
                        refusal = cloud_upload_refusal(args)
                        if refusal:
                            raise RuntimeError(f"local parse failed and cloud fallback is blocked: {local_exc}; {refusal}")
                        eprint(f"[{idx}/{total}] Local parse failed, falling back to official API: {local_exc}")
                        saved_item, cleanup_info, cleanup_err = convert_one_file_official(args, output_dir, file_path, args.timeout)
                        saved_item["auto_fallback_from"] = "local"
                else:
                    refusal = cloud_upload_refusal(args)
                    if refusal:
                        raise RuntimeError(f"local MinerU unavailable and cloud fallback is blocked: {refusal}")
                    saved_item, cleanup_info, cleanup_err = convert_one_file_official(args, output_dir, file_path, args.timeout)
                    saved_item["auto_fallback_from"] = "local_unavailable"
            else:
                raise RuntimeError(f"Unknown parser backend: {args.parser_backend}")
            saved.append(saved_item)
            eprint(f"[{idx}/{total}] Saved: {saved_item['output']}")
            if cleanup_info:
                cleaned.append(cleanup_info)
            if cleanup_err:
                cleanup_errors.append({"input": str(file_path), "error": cleanup_err})
        except TimeoutError:
            if args.retry_timeout > args.timeout:
                eprint(f"[{idx}/{total}] Timeout, retrying with longer wait: {file_path}")
                try:
                    saved_item, cleanup_info, cleanup_err = convert_one_file(args, base_url, output_dir, file_path, args.retry_timeout)
                    saved.append(saved_item)
                    if cleanup_info:
                        cleaned.append(cleanup_info)
                except Exception as e2:
                    errors.append({"input": str(file_path), "error": str(e2)[:300]})
            else:
                errors.append({"input": str(file_path), "error": "timeout"})
        except Exception as e:
            errors.append({"input": str(file_path), "error": str(e)[:300]})

    result = {"saved": saved}
    if errors:
        result["errors"] = errors
    if skipped:
        result["skipped"] = skipped
    if cleaned:
        result["cleaned"] = cleaned
    if cleanup_errors:
        result["cleanup_errors"] = cleanup_errors
    if args.result_file:
        Path(args.result_file).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(result, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
