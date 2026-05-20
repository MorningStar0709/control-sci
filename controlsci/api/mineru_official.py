"""MinerU official API client for signed-upload document extraction."""

from __future__ import annotations

from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path
import time
import zipfile

import httpx


@dataclass
class MinerUOfficialResult:
    status: str
    parse_ok: bool
    detail: str
    task_id: str = ""
    markdown: str = ""
    artifacts: dict = field(default_factory=dict)


def _write_zip_artifacts(zip_bytes: bytes, output_dir: Path, doc_stem: str) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    artifacts: dict = {"files": []}
    with zipfile.ZipFile(BytesIO(zip_bytes)) as zf:
        names = zf.namelist()
        md_name = next((name for name in names if name.endswith("full.md")), "")
        if not md_name:
            md_name = next((name for name in names if name.lower().endswith(".md")), "")
        markdown = zf.read(md_name).decode("utf-8", errors="replace") if md_name else ""

        for name in names:
            if name.endswith("/"):
                continue
            lower = name.lower()
            if not (
                lower.endswith(".json")
                or lower.endswith(".md")
                or "/image/" in lower
                or "/images/" in lower
                or lower.endswith((".png", ".jpg", ".jpeg", ".webp"))
            ):
                continue
            src_name = Path(name)
            if lower.endswith(".md"):
                dest = output_dir / f"{doc_stem}.md"
            elif "/image/" in lower or "/images/" in lower or lower.endswith((".png", ".jpg", ".jpeg", ".webp")):
                dest = output_dir / "image" / src_name.name
            else:
                dest = output_dir / src_name.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(zf.read(name))
            artifacts["files"].append(str(dest))

        if markdown and not (output_dir / f"{doc_stem}.md").exists():
            md_path = output_dir / f"{doc_stem}.md"
            md_path.write_text(markdown, encoding="utf-8")
            artifacts["files"].append(str(md_path))
        artifacts["markdown_path"] = str(output_dir / f"{doc_stem}.md") if markdown else ""
        artifacts["markdown"] = markdown
        artifacts["zip_entries"] = names
    return artifacts


def parse_mineru_official_upload(
    pdf_path: Path,
    *,
    token: str,
    base_url: str = "https://mineru.net",
    model_version: str = "vlm",
    language: str = "ch",
    timeout: int = 180,
    output_dir: Path | None = None,
    data_id: str | None = None,
) -> MinerUOfficialResult:
    """Upload a local document to the official MinerU API and fetch Markdown output."""

    if not token:
        return MinerUOfficialResult("failed", False, "MINERU_API_TOKEN 未配置")

    base_url = base_url.rstrip("/")
    data_id = data_id or pdf_path.stem
    try:
        with httpx.Client(timeout=30, trust_env=False) as client:
            create_resp = client.post(
                f"{base_url}/api/v4/file-urls/batch",
                params={"enable_formula": "true", "enable_table": "true", "language": language},
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                json={"files": [{"name": pdf_path.name, "data_id": data_id}], "model_version": model_version or "vlm"},
            )
            if create_resp.status_code != 200:
                return MinerUOfficialResult("failed", False, f"MinerU 官方上传 URL 申请失败 HTTP {create_resp.status_code}")
            create_data = create_resp.json()
            if create_data.get("code") != 0:
                return MinerUOfficialResult("failed", False, f"MinerU 官方上传 URL 申请失败: {create_data.get('msg') or create_data}")

            data = create_data.get("data") or {}
            batch_id = data.get("batch_id", "")
            urls = data.get("file_urls") or []
            if not batch_id or not urls:
                return MinerUOfficialResult("failed", False, "MinerU 官方 API 未返回 batch_id/file_urls")

            with pdf_path.open("rb") as f:
                put_resp = client.put(urls[0], content=f.read(), headers={})
            if put_resp.status_code not in (200, 201):
                return MinerUOfficialResult("failed", False, f"MinerU 官方文件上传失败 HTTP {put_resp.status_code}", task_id=batch_id)

            deadline = time.time() + timeout
            last_state = ""
            last_detail = ""
            full_zip_url = ""
            while time.time() < deadline:
                time.sleep(3)
                result_resp = client.get(
                    f"{base_url}/api/v4/extract-results/batch/{batch_id}",
                    headers={"Authorization": f"Bearer {token}", "Accept": "*/*"},
                    timeout=20,
                )
                if result_resp.status_code != 200:
                    last_detail = f"HTTP {result_resp.status_code}"
                    continue
                result_data = result_resp.json()
                extract_results = ((result_data.get("data") or {}).get("extract_result") or [])
                first = extract_results[0] if extract_results else {}
                last_state = first.get("state", "")
                last_detail = first.get("err_msg", "") or last_state
                if last_state == "done":
                    full_zip_url = first.get("full_zip_url", "")
                    break
                if last_state == "failed":
                    return MinerUOfficialResult("failed", False, f"MinerU 官方解析失败: {last_detail}", task_id=batch_id)
            else:
                return MinerUOfficialResult("timeout", False, f"MinerU 官方解析超时，最后状态: {last_state or last_detail or 'unknown'}", task_id=batch_id)

            if not full_zip_url:
                return MinerUOfficialResult("failed", False, "MinerU 官方解析完成但未返回 full_zip_url", task_id=batch_id)

            zip_resp = client.get(full_zip_url, timeout=60)
            if zip_resp.status_code != 200:
                return MinerUOfficialResult("failed", False, f"MinerU 官方结果下载失败 HTTP {zip_resp.status_code}", task_id=batch_id)

            artifacts: dict = {"full_zip_url": full_zip_url}
            markdown = ""
            if output_dir is not None:
                artifacts.update(_write_zip_artifacts(zip_resp.content, output_dir, pdf_path.stem))
                markdown = artifacts.get("markdown", "")
            else:
                with zipfile.ZipFile(BytesIO(zip_resp.content)) as zf:
                    md_name = next((name for name in zf.namelist() if name.endswith("full.md")), "")
                    if not md_name:
                        md_name = next((name for name in zf.namelist() if name.lower().endswith(".md")), "")
                    if not md_name:
                        return MinerUOfficialResult("failed", False, "MinerU 官方结果包中未找到 Markdown", task_id=batch_id)
                    markdown = zf.read(md_name).decode("utf-8", errors="replace")

            return MinerUOfficialResult(
                "ok",
                True,
                f"MinerU 官方 API 解析完成，{len(markdown)} 字符 markdown",
                task_id=batch_id,
                markdown=markdown,
                artifacts=artifacts,
            )
    except Exception as exc:
        return MinerUOfficialResult("failed", False, f"MinerU 官方 API 调用失败: {str(exc)[:180]}")
