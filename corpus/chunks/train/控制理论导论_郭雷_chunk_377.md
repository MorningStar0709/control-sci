定理5.3.5的证明 (1)首先设 $\omega = 0$ ，假定 $x\in \mathcal{D}(A)$ ，则

$$\left\| T _ {\lambda} (t) x - T _ {\mu} (t) x \right\| \leqslant t M ^ {2} \left\| A _ {\lambda} x - A x \right\| + t M ^ {2} \left\| A _ {\mu} x - A x \right\|.$$

于是当 $\lambda \to \infty$ 时 $T_{\lambda}(t)x$ 收敛. 记 $T(t)x \stackrel{\mathrm{def}}{=} \lim_{\lambda \to \infty} T_{\lambda}(t)x$ . 容易看出, 上述收敛在 $t$ 的每一有界区间上是一致的. 由于 $\overline{\mathcal{D}(A)} = X$ 和 $\|T_{\lambda}(t)\| \leqslant M$ , 我们有

$$\lim _ {\lambda \rightarrow \infty} T _ {\lambda} (t) x - T ^ {\prime} (t) x, \quad \forall x \in X.$$

同样上述收敛在 $t$ 的每一有界区间上是一致的. 不难验证 $T(t)$ 是有界的: $\| T(t) \| \leqslant M, \forall t \geqslant 0$ , 并且 $T(0) = I$ , $T(t + s) = T(t)T(s)$ , $\forall t, s \geqslant 0$ . 此外, $T(t)x$ 仍然是 $t$ 的连续函数, 因为它是连续函数 $T_{\lambda}(t)x$ 的一致极限. 因此, $T(t)$ 是 $X$ 上的 $C_0$ 半群. 今证 $A$ 是 $T(t)$ 的生成算子. 事实上, 设 $B$ 是 $T(t)$ 的生成算子. 依据定理5.3.2

$$
\begin{array}{l} T (t) x - x = \lim _ {\lambda \rightarrow \infty} \left(T _ {\lambda} (t) x - x\right) \\ = \lim _ {\lambda \rightarrow \infty} \int_ {0} ^ {t} T _ {\lambda} (s) A _ {\lambda} x \mathrm{d} s = \int_ {0} ^ {t} T (s) A x \mathrm{d} s, \tag {5.3.16} \\ \end{array}
$$

这里我们已经利用了如下结论：当 $\lambda \to \infty$ 时， $T_{\lambda}(t)A_{\lambda}x$ 在 $t$ 的任意有界区间上一致收敛于 $T(t)Ax$ 。从式 (5.3.16) 可知 $A \subset B$ 。根据假设， $1 \in \rho(A)$ ，另一方面，依据定理5.3.3, $1 \in \rho(B)$ . 因此 $(I - B)\mathcal{D}(A) = (I - A)\mathcal{D}(A) = X$ ，从而 $\mathcal{D}(B) = (I - B)^{-1}X = \mathcal{D}(A)$ . 由此即得 $A = B$ .

(2) 现在我们考虑情形 $\omega \neq 0$ . 设 $A_{1} = A - \omega I$ . 显然 $A_{1}$ 对应于情形 $\omega = 0$ . 设 $A_{1}$ 生成一致有界 $C_{0}$ 半群 $S(t)$ , 并记 $T(t) = \mathrm{e}^{\omega t} S(t)$ , 则 $T(t)$ 由 $A$ 生成, 这是因为

$$\lim _ {t \downarrow 0} \frac {\mathrm{e} ^ {w t} S (t) x - x}{t} = \omega x + A _ {1} x = A x, \quad \forall x \in \mathcal {D} (A).$$

此外，

$$\| T (t) \| = \mathrm{e} ^ {\omega t} \| S (t) \| \leqslant M \mathrm{e} ^ {\omega t}, \quad \forall t \geqslant 0.$$

(3) 最后我们证明唯一性. 设 $S(t)$ 是由 $A$ 生成的另一个 $C_0$ 半群. 那么 $\forall x \in \mathcal{D}(A), t > 0$ , 我们有

$$\frac {\mathrm{d}}{\mathrm{d} s} \left[ T (t - s) S (s) x \right] = T (t - s) A S (s) x - A T (t - s) S (s) x = 0, \qquad 0 < s < t,$$

这意味着 $T(t - s)S(s)x$ 与 $s\in (0,t)$ 无关．于是

$$T (t) x = \lim _ {s \downarrow 0} T (t - s) S (s) x = \lim _ {s \uparrow t} T (t - s) S (s) x = S (t) x.$$

但是 $\overline{\mathcal{D}(A)} = X$ ，从而 $T(t) = S(t),\forall t\geqslant 0.$ 证毕.

从定理5.3.5的证明我们看到，条件(1)和(2)可以代之以
