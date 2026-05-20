"""Small retrieval comparison for local medical embedding providers."""

from __future__ import annotations

import argparse
import json
import pickle
import time
from pathlib import Path

import numpy as np

from controlsci.core.paths import PROJECT_ROOT
from controlsci.medical.embedding_providers import OLLAMA_DEFAULT_MODEL, embed_texts, read_index_metadata
from controlsci.medical.indexing import _load_chunk_texts, _lazy_import_faiss, load_manifest


DEFAULT_QUERIES = [
    "primary endpoint adverse events",
    "overall survival progression free survival",
    "inclusion criteria randomized controlled trial",
    "safety endpoint serious adverse event",
    "closed loop insulin hypoglycaemia primary endpoint",
    "chemotherapy dose reduction treatment delay adverse events",
    "Kaplan Meier survival curve median overall survival",
    "statistical analysis intention to treat population",
]


def _load_bm25(index_dir: Path):
    with open(index_dir / "bm25.pkl", "rb") as f:
        return pickle.load(f)


def _bm25_search(query: str, bm25_data: dict, manifest: dict, texts: list[str], k: int) -> list[dict]:
    scores = np.asarray(bm25_data["bm25"].get_scores(query.lower().split()))
    top = np.argsort(scores)[-k:][::-1]
    return [_result_item(int(idx), float(scores[int(idx)]), "bm25", manifest, texts, rank + 1) for rank, idx in enumerate(top)]


def _dense_search(query_emb: np.ndarray, index_dir: Path, manifest: dict, texts: list[str], k: int) -> list[dict]:
    faiss = _lazy_import_faiss()
    index = faiss.read_index(str(index_dir / "medical.index"))
    emb = query_emb.reshape(1, -1).astype(np.float32)
    faiss.normalize_L2(emb)
    scores, indices = index.search(emb, k)
    items = []
    for rank, (idx, score) in enumerate(zip(indices[0], scores[0])):
        if idx >= 0:
            items.append(_result_item(int(idx), float(score), "dense", manifest, texts, rank + 1))
    return items


def _hybrid_search(dense_items: list[dict], bm25_items: list[dict], manifest: dict, texts: list[str], k: int, rrf_k: int = 60) -> list[dict]:
    scores: dict[int, float] = {}
    for rank, item in enumerate(dense_items):
        idx = item["manifest_index"]
        scores[idx] = scores.get(idx, 0.0) + 1.0 / (rrf_k + rank + 1)
    for rank, item in enumerate(bm25_items):
        idx = item["manifest_index"]
        scores[idx] = scores.get(idx, 0.0) + 1.0 / (rrf_k + rank + 1)
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])[:k]
    return [_result_item(idx, score, "hybrid", manifest, texts, rank + 1) for rank, (idx, score) in enumerate(ranked)]


def _result_item(idx: int, score: float, mode: str, manifest: dict, texts: list[str], rank: int) -> dict:
    chunk = manifest["chunks"][idx]
    return {
        "rank": rank,
        "manifest_index": idx,
        "chunk_id": chunk.get("chunk_id", ""),
        "score": round(float(score), 6),
        "mode": mode,
        "medical_label": chunk.get("medical_label", ""),
        "medical_parent": chunk.get("medical_parent"),
        "source_section": chunk.get("source_section", ""),
        "preview": (texts[idx] if idx < len(texts) else "")[:180].replace("\n", " "),
    }


def compare(index_dirs: list[Path], manifest_path: Path, output_json: Path, k: int) -> dict:
    manifest = load_manifest(manifest_path)
    texts = _load_chunk_texts(manifest["chunks"])
    bm25_data = _load_bm25(index_dirs[0])

    results = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "manifest": str(manifest_path),
        "k": k,
        "queries": DEFAULT_QUERIES,
        "indexes": [],
        "results": {},
    }

    for index_dir in index_dirs:
        meta = read_index_metadata(index_dir)
        provider = meta.get("embedding_provider", "ollama")
        model = meta.get("embedding_model", OLLAMA_DEFAULT_MODEL)
        label = meta.get("index_id") or index_dir.name
        print(f"[Compare] {label}: {provider}:{model}", flush=True)
        t0 = time.time()
        q_emb = embed_texts(DEFAULT_QUERIES, provider, model, batch_size=min(8, len(DEFAULT_QUERIES)), progress_label=f"query_{label}")
        elapsed = time.time() - t0
        results["indexes"].append({
            "label": label,
            "index_dir": str(index_dir),
            "embedding_provider": provider,
            "embedding_model": model,
            "embedding_dim": meta.get("embedding_dim"),
            "query_embed_seconds": round(elapsed, 3),
        })

        per_query = {}
        for i, query in enumerate(DEFAULT_QUERIES):
            bm25_items = _bm25_search(query, bm25_data, manifest, texts, k * 2)
            dense_items = _dense_search(q_emb[i], index_dir, manifest, texts, k * 2)
            per_query[query] = {
                "dense": dense_items[:k],
                "hybrid": _hybrid_search(dense_items, bm25_items, manifest, texts, k),
            }
        results["results"][label] = per_query

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    output_json.with_suffix(".md").write_text(_render_markdown(results), encoding="utf-8")
    return results


def _render_markdown(data: dict) -> str:
    lines = [
        "# Medical Embedding Retrieval Comparison",
        "",
        f"- Queries: {len(data['queries'])}",
        f"- Top-k: {data['k']}",
        "",
        "## Indexes",
        "",
        "| Index | Provider | Model | Dim | Query embed sec |",
        "|---|---|---|---:|---:|",
    ]
    for item in data["indexes"]:
        lines.append(f"| {item['label']} | {item['embedding_provider']} | {item['embedding_model']} | {item.get('embedding_dim') or ''} | {item['query_embed_seconds']} |")
    lines.extend(["", "## Top Results", ""])
    for query in data["queries"]:
        lines.append(f"### {query}")
        lines.append("")
        lines.append("| Index | Hybrid top-1 | Label | Preview |")
        lines.append("|---|---|---|---|")
        for item in data["indexes"]:
            label = item["label"]
            top = data["results"][label][query]["hybrid"][0]
            preview = top["preview"].replace("|", "/")
            lines.append(f"| {label} | `{top['chunk_id']}` | {top['medical_label']} | {preview} |")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Compare local medical embedding indexes")
    parser.add_argument("--manifest", default=str(PROJECT_ROOT / "data" / "sources_medical" / "chunks" / "chunks_manifest.json"))
    parser.add_argument("--indexes", nargs="+", default=[
        str(PROJECT_ROOT / "data" / "sources_medical" / "index"),
        str(PROJECT_ROOT / "data" / "sources_medical" / "index_bge_small"),
        str(PROJECT_ROOT / "data" / "sources_medical" / "index_bge_m3"),
    ])
    parser.add_argument("--output", default=str(PROJECT_ROOT / "benchmark" / "eval" / "results" / "medical_embedding_compare.json"))
    parser.add_argument("--k", type=int, default=3)
    args = parser.parse_args()
    compare([Path(p) for p in args.indexes], Path(args.manifest), Path(args.output), args.k)
    print(f"[Compare] wrote {args.output}", flush=True)


if __name__ == "__main__":
    main()
