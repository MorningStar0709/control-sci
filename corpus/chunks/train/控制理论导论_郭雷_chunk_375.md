定理 5.3.4 设 A 是 Banach 空间 X 上 $C_{0}$ 半群 $T(t)$ 的生成算子. 那么 $\bigcap_{n=1}^{\infty} \mathcal{D}(A^{n})$ 在 X 中是稠密的.

证明 设 $C_0^\infty (0,\infty)$ 表示 $(0,\infty)$ 上有紧支集的无限次可微函数全体. 对于 $x\in X$ 和 $\varphi \in C_0^\infty (0,\infty)$ , 令

$$y = x (\varphi) = \int_ {0} ^ {\infty} \varphi (s) T (s) x \mathrm{d} s.$$

如果 $h > 0$ ，则

$$\frac {T (h) y - y}{h} = \int_ {0} ^ {\infty} \frac {1}{h} [ \varphi (s - h) - \varphi (s) ] T (s) x d s. \tag {5.3.10}$$

由于式 (5.3.10) 右端的被积函数当 $h \downarrow 0$ 时一致收敛于 $-\varphi'(s)T(s)x$ , 我们有 $y \in \mathcal{D}(A)$ , 并且

$$A y = \lim _ {h \downarrow 0} \frac {T (h) y - y}{h} = - \int_ {0} ^ {\infty} \varphi^ {\prime} (s) T (s) x d s.$$

显然当 $\varphi \in C_0^\infty (0,\infty)$ 时， $\varphi^{(n)}\in C_0^\infty (0,\infty),n = 1,2,\dots$ 然后重复上述推理，可得 $y\in \mathcal{D}(A^n)$ ，并且

$$A ^ {n} y = (- 1) ^ {n} \int_ {0} ^ {\infty} \varphi^ {(n)} (s) T (s) x \mathrm{d} s, \quad \forall n \geqslant 1.$$

这表明 $y \in \bigcap_{n=1}^{\infty} \mathcal{D}(A^n)$ . 现在我们设

$$Z = \left\{x (\varphi) \mid x \in X, \varphi \in C _ {0} ^ {\infty} (0, \infty) \right\}.$$

显然 $Z$ 是 $X$ 的一子空间. 我们已经证明了 $Z \subset \bigcap_{n=1}^{\infty} \mathcal{D}(A^n)$ . 为证定理, 还要证明 $Z$ 在 $X$ 中是稠密的. 用反证法, 假定 $Z$ 在 $X$ 中不稠. 于是根据 Hahn-Banach 定理,存在泛函 $x^{*} \in X^{*}, x^{*} \neq 0$ 使得 $x^{*}(y) = 0, \forall y \in Z$ . 因此对于 $x \in X, \varphi \in C_{0}^{\infty}(0, \infty)$ , 有

$$\int_ {0} ^ {\infty} \varphi (s) x ^ {*} (T (s) x) \mathrm{d} s = x ^ {*} \left(\int_ {0} ^ {\infty} \varphi (s) (T (s) x) \mathrm{d} s\right) = 0.$$

于是得出结论， $x^{*}(T(s)x)$ 作为 $s$ 的连续函数，必定在 $(0,\infty)$ 上恒等于零，因为否则的话，我们可以找到一函数 $\varphi \in C_0^\infty (0,\infty)$ 使得 $\int_0^\infty \varphi (s)x^* (T(s)x)\mathrm{d}s\neq 0.$ 特别取 $s = 0$ ，我们得到 $x^{*} = 0,$ 与假设矛盾．证毕.

上面我们证明了 Banach 空间 $X$ 上一 $C_0$ 半群 $T(t)$ 的生成算子 $A$ 必定是闭稠定的，当 $T(t)$ 满足 $\| T(t) \| \leqslant M e^{\omega t}$ 时， $\{\lambda \in \mathbb{C} \mid \operatorname{Re} \lambda > \omega\} \subset \rho(A)$ ，并且豫解式 $R(\lambda; A)$ 满足式 (5.3.8). 下面的 Hille-Yosida 定理则说，为了 $X$ 中的一线性算子 $A$ 是 $X$ 上一 $C_0$ 半群的生成算子，上述条件不仅必要，而且也是充分的.

定理 5.3.5 (Hille-Yosida) 设 A 是 Banach 空间 X 中一闭稠定线性算子，并假定存在常数 $M \geqslant 1$ 和 $\omega \in R$ ，使得

(1) $\{\lambda \in \mathbb{C} \mid \operatorname{Re} \lambda > \omega\} \subset \rho(A)$ ;   
(2) $\| (\lambda I - A)^{-n}\| \leqslant M(\operatorname {Re}\lambda -\omega)^{-n},\quad \forall \operatorname {Re}\lambda >\omega ,\forall n\geqslant 1,$

则在 $X$ 上存在以 $A$ 为生成算子的唯一 $C_0$ 半群 $T(t)$ , 并满足
