$$Z _ {j} ^ {\mathrm{T}} Z _ {j} \leqslant Z _ {j - 1} ^ {\mathrm{T}} Z _ {j - 1} - Z _ {j - 1} ^ {\mathrm{T}} F _ {j} Z _ {j - 1}$$

于是

$$\left\| Z _ {k + h - 1} \right\| ^ {2} \leqslant \left\| Z _ {k - 1} \right\| ^ {2} - \sum_ {j = k} ^ {k + h - 1} Z _ {j - 1} ^ {\mathrm{T}} F _ {j} Z _ {j - 1} = 1 - \sum_ {j = k} ^ {k + h - 1} \left\| F _ {j} ^ {1 / 2} Z _ {j - 1} \right\| ^ {2},$$

据此并利用式 (9.3.17) 和式 (9.3.19) 可推出

$$
\begin{array}{l} \rho_ {k - 1} = E \left[ \left\| Z _ {k + h - 1} \right\| ^ {2} \mid \mathcal {F} _ {k - 1} \right] \\ \leqslant 1 - E \left[ \sum_ {j = k} ^ {k + h - 1} \| F _ {j} ^ {1 / 2} Z _ {j - 1} \| ^ {2} \mid \mathcal {F} _ {k - 1} \right] \\ \leqslant 1 - \frac {\lambda_ {m}}{1 + h}. \\ \end{array}
$$

故引理得证.

引理9.3.2 在引理9.3.1的条件及记号下，对任何 $k_{0} \geqslant 0$ ，考虑方程

$$x _ {k} = \Phi (k h + 1, (k - 1) h + 1) x _ {k - 1}, \quad k \geqslant k _ {0} + 1, \tag {9.3.20}$$

其中初值 $x_{k_0}$ 是确定性的且 $\| x_{k_0}\| = 1$ ，那么存在 $\alpha_{k}\in [0,1]$ 使 $\alpha_{k}\in \mathcal{F}_{kh}$ ，且

$$\| x _ {k} \| \leqslant (1 - \alpha_ {k}) \| x _ {k - 1} \|, \quad k \geqslant k _ {0} + 1, \tag {9.3.21}$$

及

$$E [ \alpha_ {k + 1} | \mathcal {F} _ {k h} ] \geqslant \frac {\lambda_ {k}}{2 (1 + h)}, \quad k \geqslant k _ {0} + 1. \tag {9.3.22}$$

证明 对任何 $k \geqslant k_0 + 1$ , 定义

$$
\alpha_ {k} = \left\{ \begin{array}{l l} 1 - \frac {\| \Phi (k h + 1 , (k - 1) h + 1) x _ {k - 1} \|}{\| x _ {k - 1} \|}, & \text {若} \| x _ {k - 1} \| \neq 0, \\ 1, & \text {若} \| x _ {k - 1} \| = 0. \end{array} \right.
$$

由于 $\| \Phi (n,m)\| \leqslant 1,\forall n\geqslant m\geqslant 0$ ，易见 $\alpha_{k}\in [0,1],\alpha_{k}\in \mathcal{F}_{kh}$ ，且(9.3.21）成立．因此我们只需证明(9.3.22).

记 $\Omega_{k} = [\omega : \| x_{k}\| = 0]$ , 则 $\Omega_{k} \in \mathcal{F}_{kh}$ , 且

$$I _ {\Omega_ {k}} E [ \alpha_ {k + 1} | \mathcal {F} _ {k h} ] = E [ I _ {\Omega_ {k}} \alpha_ {k + 1} | \mathcal {F} _ {k h} ] = I _ {\Omega_ {k}},$$

从而注意到 $\lambda_{k} < 1$ 知 (9.3.22) 在 $\Omega_{k}$ 上成立。下面考虑 $\Omega_{k}^{c}$ 。利用引理9.3.1知

$$
\begin{array}{l} E [ \| \Phi ((k + 1) h + 1, k h + 1) x _ {k} \| | \mathcal {F} _ {k h} ] \\ \leqslant \left\{E [ \| \Phi ((k + 1) h + 1, k h + 1) x _ {k} \| ^ {2} | \mathcal {F} _ {k h} ] \right\} ^ {1 / 2} \\ \leqslant \left\{x _ {k} ^ {\mathrm{T}} E [ \Phi^ {\mathrm{T}} ((k + 1) h + 1, k h + 1) \cdot \Phi ((k + 1) h + 1, k h + 1) | \mathcal {F} _ {k h} ] x _ {k} \right\} ^ {1 / 2} \\ \leqslant \left\{x _ {k} ^ {\mathrm{T}} \left(1 - \frac {\lambda_ {k}}{1 + h}\right) x _ {k} \right\} ^ {1 / 2} \leqslant \left(1 - \frac {\lambda_ {k}}{2 (1 + h)}\right) \| x _ {k} \|, \\ \end{array}
$$

因此利用 $\alpha_{k + 1}$ 的定义得
