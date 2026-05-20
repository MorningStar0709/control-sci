# T2: 9-Model Deep Analysis Report

**Generated:** 2026-05-06 | **Models:** 9 | **Questions per model:** 500

---

## 1. Executive Summary

| Rank | Model | Overall | A | B | C | D | Family |
|------|-------|---------|----|----|----|----|--------|
| 1 | MiMo-v2-flash | **0.6470** | 0.6104 | 0.6056 | 0.6360 | 0.7362 | MiMo |
| 2 | DS-v4-flash | **0.6321** | 0.6336 | 0.6312 | 0.7140 | 0.5498 | DeepSeek |
| 3 | Qwen3.5:9b | **0.6249** | 0.5688 | 0.6104 | 0.6620 | 0.6586 | Qwen |
| 4 | DS-v4-pro | **0.6185** | 0.6272 | 0.5904 | 0.7420 | 0.5144 | DeepSeek |
| 5 | MM-m2.5 | **0.6016** | 0.6376 | 0.5192 | 0.6240 | 0.6258 | MiniMax |
| 6 | MM-m2.7 | **0.5735** | 0.6048 | 0.4848 | 0.6120 | 0.5925 | MiniMax |
| 7 | MiMo-v2.5-pro | **0.5391** | 0.5952 | 0.5232 | 0.6020 | 0.4358 | MiMo |
| 8 | MiMo-v2-pro | **0.5142** | 0.6376 | 0.4904 | 0.5600 | 0.3690 | MiMo |
| 9 | MiMo-v2.5 | **0.4396** | 0.6080 | 0.4664 | 0.5280 | 0.1560 | MiMo |

**Winner:** MiMo-v2-flash (0.6470) — 0.2074 ahead of last place (0.4396).

## 2. Statistical Inference

**Kruskal-Wallis Test** (non-parametric ANOVA):
- H = 89.95, df = 8, p = 0.000000 ***
- n = 9 models × 500 records = 4500 total
- Conclusion: **significant differences exist among models**.

### 2.1 Dunn's Post-Hoc (Bonferroni corrected)

Significant pairwise comparisons (p < 0.05):

| Comparison | p-value | Significance |
|-----------|---------|-------------|
| MiMo-v2-flash vs MiMo-v2.5-pro | 0.022221 | * |
| MiMo-v2-flash vs MiMo-v2-pro | 0.001064 | ** |
| MiMo-v2-flash vs MiMo-v2.5 | 0.000000 | *** |
| DS-v4-flash vs MiMo-v2.5-pro | 0.044243 | * |
| DS-v4-flash vs MiMo-v2-pro | 0.002428 | ** |
| DS-v4-flash vs MiMo-v2.5 | 0.000000 | *** |
| Qwen3.5:9b vs MiMo-v2-pro | 0.017184 | * |
| Qwen3.5:9b vs MiMo-v2.5 | 0.000000 | *** |
| DS-v4-pro vs MiMo-v2-pro | 0.010235 | * |
| DS-v4-pro vs MiMo-v2.5 | 0.000000 | *** |
| MM-m2.5 vs MiMo-v2.5 | 0.000001 | *** |
| MM-m2.7 vs MiMo-v2.5 | 0.000200 | *** |
| MiMo-v2.5-pro vs MiMo-v2.5 | 0.005469 | ** |

**13** significant pairs out of 36 total comparisons.

### 2.2 Cohen's d Effect Sizes (Top vs Others)

Reference model: **MiMo-v2-flash** (rank 1)

| vs Model | Cohen's d | Interpretation |
|----------|----------|----------------|
| DS-v4-flash | +0.038 | negligible |
| Qwen3.5:9b | +0.057 | negligible |
| DS-v4-pro | +0.072 | negligible |
| MM-m2.5 | +0.116 | negligible |
| MM-m2.7 | +0.184 | negligible |
| MiMo-v2.5-pro | +0.272 | small |
| MiMo-v2-pro | +0.333 | small |
| MiMo-v2.5 | +0.490 | small |

## 3. Per-Dimension Analysis

### 3.1 Dimension-wise Kruskal-Wallis

| Dimension | H | p | Best | Best Mean | Worst | Worst Mean | Spread |
|-----------|----|----|------|-----------|-------|-----------|--------|
| A | 2.5 | 0.9619 ns | MM-m2.5 | 0.6376 | Qwen3.5:9b | 0.5688 | 0.0688 |
| B | 22.5 | 0.0040 ** | DS-v4-flash | 0.6312 | MiMo-v2.5 | 0.4664 | 0.1648 |
| C | 26.0 | 0.0010 ** | DS-v4-pro | 0.7420 | MiMo-v2.5 | 0.5280 | 0.2140 |
| D | 326.8 | 0.0000 *** | MiMo-v2-flash | 0.7362 | MiMo-v2.5 | 0.1560 | 0.5802 |

### 3.2 Model Dimension Profiles

- **MiMo-v2-flash** (Overall: 0.6470): Best in D (0.7362), weakest in B (0.6056) | Spread: 0.1306
- **DS-v4-flash** (Overall: 0.6321): Best in C (0.7140), weakest in D (0.5498) | Spread: 0.1642
- **Qwen3.5:9b** (Overall: 0.6249): Best in C (0.6620), weakest in A (0.5688) | Spread: 0.0932
- **DS-v4-pro** (Overall: 0.6185): Best in C (0.7420), weakest in D (0.5144) | Spread: 0.2276
- **MM-m2.5** (Overall: 0.6016): Best in A (0.6376), weakest in B (0.5192) | Spread: 0.1184
- **MM-m2.7** (Overall: 0.5735): Best in C (0.6120), weakest in B (0.4848) | Spread: 0.1272
- **MiMo-v2.5-pro** (Overall: 0.5391): Best in C (0.6020), weakest in D (0.4358) | Spread: 0.1662
- **MiMo-v2-pro** (Overall: 0.5142): Best in A (0.6376), weakest in D (0.3690) | Spread: 0.2686
- **MiMo-v2.5** (Overall: 0.4396): Best in A (0.6080), weakest in D (0.1560) | Spread: 0.4520

## 4. Difficulty-Level Analysis

### 4.1 Difficulty-wise Kruskal-Wallis

| Difficulty | H | p | Best | Worst | Spread |
|-----------|----|----|------|-------|--------|
| L1 | 3.0 | 0.9360 ns | MiMo-v2-pro | MM-m2.7 | 0.1375 |
| L2 | 31.5 | 0.0001 *** | MiMo-v2-flash | MiMo-v2.5 | 0.2176 |
| L3 | 38.1 | 0.0000 *** | Qwen3.5:9b | MiMo-v2.5 | 0.2167 |
| L4 | 40.1 | 0.0000 *** | MiMo-v2-flash | MiMo-v2.5 | 0.2541 |

### 4.2 Difficulty Decay Rates

| Model | L1 Mean | L4 Mean | Decay (L1→L4) | Sensitivity |
|-------|---------|---------|---------------|-------------|
| MiMo-v2-flash | 0.6200 | 0.5973 | +0.0227 | 3.7% |
| DS-v4-flash | 0.6875 | 0.5697 | +0.1178 | 17.1% |
| Qwen3.5:9b | 0.6000 | 0.5647 | +0.0353 | 5.9% |
| DS-v4-pro | 0.6450 | 0.5490 | +0.0960 | 14.9% |
| MM-m2.5 | 0.6200 | 0.5344 | +0.0856 | 13.8% |
| MM-m2.7 | 0.5950 | 0.5062 | +0.0888 | 14.9% |
| MiMo-v2.5-pro | 0.6600 | 0.4730 | +0.1870 | 28.3% |
| MiMo-v2-pro | 0.7325 | 0.4580 | +0.2745 | 37.5% |
| MiMo-v2.5 | 0.6450 | 0.3432 | +0.3018 | 46.8% |

- **Most stable** across difficulty: MiMo-v2-flash (decay = +0.0227)
- **Most sensitive** to difficulty: MiMo-v2.5 (decay = +0.3018)

## 5. Model Score Correlation

Mean pairwise Spearman ρ: **0.5689**

| Model Pair | ρ | Strength |
|-----------|------|----------|
| MiMo-v2-flash ↔ DS-v4-flash | 0.618 | Strong |
| MiMo-v2-flash ↔ Qwen3.5:9b | 0.626 | Strong |
| MiMo-v2-flash ↔ DS-v4-pro | 0.606 | Strong |
| MiMo-v2-flash ↔ MM-m2.5 | 0.624 | Strong |
| MiMo-v2-flash ↔ MM-m2.7 | 0.646 | Strong |
| MiMo-v2-flash ↔ MiMo-v2.5-pro | 0.632 | Strong |
| MiMo-v2-flash ↔ MiMo-v2-pro | 0.641 | Strong |
| MiMo-v2-flash ↔ MiMo-v2.5 | 0.242 | Weak |
| DS-v4-flash ↔ Qwen3.5:9b | 0.623 | Strong |
| DS-v4-flash ↔ DS-v4-pro | 0.757 | Strong |
| DS-v4-flash ↔ MM-m2.5 | 0.614 | Strong |
| DS-v4-flash ↔ MM-m2.7 | 0.626 | Strong |
| DS-v4-flash ↔ MiMo-v2.5-pro | 0.651 | Strong |
| DS-v4-flash ↔ MiMo-v2-pro | 0.672 | Strong |
| DS-v4-flash ↔ MiMo-v2.5 | 0.385 | Weak |
| Qwen3.5:9b ↔ DS-v4-pro | 0.598 | Moderate |
| Qwen3.5:9b ↔ MM-m2.5 | 0.624 | Strong |
| Qwen3.5:9b ↔ MM-m2.7 | 0.602 | Strong |
| Qwen3.5:9b ↔ MiMo-v2.5-pro | 0.583 | Moderate |
| Qwen3.5:9b ↔ MiMo-v2-pro | 0.600 | Strong |
| Qwen3.5:9b ↔ MiMo-v2.5 | 0.250 | Weak |
| DS-v4-pro ↔ MM-m2.5 | 0.653 | Strong |
| DS-v4-pro ↔ MM-m2.7 | 0.640 | Strong |
| DS-v4-pro ↔ MiMo-v2.5-pro | 0.674 | Strong |
| DS-v4-pro ↔ MiMo-v2-pro | 0.662 | Strong |
| DS-v4-pro ↔ MiMo-v2.5 | 0.386 | Weak |
| MM-m2.5 ↔ MM-m2.7 | 0.692 | Strong |
| MM-m2.5 ↔ MiMo-v2.5-pro | 0.575 | Moderate |
| MM-m2.5 ↔ MiMo-v2-pro | 0.619 | Strong |
| MM-m2.5 ↔ MiMo-v2.5 | 0.345 | Weak |
| MM-m2.7 ↔ MiMo-v2.5-pro | 0.585 | Moderate |
| MM-m2.7 ↔ MiMo-v2-pro | 0.611 | Strong |
| MM-m2.7 ↔ MiMo-v2.5 | 0.327 | Weak |
| MiMo-v2.5-pro ↔ MiMo-v2-pro | 0.727 | Strong |
| MiMo-v2.5-pro ↔ MiMo-v2.5 | 0.347 | Weak |
| MiMo-v2-pro ↔ MiMo-v2.5 | 0.417 | Moderate |

## 6. Cross-Model Issue Patterns

### 6.1 Top-10 Issues (Aggregated)

| Rank | Issue | Total Count | Models Affected |
|------|-------|-------------|-----------------|
| 1 | target failure | 342 | 6/9 |
| 2 | LLM judge response parse failure | 53 | 9/9 |
| 3 | judge parse failure | 15 | 7/9 |
| 4 | 回答内容与标准答案无关 | 3 | 2/9 |
| 5 | 核心结论与标准答案不一致 | 3 | 3/9 |
| 6 | 模型回答未给出标准答案中的目标函数和约束条件 | 2 | 2/9 |
| 7 | 模型回答未使用标准答案中的符号θ_i和η_i | 2 | 2/9 |
| 8 | 未给出标准答案中的具体初始误差向量数值 | 2 | 2/9 |
| 9 | 最终结论错误 | 2 | 2/9 |
| 10 | 未给出标准答案中的具体数学表达式 | 2 | 2/9 |

## 7. Generated Charts

- **Overall Score Bar Chart (95% CI)**: `fig1_overall_bar.png`
- **Model × Dimension Heatmap**: `fig2_dimension_heatmap.png`
- **Difficulty-Level Boxplots**: `fig3_difficulty_boxplot.png`
- **Cohen's d Pairwise Matrix**: `fig4_cohens_d.png`
- **Score Correlation + Hierarchical Clustering**: `fig5_correlation_cluster.png`
- **Difficulty-Sensitivity Curves**: `fig6_difficulty_curves.png`
- **Model Dimension Radar Profiles**: `fig7_model_radar.png`

## 8. Methodology Notes

- **Kruskal-Wallis**: Non-parametric alternative to one-way ANOVA; does not assume normality.
- **Dunn's Post-hoc**: Multiple comparison correction via Bonferroni; identifies _which_ pairs differ.
- **Cohen's d**: Pooled standard deviation; thresholds: small (0.2), medium (0.5), large (0.8).
- **Spearman ρ**: Rank correlation; robust to non-linear monotonic relationships.
- **Hierarchical Clustering**: Average linkage on (1 − ρ) distance matrix.
- **95% CI**: ±1.96 × SE; assumes asymptotic normality (n=500, CLT applies).
