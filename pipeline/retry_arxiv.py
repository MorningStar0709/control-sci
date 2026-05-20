import json
import re
import time
import requests
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "corpus" / "metadata.json"
CHECKPOINT_PATH = ROOT / "pipeline" / "complete_metadata.checkpoint.json"
DELAY = 8
MAX_RETRIES = 4

def query_arxiv_abs_page(arxiv_id):
    url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        resp = requests.get(url, timeout=30, headers={"User-Agent": "MinerU metadata completion"})
        if resp.status_code != 200:
            print(f"  [arXiv abs] HTTP {resp.status_code}", flush=True)
            return None
        text = resp.text
        authors = [
            unescape(author).strip()
            for author in re.findall(r'<meta\s+name="citation_author"\s+content="([^"]+)"', text)
        ]
        title_match = re.search(r'<meta\s+name="citation_title"\s+content="([^"]+)"', text)
        year_match = re.search(r'<meta\s+name="citation_date"\s+content="(\d{4})', text)
        return {
            "title": unescape(title_match.group(1)).strip() if title_match else "",
            "authors": authors,
            "year": year_match.group(1) if year_match else "",
        }
    except Exception as exc:
        print(f"  [arXiv abs] error: {exc}", flush=True)
        return None

def query_arxiv_api(arxiv_id):
    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}&max_results=1"
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code in (429, 503):
                fallback = query_arxiv_abs_page(arxiv_id)
                if fallback and fallback.get("authors"):
                    return fallback
                retry_after = resp.headers.get("Retry-After")
                wait_seconds = int(retry_after) if retry_after and retry_after.isdigit() else 20 * (attempt + 1)
                print(f"  [arXiv] HTTP {resp.status_code}, wait {wait_seconds}s", flush=True)
                time.sleep(wait_seconds)
                continue
            if resp.status_code != 200:
                print(f"  [arXiv] HTTP {resp.status_code}", flush=True)
                return None
            root = ET.fromstring(resp.text)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            entry = root.find("atom:entry", ns)
            if entry is None:
                return None
            title = entry.find("atom:title", ns)
            authors = []
            for author in entry.findall("atom:author", ns):
                name = author.find("atom:name", ns)
                if name is not None and name.text:
                    authors.append(name.text.strip())
            published = entry.find("atom:published", ns)
            year = ""
            if published is not None and published.text:
                year = published.text[:4]
            return {"title": title.text.strip().replace("\n", " ") if title is not None else "", "authors": authors, "year": year}
        except Exception as exc:
            print(f"  [arXiv] error: {exc}", flush=True)
            time.sleep(10 * (attempt + 1))
    return None

def main():
    with open(METADATA_PATH, encoding="utf-8") as f:
        metadata = json.load(f)
    with open(CHECKPOINT_PATH, encoding="utf-8") as f:
        cp = json.load(f)

    enriched = set(cp.get("arxiv_enriched_ids", []))
    docs = metadata["docs"]

    needs_retry = [
        d for d in docs
        if d.get("arxiv_id") and d["id"] not in enriched
        and ("Unknown" in d.get("author", "") or not d.get("author"))
    ]

    print(f"[arXiv Retry] 待重试: {len(needs_retry)} 篇")

    with open(CHECKPOINT_PATH, encoding="utf-8") as f:
        cp = json.load(f)
    enriched = set(cp.get("arxiv_enriched_ids", []))
    results = {}

    for doc in needs_retry:
        arxiv_id = doc["arxiv_id"]
        doc_id = doc["id"]
        print(f"[{doc_id}] 重试: {arxiv_id} ...", flush=True)
        meta = query_arxiv_api(arxiv_id)
        if meta:
            if meta.get("authors"):
                doc["author"] = ", ".join(meta["authors"])
                print(f"  -> author: {doc['author'][:80]}", flush=True)
            if meta.get("title") and ("Unknown" in doc.get("title", "") or doc.get("title", "") == doc.get("filename", "")):
                doc["title"] = meta["title"]
            if meta.get("year"):
                doc["year"] = meta["year"]
            doc["source"] = f"arXiv: {arxiv_id}"
            doc["copyright"] = "arXiv Open Access"
            enriched.add(doc_id)
            results[doc_id] = True
            print(f"  [OK]", flush=True)
        else:
            print(f"  [FAIL/429]", flush=True)
        time.sleep(DELAY)

    cp["arxiv_enriched_ids"] = sorted(enriched)
    cp["updated"] = str(__import__("datetime").date.today())
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(cp, f, ensure_ascii=False, indent=2)

    metadata["updated"] = str(__import__("datetime").date.today())
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    total = sum(1 for d in docs if not ("Unknown" in d.get("author", "") or not d.get("author")))
    print(f"\n[Retry 完成] 新增 {len(results)} 篇, 累计 {len(enriched)} 篇 enriched, 空author剩余 {len(docs)-total}/{len(docs)}")

if __name__ == "__main__":
    main()
