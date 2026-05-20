import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKPOINT_DIR = ROOT / "pipeline"
METADATA_PATH = ROOT / "corpus" / "metadata.json"
OUTPUT_CHECKPOINT = CHECKPOINT_DIR / "complete_metadata.checkpoint.json"

CHUNKS = 4

def main():
    merged_classified = set()
    merged_results = {}
    preserved_arxiv_ids = set()
    preserved_cross_results = {}

    if OUTPUT_CHECKPOINT.exists():
        with open(OUTPUT_CHECKPOINT, encoding="utf-8") as f:
            existing_cp = json.load(f)
        preserved_arxiv_ids.update(existing_cp.get("arxiv_enriched_ids", []))
        preserved_cross_results.update(existing_cp.get("cross_results", {}))

    for i in range(CHUNKS):
        cp_path = CHECKPOINT_DIR / f"complete_metadata.checkpoint.chunk_{i}.json"
        if not cp_path.exists():
            print(f"[WARN] chunk {i} checkpoint missing: {cp_path}")
            continue
        with open(cp_path, encoding="utf-8") as f:
            cp = json.load(f)
        ids = cp.get("classified_ids", [])
        results = cp.get("classification_results", {})
        merged_classified.update(ids)
        merged_results.update(results)
        preserved_arxiv_ids.update(cp.get("arxiv_enriched_ids", []))
        print(f"[chunk {i}] {len(ids)} classified, {len(results)} results")

    print(f"\n[Merge] 合计: {len(merged_classified)} classified, {len(merged_results)} results")

    with open(METADATA_PATH, encoding="utf-8") as f:
        metadata = json.load(f)
    all_docs = metadata["docs"]

    for doc in all_docs:
        if (
            doc.get("type") == "arxiv"
            and doc.get("arxiv_id")
            and "Unknown" not in doc.get("author", "")
            and "To be verified" not in doc.get("author", "")
        ):
            preserved_arxiv_ids.add(doc["id"])

    applied = 0
    for doc in all_docs:
        doc_id = doc["id"]
        if doc_id in merged_results:
            r = merged_results[doc_id]
            doc["control_category"] = r["categories"]
            if r.get("difficulty"):
                doc["difficulty"] = r["difficulty"]
            applied += 1

    metadata["docs"] = all_docs
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"[Merge] metadata.json updated: {applied} docs classified")

    merged_cp = {
        "phase": "A_complete",
        "classified_ids": sorted(merged_classified),
        "classification_results": merged_results,
        "arxiv_enriched_ids": sorted(preserved_arxiv_ids),
        "cross_results": preserved_cross_results,
    }
    with open(OUTPUT_CHECKPOINT, "w", encoding="utf-8") as f:
        json.dump(merged_cp, f, ensure_ascii=False, indent=2)

    print(f"[Merge] 合并 checkpoint 写入: {OUTPUT_CHECKPOINT}")

    empty_cat = sum(1 for d in all_docs if not d.get("control_category"))
    print(f"\n[验证] control_category 空: {empty_cat}/{len(all_docs)}")
    non_std = 0
    import importlib.util
    spec = importlib.util.spec_from_file_location("complete_metadata", CHECKPOINT_DIR / "complete_metadata.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    STANDARD_CATEGORIES = mod.STANDARD_CATEGORIES
    for d in all_docs:
        for c in d.get("control_category", []):
            if c not in STANDARD_CATEGORIES:
                non_std += 1
    print(f"[验证] 非标准分类: {non_std}")


if __name__ == "__main__":
    main()
