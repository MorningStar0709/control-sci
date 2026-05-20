# 9.3.3 Variance

Informally, variance is a measure of how far the outcome of a random variable deviates from its mean. Later, we will use variance to quantify how confident we are in the estimate of a random variable; we can’t know the true value of that variable without randomness, but we can give a bound on its randomness.

$$\operatorname{var} (x) = \sigma^ {2} = E [ (x - \overline {{x}}) ^ {2} ] = \int_ {- \infty} ^ {\infty} (x - \overline {{x}}) ^ {2} p (x) d x$$

The standard deviation is the square root of the variance.

$$\operatorname{std} [ x ] = \sigma = \sqrt {\operatorname{var} (x)}$$

![](image/f5b30f5e7dbec8de4f37c6894e6eed340a53e1950901c18a880489032e5d1be1.jpg)

<details>
<summary>surface_3d</summary>

| x | y | p(x, y) |
| --- | --- | --- |
| -1.0 | 0.0 | 0.0 |
| -0.5 | 0.5 | 0.2 |
| 0.0 | 1.0 | 0.4 |
| 0.5 | 1.5 | 0.6 |
| 1.0 | 2.0 | 0.0 |
</details>

Figure 9.2: Joint probability density function
