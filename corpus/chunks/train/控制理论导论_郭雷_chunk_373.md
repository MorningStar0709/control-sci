$$T (t) x _ {n} - x _ {n} = \int_ {0} ^ {t} T (s) A x _ {n} d s.$$

让 $n \to \infty$ 过渡到极限，我们得到

$$T (t) x - x = \int_ {0} ^ {t} T (s) z \mathrm{d} s.$$

因此 $x \in \mathcal{D}(A)$ 并且 $Ax = z$ . 证毕.

定理5.3.3 设Banach空间 $X$ 上的 $C_0$ 半群 $T(t)$ 满足

$$\| T (t) \| \leqslant M \mathrm{e} ^ {\omega t}, \quad \forall t \geqslant 0,$$

并设 $A$ 为 $T(t)$ 的生成算子. 那么

$$\{\lambda \in \mathbb {C} \mid \operatorname{Re} \lambda > \omega \} \subset \rho (A), \tag {5.3.6}$$

并且当 $\operatorname{Re} \lambda > \omega$ 时，

$$R (\lambda ; A) x = (\lambda I - A) ^ {- 1} x = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) x \mathrm{d} t, \quad \forall x \in X, \tag {5.3.7}\| R (\lambda ; A) ^ {n} \| \leqslant \frac {M}{(\operatorname{Re} \lambda - \omega) ^ {n}}, \quad \forall n \geqslant 1. \tag {5.3.8}$$

证明 (1) 首先我们证明当 $\operatorname{Re} \lambda > \omega$ 时 $\overline{R(\lambda I - A)} = X$ . 为此只需证明对于任意给定的 $f \in X^{*}$

$$f ((\lambda I - A) x) = 0, \quad \forall x \in \mathcal {D} (A) \Longrightarrow f = 0.$$

事实上，对于 $f \in X^{*}, x \in \mathcal{D}(A), f((\lambda I - A)x) = 0$ 等价于 $f(Ax) = \lambda f(x), \forall x \in \mathcal{D}(A)$ . 另一方面，根据定理5.3.2

$$\frac {\mathrm{d}}{\mathrm{d} t} f (T (t) x) = f (A T (t) x) = \lambda f (T (t) x), \quad \forall x \in \mathcal {D} (A).$$

上述微分方程的解是 $f(T(t)x) = f(x)\mathrm{e}^{\lambda t}$ . 因此，依据定理的假设

$$| f (x) | = \left| \mathrm{e} ^ {- \lambda t} f (T (t) x) \right| \leqslant M \| f \| \| x \| \mathrm{e} ^ {(\omega - \operatorname{Re} \lambda) t}, \quad \forall x \in \mathcal {D} (A).$$

让 $t \to \infty$ 过渡到极限，我们得到 $f(x) = 0, \forall x \in \mathcal{D}(A)$ . 由于 $\overline{\mathcal{D}(A)} = X$ , 我们有 $f = 0$ .

(2) 然后我们证明，对于 $\operatorname{Re} \lambda > \omega$

$$\| (\lambda I - A) x \| \geqslant M ^ {- 1} (\operatorname{Re} \lambda - \omega) \| x \|, \quad \forall x \in \mathcal {D} (A). \tag {5.3.9}$$

事实上, 对于每一 $x \in \mathcal{D}(A)$ , 依据 Hahn-Banach 定理, 存在 $f \in X^{*}$ 使得 $f(x) = \| x\|$ , $\| f \| = 1$ . 注意到

$$\frac {\mathrm{d}}{\mathrm{d} t} f (T (t) x) = f (T (t) (A - \lambda I) x) + \lambda f (T (t) x),$$

我们有

$$f (T (t) x) = \mathrm{e} ^ {\lambda t} f (x) + \int_ {0} ^ {t} \mathrm{e} ^ {\lambda (t - s)} f (T (s) (A - \lambda I) x) \mathrm{d} s.$$

因此

$$\| x \| = | f (x) | \leqslant M \mathrm{e} ^ {(\omega - \operatorname{Re} \lambda) t} \| x \| + M (\operatorname{Re} \lambda - \omega) ^ {- 1} \| (\lambda I - A) x \|.$$

让 $t \to \infty$ 过渡到极限便得到式 (5.3.9).

由于 $A$ 是闭的，从(1)和(2)可知 $R(\lambda I - A) = X$ ，从而 $\lambda I - A$ 有有界逆，即 $\lambda \in \rho (A)$
