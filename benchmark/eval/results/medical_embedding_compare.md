# Medical Embedding Retrieval Comparison

- Queries: 8
- Top-k: 3

## Indexes

| Index | Provider | Model | Dim | Query embed sec |
|---|---|---|---:|---:|
| medical_qwen3_embedding_4b | ollama | qwen3-embedding:4b | 2560 | 4.382 |
| index_bge_small | hf | BAAI/bge-small-en-v1.5 | 384 | 8.788 |
| index_bge_m3 | hf | BAAI/bge-m3 | 1024 | 3.145 |

## Top Results

### primary endpoint adverse events

| Index | Hybrid top-1 | Label | Preview |
|---|---|---|---|
| medical_qwen3_embedding_4b | `PMC12574440_chunk_034` | outcome_measures | # Other secondary efficacy endpoints |
| index_bge_small | `PMC11929207_chunk_020` | primary_outcome | # Primary endpoint  Te primary endpoint, 28-day mortality, will be analyzed using a mixed-efects binary logistic regression [31]. Tis regression will include treatment efect and so |
| index_bge_m3 | `PMC8600696_chunk_007` | _introduction_other | # Endpoints  The primary endpoint is overall survival after R0/R1 resection (OS-res) (only patients with R0/R1 resection).  Secondary efficacy endpoints are OS of the entire patien |

### overall survival progression free survival

| Index | Hybrid top-1 | Label | Preview |
|---|---|---|---|
| medical_qwen3_embedding_4b | `PMC10882371_chunk_024` | outcome_measures | # Tertiary outcome measures |
| index_bge_small | `PMC12928687_chunk_024` | _statistical_analysis_other | # Secondary End Points  Twelve- and 24-month overall survival as well as distant progression-free survival will be evaluated by Kaplan-Meier analysis. All other secondary end point |
| index_bge_m3 | `PMC6937062_chunk_026` | outcome_measures | # Clinical outcome measures  1. Time to PSA progression; Confirmed rising PSA more than 12 weeks after randomisation. (Where there has been a decline in PSA from baseline, progress |

### inclusion criteria randomized controlled trial

| Index | Hybrid top-1 | Label | Preview |
|---|---|---|---|
| medical_qwen3_embedding_4b | `PMC6561428_chunk_012` | _randomization_other | # Box 1 Inclusion and exclusion criteria |
| index_bge_small | `PMC12898571_chunk_006` | population | # 2.2. Participants and Sample Size  The following inclusion and exclusion criteria were applied to select eligible participants for the study. |
| index_bge_m3 | `PMC12574440_chunk_008` | _methods_other | # Inclusion criteria  1. The participant has CFRD requiring insulin therapy for >3 months.    2. The participant is 16 years of age or older.    3. Baseline time in target glucose  |

### safety endpoint serious adverse event

| Index | Hybrid top-1 | Label | Preview |
|---|---|---|---|
| medical_qwen3_embedding_4b | `PMC7470506_chunk_024` | ethical_approval | # SAFETY, ETHICS AND DISSEMINATION |
| index_bge_small | `PMC6921499_chunk_024` | _data_collection_other | # Safety monitoring  In this population and within this clinical context, events that can be considered serious adverse events (SAEs), suspected unexpected serious adverse reaction |
| index_bge_m3 | `PMC6921499_chunk_024` | _data_collection_other | # Safety monitoring  In this population and within this clinical context, events that can be considered serious adverse events (SAEs), suspected unexpected serious adverse reaction |

### closed loop insulin hypoglycaemia primary endpoint

| Index | Hybrid top-1 | Label | Preview |
|---|---|---|---|
| medical_qwen3_embedding_4b | `PMC7618672_chunk_005` | front_matter | # Keywords  Type 1 diabetes; hybrid closed-loop; insulin pump; continuous glucose monitor; children; adolescents; newly-diagnosed; insulin variability |
| index_bge_small | `PMC6561428_chunk_005` | introduction | # Introduction  Type 1 diabetes is characterised by a deficiency of insulin caused by immunologically mediated damage to pancreatic beta cells, leading to raised blood glucose leve |
| index_bge_m3 | `PMC6561428_chunk_003` | _methods_other | # Abstrac t  Introduction Closed-loop systems titrate insulin based on sensor glucose levels, providing novel means to reduce the risk of hypoglycaemia while improving glycaemic co |

### chemotherapy dose reduction treatment delay adverse events

| Index | Hybrid top-1 | Label | Preview |
|---|---|---|---|
| medical_qwen3_embedding_4b | `PMC5490215_chunk_019` | secondary_outcome | # Secondary outcomes  Secondary endpoints include adverse events (registered for every chemotherapy cycle after CTC criteria version 4.0), dose reductions, treatment delays (which  |
| index_bge_small | `PMC8600696_chunk_015` | intervention | # Dose modifications and prerequisites for the start of a new cycle  Doses will be reduced for haematological and nonhaematological toxicities. In case of concurrent toxicities, al |
| index_bge_m3 | `PMC5490215_chunk_019` | secondary_outcome | # Secondary outcomes  Secondary endpoints include adverse events (registered for every chemotherapy cycle after CTC criteria version 4.0), dose reductions, treatment delays (which  |

### Kaplan Meier survival curve median overall survival

| Index | Hybrid top-1 | Label | Preview |
|---|---|---|---|
| medical_qwen3_embedding_4b | `PMC12928687_chunk_024` | _statistical_analysis_other | # Secondary End Points  Twelve- and 24-month overall survival as well as distant progression-free survival will be evaluated by Kaplan-Meier analysis. All other secondary end point |
| index_bge_small | `PMC6726216_chunk_018` | adverse_events | # Training set: Probability density function / mortality fraction  For the participants in NSABP B15, observed survival at each yearly interval following diagnosis was used to gene |
| index_bge_m3 | `PMC6726216_chunk_018` | adverse_events | # Training set: Probability density function / mortality fraction  For the participants in NSABP B15, observed survival at each yearly interval following diagnosis was used to gene |

### statistical analysis intention to treat population

| Index | Hybrid top-1 | Label | Preview |
|---|---|---|---|
| medical_qwen3_embedding_4b | `PMC11929207_chunk_018` | statistical_analysis | # Statistical analysis  In general, p-values < 0.05 are considered to indicate statistical signifcance (2-tailed test). Te p-values for the secondary endpoints will be presented bu |
| index_bge_small | `PMC11929207_chunk_018` | statistical_analysis | # Statistical analysis  In general, p-values < 0.05 are considered to indicate statistical signifcance (2-tailed test). Te p-values for the secondary endpoints will be presented bu |
| index_bge_m3 | `PMC11929207_chunk_018` | statistical_analysis | # Statistical analysis  In general, p-values < 0.05 are considered to indicate statistical signifcance (2-tailed test). Te p-values for the secondary endpoints will be presented bu |
