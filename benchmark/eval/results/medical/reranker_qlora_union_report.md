# Medical QLoRA Re-ranker Report

- Base model: `principled-intelligence/Qwen3.5-4B-text-only`
- Adapter: `finetune\output\qlora-medical-final`
- Candidate source: `union`
- Queries: 25
- Candidates: 178
- Elapsed: 55.5s

## Summary

| Metric | RRF baseline | QLoRA rerank | Delta |
|:--|--:|--:|--:|
| MRR exact | 0.3974 | 0.4533 | +0.0559 |
| NDCG@K graded | 0.6700 | 0.6845 | +0.0145 |

## By Query

| Query | Source label | MRR delta | NDCG delta | Rerank top grade |
|:--|:--|--:|--:|--:|
| `6f78941a` | results | +0.0000 | -0.1931 | 0 |
| `1c2cdc0e` | front_matter | +0.0000 | +0.0000 | 1 |
| `c2f95902` | ethical_approval | +0.0000 | +0.0371 | 3 |
| `ba5292c7` | secondary_outcome | +0.0000 | +0.4562 | 0 |
| `fb02b239` | _adverse_events_other | +0.0000 | +0.1576 | 3 |
| `313c2d9d` | _data_collection_other | +0.8000 | +0.6131 | 3 |
| `5d7cac63` | _subgroup_analysis_other | +0.0000 | -0.0823 | 3 |
| `307b9e2f` | blinding | +0.5000 | +0.3691 | 3 |
| `5e132da2` | _methods_other | -0.0833 | -0.4307 | 0 |
| `105841e9` | _population_other | +0.0000 | -0.1441 | 0 |
| `f17dc5bf` | _primary_results_other | +0.0000 | +0.0378 | 3 |
| `afd0ee3f` | study_design | +0.0000 | -1.0000 | 0 |
| `321d4de9` | supplementary | +0.5000 | +0.1993 | 3 |
| `8ec5d1e1` | conclusion | +0.0000 | +0.0828 | 2 |
| `b7d263c9` | _conclusion_other | -0.5000 | -0.3691 | 0 |
| `4d2d53a9` | subgroup_analysis | +0.0000 | +0.0000 | 0 |
| `1763d999` | _supplementary_other | +0.1905 | +0.4036 | 2 |
| `e8909c8e` | inclusion_criteria | +0.0000 | +0.0000 | 0 |
| `75097927` | _study_design_other | +0.1333 | -0.0796 | 0 |
| `5de0d25e` | _references_other | +0.8571 | +0.5593 | 3 |
| `1201108f` | sensitivity_analysis | -0.5000 | -0.1959 | 2 |
| `4c893132` | references | +0.0000 | +0.0000 | 0 |
| `d75d2d0c` | introduction | +0.0000 | +0.0000 | 1 |
| `cc5b9bbb` | _intervention_other | +0.0000 | +0.0234 | 3 |
| `dcfdcf29` | _secondary_outcome_other | -0.5000 | -0.0815 | 2 |
