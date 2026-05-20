# T3: 深度分析扩展 — A6~A9

**Generated:** 2026-05-09 | **Models:** 9 | **Questions per model:** 500

---

## A6: 评分分布 (Score Distribution)

| Model | Mean | Std | Skew | Kurt | Q25 | Median | Q75 | IQR | Zeros% |
|-------|------|-----|------|------|-----|--------|-----|-----|--------|
| MiMo-v2-flash | 0.6470 | 0.3890 | -0.64 | -1.18 | 0.2500 | 0.7800 | 1.0000 | 0.7500 | 18.2% |
| DS-v4-flash | 0.6321 | 0.3951 | -0.50 | -1.36 | 0.2500 | 0.7700 | 1.0000 | 0.7500 | 17.2% |
| Qwen3.5:9b | 0.6249 | 0.3852 | -0.49 | -1.29 | 0.2500 | 0.7200 | 1.0000 | 0.7500 | 17.2% |
| DS-v4-pro | 0.6185 | 0.4079 | -0.44 | -1.47 | 0.2000 | 0.7500 | 1.0000 | 0.8000 | 19.4% |
| MM-m2.5 | 0.6016 | 0.3947 | -0.42 | -1.38 | 0.2000 | 0.6900 | 1.0000 | 0.8000 | 20.6% |
| MM-m2.7 | 0.5735 | 0.4108 | -0.31 | -1.56 | 0.1650 | 0.6900 | 1.0000 | 0.8350 | 24.4% |
| MiMo-v2.5-pro | 0.5391 | 0.4043 | -0.05 | -1.61 | 0.1800 | 0.5000 | 1.0000 | 0.8200 | 21.6% |
| MiMo-v2-pro | 0.5142 | 0.4084 | +0.08 | -1.64 | 0.1200 | 0.4400 | 1.0000 | 0.8800 | 21.8% |
| MiMo-v2.5 | 0.4396 | 0.4556 | +0.25 | -1.78 | 0.0000 | 0.2750 | 1.0000 | 1.0000 | 45.8% |

### Distribution Charts

- **A6 Density Ridges**: `a6_density_ridges.png` — Per-model score density curves
- **A6 Skewness vs Mean**: `a6_skewness_vs_mean.png` — Distribution shape vs central tendency
- **A6 ECDF**: `a6_ecdf.png` — Empirical cumulative distribution functions

## A7: 维度 κ 一致性 (Dimension Agreement)

**Kendall's W (Coefficient of Concordance):** 0.4420

- Friedman χ² = 11.93, p = 0.0076 **
- ICC(2,1) = 0.1962

### Pairwise Dimension Spearman ρ

| Dimension Pair | ρ | Significance |
|---------------|----|-------------|
| A↔B | -0.0586 | ns |
| A↔C | 0.0586 | ns |
| A↔D | -0.1423 | ns |
| B↔C | 0.8167 | ** |
| B↔D | 0.5500 | ns |
| C↔D | 0.5667 | ns |

### Charts
- **A7 Dimension Agreement**: `a7_dimension_agreement.png` — Score matrix normalized by dimension
- **A7 Concordance Radar**: `a7_concordance_radar.png` — Polar plot of dimension profiles

## A8: 难度矩阵 (Difficulty Matrix)

| Model | L1 | L2 | L3 | L4 | AbsΔ | RelΔ |
|-------|----|----|----|----|------|------|
| MiMo-v2-flash | 0.6200 | 0.7009 | 0.6471 | 0.5973 | 0.0227 | 3.7% |
| DS-v4-flash | 0.6875 | 0.6685 | 0.6396 | 0.5697 | 0.1178 | 17.1% |
| Qwen3.5:9b | 0.6000 | 0.6613 | 0.6501 | 0.5647 | 0.0353 | 5.9% |
| DS-v4-pro | 0.6450 | 0.6618 | 0.6328 | 0.5490 | 0.0960 | 14.9% |
| MM-m2.5 | 0.6200 | 0.6359 | 0.6244 | 0.5344 | 0.0856 | 13.8% |
| MM-m2.7 | 0.5950 | 0.6016 | 0.6014 | 0.5062 | 0.0888 | 14.9% |
| MiMo-v2.5-pro | 0.6600 | 0.5612 | 0.5470 | 0.4730 | 0.1870 | 28.3% |
| MiMo-v2-pro | 0.7325 | 0.5293 | 0.4963 | 0.4580 | 0.2745 | 37.5% |
| MiMo-v2.5 | 0.6450 | 0.4833 | 0.4334 | 0.3432 | 0.3018 | 46.8% |

**Most stable:** MiMo-v2-flash (decay=0.0227)

**Most sensitive:** MiMo-v2.5 (decay=0.3018)

### Item Difficulty Distribution

Mean item difficulty (all models): **0.5767**

| Category | Count | % |
|----------|-------|---|
| very_hard (0.0-0.2) | 80 | 16.0% |
| hard (0.2-0.4) | 75 | 15.0% |
| medium (0.4-0.6) | 111 | 22.2% |
| easy (0.6-0.8) | 76 | 15.2% |
| very_easy (0.8-1.0) | 158 | 31.6% |

### Charts
- **A8 Difficulty Matrix**: `a8_difficulty_matrix.png` — Model × Difficulty level heatmap
- **A8 Decay Curves**: `a8_decay_curves.png` — Score decay L1→L4 per model
- **A8 Item Difficulty Histogram**: `a8_item_difficulty_hist.png` — Distribution of item p-values

## A9: 长度偏见 (Length Bias)

**Global Pearson r:** -0.0232 ns
**Global Spearman ρ:** 0.0356 *

| Model | AvgLen | Min | Max | Pearson r | p | Spearman ρ | p |
|-------|--------|-----|-----|-----------|----|------------|----|
| MiMo-v2-flash | 3862 | 87 | 7754 | -0.0946 | * | -0.1832 | *** |
| DS-v4-flash | 2747 | 39 | 8286 | -0.3332 | *** | -0.2890 | *** |
| Qwen3.5:9b | 3914 | 140 | 7984 | -0.2946 | *** | -0.3434 | *** |
| DS-v4-pro | 2478 | 0 | 8235 | -0.1191 | ** | 0.0144 | ns |
| MM-m2.5 | 2840 | 0 | 11758 | 0.2031 | *** | 0.2110 | *** |
| MM-m2.7 | 2646 | 0 | 10928 | 0.2892 | *** | 0.3272 | *** |
| MiMo-v2.5-pro | 3024 | 0 | 7798 | -0.2405 | *** | -0.0806 | † |
| MiMo-v2-pro | 3188 | 0 | 16122 | -0.3122 | *** | -0.1548 | *** |
| MiMo-v2.5 | 762 | 0 | 4536 | 0.5207 | *** | 0.6905 | *** |

### Dimension Breakdown

- **Dim A**: Pearson r = 0.0366 ns
- **Dim B**: Pearson r = -0.0760 *
- **Dim C**: Pearson r = -0.1483 ***
- **Dim D**: Pearson r = 0.3651 ***

### Charts
- **A9 Length vs Score**: `a9_length_vs_score.png` — Scatter plot per model with regression line
- **A9 Length Distribution**: `a9_length_distribution.png` — Histogram + binned mean score
- **A9 Length Ratio**: `a9_length_ratio.png` — Model/Expected length ratio vs score

## Methodology Notes

- **A6**: Skewness = Fisher-Pearson standardized moment; Kurtosis = Fisher (excess, 0=normal). Dip test requires `scipy.stats` or `diptest` package.
- **A7**: Kendall's W measures rank concordance across dimensions (0=no agreement, 1=perfect). ICC(2,1) = two-way random effects, single rater.
- **A8**: Item difficulty = mean score across all 9 models (classical test theory p-value). Decay = L1 - L4 absolute difference.
- **A9**: Length = len(model_answer) in characters. Both Pearson (linear) and Spearman (monotonic) correlations reported.
