$$
\begin{array}{l} \| x (t - \delta) - x (t) \| \leqslant \int_ {0} ^ {t - \delta} \| T (t - \delta - s) f (s) - T (t - s) f (s) \| d s \\ + \int_ {t - \delta} ^ {t} \| T (t - s) f (s) \| d s, \\ \end{array}
$$

并且同理，当 $\delta \to 0$ 时，上式右端收敛于0.证毕.

定理 5.3.23 设 X 是自反 Banach 空间， $x_{0} \in X$ . 如果 $f \in L^{p}([0, t_{1}]; X)$ , $p \geqslant 1$ , 那么方程 (5.3.53) 的温和解式 (5.3.62) 是方程 (5.3.53) 的唯一弱解.

证明 首先我们证明由式 (5.3.62) 给出的 $x(t)$ 是方程 (5.3.53) 的一个弱解. 事实上, 设 $x^{*} \in \mathcal{D}(A^{*})$ , 则由于 $X$ 自反, $T^{*}(t)$ 是 $X^{*}$ 上由 $A^{*}$ 生成的 $C_{0}$ 半群, 从而

$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} \langle x (t), x ^ {*} \rangle = \frac {\mathrm{d}}{\mathrm{d} t} \left\langle x _ {0}, T ^ {*} (t) x ^ {*} \right\rangle + \frac {\mathrm{d}}{\mathrm{d} t} \int_ {0} ^ {t} \left\langle T (t - s) f (s), x ^ {*} \right\rangle \mathrm{d} s \\ = \langle x _ {0}, T ^ {*} (t) A ^ {*} x ^ {*} \rangle + \frac {\mathrm{d}}{\mathrm{d} t} \int_ {0} ^ {t} \langle f (s), T ^ {*} (t - s) x ^ {*} \rangle \mathrm{d} s \\ = \langle T (t) x _ {0}, A ^ {*} x ^ {*} \rangle + \langle f (t), x ^ {*} \rangle \\ + \left\langle \int_ {0} ^ {t} T (t - s) f (s) \mathrm{d} s, A ^ {*} x ^ {*} \right\rangle \\ = \langle x (t), A ^ {*} x ^ {*} \rangle + \langle f (t), x ^ {*} \rangle , \quad \text { a.e. } \quad t \in (0, t _ {1}). \tag {5.3.63} \\ \end{array}
$$

对式 (5.3.63) 两端积分便得到式 (5.3.61), 即 $x(t)$ 是方程 (5.3.53) 的弱解.

为证方程 (5.3.53) 弱解的唯一性，我们只需证明 $x(\cdot) \in C([0, t_1]; X)$ 满足

$$\langle x (t), x ^ {*} \rangle = \int_ {0} ^ {t} \langle x (s), A ^ {*} x ^ {*} \rangle \mathrm{d} s, \quad \forall x ^ {*} \in \mathcal {D} (A ^ {*}),$$

从而 $x(t) = 0, 0 \leqslant t \leqslant t_1$ . 为此，对于任意 $t \in (0, t_1)$ ，令

$$u (s) = T (t - s) x (s), \quad 0 \leqslant s \leqslant t,$$

并设 $x^{*} \in \mathcal{D}(A^{*})$ . 于是根据 $x(\cdot)$ 的强连续性，我们得到

$$
\begin{array}{l} \lim _ {h \rightarrow 0} \left\langle \frac {x (h + s) - x (s)}{h}, T ^ {*} (t - s) x ^ {*} \right\rangle \\ = \lim _ {h \rightarrow 0} \frac {1}{h} \left\langle \int_ {s} ^ {s + h} x (\tau) d \tau , A ^ {*} T ^ {*} (t - s) x ^ {*} \right\rangle \\ = \langle x (s), T ^ {*} (t - s) A ^ {*} x ^ {*} \rangle . \\ \end{array}
$$

于是对于 $s \in (0, t)$
