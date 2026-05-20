下面我们假定 $T(t)$ 一致有界，并且 $A$ 是 $T(t)$ 的生成算子。令

$$X _ {0} = \{x \in X \mid \lim _ {t \rightarrow \infty} T (t) x = 0 \}.$$

显然 $X_0$ 是 $X$ 的闭子空间。于是 $X_0 = X$ 等价于 $T(t)$ 的强稳定性。

我们定义商空间 $X_{1} = X / X_{0}$ ，在范数 $\| [x]\| _1 = \inf \left\{\| y\| \mid y\in [x]\right\} ([x]\in X_1)$ 下 $X_{1}$ 也是一个Banach空间．由于 $X_0$ 对于 $T(t)$ 是不变的，即 $T(t)X_0\subset X_0,\forall t\geqslant 0,$ 易见 $X_0$ 对于 $A$ 也是不变的．于是 $A$ 诱导 $X_{1}$ 上一算子[A]

$$[ A ] [ x ] = [ A x ], \quad \forall x \in \mathcal {D} (A),\mathcal {D} ([ A ]) = [ \mathcal {D} (A) ] = \left\{\left[ x \right] \in X _ {1} \mid x \in \mathcal {D} (A) \right\},$$

并且 $T(t)$ 诱导 $X_{1}$ 上一 $C_0$ 半群 $T_{1}(t)$

$$T _ {1} (t) [ x ] = [ T (t) x ], \quad \forall [ x ] \in X _ {1}, x \in [ x ].$$

设 $\| T(t)\| \leqslant M,\forall t\geqslant 0.$ 对于任意 $[x]\in X_1$ ，我们有

$$\| T _ {1} (t) [ x ] \| _ {1} = \inf \left\{\| T (t) x + y \| \mid y \in X _ {0} \right\} \leqslant \| T (t) x \| \leqslant M \| x \|, \quad \forall x \in [ x ], \forall t \geqslant 0.$$

于是 $\| T_1(t)[x] \|_1 \leqslant M \| [x] \|_1$ ，这表明 $T_1(t)$ 在 $X_1$ 上也是一致有界的。

引理 10.1.4 设 $T(t)$ 是 Banach 空间 X 上闭稠定线性算子 A 生成的一致有界 $C_{0}$ 半群。设 $X_{0}, X_{1}$ 和 $T_{1}(t)$ 如上。用 $A_{1}$ 表示 $T_{1}(t)$ 的生成算子。那么 (1) $A_{1} = [A]$ ; (2) $\sigma(A_{1}) \subset \sigma(A)$ .

证明 (1) 对于任意的 $x \in \mathcal{D}(A)$ , 根据定义, $Ax = \lim_{t \to 0^{+}} t^{-1}(T(t)x - x)$ , 故

$$[ A x ] = \lim _ {t \rightarrow 0 ^ {+}} t ^ {- 1} ([ T (t) x ] - [ x ]) = A _ {1} [ x ].$$

因此 $[A] \subset A_1$ .

另一方面，设 $\operatorname{Re} \lambda > \max\{\omega(A_1), \omega(A)\}$ ，则对任意的 $[y] \in X_1$ ，我们有

$$R (\lambda ; A _ {1}) [ y ] = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} [ T (t) ] [ y ] \mathrm{d} t = [ R (\lambda ; A) y ], \quad \forall y \in X.$$

因此

$$\mathcal {D} (A _ {1}) = \left\{R (\lambda ; A _ {1}) [ y ] \mid y \in X \right\} = \left\{\left[ R (\lambda ; A) y \right] \mid y \in X \right\} = \mathcal {D} ([ A ]),$$

从而 $A_{1} = [A]$

(2) 设 $\lambda \in \rho(A)$ , 则 $\mathcal{R}(\lambda I - A) = X$ , 从而 $\mathcal{R}(\lambda I - A_1) = X_1$ . 由于 $T(t)$ 与 $R(\lambda; A)$ 可交换, 故 $X_0$ 对于 $R(\lambda; A)$ 是不变的. 由此可见 $\lambda I - A_1$ 是可逆的. 于是依据闭图像定理, $\lambda \in \rho(A_1)$ , 这证明了 $\rho(A) \subset \rho(A_1)$ , 即 $\sigma(A_1) \subset \sigma(A)$ . 证毕.

由于 $T(t)$ 一致有界，不失一般性，我们可以假定 $T(t)$ 是压缩的（如不然， $X$ 可重新赋范使得在新范数下 $T(t)$ 是压缩的）。于是对于 $x \in X, \| T(t)x\|_1$ 是 $t \geqslant 0$ 的非增函数。因此我们可以定义

$$\| [ x ] \| _ {2} = \lim _ {t \rightarrow \infty} \| T (t) x \| > 0, \quad \forall [ x ] \in X _ {1},$$
