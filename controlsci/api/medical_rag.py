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
import sys
import uuid
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from controlsci.core.paths import PROJECT_ROOT
from controlsci.medical.indexing import _load_chunk_texts, load_manifest, search_hybrid

LOCAL_MEDICAL_ROOT = PROJECT_ROOT / "data" / "sources_medical"
DEMO_MEDICAL_ROOT = PROJECT_ROOT / "data" / "demo_cloud" / "medical"
REPORT_DIR = PROJECT_ROOT / "benchmark" / "eval" / "results" / "medical"

app = FastAPI(
    title="Clinical Evidence Synthesis Agent",
    description="基于 MinerU 解析 + Hybrid 检索 (FAISS Dense + BM25 Sparse + RRF) 的医疗文献 RAG API",
    version="1.0.0",
)


class SynthesizeRequest(BaseModel):
    query: str
    doc_ids: list[int] = []


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
    top_k: int
    vision_enabled: bool = False
    count: int
    results: list[SearchResultItem]


_chunk_texts_cache = None


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
    return DEMO_MEDICAL_ROOT if _is_cloud_demo() else LOCAL_MEDICAL_ROOT


def _index_dir():
    return _medical_root() / "index"


def _manifest_candidates():
    root = _medical_root()
    return [
        root / "chunks" / "chunks_manifest.json",
        root / "md" / "chunks" / "chunks_manifest.json",
    ]


def _dense_path():
    return _index_dir() / "medical.index"


def _sparse_path():
    return _index_dir() / "bm25.pkl"


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


def _check_index_issues():
    issues = []
    if _is_cloud_demo() and not DEMO_MEDICAL_ROOT.exists():
        issues.append(f"cloud_demo 数据目录缺失: {DEMO_MEDICAL_ROOT}")
    if not _dense_path().exists():
        issues.append(f"FAISS 索引缺失: {_dense_path()}")
    if not _sparse_path().exists():
        issues.append(f"BM25 索引缺失: {_sparse_path()}")
    return issues


def _check_vision_available():
    return _vision_index_path().exists() and _vision_chunks_path().exists()


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
    text = text.replace(str(DEMO_MEDICAL_ROOT), "data/demo_cloud/medical")
    text = text.replace(str(LOCAL_MEDICAL_ROOT), "data/sources_medical")
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


def _require_index():
    issues = _check_index_issues()
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


def _search(query, k, manifest):
    texts = _get_or_load_texts(manifest)
    return search_hybrid(query, _index_dir(), manifest, k=k, texts_override=texts)


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


def _search_combined(query, k, manifest):
    text_results = _search(query, k * 2, manifest)
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


@app.get("/api/health", response_model=HealthResponse)
def health():
    manifest_path = _find_manifest()
    index_issues = _check_index_issues()

    dense_ok = _dense_path().exists()
    sparse_ok = _sparse_path().exists()

    issues = [_safe_issue(issue) for issue in index_issues]
    if not manifest_path:
        issues.append("chunks manifest 未找到")

    status = "ok" if dense_ok and sparse_ok and manifest_path else "degraded"

    return {
        "status": status,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "profile": _api_profile(),
        "components": {
            "privacy_boundary": {
                "cloud_demo": _is_cloud_demo(),
                "text_full_exposed": not _is_cloud_demo(),
                "source_paths_exposed": not _is_cloud_demo(),
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
        },
        "issues": issues,
    }


@app.get("/api/evidence/search", response_model=SearchResponse)
def search(
    q: str = Query(..., description="临床查询文本 (如 'primary endpoint', 'adverse events')"),
    k: int = Query(default=5, ge=1, le=20, description="返回 top-k 结果"),
    vision: bool = Query(default=False, description="启用视觉通道（双通道 RRF 融合）"),
):
    _require_index()
    manifest = _require_manifest()

    try:
        if vision and _check_vision_available():
            results = _search_combined(q, k, manifest)
            vision_enabled = True
        else:
            results = _search(q, k, manifest)
            vision_enabled = False
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=f"索引文件缺失: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"检索失败: {e}")

    formatted = [_format_search_result(r, i + 1) if not r.get("is_vision") else _format_vision_result(r, i + 1) for i, r in enumerate(results)]
    return {"query": q, "top_k": k, "vision_enabled": vision_enabled, "count": len(formatted), "results": formatted}


@app.post("/api/evidence/synthesize")
def synthesize(req: SynthesizeRequest):
    _require_index()
    manifest = _require_manifest()

    try:
        results = _search(req.query, 10, manifest)
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
                "medical_label": r.get("medical_label", ""),
                "medical_parent": r.get("medical_parent"),
                "rrf_score": r.get("_rrf_score", 0.0),
                "text": _exposed_text(text),
                "text_preview": _preview_text(text),
            }
        )

    sources = [{"file": k, "chunk_count": len(v), "chunk_ids": v} for k, v in source_map.items()]

    synthesis_report = {
        "task_id": task_id,
        "query": req.query,
        "generated_at": timestamp,
        "evidence_items": evidence_items,
        "source_summary": {
            "total_sources": len(sources),
            "total_chunks": len(evidence_items),
            "sources": sources,
        },
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"{task_id}.json"
    tmp_path = str(report_path) + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(synthesis_report, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, str(report_path))

    return synthesis_report


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
    parser.add_argument("--port", type=int, default=8001, help="监听端口 (默认 8001)")
    parser.add_argument("--host", default="127.0.0.1", help="绑定地址 (默认 127.0.0.1)")
    parser.add_argument("--check", action="store_true", help="仅运行健康检查后退出")
    args = parser.parse_args()

    if args.check:
        result = health()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result["status"] == "ok" else 1)
    else:
        import uvicorn

        uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
