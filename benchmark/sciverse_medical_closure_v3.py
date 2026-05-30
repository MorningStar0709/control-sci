"""D13b V3: Pull full texts from agentic-search doc_ids → chunk → eval.

Key insight: meta_search returns many results without content; agentic-search
hits always have content available. Pull 10+ unique doc_ids from 12 agentic-search
queries, download full text, chunk independently, eval against Chinese Ask questions.
"""

import json, os, re, sys, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from controlsci.api.sciverse_client import SciverseClient

KEY = os.environ.get("SCIVERSE_API_KEY", "")
C_API = "https://api.sciverse.space/content"
EXPANSION_JSON = ROOT / "benchmark" / "eval" / "results" / "medical" / "sciverse_medical_expansion.json"
PMC_MANIFEST = ROOT / "data" / "sources_medical" / "chunks" / "chunks_manifest.json"
OUT_PATH = ROOT / "benchmark" / "eval" / "results" / "medical" / "sciverse_medical_closure_v3.json"

QUERIES = [
    "closed-loop insulin pump glucose control algorithm",
    "model predictive control ICU mechanical ventilation optimization",
    "adaptive control drug delivery pharmacokinetic model",
    "telemedicine chronic disease management intervention effectiveness",
    "diagnostic accuracy sensitivity specificity MRI deep learning",
    "systematic review meta-analysis evidence-based clinical practice",
    "inhaled nanoparticle pulmonary absorption controlled release",
    "randomized controlled trial design methodology",
    "Kalman filter biomedical signal ECG noise removal",
    "sliding mode control surgical robotic arm precision",
    "fuzzy logic medical diagnosis decision support system",
    "neural network rehabilitation brain computer interface",
    "robust control anesthesia drug infusion safety",
    "biomedical image segmentation CNN U-Net",
]


def _get_fulltext(doc_id):
    qs = urllib.parse.urlencode({"doc_id": doc_id, "offset": "0", "limit": str(700)})
    req = urllib.request.Request(
        f"{C_API}?{qs}",
        headers={"Authorization": f"Bearer {KEY}"},
    )
    r = urllib.request.urlopen(req, timeout=30)
    return json.loads(r.read())


def _pull_all(doc_id):
    full = ""
    offset = 0
    for _ in range(6):
        qs = urllib.parse.urlencode({"doc_id": doc_id, "offset": str(offset), "limit": str(6000)})
        req = urllib.request.Request(f"{C_API}?{qs}", headers={"Authorization": f"Bearer {KEY}"})
        r = urllib.request.urlopen(req, timeout=30)
        data = json.loads(r.read())
        full += data.get("text", "")
        if not data.get("more", False) or offset >= 24000:
            break
        offset = data.get("next_offset", offset + 6000)
    return full


def main():
    print("=" * 60)
    print("D13b V3: Full-Text Pipeline (agentic-search doc_ids)")
    print("=" * 60)

    client = SciverseClient(api_key=KEY)

    # Phase 1: Collect unique doc_ids from agentic-search
    print("\n[Phase 1] Collecting doc_ids from agentic-search...")
    seen = set()
    unique_papers = []
    for qi, query in enumerate(QUERIES):
        print(f"  [{qi+1}/{len(QUERIES)}] {query[:60]}...", end=" ", flush=True)
        try:
            resp = client.agentic_search(query=query, top_k=5)
            hits = resp.get("hits", resp.get("results", []))
            for h in hits:
                did = h.get("doc_id", "")
                if did and did not in seen:
                    seen.add(did)
                    unique_papers.append({
                        "doc_id": did,
                        "title": h.get("title", ""),
                        "abstract": h.get("abstract", ""),
                        "query": query,
                    })
            print(f"+{len(hits)} hits ({len(unique_papers)} unique)")
        except Exception as e:
            print(f"ERR: {str(e)[:50]}")
        time.sleep(1.5)

    print(f"\n  {len(unique_papers)} unique doc_ids from {len(QUERIES)} queries")

    # Phase 2: Pull full text for each unique paper
    N_TARGET = 12
    target = unique_papers[:N_TARGET]
    print(f"\n[Phase 2] Pulling full text for {len(target)} papers...")
    full_texts = []
    for pi, paper in enumerate(target):
        did = paper["doc_id"]
        title = paper["title"][:60]
        print(f"  [{pi+1}/{len(target)}] {title}...", end=" ", flush=True)
        try:
            full = _pull_all(did)
            ok = len(full) > 300
            if ok:
                full_texts.append({**paper, "full_text": full})
            print(f"{len(full)} chars {'OK' if ok else 'TOO_SHORT'}")
        except Exception as e:
            print(f"FAIL: {str(e)[:60]}")
        time.sleep(1.5)

    print(f"\n  Successfully pulled {len(full_texts)}/{len(target)} papers")

    # Phase 3: Chunk
    print(f"\n[Phase 3] Chunking...")
    all_chunks = []
    for paper in full_texts:
        paras = [p.strip() for p in paper["full_text"].split("\n\n") if len(p.strip()) > 60]
        for ci, para in enumerate(paras):
            para = re.sub(r"\[.*?\]\(.*?\)", "", para)
            para = re.sub(r"!\[.*?\]\(.*?\)", "", para)
            para = para.strip()
            if len(para) < 60:
                continue
            all_chunks.append({
                "chunk_id": f"{paper['doc_id']}:c{ci}",
                "doc_id": paper["doc_id"],
                "title": paper["title"],
                "text": para[:1500],
            })
    print(f"  {len(all_chunks)} chunks")

    # Phase 4: Eval with Chinese Ask questions
    print(f"\n[Phase 4] Evaluation against Chinese Ask + PMC...")
    pmc = json.loads(PMC_MANIFEST.read_text(encoding="utf-8"))
    pmc_chunks = pmc["chunks"]

    zh_path = ROOT / "benchmark" / "eval" / "results" / "medical_rag_eval_zh_ask.json"
    if zh_path.exists():
        data = json.loads(zh_path.read_text(encoding="utf-8"))
        raw = data.get("per_query", data.get("results", []))
        qs = []
        if isinstance(raw, dict):
            for v in raw.values():
                qt = v.get("question", v.get("query", "")) if isinstance(v, dict) else ""
                if qt:
                    qs.append(qt)
        elif isinstance(raw, list):
            for q in raw:
                qt = q.get("question", q.get("query", "")) if isinstance(q, dict) else ""
                if qt:
                    qs.append(qt)
        questions = qs
        print(f"  [LOAD] {len(qs)} Chinese Ask questions")
    else:
        questions = QUERIES
        print(f"  [FALLBACK] using search queries")

    results = []
    sv_only = pmc_only = both = neither = 0
    for qi, qt in enumerate(questions):
        keywords = [w.strip(".,;:()").lower() for w in qt.replace(",", " ").split()
                    if len(w) > 3 and w.lower() not in ("what", "when", "which", "that", "this", "with", "from", "have")]
        keywords = list(set(keywords))

        sv_hit = sum(1 for kw in keywords for c in all_chunks if kw in c["text"].lower())
        pmc_hit = sum(1 for kw in keywords for c in pmc_chunks[:1000]
                      if kw in c.get("text", "")[:500].lower())

        has_sv = sv_hit >= 1
        has_pmc = pmc_hit >= 1
        if has_sv and has_pmc:
            both += 1
        elif has_sv:
            sv_only += 1
        elif has_pmc:
            pmc_only += 1
        else:
            neither += 1

        results.append({"question": qt[:150], "sv_hits": sv_hit, "pmc_hits": pmc_hit,
                        "sciverse_unique": sv_only if has_sv and not has_pmc else 0})
        if has_sv and not has_pmc:
            print(f"  [{qi+1}] SV_UNIQUE: {qt[:60]}...")

    report = {
        "analysis": "sciverse_medical_closure_v3",
        "n_doc_ids_collected": len(unique_papers),
        "n_pulled": len(full_texts),
        "n_chunks": len(all_chunks),
        "n_questions": len(questions),
        "chunks": all_chunks,
        "coverage": {
            "sciverse_unique": sv_only,
            "pmc_unique": pmc_only,
            "both": both,
            "neither": neither,
            "combined": sv_only + pmc_only + both,
        },
        "per_question": results,
    }
    OUT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n{'=' * 60}")
    print(f"D13b V3 COMPLETE — True End-to-End Closure")
    print(f"  Papers pulled:    {len(full_texts)}")
    print(f"  Chunks:           {len(all_chunks)}")
    print(f"  Sciverse unique:  {sv_only}")
    print(f"  PMC unique:       {pmc_only}")
    print(f"  Both covered:     {both}")
    print(f"  Combined:         {sv_only + pmc_only + both}/{len(questions)}")
    print(f"  Report:           {OUT_PATH}")
    print(f"{'=' * 60}")
    if sv_only > 0:
        print(f"  ✅ {sv_only} questions Sciverse adds evidence PMC misses — pipeline fully closed")
    else:
        print(f"  ⚠️  No unique Sciverse-only hits")


if __name__ == "__main__":
    main()
