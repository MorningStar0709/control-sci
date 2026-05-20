# Example: Searching Multi-Agent Control Papers

## User Prompt

"帮我搜一下多智能体系统控制方向的最新论文，需要 30 篇。"

## What the Skill Should Do

1. Translate to arXiv query: `abs:"multi-agent" AND abs:control AND cat:eess.SY`
2. Run `resources/mass_search.py` from the Skill directory (or use `--project-dir` from project root)
3. If no custom direction specified, run with the default 19 control-science directions
4. Download first 30 candidates to `data/pdf/arXiv/`
5. Report summary

## Expected Output Structure

```
=== 多智能体系统 (multi_agent) ===
    Query: abs:"multi-agent" AND abs:control AND cat:eess.SY
    New candidates: 24
    Sleeping 3s...

...

Done!
Total directions: 19
Total candidates: 490
Total target: 277

Download: 342 OK, 0 skipped, 0 failed
Saved to: D:\...\data\pdf\arXiv
```

## Candidate JSON Snippet

```json
{
  "direction": "multi_agent",
  "direction_cn": "多智能体系统",
  "target": 30,
  "candidates": [
    {
      "arxiv_id": "2511.05900",
      "title": "Disentangled Control of Multi-Agent Systems",
      "authors": ["Ruoyu Lin", "Gennaro Notomista", "Magnus Egerstedt"],
      "year": 2025,
      "category": "eess.SY",
      "pdf_url": "https://arxiv.org/pdf/2511.05900v2",
      "selected": true,
      "notes": ""
    }
  ]
}
```

# Example: Single Custom Direction

## User Prompt

"帮我在 arXiv 上搜一下滑模控制的论文，下载 10 篇。"

## Skill Mapping

- direction_key: `sliding_mode_custom`
- display_name: "滑模控制"
- query: `abs:"sliding mode" AND cat:eess.SY`
- target: 10
