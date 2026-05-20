为 Markov 时间. 据引理 4.2.3 $\xi_{n\wedge \tau_M}$ 为鞅.

注意到 $\{k\leqslant \tau_M\} = \{\tau_M < k\}^c -\{\tau_M\leqslant k - 1\}^c$ 对 $\mathcal{F}_{k - 1}$ 可测，所以对 $k > j,$

$$
\begin{array}{l} E x _ {k} I _ {\{k \leqslant \tau_ {M} \}} x _ {j} I _ {\{j \leqslant \tau_ {m} \}} \\ = E \left(E \left(x _ {k} I _ {\{x _ {k} \leqslant \tau_ {M} \}} x _ {j} I _ {\{j \leqslant \tau_ {M} \}} \mid \mathcal {F} _ {k - 1}\right)\right) \\ = E \left(I _ {\{x _ {k} \leqslant r _ {M} \}} x _ {j} I _ {\{j \leqslant r _ {M} \}} \cdot E \left(x _ {k} \mid \mathcal {F} _ {k - 1}\right)\right) \\ = 0. \\ \end{array}
$$

用引理 4.2.3 便知当 $n \to \infty$ 时， $\xi_{n \wedge \tau_M}$ 收敛到有穷极限。在 $\{\tau_M = \infty\}$ 上， $\xi_{n \wedge \tau_M} = \xi_n$ ，所以当 $n \to \infty$ 时， $\xi_n$ 在 $\{M = \infty\}$ 上收敛到有穷极限。由于 $M$ 是任意的，所以 $\xi_n$ 在 $\bigcup_{M=1}^{\infty} \{\tau_M = \infty\}$ 上收敛。但 $A = \bigcup_{M=1}^{\infty} \{\tau_M = \infty\}$ ，这就证明了定理。

定理 4.2.7 设 $\{x_{k}, F_{k}\}$ 是鞅差列.

i) 若 $E(\sup_k x_k)^+$ < $\infty$ , 则 $\xi_n \stackrel{\mathrm{def}}{=} \sum_{k=1}^{n} x_k$ 在 $A_1 \stackrel{\mathrm{def}}{=} \{\sup_k \xi_k < \infty\}$ 上收敛;  
ii) 若 $E(\inf_k x_k)^{-} < \infty$ , 则 $\xi_n$ 在 $A_2 \stackrel{\mathrm{def}}{=} \{\inf_k \xi_k > -\infty\}$ 上收敛.

证明 只要证明 i) 就够了，因为用 $-x_{k}$ 取代 $x_{k}$ 后，ii) 就归结为 i).

记

$$
\tau_ {M} \stackrel {\mathrm{def}} {=} \left\{ \begin{array}{l l} {\min \{n: \xi_ {n} > M, n \geqslant 1 \},} \\ {\infty , \qquad \text {若} \xi_ {n} \leqslant M, \forall n.} \end{array} \right.
$$

从引理 4.2.2, 4.2.3 知 $(\xi_{k\wedge\tau_{M}}, \mathcal{F}_{k})$ 是鞅. 容易看到

$$
\xi_ {n \wedge \tau_ {M}} = \left\{ \begin{array}{l l} {\leqslant M, \text {若} n <   \tau_ {M},} \\ {= \xi_ {\tau_ {M} - 1} + x _ {\tau_ {M}} \leqslant M + \underset {k} {\sup} x _ {k}, \qquad \text {若} n \geqslant \tau_ {M}.} \end{array} \right.
$$

由此及定理条件知

$$\sup _ {n} E \left(\xi_ {n \wedge \tau_ {M}}\right) ^ {+} \leqslant E \left[ \sup _ {n} \left(\xi_ {n \wedge \tau_ {M}}\right) ^ {+} \right] \leqslant E \left[ M + \left(\sup _ {k} x _ {k}\right) ^ {+} \right] < \infty .$$

由定理4.2.5知当 $n\to \infty$ 时， $\xi_{n\wedge \tau_M}$ a.s.收敛到有穷极限

注意到在 $\{\tau_M = \infty\}$ 上， $\xi_{n \wedge \tau_M} = \xi_n$ ，所以 $\xi_n$ 在 $\{\tau_M = \infty\}$ 上收敛。由于 $A_1 = \bigcup_{M=1}^{\infty} \{\tau_M = \infty\}$ ，所以 $\xi_n$ 在 $A_1$ 上收敛。

定理 4.2.8 (Borel-Cantelli-Lévy) 设 $B_{k} \in F_{k}, \forall k$ . 那么 $\sum_{k=1}^{\infty} I_{B_{k}} < \infty$ 的充分必要条件是 $\sum_{k=1}^{\infty} P(B_{k} | \mathcal{F}_{k-1}) < \infty$ . 换句话说
