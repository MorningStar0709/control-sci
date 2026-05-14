"""四路径资源调度器 — GPU/API/Ollama/MinerU 资源感知 + 自动降级

架构：
  Layer 2: Resource Scheduler
  ├─ 四路径决策 (优先级: 可复现性 > 隐私 > 成本)
  │  ├─ api → DeepSeek v4-flash API
  │  ├─ mimo_vision → MiMo-V2.5 原生视觉 (raw httpx, 单模型零拼接)
  │  ├─ ollama → Ollama qwen3.5:9b 本地 (native /api/chat)
  │  └─ mineru → MinerU 本地 API
  ├─ HealthCheck — 每 provider 独立探活，零密钥泄露
  ├─ ClientFactory — 每 provider 独立客户端实例（规则 10.1.2）
  ├─ ProviderParameterMap — 从 agent_capabilities.json 加载（规则 10.1.5）
  └─ Scheduler — resolve → schedule → execute → fallback 闭环

环境变量：
  OPENAI_API_KEY / DEEPSEEK_API_KEY — DeepSeek API
  MIMO_API_KEY — MiMo API（视觉 + 文本共享）
  MINIMAX_API_KEY — MiniMax Anthropic API
  OLLAMA_HOST — Ollama 地址（默认 http://localhost:11434）
  MINERU_API_BASE — MinerU API 地址

安全红线：
  - HealthCheck 不暴露 GPU 显存原始数据
  - 所有 Key 从 os.environ 读取，零硬编码
  - 日志不包含 API Key / 本地路径 / 个人邮箱
"""

import json
import logging
import os
import subprocess
import sys
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import httpx

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CAPABILITIES_PATH = Path(__file__).resolve().parent / "agent_capabilities.json"

logger = logging.getLogger("ResourceScheduler")

HEALTH_TTL_SECONDS = 30

PROVIDER_TO_HEALTH_KEY = {
    "deepseek": "deepseek",
    "mimo": "mimo_vision",
    "minimax": "minimax",
    "ollama": "ollama_chat",
    "mineru": "mineru",
}


# Provider → fallback provider 列表（与 ProviderParameterMap._fallback_order 互补：
# 前者按 provider 维度，后者按 resource_type 维度，key space 不同，各自服务不同调用方）
PROVIDER_FALLBACK = {
    "deepseek": ["script"],
    "mimo": ["script"],
    "minimax": ["script"],
    "ollama": ["script"],
    "mineru": ["script"],
}

LOCAL_ONLY_INTENTS = {
    "mineru_parse",
    "corpus_parse",
    "multi_format_parse",
    "medical_rag",
    "local_finetune",
}

PUBLIC_OR_SANITIZED_INTENTS = {
    "arxiv_search",
    "cross_modal_audit",
    "corpus_quality_report",
    "benchmark_build",
    "quality_arbitrate",
    "model_evaluate",
    "multi_judge_compare",
    "leaderboard_viz",
    "reproduce_all",
}

AUTO_PROVIDER_MAPPING = {
    "arxiv_search": ("script", "script"),
    "mineru_parse": ("mineru", "chat"),
    "corpus_parse": ("mineru", "chat"),
    "cross_modal_audit": ("mimo", "vision"),
    "corpus_quality_report": ("deepseek", "chat"),
    "benchmark_build": ("deepseek", "chat"),
    "quality_arbitrate": ("deepseek", "chat"),
    "model_evaluate": ("deepseek", "chat"),
    "multi_judge_compare": ("deepseek", "chat"),
    "leaderboard_viz": ("script", "chat"),
    "local_finetune": ("ollama", "chat"),
    "multi_format_parse": ("mineru", "chat"),
    "medical_rag": ("ollama", "chat"),
    "reproduce_all": ("script", "chat"),
}

LOCAL_PROVIDER_MAPPING = {
    "arxiv_search": ("script", "script"),
    "mineru_parse": ("mineru", "chat"),
    "corpus_parse": ("mineru", "chat"),
    "cross_modal_audit": ("ollama", "chat"),
    "corpus_quality_report": ("ollama", "chat"),
    "benchmark_build": ("ollama", "chat"),
    "quality_arbitrate": ("ollama", "chat"),
    "model_evaluate": ("ollama", "chat"),
    "multi_judge_compare": ("ollama", "chat"),
    "leaderboard_viz": ("script", "chat"),
    "local_finetune": ("ollama", "chat"),
    "multi_format_parse": ("mineru", "chat"),
    "medical_rag": ("ollama", "chat"),
    "reproduce_all": ("script", "chat"),
}


class ResourceType(str, Enum):
    API = "api"
    LOCAL_API = "local_api"
    LOCAL_GPU = "local_gpu"
    SCRIPT = "script"


class ProviderStatus(str, Enum):
    AVAILABLE = "available"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"


@dataclass
class ProviderHealth:
    provider: str
    status: ProviderStatus
    latency_ms: int = 0
    detail: str = ""


@dataclass
class ResourceStatus:
    providers: Dict[str, ProviderHealth] = field(default_factory=dict)
    available_providers: List[str] = field(default_factory=list)
    degraded_providers: List[str] = field(default_factory=list)
    unavailable_providers: List[str] = field(default_factory=list)
    checked_at: str = ""

    @property
    def summary(self) -> str:
        lines = [f"ResourceStatus @ {self.checked_at}"]
        for name, h in self.providers.items():
            emoji = {"available": "✅", "degraded": "🟡",
                     "unavailable": "❌", "unknown": "❓"}.get(h.status, "❓")
            lines.append(f"  {emoji} {name:<18s} {h.status:<12s} {h.detail}")
        return "\n".join(lines)

    def is_available(self, provider: str) -> bool:
        h = self.providers.get(provider)
        return h is not None and h.status in (ProviderStatus.AVAILABLE, ProviderStatus.DEGRADED)


@dataclass
class ResolvedProvider:
    provider: str
    sub_type: str
    model: str
    base_url: str
    api_key_env: str
    client_type: str
    temperature: float
    max_tokens: int
    timeout: int = 120
    extra_config: dict = field(default_factory=dict)


class ProviderParameterMap:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._loaded = False
        return cls._instance

    def __init__(self):
        if self._loaded:
            return
        self._loaded = True
        self._raw = {}
        self._intent_map: Dict[str, dict] = {}
        self._provider_map: Dict[str, Dict[str, dict]] = {}
        self._fallback_order: Dict[str, list] = {}
        self._resource_types: Dict[str, dict] = {}
        self._load()

    def _load(self):
        if not CAPABILITIES_PATH.exists():
            logger.warning("agent_capabilities.json not found at %s, using built-in defaults", CAPABILITIES_PATH)
            self._load_defaults()
            return
        with open(CAPABILITIES_PATH, "r", encoding="utf-8") as f:
            self._raw = json.load(f)
        for intent in self._raw.get("intents", []):
            self._intent_map[intent["intent_id"]] = intent
        sched = self._raw.get("resource_scheduler_config", {})
        self._provider_map = sched.get("provider_parameter_map", {})
        self._fallback_order = sched.get("fallback_order", {})
        self._resource_types = sched.get("resource_types", {})

    def _load_defaults(self):
        self._provider_map = {
            "deepseek": {
                "chat": {
                    "model": "deepseek-v4-flash",
                    "base_url": "https://api.deepseek.com",
                    "default_temperature": 0.1,
                    "default_max_tokens": 4096,
                    "client_type": "openai",
                    "proxy_required": False,
                }
            },
            "mimo": {
                "vision": {
                    "model": "mimo-v2.5",
                    "base_url": "https://api.xiaomimimo.com/v1",
                    "default_temperature": 1.0,
                    "default_max_tokens": 4096,
                    "client_type": "raw_httpx",
                    "auth_type": "api-key header",
                },
                "text": {
                    "model": "mimo-v2-flash",
                    "base_url": "https://api.xiaomimimo.com/v1",
                    "default_temperature": 0.7,
                    "default_max_tokens": 4096,
                    "client_type": "openai",
                    "proxy_required": False,
                },
            },
            "minimax": {
                "chat": {
                    "model": "minimax-2.5",
                    "base_url": "https://api.minimaxi.com/anthropic",
                    "client_type": "anthropic",
                    "default_temperature": 0.7,
                    "default_max_tokens": 4096,
                    "proxy_required": False,
                }
            },
            "ollama": {
                "chat": {
                    "model": "qwen3.5:9b",
                    "base_url": "http://localhost:11434",
                    "api_path": "/api/chat",
                    "default_temperature": 0.1,
                    "default_max_tokens": 4096,
                    "client_type": "raw_httpx",
                },
                "completions": {
                    "model": "qwen3.5:9b",
                    "base_url": "http://localhost:11434",
                    "api_path": "/v1/chat/completions",
                    "default_temperature": 0.1,
                    "default_max_tokens": 4096,
                    "client_type": "openai",
                },
            },
        }
        self._fallback_order = {
            "api": ["script"],
            "local_api": ["script"],
            "local_gpu": ["script"],
            "script": [],
        }
        self._resource_types = {
            "api": {"description": "外部 API 调用", "default_timeout": 120},
            "local_api": {"description": "本地 API 服务", "default_timeout": 300},
            "local_gpu": {"description": "本地 GPU 任务", "default_timeout": 3600},
            "script": {"description": "纯本地脚本", "default_timeout": 600},
        }

    def get_intent(self, intent_id: str) -> Optional[dict]:
        return self._intent_map.get(intent_id)

    def get_provider_config(self, provider: str, sub_type: str = "chat") -> Optional[dict]:
        return self._provider_map.get(provider, {}).get(sub_type)

    def get_fallback_types(self, resource_type: str) -> List[str]:
        return self._fallback_order.get(resource_type, [])

    def get_resource_timeout(self, resource_type: str) -> int:
        return self._resource_types.get(resource_type, {}).get("default_timeout", 120)

    def list_providers(self) -> List[str]:
        return list(self._provider_map.keys())

    def list_sub_types(self, provider: str) -> List[str]:
        return list(self._provider_map.get(provider, {}).keys())


class HealthCheck:
    TIMEOUT = 5

    @staticmethod
    def check_all() -> ResourceStatus:
        status = ResourceStatus()
        checks = [
            ("deepseek", HealthCheck._check_deepseek),
            ("mimo_vision", HealthCheck._check_mimo_vision),
            ("mimo_text", HealthCheck._check_mimo_text),
            ("minimax", HealthCheck._check_minimax),
            ("ollama_chat", HealthCheck._check_ollama_chat),
            ("ollama_compat", HealthCheck._check_ollama_compat),
            ("mineru", HealthCheck._check_mineru),
            ("gpu", HealthCheck._check_gpu),
        ]
        for name, fn in checks:
            h = fn()
            status.providers[name] = h
        status.available_providers = [n for n, h in status.providers.items()
                                       if h.status == ProviderStatus.AVAILABLE]
        status.degraded_providers = [n for n, h in status.providers.items()
                                      if h.status == ProviderStatus.DEGRADED]
        status.unavailable_providers = [n for n, h in status.providers.items()
                                         if h.status == ProviderStatus.UNAVAILABLE]
        status.checked_at = time.strftime("%Y-%m-%dT%H:%M:%S")
        return status

    @staticmethod
    def _check_deepseek() -> ProviderHealth:
        api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY", "")
        if not api_key:
            return ProviderHealth("deepseek", ProviderStatus.UNAVAILABLE, detail="API Key 未设置")
        t0 = time.time()
        try:
            resp = httpx.get("https://api.deepseek.com/v1/models",
                             headers={"Authorization": f"Bearer {api_key}"},
                             timeout=HealthCheck.TIMEOUT)
            latency = int((time.time() - t0) * 1000)
            if resp.status_code == 200:
                return ProviderHealth("deepseek", ProviderStatus.AVAILABLE, latency, "连通正常")
            if resp.status_code == 401:
                return ProviderHealth("deepseek", ProviderStatus.UNAVAILABLE, latency, "API Key 无效 (401)")
            return ProviderHealth("deepseek", ProviderStatus.DEGRADED, latency,
                                  f"HTTP {resp.status_code}")
        except Exception as e:
            latency = int((time.time() - t0) * 1000)
            return ProviderHealth("deepseek", ProviderStatus.UNAVAILABLE, latency, str(e)[:100])

    @staticmethod
    def _check_mimo_vision() -> ProviderHealth:
        api_key = os.environ.get("MIMO_API_KEY", "")
        if not api_key:
            return ProviderHealth("mimo_vision", ProviderStatus.UNAVAILABLE, detail="MIMO_API_KEY 未设置")
        t0 = time.time()
        try:
            payload = {
                "model": "mimo-v2.5",
                "messages": [{"role": "user", "content": "ping"}],
                "max_tokens": 1,
                "thinking": {"type": "disabled"},
            }
            headers = {"api-key": api_key, "Content-Type": "application/json"}
            resp = httpx.post("https://api.xiaomimimo.com/v1/chat/completions",
                              json=payload, headers=headers, timeout=HealthCheck.TIMEOUT)
            latency = int((time.time() - t0) * 1000)
            if resp.status_code in (200, 400):
                return ProviderHealth("mimo_vision", ProviderStatus.AVAILABLE, latency, "连通正常")
            return ProviderHealth("mimo_vision", ProviderStatus.DEGRADED, latency,
                                  f"HTTP {resp.status_code}")
        except Exception as e:
            latency = int((time.time() - t0) * 1000)
            return ProviderHealth("mimo_vision", ProviderStatus.UNAVAILABLE, latency, str(e)[:100])

    @staticmethod
    def _check_mimo_text() -> ProviderHealth:
        api_key = os.environ.get("MIMO_API_KEY", "")
        if not api_key:
            return ProviderHealth("mimo_text", ProviderStatus.UNAVAILABLE, detail="MIMO_API_KEY 未设置")
        t0 = time.time()
        try:
            payload = {
                "model": "mimo-v2-flash",
                "messages": [{"role": "user", "content": "ping"}],
                "max_tokens": 1,
            }
            headers = {"api-key": api_key, "Content-Type": "application/json"}
            resp = httpx.post("https://api.xiaomimimo.com/v1/chat/completions",
                              json=payload, headers=headers, timeout=HealthCheck.TIMEOUT)
            latency = int((time.time() - t0) * 1000)
            if resp.status_code in (200, 400):
                return ProviderHealth("mimo_text", ProviderStatus.AVAILABLE, latency, "文本 API 连通正常")
            return ProviderHealth("mimo_text", ProviderStatus.DEGRADED, latency,
                                  f"HTTP {resp.status_code}")
        except Exception as e:
            latency = int((time.time() - t0) * 1000)
            return ProviderHealth("mimo_text", ProviderStatus.UNAVAILABLE, latency, str(e)[:100])

    @staticmethod
    def _check_minimax() -> ProviderHealth:
        api_key = os.environ.get("MINIMAX_API_KEY", "")
        if not api_key:
            return ProviderHealth("minimax", ProviderStatus.UNAVAILABLE, detail="MINIMAX_API_KEY 未设置")
        t0 = time.time()
        try:
            resp = httpx.get("https://api.minimaxi.com/anthropic/v1/messages",
                             headers={"x-api-key": api_key},
                             timeout=HealthCheck.TIMEOUT)
            latency = int((time.time() - t0) * 1000)
            if resp.status_code in (200, 400, 405):
                return ProviderHealth("minimax", ProviderStatus.AVAILABLE, latency, "连通正常")
            return ProviderHealth("minimax", ProviderStatus.DEGRADED, latency,
                                  f"HTTP {resp.status_code}")
        except Exception as e:
            latency = int((time.time() - t0) * 1000)
            return ProviderHealth("minimax", ProviderStatus.UNAVAILABLE, latency, str(e)[:100])

    @staticmethod
    def _check_ollama_chat() -> ProviderHealth:
        base = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        t0 = time.time()
        try:
            resp = httpx.get(f"{base}/api/tags", timeout=HealthCheck.TIMEOUT)
            latency = int((time.time() - t0) * 1000)
            if resp.status_code == 200:
                data = resp.json()
                models = [m.get("name", "") for m in data.get("models", [])]
                model_list = ", ".join(models[:5]) if models else "无模型"
                return ProviderHealth("ollama_chat", ProviderStatus.AVAILABLE, latency,
                                      f"模型: {model_list}")
            return ProviderHealth("ollama_chat", ProviderStatus.DEGRADED, latency,
                                  f"HTTP {resp.status_code}")
        except Exception as e:
            latency = int((time.time() - t0) * 1000)
            return ProviderHealth("ollama_chat", ProviderStatus.UNAVAILABLE, latency, str(e)[:100])

    @staticmethod
    def _check_ollama_compat() -> ProviderHealth:
        base = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        t0 = time.time()
        try:
            resp = httpx.get(f"{base}/v1/models", timeout=HealthCheck.TIMEOUT)
            latency = int((time.time() - t0) * 1000)
            if resp.status_code == 200:
                return ProviderHealth("ollama_compat", ProviderStatus.AVAILABLE, latency,
                                      "OpenAI-compatible 口可用")
            return ProviderHealth("ollama_compat", ProviderStatus.DEGRADED, latency,
                                  f"HTTP {resp.status_code}")
        except Exception as e:
            latency = int((time.time() - t0) * 1000)
            return ProviderHealth("ollama_compat", ProviderStatus.UNAVAILABLE, latency, str(e)[:100])

    @staticmethod
    def _check_mineru() -> ProviderHealth:
        base = os.environ.get("MINERU_API_BASE", "")
        if not base:
            return ProviderHealth("mineru", ProviderStatus.UNAVAILABLE, detail="MINERU_API_BASE 未设置")
        t0 = time.time()
        try:
            resp = httpx.get(f"{base}/health", timeout=HealthCheck.TIMEOUT)
            latency = int((time.time() - t0) * 1000)
            if resp.status_code == 200:
                return ProviderHealth("mineru", ProviderStatus.AVAILABLE, latency, "服务健康")
            return ProviderHealth("mineru", ProviderStatus.DEGRADED, latency, f"HTTP {resp.status_code}")
        except Exception as e:
            latency = int((time.time() - t0) * 1000)
            return ProviderHealth("mineru", ProviderStatus.UNAVAILABLE, latency, str(e)[:100])

    @staticmethod
    def _check_gpu() -> ProviderHealth:
        try:
            result = subprocess.run(
                ["nvidia-smi", "--query-gpu=name,driver_version", "--format=csv,noheader"],
                capture_output=True, text=True, timeout=10,
            )
            if result.returncode == 0:
                gpu_count = len([l for l in result.stdout.strip().split("\n") if l.strip()])
                return ProviderHealth("gpu", ProviderStatus.AVAILABLE, 0,
                                      f"{gpu_count} 个 GPU 可用")
            return ProviderHealth("gpu", ProviderStatus.UNAVAILABLE, detail="nvidia-smi 返回非零")
        except FileNotFoundError:
            return ProviderHealth("gpu", ProviderStatus.UNAVAILABLE, detail="nvidia-smi 未找到")
        except subprocess.TimeoutExpired:
            return ProviderHealth("gpu", ProviderStatus.UNAVAILABLE, detail="nvidia-smi 查询超时（GPU 驱动可能无响应）")
        except Exception as e:
            return ProviderHealth("gpu", ProviderStatus.UNAVAILABLE, detail=str(e)[:100])


class ClientFactory:
    """为每个 Provider 创建独立客户端实例（规则 10.1.2：四路径各自独立，不可共享）。"""

    @staticmethod
    def create_deepseek() -> Tuple:
        from openai import OpenAI, DefaultHttpxClient
        api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY", "")
        if not api_key:
            raise ValueError("OPENAI_API_KEY 或 DEEPSEEK_API_KEY 未设置")
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",
            timeout=120,
            max_retries=0,
            http_client=DefaultHttpxClient(proxy=None),
        )
        return client, "deepseek-v4-flash"

    @staticmethod
    def create_deepseek_custom(model: str = None, timeout: int = 120) -> Tuple:
        from openai import OpenAI, DefaultHttpxClient
        api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY", "")
        if not api_key:
            raise ValueError("OPENAI_API_KEY 或 DEEPSEEK_API_KEY 未设置")
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",
            timeout=timeout,
            max_retries=0,
            http_client=DefaultHttpxClient(proxy=None),
        )
        return client, model or "deepseek-v4-flash"

    @staticmethod
    def create_mimo_vision() -> Tuple:
        api_key = os.environ.get("MIMO_API_KEY", "")
        if not api_key:
            raise ValueError("MIMO_API_KEY 未设置")
        return None, "mimo-v2.5"

    @staticmethod
    def create_mimo_text(model: str = None, timeout: int = 120) -> Tuple:
        from openai import OpenAI, DefaultHttpxClient
        api_key = os.environ.get("MIMO_API_KEY", "")
        if not api_key:
            raise ValueError("MIMO_API_KEY 未设置")
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.xiaomimimo.com/v1",
            timeout=timeout,
            max_retries=0,
            http_client=DefaultHttpxClient(proxy=None),
        )
        return client, model or "mimo-v2-flash"

    @staticmethod
    def create_minimax(timeout: int = 120) -> Tuple:
        from anthropic import Anthropic
        api_key = os.environ.get("MINIMAX_API_KEY", "")
        if not api_key:
            raise ValueError("MINIMAX_API_KEY 未设置")
        client = Anthropic(
            api_key=api_key,
            base_url="https://api.minimaxi.com/anthropic",
            timeout=timeout,
            http_client=httpx.Client(proxy=None),
        )
        return client, "MiniMax-M2.5-highspeed"

    @staticmethod
    def create_ollama_native() -> Tuple:
        return None, "qwen3.5:9b"

    @staticmethod
    def create_ollama_openai(timeout: int = 120) -> Tuple:
        from openai import OpenAI, DefaultHttpxClient
        base = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        client = OpenAI(
            api_key="ollama",
            base_url=f"{base}/v1",
            timeout=timeout,
            max_retries=0,
            http_client=DefaultHttpxClient(proxy=None),
        )
        return client, "qwen3.5:9b"

    @staticmethod
    def create_mineru(timeout: int = 300) -> httpx.Client:
        return httpx.Client(timeout=timeout, proxy=None)


class ResourceScheduler:
    """四路径资源调度器 — 决策优先级：隐私边界 > 可复现性 > 成本。

    数据边界原则:
      - local_only: 原文、医疗、微调数据、本地解析中间产物不出本机。
      - public_or_sanitized: 公开论文、脱敏统计、评测题与排行榜可使用云端 API 增强。
      - local_mode=True: 全部可替代任务优先走 Ollama/MinerU/本地脚本。

    Usage:
        scheduler = ResourceScheduler()
        status = scheduler.health_check()
        print(status.summary)

        resolved = scheduler.resolve("corpus_quality_report", local_mode=False)
        # → ResolvedProvider(provider="deepseek", model="deepseek-v4-flash", ...)

        resolved_local = scheduler.resolve("corpus_quality_report", local_mode=True)
        # → ResolvedProvider(provider="ollama", model="qwen3.5:9b", ...)
    """

    def __init__(self, local_mode: bool = False):
        self.local_mode = local_mode
        self._ppm = ProviderParameterMap()
        self._resource_status: Optional[ResourceStatus] = None
        self._health_checked_at: float = 0.0

    def health_check(self, force: bool = False) -> ResourceStatus:
        now = time.time()
        if not force and self._resource_status is not None and (now - self._health_checked_at) < HEALTH_TTL_SECONDS:
            return self._resource_status
        self._resource_status = HealthCheck.check_all()
        self._health_checked_at = now
        return self._resource_status

    @staticmethod
    def _infer_sub_type(provider: str, intent_id: str = None) -> str:
        if provider == "mimo":
            return "vision" if intent_id == "cross_modal_audit" else "text"
        return "chat"

    @staticmethod
    def _data_policy(intent_id: str) -> dict:
        if intent_id in LOCAL_ONLY_INTENTS:
            return {
                "boundary": "local_only",
                "cloud_allowed": False,
                "reason": "raw_or_sensitive_artifacts_remain_local",
            }
        if intent_id in PUBLIC_OR_SANITIZED_INTENTS:
            return {
                "boundary": "public_or_sanitized",
                "cloud_allowed": True,
                "reason": "public_inputs_or_sanitized_derivatives_only",
            }
        return {
            "boundary": "review_required",
            "cloud_allowed": False,
            "reason": "unknown_intent_defaults_to_local_review",
        }

    def resolve(self, intent_id: str, local_mode: bool = None,
                force_provider: str = None) -> ResolvedProvider:
        """根据 intent_id 解析最佳 Provider 及参数。

        Args:
            intent_id: 意图标识（如 corpus_quality_report, cross_modal_audit）
            local_mode: 是否强制本地模式。None 时使用实例默认值。
            force_provider: 强制使用指定 provider，跳过自动选择。

        Returns:
            ResolvedProvider: 解析后的 Provider 配置
        """
        if local_mode is None:
            local_mode = self.local_mode

        intent = self._ppm.get_intent(intent_id)
        if intent is None:
            raise KeyError(f"Unknown intent_id: {intent_id}")

        provider_defaults = intent.get("provider_defaults", {})

        if force_provider:
            sub_type = self._infer_sub_type(force_provider, intent_id)
            return self._build_resolved(force_provider, sub_type, intent, provider_defaults)

        data_policy = self._data_policy(intent_id)
        if local_mode or not data_policy["cloud_allowed"]:
            return self._resolve_local(intent_id, intent, provider_defaults)

        return self._resolve_auto(intent_id, intent, provider_defaults)

    def _resolve_auto(self, intent_id, intent, provider_defaults):
        provider, sub_type = AUTO_PROVIDER_MAPPING.get(intent_id, ("deepseek", "chat"))
        return self._build_resolved(provider, sub_type, intent, provider_defaults)

    def _resolve_local(self, intent_id, intent, provider_defaults):
        provider, sub_type = LOCAL_PROVIDER_MAPPING.get(intent_id, ("ollama", "chat"))
        return self._build_resolved(provider, sub_type, intent, provider_defaults)

    def _build_resolved(self, provider, sub_type, intent, provider_defaults):
        if provider == "script":
            return ResolvedProvider(
                provider="script", sub_type="script", model="local_script",
                base_url="", api_key_env="", client_type="subprocess",
                temperature=0, max_tokens=0, timeout=600,
                extra_config={"data_policy": self._data_policy(intent.get("intent_id", ""))},
            )

        if provider == "mineru":
            base = os.environ.get("MINERU_API_BASE", "http://127.0.0.1:8000")
            timeout = self._ppm.get_resource_timeout("local_api")
            return ResolvedProvider(
                provider="mineru", sub_type="chat", model="mineru",
                base_url=base, api_key_env="", client_type="raw_httpx",
                temperature=0, max_tokens=0, timeout=timeout,
                extra_config={"data_policy": self._data_policy(intent.get("intent_id", ""))},
            )

        config = self._ppm.get_provider_config(provider, sub_type)
        if config is None:
            config = self._ppm.get_provider_config(provider, "chat") or {}

        model = config.get("model", "")
        base_url = config.get("base_url", "")
        client_type = config.get("client_type", "openai")
        pd_temp = provider_defaults.get("temperature")
        temperature = pd_temp if pd_temp is not None else config.get("default_temperature", 0.1)
        pd_tok = provider_defaults.get("max_tokens")
        max_tokens = pd_tok if pd_tok is not None else config.get("default_max_tokens", 4096)
        timeout = self._ppm.get_resource_timeout(intent.get("resource_type", "api"))

        api_key_env_map = {
            "deepseek": "OPENAI_API_KEY",
            "mimo": "MIMO_API_KEY",
            "minimax": "MINIMAX_API_KEY",
            "ollama": "OLLAMA_HOST",  # Ollama 不需要 API key，OLLAMA_HOST 是服务地址
        }
        api_key_env = api_key_env_map.get(provider, "")

        extra_config = {}
        if client_type == "raw_httpx" and "auth_type" in config:
            extra_config["auth_type"] = config["auth_type"]
        if "api_path" in config:
            extra_config["api_path"] = config["api_path"]
        extra_config["data_policy"] = self._data_policy(intent.get("intent_id", ""))

        return ResolvedProvider(
            provider=provider,
            sub_type=sub_type,
            model=model,
            base_url=base_url,
            api_key_env=api_key_env,
            client_type=client_type,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
            extra_config=extra_config,
        )

    def get_fallback(self, resolved: ResolvedProvider) -> Optional[ResolvedProvider]:
        fallback_list = PROVIDER_FALLBACK.get(resolved.provider, ["script"])
        if not fallback_list:
            return None
        status = self.health_check()
        for fb_provider in fallback_list:
            if fb_provider == "script":
                return ResolvedProvider(
                    provider="script", sub_type="script", model="local_script",
                    base_url="", api_key_env="", client_type="subprocess",
                    temperature=0, max_tokens=0, timeout=600,
                )
            health_key = PROVIDER_TO_HEALTH_KEY.get(fb_provider)
            if health_key and status.is_available(health_key):
                return self._build_resolved(fb_provider, "chat", {}, {})
        return None

    def get_timeout(self, intent_id: str) -> int:
        intent = self._ppm.get_intent(intent_id)
        if intent is None:
            return 120
        return self._ppm.get_resource_timeout(intent.get("resource_type", "api"))

    def list_available_providers(self) -> List[str]:
        status = self.health_check()
        return [p for p, h in status.providers.items()
                if h.status in (ProviderStatus.AVAILABLE, ProviderStatus.DEGRADED)]

    def is_ready(self, intent_id: str, local_mode: bool = None) -> Tuple[bool, str]:
        """检查指定 intent 的 Provider 是否就绪。

        Returns:
            (ready, message): 是否就绪及原因描述
        """
        try:
            resolved = self.resolve(intent_id, local_mode=local_mode)
        except Exception as e:
            return False, f"解析失败: {e}"

        if resolved.provider == "script":
            return True, "本地脚本无需外部依赖"

        status = self.health_check()
        health_key = PROVIDER_TO_HEALTH_KEY.get(resolved.provider)
        if health_key is None:
            h = status.providers.get(resolved.provider)
        else:
            h = status.providers.get(health_key)
        display_key = health_key or resolved.provider
        if h is None:
            return False, f"Provider {display_key} 不在健康检查列表中"
        if h.status == ProviderStatus.AVAILABLE:
            return True, f"{display_key} 就绪: {h.detail}"
        if h.status == ProviderStatus.DEGRADED:
            return True, f"{display_key} 降级可用: {h.detail}"
        return False, f"{display_key} 不可用: {h.detail}"


_global_scheduler: Optional[ResourceScheduler] = None
_global_scheduler_local_mode: Optional[bool] = None


def get_global_scheduler(local_mode: bool = False) -> ResourceScheduler:
    global _global_scheduler, _global_scheduler_local_mode
    if _global_scheduler is not None and _global_scheduler_local_mode == local_mode:
        return _global_scheduler
    _global_scheduler = ResourceScheduler(local_mode=local_mode)
    _global_scheduler_local_mode = local_mode
    return _global_scheduler
