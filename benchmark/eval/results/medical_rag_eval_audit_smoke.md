# Medical RAG Evaluation

- Cases: 1
- Case set: zh_ask
- Top-k: 3
- Synthesis: enabled

## Summary

| Index | Provider | Model | Hit@K | Label Hit@K | Mean Hit Rank | Citation Coverage | Structured | Audit Pass | Mechanism | Bridged | Multi-query | Query Embed Sec |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| index_bge_m3 | hf | BAAI/bge-m3 | 1/1 | 1/1 | 1.00 | 1.00 | 1 | 1 | 0 | 1 | 0 | 0.0 |

## Case Details

### zh_primary_endpoint_safety: 主要终点和安全性证据

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| index_bge_m3 | True | True | primary endpoint outcome safety adverse events | `PMC8600696_chunk_007` | _introduction_other | # Endpoints  The primary endpoint is overall survival after R0/R1 resection (OS-res) (only patients with R0/R1 resection).  Secondary efficacy endpoints are OS of the entire patients cohort, R0/R1 resection rate and prog |
