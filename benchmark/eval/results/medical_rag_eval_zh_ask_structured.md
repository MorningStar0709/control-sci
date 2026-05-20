# Medical RAG Evaluation

- Cases: 7
- Case set: zh_ask
- Top-k: 3
- Synthesis: enabled

## Summary

| Index | Provider | Model | Hit@K | Label Hit@K | Mean Hit Rank | Citation Coverage | Structured | Mechanism | Bridged | Multi-query | Query Embed Sec |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| index_bge_m3 | hf | BAAI/bge-m3 | 7/7 | 6/7 | 1.00 | 1.00 | 7 | 1 | 7 | 2 | 0.0 |

## Case Details

### zh_primary_endpoint_safety: 主要终点和安全性证据

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| index_bge_m3 | True | True | primary endpoint outcome safety adverse events | `PMC8600696_chunk_007` | _introduction_other | # Endpoints  The primary endpoint is overall survival after R0/R1 resection (OS-res) (only patients with R0/R1 resection).  Secondary efficacy endpoints are OS of the entire patients cohort, R0/R1 resection rate and prog |

### zh_survival_endpoint: 总生存和无进展生存证据

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| index_bge_m3 | True | True | overall survival progression free | `PMC6937062_chunk_031` | statistical_analysis | # Data analysis plan  Analyses will be conducted on an intention-to-treat basis, with sensitivity analyses used to investigate the impact of non-compliance to allocated arm. Given the feasibility status of this study, al |

### zh_chemo_toxicity: 化疗剂量减少和治疗延迟的不良事件证据

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| index_bge_m3 | True | True | chemotherapy dose reduction treatment delay adverse events | `PMC8600696_chunk_015` | intervention | # Dose modifications and prerequisites for the start of a new cycle  Doses will be reduced for haematological and nonhaematological toxicities. In case of concurrent toxicities, all dose modifications should be based on  |

### zh_serious_adverse_event: 严重不良事件的安全性终点证据

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| index_bge_m3 | True | True | serious adverse event safety endpoint events outcome | `PMC12574440_chunk_039` | _intervention_other | # Safety analysis  For each of the following safety outcomes, mean±SD or summary statistics appropriate to the distribution will be tabulated by treatment group:  ► Number of severe hypoglycaemia events.    ► Number of p |

### zh_itt_population: 意向治疗分析人群的统计分析证据

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| index_bge_m3 | True | True | intention to treat population analysis statistical | `PMC11929207_chunk_018` | statistical_analysis | # Statistical analysis  In general, p-values < 0.05 are considered to indicate statistical signifcance (2-tailed test). Te p-values for the secondary endpoints will be presented but considered descriptive and hypothesis  |

### zh_closed_loop_mechanism: 为什么诊断后48个月内胰岛素需求上升支持早期使用自适应闭环系统？

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| index_bge_m3 | True | False | 48 months insulin requirements closed loop daily dose adaptive | `PMC7618672_chunk_004` | front_matter | # Abstract  Objective: To evaluate trends in insulin delivery and day-to-day variability of insulin requirements over 48 months of hybrid closed-loop use following diagnosis of type 1 diabetes in individuals aged 10 to 1 |

### zh_eligibility: 随机对照试验的纳入排除标准

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| index_bge_m3 | True | True | randomized controlled trial inclusion criteria exclusion | `PMC6561428_chunk_012` | _randomization_other | # Box 1 Inclusion and exclusion criteria |
