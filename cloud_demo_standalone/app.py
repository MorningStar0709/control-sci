from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from contextlib import contextmanager
import ipaddress
import json
import os
import re
import socket
import tempfile
import threading
import time
import zipfile
from io import BytesIO
from typing import Any
from urllib.parse import unquote, urlparse

import httpx
from fastapi import FastAPI, File, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT / "static"
DATA_DIR = ROOT / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
QUOTA_PATH = DATA_DIR / "quota.json"
QUOTA_LOCK_PATH = DATA_DIR / "quota.lock"
_quota_thread_lock = threading.Lock()
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


def format_extensions(extensions: set[str]) -> str:
    return "/".join(ext.lstrip(".").upper() for ext in sorted(extensions))


def is_supported_official_url(raw_url: str) -> bool:
    parsed = urlparse(raw_url or "")
    suffix = Path(unquote(parsed.path or "")).suffix.lower()
    if suffix in OFFICIAL_URL_EXTENSIONS:
        return True
    query = unquote(parsed.query or "").lower()
    return any(ext in query for ext in OFFICIAL_URL_EXTENSIONS)


def env_int(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, str(default)))
    except ValueError:
        return default


def settings() -> dict[str, Any]:
    demo_access_code = os.environ.get("DEMO_ACCESS_CODE", "").strip()
    return {
        "host": os.environ.get("CLOUD_DEMO_HOST", "127.0.0.1"),
        "port": env_int("CLOUD_DEMO_PORT", 18080),
        "daily_limit": env_int("DEMO_DAILY_LIMIT", 100),
        "upload_max_mb": env_int("DEMO_UPLOAD_MAX_MB", 20),
        "demo_access_code": demo_access_code,
        "require_access_code": env_bool("DEMO_REQUIRE_ACCESS_CODE", True),
        "allow_dry_run_without_code": env_bool("DEMO_ALLOW_DRY_RUN_WITHOUT_CODE", False),
        "mineru_token": os.environ.get("MINERU_API_TOKEN", os.environ.get("MINERU_OFFICIAL_TOKEN", "")).strip(),
        "mineru_base_url": os.environ.get("MINERU_OFFICIAL_BASE_URL", "https://mineru.net").rstrip("/"),
        "deepseek_key": os.environ.get("DEEPSEEK_API_KEY", os.environ.get("OPENAI_API_KEY", "")).strip(),
        "deepseek_base": os.environ.get("DEEPSEEK_API_BASE", "https://api.deepseek.com").rstrip("/"),
        "deepseek_model": os.environ.get("DEEPSEEK_MODEL", "deepseek-chat"),
    }


def env_bool(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@contextmanager
def quota_file_lock():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with _quota_thread_lock:
        lock_file = QUOTA_LOCK_PATH.open("a+")
        try:
            if os.name == "nt":
                yield
            else:
                import fcntl
                fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
                try:
                    yield
                finally:
                    fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
        finally:
            lock_file.close()


def write_quota_atomic(data: dict[str, Any]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix="quota.", suffix=".tmp", dir=str(DATA_DIR))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp_name, QUOTA_PATH)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def _read_quota_unlocked() -> dict[str, Any]:
    cfg = settings()
    today = date.today().isoformat()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if QUOTA_PATH.exists():
        try:
            data = json.loads(QUOTA_PATH.read_text(encoding="utf-8"))
        except Exception:
            data = {}
    else:
        data = {}
    if data.get("date") != today:
        data = {"date": today, "used": 0, "limit": cfg["daily_limit"]}
    data["limit"] = cfg["daily_limit"]
    data["remaining"] = max(0, int(data["limit"]) - int(data.get("used", 0)))
    return data


def read_quota() -> dict[str, Any]:
    with quota_file_lock():
        data = _read_quota_unlocked()
        write_quota_atomic(data)
        return data


def consume_quota(reason: str) -> dict[str, Any]:
    with quota_file_lock():
        data = _read_quota_unlocked()
        if data["remaining"] <= 0:
            raise HTTPException(status_code=429, detail={"error": "今日云端实时调用额度已用完", "quota": data})
        data["used"] = int(data.get("used", 0)) + 1
        data["last_reason"] = reason
        data["last_used_at"] = datetime.now().isoformat(timespec="seconds")
        data["remaining"] = max(0, int(data["limit"]) - int(data["used"]))
        write_quota_atomic(data)
        return data


def _is_public_ip(value: str) -> bool:
    try:
        ip = ipaddress.ip_address(value)
    except ValueError:
        return False
    return ip.is_global


def validate_public_extract_url(raw_url: str) -> str:
    url = (raw_url or "").strip()
    parsed = urlparse(url)
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.hostname:
        raise HTTPException(status_code=400, detail={"error": "只接受公开 http(s) 文档 URL"})

    if not is_supported_official_url(url):
        raise HTTPException(
            status_code=400,
            detail={"error": f"URL 必须指向 MinerU 官方 URL API 支持的文件格式：{format_extensions(OFFICIAL_URL_EXTENSIONS)}"},
        )

    host = parsed.hostname
    try:
        literal_ip = ipaddress.ip_address(host)
        if not literal_ip.is_global:
            raise HTTPException(status_code=400, detail={"error": "拒绝内网、回环或保留地址 URL"})
    except ValueError:
        try:
            infos = socket.getaddrinfo(host, None)
        except socket.gaierror:
            raise HTTPException(status_code=400, detail={"error": "URL 域名无法解析"})
        resolved_ips = {info[4][0] for info in infos}
        if not resolved_ips or not all(_is_public_ip(ip) for ip in resolved_ips):
            raise HTTPException(status_code=400, detail={"error": "拒绝解析到内网、回环或保留地址的 URL"})
    return url


def require_access(code: str | None, *, allow_unconfigured: bool = False) -> None:
    cfg = settings()
    expected = cfg["demo_access_code"]
    unconfigured_dry_run_allowed = allow_unconfigured and cfg["allow_dry_run_without_code"]
    if cfg["require_access_code"] and not expected and not allow_unconfigured:
        raise HTTPException(status_code=503, detail={"error": "DEMO_ACCESS_CODE 未配置，云端实时调用已锁定"})
    if cfg["require_access_code"] and not expected and allow_unconfigured and not unconfigured_dry_run_allowed:
        raise HTTPException(
            status_code=503,
            detail={"error": "DEMO_ACCESS_CODE 未配置；如需本地 dry-run 验证，请设置 DEMO_ALLOW_DRY_RUN_WITHOUT_CODE=1"},
        )
    if expected and (code or "").strip() != expected:
        raise HTTPException(status_code=403, detail={"error": "Demo access code required"})


def public_boundary() -> dict[str, Any]:
    return {
        "profile": "pure_cloud_demo",
        "allowed": ["public_document_url", "public_pdf_upload", "desensitized_question"],
        "supported_url_formats": format_extensions(OFFICIAL_URL_EXTENSIONS),
        "forbidden": [
            "patient_material",
            "private_enterprise_document",
            "confidential_document",
            "private_vector_index",
            "local_gpu_task",
            "frontend_api_key",
        ],
        "services": ["MinerU official API", "DeepSeek API"],
    }


class UrlParseRequest(BaseModel):
    url: str
    model_version: str = "vlm"
    access_code: str = ""


class AskRequest(BaseModel):
    question: str
    context: str = ""
    access_code: str = ""
    dry_run: bool = False


class QuizGenerateRequest(BaseModel):
    source_text: str
    topic: str = "主要终点、安全性来源与研究局限"
    count: int = 3
    access_code: str = ""
    dry_run: bool = False


class QuizGradeRequest(BaseModel):
    question: str
    expected_answer: str = ""
    rubric: str = ""
    student_answer: str
    source_text: str = ""
    access_code: str = ""
    dry_run: bool = False


class AgentPlanRequest(BaseModel):
    goal: str
    access_code: str = ""


class MedicalRagRequest(BaseModel):
    question: str
    access_code: str = ""
    dry_run: bool = False


app = FastAPI(title="ControlMind Pure Cloud Demo", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index() -> dict[str, Any]:
    return {
        "name": "ControlMind Pure Cloud Demo API",
        "ui": "Serve the Next.js workbench from cloud_demo_standalone/web or docker compose.",
        "health": "/api/health",
        "runtime": "/api/runtime",
    }


@app.get("/api/health")
def health() -> dict[str, Any]:
    cfg = settings()
    return {
        "status": "ready",
        "profile": "pure_cloud_demo",
        "runtime": "standalone",
        "components": {
            "mineru_official_api": {"available": bool(cfg["mineru_token"]), "base_url": cfg["mineru_base_url"]},
            "deepseek_api": {"available": bool(cfg["deepseek_key"]), "base_url": cfg["deepseek_base"], "model": cfg["deepseek_model"]},
            "quota": read_quota(),
            "web_workbench": {"available": True, "implementation": "nextjs_starboard_shell"},
        },
        "limits": {
            "upload_max_mb": cfg["upload_max_mb"],
            "daily_live_calls": cfg["daily_limit"],
            "access_code_required": bool(cfg["require_access_code"]),
        },
        "boundary": public_boundary(),
    }


@app.get("/api/runtime")
def runtime() -> dict[str, Any]:
    return {
        "mode": "pure_cloud_only",
        "profiles": [{"id": "pure_cloud_demo", "label": "公开云端 Demo"}],
        "parser_backends": [{"id": "mineru_official", "label": "MinerU 官方 API"}],
        "generation_backends": [{"id": "deepseek", "label": "DeepSeek API"}],
        "local_models": [],
        "local_indexes": [],
        "defaults": {
            "profile": "pure_cloud_demo",
            "parser_backend": "mineru_official",
            "generation_backend": "deepseek",
            "data_boundary": "public_or_desensitized_only",
        },
    }


@app.get("/api/quota")
def quota() -> dict[str, Any]:
    return read_quota()


@app.get("/api/tracks")
def tracks() -> dict[str, Any]:
    return {
        "tracks": [
            {
                "id": "track1",
                "title": "公开论文解析与题目生成",
                "flow": ["公开 PDF", "MinerU 官方 API", "Markdown 摘要", "DeepSeek 题目/评分说明"],
            },
            {
                "id": "track2",
                "title": "公开任务规划与产物回放",
                "flow": ["公开任务目标", "意图识别", "云端 DAG", "回放产物索引", "核验摘要"],
            },
            {
                "id": "track3",
                "title": "医学 RAG 来源回放",
                "flow": ["中文问题", "公开来源匹配", "来源卡片", "稳定回答回放", "安全边界"],
            },
        ],
        "boundary": public_boundary(),
    }


@app.post("/api/mineru/url")
def mineru_parse_url(req: UrlParseRequest, x_demo_code: str | None = Header(default=None)) -> dict[str, Any]:
    require_access(req.access_code or x_demo_code)
    cfg = settings()
    if not cfg["mineru_token"]:
        raise HTTPException(status_code=503, detail={"error": "MINERU_API_TOKEN 未配置"})
    public_url = validate_public_extract_url(req.url)
    quota_after = consume_quota("mineru_url_parse")
    try:
        with httpx.Client(timeout=25, trust_env=False) as client:
            response = client.post(
                f"{cfg['mineru_base_url']}/api/v4/extract/task",
                headers={"Authorization": f"Bearer {cfg['mineru_token']}", "Content-Type": "application/json"},
                json={"url": public_url, "model_version": req.model_version or "vlm"},
            )
            data = response.json() if response.text else {}
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail={"error": "MinerU 官方 API 请求超时"})
    except Exception as exc:
        raise HTTPException(status_code=502, detail={"error": f"MinerU 官方 API 调用失败: {str(exc)[:180]}"})
    if response.status_code >= 400:
        raise HTTPException(status_code=response.status_code, detail={"error": data})
    return {"status": "submitted", "provider": "mineru_official", "response": data, "quota": quota_after}


@app.post("/api/mineru/upload")
async def mineru_parse_upload(
    file: UploadFile = File(...),
    access_code: str = "",
    x_demo_code: str | None = Header(default=None),
) -> dict[str, Any]:
    require_access(access_code or x_demo_code)
    cfg = settings()
    if not cfg["mineru_token"]:
        raise HTTPException(status_code=503, detail={"error": "MINERU_API_TOKEN 未配置"})
    original_name = file.filename or "upload.pdf"
    if file.content_type not in {"application/pdf", "application/octet-stream"} and not original_name.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail={"error": "只接受 PDF 文件"})
    content = await file.read()
    max_bytes = cfg["upload_max_mb"] * 1024 * 1024
    if len(content) > max_bytes:
        raise HTTPException(status_code=413, detail={"error": f"文件超过 {cfg['upload_max_mb']}MB 限制"})

    quota_after = consume_quota("mineru_upload_parse")
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", Path(original_name).name)
    pdf_path = UPLOAD_DIR / f"{int(time.time())}_{safe_name}"
    pdf_path.write_bytes(content)

    result = parse_mineru_official_upload(pdf_path, cfg["mineru_token"], cfg["mineru_base_url"])
    result["quota"] = quota_after
    return result


def parse_mineru_official_upload(pdf_path: Path, token: str, base_url: str) -> dict[str, Any]:
    with httpx.Client(timeout=30, trust_env=False) as client:
        create_resp = client.post(
            f"{base_url}/api/v4/file-urls/batch",
            params={"enable_formula": "true", "enable_table": "true", "language": "ch"},
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "*/*"},
            json={"files": [{"name": pdf_path.name, "data_id": pdf_path.stem}], "model_version": "vlm"},
        )
        if create_resp.status_code != 200:
            raise HTTPException(status_code=create_resp.status_code, detail={"error": "MinerU 上传 URL 申请失败"})
        create_data = create_resp.json()
        data = create_data.get("data") or {}
        batch_id = data.get("batch_id", "")
        urls = data.get("file_urls") or []
        if not batch_id or not urls:
            raise HTTPException(status_code=502, detail={"error": "MinerU 未返回 batch_id/file_urls"})

        put_resp = client.put(urls[0], content=pdf_path.read_bytes(), headers={})
        if put_resp.status_code not in {200, 201}:
            raise HTTPException(status_code=put_resp.status_code, detail={"error": "PDF 上传到 MinerU 失败", "task_id": batch_id})

        deadline = time.time() + 180
        last_state = ""
        while time.time() < deadline:
            time.sleep(3)
            result_resp = client.get(
                f"{base_url}/api/v4/extract-results/batch/{batch_id}",
                headers={"Authorization": f"Bearer {token}", "Accept": "*/*"},
                timeout=20,
            )
            if result_resp.status_code != 200:
                continue
            result_data = result_resp.json()
            first = (((result_data.get("data") or {}).get("extract_result") or [{}])[0]) or {}
            last_state = first.get("state", "")
            if last_state == "failed":
                raise HTTPException(status_code=502, detail={"error": first.get("err_msg") or "MinerU 解析失败", "task_id": batch_id})
            if last_state == "done":
                zip_url = first.get("full_zip_url", "")
                if not zip_url:
                    raise HTTPException(status_code=502, detail={"error": "MinerU 未返回结果包", "task_id": batch_id})
                zip_resp = client.get(zip_url, timeout=60)
                if zip_resp.status_code != 200:
                    raise HTTPException(status_code=zip_resp.status_code, detail={"error": "MinerU 结果包下载失败", "task_id": batch_id})
                markdown = read_markdown_from_zip(zip_resp.content)
                return {
                    "status": "ok",
                    "provider": "mineru_official",
                    "task_id": batch_id,
                    "markdown_preview": markdown[:4000],
                    "markdown_chars": len(markdown),
                }
        return {"status": "timeout", "provider": "mineru_official", "task_id": batch_id, "last_state": last_state}


def read_markdown_from_zip(zip_bytes: bytes) -> str:
    with zipfile.ZipFile(BytesIO(zip_bytes)) as zf:
        names = zf.namelist()
        md_name = next((name for name in names if name.endswith("full.md")), "")
        if not md_name:
            md_name = next((name for name in names if name.lower().endswith(".md")), "")
        return zf.read(md_name).decode("utf-8", errors="replace") if md_name else ""


def call_deepseek(messages: list[dict[str, str]], reason: str, *, temperature: float = 0.2) -> tuple[str, dict[str, Any] | None, dict[str, Any]]:
    cfg = settings()
    if not cfg["deepseek_key"]:
        raise HTTPException(status_code=503, detail={"error": "DEEPSEEK_API_KEY 未配置"})
    quota_after = consume_quota(reason)
    try:
        with httpx.Client(timeout=60, trust_env=False) as client:
            resp = client.post(
                f"{cfg['deepseek_base']}/chat/completions",
                headers={"Authorization": f"Bearer {cfg['deepseek_key']}", "Content-Type": "application/json"},
                json={
                    "model": cfg["deepseek_model"],
                    "messages": messages,
                    "temperature": temperature,
                },
            )
            data = resp.json() if resp.text else {}
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail={"error": "DeepSeek API 请求超时"})
    except Exception as exc:
        raise HTTPException(status_code=502, detail={"error": f"DeepSeek API 调用失败: {str(exc)[:180]}"})
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail={"error": data})
    answer = (((data.get("choices") or [{}])[0]).get("message") or {}).get("content", "")
    return answer, data.get("usage"), quota_after


def mock_quiz(source_text: str, topic: str, count: int) -> list[dict[str, Any]]:
    clean = re.sub(r"\s+", " ", source_text or "").strip()
    evidence = clean[:220] if clean else "公开/脱敏解析文本未提供，验收时请传入 MinerU 解析结果或论文摘要。"
    base = [
        ("来源定位题", f"根据材料，概括与「{topic}」最直接相关的研究结论，并指出来源来自哪里。"),
        ("机制理解题", "解释该研究结果可能支持或限制某个科学判断的原因。"),
        ("边界判断题", "指出该材料不能支持哪些过度推断，并说明原因。"),
        ("评分应用题", "给出一个候选回答，判断它是否忠实于材料并列出扣分点。"),
        ("综合题", "用三句话总结研究问题、关键来源和安全边界。"),
    ]
    return [
        {
            "id": f"q{i + 1}",
            "type": base[i % len(base)][0],
            "question": base[i % len(base)][1],
            "expected_answer": f"应基于公开解析材料回答，至少引用一个来源片段：{evidence}",
            "rubric": "满分 10 分：事实准确 4 分，来源引用 3 分，边界表述 2 分，中文表达 1 分。",
        }
        for i in range(max(1, min(count, 8)))
    ]


PUBLIC_MEDICAL_CHUNKS: list[dict[str, str]] = [
    {
        "id": "pmc-t1d-closed-loop-48m-01",
        "title": "Adaptive closed-loop insulin delivery after diagnosis in children and adolescents",
        "source": "公开 PMC 糖尿病闭环胰岛素随访研究",
        "topic": "closed_loop_insulin",
        "text": (
            "In children and adolescents with newly diagnosed type 1 diabetes, daily insulin requirements increased "
            "substantially during the first 48 months after diagnosis. The proportion of insulin delivered by the "
            "closed-loop algorithm also increased over time, suggesting that adaptive closed-loop systems can respond "
            "to changing insulin needs during early disease progression."
        ),
        "zh": (
            "新诊断 1 型糖尿病儿童和青少年在诊断后 48 个月内每日胰岛素需求明显上升；闭环算法输送的胰岛素比例也随时间增加，"
            "说明自适应闭环系统的意义在于跟随需求变化调整输送，而不是给出固定剂量。"
        ),
    },
    {
        "id": "pmc-t1d-hypoglycaemia-02",
        "title": "Closed-loop therapy and hypoglycaemia safety endpoints",
        "source": "公开 PMC 闭环胰岛素安全性终点研究",
        "topic": "hypoglycaemia",
        "text": (
            "Trials of hybrid closed-loop therapy commonly report time below range and severe hypoglycaemia as safety "
            "endpoints. Interpretation should distinguish population-level safety outcomes from individual treatment "
            "decisions, because personal dosing requires clinician assessment and device-specific data."
        ),
        "zh": (
            "闭环治疗研究通常把低于目标血糖范围时间和严重低血糖作为安全性终点。文献层面的安全性结论只能说明群体趋势，"
            "不能替代个体剂量调整或设备处方。"
        ),
    },
    {
        "id": "pmc-chemo-dose-modification-03",
        "title": "Chemotherapy dose modification in oncology trials",
        "source": "公开肿瘤治疗试验方案摘要",
        "topic": "chemotherapy_dose",
        "text": (
            "Oncology trial protocols usually define dose modification rules for toxicity, organ function, and treatment "
            "delays. These rules are protocol-level safeguards and should not be used as patient-specific medication advice "
            "without full clinical context."
        ),
        "zh": (
            "肿瘤试验方案中的化疗剂量调整规则通常围绕毒性、器官功能和延迟治疗设定，是研究方案层面的安全控制，"
            "不能直接当作个人用药建议。"
        ),
    },
    {
        "id": "pmc-survival-itt-04",
        "title": "Intention-to-treat population and survival endpoints",
        "source": "公开临床试验统计方法摘要",
        "topic": "itt_survival",
        "text": (
            "Intention-to-treat analysis preserves the original randomized groups and is widely used for primary efficacy "
            "analysis. Survival endpoints require careful censoring rules, follow-up definitions, and transparent reporting "
            "of excluded or missing data."
        ),
        "zh": (
            "ITT 分析保留原始随机分组，常用于主要疗效分析。生存获益判断需要同时说明删失规则、随访定义以及缺失数据处理。"
        ),
    },
    {
        "id": "pmc-inclusion-exclusion-05",
        "title": "Eligibility criteria in clinical trials",
        "source": "公开临床试验纳入排除标准摘要",
        "topic": "eligibility",
        "text": (
            "Eligibility criteria define the population to which a trial result most directly applies. Inclusion and exclusion "
            "rules protect participants and reduce confounding, but they also limit generalization to patients outside the "
            "studied population."
        ),
        "zh": (
            "纳入排除标准决定研究结论最直接适用的人群。它既保护受试者并减少混杂，也会限制结论向真实世界患者外推。"
        ),
    },
]


MEDICAL_QUERY_HINTS: dict[str, list[str]] = {
    "closed_loop_insulin": ["闭环", "胰岛素", "低血糖", "48", "儿童", "青少年", "insulin", "closed", "loop", "hypoglycaemia", "hypoglycemia"],
    "hypoglycaemia": ["闭环", "胰岛素", "低血糖", "安全", "终点", "insulin", "closed", "loop", "hypoglycaemia", "hypoglycemia", "safety"],
    "chemotherapy_dose": ["化疗", "剂量", "毒性", "减量", "chemotherapy", "dose", "toxicity"],
    "itt_survival": ["生存", "获益", "itt", "人群", "survival", "endpoint", "intention"],
    "eligibility": ["纳入", "排除", "标准", "eligibility", "inclusion", "exclusion"],
}


def is_personal_medical_question(question: str) -> bool:
    lowered = question.lower()
    patterns = [
        "我该", "我要不要", "帮我诊断", "怎么吃药", "吃多少", "能不能停药", "胸痛", "呼吸困难",
        "my dose", "diagnose me", "should i take", "chest pain", "emergency",
    ]
    return any(pattern in lowered for pattern in patterns)


def retrieve_public_medical_chunks(question: str, limit: int = 3) -> list[dict[str, Any]]:
    lowered = question.lower()
    scored: list[tuple[int, dict[str, str]]] = []
    for chunk in PUBLIC_MEDICAL_CHUNKS:
        haystack = " ".join([chunk["title"], chunk["topic"], chunk["text"], chunk["zh"]]).lower()
        score = 0
        for token in re.findall(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]{2,}", lowered):
            if token and token in haystack:
                score += 2
        for topic, hints in MEDICAL_QUERY_HINTS.items():
            if topic == chunk["topic"]:
                score += sum(1 for hint in hints if hint.lower() in lowered)
        if score:
            scored.append((score, chunk))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [
        {
            "id": chunk["id"],
            "title": chunk["title"],
            "source": chunk["source"],
            "score": score,
            "text": chunk["text"],
            "zh": chunk["zh"],
        }
        for score, chunk in scored[:limit]
    ]


def synthesize_medical_answer(question: str, chunks: list[dict[str, Any]]) -> str:
    if not chunks:
        return (
            "当前公开来源回放集中没有检索到足够来源，不能强行回答。云端 Demo 只展示公开/脱敏医学文献的来源回放；"
            "完整系统会使用更大的医学索引、混合检索和 claim 校验。"
        )
    source_lines = "\n".join([f"- {chunk['id']}：{chunk['zh']}" for chunk in chunks])
    lowered = question.lower()
    if any("闭环" in question or word in lowered for word in ["insulin", "hypogly"]):
        return (
            "机制解释：公开来源显示，新诊断 1 型糖尿病儿童和青少年在诊断后 48 个月内每日胰岛素需求明显上升，"
            "闭环算法输送的胰岛素比例也随时间增加。因此，这个案例支持的是“自适应系统能跟随需求变化调整输送”的机制，"
            "而不是“给出某个固定剂量”。安全性需要看低于目标血糖范围时间、严重低血糖等终点，并且只能解释群体层面的研究结论。"
            "这不是个人治疗、处方或急诊判断。\n\n"
            f"来源摘要：\n{source_lines}"
        )
    if any(token in lowered or token in question for token in ["os", "pfs", "rpfs", "总生存", "无进展", "生存获益"]):
        return (
            "机制解释：这里要先区分“终点定义”和“生存获益结论”。OS 通常是更硬的生存终点；"
            "PFS/rPFS 是进展相关终点，可以说明疾病控制时间，但不能自动等同于已经证明延长总生存。"
            "如果来源只给出从首次给药到死亡或影像学进展的计算规则，那只是该研究的 endpoint definition，"
            "不是治疗获益结论。\n\n"
            "边界：判断生存获益还需要看随机化/ITT 人群、删失规则、随访成熟度、对照组差异和最终 OS 分析。"
            "这个回答只解释公开文献中的统计终点，不推断具体患者预后。\n\n"
            f"来源摘要：\n{source_lines}"
        )
    if any(token in lowered or token in question for token in ["itt", "intention", "获益"]):
        return (
            "机制解释：ITT 分析保留原始随机分组，能减少因退出、换组或治疗依从性差异带来的选择偏倚。"
            "因此，当问题是“生存获益是否成立”时，不能只看完成治疗人群，还要看随机化人群、删失规则、随访定义和缺失数据。"
            "这个回答只说明文献统计方法的适用边界，不推断具体患者预后。\n\n"
            f"来源摘要：\n{source_lines}"
        )
    if any(token in lowered or token in question for token in ["eligibility", "inclusion", "exclusion", "纳入", "排除"]):
        return (
            "机制解释：纳入排除标准决定研究结论最直接适用的人群。严格标准能降低混杂、保护受试者，"
            "但也会让试验人群和真实世界患者产生差距，所以外推结论时必须说明哪些人群没有被研究覆盖。"
            "这个回答只讨论研究设计边界，不判断个体是否应入组或接受治疗。\n\n"
            f"来源摘要：\n{source_lines}"
        )
    if any(token in lowered or token in question for token in ["chemotherapy", "dose", "toxicity", "化疗", "剂量"]):
        return (
            "机制解释：化疗剂量调整规则通常来自试验方案，对毒性、器官功能和延迟治疗做预设处理。"
            "它的作用是保证研究执行一致和受试者安全，而不是把方案规则直接变成个人用药建议。"
            "具体剂量必须由临床医生结合完整病情判断。\n\n"
            f"来源摘要：\n{source_lines}"
        )
    return (
        "根据公开来源，当前问题可以从研究设计、适用人群和安全边界三个层面理解。系统先匹配公开来源，"
        "再基于命中来源合成中文回答；如果问题转向个人诊疗或用药，云端 Demo 会保留边界而不直接给建议。\n\n"
        f"来源摘要：\n{source_lines}"
    )


@app.post("/api/quiz/generate")
def quiz_generate(req: QuizGenerateRequest, x_demo_code: str | None = Header(default=None)) -> dict[str, Any]:
    require_access(req.access_code or x_demo_code, allow_unconfigured=req.dry_run)
    source = (req.source_text or "").strip()
    if len(source) < 20:
        raise HTTPException(status_code=400, detail={"error": "source_text 至少需要 20 个字符，可传入 MinerU markdown_preview 或论文摘要"})
    count = max(1, min(int(req.count or 3), 8))
    cfg = settings()
    if req.dry_run or not cfg["deepseek_key"]:
        return {
            "status": "dry_run" if req.dry_run else "mock",
            "provider": "deepseek",
            "questions": mock_quiz(source, req.topic, count),
            "boundary": public_boundary(),
            "quota": read_quota(),
        }

    prompt = (
        "请只基于公开/脱敏解析文本生成中文评测题。返回严格 JSON，不要 Markdown 代码块。"
        "JSON schema: {\"questions\":[{\"id\":\"q1\",\"type\":\"...\",\"question\":\"...\","
        "\"expected_answer\":\"...\",\"rubric\":\"...\"}]}\n\n"
        f"主题：{req.topic}\n题目数量：{count}\n解析文本：{source[:8000]}"
    )
    answer, usage, quota_after = call_deepseek(
        [
            {"role": "system", "content": "你是 ControlMind 云端 Demo 的出题 API，只处理公开或脱敏材料。"},
            {"role": "user", "content": prompt},
        ],
        "quiz_generate",
        temperature=0.1,
    )
    parsed: dict[str, Any]
    try:
        parsed = json.loads(answer)
    except Exception:
        parsed = {"questions": mock_quiz(source, req.topic, count), "raw_answer": answer}
    questions = parsed.get("questions") if isinstance(parsed, dict) else None
    if not isinstance(questions, list) or not questions:
        questions = mock_quiz(source, req.topic, count)
    return {"status": "ok", "provider": "deepseek", "questions": questions[:count], "raw_usage": usage, "quota": quota_after}


@app.post("/api/quiz/grade")
def quiz_grade(req: QuizGradeRequest, x_demo_code: str | None = Header(default=None)) -> dict[str, Any]:
    require_access(req.access_code or x_demo_code, allow_unconfigured=req.dry_run)
    question = (req.question or "").strip()
    student_answer = (req.student_answer or "").strip()
    if not question or not student_answer:
        raise HTTPException(status_code=400, detail={"error": "question 和 student_answer 不能为空"})
    cfg = settings()
    if req.dry_run or not cfg["deepseek_key"]:
        score = 7 if len(student_answer) >= 30 else 5
        return {
            "status": "dry_run" if req.dry_run else "mock",
            "provider": "deepseek",
            "score": score,
            "max_score": 10,
            "feedback": "演示评分：回答已进入云端评分 API；正式配置 DeepSeek key 后会根据题目、评分点和公开来源给出细分扣分理由。",
            "rubric_hits": ["边界检查已生效", "密钥未进入前端", "仅公开/脱敏材料"],
            "quota": read_quota(),
        }

    prompt = (
        "请作为严格评分 API，只根据题目、标准答案/评分点、学生回答和公开来源评分。"
        "返回严格 JSON，不要 Markdown 代码块。"
        "JSON schema: {\"score\":0-10,\"max_score\":10,\"feedback\":\"...\",\"rubric_hits\":[\"...\"],\"deductions\":[\"...\"]}\n\n"
        f"题目：{question}\n标准答案：{req.expected_answer}\n评分点：{req.rubric}\n学生回答：{student_answer}\n公开来源：{req.source_text[:6000]}"
    )
    answer, usage, quota_after = call_deepseek(
        [
            {"role": "system", "content": "你是 ControlMind 云端 Demo 的评分 API，只处理公开或脱敏材料，不给个人诊疗建议。"},
            {"role": "user", "content": prompt},
        ],
        "quiz_grade",
        temperature=0,
    )
    try:
        parsed = json.loads(answer)
    except Exception:
        parsed = {"score": None, "max_score": 10, "feedback": answer, "rubric_hits": [], "deductions": []}
    return {"status": "ok", "provider": "deepseek", **parsed, "raw_usage": usage, "quota": quota_after}


@app.post("/api/agent/plan")
def agent_plan(req: AgentPlanRequest, x_demo_code: str | None = Header(default=None)) -> dict[str, Any]:
    require_access(req.access_code or x_demo_code, allow_unconfigured=True)
    goal = (req.goal or "").strip()
    if len(goal) < 4:
        raise HTTPException(status_code=400, detail={"error": "goal 至少需要 4 个字符"})
    lowered = goal.lower()
    if any(token in lowered for token in ["rag", "医学", "问答", "medical"]):
        intent = "medical_rag_public_check"
        dag = ["边界判定", "公开来源检索", "中文合成", "claim 支撑状态", "安全声明"]
        artifacts = ["docs/submissions/track3_medical_rag_report.md", "docs/submissions/data_trace_bundle/07_medical_rag/"]
    elif any(token in lowered for token in ["评测", "出题", "评分", "quiz", "benchmark"]):
        intent = "sci_align_quiz_eval"
        dag = ["公开 PDF 解析", "Markdown 摘要", "ABCD 出题", "Rubric 评分", "来源路径记录"]
        artifacts = ["docs/submissions/track1_sci_align_report.md", "benchmark/dataset/core.json"]
    else:
        intent = "data_agent_public_plan"
        dag = ["目标解析", "输入边界检查", "资源选择", "执行步骤生成", "核验摘要"]
        artifacts = ["docs/submissions/track2_agent_report.md", "docs/submissions/data_trace_bundle/manifest.json"]
    return {
        "status": "ok",
        "provider": "deterministic_cloud_planner",
        "goal": goal,
        "intent": intent,
        "dag": [{"step": idx + 1, "name": name, "mode": "cloud_public_demo"} for idx, name in enumerate(dag)],
        "resource_policy": {
            "allowed": ["MinerU 官方 API", "DeepSeek API", "公开报告路径", "公开/脱敏 demo index"],
            "removed": ["重资产长任务", "私有原文", "私有向量库", "批量实验"],
        },
        "local_artifacts": artifacts,
        "acceptance": ["页面可回放已验证产物", "云端只处理公开轻量任务", "密钥不进入浏览器", "每个结论可回到来源或产物"],
        "boundary": public_boundary(),
    }


@app.post("/api/medical-rag/ask")
def medical_rag_ask(req: MedicalRagRequest, x_demo_code: str | None = Header(default=None)) -> dict[str, Any]:
    require_access(req.access_code or x_demo_code, allow_unconfigured=req.dry_run)
    question = (req.question or "").strip()
    if not question:
        raise HTTPException(status_code=400, detail={"error": "question 不能为空"})
    if is_personal_medical_question(question):
        return {
            "status": "refused",
            "provider": "public_medical_mini_rag",
            "answer": "该问题看起来涉及个人诊疗、用药或急症判断。云端 Demo 只回答公开医学文献层面的来源问答，不替代医生诊断、处方或急诊处理。",
            "retrieved_sources": [],
            "claim_status": "refused_personal_medical_advice",
            "boundary": public_boundary(),
            "quota": read_quota(),
        }
    chunks = retrieve_public_medical_chunks(question)
    cfg = settings()
    if req.dry_run or not cfg["deepseek_key"] or not chunks:
        return {
            "status": "dry_run" if req.dry_run else "ok",
            "provider": "public_medical_mini_rag",
            "answer": synthesize_medical_answer(question, chunks),
            "retrieved_sources": chunks,
            "claim_status": "supported" if chunks else "insufficient_sources",
            "boundary": public_boundary(),
            "quota": read_quota(),
        }
    context = "\n\n".join([f"[{chunk['id']}] {chunk['title']}\n{chunk['text']}\n中文摘要：{chunk['zh']}" for chunk in chunks])
    answer, usage, quota_after = call_deepseek(
        [
            {
                "role": "system",
                "content": (
                    "你是 ControlMind 云端公开医学 RAG 合成器。必须只基于给定来源回答，"
                    "用中文解释机制，列出来源 id，并明确不替代个人诊疗或用药建议。"
                ),
            },
            {"role": "user", "content": f"问题：{question}\n\n检索到的公开来源：\n{context}"},
        ],
        "medical_rag_ask",
        temperature=0.1,
    )
    return {
        "status": "ok",
        "provider": "deepseek_with_public_medical_mini_rag",
        "answer": answer,
        "retrieved_sources": chunks,
        "claim_status": "supported",
        "raw_usage": usage,
        "quota": quota_after,
    }


@app.post("/api/deepseek/ask")
def deepseek_ask(req: AskRequest, x_demo_code: str | None = Header(default=None)) -> dict[str, Any]:
    require_access(req.access_code or x_demo_code, allow_unconfigured=req.dry_run)
    question = (req.question or "").strip()
    if not question:
        raise HTTPException(status_code=400, detail={"error": "question 不能为空"})
    cfg = settings()
    if req.dry_run or not cfg["deepseek_key"]:
        return {
            "status": "dry_run" if req.dry_run else "mock",
            "provider": "deepseek",
            "answer": f"演示边界已生效：问题「{question}」只能基于公开/脱敏来源回答，不处理个人诊疗或私有材料。",
            "boundary": public_boundary(),
            "quota": read_quota(),
        }
    system_prompt = "你是 ControlMind 公开云端 Demo 助手。只基于公开或脱敏材料回答，不能给个人诊断、处方或处理私有材料。"
    user_prompt = f"问题：{question}\n\n公开/脱敏上下文：{req.context[:4000] if req.context else '未提供额外上下文，请给出边界清晰的演示性回答。'}"
    answer, usage, quota_after = call_deepseek(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "deepseek_ask",
        temperature=0.2,
    )
    return {"status": "ok", "provider": "deepseek", "answer": answer, "raw_usage": usage, "quota": quota_after}


@app.get("/api/assets/{name:path}")
def asset(name: str) -> FileResponse:
    safe = Path(name)
    if safe.is_absolute() or ".." in safe.parts:
        raise HTTPException(status_code=400, detail={"error": "非法资源路径"})
    candidate_roots = [
        ROOT.parent / "docs" / "submissions" / "data_trace_bundle",
        ROOT.parent / "docs" / "submissions" / "shared" / "assets",
    ]
    for base in candidate_roots:
        path = (base / safe).resolve()
        if base.resolve() in path.parents and path.is_file():
            return FileResponse(path)
    raise HTTPException(status_code=404, detail={"error": "资源不存在"})
