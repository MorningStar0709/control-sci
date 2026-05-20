We next show that choosing a prior weighting that underbounds the MHE arrival cost is the key sufficient condition for stability and convergence of MHE.

![](image/4ea4237b85e3bfb8eae5979317e5ca9dbf54f13f30cd8cded9758e4d3a7f35a0.jpg)

<details>
<summary>line</summary>

| p | Z_k(p) | Γ_k(p) |
| --- | --- | --- |
| x̂(k) | 0 | 0 |
| v̂_k^0 | 0 | 0 |
</details>

Figure 4.1: MHE arrival cost $\hat { Z } _ { k } ( p )$ , underbounding prior weighting $\Gamma _ { k } ( p )$ , and MHE optimal value $\hat { V } _ { k } ^ { 0 . } ,$ for all p and $k > N$ , $\hat { Z } _ { k } ( p ) \ge \Gamma _ { k } ( p ) \ge \hat { V } _ { k } ^ { 0 }$ , and $\hat { Z } _ { k } ( \hat { x } ( k ) ) = \Gamma _ { k } ( \hat { x } ( k ) ) = \hat { V } _ { k } ^ { 0 }$ .

Assumption 4.17 (Prior weighting). We assume that $\Gamma _ { k } ( \cdot )$ is continuous and satisfies the following inequalities for all $k > N$

(a) Upper bound

$$\Gamma_ {k} (p) \leq \hat {Z} _ {k} (p) = \min _ {z, \omega} \Gamma_ {k - N} (z) + \sum_ {i = k - N} ^ {k - 1} \ell_ {i} (\omega (i), \nu (i)) \tag {4.20}$$

subject to $\chi ^ { + } = f ( \chi , \omega ) , \gamma = h ( \chi ) + \nu , \chi ( k ; z , k - N , \omega ) = p .$ .

(b) Lower bound

$$\Gamma_ {k} (p) \geq \hat {V} _ {k} ^ {0} + \underline {{\gamma}} _ {p} (\left| p - \hat {x} (k) \right|) \tag {4.21}$$

in which $\underline { { \gamma } } _ { p } \in \mathcal { K } _ { \infty }$ .

This assumption is depicted in Figure 4.1.

To establish convergence of the MHE estimates, it will prove useful to have an upper bound for the MHE optimal cost. Next we establish the stronger result that the MHE arrival cost is bounded above by the full information arrival cost as stated in the following proposition.

Proposition 4.18 (Arrival cost of full information greater than MHE).

$$\hat {Z} _ {T} (\cdot) \leq Z _ {T} (\cdot) \quad T \geq 1 \tag {4.22}$$

Proof. We know this result holds for $T \in \mathbb { I } _ { 1 : N }$ because MHE is equivalent to full information for these T . Next we show that the inequality at $T$ implies the inequality at $T + N$ . Indeed, we have by the definition of the arrival costs

$$
\begin{array}{l} \hat {Z} _ {T + N} (p) = \min _ {z, \boldsymbol {\omega}} \Gamma_ {T} (z) + \sum_ {i = T} ^ {T + N - 1} \ell_ {i} (\omega (i), \nu (i)) \\ Z _ {T + N} (p) = \min _ {z, \boldsymbol {\omega}} Z _ {T} (z) + \sum_ {i = T} ^ {T + N - 1} \ell_ {i} (\omega (i), \nu (i)) \\ \end{array}
$$
