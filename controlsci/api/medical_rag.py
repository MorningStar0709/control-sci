"""Clinical Evidence Synthesis Agent — FastAPI REST API

三端点:
  GET  /api/evidence/search?q=...&k=5      Hybrid 检索 (FAISS + BM25 + RRF)
  POST /api/evidence/synthesize            跨文献证据合成 (检索 → 格式化 → 存档)
  GET  /api/evidence/report/{task_id}      查询历史报告

启动:
  conda run --no-capture-output -n myenv uvicorn controlsci.api.medical_rag:app --port 8001

前置条件:
  - FAISS + BM25 索引已构建 (data/sources_medical/index/)
  - chunks manifest 就绪 (data/sources_medical/chunks/)
  - Ollama qwen3-embedding:4b 运行中 (http://localhost:11434)
"""

import json
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from controlsci.api.settings import get_settings
from controlsci.core.paths import PROJECT_ROOT
from controlsci.medical.indexing import _load_chunk_texts, load_manifest, search_hybrid
from controlsci.medical.embedding_providers import read_index_metadata

LOCAL_MEDICAL_ROOT = PROJECT_ROOT / "data" / "sources_medical"
DEMO_MEDICAL_ROOT = PROJECT_ROOT / "data" / "demo_cloud" / "medical"
REPORT_DIR = PROJECT_ROOT / "benchmark" / "eval" / "results" / "medical"
TRACE_JSONL = PROJECT_ROOT / "benchmark" / "eval" / "results" / "medical_rag_live_traces.jsonl"

app = FastAPI(
    title="Clinical Evidence Synthesis Agent",
    description="基于 MinerU 解析 + Hybrid 检索 (FAISS Dense + BM25 Sparse + RRF) 的医疗文献 RAG API",
    version="1.0.0",
)

from controlsci.api.demo_endpoints import router as demo_router
app.include_router(demo_router)


class SynthesizeRequest(BaseModel):
    query: str
    doc_ids: list[int] = []
    k: int = 3
    synthesis_model: str = "qwen3.5:9b"
    mode: str = "hybrid"
    index_id: str = "qwen"


class AskRequest(BaseModel):
    question: str
    k: int = 3
    synthesis_model: str = "qwen3.5:9b"
    mode: str = "hybrid"
    index_id: str = "bge_m3"
    session_id: str | None = None
    history: list[dict] = []
    triage_model: str | None = None
    runtime_config: dict | None = None


class HealthResponse(BaseModel):
    status: str
    timestamp: str
    profile: str
    components: dict
    issues: list[str]


class SearchResultItem(BaseModel):
    rank: int
    chunk_id: str
    rrf_score: float
    vision_score: float | None = None
    is_vision: bool = False
    medical_label: str
    medical_parent: str | None
    source_file: str
    source_section: str
    text_preview: str
    text_full: str


class SearchResponse(BaseModel):
    query: str
    search_query: str | None = None
    search_queries: list[str] = []
    query_language: str | None = None
    query_rewrites: list[dict] = []
    rewrite_method: str | None = None
    top_k: int
    mode: str = "hybrid"
    vision_enabled: bool = False
    count: int
    results: list[SearchResultItem]


_chunk_texts_cache = None
_INDEX_ALIASES = {
    "qwen": "index",
    "qwen3": "index",
    "qwen3_embedding": "index",
    "bge_small": "index_bge_small",
    "bge-small": "index_bge_small",
    "bge_m3": "index_bge_m3",
    "bge-m3": "index_bge_m3",
}


def _api_profile():
    profile = os.environ.get("CONTROLSCI_API_PROFILE", "").strip().lower()
    if profile:
        return profile
    if os.environ.get("DEMO_MODE", "").strip().lower() in {"1", "true", "yes", "cloud_demo"}:
        return "cloud_demo"
    return "local_private"


def _is_cloud_demo():
    return _api_profile() == "cloud_demo"


def _medical_root():
    if _is_cloud_demo() and DEMO_MEDICAL_ROOT.exists():
        return DEMO_MEDICAL_ROOT
    return LOCAL_MEDICAL_ROOT


def _index_dir(index_id: str | None = None):
    key = (index_id or "qwen").strip()
    dirname = _INDEX_ALIASES.get(key, key)
    if Path(dirname).is_absolute():
        raise HTTPException(status_code=400, detail={"error": "index_id 不允许使用绝对路径"})
    if ".." in Path(dirname).parts:
        raise HTTPException(status_code=400, detail={"error": "index_id 不允许访问上级目录"})
    return _medical_root() / dirname


def _index_meta(index_id: str | None = None) -> dict:
    meta = read_index_metadata(_index_dir(index_id))
    if not meta:
        meta = {
            "index_id": Path(_index_dir(index_id)).name,
            "embedding_provider": "unknown",
            "embedding_model": "unknown",
        }
    if _is_cloud_demo():
        allowed = {
            "index_id",
            "created_at",
            "embedding_provider",
            "embedding_model",
            "embedding_dim",
            "chunk_count",
            "manifest_sha256",
            "cache_shape",
            "note",
        }
        meta = {key: value for key, value in meta.items() if key in allowed}
    meta["alias"] = (index_id or "qwen").strip() or "qwen"
    meta["path"] = _safe_source_file(str(_index_dir(index_id)))
    meta["available"] = _dense_path(index_id).exists() and _sparse_path(index_id).exists()
    meta["dense_size_kb"] = _safe_file_size_kb(_dense_path(index_id)) if _dense_path(index_id).exists() else 0
    meta["bm25_size_kb"] = _safe_file_size_kb(_sparse_path(index_id)) if _sparse_path(index_id).exists() else 0
    return meta


def _available_indexes() -> list[dict]:
    items = [
        ("qwen", "Qwen3 Embedding"),
        ("bge_small", "BGE Small"),
        ("bge_m3", "BGE M3"),
    ]
    result = []
    for alias, label in items:
        meta = _index_meta(alias)
        meta["label"] = label
        result.append(meta)
    return result


def _manifest_candidates():
    root = _medical_root()
    return [
        root / "chunks" / "chunks_manifest.json",
        root / "md" / "chunks" / "chunks_manifest.json",
    ]


def _dense_path(index_id: str | None = None):
    return _index_dir(index_id) / "medical.index"


def _sparse_path(index_id: str | None = None):
    return _index_dir(index_id) / "bm25.pkl"


def _vision_index_path():
    return _index_dir() / "medical_vision.index"


def _vision_chunks_path():
    return _index_dir() / "medical_vision.chunks.json"


def _get_or_load_texts(manifest):
    global _chunk_texts_cache
    if _chunk_texts_cache is None:
        _chunk_texts_cache = _load_chunk_texts(manifest["chunks"])
    return _chunk_texts_cache


def _find_manifest():
    for p in _manifest_candidates():
        if p.exists():
            return p
    return None


def _check_index_issues(index_id: str | None = None):
    issues = []
    if not _dense_path(index_id).exists():
        issues.append(f"FAISS 索引缺失: {_dense_path(index_id)}")
    if not _sparse_path(index_id).exists():
        issues.append(f"BM25 索引缺失: {_sparse_path(index_id)}")
    return issues


def _check_vision_available():
    return _vision_index_path().exists() and _vision_chunks_path().exists()


def _public_medical_evidence_dir():
    return PROJECT_ROOT / "docs" / "submissions" / "data_trace_bundle" / "09_medical_rag"


def _public_medical_evidence_ok():
    root = _public_medical_evidence_dir()
    required = [
        "medical_rag_eval.json",
        "medical_rag_eval_zh_ask.json",
        "vision_chunks_manifest.json",
        "vision_descriptions_qwen35.jsonl",
    ]
    return all((root / name).exists() for name in required)


def _format_vision_result(r, rank):
    text = r.get("text", "")
    return {
        "rank": rank,
        "chunk_id": r.get("chunk_id", ""),
        "rrf_score": r.get("_rrf_score", 0.0),
        "vision_score": r.get("_vision_score", 0.0),
        "is_vision": True,
        "medical_label": "vision_chunk",
        "medical_parent": None,
        "source_file": _safe_source_file(r.get("source_pmc", "")),
        "source_section": "",
        "text_preview": _preview_text(text),
        "text_full": _exposed_text(text),
    }


def _safe_file_size_kb(path):
    try:
        return path.stat().st_size // 1024
    except OSError:
        return -1


def _safe_source_file(path_value):
    if not path_value:
        return ""
    try:
        path = Path(path_value)
        if path.is_absolute():
            return path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix()
    except Exception:
        pass
    if _is_cloud_demo() and Path(path_value) in {DEMO_MEDICAL_ROOT, LOCAL_MEDICAL_ROOT}:
        return "medical_data"
    return Path(path_value).name if _is_cloud_demo() else str(path_value)


def _preview_text(text):
    limit = 180 if _is_cloud_demo() else 300
    return (text or "")[:limit].replace("\n", " ")


def _exposed_text(text):
    return "" if _is_cloud_demo() else (text or "")


def _safe_issue(issue):
    if not _is_cloud_demo():
        return issue
    text = str(issue)
    text = text.replace(str(DEMO_MEDICAL_ROOT), "medical_data")
    text = text.replace(str(LOCAL_MEDICAL_ROOT), "medical_data")
    text = text.replace(str(PROJECT_ROOT), ".")
    return text


@lru_cache(maxsize=1)
def _cached_manifest():
    path = _find_manifest()
    if not path:
        raise HTTPException(
            status_code=503,
            detail={
                "error": "chunks manifest 未找到",
                "profile": _api_profile(),
                "checked": [_safe_source_file(str(p)) for p in _manifest_candidates()],
            },
        )
    try:
        return load_manifest(path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"manifest 加载失败 ({path}): {e}")


def _require_manifest():
    return _cached_manifest()


def _require_index(index_id: str | None = None):
    issues = _check_index_issues(index_id)
    if issues:
        raise HTTPException(status_code=503, detail={"error": "索引不可用", "issues": issues})


def _format_search_result(r, rank):
    text = r.get("text", "")
    return {
        "rank": rank,
        "chunk_id": r.get("chunk_id", ""),
        "rrf_score": r.get("_rrf_score", 0.0),
        "vision_score": None,
        "is_vision": False,
        "medical_label": r.get("medical_label", ""),
        "medical_parent": r.get("medical_parent"),
        "source_file": _safe_source_file(r.get("filepath", "")),
        "source_section": r.get("source_section", ""),
        "text_preview": _preview_text(text),
        "text_full": _exposed_text(text),
    }


def _search(query, k, manifest, index_id: str | None = None):
    texts = _get_or_load_texts(manifest)
    return search_hybrid(query, _index_dir(index_id), manifest, k=k, texts_override=texts)


def _attach_text(chunk, texts, idx, score_key, score):
    result = dict(chunk)
    result["_rrf_score"] = round(float(score), 6)
    result[score_key] = round(float(score), 6)
    if idx < len(texts):
        result["text"] = texts[idx]
    return result


def _search_dense(query, k, manifest, index_id: str | None = None):
    import faiss
    from controlsci.medical.embedding_providers import OLLAMA_DEFAULT_MODEL, embed_texts

    meta = _index_meta(index_id)
    index = faiss.read_index(str(_dense_path(index_id)))
    q_emb = embed_texts(
        [query],
        meta.get("embedding_provider", "ollama"),
        meta.get("embedding_model", OLLAMA_DEFAULT_MODEL),
        batch_size=1,
        progress_label="query_embed",
    )
    q_emb_norm = q_emb.copy()
    faiss.normalize_L2(q_emb_norm)
    scores, indices = index.search(q_emb_norm, k)
    texts = _get_or_load_texts(manifest)

    results = []
    for idx, score in zip(indices[0], scores[0]):
        if 0 <= idx < len(manifest["chunks"]):
            results.append(_attach_text(manifest["chunks"][idx], texts, idx, "_dense_score", score))
    return results


def _search_bm25(query, k, manifest, index_id: str | None = None):
    import pickle
    import numpy as np

    with open(_sparse_path(index_id), "rb") as f:
        bm25_data = pickle.load(f)
    tokenized_query = query.lower().split()
    sparse_scores = np.array(bm25_data["bm25"].get_scores(tokenized_query))
    top_indices = np.argsort(sparse_scores)[-k:][::-1]
    texts = _get_or_load_texts(manifest)

    results = []
    for idx in top_indices:
        if 0 <= idx < len(manifest["chunks"]):
            results.append(_attach_text(manifest["chunks"][int(idx)], texts, int(idx), "_bm25_score", sparse_scores[int(idx)]))
    return results


def _search_by_mode(query, k, manifest, mode, index_id: str | None = None):
    if mode == "dense":
        return _search_dense(query, k, manifest, index_id=index_id), False
    if mode == "bm25":
        return _search_bm25(query, k, manifest, index_id=index_id), False
    if mode == "vision":
        if _check_vision_available():
            return _search_combined(query, k, manifest, index_id=index_id), True
        try:
            return _search(query, k, manifest, index_id=index_id), False
        except Exception:
            return _search_bm25(query, k, manifest, index_id=index_id), False
    try:
        return _search(query, k, manifest, index_id=index_id), False
    except Exception:
        return _search_bm25(query, k, manifest, index_id=index_id), False


def _search_multi_query(query_info: dict, k, manifest, mode, index_id: str | None = None):
    queries = query_info.get("search_queries") or [query_info.get("search_query") or query_info.get("original_query", "")]
    queries = [q for q in queries if q]
    if len(queries) <= 1:
        return _search_by_mode(queries[0], k, manifest, mode, index_id=index_id)

    rrf_k = 60
    fused_scores = {}
    fused_items = {}
    vision_enabled = False
    per_query_k = max(k * 2, 5)
    for query in queries:
        items, query_vision = _search_by_mode(query, per_query_k, manifest, mode, index_id=index_id)
        vision_enabled = vision_enabled or query_vision
        for rank, item in enumerate(items):
            chunk_id = item.get("chunk_id")
            if not chunk_id:
                continue
            fused_scores[chunk_id] = fused_scores.get(chunk_id, 0.0) + 1.0 / (rrf_k + rank + 1)
            if chunk_id not in fused_items:
                fused_items[chunk_id] = dict(item)

    results = []
    for chunk_id, score in sorted(fused_scores.items(), key=lambda x: -x[1])[:k]:
        item = fused_items[chunk_id]
        item["_rrf_score"] = round(score, 6)
        item["_multi_query_count"] = len(queries)
        results.append(item)
    return results, vision_enabled


def _search_vision(query, k):
    import faiss, json
    import numpy as np
    from benchmark.eval.chunk_embedding_analysis import get_embeddings

    index = faiss.read_index(str(_vision_index_path()))
    visual_chunks = json.loads(_vision_chunks_path().read_text(encoding="utf-8"))

    q_emb = get_embeddings([query])
    q_emb_norm = q_emb.copy()
    faiss.normalize_L2(q_emb_norm)
    scores, indices = index.search(q_emb_norm, k * 2)

    results = []
    for rank, (idx, score) in enumerate(zip(indices[0], scores[0])):
        if idx < 0 or idx >= len(visual_chunks):
            continue
        c = dict(visual_chunks[idx])
        c["_rrf_score"] = round(float(score), 6)
        c["_vision_score"] = round(float(score), 6)
        results.append(c)
    return results


def _search_combined(query, k, manifest, index_id: str | None = None):
    text_results = _search(query, k * 2, manifest, index_id=index_id)
    vision_results = _search_vision(query, k * 2)

    rrf_k = 60
    rrf_scores = {}
    for rank, r in enumerate(text_results):
        rrf_scores[r["chunk_id"]] = rrf_scores.get(r["chunk_id"], 0) + 1.0 / (rrf_k + rank + 1)

    for rank, r in enumerate(vision_results):
        rrf_scores[r["chunk_id"]] = rrf_scores.get(r["chunk_id"], 0) + 1.0 / (rrf_k + rank + 1)

    seen = set()
    results = []
    for chunk_id, score in sorted(rrf_scores.items(), key=lambda x: -x[1])[:k]:
        if chunk_id in seen:
            continue
        seen.add(chunk_id)
        is_vision = chunk_id.startswith("vision_")
        src = [r for r in (vision_results if is_vision else text_results) if r["chunk_id"] == chunk_id]
        if src:
            r = dict(src[0])
            r["_rrf_score"] = round(score, 6)
            results.append(r)

    return results


def _clean_model_choice(model: str | None) -> str:
    value = (model or "").strip()
    if not value or value in {"local", "replay"}:
        return "qwen3.5:9b"
    if value in {"deepseek", "openai", "minimax", "mimo"}:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Task3 医疗 RAG 必须使用本地模型合成，不能将医疗检索上下文发送到云端 API。",
                "requested_model": value,
            },
        )
    return value


_ZH_RETRIEVAL_TERMS = [
    ("主要终点", "primary endpoint", "specific"),
    ("次要终点", "secondary endpoint", "specific"),
    ("终点", "endpoint outcome", "specific"),
    ("安全性", "safety adverse events", "specific"),
    ("严重不良事件", "serious adverse event safety endpoint", "specific"),
    ("不良事件", "adverse events", "specific"),
    ("总生存", "overall survival", "specific"),
    ("总体生存", "overall survival", "specific"),
    ("无进展生存", "progression free survival", "specific"),
    ("生存曲线", "survival curve", "specific"),
    ("中位生存", "median overall survival", "specific"),
    ("纳入排除", "inclusion criteria exclusion criteria", "specific"),
    ("纳入标准", "inclusion criteria", "specific"),
    ("排除标准", "exclusion criteria", "specific"),
    ("随机对照", "randomized controlled trial", "specific"),
    ("随机试验", "randomized clinical trial", "specific"),
    ("意向治疗", "intention to treat population", "specific"),
    ("分析人群", "analysis population", "specific"),
    ("统计分析", "statistical analysis", "specific"),
    ("化疗", "chemotherapy", "specific"),
    ("剂量减少", "dose reduction", "specific"),
    ("治疗延迟", "treatment delay", "specific"),
    ("毒性", "toxicity adverse events", "specific"),
    ("闭环胰岛素", "closed loop insulin", "specific"),
    ("自适应闭环", "adaptive closed loop insulin", "specific"),
    ("闭环", "closed loop", "specific"),
    ("低血糖", "hypoglycaemia hypoglycemia", "specific"),
    ("48个月", "48 months insulin requirements closed loop", "specific"),
    ("胰岛素需求", "insulin requirements daily insulin dose", "specific"),
    ("儿童", "children adolescents type 1 diabetes", "specific"),
    ("青少年", "children adolescents type 1 diabetes", "specific"),
    ("1型糖尿病", "type 1 diabetes", "specific"),
    ("血糖", "glucose insulin diabetes", "specific"),
    ("证据", "evidence clinical trial", "generic"),
    ("研究", "clinical study", "generic"),
    ("试验", "clinical trial", "generic"),
]


def _contains_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text or ""))


def _dedupe_words(text: str) -> str:
    seen = set()
    words = []
    for word in re.findall(r"[A-Za-z0-9][A-Za-z0-9\-]*", text or ""):
        key = word.lower()
        if key not in seen:
            seen.add(key)
            words.append(word)
    return " ".join(words)


def _unique_queries(items: list[str]) -> list[str]:
    seen = set()
    queries = []
    for item in items:
        text = _dedupe_words(item)
        key = text.lower()
        if text and key not in seen:
            seen.add(key)
            queries.append(text)
    return queries


def _rewrite_query_for_retrieval(query: str) -> dict:
    original = (query or "").strip()
    ascii_terms = " ".join(re.findall(r"[A-Za-z0-9][A-Za-z0-9\-]*", original))
    matched = []
    for zh, en, kind in _ZH_RETRIEVAL_TERMS:
        pos = original.find(zh)
        if pos >= 0:
            matched.append({"source": zh, "rewrite": en, "kind": kind, "pos": pos})

    if not _contains_cjk(original):
        clean = _dedupe_words(ascii_terms or original)
        return {
            "original_query": original,
            "search_query": clean or original,
            "search_queries": [clean or original],
            "query_language": "en",
            "query_rewrites": [],
            "rewrite_method": "identity",
        }

    has_specific = any(item["kind"] == "specific" for item in matched)
    ordered_matches = sorted(
        (item for item in matched if item["kind"] == "specific" or not has_specific),
        key=lambda item: item["pos"],
    )
    english_parts = [item["rewrite"] for item in ordered_matches]
    if ascii_terms:
        english_parts.insert(0, ascii_terms)
    if not english_parts:
        english_parts.append("clinical trial outcome safety evidence")

    search_query = _dedupe_words(" ".join(english_parts))
    search_queries = _unique_queries([
        search_query,
        " ".join(item["rewrite"] for item in ordered_matches if item["source"] in {"主要终点", "次要终点", "终点", "安全性", "严重不良事件", "不良事件", "总生存", "总体生存", "无进展生存", "纳入排除", "纳入标准", "排除标准", "统计分析", "意向治疗", "分析人群"}),
        " ".join(item["rewrite"] for item in ordered_matches if item["source"] in {"化疗", "剂量减少", "治疗延迟", "毒性", "闭环胰岛素", "自适应闭环", "闭环", "低血糖", "48个月", "胰岛素需求", "儿童", "青少年", "1型糖尿病", "血糖"}),
    ])
    return {
        "original_query": original,
        "search_query": search_query,
        "search_queries": search_queries[:3] or [search_query],
        "query_language": "zh",
        "query_rewrites": [{"source": item["source"], "rewrite": item["rewrite"]} for item in ordered_matches],
        "rewrite_method": "rule_based_medical_terms",
    }


def _classify_question_profile(query: str) -> dict:
    text = (query or "").lower()
    categories = [
        (
            "endpoint_definition",
            ("终点定义", "如何定义", "怎么定义", "定义为", "endpoint definition", "defined as"),
            ["结论", "终点口径", "不可外推", "局限"],
            "说明研究如何定义终点，同时避免把终点口径解释为疗效结论。",
        ),
        (
            "survival_benefit_judgement",
            ("生存获益", "延长生存", "总生存", "无进展生存", "os", "pfs", "rpfs", "overall survival", "progression free"),
            ["结论", "终点定义", "获益判断", "局限"],
            "区分 OS/PFS 终点定义、统计分析和是否足以支持生存获益结论。",
        ),
        (
            "mechanism_explanation",
            ("为什么", "为何", "原因", "机制", "意义", "说明什么", "支持", "背后", "怎么解释", "如何解释", "why", "mechanism", "rationale"),
            ["结论", "机制解释", "适用边界", "安全声明"],
            "解释文献结论背后的机制或逻辑链条，同时明确证据边界。",
        ),
        (
            "safety_judgement",
            ("安全", "风险", "不良事件", "严重不良事件", "低血糖", "毒性", "adverse", "safety", "hypogly"),
            ["结论", "安全性发现", "适用边界", "安全声明"],
            "围绕安全性结局、不良事件和适用边界回答。",
        ),
        (
            "efficacy_judgement",
            ("主要终点", "次要终点", "疗效", "获益", "有效", "生存", "endpoint", "survival", "efficacy"),
            ["结论", "关键终点", "证据强度", "局限"],
            "围绕终点、疗效方向和证据强度回答。",
        ),
        (
            "population_applicability",
            ("人群", "纳入", "排除", "适用", "itt", "intention", "population", "inclusion", "exclusion"),
            ["结论", "研究人群", "外推边界", "局限"],
            "说明研究对象、纳排标准和结果可外推边界。",
        ),
        (
            "study_design",
            ("研究设计", "随机", "对照", "统计分析", "方法", "design", "randomized", "statistical"),
            ["结论", "设计要点", "统计口径", "局限"],
            "解释研究设计、统计口径和方法学边界。",
        ),
    ]
    for question_type, triggers, strategy, instruction in categories:
        if any(token in text for token in triggers):
            return {
                "question_type": question_type,
                "answer_strategy": strategy,
                "strategy_instruction": instruction,
            }
    return {
        "question_type": "evidence_summary",
        "answer_strategy": ["结论", "关键证据", "适用边界", "局限"],
        "strategy_instruction": "汇总检索证据中的直接结论，并明确不能外推的部分。",
    }


def _evidence_role(item: dict) -> str:
    blob = " ".join(
        str(item.get(key) or "").lower()
        for key in ("medical_label", "medical_parent", "source_section", "text", "text_preview")
    )
    if any(token in blob for token in ("defined as", "definition", "endpoint was", "endpoint is", "duration from", "time from")):
        return "endpoint_definition"
    if any(token in blob for token in ("overall survival", "progression-free", "progression free", "kaplan", "hazard ratio", "median survival")):
        return "survival_outcome"
    if any(token in blob for token in ("adverse", "safety", "hypogly", "toxicity")):
        return "safety"
    if any(token in blob for token in ("primary", "secondary", "outcome", "endpoint")):
        return "endpoint"
    if any(token in blob for token in ("population", "eligibility", "inclusion", "exclusion", "itt")):
        return "population"
    if any(token in blob for token in ("intervention", "dose", "treatment")):
        return "intervention"
    if any(token in blob for token in ("statistical", "analysis", "method", "random")):
        return "method"
    return "context"


def _is_survival_endpoint_question(query: str) -> bool:
    text = (query or "").lower()
    return any(token in text or token in query for token in ["os", "pfs", "rpfs", "总生存", "无进展", "生存获益", "延长生存", "overall survival", "progression free"])


def _support_level_for_card(role: str, question_type: str, text: str) -> tuple[str, str]:
    blob = (text or "").lower()
    direct_roles = {
        "endpoint_definition": {"endpoint_definition", "endpoint", "survival_outcome"},
        "survival_benefit_judgement": {"survival_outcome", "endpoint_definition", "method", "population"},
        "safety_judgement": {"safety", "endpoint"},
        "mechanism_explanation": {"safety", "intervention", "survival_outcome", "endpoint_definition", "context"},
        "population_applicability": {"population", "method"},
        "study_design": {"method", "population", "endpoint"},
        "efficacy_judgement": {"survival_outcome", "endpoint", "method", "population"},
    }
    if role in direct_roles.get(question_type, set()):
        return "direct", "与问题类型直接匹配"
    if any(token in blob for token in ("secondary endpoint", "primary endpoint", "statistical analysis", "intention-to-treat")):
        return "supporting", "可支持统计或终点边界"
    return "context", "仅作背景，不能单独支撑结论"


def _build_evidence_cards(evidence_items: list[dict], question_profile: dict | None = None) -> list[dict]:
    cards = []
    question_type = (question_profile or {}).get("question_type", "evidence_summary")
    for idx, item in enumerate(evidence_items, start=1):
        text = item.get("text") or item.get("text_preview") or ""
        role = _evidence_role(item)
        support_level, support_reason = _support_level_for_card(role, question_type, text)
        cards.append(
            {
                "card_id": f"E{idx}",
                "chunk_id": item.get("chunk_id", ""),
                "source_file": item.get("source_file", "unknown"),
                "section": item.get("source_section") or "-",
                "label": item.get("medical_label") or item.get("medical_parent") or "-",
                "role": role,
                "support_level": support_level,
                "support_reason": support_reason,
                "score": round(float(item.get("rrf_score") or item.get("_rrf_score") or 0.0), 6),
                "key_text": (text or "")[:260].replace("\n", " "),
            }
        )
    return cards


def _build_rag_prompt(
    query: str,
    evidence_items: list[dict],
    search_query: str | None = None,
    question_profile: dict | None = None,
    evidence_cards: list[dict] | None = None,
) -> list[dict]:
    question_profile = question_profile or _classify_question_profile(query)
    evidence_cards = evidence_cards or _build_evidence_cards(evidence_items, question_profile)
    evidence_blocks = []
    for item in evidence_items:
        text = item.get("text") or item.get("text_preview") or ""
        evidence_blocks.append(
            "\n".join(
                [
                    f"[{item.get('chunk_id')}]",
                    f"section: {item.get('source_section') or '-'}",
                    f"label: {item.get('medical_parent') or '-'} / {item.get('medical_label') or '-'}",
                    f"evidence: {text[:1800]}",
                ]
            )
        )

    system = (
        "你是一个本地运行的医学文献 RAG 合成器。"
        "只能依据提供的 evidence chunks 作答，不得使用外部知识或编造医学结论。"
        "如果证据不足，必须拒答。"
        "输出必须是 JSON，不要输出 markdown。"
    )
    strategy_text = " -> ".join(question_profile.get("answer_strategy") or [])
    card_lines = [
        f"{card['card_id']} | {card['chunk_id']} | role={card['role']} | label={card['label']} | {card['key_text']}"
        for card in evidence_cards
    ]
    explanation_mode = question_profile.get("question_type") == "mechanism_explanation" or _is_mechanism_question(query)
    explanation_line = (
        "\n本问题属于机制解释/原因解释型问题。回答时必须先给出文献支持的结论，再解释可能机制或逻辑链条；"
        "不得只复述用户问题或证据原句。如果证据只能支持结论、不能支持机制，必须明确写出机制证据不足。\n"
        if explanation_mode
        else ""
    )
    survival_endpoint_line = (
        "\n本问题涉及 OS/PFS/rPFS、生存获益或终点判断。回答时必须区分："
        "1）单篇研究中 OS/PFS 的 endpoint definition；2）该终点是否足以支持治疗带来生存获益的 clinical conclusion。"
        "不得把某一篇研究的起算日期、事件定义或影像学进展规则泛化为所有研究的通用定义；"
        "不得把“报告了 OS/PFS”写成“已经证明延长生存”。如来源只支持终点口径，必须明确说明这只是研究定义，不是获益结论。\n"
        if any(token in query.lower() or token in query for token in ["os", "pfs", "rPFS", "rpfs", "总生存", "无进展", "生存获益", "影像学进展"])
        else ""
    )
    search_line = f"\n英文检索词：\n{search_query}\n" if search_query and search_query != query else ""
    user = f"""用户问题：
{query}
{search_line}
{explanation_line}
{survival_endpoint_line}

问题类型：
{question_profile.get('question_type')}

回答策略：
{strategy_text}

结构化证据卡：
{chr(10).join(card_lines)}

本地检索证据：
{chr(10).join(evidence_blocks)}

请输出 JSON，字段如下：
{{
  "answer": "中文回答。必须引用 chunk_id，例如 [PMCxxx_chunk_001]。",
  "question_type": "{question_profile.get('question_type')}",
  "answer_strategy": {json.dumps(question_profile.get("answer_strategy") or [], ensure_ascii=False)},
  "citations": ["chunk_id"],
  "claims": [
    {{"claim": "可由证据支持的中文结论。", "citations": ["chunk_id"], "supported": true}}
  ],
  "reasoning_trace": [
    {{"step": "识别问题类型/匹配证据卡/组织回答", "citations": ["chunk_id"], "status": "supported"}}
  ],
  "confidence": "high|medium|low",
  "limitations": "证据局限。",
  "abstain": false,
  "abstain_reason": ""
}}

规则：
1. 只允许引用上面出现的 chunk_id。
2. 每个事实性结论必须写入 claims，并给出支撑它的 chunk_id。
3. 如果某个结论没有证据支撑，supported=false 且 citations=[]。
4. 如果证据不能支持回答，answer 写“当前本地知识库证据不足，无法回答该问题。”，abstain=true。
5. 不提供诊疗建议，不替代医生判断。
6. 对“为什么/机制/原因/意义/支持使用”类问题，answer 按“结论、机制解释、适用边界、安全声明”组织；机制解释只能来自 evidence，不能用外部常识补全。
7. 对 OS/PFS/rPFS/生存获益类问题，必须先写清“终点定义”和“获益结论”的区别；若只检索到单篇研究定义，只能回答“该研究如何定义终点”，不能推导疗效获益。
8. reasoning_trace 只记录可由 evidence 支撑的步骤，不输出隐藏推理，不得包含未引用的医学断言。
"""
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def _is_mechanism_question(query: str) -> bool:
    text = query or ""
    triggers = [
        "为什么",
        "为何",
        "原因",
        "机制",
        "意义",
        "说明什么",
        "支持",
        "背后",
        "怎么解释",
        "如何解释",
        "why",
        "mechanism",
        "rationale",
    ]
    return any(token.lower() in text.lower() for token in triggers)


def _extract_json_object(text: str) -> dict:
    try:
        return json.loads(text)
    except Exception:
        pass

    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        try:
            return json.loads(text[start : end + 1])
        except Exception:
            return {}
    return {}


def _tokenize_query(text: str) -> set[str]:
    return {token.lower() for token in re.findall(r"[A-Za-z0-9_\-]{3,}", text or "")}


def _score_evidence_sufficiency(query: str, evidence_items: list[dict]) -> dict:
    query_terms = _tokenize_query(query)
    evidence_terms = _tokenize_query(" ".join((item.get("text") or item.get("text_preview") or "") for item in evidence_items))
    matched = sorted(query_terms & evidence_terms)
    max_rrf = max((float(item.get("rrf_score") or 0.0) for item in evidence_items), default=0.0)
    has_evidence = bool(evidence_items)
    sufficient = has_evidence and (not query_terms or len(matched) >= min(2, len(query_terms)) or max_rrf > 0)
    return {
        "sufficient": sufficient,
        "query_terms": sorted(query_terms)[:20],
        "matched_terms": matched[:20],
        "matched_term_count": len(matched),
        "top_rrf_score": max_rrf,
        "evidence_count": len(evidence_items),
    }


def _call_local_ollama_chat(model: str, messages: list[dict], timeout: float = 180.0) -> tuple[dict, dict]:
    import httpx

    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "think": False,
        "format": "json",
        "options": {
            "temperature": 0.1,
            "top_p": 0.8,
            "num_predict": 1200,
        },
        "keep_alive": "10m",
    }
    try:
        response = httpx.post(
            f"{get_settings().ollama_base_url}/api/chat",
            json=payload,
            timeout=timeout,
            trust_env=False,
        )
        response.raise_for_status()
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail={
                "error": f"本地 Ollama 生成失败: {e}",
                "model": model,
                "privacy": "local_only",
            },
        )

    data = response.json()
    content = (data.get("message") or {}).get("content") or data.get("response") or ""
    parsed = _extract_json_object(content)
    if not parsed:
        parsed = {
            "answer": content.strip() or "本地模型未返回有效回答。",
            "citations": [],
            "confidence": "low",
            "limitations": "模型未按 JSON 结构输出，已保存原始回答。",
            "abstain": False,
            "abstain_reason": "",
        }
    return parsed, data


def _normalize_claims(raw: dict, evidence_items: list[dict]) -> tuple[list[dict], dict]:
    allowed = {item["chunk_id"] for item in evidence_items if item.get("chunk_id")}
    claims = []
    raw_claims = raw.get("claims")
    if not isinstance(raw_claims, list):
        raw_claims = []

    for entry in raw_claims:
        if not isinstance(entry, dict):
            continue
        claim = str(entry.get("claim") or "").strip()
        if not claim:
            continue
        claim_citations = [c for c in entry.get("citations", []) if c in allowed]
        supported = bool(entry.get("supported", False)) and bool(claim_citations)
        claims.append(
            {
                "claim": claim,
                "citations": claim_citations,
                "supported": supported,
            }
        )

    if not claims:
        answer = str(raw.get("answer") or "").strip()
        raw_citations = [c for c in raw.get("citations", []) if c in allowed]
        if answer:
            claims.append(
                {
                    "claim": answer,
                    "citations": raw_citations,
                    "supported": bool(raw_citations) and not bool(raw.get("abstain", False)),
                }
            )

    supported_count = sum(1 for claim in claims if claim["supported"])
    unsupported_count = len(claims) - supported_count
    coverage = supported_count / len(claims) if claims else 0.0
    return claims, {
        "claim_count": len(claims),
        "supported_claims": supported_count,
        "unsupported_claims": unsupported_count,
        "citation_coverage": round(coverage, 4),
    }


def _normalize_reasoning_trace(raw: dict, evidence_items: list[dict]) -> list[dict]:
    allowed = {item["chunk_id"] for item in evidence_items if item.get("chunk_id")}
    raw_steps = raw.get("reasoning_trace")
    if not isinstance(raw_steps, list):
        raw_steps = []

    trace = []
    for idx, entry in enumerate(raw_steps[:6], start=1):
        if not isinstance(entry, dict):
            continue
        citations = [c for c in entry.get("citations", []) if c in allowed]
        step = str(entry.get("step") or "").strip()
        if not step:
            continue
        status = str(entry.get("status") or ("supported" if citations else "unsupported")).lower()
        if status not in {"supported", "unsupported", "partial"}:
            status = "supported" if citations else "unsupported"
        trace.append({"step": step, "citations": citations, "status": status})

    if not trace and evidence_items:
        trace.append(
            {
                "step": "检索到本地证据并按问题类型组织回答",
                "citations": [item["chunk_id"] for item in evidence_items[:2] if item.get("chunk_id")],
                "status": "supported",
            }
        )
    return trace


def _review_rag_answer(
    query: str,
    raw: dict,
    evidence_items: list[dict],
    claims: list[dict],
    question_profile: dict,
    evidence_cards: list[dict],
) -> dict:
    answer = str(raw.get("answer") or "")
    question_type = question_profile.get("question_type", "evidence_summary")
    issues = []
    passed = []

    allowed = {item["chunk_id"] for item in evidence_items if item.get("chunk_id")}
    cited = {c for claim in claims for c in claim.get("citations", [])}
    if cited and cited <= allowed:
        passed.append("所有 claim 引用均来自本轮检索来源")
    else:
        issues.append("存在未引用或引用覆盖不足的 claim")

    direct_cards = [card for card in evidence_cards if card.get("support_level") == "direct"]
    if direct_cards:
        passed.append(f"命中 {len(direct_cards)} 张直接来源卡")
    else:
        issues.append("未命中直接来源卡，回答应降级为依据不足或背景说明")

    unsupported = [claim for claim in claims if not claim.get("supported")]
    if unsupported:
        issues.append(f"{len(unsupported)} 条 claim 未被来源支撑")
    else:
        passed.append("claim-level 支撑检查通过")

    if _is_survival_endpoint_question(query) or question_type in {"endpoint_definition", "survival_benefit_judgement"}:
        has_definition_boundary = any(token in answer for token in ("终点定义", "终点口径", "定义"))
        has_conclusion_boundary = any(token in answer for token in ("不等于", "不等同", "不能自动", "不是", "不足以", "不能推导", "无法直接推导", "不能外推", "不能将", "不能仅因", "并非直接"))
        if has_definition_boundary and has_conclusion_boundary:
            passed.append("OS/PFS 终点定义与获益结论边界已写明")
        else:
            issues.append("OS/PFS 类问题缺少“终点定义 vs 获益结论”的边界")
        if (
            re.search(r"(?<!已)(证明|证实|显著).{0,12}(延长|改善).{0,12}(生存|OS|PFS)", answer, flags=re.IGNORECASE)
            and not has_conclusion_boundary
        ):
            issues.append("疑似把终点报告泛化为生存获益结论")

    personal_advice_pattern = re.compile(
        r"(你|您|患者|本人).{0,16}(应该|建议|需要|可以).{0,16}(吃|服用|使用|调整|加量|减量|停药|剂量|治疗)"
        r"|(?:应该|建议).{0,12}(吃什么药|服用|用药|剂量|治疗方案)"
        r"|(?:take|use|increase|decrease|stop).{0,16}(medicine|drug|dose|dosage)",
        flags=re.IGNORECASE,
    )
    if personal_advice_pattern.search(answer):
        issues.append("回答中疑似包含个人诊疗或用药建议")
    else:
        passed.append("未发现个人诊疗建议")

    return {
        "status": "needs_review" if issues else "passed",
        "passed": passed,
        "issues": issues,
        "direct_source_cards": [card["card_id"] for card in direct_cards],
        "question_type": question_type,
    }


def _normalize_rag_answer(
    raw: dict,
    evidence_items: list[dict],
    question_profile: dict | None = None,
    evidence_cards: list[dict] | None = None,
    original_query: str | None = None,
) -> dict:
    allowed = {item["chunk_id"] for item in evidence_items if item.get("chunk_id")}
    citations = [c for c in raw.get("citations", []) if c in allowed]
    answer = str(raw.get("answer") or "").strip()
    abstain = bool(raw.get("abstain", False))
    claims, claim_stats = _normalize_claims(raw, evidence_items)
    reasoning_trace = _normalize_reasoning_trace(raw, evidence_items)
    evidence_sufficiency = _score_evidence_sufficiency(raw.get("query", ""), evidence_items)
    question_profile = question_profile or _classify_question_profile(original_query or raw.get("original_query") or raw.get("query") or "")
    evidence_cards = evidence_cards or _build_evidence_cards(evidence_items, question_profile)
    answer_audit = _review_rag_answer(original_query or raw.get("original_query") or raw.get("query") or "", raw, evidence_items, claims, question_profile, evidence_cards)
    if not evidence_items:
        abstain = True
    if claim_stats["claim_count"] and claim_stats["supported_claims"] == 0:
        abstain = True
    if answer_audit["status"] != "passed" and not citations:
        abstain = True
    if abstain and not answer:
        answer = "当前本地知识库证据不足，无法回答该问题。"
    if not citations and claims:
        citations = sorted({c for claim in claims for c in claim.get("citations", [])})
    if not citations and not abstain:
        citations = [item["chunk_id"] for item in evidence_items[:2] if item.get("chunk_id")]

    confidence = str(raw.get("confidence") or "medium").lower()
    if confidence not in {"high", "medium", "low"}:
        confidence = "medium"
    if abstain or claim_stats["citation_coverage"] < 0.5:
        confidence = "low"

    return {
        "answer": answer or "当前本地知识库证据不足，无法回答该问题。",
        "citations": citations,
        "claims": claims,
        "reasoning_trace": reasoning_trace,
        "claim_count": claim_stats["claim_count"],
        "supported_claims": claim_stats["supported_claims"],
        "unsupported_claims": claim_stats["unsupported_claims"],
        "citation_coverage": claim_stats["citation_coverage"],
        "evidence_sufficiency": evidence_sufficiency,
        "confidence": confidence,
        "limitations": str(raw.get("limitations") or "仅基于当前本地医学文献知识库检索结果，不构成诊疗建议。"),
        "abstain": abstain,
        "abstain_reason": str(raw.get("abstain_reason") or ("证据不足" if abstain else "")),
        "answer_audit": answer_audit,
    }


_EMERGENCY_TERMS = (
    "胸痛", "呼吸困难", "喘不上气", "昏迷", "休克", "抽搐", "大出血", "自杀", "轻生",
    "overdose", "chest pain", "shortness of breath", "suicide", "stroke", "seizure",
)
_PERSONAL_ADVICE_TERMS = (
    "我", "我的", "本人", "孩子", "老人", "孕妇", "症状", "发烧", "疼", "痛", "吃什么药",
    "用药", "剂量", "怎么办", "要不要去医院", "能不能吃", "诊断", "治疗方案",
    "my ", "i ", "symptom", "diagnose", "dosage", "medicine", "should i",
)
_HARD_PERSONAL_ADVICE_TERMS = (
    "吃什么药", "用药", "剂量", "要不要去医院", "能不能吃", "诊断", "治疗方案",
    "应该吃", "该吃", "处方", "dosage", "medicine", "should i", "diagnose",
)
_EVIDENCE_TERMS = (
    "文献", "研究", "试验", "证据", "endpoint", "primary", "secondary", "adverse",
    "survival", "kaplan", "clinical trial", "randomized", "outcome", "safety",
    "intention to treat", "intention-to-treat",
)
_GENERIC_FOLLOWUP_TERMS = (
    "更多信息", "详细一点", "展开", "继续说", "多说一点", "再解释", "什么意思",
    "more information", "tell me more", "explain more",
)


def _triage_medical_question(question: str, history: list[dict] | None = None, model: str | None = None) -> dict:
    text = (question or "").strip()
    lowered = f" {text.lower()} "
    emergency_hits = [term for term in _EMERGENCY_TERMS if term in lowered or term in text]
    personal_hits = [term for term in _PERSONAL_ADVICE_TERMS if term in lowered or term in text]
    hard_personal_hits = [term for term in _HARD_PERSONAL_ADVICE_TERMS if term in lowered or term in text]
    evidence_hits = [term for term in _EVIDENCE_TERMS if term in lowered or term in text]
    followup_hits = [term for term in _GENERIC_FOLLOWUP_TERMS if term in lowered or term in text]
    has_history = bool(history)

    if emergency_hits:
        return {
            "category": "urgent_or_emergency",
            "risk_level": "high",
            "allow_rag": False,
            "matched_terms": emergency_hits[:6],
            "user_message": "该问题可能涉及急症或高风险情况。请立即联系当地急救服务或前往急诊，本系统不能处理紧急医疗处置。",
        }
    if followup_hits and has_history:
        return {
            "category": "followup",
            "risk_level": "low",
            "allow_rag": True,
            "matched_terms": followup_hits[:6],
            "user_message": "该问题像是上一轮文献证据问答的追问；若上下文不足，请补充具体医学文献问题。",
            "triage_source": "rule_followup",
        }
    if evidence_hits:
        return {
            "category": "medical_evidence_question",
            "risk_level": "low",
            "allow_rag": True,
            "matched_terms": evidence_hits[:6],
            "user_message": "将基于平台预构建、已审核的本地 PMC 医学证据库回答。",
            "triage_source": "rule_evidence",
        }

    ollama_triage = _triage_with_local_ollama(text, history or [], model=model)
    if ollama_triage:
        return ollama_triage

    if hard_personal_hits and personal_hits and not evidence_hits:
        return {
            "category": "personal_medical_advice",
            "risk_level": "medium",
            "allow_rag": False,
            "matched_terms": (hard_personal_hits + personal_hits)[:6],
            "user_message": "该问题看起来像个人诊疗或用药建议。当前系统只提供基于已审核医学文献库的证据问答，不替代医生诊断、处方或急诊判断。",
            "triage_source": "fallback_hard_rule",
        }

    if personal_hits:
        return {
            "category": "personal_medical_advice",
            "risk_level": "medium",
            "allow_rag": False,
            "matched_terms": personal_hits[:6],
            "user_message": "该问题可能涉及个人诊疗或用药建议。当前系统只提供基于已审核医学文献库的证据问答，不替代医生诊断、处方或急诊判断。",
            "triage_source": "fallback_rule",
        }
    return {
        "category": "medical_evidence_question" if evidence_hits else "general_medical_question",
        "risk_level": "low" if evidence_hits else "medium",
        "allow_rag": True,
        "matched_terms": evidence_hits[:6],
        "user_message": "将基于平台预构建、已审核的本地 PMC 医学证据库回答。",
        "triage_source": "fallback_rule",
    }


def _triage_with_local_ollama(question: str, history: list[dict], model: str | None = None) -> dict | None:
    import httpx

    triage_model = (model or os.environ.get("CONTROLMIND_TRIAGE_MODEL") or os.environ.get("CONTROLSCI_TRIAGE_MODEL") or "qwen3.5:9b").strip()
    if triage_model.lower() in {"", "off", "none", "rule", "rules"}:
        return None

    history_summary = []
    for item in (history or [])[-4:]:
        role = str(item.get("role") or "")[:20]
        content = str(item.get("content") or item.get("answer") or "")[:240]
        if role and content:
            history_summary.append({"role": role, "content": content})

    system = (
        "你是医学文献问答系统的本地安全分诊器，只做意图分类，不回答医学问题。"
        "请只输出 JSON，不要输出多余文字。分类必须保守但不要误伤普通追问。"
        "类别只能是: medical_evidence_question, followup, personal_medical_advice, urgent_or_emergency, unclear。"
        "allow_rag 只有在问题是文献证据问题或有上下文的证据追问时才为 true。"
    )
    user = {
        "question": question,
        "recent_history": history_summary,
        "output_schema": {
            "category": "medical_evidence_question|followup|personal_medical_advice|urgent_or_emergency|unclear",
            "risk_level": "low|medium|high",
            "allow_rag": True,
            "need_context": False,
            "reason": "短中文理由",
            "user_message": "给用户看的短提示",
        },
        "examples": [
            {"question": "能给我更多信息吗？", "with_history": True, "category": "followup", "allow_rag": True},
            {"question": "能给我更多信息吗？", "with_history": False, "category": "unclear", "allow_rag": False},
            {"question": "我发烧了应该吃什么药", "category": "personal_medical_advice", "allow_rag": False},
            {"question": "主要终点和安全性证据", "category": "medical_evidence_question", "allow_rag": True},
        ],
    }
    payload = {
        "model": triage_model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(user, ensure_ascii=False)},
        ],
        "stream": False,
        "think": False,
        "format": "json",
        "options": {"temperature": 0, "num_predict": 220},
        "keep_alive": "10m",
    }
    try:
        response = httpx.post(
            f"{get_settings().ollama_base_url}/api/chat",
            json=payload,
            timeout=12,
            trust_env=False,
        )
        response.raise_for_status()
        data = response.json()
        content = (data.get("message") or {}).get("content") or data.get("response") or ""
        parsed = _extract_json_object(content)
    except Exception:
        return None

    category = str(parsed.get("category") or "unclear")
    if category not in {"medical_evidence_question", "followup", "personal_medical_advice", "urgent_or_emergency", "unclear"}:
        return None
    risk_level = str(parsed.get("risk_level") or ("high" if category == "urgent_or_emergency" else "medium"))
    allow_rag = bool(parsed.get("allow_rag")) and category in {"medical_evidence_question", "followup"}
    if category == "followup" and not history:
        category = "unclear"
        allow_rag = False
    if category == "urgent_or_emergency":
        allow_rag = False
        risk_level = "high"
    if category == "personal_medical_advice":
        allow_rag = False
    default_messages = {
        "medical_evidence_question": "将基于平台预构建、已审核的本地 PMC 医学证据库回答。",
        "followup": "将结合上一轮文献证据回答继续说明。",
        "personal_medical_advice": "该问题看起来像个人诊疗或用药建议。当前系统只提供基于已审核医学文献库的证据问答，不替代医生诊断、处方或急诊判断。",
        "urgent_or_emergency": "该问题可能涉及急症或高风险情况。请立即联系当地急救服务或前往急诊，本系统不能处理紧急医疗处置。",
        "unclear": "请补充一个具体的医学文献证据问题，例如研究终点、安全性证据或分析人群。",
    }
    return {
        "category": category,
        "risk_level": risk_level if risk_level in {"low", "medium", "high"} else "medium",
        "allow_rag": allow_rag,
        "matched_terms": [],
        "user_message": str(parsed.get("user_message") or default_messages[category])[:240],
        "need_context": bool(parsed.get("need_context")),
        "reason": str(parsed.get("reason") or "")[:240],
        "triage_source": f"local_ollama:{triage_model}",
    }


def _safety_refusal(question: str, triage: dict, session_id: str | None = None) -> dict:
    payload = {
        "session_id": session_id or uuid.uuid4().hex[:10],
        "question": question,
        "answer": triage["user_message"],
        "status": "safety_refusal",
        "model": "safety_triage",
        "retrieval_mode": "none",
        "retrieval_index": {},
        "privacy": "local_only",
        "citations": [],
        "claims": [],
        "claim_count": 0,
        "supported_claims": 0,
        "unsupported_claims": 0,
        "citation_coverage": 0.0,
        "evidence_sufficiency": {"sufficient": False, "reason": triage["category"]},
        "confidence": "low",
        "limitations": "安全分诊命中后未执行医学文献检索；请改问医学文献证据问题，或咨询合格医生。",
        "abstain": True,
        "abstain_reason": triage["category"],
        "evidence_items": [],
        "source_summary": {"total_sources": 0, "total_chunks": 0, "sources": []},
        "task_id": "",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "safety_triage": triage,
        "audit": {
            "interface": "medical_rag_ask",
            "prompt_policy": "safety_triage_no_retrieval",
            "raw_medical_context_sent_to_cloud": False,
        },
    }
    _append_rag_trace(payload)
    return payload


def _append_rag_trace(payload: dict) -> None:
    TRACE_JSONL.parent.mkdir(parents=True, exist_ok=True)
    trace = {
        "trace_id": payload.get("task_id") or payload.get("session_id") or uuid.uuid4().hex[:12],
        "generated_at": payload.get("generated_at") or datetime.now(timezone.utc).isoformat(),
        "status": payload.get("status"),
        "question": payload.get("query") or payload.get("question"),
        "question_type": payload.get("question_type") or (payload.get("audit") or {}).get("question_type"),
        "retrieval_mode": payload.get("retrieval_mode"),
        "index_id": (payload.get("retrieval_index") or {}).get("alias"),
        "privacy": payload.get("privacy"),
        "search_query": payload.get("search_query"),
        "search_queries": payload.get("search_queries") or [],
        "citations": payload.get("citations") or [],
        "claim_count": payload.get("claim_count", 0),
        "supported_claims": payload.get("supported_claims", 0),
        "citation_coverage": payload.get("citation_coverage", 0.0),
        "abstain": payload.get("abstain", False),
        "abstain_reason": payload.get("abstain_reason", ""),
        "answer_audit": payload.get("answer_audit") or {},
        "safety_triage": payload.get("safety_triage") or {},
        "source_summary": payload.get("source_summary") or {},
        "audit": payload.get("audit") or {},
    }
    with open(TRACE_JSONL, "a", encoding="utf-8") as f:
        f.write(json.dumps(trace, ensure_ascii=False) + "\n")


@app.get("/api/health", response_model=HealthResponse)
def health():
    manifest_path = _find_manifest()
    index_issues = _check_index_issues()

    dense_ok = _dense_path().exists()
    sparse_ok = _sparse_path().exists()
    public_evidence_ok = _public_medical_evidence_ok()

    issues = [_safe_issue(issue) for issue in index_issues]
    if not manifest_path:
        issues.append("chunks manifest 未找到")

    if dense_ok and sparse_ok and manifest_path:
        status = "ok"
    elif public_evidence_ok:
        status = "public_evidence"
        issues = []
    else:
        status = "degraded"

    return {
        "status": status,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "profile": _api_profile(),
        "components": {
            "privacy_boundary": {
                "cloud_demo": _is_cloud_demo(),
                "text_full_exposed": (not _is_cloud_demo()) and not public_evidence_ok,
                "source_paths_exposed": (not _is_cloud_demo()) and not public_evidence_ok,
                "data_root": _safe_source_file(str(_medical_root())),
            },
            "faiss_index": {
                "available": dense_ok,
                "size_kb": _safe_file_size_kb(_dense_path()) if dense_ok else 0,
            },
            "bm25_index": {
                "available": sparse_ok,
                "size_kb": _safe_file_size_kb(_sparse_path()) if sparse_ok else 0,
            },
            "chunks_manifest": {
                "available": manifest_path is not None,
                "path": _safe_source_file(str(manifest_path)) if manifest_path else None,
            },
            "public_evidence_bundle": {
                "available": public_evidence_ok,
                "path": "docs/submissions/data_trace_bundle/09_medical_rag",
            },
            "retrieval_indexes": _available_indexes(),
        },
        "issues": issues,
    }


@app.get("/api/evidence/search", response_model=SearchResponse)
def search(
    q: str = Query(..., description="临床查询文本 (如 'primary endpoint', 'adverse events')"),
    k: int = Query(default=5, ge=1, le=20, description="返回 top-k 结果"),
    mode: str = Query(default="hybrid", pattern="^(dense|bm25|hybrid|vision)$", description="检索模式"),
    vision: bool = Query(default=False, description="启用视觉通道（双通道 RRF 融合）"),
    index_id: str = Query(default="qwen", description="检索索引: qwen | bge_small | bge_m3"),
):
    _require_index(index_id)
    manifest = _require_manifest()
    query_info = _rewrite_query_for_retrieval(q)

    try:
        selected_mode = "vision" if vision else mode
        results, vision_enabled = _search_multi_query(query_info, k, manifest, selected_mode, index_id=index_id)
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=f"索引文件缺失: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"检索失败: {e}")

    formatted = [_format_search_result(r, i + 1) if not r.get("is_vision") else _format_vision_result(r, i + 1) for i, r in enumerate(results)]
    return {
        "query": q,
        "search_query": query_info["search_query"],
        "search_queries": query_info["search_queries"],
        "query_language": query_info["query_language"],
        "query_rewrites": query_info["query_rewrites"],
        "rewrite_method": query_info["rewrite_method"],
        "top_k": k,
        "mode": selected_mode,
        "vision_enabled": vision_enabled,
        "count": len(formatted),
        "results": formatted,
    }


@app.post("/api/evidence/synthesize")
def synthesize(req: SynthesizeRequest):
    _require_index(req.index_id)
    manifest = _require_manifest()
    model = _clean_model_choice(req.synthesis_model)
    query_info = _rewrite_query_for_retrieval(req.query)

    try:
        top_k = min(max(req.k, 1), 10)
        mode = req.mode if req.mode in {"dense", "bm25", "hybrid", "vision"} else "hybrid"
        results, vision_enabled = _search_multi_query(query_info, top_k, manifest, mode, index_id=req.index_id)
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=f"索引文件缺失: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"检索失败: {e}")

    task_id = uuid.uuid4().hex[:12]
    timestamp = datetime.now(timezone.utc).isoformat()

    evidence_items = []
    source_map = {}
    for r in results:
        text = r.get("text", "")
        chunk_id = r.get("chunk_id", "")
        source_file = Path(r.get("filepath", "")).stem if r.get("filepath") else "unknown"

        if source_file not in source_map:
            source_map[source_file] = []
        source_map[source_file].append(chunk_id)

        evidence_items.append(
            {
                "chunk_id": chunk_id,
                "source_file": _safe_source_file(source_file),
                "source_section": r.get("source_section", ""),
                "medical_label": r.get("medical_label", ""),
                "medical_parent": r.get("medical_parent"),
                "rrf_score": r.get("_rrf_score", 0.0),
                "text": _exposed_text(text),
                "prompt_text": text[:1800],
                "text_preview": _preview_text(text),
            }
        )

    sources = [{"file": k, "chunk_count": len(v), "chunk_ids": v} for k, v in source_map.items()]
    retrieval_index = _index_meta(req.index_id)
    prompt_items = [{**item, "text": item.get("prompt_text", "")} for item in evidence_items]
    question_profile = _classify_question_profile(req.query)
    evidence_cards = _build_evidence_cards(prompt_items, question_profile)
    messages = _build_rag_prompt(req.query, prompt_items, query_info["search_query"], question_profile, evidence_cards)
    rag_raw, ollama_meta = _call_local_ollama_chat(model, messages)
    rag_raw["query"] = query_info["search_query"]
    rag_raw["original_query"] = req.query
    rag_answer = _normalize_rag_answer(
        rag_raw,
        evidence_items,
        question_profile=question_profile,
        evidence_cards=evidence_cards,
        original_query=req.query,
    )

    for item in evidence_items:
        item.pop("prompt_text", None)

    synthesis_report = {
        "task_id": task_id,
        "status": "local_rag",
        "query": req.query,
        "search_query": query_info["search_query"],
        "search_queries": query_info["search_queries"],
        "query_language": query_info["query_language"],
        "query_rewrites": query_info["query_rewrites"],
        "rewrite_method": query_info["rewrite_method"],
        "generated_at": timestamp,
        "model": model,
        "retrieval_mode": mode,
        "retrieval_index": retrieval_index,
        "vision_enabled": vision_enabled,
        "privacy": "local_only",
        "rag_mode": "evidence_structured",
        "question_type": question_profile["question_type"],
        "answer_strategy": question_profile["answer_strategy"],
        "strategy_instruction": question_profile["strategy_instruction"],
        "evidence_cards": evidence_cards,
        "answer": rag_answer["answer"],
        "citations": rag_answer["citations"],
        "claims": rag_answer["claims"],
        "reasoning_trace": rag_answer["reasoning_trace"],
        "claim_count": rag_answer["claim_count"],
        "supported_claims": rag_answer["supported_claims"],
        "unsupported_claims": rag_answer["unsupported_claims"],
        "citation_coverage": rag_answer["citation_coverage"],
        "evidence_sufficiency": rag_answer["evidence_sufficiency"],
        "answer_audit": rag_answer["answer_audit"],
        "confidence": rag_answer["confidence"],
        "limitations": rag_answer["limitations"],
        "abstain": rag_answer["abstain"],
        "abstain_reason": rag_answer["abstain_reason"],
        "evidence_items": evidence_items,
        "source_summary": {
            "total_sources": len(sources),
            "total_chunks": len(evidence_items),
            "sources": sources,
        },
        "audit": {
            "prompt_policy": "local_only_evidence_structured_rag_json",
            "rag_mode": "evidence_structured",
            "raw_medical_context_sent_to_cloud": False,
            "question_type": question_profile["question_type"],
            "answer_strategy": question_profile["answer_strategy"],
            "evidence_cards": len(evidence_cards),
            "original_query": req.query,
            "search_query": query_info["search_query"],
            "search_queries": query_info["search_queries"],
            "query_language": query_info["query_language"],
            "rewrite_method": query_info["rewrite_method"],
            "retrieval_index": retrieval_index,
            "claim_count": rag_answer["claim_count"],
            "citation_coverage": rag_answer["citation_coverage"],
            "evidence_sufficiency": rag_answer["evidence_sufficiency"],
            "answer_audit_status": rag_answer["answer_audit"]["status"],
            "answer_audit_issues": rag_answer["answer_audit"]["issues"],
            "ollama_model": ollama_meta.get("model", model),
            "prompt_eval_count": ollama_meta.get("prompt_eval_count"),
            "eval_count": ollama_meta.get("eval_count"),
            "total_duration_ns": ollama_meta.get("total_duration"),
        },
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"{task_id}.json"
    tmp_path = str(report_path) + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(synthesis_report, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, str(report_path))
    _append_rag_trace(synthesis_report)

    return synthesis_report


@app.post("/api/medical-rag/ask")
def ask(req: AskRequest):
    question = (req.question or "").strip()
    if not question:
        raise HTTPException(status_code=400, detail={"error": "question 不能为空"})

    triage_model = req.triage_model or (req.runtime_config or {}).get("local_model") or req.synthesis_model
    triage = _triage_medical_question(question, history=req.history or [], model=triage_model)
    if not triage["allow_rag"]:
        return _safety_refusal(question, triage, req.session_id)

    synthesis = synthesize(
        SynthesizeRequest(
            query=question,
            doc_ids=[],
            k=req.k,
            synthesis_model=req.synthesis_model,
            mode=req.mode,
            index_id=req.index_id,
        )
    )
    return {
        "session_id": req.session_id or uuid.uuid4().hex[:10],
        "question": question,
        "answer": synthesis["answer"],
        "status": synthesis["status"],
        "search_query": synthesis["search_query"],
        "search_queries": synthesis["search_queries"],
        "query_language": synthesis["query_language"],
        "query_rewrites": synthesis["query_rewrites"],
        "rewrite_method": synthesis["rewrite_method"],
        "model": synthesis["model"],
        "retrieval_mode": synthesis["retrieval_mode"],
        "retrieval_index": synthesis["retrieval_index"],
        "privacy": synthesis["privacy"],
        "rag_mode": synthesis["rag_mode"],
        "question_type": synthesis["question_type"],
        "answer_strategy": synthesis["answer_strategy"],
        "strategy_instruction": synthesis["strategy_instruction"],
        "evidence_cards": synthesis["evidence_cards"],
        "citations": synthesis["citations"],
        "claims": synthesis["claims"],
        "reasoning_trace": synthesis["reasoning_trace"],
        "claim_count": synthesis["claim_count"],
        "supported_claims": synthesis["supported_claims"],
        "unsupported_claims": synthesis["unsupported_claims"],
        "citation_coverage": synthesis["citation_coverage"],
        "evidence_sufficiency": synthesis["evidence_sufficiency"],
        "answer_audit": synthesis["answer_audit"],
        "confidence": synthesis["confidence"],
        "limitations": synthesis["limitations"],
        "abstain": synthesis["abstain"],
        "abstain_reason": synthesis["abstain_reason"],
        "evidence_items": synthesis["evidence_items"],
        "source_summary": synthesis["source_summary"],
        "task_id": synthesis["task_id"],
        "generated_at": synthesis["generated_at"],
        "safety_triage": triage,
        "audit": {
            **synthesis["audit"],
            "interface": "medical_rag_ask",
            "history_turns_received": len(req.history or []),
            "note": "当前 MVP 使用单轮问题检索；history 仅记录接口契约，暂不注入医疗检索上下文。",
        },
    }


@app.get("/api/evidence/report/{task_id}")
def report(task_id: str):
    report_path = REPORT_DIR / f"{task_id}.json"
    if report_path.is_file():
        return json.loads(report_path.read_text(encoding="utf-8"))

    available = sorted([p.stem for p in REPORT_DIR.glob("*.json")]) if REPORT_DIR.exists() else []
    raise HTTPException(
        status_code=404,
        detail={
            "error": f"报告未找到: {task_id}",
            "available_reports": available[:20],
        },
    )


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Clinical Evidence Synthesis Agent — REST API")
    settings = get_settings()
    parser.add_argument("--port", type=int, default=settings.api_port, help=f"监听端口 (默认 {settings.api_port})")
    parser.add_argument("--host", default=settings.api_host, help=f"绑定地址 (默认 {settings.api_host})")
    parser.add_argument("--check", action="store_true", help="仅运行健康检查后退出")
    args = parser.parse_args()

    if args.check:
        result = health()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result["status"] in {"ok", "public_evidence"} else 1)
    else:
        import uvicorn

        uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
