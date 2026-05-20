# 4.2.2 Duality of Linear Estimation and Regulation

For linear systems, the estimate error $\tilde { x }$ in full information and state x in regulation to the origin display an interesting duality that we summarize briefly here. Consider the following steady-state estimation and infinite horizon regulation problems.

Estimator problem.

$$x (k + 1) = A x (k) + G w (k)\mathcal {Y} (k) = C x (k) + \nu (k)R > 0 \quad Q > 0 \quad (A, C) \text {detectable} \quad (A, G) \text {stabilizable}\tilde {x} (k + 1) = \left(A - \tilde {L} C\right) \tilde {x} (k)$$

Regulator problem.

$$x (k + 1) = A x (k) + B u (k)y (k) = C x (k)R > 0 \quad Q > 0 \quad (A, B) \text { stabilizable } \quad (A, C) \text { detectable }x (k + 1) = (A + B K) x (k)$$

<table><tr><td>Regulator</td><td>Estimator</td></tr><tr><td>A</td><td> $A'$ </td></tr><tr><td>B</td><td> $C'$ </td></tr><tr><td>C</td><td> $G'$ </td></tr><tr><td>k</td><td> $l = N - k$ </td></tr><tr><td> $\Pi(k)$ </td><td> $P^{-}(l)$ </td></tr><tr><td> $\Pi(k-1)$ </td><td> $P^{-}(l+1)$ </td></tr><tr><td> $\Pi$ </td><td> $P^{-}$ </td></tr><tr><td>Q</td><td>Q</td></tr><tr><td>R</td><td>R</td></tr><tr><td> $P_f$ </td><td> $P^{-}(0)$ </td></tr><tr><td>K</td><td> $-\tilde{L}'$ </td></tr><tr><td> $A + BK$ </td><td> $(A - \tilde{L}C)'$ </td></tr><tr><td>x</td><td> $\tilde{x}'$ </td></tr></table>

<table><tr><td>Regulator</td><td>Estimator</td></tr><tr><td> $R > 0$ ,  $Q > 0$ </td><td> $R > 0$ ,  $Q > 0$ </td></tr><tr><td>(A,B) stabilizable</td><td>(A,C) detectable</td></tr><tr><td>(A,C) detectable</td><td>(A,G) stabilizable</td></tr></table>

Table 4.2: Duality variables and stability conditions for linear quadratic regulation and least squares estimation.

In Appendix A, we derive the dual dynamic system following the approach in Callier and Desoer (1991), and obtain the duality variables in regulation and estimation listed in Table 4.2.

We also have the following result connecting controllability of the original system and observability of the dual system

Lemma 4.9 (Duality of controllability and observability). (A, B) is controllable (stabilizable) if and only $i f \left( A ^ { \prime } , B ^ { \prime } \right)$ is observable (detectable).
