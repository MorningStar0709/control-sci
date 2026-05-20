显然，若方程(9.3.2)是 $L_{p^{-}}$ 指数稳定的，则在关于初值 $x_0$ 和干扰 $\{\xi_t\}$ 的一定条件下，式(9.3.1)的解 $\{x_t\}$ 也在一定意义下是稳定的。反之，下面的定理将说明，若对任何 $L_{2^{-}}$ 有界扰动 $\{\xi_t\}$ ，(9.3.1)的解是 $L_{2}$ 一致有界的，则方程(9.3.2)必是 $L_{2}$ 指数稳定的。

定理9.3.3 考虑方程(9.3.1)，并设 $x_0 = 0, \det(A_t) \neq 0, \forall t \geqslant 0.$ 记

$$\mathcal {B} = \left\{\xi : \sup _ {t} \| \xi_ {t} \| _ {L _ {2}} \leqslant 1 \right\}.$$

若下式成立：

$$\sup _ {\xi \in \mathcal {B}} \sup _ {t} \| x _ {t} \| _ {L _ {2}} < \infty ,$$

则方程 (9.3.2) 必是 $L_{2}$ 指数稳定的.

证明 首先记式 (9.3.2) 的转移矩阵为 $\Phi(n, m)$ , 即,

$$\Phi (n + 1, m) = A _ {n + 1} \Phi (n, m), \quad \Phi (m, m) = I, \quad \forall n \geqslant m,$$

则式 (9.3.1) 的解可表示为

$$x _ {t + 1} = \sum_ {i = 0} ^ {t} \Phi (t, i) \xi_ {i + 1}, \tag {9.3.3}$$

对任何固定的 $k \geqslant 0$ , 令

$$
\xi_ {i + 1} = \left\{ \begin{array}{l l} \Phi (i, k) [ E \Phi^ {\mathrm{T}} (i, k) \Phi (i, k) ] ^ {- \frac {1}{2}} \eta_ {i + 1}, & i \geqslant k, \\ 0, & i <   k, \end{array} \right.
$$

其中 $\{\eta_i\}$ 是与 $\{A_i\}$ 独立的 $d$ 维序列， $E\eta_i = 0, E\eta_i\eta_i^{\mathrm{T}} = d^{-1}I.$ 易见

$$E \| \xi_ {i + 1} \| ^ {2} = \operatorname{tr} [ E (\xi_ {i + 1} \xi_ {i + 1} ^ {\mathrm{T}}) ] = 1, \quad \forall i \geqslant k.$$

故 $\xi \in \mathcal{B}$ . 将 $\xi_{i+1}$ 代入式 (9.3.3) 并计算方差得 $\forall t \geqslant k$

$$E x _ {t + 1} x _ {t + 1} ^ {\mathrm{T}} = \frac {1}{d} E \sum_ {i = k} ^ {t} \Phi (t, k) [ E \Phi^ {\mathrm{T}} (i, k) \Phi (i, k) ] ^ {- 1} \Phi^ {\mathrm{T}} (t, k), k \geqslant 0.$$

于是

$$
\begin{array}{l} \left[ E \Phi^ {\mathrm{T}} (t, k) \Phi (t, k) \right] ^ {\frac {1}{2}} \sum_ {i = k} ^ {t} \left[ E \Phi^ {\mathrm{T}} (i, k) \Phi (i, k) \right] ^ {- 1} \left[ E \Phi^ {\mathrm{T}} (t, k) \Phi (t, k) \right] ^ {\frac {1}{2}} \\ \leqslant \operatorname{tr} E \left\{\sum_ {i = k} ^ {t} \Phi (t, k) [ E \Phi^ {\mathrm{T}} (i, k) \Phi (i, k) ] ^ {- 1} \Phi^ {\mathrm{T}} (t, k) \right\} \cdot I \\ = \mathrm{d} E \| x _ {t + 1} \| ^ {2} \cdot I \leqslant c \cdot I, \quad \forall t \geqslant k \geqslant 0 \\ \end{array}
$$

其中 $c$ 是有限正常数．上式意味着

$$\sum_ {i = k} ^ {t} \left[ E \Phi^ {\mathrm{T}} (i, k) \Phi (i, k) \right] ^ {- 1} \leqslant c \left[ E \Phi^ {\mathrm{T}} (t, k) \Phi (t, k) \right] ^ {- 1}.$$

记

$$a ^ {- 1} (i, k) = \lambda_ {\min} \left\{\left[ E \Phi^ {T} (i, k) \Phi (i, k) \right] ^ {- 1} \right\}, \quad i \geqslant k,$$

则由上式知

$$\sum_ {i = k} ^ {t} a ^ {- 1} (i, k) \leqslant c a ^ {- 1} (t, k), \quad \forall t \geqslant k. \tag {9.3.4}$$

于是
