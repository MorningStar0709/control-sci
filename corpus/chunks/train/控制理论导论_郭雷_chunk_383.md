# 谱映象定理

设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $A$ 为其生成算子。下面讨论 $A$ 与 $T(t)$ 的谱之间的关系。

引理5.3.5 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $A$ 为其生成算子。对于任意 $\lambda \in \mathbb{C}$ ，定义

$$B _ {\lambda} (t) x = \int_ {0} ^ {t} \mathrm{e} ^ {\lambda (t - s)} T (s) x \mathrm{d} s, \quad x \in X, t \geqslant 0, \tag {5.3.27}$$

则

$$(\lambda I - A) B _ {\lambda} (t) x = \mathrm{e} ^ {\lambda t} x - T (t) x, \quad x \in X, \tag {5.3.28}B _ {\lambda} (t) (\lambda I - A) x = \mathrm{e} ^ {\lambda t} x - T (t) x, \quad x \in \mathcal {D} (A). \tag {5.3.29}$$

证明 对于任意固定的 $\lambda$ 和 $t$ , 由式 (5.3.27) 定义的 $B_{\lambda}(t)$ 是 $X$ 上的有界线性算子. 于是对于任意 $x \in X$ 和 $h > 0$ , 我们有

$$
\begin{array}{l} \frac {T (h) - I}{h} B _ {\lambda} (t) x = \frac {\mathrm{e} ^ {\lambda h}}{h} \int_ {t} ^ {t + h} \mathrm{e} ^ {\lambda (t - s)} T (s) x \mathrm{d} s - \frac {1}{h} \int_ {0} ^ {h} \mathrm{e} ^ {\lambda (t - s)} T (s) x \mathrm{d} s \\ + \frac {\mathrm{e} ^ {\lambda h} - 1}{h} \int_ {h} ^ {t} \mathrm{e} ^ {\lambda (t - s)} T (s) x \mathrm{d} s. \\ \end{array}
$$

当 $h \downarrow 0$ 时，上式右端收敛于 $\lambda B_{\lambda}(t)x + T(t)x - \mathrm{e}^{\lambda t}x$ 。因此我们得到 $B_{\lambda}(t)x \in \mathcal{D}(A)$ ，并且

$$A B _ {\lambda} (t) x = \lambda B _ {\lambda} (t) x + T (t) x - \mathrm{e} ^ {\lambda t} x,$$

即式 (5.3.28) 成立. 从 $B_{\lambda}(t)$ 的定义容易看出 $B_{\lambda}(t)Ax = AB_{\lambda}(t)x, \forall x \in \mathcal{D}(A)$ , 从而式 (5.3.29) 成立. 证毕.

定理5.3.9 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $A$ 为其生成算子，则

$$\sigma (T (t)) \supset \exp (t \sigma (A)), \quad \forall t \geqslant 0. \tag {5.3.30}$$

证明 用反证法，假定存在 $\lambda \in \sigma(A)$ 使得对于某个 $t \geqslant 0$ ，有 $e^{\lambda t} \in \rho(T(t))$ . 记 $Q_{\lambda}(t) = (e^{\lambda t} I - T(t))^{-1}$ ，显然 $B_{\lambda}(t)$ 和 $Q_{\lambda}(t)$ 是可交换的。从式 (5.3.28) 和式 (5.3.29) 我们有

$$(\lambda I - A) B _ {\lambda} (t) Q _ {\lambda} (t) x = x, \quad \forall x \in X.Q _ {\lambda} (t) B _ {\lambda} (t) (\lambda I - A) x = x, \quad \forall x \in \mathcal {D} (A),$$

这表明 $\lambda \in \rho(A)$ , 与假设矛盾. 证毕

定理5.3.10 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群， $A$ 为其生成算子，则

$$\exp (t \sigma_ {p} (A)) \subset \sigma_ {p} (T (t)) \subset \exp (t \sigma_ {p} (A)) \cup \{0 \}. \tag {5.3.31}$$

更确切地说，如果 $\lambda \in \sigma_p(A)$ ，则 $\mathrm{e}^{\lambda t} \in \sigma_p(T(t))$ ；而若 $\mathrm{e}^{\lambda t} \in \sigma_p(T(t))$ ，则存在 $k \in \mathbb{N}$ 使得 $\lambda_k = \lambda + 2\pi ki / t \in \sigma_p(A)$ ，其中 $\mathbb{N}$ 表示正整数集。
