# Example 5.19 (dc Servo)

For the dc servo of Example 5.18, calculate $\ell(j\omega)$ with the given parameter variations.

Solution The computation is relatively straightforward. First, $P(j\omega)$ is calculated for 25 values of the parameter pair $(K_m, J_e)$ . Then $P_0(j\omega)$ is calculated from the nominal plant, with $K_{m}=0.05$ , J=0.02, and $J_{m}=8\times15^{-4}$ . Finally, $\Delta(j\omega)$ and $\ell(j\omega)$ are computed using Equations 5.31 and 5.32. Figure 5.30 shows $\ell(j\omega)$ .

![](image/9b85be05c4659570a88182fbf04193a8025bf012c475a5b4b3ef178066130140.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude |
| --- | --- |
| 0 | 0.25 |
| 1 | 0.30 |
| 2 | 0.34 |
| 3 | 0.36 |
| 4 | 0.37 |
| 5 | 0.37 |
| 6 | 0.37 |
| 7 | 0.37 |
| 8 | 0.37 |
| 9 | 0.37 |
| 10 | 0.37 |
</details>

Figure 5.30 Upper bound on the uncertainty

In general, $\ell(j\omega)$ is small at low frequencies and larger at high frequencies. This reflects the fact that low-frequency effects are usually easier to model. The actual $\ell(j\omega)$ used in a design is usually the product of an educated guess; uncertainty is, quite naturally, uncertain.
