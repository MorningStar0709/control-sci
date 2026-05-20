import os

import httpx


def resolve_api_key(base_url, explicit_key=None, fallback_key=None):
    if explicit_key:
        return explicit_key
    base = str(base_url or "").lower()
    if "localhost" in base or "127.0.0.1" in base:
        return "ollama"
    if "minimaxi.com" in base and "/anthropic" in base:
        return os.environ.get("MINIMAX_API_KEY") or fallback_key
    if "xiaomimimo.com" in base:
        return os.environ.get("MIMO_API_KEY") or fallback_key
    if "deepseek.com" in base:
        return fallback_key or os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY")
    return fallback_key or os.environ.get("OPENAI_API_KEY")


class OllamaMessage:
    def __init__(self, content):
        self.content = content


class OllamaChoice:
    def __init__(self, content):
        self.message = OllamaMessage(content)


class OllamaCompletionsResult:
    def __init__(self, choices):
        self.choices = choices


class OllamaClient:
    def __init__(self, base_url):
        base = str(base_url).rstrip("/")
        if base.endswith("/v1"):
            base = base[:-3]
        self._api_url = f"{base}/api/chat"
        self._completions = _OllamaCompletions(self._api_url)
        self._chat = _OllamaChat(self._completions)

    @property
    def chat(self):
        return self._chat


class _OllamaCompletions:
    def __init__(self, api_url):
        self._api_url = api_url

    def create(self, *, model, messages, temperature=0, max_tokens=2000, **kwargs):
        resp = httpx.post(
            self._api_url,
            json={
                "model": model,
                "messages": messages,
                "stream": False,
                "think": False,
                "options": {
                    "temperature": temperature,
                    "num_predict": max_tokens,
                },
            },
            timeout=600,
        )
        resp.raise_for_status()
        data = resp.json()
        content = (data.get("message") or {}).get("content", "")
        return OllamaCompletionsResult([OllamaChoice(content)])


class _OllamaChat:
    def __init__(self, completions):
        self.completions = completions


def create_client(api_key=None, base_url="https://api.deepseek.com", model="deepseek-v4-flash"):
    if base_url is None or str(base_url).strip() == "":
        raise ValueError(
            "base_url is required. Provide a localhost URL for Ollama, "
            "a MiniMax Anthropic endpoint, or an OpenAI-compatible endpoint."
        )
    base_lower = str(base_url).lower()

    if "localhost" in base_lower or "127.0.0.1" in base_lower:
        return OllamaClient(base_url), model, "ollama"

    if "minimaxi.com" in base_lower and "/anthropic" in base_lower:
        from anthropic import Anthropic

        if api_key is None:
            api_key = os.environ.get("MINIMAX_API_KEY", "")
        if not api_key:
            raise ValueError("Anthropic API key required. Set MINIMAX_API_KEY env var or pass --target-api-key.")
        client = Anthropic(api_key=api_key, base_url=base_url, timeout=120, http_client=httpx.Client(proxy=None, trust_env=False))
        return client, model, "anthropic"

    from openai import OpenAI, DefaultHttpxClient

    if api_key is None:
        api_key = resolve_api_key(base_url)
    if not api_key:
        raise ValueError("API key is required. Set via --api-key or provider env var (DEEPSEEK_API_KEY/OPENAI_API_KEY for DeepSeek).")
    client = OpenAI(api_key=api_key, base_url=base_url, timeout=120, max_retries=0, http_client=DefaultHttpxClient(proxy=None))
    return client, model, "openai"
