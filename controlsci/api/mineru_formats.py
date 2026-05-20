"""Backend-specific MinerU format policy.

The official cloud URL API, official signed-upload API, local Docker API, and
local replay fallback are related but not identical surfaces. Keep their
extension policies separate to avoid false rejects or false accepts.
"""

from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import unquote, urlparse


OFFICIAL_URL_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".png",
    ".jpg",
    ".jpeg",
    ".jp2",
    ".webp",
    ".gif",
    ".bmp",
    ".html",
}

OFFICIAL_UPLOAD_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".png",
    ".jpg",
    ".jpeg",
    ".jp2",
    ".webp",
    ".gif",
    ".bmp",
    ".html",
}

LOCAL_DOCKER_DEFAULT_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".jp2",
    ".webp",
    ".gif",
    ".bmp",
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
}

REPLAY_EXTENSIONS = {".pdf", ".md", ".markdown"}


def _parse_extensions(raw: str, default: set[str]) -> set[str]:
    if not raw.strip():
        return set(default)
    result = set()
    for item in raw.split(","):
        ext = item.strip().lower()
        if not ext:
            continue
        result.add(ext if ext.startswith(".") else f".{ext}")
    return result or set(default)


def official_url_extensions() -> set[str]:
    return _parse_extensions(os.environ.get("CONTROLMIND_OFFICIAL_URL_EXTENSIONS", ""), OFFICIAL_URL_EXTENSIONS)


def official_upload_extensions() -> set[str]:
    return _parse_extensions(os.environ.get("CONTROLMIND_OFFICIAL_UPLOAD_EXTENSIONS", ""), OFFICIAL_UPLOAD_EXTENSIONS)


def local_docker_extensions() -> set[str]:
    return _parse_extensions(os.environ.get("CONTROLMIND_LOCAL_MINERU_EXTENSIONS", ""), LOCAL_DOCKER_DEFAULT_EXTENSIONS)


def replay_extensions() -> set[str]:
    return _parse_extensions(os.environ.get("CONTROLMIND_REPLAY_EXTENSIONS", ""), REPLAY_EXTENSIONS)


def extensions_for_backend(backend: str) -> set[str]:
    backend = (backend or "local").strip().lower()
    if backend == "official_url":
        return official_url_extensions()
    if backend == "official":
        return official_upload_extensions()
    if backend == "replay":
        return replay_extensions()
    if backend in {"local", "auto"}:
        return local_docker_extensions()
    return set()


def format_label(extensions: set[str]) -> str:
    return "/".join(ext.lstrip(".").upper() for ext in sorted(extensions))


def path_suffix(path_value: str | Path) -> str:
    return Path(str(path_value)).suffix.lower()


def is_supported_path(path_value: str | Path, backend: str) -> bool:
    return path_suffix(path_value) in extensions_for_backend(backend)


def is_supported_url(raw_url: str, backend: str = "official_url") -> bool:
    parsed = urlparse(raw_url or "")
    suffix = Path(unquote(parsed.path or "")).suffix.lower()
    extensions = extensions_for_backend(backend)
    if suffix in extensions:
        return True
    query = unquote(parsed.query or "").lower()
    return any(ext in query for ext in extensions)
