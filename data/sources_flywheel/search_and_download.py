import argparse, urllib.request, urllib.parse, re, json, time, ssl, pathlib, sys, os

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass


def _default_dl_dir(root):
    return root / 'data' / 'sources_flywheel'


def _keyword_to_queries(keywords):
    """Build arXiv queries from a list of keywords. One query per keyword."""
    queries = []
    for kw in keywords:
        key = kw.lower().replace(' ', '_').replace('-', '_')[:40]
        q = f'abs:"{kw}" AND cat:eess.SY'
        queries.append((key, kw, q))
    return queries


def _safe_filename_part(text, max_len=60):
    text = ' '.join(str(text or '').split())
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', text)
    text = re.sub(r'_+', '_', text).strip(' ._')
    return text[:max_len].rstrip(' ._') or 'untitled'


def _normalise_arxiv_id(value):
    arxiv_id = str(value or '').strip()
    if 'v' in arxiv_id:
        arxiv_id = arxiv_id.split('v')[0]
    if not re.fullmatch(r'\d{4}\.\d{4,5}', arxiv_id):
        return ''
    return arxiv_id


def _download_pdfs(selected, dl_dir, ctx):
    dl_dir = pathlib.Path(dl_dir)
    dl_dir.mkdir(parents=True, exist_ok=True)

    for i, paper in enumerate(selected, 1):
        aid = paper['arxiv_id']
        short_title = _safe_filename_part(paper['title'])
        fname = f"{aid}_{short_title}.pdf"
        fpath = dl_dir / fname

        if fpath.exists():
            print(f'  [{i}/{len(selected)}] {aid} already downloaded, skip')
            continue

        pdf_url = f'https://arxiv.org/pdf/{aid}'
        print(f'  [{i}/{len(selected)}] Downloading {aid}...', end=' ', flush=True)
        for attempt in range(3):
            try:
                req = urllib.request.Request(pdf_url, headers={'User-Agent': 'MinerU-Research/1.0'})
                with urllib.request.urlopen(req, timeout=120, context=ctx) as resp:
                    fpath.write_bytes(resp.read())
                size_mb = fpath.stat().st_size / (1024 * 1024)
                print(f'OK ({size_mb:.1f}MB)')
                break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print('SKIP (404)')
                    break
                if e.code == 429:
                    wait = 10 * (attempt + 1)
                    print(f'rate limited (429), waiting {wait}s...', end=' ', flush=True)
                    time.sleep(wait)
                elif attempt < 2:
                    print(f'retry ({e.code})...', end=' ', flush=True)
                    time.sleep(5)
                else:
                    print(f'FAIL (HTTP {e.code})')
            except Exception as e:
                if attempt < 2:
                    print('retry...', end=' ', flush=True)
                    time.sleep(5)
                else:
                    print(f'FAIL: {e}')
        time.sleep(2)


def search_and_download(root, queries, max_papers, dl_dir, existing_ids=None, write_meta=True):
    if existing_ids is None:
        existing_ids = set()
        candidates_path = root / 'data' / 'sources' / 'arxiv_candidates.json'
        if candidates_path.exists():
            data = json.loads(candidates_path.read_text('utf-8'))
            for entry in data:
                for c in entry.get('candidates', []):
                    existing_ids.add(c['arxiv_id'])

    print(f'Existing corpus: {len(existing_ids)} papers')

    ctx = ssl.create_default_context()
    new_papers = []

    for key, name, query in queries:
        params = urllib.parse.urlencode({
            'search_query': query, 'max_results': 8,
            'sortBy': 'submittedDate', 'sortOrder': 'descending'
        })
        url = f'http://export.arxiv.org/api/query?{params}'
        print(f'\nSearching: {name} ({key})...')

        for search_attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'MinerU-Research/1.0'})
                with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
                    xml = resp.read().decode('utf-8')
                break
            except urllib.error.HTTPError as e:
                if e.code == 429 and search_attempt < 2:
                    wait = 10 * (search_attempt + 1)
                    print(f'  Rate limited (429), waiting {wait}s...')
                    time.sleep(wait)
                elif search_attempt < 2:
                    time.sleep(3)
                else:
                    print(f'  Failed: {e}')
            except Exception as e:
                if search_attempt < 2:
                    time.sleep(3)
                else:
                    print(f'  Failed: {e}')
        else:
            continue

        entries = re.findall(r'<entry>(.*?)</entry>', xml, re.DOTALL)
        for entry in entries:
            id_match = re.search(r'<id>http://arxiv.org/abs/([^<]+)</id>', entry)
            title_match = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
            year_match = re.search(r'<published>(\d{4})', entry)

            if not id_match or not title_match:
                continue
            arxiv_id = _normalise_arxiv_id(id_match.group(1))
            if not arxiv_id:
                continue
            title = ' '.join(title_match.group(1).strip().split())
            year = int(year_match.group(1)) if year_match else 0

            if arxiv_id in existing_ids:
                continue
            if year < 2025:
                continue

            print(f'  NEW [{year}] {arxiv_id}: {title[:80]}')
            new_papers.append({
                'arxiv_id': arxiv_id, 'title': title, 'year': year,
            })
            existing_ids.add(arxiv_id)
        time.sleep(1.2)

    selected = new_papers[:max_papers]
    print(f'\n=== Selected {len(selected)} papers ===')
    for p in selected:
        print(f'  [{p["year"]}] {p["arxiv_id"]}: {p["title"][:80]}')

    _download_pdfs(selected, dl_dir, ctx)

    if write_meta:
        meta_path = dl_dir / 'flywheel_papers.json'
        meta_path.write_text(json.dumps(selected, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'\nMetadata saved: {meta_path}')

    pdfs = list(dl_dir.glob('*.pdf'))
    print(f'PDFs downloaded: {len(pdfs)}')
    for p in sorted(pdfs):
        print(f'  {p.name} ({p.stat().st_size / 1024:.0f}KB)')

    return selected


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search arXiv and download papers')
    parser.add_argument('--keywords', type=str, default='',
                        help='Comma-separated keywords, e.g. "CBF,MPC,reinforcement learning"')
    parser.add_argument('--max-papers', type=int, default=5,
                        help='Max papers to download (default 5)')
    parser.add_argument('--output-dir', type=str, default='',
                        help='Output directory for PDFs')
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parents[2]
    dl_dir = pathlib.Path(args.output_dir) if args.output_dir else _default_dl_dir(root)

    if args.keywords:
        keywords = [k.strip() for k in args.keywords.split(',') if k.strip()]
        queries = _keyword_to_queries(keywords)
    else:
        queries = [
            ('control_barrier_functions', 'Control Barrier Functions',
             'abs:"control barrier function" AND abs:safety AND cat:eess.SY'),
            ('koopman_control', 'Koopman Operator Control',
             'abs:"Koopman" AND abs:control AND cat:eess.SY'),
            ('diff_mpc', 'Differentiable MPC',
             'abs:"differentiable" AND abs:"model predictive control" AND cat:eess.SY'),
            ('safe_rl_control', 'Safe RL Control',
             'abs:"safe reinforcement learning" AND abs:control AND cat:eess.SY'),
            ('event_triggered_2025', 'Event-Triggered Control 2025',
             'abs:"event-triggered" AND abs:control AND cat:eess.SY'),
        ]

    # Backup cascade: if primary queries don't yield enough papers,
    # fall through to broader backup queries.
    BACKUP_QUERIES = [
        ('robust_mpc', 'Robust MPC',
         'abs:"robust" AND abs:"model predictive control" AND cat:eess.SY'),
        ('nonlinear_observer', 'Nonlinear Observer',
         'abs:"nonlinear" AND abs:observer AND cat:eess.SY'),
        ('adaptive_control', 'Adaptive Control 2025+',
         'abs:"adaptive control" AND abs:stability AND cat:eess.SY'),
    ]

    selected = search_and_download(root, queries, args.max_papers, dl_dir, write_meta=False)
    existing_ids = {p['arxiv_id'] for p in selected}

    if len(selected) < args.max_papers:
        shortfall = args.max_papers - len(selected)
        print(f'\nWARN: Only {len(selected)} papers found, searching backup directions for {shortfall} more...')
        for bq in BACKUP_QUERIES:
            if shortfall <= 0:
                break
            print(f'\n--- Backup: {bq[1]} ---')
            extra = search_and_download(root, [bq], shortfall, dl_dir,
                                        existing_ids=existing_ids, write_meta=False)
            for p in extra:
                existing_ids.add(p['arxiv_id'])
            shortfall -= len(extra)
            selected += extra
        print(f'\n=== Total selected: {len(selected)} papers ===')

    if len(selected) < args.max_papers:
        seed_path = root / 'data' / 'sources_flywheel' / 'flywheel_papers.json'
        if seed_path.exists():
            shortfall = args.max_papers - len(selected)
            print(f'\nWARN: arXiv search returned {len(selected)} papers; using packaged seed list for {shortfall} fallback download(s).')
            seed_items = json.loads(seed_path.read_text('utf-8-sig'))
            selected_ids = {p['arxiv_id'] for p in selected}
            fallback = []
            for item in seed_items:
                aid = _normalise_arxiv_id(item.get('arxiv_id'))
                if aid and aid not in selected_ids:
                    fallback.append({
                        'arxiv_id': aid,
                        'title': item.get('title') or aid,
                        'year': item.get('year') or 0,
                    })
                    selected_ids.add(aid)
                if len(fallback) >= shortfall:
                    break
            if fallback:
                print(f'Fallback seed downloads: {len(fallback)}')
                _download_pdfs(fallback, dl_dir, ssl.create_default_context())
                selected += fallback

    # Write unified metadata once
    meta_path = dl_dir / 'flywheel_papers.json'
    meta_path.write_text(json.dumps(selected, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Metadata saved: {meta_path}')
