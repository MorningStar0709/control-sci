# EXAMPLE 2.16 Different estimation methods

In the previous examples the RLS and ELS methods were used. Simplified estimation methods based on projection were discussed in Section 2.2. Three different projection algorithms will now be compared with the RLS method. All have the following form:

$$\hat {\theta} (t) = \hat {\theta} (t - 1) + P (t) \varphi (t) \left(y (t) - \varphi^ {T} (t) \hat {\theta} (t - 1)\right) \tag {2.54}$$

![](image/a5b6e97b68a3a0a1d9a6fd29bdf33c790c46e042eb281b18d5cccb0b0e42f335.jpg)

<details>
<summary>line</summary>

| Time | Ê | â |
| --- | --- | --- |
| 0 | 1.0 | -1.0 |
| 200 | 0.5 | -1.0 |
| 400 | 0.5 | -1.0 |
| 600 | 0.5 | -1.0 |
| 800 | 0.5 | -1.0 |
| 1000 | 0.5 | -1.0 |
</details>

![](image/d4a3ebd599e379f823f5de0decc6c5539c6a373b2fcb2418eac4ef176f033752.jpg)

<details>
<summary>line</summary>

| Time | Ê | â |
| --- | --- | --- |
| 0 | 1.0 | -1.0 |
| 200 | 0.5 | -1.0 |
| 400 | 0.5 | -1.0 |
| 600 | 0.5 | -1.0 |
| 800 | 0.5 | -1.0 |
| 1000 | 0.5 | -1.0 |
</details>

![](image/9fd833724e007bb5956b65c7d6e6e413f49834563bd8edb3c3e98a7cb359c5df.jpg)

<details>
<summary>line</summary>

| Time | b̂ | â |
| --- | --- | --- |
| 0 | 1.0 | -1.0 |
| 200 | 0.5 | -1.0 |
| 600 | 0.5 | -1.0 |
| 1000 | 0.5 | -1.0 |
</details>

![](image/d8a33a5963fdaf3981cd1125941308eeec65bef5d81e45f2fd496ebaff7d0a62.jpg)

<details>
<summary>line</summary>

| Time | b̂ | â |
| --- | --- | --- |
| 0 | ~1.0 | ~-0.5 |
| 200 | ~0.5 | ~-0.8 |
| 600 | ~0.3 | ~-0.7 |
| 1000 | ~0.4 | ~-0.6 |
</details>

Figure 2.12 Estimates of the parameters in the process (2.53) when RLS is used and (a) $\lambda = 1$ , (b) $\lambda = 0.999$ , (c) $\lambda = 0.99$ , and (d) $\lambda = 0.95$ .

Compare with Eq. (2.24). The scalar gain $P(t)$ is given by the following algorithms.

Least mean squares (LMS):

$$P (t) = \gamma$$

Projection algorithm (PA):

$$P (t) = \frac {\gamma}{\alpha + \varphi^ {T} (t) \varphi (t)} \quad \alpha \geq 0, \quad 0 < \gamma < 2$$

Stochastic approximation (SA):

$$P (t) = \frac {\gamma}{\Sigma_ {i = 1} ^ {t} \varphi^ {T} (i) \varphi (i)}$$
