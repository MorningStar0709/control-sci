# 4.7.2 Sampling and Importance Sampling

Consider a random variable $\xi$ with a smooth probability density $p ( x )$ . Assume one is able to draw samples $x _ { i }$ of $\xi$ with probability

$$p _ {\mathrm{sa}} \left(x _ {i}\right) = p \left(x _ {i}\right) \tag {4.38}$$

in which $p _ { \mathtt { S a } } ( x _ { i } )$ denotes the probability of drawing a sample with value $x _ { i }$ . In this case, if one draws s samples, a sampled density for $\xi$ is given by

$$p _ {s} (x) = \sum_ {i} w _ {i} \delta (x - x _ {i}) \quad w _ {i} = 1 / s, \quad i = 1, \dots , s \tag {4.39}$$

and the weights are all equal to $1 / s .$ .

Convergence of sampled densities. It is instructive to examine how a typical sampled density converges with sample size to the density from which the samples are drawn. Consider a set of s samples. When drawing multiple samples of a density, we assume the samples are mutually independent

$$p _ {\mathrm{sa}} (x _ {1}, x _ {2}, \dots , x _ {s}) = p _ {\mathrm{sa}} (x _ {1}) p _ {\mathrm{sa}} (x _ {2}) \cdot \cdot \cdot p _ {\mathrm{sa}} (x _ {s})$$

We denote the cumulative distribution of the sampled density as

$$P _ {s} (x; s) = \sum_ {i \in \mathbb {I} _ {x}} w _ {i} \quad \mathbb {I} _ {x} = \{i | x _ {i} \leq x \}$$

in which the second argument s is included to indicate $P _ { s } { ' } s$ dependence on the sample size. The value of $P _ { s }$ is itself a random variable because it is determined by the sample values $x _ { i }$ and weights $w _ { i }$ . We consider the case with equal sample weights $w _ { i } = 1 / s$ and study the $P _ { s }$ values as a function of s and scalar x. They take values in the range

![](image/24a0b95300d97879f7f7df0866805d1ecf9b2845264ba6d82f151a05c00d81f9.jpg)

<details>
<summary>bar</summary>

| Ps Range | Pr(Ps) |
| --- | --- |
| 0.0 | 0.03 |
| 0.2 | 0.15 |
| 0.4 | 0.31 |
| 0.6 | 0.31 |
| 0.8 | 0.15 |
| 1.0 | 0.03 |
</details>

Figure 4.10: Probability density $\operatorname* { P r } ( P _ { s } ( x ; s ) )$ for x corresponding to $P ( x ) = 0 . 5$ and $s = 5$ samples. The distribution is centered at correct value, $P ( x )$ , but the variance is large.

$$P _ {s} \in \left\{0, \frac {1}{s}, \dots , \frac {s - 1}{s}, 1 \right\} \quad s \geq 1 \quad - \infty < x < \infty$$

Given the sampling process we can readily evaluate the probability of $P _ { s }$ over this set
