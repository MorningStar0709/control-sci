# Medical RAG Evaluation

- Cases: 1
- Case set: en
- Top-k: 3
- Synthesis: enabled

## Summary

| Index | Provider | Model | Hit@K | Label Hit@K | Mean Hit Rank | Citation Coverage | Structured | Audit Pass | Mechanism | Bridged | Multi-query | Query Embed Sec |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| index_bge_small | hf | BAAI/bge-small-en-v1.5 | 1/1 | 1/1 | 1.00 | 0.80 | 1 | 0 | 0 | 0 | 0 | 39.307 |

## Case Details

### primary_endpoint_safety: primary endpoint adverse events

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| index_bge_small | True | True | primary endpoint adverse events | `PMC11929207_chunk_020` | primary_outcome | # Primary endpoint  Te primary endpoint, 28-day mortality, will be analyzed using a mixed-efects binary logistic regression [31]. Tis regression will include treatment efect and source of sepsis as fxed efects and site a |
