"""Sciverse 检索器 + 双引擎 RRF 融合评测

与现有 Hybrid 检索器（FAISS + BM25 RRF）接口兼容，通过 Sciverse agentic-search API
实现双引擎检索 + RRF 融合，并对 6 个中文 Ask case 做三列对比评测。

对比指标:
  - Hit@3: 检索到的 chunk 是否包含目标医学标签
  - claim_support: chunk 内容是否支撑 case 的证据需求
  - overlap_rate: 两个引擎返回 chunk 的重叠率

输出:
  benchmark/eval/results/medical/sciverse_fused_rrf.json

用法:
  conda run --no-capture-output -n myenv python -m controlsci.medical.sciverse_retriever
  conda run --no-capture-output -n myenv python -m controlsci.medical.sciverse_retriever --trace-path custom/traces.jsonl
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from controlsci.api.sciverse_client import SciverseClient
from controlsci.core.paths import PROJECT_ROOT
from controlsci.medical.indexing import load_manifest, search_hybrid

DEFAULT_TRACE = (
    PROJECT_ROOT
    / "benchmark"
    / "eval"
    / "results"
    / "medical_rag_zh_ask_traces.jsonl"
)
DEFAULT_MANIFEST = (
    PROJECT_ROOT / "data" / "sources_medical" / "chunks" / "chunks_manifest.json"
)
DEFAULT_INDEX_DIR = PROJECT_ROOT / "data" / "sources_medical" / "index"
DEFAULT_OUTPUT = (
    PROJECT_ROOT
    / "benchmark"
    / "eval"
    / "results"
    / "medical"
    / "sciverse_fused_rrf.json"
)


class SciverseRetriever:
    def __init__(self, client: SciverseClient | None = None):
        self._client = client or SciverseClient()

    def search(self, query: str, k: int = 5) -> list[dict]:
        r = self._client.agentic_search(query=query, top_k=k)
        results = []
        for i, hit in enumerate(r.get("hits", [])):
            results.append(
                {
                    "rank": i + 1,
                    "score": hit.get("score", 0),
                    "chunk_id": hit.get("chunk_id", ""),
                    "chunk": hit.get("chunk", ""),
                    "title": hit.get("title", ""),
                    "source": "sciverse",
                    "doc_id": hit.get("doc_id", ""),
                    "page_no": hit.get("page_no"),
                }
            )
        return results

    def search_fused(self, query: str, index_dir: str, manifest: dict,
                     k: int = 5, rrf_k: int = 60) -> list[dict]:
        hy_results = search_hybrid(query, index_dir, manifest, k=k * 2)

        sv_raw = self._client.agentic_search(query=query, top_k=k * 2)
        sv_results = []
        for hit in sv_raw.get("hits", []):
            sv_results.append({
                "chunk_id": f"sv:{hit.get('chunk_id', '')}",
                "chunk": hit.get("chunk", ""),
                "title": hit.get("title", ""),
                "score": hit.get("score", 0),
                "doc_id": hit.get("doc_id", ""),
                "source": "sciverse",
            })

        rrf_scores = {}
        hy_map = {}
        for rank, r in enumerate(hy_results):
            cid = r.get("chunk_id", str(rank))
            rrf_scores[cid] = 1.0 / (rrf_k + rank + 1)
            hy_map[cid] = r

        for rank, r in enumerate(sv_results):
            cid = r["chunk_id"]
            rrf_scores[cid] = rrf_scores.get(cid, 0) + 1.0 / (rrf_k + rank + 1)
            hy_map[cid] = r

        ranked = sorted(rrf_scores.items(), key=lambda x: -x[1])[:k]
        fused = []
        for cid, rrf_score in ranked:
            item = hy_map.get(cid, {})
            if item.get("source") == "sciverse":
                fused.append({
                    "rank": len(fused) + 1,
                    "chunk_id": item.get("chunk_id", ""),
                    "rrf": round(rrf_score, 6),
                    "chunk": item.get("chunk", ""),
                    "title": item.get("title", ""),
                    "source": "sciverse",
                })
            else:
                fused.append({
                    "rank": len(fused) + 1,
                    "chunk_id": item.get("chunk_id", ""),
                    "rrf": round(rrf_score, 6),
                    "text": item.get("text", ""),
                    "medical_label": item.get("medical_label", ""),
                    "source": "local",
                })
        return fused


def _load_traces(trace_path: Path) -> list[dict]:
    traces = []
    with open(trace_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                traces.append(json.loads(line))
    return traces


def _hits_target_labels(hit_chunk: str, target_terms: list[str]) -> bool:
    chunk_lower = hit_chunk.lower()
    return any(term.lower() in chunk_lower for term in target_terms)


def _compute_overlap(
    hybrid_results: list[dict], sciverse_results: list[dict]
) -> dict:
    hybrid_chunk_ids = {r.get("chunk_id", "") for r in hybrid_results if r.get("chunk_id")}
    sv_chunk_ids = {r.get("chunk_id", "") for r in sciverse_results if r.get("chunk_id")}
    if not hybrid_chunk_ids or not sv_chunk_ids:
        return {"overlap": 0, "hybrid_only": len(hybrid_chunk_ids), "sciverse_only": len(sv_chunk_ids)}
    intersection = hybrid_chunk_ids & sv_chunk_ids
    union = hybrid_chunk_ids | sv_chunk_ids
    return {
        "overlap": len(intersection),
        "overlap_rate": round(len(intersection) / len(union), 4),
        "hybrid_only": len(hybrid_chunk_ids - sv_chunk_ids),
        "sciverse_only": len(sv_chunk_ids - hybrid_chunk_ids),
    }


def run_comparison(
    trace_path: Path | None = None,
    manifest_path: Path | None = None,
    index_dir: Path | None = None,
    output_path: Path | None = None,
    top_k: int = 5,
) -> dict:
    trace_path = Path(trace_path) if trace_path else DEFAULT_TRACE
    manifest_path = Path(manifest_path) if manifest_path else DEFAULT_MANIFEST
    index_dir = Path(index_dir) if index_dir else DEFAULT_INDEX_DIR
    output_path = Path(output_path) if output_path else DEFAULT_OUTPUT

    traces = _load_traces(trace_path)
    manifest = load_manifest(str(manifest_path))
    retriever = SciverseRetriever()

    cases = []
    sv_hits_total = 0
    hy_hits_total = 0
    sv_support_hits = 0
    hy_support_hits = 0
    fu_hits_total = 0
    fu_support_hits = 0

    for trace in traces:
        case = trace.get("case", {})
        case_id = case.get("case_id", "?")
        query_zh = case.get("query", "")
        search_query = trace.get("search_query", query_zh)
        target_terms = case.get("target_terms", [])
        target_labels = case.get("target_labels", [])

        hy_results = search_hybrid(search_query, str(index_dir), manifest, k=top_k)
        sv_results = retriever.search(search_query, k=top_k)
        fu_results = retriever.search_fused(search_query, str(index_dir), manifest, k=top_k)

        hy_hits_total += len(hy_results)
        sv_hits_total += len(sv_results)
        fu_hits_total += len(fu_results)

        hy_support = any(
            _hits_target_labels(r.get("text", r.get("chunk", "")), target_terms)
            for r in hy_results
        )
        sv_support = any(
            _hits_target_labels(r.get("chunk", ""), target_terms)
            for r in sv_results
        )
        fu_support = any(
            _hits_target_labels(r.get("text", r.get("chunk", "")), target_terms)
            for r in fu_results
        )
        if hy_support:
            hy_support_hits += 1
        if sv_support:
            sv_support_hits += 1
        if fu_support:
            fu_support_hits += 1

        overlap = _compute_overlap(hy_results, sv_results)

        hy_chunks = [
            {
                "rank": r.get("rank", i + 1),
                "chunk_id": r.get("chunk_id", ""),
                "score": r.get("score", r.get("_rrf_score", 0)),
                "preview": r.get("text", r.get("chunk", ""))[:200],
                "medical_label": r.get("medical_label", ""),
            }
            for i, r in enumerate(hy_results)
        ]
        sv_chunks = [
            {
                "rank": r["rank"],
                "score": r["score"],
                "chunk_id": r["chunk_id"],
                "preview": r["chunk"][:200],
            }
            for r in sv_results
        ]
        fu_chunks = [
            {
                "rank": r["rank"],
                "rrf": r.get("rrf", 0),
                "chunk_id": r.get("chunk_id", ""),
                "source": r.get("source", ""),
                "preview": r.get("text", r.get("chunk", ""))[:200],
                "medical_label": r.get("medical_label", ""),
            }
            for r in fu_results
        ]

        cases.append(
            {
                "case_id": case_id,
                "query_zh": query_zh,
                "search_query": search_query,
                "target_terms": target_terms,
                "target_labels": target_labels,
                "overlap": overlap,
                "local_hybrid": {
                    "results": hy_chunks,
                    "claim_support": hy_support,
                    "hit_count": len(hy_results),
                },
                "sciverse": {
                    "results": sv_chunks,
                    "claim_support": sv_support,
                    "hit_count": len(sv_results),
                },
                "fused_rrf": {
                    "results": fu_chunks,
                    "claim_support": fu_support,
                    "hit_count": len(fu_results),
                },
            }
        )

    n = len(cases)
    summary = {
        "case_count": n,
        "local_hybrid": {
            "claim_support_rate": round(hy_support_hits / n, 4) if n else 0,
            "avg_hits": round(hy_hits_total / n, 2) if n else 0,
        },
        "sciverse": {
            "claim_support_rate": round(sv_support_hits / n, 4) if n else 0,
            "avg_hits": round(sv_hits_total / n, 2) if n else 0,
        },
        "fused_rrf": {
            "claim_support_rate": round(fu_support_hits / n, 4) if n else 0,
            "avg_hits": round(fu_hits_total / n, 2) if n else 0,
        },
        "avg_overlap_rate": (
            round(sum(c["overlap"].get("overlap_rate", 0) for c in cases) / n, 4)
            if n
            else 0
        ),
    }

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input": {
            "trace_path": str(trace_path),
            "manifest_path": str(manifest_path),
            "index_dir": str(index_dir),
            "top_k": top_k,
        },
        "summary": summary,
        "cases": cases,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    return report


def main():
    parser = argparse.ArgumentParser(
        description="SciverseRetriever 双引擎 + RRF 融合评测"
    )
    parser.add_argument(
        "--trace-path",
        default=str(DEFAULT_TRACE),
        help="中文 Ask trace JSONL 路径",
    )
    parser.add_argument(
        "--manifest",
        default=str(DEFAULT_MANIFEST),
        help="chunk manifest 路径",
    )
    parser.add_argument(
        "--index-dir",
        default=str(DEFAULT_INDEX_DIR),
        help="FAISS + BM25 索引目录",
    )
    parser.add_argument("--top-k", type=int, default=5, help="检索数量")
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="对比结果 JSON 输出路径",
    )
    args = parser.parse_args()

    print(f"[SciverseRetriever] trace={args.trace_path}", flush=True)
    print(f"[SciverseRetriever] index={args.index_dir}", flush=True)
    print(f"[SciverseRetriever] top_k={args.top_k}", flush=True)

    report = run_comparison(
        trace_path=Path(args.trace_path),
        manifest_path=Path(args.manifest),
        index_dir=Path(args.index_dir),
        output_path=Path(args.output),
        top_k=args.top_k,
    )

    s = report["summary"]
    print(f"\n[Results] {s['case_count']} cases", flush=True)
    print(
        f"  Local Hybrid:  claim_support={s['local_hybrid']['claim_support_rate']:.3f}  avg_hits={s['local_hybrid']['avg_hits']}",
        flush=True,
    )
    print(
        f"  Sciverse:      claim_support={s['sciverse']['claim_support_rate']:.3f}  avg_hits={s['sciverse']['avg_hits']}",
        flush=True,
    )
    print(
        f"  Fused RRF:     claim_support={s['fused_rrf']['claim_support_rate']:.3f}  avg_hits={s['fused_rrf']['avg_hits']}",
        flush=True,
    )
    print(
        f"  Overlap rate:  {s['avg_overlap_rate']:.3f}",
        flush=True,
    )
    print(f"\n[Output] {args.output}", flush=True)


if __name__ == "__main__":
    main()
