$$\lambda_ {\max} \{E [ \Phi^ {T} (k + h, k) \Phi (k + h, k) | \mathcal {F} _ {k - 1} ] \} \leqslant 1 - \frac {\lambda_ {m}}{1 + h},$$

其中 $k = mh + 1, m \geqslant 1, \lambda_m$ 由 (9.3.15) 定义，而 $\Phi(\cdot, \cdot)$ 由下面定义：

$$\Phi (n + 1, m) = (I - F _ {n}) \Phi (n, m), \quad \Phi (m, m) = 1, \quad \forall n \geqslant m.$$

证明 记 $Z_{k - 1}$ 是对应于矩阵

$$E [ \Phi^ {T} (k + h, k) \Phi (k + h, k) | \mathcal {F} _ {k - 1} ]$$

之最大特征值 $\rho_{k - 1}$ 的单位特征向量．递推定义序列 $\{Z_j,j\geqslant k\}$ 如下：

$$Z _ {j} = (I - F _ {j}) Z _ {j - 1}, \quad j \geqslant k. \tag {9.3.16}$$

易见 $Z_{k + h - 1} = \Phi (k + h,k)Z_{k - 1}$ ，于是有

$$
\begin{array}{l} E \left[ \| Z _ {k + h - 1} \| ^ {2} \mid \mathcal {F} _ {k - 1} \right] = Z _ {k - 1} ^ {\mathrm{T}} E \left[ \Phi^ {\mathrm{T}} (k + h, k) \Phi (k + h, k) \mid \mathcal {F} _ {k - 1} \right] Z _ {k - 1} \\ = \rho_ {k - 1} \| Z _ {k - 1} \| ^ {2} = \rho_ {k - 1}. \tag {9.3.17} \\ \end{array}
$$

从式 (9.3.16) 得

$$Z _ {j} = Z _ {k - 1} - \sum_ {i = k} ^ {j} F _ {i} Z _ {i - 1}, \forall j \in [ k, k + h - 1 ],$$

于是利用 Schwarz 不等式知对任何 $j \in [k, k + h]$ ,

$$
\begin{array}{l} E \left[ \left\| Z _ {j - 1} - Z _ {k - 1} \right\| ^ {2} \mid \mathcal {F} _ {k - 1} \right] = E \left[ \left\| \sum_ {i = k} ^ {j - 1} F _ {i} Z _ {i - 1} \right\| ^ {2} \mid \mathcal {F} _ {k - 1} \right] \\ \leqslant E \left[ \left(\sum_ {i = k} ^ {j - 1} \| F _ {i} ^ {1 / 2} Z _ {i - 1} \| ^ {2}\right) \left(\sum_ {i = k} ^ {j - 1} \| F _ {i} ^ {1 / 2} \| ^ {2}\right) | \mathcal {F} _ {k - 1} \right] \\ \leqslant h \cdot E \left[ \sum_ {i = k} ^ {j - 1} Z _ {i - 1} ^ {\mathrm{T}} F _ {i} Z _ {i - 1} \mid \mathcal {F} _ {k - 1} \right]. \tag {9.3.18} \\ \end{array}
$$

利用 $\lambda_{m}$ 的定义及Minkowski不等式知

$$
\begin{array}{l} \sqrt {(1 + h) \lambda_ {m}} \leqslant \left\{Z _ {k - 1} ^ {\mathrm{T}} E \left[ \sum_ {i = m h + 1} ^ {(m + 1) h} F _ {i} \mid \mathcal {F} _ {m h} \right] Z _ {k - 1} \right\} ^ {1 / 2} \\ \leqslant \left\{E \left[ \sum_ {i = k} ^ {k + h - 1} \| F _ {i} ^ {1 / 2} Z _ {i - 1} \| ^ {2} \right] | \mathcal {F} _ {k - 1} \right\} ^ {1 / 2} + \left\{E \left[ \sum_ {i = k} ^ {k + h - 1} \| Z _ {i - 1} - Z _ {k - 1} \| ^ {2} | \mathcal {F} _ {k - 1} \right] \right\} ^ {1 / 2}. \\ \end{array}
$$

据此及式 (9.3.18) 得

$$\sqrt {(1 + h) \lambda_ {m}} \leqslant (1 + h) \left\{E \left[ \sum_ {i = k} ^ {k + h - 1} \| F _ {i} ^ {1 / 2} Z _ {i - 1} \| ^ {2} \mid \mathcal {F} _ {k - 1} \right] \right\} ^ {1 / 2},$$

或

$$E \left[ \sum_ {i = k} ^ {k + h - 1} \| F _ {i} ^ {1 / 2} Z _ {i - 1} \| ^ {2} \mid \mathcal {F} _ {k - 1} \right] \geqslant \frac {\lambda_ {m}}{1 + h}, \tag {9.3.19}$$

再次利用式 (9.3.16) 并注意到 $0 \leqslant F_{i} \leqslant I$ 得
