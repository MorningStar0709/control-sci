$$T (t) x = \left(\mathrm{e} ^ {- t} \xi_ {1}, \mathrm{e} ^ {- t / 2} \xi_ {2}, \dots , \mathrm{e} ^ {- t / n} \xi_ {n}, \dots\right), \quad t \geqslant 0, x = \left(\xi_ {1}, \xi_ {2}, \dots\right) \in l ^ {2}.$$

容易验证 $T(t)$ 是 $\ell^2$ 上一 $C_0$ 半群，并且 $\| T'(t) \| = 1, \forall t \geqslant 0$ . 通过计算，我们得到

$$\lim _ {t \rightarrow \infty} T (t) x = 0, \quad \forall x \in l ^ {2}.$$

因此 $T(t)$ 强稳定但不指数稳定.

例10.1.2 在 $L^2 (0,2\pi)$ 中定义

$$T (t) f = \mathrm{e} ^ {\mathrm{i} x t} f (x), \quad f \in L ^ {2} (0, 2 \pi), t \geqslant 0.$$

显然 $T(t)$ 是 $L^2 (0,2\pi)$ 上一 $C_0$ 半群. 根据Riemann-Lebesgue引理，对于任意 $f,g\in L^{2}(0,2\pi)$ ，

$$\lim _ {t \rightarrow \infty} (T (t) f, g) = \lim _ {t \rightarrow \infty} \int_ {0} ^ {2 \pi} \mathrm{e} ^ {\mathrm{i} x t} f (x) \overline {{{g (x)}}} \mathrm{d} x = 0,$$

即 $T(t)$ 是弱稳定的．但 $\| T(t)f\| = \| f\|, \forall t \geqslant 0$ ，从而 $T(t)$ 并不是强稳定的.

例10.1.3 设 $\{\lambda_n\} \subset \mathbb{R}$ 为一实数列．在 $\ell^2$ 中定义

$$T (t) x = \sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {i \lambda_ {n} t} \xi_ {n} e _ {n}, \quad \forall x = (\xi_ {n}) \in \ell^ {2}, t \geqslant 0,$$

其中 $e_n = (\delta_{n1}, \delta_{n2}, \cdots), \delta_{nk}$ 为常用的 Kronecker delta 符号。显然 $T(t)$ 是 $\ell^2$ 上一 $C_0$ 半群，并且 $\|T(t)x\| = \|x\|$ , $\forall x \in \ell^2$ 。因此 $\|T(t)\| = 1, \forall t \geqslant 0$ 。然而 $(T(t)e_n, e_n) = e^{i\lambda_n t}$ ，这意味着 $T(t)$ 不可能是弱稳定的。

定理10.1.2 设 $T(t)$ 是Banach空间 $X$ 上 $C_0$ 半群，并设 $A$ 为其生成算子.如果下列两条件之一成立：

(1) A 有紧豫解式 $R(\lambda; A)$ ;

(2) $X$ 是 Hilbert 空间，并且 $T(t)$ 是自伴半群，即 $T(t) = T(t)^*$ ， $\forall t \geqslant 0$ ，那么 $T(t)$ 的强稳定性和弱稳定性是等价的。

证明 我们只需证明弱稳定性蕴含强稳定性。首先假定 Hilbert 空间 X 上的自伴半群 $T(t)$ 是弱稳定的。于是依据 $T(t)$ 的弱稳定性，对于任意 $x \in X$ ，

$$\lim _ {t \rightarrow \infty} \| T (t) x \| ^ {2} = \lim _ {t \rightarrow \infty} (T (t) x, T (t) x) = \lim _ {t \rightarrow \infty} (T (2 t) x, x) = 0.$$

这正是说 $T(t)$ 是强稳定的。现在假定 $A$ 有紧豫解式，并且 $T(t)$ 是弱稳定的。任取一 $\lambda \in \rho(A)$ ，对于任意的 $x \in \mathcal{D}(A)$ ，存在 $y \in X$ 使得 $x = R(\lambda; A)y$ ，从而

$$T (t) x = T (t) R (\lambda ; A) y = R (\lambda ; A) T (t) y.$$

根据 $T(t)$ 的弱稳定性，有 $w - \lim_{t\to \infty}T(t)y = 0$ 。但依据假设豫解式 $R(\lambda ;A)$ 是紧的，从而由上式可知，对任意 $x\in \mathcal{D}(A)$ ，有

$$\lim _ {t \rightarrow \infty} T (t) x = 0.$$

另一方面，由 $T(t)$ 的弱稳定性可知 $T(t)$ 是一致有界的。于是根据线性算子的一致有界性原理，上述收敛可以推广到所有 $x \in X$ 。这正是说 $T(t)$ 是强稳定的。证毕。

设 $A$ 是Banach空间 $X$ 上一 $C_0$ 半群 $T(t)$ 的生成算子，并记
