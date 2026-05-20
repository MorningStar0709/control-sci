---
name: searching-arxiv-papers
description: Search and batch-download arXiv papers by research direction using the arXiv API. Use when the user asks to search for papers, collect references, build a paper corpus, or download arXiv PDFs by topic, including Chinese requests such as "搜论文", "批量下载", "收集文献", "搜 arXiv"等. Do not use for generic web search, Google Scholar search, or non-arXiv paper collection. Do not use when papers must come from IEEE, Springer, or other paywalled sources. Do not use when the user needs a literature survey or paper summary. Do not use when the user asks for real-time search results without storing as candidates.
---

## When to Use

- User asks to "search papers about [topic]" or "collect references on [direction]"
- User needs to download multiple arXiv PDFs by topic keywords
- User needs to build a paper candidate list with metadata (title, authors, year, abstract)
- The target corpus is arXiv-only (OA, no copyright risk)

## When Not to Use

- Papers must come from IEEE, Springer, or other paywalled sources
- User only needs a single paper by arXiv ID (use direct download instead)
- User needs a literature survey or paper summary output
- User asks for real-time search results without storing as candidates

## Inputs

Inputs are expressed in natural language, then translated to script parameters:

| Input | Required? | Description |
|-------|-----------|-------------|
| **Topic / direction** | ✅ Yes | What papers to search for. Can be one direction (e.g., "sliding mode control") or a list of directions. |
| **Quantity** | ❌ No | How many papers per direction. Defaults to 10-30 depending on the direction. |
| **Output location** | ❌ No | Where to save metadata and PDFs. Defaults to project standard paths (`data/sources/`, `data/pdf/arXiv/`). |

The agent MUST translate natural-language inputs into script parameters as follows:

- If user says "search for papers on [topic]" → build an arXiv query string following Step 1 syntax, then pass as custom queries to `mass_search.py` (see `--queries-file` below).
- If user gives a project name or path → use as `--project-dir`.
- If user says "save to [folder]" → use as `--output-dir` or `--download-dir`.

### Script Parameter Reference

**mass_search.py**:
| Parameter | When to use |
|-----------|-------------|
| `--project-dir /path/to/project` | Target project has standard `data/sources/` structure |
| `--output-dir /any/path` | Save candidates to an arbitrary directory |
| `--queries-file /path/to/queries.json` | Load custom query definitions from JSON file instead of hardcoded defaults. JSON format: `[{"key": "dir1", "name": "方向1", "query": "abs:...", "target": 10}]` |
| `--max-results N` | Override results per query (default 60) |
| `--delay N` | Override delay between queries (default 3) |

**download_arxiv.py**:
| Parameter | When to use |
|-----------|-------------|
| `--project-dir /path/to/project` | Target project has standard `data/sources/` + `data/pdf/arXiv/` structure |
| `--candidate-file /path/to/candidates.json` | Candidates are stored in an arbitrary location |
| `--download-dir /any/path` | Save PDFs to an arbitrary directory |
| `--delay N` | Override delay between downloads (default 3) |

## Workflow

### Step 1: Define Search Directions

The script `resources/mass_search.py` has default queries for control science (19 directions). For other domains, the agent MUST customize queries.

**If the user's topic is NOT control science**, do NOT use the hardcoded defaults. Instead:

Option A — Build a queries JSON file and pass it via `--queries-file`:
```json
[
  {"key": "your_topic", "name": "Your Topic", "query": "abs:\"your keyword\" AND cat:cs.XX", "target": 15}
]
```
Then run: `python resources/mass_search.py --queries-file /path/to/custom.json`

Option B — If only 1-2 directions, modify the `QUERIES` list in `mass_search.py` directly.

The arxiv_query_string uses arXiv API syntax. Common patterns:

| Pattern | Example |
|---------|---------|
| Title match | `ti:"multi-agent" AND cat:eess.SY` |
| Abstract + category | `abs:"reinforcement learning" AND abs:control AND cat:eess.SY` |
| OR combination | `(abs:"robust control" OR abs:"H-infinity") AND cat:eess.SY` |
| Exclusion | `AND NOT abs:reinforcement` |

If the user provides only natural language directions (e.g., "search for papers on multi-agent systems"), translate them to arXiv query strings using these conventions:
- Quote multi-word terms: `abs:"sliding mode"`
- Limit to eess.SY (Systems and Control) category
- Use AND/OR operators
- Set max_results=60 per query

When running the scripts, use `--project-dir` to point to the project root if the script is called from outside the project (e.g., from Skill resources):

```powershell
python .trae\skills\searching-arxiv-papers\resources\mass_search.py --project-dir D:\Projects\YourProject
```

Without `--project-dir`, the script auto-detects the project root by walking up from its own location.

Query efficiency ranking (from real-world experiments):
| Mode | Example | Yield per query |
|------|---------|----------------|
| Best | `abs:"keyword phrase" AND cat:eess.SY` | 15-30 papers (deduplicated) |
| Good | `(abs:"kw1" OR abs:"kw2") AND cat:eess.SY` | 20-40 papers |
| Fair | `abs:"cross-domain" OR abs:"other-domain" AND cat:eess.SY` | Many but lower relevance |
| Avoid | `ti:"keyword" AND cat:eess.SY` | 2-6 papers — only for exact lookup |

arXiv category codes for control science: `eess.SY` (Systems and Control), `math.OC` (Optimization and Control), `cs.RO` (Robotics), `cs.MA` (Multi-Agent Systems).

### Step 2: Run Search

Run `resources/mass_search.py` from the Skill directory (or from project root with `--project-dir`).

The script:
1. Builds the URL using `urllib.parse.urlencode({"search_query": query, "max_results": 60, ...})` — **never** concatenate query strings with f-string or `+`; spaces in queries will cause HTTP 400 errors.
2. Sends HTTP GET requests to `http://export.arxiv.org/api/query`
3. Parses Atom XML response using regex (`<entry>`, `<id>`, `<title>`, `<published>`, etc.)
4. Filters out papers published before 2022 and papers already in the existing candidate list
5. Appends new candidates to `arxiv_candidates.json`
6. Sleeps 3 seconds between queries to avoid rate limiting

### Step 3: Clean Duplicate Directions

If the candidate file contains old entries with the same `direction` key as new ones (from prior searches), keep only the entry with the larger candidate pool. Run:

```python
# Keep the largest candidate pool per direction key
best = {}
for entry in data:
    k = entry["direction"]
    if k not in best or len(entry["candidates"]) > len(best[k]["candidates"]):
        best[k] = entry
data = list(best.values())
```

### Step 4: Download Selected PDFs

Run `resources/download_arxiv.py` from the Skill directory (or from project root with `--project-dir`).

The script:
1. Reads `arxiv_candidates.json`
2. For each direction, selects the first N candidates (where N = direction's `target` count)
3. Marks them as `selected: true`
4. Downloads PDFs to `{project_dir}/data/pdf/arXiv/` with filename format `{arxiv_id}_{short_title}.pdf` (title truncated to 60 chars for Windows path safety)
5. Skips already-downloaded files (filename check)
6. Retries on transient failures (3 attempts, 5s delay, timeout=120s)
7. Handles 404 (paper not available — skip without retry), 429 (rate limited — waits 10s then retry), other HTTP errors (retry up to 3 times)
8. Sleeps 3 seconds between downloads

Required retry logic summary:
```
1. 3 retry attempts, 5s interval             ← network fluctuation
2. timeout=120s                              ← large/slow PDFs
3. HTTP 404 → skip without retry             ← arXiv version unavailable
4. HTTP 429 → sleep(10s) then retry          ← rate limit
5. Other exceptions → retry 3 times then give up ← SSL drops
6. Filename dedup from existing files        ← idempotent reruns
7. Filename truncation to 60 chars           ← Windows path limit
```

### Step 5: Verify

Count total PDFs and print summary:

```powershell
(Get-ChildItem {project_dir}\data\pdf\arXiv\*.pdf).Count
Get-ChildItem {project_dir}\data\pdf\arXiv\*.pdf | Measure-Object -Property Length -Sum | Select-Object Count, @{N="MB";E={[math]::Round($_.Sum/1MB, 1)}}
```

## Output

- `{project_dir}/data/sources/arxiv_candidates.json`: JSON array with per-direction entries. Each entry has `direction`, `direction_cn`, `target`, and `candidates` array. Each candidate has `arxiv_id`, `title`, `authors`, `year`, `category`, `pdf_url`, `abstract_preview`, `selected`, `notes`.
- `{project_dir}/data/pdf/arXiv/`: downloaded PDF files.
- Console summary: total downloaded, skipped, failed counts.

## Failure Handling

| Situation | Response |
|-----------|----------|
| arXiv API returns 400 Bad Request | Check query string for unencoded spaces. Always use `urllib.parse.urlencode`. |
| arXiv API returns 429 Too Many Requests | Increase delay to 10s between queries, reduce max_results. Script already retries. |
| PDF download returns 404 | Paper version may not exist on arXiv. Skip and report. |
| SSL/network timeout during search | The urllib timeout is set to 120s. Retry the specific failed query, not all queries. |
| `arxiv` Python library (third-party) fails | Prefer direct HTTP/Atom parsing via `urllib` + regex. The third-party library has SSL proxy issues on some networks. |
| Candidate JSON already exists with old directions | Run Step 3 deduplication before downloading. |

## Resources

- `resources/mass_search.py`: search script — sends queries to arXiv API, parses Atom XML, deduplicates, saves candidates. Supports `--project-dir`, `--output-dir`, `--queries-file`, `--max-results`, `--delay`.
- `resources/download_arxiv.py`: download script — reads candidates.json, downloads selected PDFs with retry logic. Supports `--project-dir`, `--candidate-file`, `--download-dir`, `--delay`.

## Examples

See `examples/` directory for sample input prompts and expected output format.
