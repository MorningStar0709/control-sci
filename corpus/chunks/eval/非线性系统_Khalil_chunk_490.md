# C. 1 证明定理 3.1 和定理 3.2

证明定理 3.1 首先注意到, 如果 $x(t)$ 是

$$\dot {x} = f (t, x), \quad x \left(t _ {0}\right) = x _ {0} \tag {C.1}$$

的解,那么通过积分,有 $x(t)=x_{0}+\int_{t_{0}}^{t}f(s,x(s))ds$ (C.2)

反之,如果 $x(t)$ 满足方程(C.2),那么 $x(t)$ 就满足方程(C.1)。这样,研究微分方程(C.1)解的存在性和唯一性就等同于研究积分方程(C.2)解的存在性与唯一性。继续讨论方程(C.2),把(C.2)的右边看成连续函数的映射 $x:[t_{0},t_{1}]\rightarrow R^{n}$ ,记为 $(Px)(t)$ ,则方程(C.2)可改写为

$$x (t) = (P x) (t) \tag {C.3}$$

注意到 $(Px)(t)$ 是 $t$ 的连续函数。方程(C.3)的一个解为映射 $P$ 的一个不动点，这里 $P$ 为 $x$ 到 $Px$ 的映射。方程(C.3)不动点的存在性可由压缩映射定理证明，这要求定义一个Banach空间 $\mathcal{X}$ 以及一个闭集 $S\subset \mathcal{X}$ ，使得 $P$ 把 $S$ 映射到 $S$ ，且是 $S$ 上的压缩映射。设

$$\mathcal {X} = C [ t _ {0}, t _ {0} + \delta ], \quad \text {具有范数} \quad \| x \| _ {C} = \max _ {t \in [ t _ {0}, t _ {0} + \delta ]} \| x (t) \|$$

和 $S = \{x\in \mathcal{X}\mid \| x - x_0\| _C\leqslant r\}$

其中 $r$ 是球 $B$ 的半径， $\delta$ 是选定的正常数。限制 $\delta$ 的选择范围满足 $\delta \leqslant t_1 - t_0$ ，以使 $[t_0, t_0 + \delta] \subset [t_0, t_1]$ 。注意 $\| x(t) \|$ 表示 $R^n$ 上的范数，而 $\| x \|_C$ 表示在 $\mathcal{X}$ 上的范数。同时， $B$ 是 $R^n$ 内的球， $S$ 是 $\mathcal{X}$ 中的球。根据定义， $P$ 为 $\mathcal{X}$ 到 $\mathcal{X}$ 的映射。为证明 $P$ 是 $S$ 到 $S$ 的映射，写出

$$(P x) (t) - x _ {0} = \int_ {t _ {0}} ^ {t} f (s, x (s)) d s = \int_ {t _ {0}} ^ {t} [ f (s, x (s)) - f (s, x _ {0}) + f (s, x _ {0}) ] d s$$

由 $f$ 的分段连续性可知， $f(t, x_0)$ 在 $[t_0, t_1]$ 上是有界的。设

$$h = \max _ {t \in [ t _ {0}, t _ {1} ]} \| f (t, x _ {0}) \|$$

利用利普希茨条件(3.2)以及对于每个 $x\in S$ ，有

$$\| x (t) - x _ {0} \| \leqslant r, \quad \forall t \in [ t _ {0}, t _ {0} + \delta ]$$

可得

$$
\begin{array}{l} \| (P x) (t) - x _ {0} \| \leqslant \int_ {t _ {0}} ^ {t} [ \| f (s, x (s)) - f (s, x _ {0}) \| + \| f (s, x _ {0}) \| ] d s \\ \leqslant \int_ {t _ {0}} ^ {t} [ L \| x (s) - x _ {0} \| + h ] d s \leqslant \int_ {t _ {0}} ^ {t} (L r + h) d s \\ = (t - t _ {0}) (L r + h) \leqslant \delta (L r + h) \\ \end{array}
$$

和

$$\| P x - x _ {0} \| _ {C} = \max _ {t \in [ t _ {0}, t _ {0} + \delta ]} \| (P x) (t) - x _ {0} \| \leqslant \delta (L r + h)$$

因此,选择 $\delta\leqslant r/(Lr+h)$ , 即保证 P 是 S 到 S 的映射。为了证明 P 是 S 上的压缩映射, 设 $x, y\in S$ , 并考虑

$$
\begin{array}{l} \| (P x) (t) - (P y) (t) \| = \left\| \int_ {t _ {0}} ^ {t} [ f (s, x (s)) - f (s, y (s)) ] d s \right\| \\ \leqslant \int_ {t _ {0}} ^ {t} \| f (s, x (s)) - f (s, y (s)) \| d s \\ \leqslant \int_ {t _ {0}} ^ {t} L \| x (s) - y (s) \| d s \leqslant \int_ {t _ {0}} ^ {t} d s L \| x - y \| _ {C} \\ \end{array}
$$

因此

$$\| P x - P y \| _ {C} \leqslant L \delta \| x - y \| _ {C} \leqslant \rho \| x - y \| _ {C}, \quad \delta \leqslant \frac {\rho}{L}$$

这样,选择 $\rho<1$ 和 $\delta\leqslant\rho/L$ 即保证 P 是 S 上的压缩映射。由压缩映射定理可知,如果选择 $\delta$ 满足
