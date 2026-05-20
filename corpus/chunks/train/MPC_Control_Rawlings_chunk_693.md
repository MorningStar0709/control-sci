# Solution

(a) The first 10 iterations of the noncooperative steady-state calculation are shown in Figure 6.2. Notice the iteration is unstable and the steady-state target does not converge. The cooperative case is shown in Figure 6.3. This case is stable and the iterations converge to the centralized target and achieve zero offset. The magnitudes of the eigenvalues of $L _ { s }$ for the noncooperative (nc) and cooperative (co) cases are given by

$$\left| \operatorname{eig} \left(L _ {s n c}\right) \right| = \{1. 1 2, 1. 1 2 \} \quad \left| \operatorname{eig} \left(L _ {s c o}\right) \right| = \{0. 7 5 7, 0. 2 4 3 \}$$

Stability of the iteration is determined by the magnitudes of the eigenvalues of $L _ { s }$ .

(b) Reversing the pairings leads to the following gain matrix in which we have reversed the labels of the outputs for the two systems

$$
\left[ \begin{array}{c} y _ {1 s} \\ y _ {2 s} \end{array} \right] = \left[ \begin{array}{c c} 2. 0 & 1. 0 \\ - 0. 5 & 1. 0 \end{array} \right] \left[ \begin{array}{c} u _ {1 s} \\ u _ {2 s} \end{array} \right]
$$

The first 10 iterations of the noncooperative and cooperative games are shown in Figures 6.4 and 6.5. For this pairing, the noncooperative case also converges to the centralized target. The eigenvalues are given by

$$\left| \operatorname{eig} \left(L _ {s n c}\right) \right| = \{0. 5 5 9, 0. 5 5 9 \} \quad \left| \operatorname{eig} \left(L _ {s c o}\right) \right| = \{0. 7 5 7, 0. 2 4 3 \}$$

The eigenvalues of the cooperative case are unaffected by the reversal of pairings. -

Given the stability analysis of the simple unconstrained two-player game, we remove from further consideration two options we have been

![](image/53cb59f35cb397ffeafed553f565ee782c399637c47631facd46a487faf230c1.jpg)

<details>
<summary>scatter</summary>

| u1 | u2 | Label |
| --- | --- | --- |
| -2.5 | 2.0 | y1 = 1 |
| -1.5 | 3.0 | ude |
| -0.5 | 5.0 | y2 = 1 |
| 0.5 | 3.0 | uce |
| 1.5 | 3.0 | y2 = 1 |
| 2.5 | 0.5 | uce |
| 4.0 | 3.5 | y2 = 1 |
| 4.5 | -2.0 | y1 = 1 |
</details>

Figure 6.2: Ten iterations of the noncooperative steady-state calculation, $u ^ { [ 0 ] } = u _ { d e }$ iterations are unstable, $u ^ { p } \to \infty$ .

![](image/934e1e0fc2a61e846e25d78935a141381e1ac0dc4da37632f418eaf815015bae.jpg)  
Figure 6.3: Ten iterations of the cooperative steady-state calculation, $u ^ { [ 0 ] } = u _ { d e }$ ; iterations are stable, $u ^ { p } \to u _ { c e }$ .

![](image/a5be229845b524e94840ba6a368f9a0af45bbc316a48a891f6b0a126c00a0faa.jpg)
