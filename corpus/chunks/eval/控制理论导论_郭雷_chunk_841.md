$$\left(\boldsymbol {A} ^ {d n + d}\right) _ {i j} = \left(\boldsymbol {A} ^ {d n}\right) _ {i j} = \left(\boldsymbol {A} ^ {d}\right) _ {i i _ {0}} ^ {+} \left(\boldsymbol {A} ^ {d}\right) _ {i _ {0} j} ^ {+}, \quad \forall n > n _ {0}. \tag {11.4.15}$$

由于 $i_0$ 在长为 $n$ 的最重路上，所以易知

$$(A ^ {d n}) _ {i j} = \sum_ {i _ {0} \in \mathcal {N} _ {i j}} (A ^ {d}) _ {i i _ {0}} ^ {+} (A ^ {d}) _ {i _ {0} j} ^ {+} = \sum_ {i _ {0} \in \mathcal {N}} (A ^ {d}) _ {i i _ {0}} ^ {+} (A ^ {d}) _ {i _ {0} j} ^ {+}, \quad \forall n > n _ {0}. \tag {11.4.16}$$

若 $i$ 到 $j$ 无路，则 $(A^{dn})_{ij} = -\infty, \forall n,$ 从而也有式 (11.4.16) 成立。综上所述，有

$$\boldsymbol {A} ^ {d n + d} = \boldsymbol {A} ^ {d n}, \quad \forall n > \max _ {i, j} n _ {0} (i, j) =: n _ {0}. \tag {11.4.17}$$

上式两边同乘 $A^h$ ，得到

$$\boldsymbol {A} ^ {d n + h + d} = \boldsymbol {A} ^ {d n + h}, \quad \forall n > n _ {0}, 0 \leqslant h < d$$

对于 $\lambda \neq e$ ，可在 $A_{\lambda}$ 上同样讨论，得到

$$\left(\frac {1}{\lambda} \boldsymbol {A}\right) ^ {d n + h + d} = \left(\frac {1}{\lambda} \boldsymbol {A}\right) ^ {d n + h}, \quad \boldsymbol {A} ^ {d n + h + d} = \lambda^ {d} \boldsymbol {A} ^ {d n + d}, \quad 0 \leqslant h < d, \forall n > n _ {0}.$$

所以 A 是 d 阶 $\lambda$ 周期阵.

必要性. 今若有一个不可约阵 $A_{t}$ 的 $\lambda_{t} \neq \lambda$ , 并设 $i_{0}$ 为 $\lambda_{t}$ 对应的临界回路上的点, 则

$$\lim _ {n \rightarrow \infty} \left(\boldsymbol {A} _ {\lambda_ {t}} ^ {d n}\right) _ {i _ {0} i _ {0}} = e. \tag {11.4.18}$$

反设存在 $\hat{d},\hat{\lambda}$ 使 $\pmb{A}$ 为 $\hat{d}$ 阶 $\hat{\lambda}$ 周期阵，则由 $\lambda_{t}\neq \lambda ,$ 得 $\hat{\lambda}\neq \lambda$ 或 $\hat{\lambda}\neq \lambda_{t}$ .不妨设 $\hat{\lambda}\neq \lambda_t$ 取定 $n_0$ 后有

$$
\lim _ {n \to \infty} (A _ {\lambda_ {t}} ^ {\hat {d} d (n + n _ {0})}) _ {i _ {0} i _ {0}} = \lim _ {n \to \infty} (\hat {\lambda} / \lambda_ {t}) ^ {\hat {d} d n} (A _ {\lambda_ {t}} ^ {\hat {d} d n _ {0}}) = \left\{ \begin{array}{l l} {+ \infty ,} & {\quad \text {若} \hat {\lambda} > \lambda_ {t},} \\ {- \infty ,} & {\quad \text {若} \hat {\lambda} <   \lambda_ {t}.} \end{array} \right.
$$

这与式 (11.4.18) 矛盾. 所以 $\pmb{A}$ 不是 $\hat{d}$ 阶 $\hat{\lambda}$ 周期阵.

(ii) 由式 (11.4.7), (11.4.16) 知 $Q_{h}$ 存在，且
