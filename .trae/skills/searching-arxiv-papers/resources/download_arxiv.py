import argparse
import json
import os
import re
import sys
import time
import urllib.request


def safe_filename(arxiv_id, title):
    short = re.sub(r'[^\w\s-]', '', title)[:60]
    short = re.sub(r'[-\s]+', '_', short.strip())
    return f"{arxiv_id}_{short}.pdf"


def main():
    parser = argparse.ArgumentParser(description="Download selected arXiv papers from candidate list")
    parser.add_argument("--project-dir", default=None, help="Override project root detection")
    parser.add_argument("--candidate-file", default=None, help="Path to arxiv_candidates.json (overrides --project-dir)")
    parser.add_argument("--download-dir", default=None, help="Custom download directory for PDFs (overrides --project-dir)")
    parser.add_argument("--delay", type=int, default=3, help="Seconds between downloads (default 3)")
    args = parser.parse_args()

    if args.candidate_file:
        candidates_path = os.path.abspath(args.candidate_file)
    elif args.download_dir:
        candidates_path = os.path.join(os.path.abspath(args.download_dir), "..", "sources", "arxiv_candidates.json")
    elif args.project_dir:
        base_dir = os.path.abspath(args.project_dir)
        candidates_path = os.path.join(base_dir, "data", "sources", "arxiv_candidates.json")
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        candidates_path = os.path.join(base_dir, "data", "sources", "arxiv_candidates.json")

    if args.download_dir:
        pdf_dir = os.path.abspath(args.download_dir)
    elif args.project_dir:
        pdf_dir = os.path.join(os.path.abspath(args.project_dir), "data", "pdf", "arXiv")
    else:
        pdf_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data", "pdf", "arXiv")

    os.makedirs(pdf_dir, exist_ok=True)

    with open(candidates_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    selected_papers = []
    for entry in data:
        target = entry["target"]
        candidates = entry["candidates"]
        selected_count = 0
        for c in candidates:
            if selected_count < target:
                c["selected"] = True
                selected_papers.append(c)
                selected_count += 1
            else:
                c["selected"] = False

    print(f"Selected {len(selected_papers)} papers for download")

    with open(candidates_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    existing_files = set(os.listdir(pdf_dir))
    downloaded = 0
    skipped = 0
    failed = 0

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    for paper in selected_papers:
        arxiv_id = paper["arxiv_id"]
        filename = safe_filename(arxiv_id, paper["title"])
        filepath = os.path.join(pdf_dir, filename)

        if filename in existing_files:
            print(f"  SKIP: {arxiv_id} (exists)")
            skipped += 1
            continue

        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
        success = False
        for attempt in range(3):
            if attempt > 0:
                print(f"    RETRY {attempt+1}/3...")
                time.sleep(5)
            try:
                req = urllib.request.Request(pdf_url, headers=headers)
                with urllib.request.urlopen(req, timeout=120) as response:
                    with open(filepath, "wb") as f:
                        f.write(response.read())
                size_kb = os.path.getsize(filepath) / 1024
                print(f"  OK: {arxiv_id} ({size_kb:.0f} KB)")
                downloaded += 1
                success = True
                break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print(f"  FAIL 404: {arxiv_id} not found")
                    failed += 1
                    break
                elif e.code == 429:
                    print(f"    RATE LIMITED, waiting 10s...")
                    time.sleep(10)
                    continue
                else:
                    if attempt < 2:
                        continue
                    print(f"  FAIL HTTP {e.code}: {arxiv_id}")
                    failed += 1
                    success = False
                    break
            except Exception as e:
                if attempt < 2:
                    print(f"    TRANSIENT, retrying...")
                    continue
                print(f"  FAIL: {arxiv_id} ({e})")
                failed += 1

        time.sleep(args.delay)

    print(f"\nDone: {downloaded} OK, {skipped} skipped, {failed} failed")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
