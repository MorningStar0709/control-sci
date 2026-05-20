$$\| T (t) \| \leqslant M \mathrm{e} ^ {\omega t}, \quad \forall t \geqslant 0.$$

这时我们就说 $A$ 生成 $C_0$ 半群 $T(t)$ , 或 $T(t)$ 由 $A$ 生成.

为证该定理，我们需要几个引理.

引理5.3.1 设 $A$ 满足定理5.3.5的条件，并且 $\omega = 0$ ，那么

$$\lim _ {\lambda \rightarrow \infty} \lambda R (\lambda ; A) x = x, \quad \forall x \in X. \tag {5.3.11}$$

证明 设 $x \in \mathcal{D}(A)$ 和 $\lambda > 0$ , 则当 $\lambda \to \infty$ 时, 我们有

$$\| \lambda R (\lambda ; A) x - x \| = \| R (\lambda ; A) A x \| \leqslant \frac {M}{\lambda} \| A x \| \rightarrow 0.$$

但是 $\overline{\mathcal{D}(A)} = X$ ，并且 $\| \lambda R(\lambda; A) \| \leqslant M, \forall \lambda > 0$ ，故依据一致有界性定理，式 (5.3.11) 成立。

对于 $\lambda > 0$ , 定义 $A$ 的 Yosida 近似 $A_{\lambda}$ 如下:

$$A _ {\lambda} = \lambda A R (\lambda ; A) (= \lambda^ {2} R (\lambda ; A) - \lambda I). \tag {5.3.12}$$

引理5.3.2 设 $A$ 满足定理5.3.5的条件，并且 $\omega = 0$ ，则

$$\lim _ {\lambda \rightarrow \infty} A _ {\lambda} x = A x, \quad \forall x \in \mathcal {D} (A). \tag {5.3.13}$$

证明 这是Yosida近似 $A_{\lambda}$ 定义和引理5.3.1的直接结果.

引理5.3.3 设 $\lambda, \mu > 0$ ，则在定理5.3.5的条件下，对于任意 $\lambda > 0, T_{\lambda}(t) = e^{tA_{\lambda}}$ 是 $X$ 上的一致有界 $C_0$ 半群，并且满足

$$
\left\{ \begin{array}{l l} \| T _ {\lambda} (t) \| \leqslant M, & \forall t \geqslant 0, \lambda > 0, \\ \| T _ {\lambda} (t) x - T _ {\mu} (t) x \| \leqslant t M ^ {2} \| A _ {\lambda} x - A _ {\mu} x \|, & x \in X. \end{array} \right. \tag {5.3.14}
$$

证明 由于 $A_{\lambda} \in \mathcal{L}(X)$ , 故 $A_{\lambda}$ 是一致有界半群 $T_{\lambda}(t) = \mathrm{e}^{tA_{\lambda}}$ 的生成算子. 而由于 $\| \lambda^n R(\lambda; A)^n \| \leqslant M, \forall \lambda > 0, n \geqslant 1$ , 我们有 $\left\| \mathrm{e}^{t\lambda^2 R(\lambda; A)} \right\| \leqslant M \mathrm{e}^{\lambda t}, \forall t \geqslant 0$ . 因此

$$\left\| T _ {\lambda} (t) \right\| = \mathrm{e} ^ {- \lambda t} \left\| \mathrm{e} ^ {t \lambda^ {2} R (\lambda ; A)} \right\| \leqslant M, \quad \forall t \geqslant 0. \tag {5.3.15}$$

此外， $T_{\lambda}(t), T_{\mu}(t), A_{\lambda}$ 和 $A_{\mu}$ 是可交换的，故 $\forall x \in X, \lambda, \mu > 0, t \geqslant 0,$ 我们有

$$
\begin{array}{l} \left\| T _ {\lambda} (t) x - T _ {\mu} (t) x \right\| = \left\| \int_ {0} ^ {1} \frac {\mathrm{d}}{\mathrm{d} s} \left(T _ {\lambda} (t s) T _ {\mu} (t (1 - s)) x\right) \mathrm{d} s \right\| \\ \leqslant \int_ {0} ^ {1} t \| T _ {\lambda} (t s) T _ {\mu} (t (1 - s)) \left(A _ {\mu} x - A _ {\lambda} x\right) \| d s \\ \leqslant t M ^ {2} \left\| A _ {\lambda} x - A _ {\mu} x \right\|. \\ \end{array}
$$

证毕.
