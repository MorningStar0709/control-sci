# Summary

There are many ways to make direct self-tuning regulators with good properties. The amount of computation is moderate, since the design calculations are eliminated. It has been shown that the generalized direct self-tuning algorithm, Algorithm 4.2, is very flexible. By using the filter $Q^{*}/P^{*}$ and the prediction horizon, it is possible to determine the behavior of the closed-loop system. It is possible to choose, for instance, moving-average control, generalized minimum-variance control, or pole-zero placement control.

The observer polynomial does not influence the asymptotic properties. It will instead influence the transient properties and can be used to improve the convergence properties of the algorithm. The robustness and sensitivity of the algorithm are also influenced by the filter $Q^{*}/P^{*}$ .

For simplicity, Algorithm 4.2 has been derived for the regulator case, in which the reference value is equal to zero. It is easy to modify the algorithm such that the output follows a reference trajectory; some ideas are suggested in the problems at the end of this chapter and in Section 11.3.

![](image/c0b4f81e69bae0c9f6946ecab208bbf8f6895ab79d5d4b4cd9ef32ae02cab382.jpg)

<details>
<summary>line</summary>

| Time | Subplot (a) | Subplot (b) | Subplot (c) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 100 | ~150 | ~200 | ~300 |
| 200 | ~250 | ~350 | ~450 |
| 300 | ~350 | ~450 | ~600 |
| 400 | ~450 | ~550 | ~700 |
| 500 | ~550 | ~650 | ~800 |
</details>

Figure 4.13 Simulation of the generalized minimum variance self-tuning algorithm on the system in Example 4.8 when (a) $\rho = 0$ (minimum-variance control); (b) $\rho = 4$ ; (c) $\rho = 100$ ("almost" open-loop control).
