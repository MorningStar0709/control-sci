# Medical QLoRA Re-ranker Report

- Base model: `principled-intelligence/Qwen3.5-4B-text-only`
- Adapter: `finetune\output\qlora-medical-final`
- Candidate source: `hybrid`
- Queries: 2
- Candidates: 10
- Elapsed: 14.3s

## Summary

| Metric | RRF baseline | QLoRA rerank | Delta |
|:--|--:|--:|--:|
| MRR exact | 0.0000 | 0.0000 | +0.0000 |
| NDCG@K graded | 0.9914 | 0.8803 | -0.1111 |

## By Query

| Query | Source label | MRR delta | NDCG delta | Rerank top grade |
|:--|:--|--:|--:|--:|
| `6f78941a` | results | +0.0000 | -0.2223 | 0 |
| `1c2cdc0e` | front_matter | +0.0000 | +0.0000 | 1 |
