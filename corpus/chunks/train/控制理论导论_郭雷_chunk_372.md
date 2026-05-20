$$
M = \left\{ \begin{array}{l l} {\sup \big \{\| T (t) \| \big | 0 \leqslant t \leqslant 1 \big \},} & {\quad \text {若} \omega > 0,} \\ {\mathrm{e} ^ {- \omega} \sup \big \{\| T (t) \| \big | 0 \leqslant t \leqslant 1 \big \},} & {\quad \text {若} \omega \leqslant 0,} \end{array} \right.
$$

则可直接得到结论 (c).

显然 $M < 1$ 是不可能的，因为 $T(0) = I$ .

定义5.3.2 设 $T(t)$ 是Banach空间 $X$ 上的 $C_0$ 半群. $T(t)$ 的(无穷小)生成算子 $A$ 定义为

$$A x = \lim _ {t \downarrow 0} \frac {T (t) x - x}{t}, \quad \forall x \in \mathcal {D} (A),\mathcal {D} (A) = \left\{x \in X \middle | \lim _ {t \downarrow 0} {\frac {T (t) x - x}{t}} \text {存在} \right\}.$$

定理5.3.2 设 $A$ 是Banach空间 $X$ 上的 $C_0$ 半群. 那么

(a) $\forall x \in \mathcal{D}(A), T(t)x \in \mathcal{D}(A), t \geqslant 0$ ;   
(b) $\frac{\mathrm{d}}{\mathrm{d}t}(T(t)x) = AT(t)x = T(t)Ax, \forall x \in \mathcal{D}(A), t \geqslant 0;$   
(c) $\frac{\mathrm{d}^n}{\mathrm{d}t^n}(T(t)x) = A^n T(t)x = T(t)A^n x,\quad \forall x\in \mathcal{D}(A^n),t > 0;$

(d) $T(t)x - x = \int_0^t AT(s)x\mathrm{d}s,\quad \forall x\in \mathcal{D}(A),t\geqslant 0;$

(e) $A$ 是闭稠定的.

证明 (a) 是显然的;

(b), 对于每一 $x \in \mathcal{D}(A)$ 和 $t > 0$ , 我们有

$$\frac {\mathrm{d} ^ {+}}{\mathrm{d} t} T (t) x = \lim _ {\delta \downarrow 0} \frac {T (t + \delta) x - T (t) x}{\delta} = T (t) A x = A T (t) x.$$

此外，对于 $t > 0$ ，我们有

$$
\begin{array}{l} \frac {\mathrm{d} ^ {-}}{\mathrm{d} t} T (t) x = \lim _ {\delta \downarrow 0} \frac {T (t) x - I ^ {\prime} (t - \delta) x}{\delta} \\ = \lim _ {\delta \downarrow 0} \left[ T (t - \delta) A x - T (t - \delta) \left(A x - \frac {T (\delta) x - x}{\delta}\right) \right] \\ = T (t) A x, \\ \end{array}
$$

这是因为 $\| T(t - \delta)\|$ 关于 $\delta \in [0,\delta_0]$ 是有界的．因此 (b) 成立；

(c) 是 (b) 的直接结果. 考虑到 $T(t)x$ 作为 $t$ 的函数的强连续性, (d) 可以直接从 (b) 推出;

(e). 首先任取 $x \in X$ 和 $t > 0$ , 并记 $y = \int_{0}^{t} T(s)x \mathrm{d}s$ , 则当 $\delta \to 0^{+}$ 时,

$$
\begin{array}{l} \frac {T (\delta) y - y}{\delta} = \frac {1}{\delta} \int_ {0} ^ {t} T (s + \delta) x \mathrm{d} s - \frac {1}{\delta} \int_ {0} ^ {t} T (s) x \mathrm{d} s \\ = \frac {1}{\delta} \int_ {t} ^ {t + \delta} T (s) x \mathrm{d} s - \frac {1}{\delta} \int_ {0} ^ {\delta} T (s) x \mathrm{d} s \rightarrow T (t) x - x, \\ \end{array}
$$

这表明 $y = \int_0^t T(s)x\mathrm{d}s\in \mathcal{D}(A),\forall t\geqslant 0.$ 但是

$$\lim _ {t \downarrow 0} \frac {1}{t} \int_ {0} ^ {t} T (s) x \mathrm{d} s = x,$$

因此 $\mathcal{D}(A)$ 在 $X$ 中稠. 下证 $A$ 的闭性. 设 $x_{n} \in \mathcal{D}(A)$ 使得 $x_{n} \to x, Ax_{n} \to z (n \to \infty)$ . 根据 (d)
