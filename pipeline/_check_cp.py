import json
from pathlib import Path
cp = json.load(open(Path("pipeline/complete_metadata.checkpoint.json")))
print(f"arXiv enriched: {len(cp.get('arxiv_enriched_ids', []))}")
print(f"enriched: {cp.get('arxiv_enriched_ids', [])}")
