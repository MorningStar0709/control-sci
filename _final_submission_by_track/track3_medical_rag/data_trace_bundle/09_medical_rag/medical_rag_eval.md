# Medical RAG Evaluation

- Cases: 8
- Case set: en
- Top-k: 3
- Synthesis: disabled

## Summary

| Index | Provider | Model | Hit@K | Label Hit@K | Mean Hit Rank | Citation Coverage | Bridged | Multi-query | Query Embed Sec |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| medical_qwen3_embedding_4b | ollama | qwen3-embedding:4b | 8/8 | 7/8 | 1.00 |  | 0 | 0 | 3.562 |
| index_bge_small | hf | BAAI/bge-small-en-v1.5 | 8/8 | 6/8 | 1.25 |  | 0 | 0 | 9.291 |
| index_bge_m3 | hf | BAAI/bge-m3 | 8/8 | 8/8 | 1.00 |  | 0 | 0 | 3.302 |

## Case Details

### primary_endpoint_safety: primary endpoint adverse events

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| medical_qwen3_embedding_4b | True | True | primary endpoint adverse events | `PMC12574440_chunk_034` | outcome_measures | # Other secondary efficacy endpoints |
| index_bge_small | True | True | primary endpoint adverse events | `PMC11929207_chunk_020` | primary_outcome | # Primary endpoint  Te primary endpoint, 28-day mortality, will be analyzed using a mixed-efects binary logistic regression [31]. Tis regression will include treatment efect and source of sepsis as fxed efects and site a |
| index_bge_m3 | True | True | primary endpoint adverse events | `PMC8600696_chunk_007` | _introduction_other | # Endpoints  The primary endpoint is overall survival after R0/R1 resection (OS-res) (only patients with R0/R1 resection).  Secondary efficacy endpoints are OS of the entire patients cohort, R0/R1 resection rate and prog |

### survival_endpoint: overall survival progression free survival

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| medical_qwen3_embedding_4b | True | True | overall survival progression free survival | `PMC10882371_chunk_024` | outcome_measures | # Tertiary outcome measures |
| index_bge_small | True | False | overall survival progression free survival | `PMC12928687_chunk_024` | _statistical_analysis_other | # Secondary End Points  Twelve- and 24-month overall survival as well as distant progression-free survival will be evaluated by Kaplan-Meier analysis. All other secondary end points will be descriptively summarized. |
| index_bge_m3 | True | True | overall survival progression free survival | `PMC6937062_chunk_026` | outcome_measures | # Clinical outcome measures  1. Time to PSA progression; Confirmed rising PSA more than 12 weeks after randomisation. (Where there has been a decline in PSA from baseline, progression will be a 25% or greater increase, a |

### eligibility: inclusion criteria randomized controlled trial

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| medical_qwen3_embedding_4b | True | True | inclusion criteria randomized controlled trial | `PMC6561428_chunk_012` | _randomization_other | # Box 1 Inclusion and exclusion criteria |
| index_bge_small | True | True | inclusion criteria randomized controlled trial | `PMC12898571_chunk_006` | population | # 2.2. Participants and Sample Size  The following inclusion and exclusion criteria were applied to select eligible participants for the study. |
| index_bge_m3 | True | True | inclusion criteria randomized controlled trial | `PMC12574440_chunk_008` | _methods_other | # Inclusion criteria  1. The participant has CFRD requiring insulin therapy for >3 months.    2. The participant is 16 years of age or older.    3. Baseline time in target glucose range <80% during the run-in period.     |

### safety_sae: safety endpoint serious adverse event

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| medical_qwen3_embedding_4b | True | False | safety endpoint serious adverse event | `PMC7470506_chunk_024` | ethical_approval | # SAFETY, ETHICS AND DISSEMINATION |
| index_bge_small | True | True | safety endpoint serious adverse event | `PMC6921499_chunk_024` | _data_collection_other | # Safety monitoring  In this population and within this clinical context, events that can be considered serious adverse events (SAEs), suspected unexpected serious adverse reactions (SUSA Rs) or serious adverse device ev |
| index_bge_m3 | True | True | safety endpoint serious adverse event | `PMC6921499_chunk_024` | _data_collection_other | # Safety monitoring  In this population and within this clinical context, events that can be considered serious adverse events (SAEs), suspected unexpected serious adverse reactions (SUSA Rs) or serious adverse device ev |

### closed_loop_diabetes: closed loop insulin hypoglycaemia primary endpoint

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| medical_qwen3_embedding_4b | True | True | closed loop insulin hypoglycaemia primary endpoint | `PMC7618672_chunk_005` | front_matter | # Keywords  Type 1 diabetes; hybrid closed-loop; insulin pump; continuous glucose monitor; children; adolescents; newly-diagnosed; insulin variability |
| index_bge_small | True | False | closed loop insulin hypoglycaemia primary endpoint | `PMC6561428_chunk_005` | introduction | # Introduction  Type 1 diabetes is characterised by a deficiency of insulin caused by immunologically mediated damage to pancreatic beta cells, leading to raised blood glucose levels. Diabetes is one of the most common m |
| index_bge_m3 | True | True | closed loop insulin hypoglycaemia primary endpoint | `PMC6561428_chunk_003` | _methods_other | # Abstrac t  Introduction Closed-loop systems titrate insulin based on sensor glucose levels, providing novel means to reduce the risk of hypoglycaemia while improving glycaemic control. We will assess effectiveness of 6 |

### chemo_toxicity: chemotherapy dose reduction treatment delay adverse events

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| medical_qwen3_embedding_4b | True | True | chemotherapy dose reduction treatment delay adverse events | `PMC5490215_chunk_019` | secondary_outcome | # Secondary outcomes  Secondary endpoints include adverse events (registered for every chemotherapy cycle after CTC criteria version 4.0), dose reductions, treatment delays (which follow the standardized guidelines of th |
| index_bge_small | True | True | chemotherapy dose reduction treatment delay adverse events | `PMC8600696_chunk_015` | intervention | # Dose modifications and prerequisites for the start of a new cycle  Doses will be reduced for haematological and nonhaematological toxicities. In case of concurrent toxicities, all dose modifications should be based on  |
| index_bge_m3 | True | True | chemotherapy dose reduction treatment delay adverse events | `PMC5490215_chunk_019` | secondary_outcome | # Secondary outcomes  Secondary endpoints include adverse events (registered for every chemotherapy cycle after CTC criteria version 4.0), dose reductions, treatment delays (which follow the standardized guidelines of th |

### kaplan_meier: Kaplan Meier survival curve median overall survival

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| medical_qwen3_embedding_4b | True | True | Kaplan Meier survival curve median overall survival | `PMC12928687_chunk_024` | _statistical_analysis_other | # Secondary End Points  Twelve- and 24-month overall survival as well as distant progression-free survival will be evaluated by Kaplan-Meier analysis. All other secondary end points will be descriptively summarized. |
| index_bge_small | True | True | Kaplan Meier survival curve median overall survival | `PMC6726216_chunk_018` | adverse_events | # Training set: Probability density function / mortality fraction  For the participants in NSABP B15, observed survival at each yearly interval following diagnosis was used to generate a survival curve for the group as a |
| index_bge_m3 | True | True | Kaplan Meier survival curve median overall survival | `PMC6726216_chunk_018` | adverse_events | # Training set: Probability density function / mortality fraction  For the participants in NSABP B15, observed survival at each yearly interval following diagnosis was used to generate a survival curve for the group as a |

### itt_population: statistical analysis intention to treat population

| Index | Hit | Label Hit | Search Query | Top-1 | Label | Preview |
|---|---|---|---|---|---|---|
| medical_qwen3_embedding_4b | True | True | statistical analysis intention to treat population | `PMC11929207_chunk_018` | statistical_analysis | # Statistical analysis  In general, p-values < 0.05 are considered to indicate statistical signifcance (2-tailed test). Te p-values for the secondary endpoints will be presented but considered descriptive and hypothesis  |
| index_bge_small | True | True | statistical analysis intention to treat population | `PMC11929207_chunk_018` | statistical_analysis | # Statistical analysis  In general, p-values < 0.05 are considered to indicate statistical signifcance (2-tailed test). Te p-values for the secondary endpoints will be presented but considered descriptive and hypothesis  |
| index_bge_m3 | True | True | statistical analysis intention to treat population | `PMC11929207_chunk_018` | statistical_analysis | # Statistical analysis  In general, p-values < 0.05 are considered to indicate statistical signifcance (2-tailed test). Te p-values for the secondary endpoints will be presented but considered descriptive and hypothesis  |
