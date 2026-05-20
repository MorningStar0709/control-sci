# 控制受约束的极大值原理 (Pontryagin 方法)

这里控制受约束是指 $\mathbb{U}_r$ 是 $\mathbb{R}^r$ 中有界闭子集。为简化叙述，这里假定 $f(x,u)$ 连续可微，并且存在常数 $a,b$ 满足

$$
\left\{ \begin{array}{l l} | f (x, u) | \leqslant \frac {a}{2}, & \forall x \in \mathbb {R} ^ {n}, u \in \mathbb {U} _ {r}, \\ | f (x, u) - f (y, u) | \leqslant b | x - y |, & \forall x, y \in \mathbb {R} ^ {n}, u \in \mathbb {U} _ {r}. \end{array} \right. \tag {7.1.32}
$$

首先讨论终端时刻 $t_f$ 固定情况。当 $x(t_f)$ 自由时，通过引入Lagrange乘子向量值函数 $\psi(t)$ 将式(7.1.1)和式(7.1.3)的最优控制问题中化为求 $u(t) \in \mathcal{U}_{[t_0, t_f]}$ 使 $J_1[u]$ 达到极小的问题。注意这里的 $J_1[u]$ 为

$$J _ {1} [ u ] = k (x (t _ {f})) + \int_ {t _ {0}} ^ {t _ {f}} \left(l (x (t), u (t)) + \psi^ {\mathrm{T}} (t) (\dot {x} (t) - f (x (t), u (t)))\right) \mathrm{d} t, \tag {7.1.33}$$

显然形式上与上面式 (7.1.5) 中的 $J_{1}[u]$ 完全相同，但由于要求 $u(t) \in \mathbb{U}_{r}$ ，从而不能直接采用上面的古典变分方法处理。本小节将采用“针状变分”方法。

利用式 (7.1.1) 和式 (7.1.3) 的 Hamilton 函数 $H(x, u, \psi) \stackrel{\mathrm{def}}{=} -l(x, u) + \psi^{\mathrm{T}}f(x, u)$ 将式 (7.1.33) 改写为

$$
\begin{array}{l} J _ {1} [ u ] = k \left(x \left(t _ {f}\right)\right) + \psi^ {\mathrm{T}} \left(t _ {f}\right) x \left(t _ {f}\right) - \psi^ {\mathrm{T}} \left(t _ {0}\right) x _ {0} \\ - \int_ {t _ {0}} ^ {t _ {f}} [ \dot {\psi} ^ {\mathrm{T}} (t) x (t) + H (x (t), u (t), \psi (t)) ] \mathrm{d} t. \\ \end{array}
$$

令 $u^{*}(t), x^{*}(t)$ 分别是最优控制和最优轨线，从而 $u^{*}(t)$ 使 $J_{1}[u]$ 达到极小。取形如下的控制函数 $u(t)$

$$u (t) = u ^ {*} (t) + \Delta u (t), \quad t \in [ t _ {0}, t _ {f} ], \tag {7.1.34}$$

其中 $\Delta u(t)$ 是定义在 $[t_0, t_f]$ 上的分段连续 $r$ 维向量值函数，且 $\forall t \in [t_0, t_f]$ 有 $u(t) \in \mathbb{U}_r$ 。称 $\Delta u(t)$ 为最优控制 $u^*(t)$ 的容许改变量。

式 (7.1.1) 对应于式 (7.1.34) 中 $u(t)$ 的轨线 $x(t)$ 可写成

$$x (t) = x ^ {*} (t) + \Delta x (t), \tag {7.1.35}$$

其中 $\Delta x(t)$ 称为最优轨线 $x^{*}(t)$ 对应于 $\Delta u(t)$ 的改变量，它满足

$$
\left\{ \begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} (\Delta x (t)) = f (x ^ {*} (t) + \Delta x (t), u ^ {*} (t) + \Delta u (t)) - f (x ^ {*} (t), u ^ {*} (t)), \\ \Delta x (t _ {0}) = 0. \end{array} \right. \tag {7.1.36}
$$

将式 (7.1.34), (7.1.35) 中 $u(t)$ , $x(t)$ 对应的 $J_{1}[u]$ 与 $J_{1}[u^{*}]$ 相减得 $J_{1}[u^{*}]$ 的改变量 $\Delta J_{1}[u]$ 为
