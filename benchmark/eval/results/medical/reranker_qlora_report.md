# Medical QLoRA Re-ranker Report

- Base model: `principled-intelligence/Qwen3.5-4B-text-only`
- Adapter: `finetune\output\qlora-medical-final`
- Candidate source: `hybrid`
- Queries: 25
- Candidates: 125
- Elapsed: 44.3s

## Summary

| Metric | RRF baseline | QLoRA rerank | Delta |
|:--|--:|--:|--:|
| MRR exact | 0.3860 | 0.4300 | +0.0440 |
| NDCG@K graded | 0.7480 | 0.7907 | +0.0427 |

## By Query

| Query | Source label | MRR delta | NDCG delta | Rerank top grade |
|:--|:--|--:|--:|--:|
| `6f78941a` | results | +0.0000 | -0.2223 | 0 |
| `1c2cdc0e` | front_matter | +0.0000 | +0.0000 | 1 |
| `c2f95902` | ethical_approval | +0.0000 | -0.0091 | 3 |
| `ba5292c7` | secondary_outcome | +0.0000 | +0.2441 | 0 |
| `fb02b239` | _adverse_events_other | +0.0000 | +0.0705 | 3 |
| `313c2d9d` | _data_collection_other | +0.8000 | +0.6131 | 3 |
| `5d7cac63` | _subgroup_analysis_other | +0.0000 | -0.0676 | 3 |
| `307b9e2f` | blinding | +0.5000 | +0.3691 | 3 |
| `5e132da2` | _methods_other | +0.0000 | +0.0000 | 0 |
| `105841e9` | _population_other | +0.0000 | +0.0206 | 2 |
| `f17dc5bf` | _primary_results_other | +0.0000 | +0.0705 | 3 |
| `afd0ee3f` | study_design | +0.0000 | -0.5693 | 0 |
| `321d4de9` | supplementary | +0.5000 | +0.2475 | 3 |
| `8ec5d1e1` | conclusion | +0.0000 | +0.1145 | 2 |
| `b7d263c9` | _conclusion_other | -0.5000 | -0.3691 | 0 |
| `4d2d53a9` | subgroup_analysis | +0.0000 | +0.0000 | 0 |
| `1763d999` | _supplementary_other | +0.0000 | +0.1145 | 2 |
| `e8909c8e` | inclusion_criteria | +0.0000 | +0.0000 | 0 |
| `75097927` | _study_design_other | +0.8000 | +0.4593 | 3 |
| `5de0d25e` | _references_other | +0.0000 | +0.1145 | 2 |
| `1201108f` | sensitivity_analysis | -0.5000 | -0.0842 | 2 |
| `4c893132` | references | +0.0000 | +0.0000 | 0 |
| `d75d2d0c` | introduction | +0.0000 | +0.0000 | 1 |
| `cc5b9bbb` | _intervention_other | +0.0000 | +0.0234 | 3 |
| `dcfdcf29` | _secondary_outcome_other | -0.5000 | -0.0716 | 2 |
