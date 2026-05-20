# 4.7 Particle Filtering

Particle filtering is a different approach to the state estimation problem in which statistical sampling is used to approximate the evolution of the conditional density of the state given measurements (Handschin and Mayne, 1969). This method also handles nonlinear dynamic models and can address nonnormally distributed random disturbances to the state and measurement.

Sampled density. Consider a smooth probability density, p(x). In particle filtering we find it convenient to represent this smooth density as a weighted, sampled density, $p _ { s } ( x )$

![](image/9d1cdd61ec424381e3bade4bf104bc8c004f43799588a64c0138c43b473a954f.jpg)

<details>
<summary>line</summary>

| x | p(x) | p_s(x) |
| --- | --- | --- |
| -3.0 | 0.000 | 0.000 |
| -2.0 | 0.050 | 0.000 |
| -1.0 | 0.200 | 0.000 |
| 0.0 | 0.400 | 0.250 |
| 1.0 | 0.200 | 0.150 |
| 2.0 | 0.050 | 0.000 |
| 3.0 | 0.000 | 0.000 |
</details>

![](image/b0a21aa36786ecca53709c08554840d4790d076d52bf4c826d5c88afae8e19a2.jpg)

<details>
<summary>line</summary>

| x | P(x) | P_s(x) |
| --- | --- | --- |
| -4 | 0.000 | 0.000 |
| -3 | 0.000 | 0.000 |
| -2 | 0.000 | 0.000 |
| -1 | 0.100 | 0.100 |
| 0 | 0.500 | 0.500 |
| 1 | 0.800 | 0.800 |
| 2 | 0.950 | 0.950 |
| 3 | 0.990 | 0.990 |
| 4 | 1.000 | 1.000 |
</details>

Figure 4.7: Top: exact density $p ( x )$ and a sampled density $p _ { s } ( x )$ with five samples for $\xi \sim N ( 0 , 1 )$ . Bottom: corresponding exact $P ( x )$ and sampled $P _ { s } ( x )$ cumulative distributions.

$$p (x) \approx p _ {s} (x) := \sum_ {i = 1} ^ {s} w _ {i} \delta (x - x _ {i})$$
