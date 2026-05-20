# ◆ ◆ ◆ REMARK

Theorem 7.5 can be used to check stability in this example. Since $S = Q + K^T RK$ and $Q > 0$ , it follows that

$$\mathbf {x} ^ {T} S \mathbf {x} = \mathbf {x} ^ {T} Q \mathbf {x} + \mathbf {x} ^ {T} K ^ {T} R K \mathbf {x} = \mathbf {x} ^ {T} Q \mathbf {x} + (K \mathbf {x}) ^ {T} R (K \mathbf {x}) > 0$$

if $\mathbf{x} \neq 0$ ; as a result, $S$ is positive definite, and detectability of the pair $(A, S^{1/2})$ is assured. To check stability, we must verify that $P \geq 0$ . One way to do this is to

![](image/394ba91cf0ef8966d51a0cd4ea2735c9c4922719c7d59fe5db1190cfaa41e83c.jpg)

<details>
<summary>line</summary>

| Gain k | r = 0 | r = 1 | r = 2 |
| --- | --- | --- | --- |
| 0.5 | ~2.5 | ~3.0 | ~3.5 |
| 1.0 | ~2.5 | ~4.0 | ~5.0 |
| 1.5 | ~2.5 | ~5.0 | ~7.0 |
| 2.0 | ~2.5 | ~6.0 | ~9.0 |
| 2.5 | ~2.5 | ~7.0 | ~11.0 |
| 3.0 | ~2.5 | ~8.0 | ~13.0 |
| 3.5 | ~2.5 | ~9.0 | ~15.0 |
| 4.0 | ~2.5 | ~10.0 | ~17.0 |
| 4.5 | ~2.5 | ~11.0 | ~19.0 |
| 5.0 | ~2.5 | ~12.0 | ~21.0 |
</details>

Figure 7.6 Performance index vs. gain for differential control weights

![](image/3483f0e7bea22de9185c2fcff08ead11048950988785608d00dfee032601c233.jpg)

<details>
<summary>line</summary>

| Gain k | Index J (x₁ = 1, x₂ = 0) | Index J (x₁ = 0, x₂ = 1) |
| --- | --- | --- |
| 0.0 | 30.0 | 5.0 |
| 0.5 | 2.0 | 2.0 |
| 1.0 | 2.5 | 2.0 |
| 1.5 | 3.0 | 2.0 |
| 2.0 | 4.0 | 2.0 |
| 2.5 | 6.0 | 2.0 |
| 3.0 | 8.0 | 2.0 |
| 3.5 | 10.0 | 2.0 |
| 4.0 | 12.0 | 2.0 |
| 4.5 | 15.0 | 2.5 |
| 5.0 | 18.0 | 3.0 |
</details>

Figure 7.7 Performance vs. gain for two different initial states

verify that the principal minors of $P$ (determinants of the $1 \times 1, 2 \times 2, 3 \times 3, \ldots$ matrices formed from the upper left-hand corner) are all positive or zero. In this case, the principal minors are

$$P _ {1 1} = \frac {1}{2 k} + \frac {1}{2} + (r + 1) \frac {k}{2} + r \frac {k ^ {2}}{2}$$

and

$$P _ {1 1} P _ {2 2} - P _ {1 2} ^ {2} = \frac {1}{2 k} + \frac {1}{2} + \frac {(3 r + s)}{4} k + \frac {r}{2} k ^ {2} + \frac {s ^ {2} k ^ {3}}{4}.$$

It is clear that both are positive if $k > 0$ .

The numerical solution of the matrix Lyapunov equation does not follow the by-hand procedure. The most widely used procedure makes use of orthogonal transformations to reduce the problem to a sequence of solutions of linear equations of order 1 or 2 [5].
