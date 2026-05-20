"""Shared configuration for ControlMind API services."""

from functools import lru_cache
import json
import os
from pathlib import Path

from pydantic import BaseModel


class ApiSettings(BaseModel):
    api_host: str = "127.0.0.1"
    api_port: int = 17001
    mineru_base_url: str = "http://localhost:8000"
    mineru_official_base_url: str = "https://mineru.net"
    mineru_official_token: str = ""
    ollama_base_url: str = "http://localhost:11434"
    upload_max_mb: int = 20
    cloud_demo_profile: str = "cloud_demo"
    cloud_daily_limit: int = 100
    demo_access_code: str = ""
    python_path: str = ""

    @property
    def api_base_url(self) -> str:
        return f"http://{self.api_host}:{self.api_port}"


def _int_env(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, str(default)))
    except ValueError:
        return default


CONFIG_PATH = Path.home() / ".controlmind" / "config.json"


def _read_cli_config() -> dict:
    try:
        if CONFIG_PATH.exists():
            return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"ControlMind 配置文件损坏：{CONFIG_PATH} ({exc})") from exc
    except OSError:
        return {}
    return {}


def _config_value(config: dict, key: str, default: str = "") -> str:
    value = config.get(key, default)
    return str(value).strip() if value is not None else default


def _env_or_config(env_names: tuple[str, ...], config: dict, config_key: str, default: str) -> str:
    for name in env_names:
        value = os.environ.get(name)
        if value is not None and str(value).strip() != "":
            return str(value).strip()
    return _config_value(config, config_key, default)


def _int_env_or_config(env_names: tuple[str, ...], config: dict, config_key: str, default: int) -> int:
    for name in env_names:
        value = os.environ.get(name)
        if value is not None and str(value).strip() != "":
            try:
                return int(value)
            except ValueError:
                return default
    try:
        return int(config.get(config_key, default))
    except (TypeError, ValueError):
        return default


@lru_cache(maxsize=1)
def get_settings() -> ApiSettings:
    config = _read_cli_config()
    return ApiSettings(
        api_host=_env_or_config(("CONTROLMIND_API_HOST", "CONTROLSCI_API_HOST"), config, "api.host", "127.0.0.1"),
        api_port=_int_env_or_config(("CONTROLMIND_API_PORT", "CONTROLSCI_API_PORT"), config, "api.port", 17001),
        mineru_base_url=_env_or_config(("CONTROLMIND_MINERU_URL", "CONTROLSCI_MINERU_URL"), config, "mineru.url", "http://localhost:8000").rstrip("/"),
        mineru_official_base_url=_env_or_config(("MINERU_OFFICIAL_BASE_URL",), config, "mineru.official_url", "https://mineru.net").rstrip("/"),
        mineru_official_token=_env_or_config(("MINERU_API_TOKEN", "MINERU_OFFICIAL_TOKEN"), config, "mineru.official_token", ""),
        ollama_base_url=_env_or_config(("CONTROLMIND_OLLAMA_URL", "CONTROLSCI_OLLAMA_URL"), config, "ollama.url", "http://localhost:11434").rstrip("/"),
        upload_max_mb=_int_env_or_config(("CONTROLMIND_UPLOAD_MAX_MB", "CONTROLSCI_UPLOAD_MAX_MB"), config, "upload.max_mb", 20),
        cloud_demo_profile=_env_or_config(("CONTROLMIND_PROFILE", "PROFILE"), config, "profile", "cloud_demo"),
        cloud_daily_limit=_int_env_or_config(("CONTROLMIND_DAILY_API_LIMIT", "DEMO_DAILY_API_LIMIT"), config, "daily_api_limit", 100),
        demo_access_code=_env_or_config(("CONTROLMIND_DEMO_ACCESS_CODE", "DEMO_ACCESS_CODE"), config, "demo.access_code", ""),
        python_path=_env_or_config(("CONTROLMIND_PYTHON", "CONTROLSCI_PYTHON"), config, "python.path", ""),
    )
