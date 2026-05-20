# Zeros

It is not possible to give a simple formula for the mapping of zeros. If a continuous-time transfer function is viewed as a rational function, it has zeros at the zeros of the numerator polynomial and d zeros at infinity, where d is the pole excess for the continuous-time transfer function—that is, the difference between the number of poles and the number of zeros. The discrete-time system has, in general, n - 1 zeros; compare Examples 2.12 and 2.13. The sampling procedure thus gives extra zeros.

![](image/4112283eef00c46847c681dcfd41a6ff17719b908fc82f59a91d7a0bd89719d5.jpg)

<details>
<summary>radar</summary>

| Real axis | Imaginary axis | ζ = 0 | ζ = 0.2 | ζ = 0.4 | ζ = 0.6 | ζ = 0.8 | ζ = 1.0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| -1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| -0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| 0.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| 0.5 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
</details>

Figure 2.8 Loci of constant $\zeta$ (solid) and $\omega_0h$ (dashed) when (2.37) is sampled.

For short sampling periods, a discrete-time system will have zeros in

$$z _ {i} \approx e ^ {s _ {i} h}$$

where the $s_{i}$ 's are the zeros of the continuous-time system. The r = d - 1 zeros introduced by the sampling will go to the zeros of the polynomials $Z_{d}$ in Table 2.4 as the sampling interval goes to zero, because for large s, the transfer function of the continuous-time system is approximately given by $G(s) \approx s^{-d}$ .
