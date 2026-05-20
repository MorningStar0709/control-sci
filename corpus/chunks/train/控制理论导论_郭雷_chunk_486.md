# 最优控制问题叙述

为了对一个实际的工程被控对象实施最优控制，通常需要：

(1) 有一个表征被控对象的动力学模型，通常用一阶常微分方程组描述

$$\dot {x} = f (x, u, t), \tag {7.1.1}$$

它称为系统的状态方程，其中状态变量 $x \in \mathbb{R}^n$ ，控制变量 $u \in \mathbb{U}_r \subseteq \mathbb{R}^r$ ，时间变量 $t \in [t_0, t_f]$ ， $t_0 < t_f, n, r$ 为正整数，且 $r \leqslant n$ ； $f: \mathbb{R}^n \times \mathbb{U}_r \times [t_0, t_f] \to \mathbb{R}^n$ ;

(2) 存在控制 $u(t)$ 使系统 (7.1.1) 从初态 $x(t_0) = x_0$ 出发，于时刻 $t_f$ ，状态 $x(t_f)$ 达到目标集 $S$ 上

$$S = \{x \in \mathbb {R} ^ {p} \mid g (x, t _ {f}) = 0 \}, \tag {7.1.2}$$

其中 $g: \mathbb{R}^n \times (t_0, +\infty) \to \mathbb{R}^p, p \leqslant n, t_f$ 称为终端时刻；

(3) 有一个表征系统控制过程品质的泛函指标 $J[u]$ (性能指标) $-\infty < J[u] < +\infty$

$$J [ u ] = k (x (t _ {f}), t _ {f}) + \int_ {t _ {0}} ^ {t _ {f}} l (x (t), u (t), t) \mathrm{d} t, \tag {7.1.3}$$

其中 $k: \mathbb{R}^n \times (t_0, +\infty) \to \mathbb{R}^1, l: \mathbb{R}^n \times \mathbb{U}_r \times [t_0, t_f] \to \mathbb{R}^1, x(t)$ 是系统 (7.1.1) 在控制 $u(t)$ 作用下从初始状态 $x(t_0) = x_0$ 出发的轨线；

(4) 有一个使系统控制过程有意义的控制函数类，称之为容许控制函数类，其中每个函数称为容许控制。本章取容许控制函数类 $U_{[t_0, t_f]}$ 为

$$\mathcal {U} _ {[ t _ {0}, t _ {f} ]} = \left\{u (\cdot): [ t _ {0}, t _ {f} ] \to \mathbb {U} _ {r} \mid u (\cdot) \text {有界分段连续,} x (t _ {f}; t _ {0}, x _ {0}, u) \in S \right\},$$

其中 $x(t; t_0, x, u)$ 表示方程 (7.1.1) 的满足 $x(t_0) = x_0$ 的解.

今后我们把方程 (7.1.1) 在 $u(t) \in \mathcal{U}_{[t_0, t_f]}$ 作用下 $t_0$ 时刻从 $x_0$ 出发的解 $x(t) = x(t; t_0, x, u)$ 简称为方程 (7.1.1) 对应于 $u(t)$ 的轨线.

所谓系统 (7.1.1) 以式 (7.1.3) 为性能指标的最优控制问题是指选择容许控制 $u^{*}(\cdot) \in \mathcal{U}_{[t_{0}, t_{f}]}$ , 使得 $J(u^{*}) = \min_{u \in \mathcal{U}_{[t_{0}, t_{f}]} J[u]}$ . $u^{*}(t)$ 称为式 (7.1.1) 和式 (7.1.3) 的最优控制, 式 (7.1.1) 相应于 $u^{*}(t)$ 的轨线 $x^{*}(t)$ 称为最优轨线, $x^{*}(t)$ 到达目标集 $S$ 的时刻 $t_{f}^{*}$ 称为最优过渡时刻 (当 $t_{f}$ 非固定时), 相应于 $u^{*}(t)$ 的指标值 $J[u^{*}]$ 称为最优性能指标值, 即

$$J \left[ u ^ {*} \right] = k \left(x ^ {*} \left(t _ {f} ^ {*}\right), t _ {f} ^ {*}\right) + \int_ {t _ {0}} ^ {t _ {f} ^ {*}} l \left(x ^ {*} (t), u ^ {*} (t), t\right) d t. \tag {7.1.4}$$

$(u^{*}(t), x^{*}(t))$ 简称为最优控制问题 (7.1.1), (7.1.3) 的解.

下面，为简化讨论，总假设 $f(x,u,t), g(x,t), k(x,t)$ 和 $l(x,u,t)$ 皆是在其定义区域内连续可微的。如果不特别注明，总认为系统的初始时刻 $t_0(\geqslant 0)$ 和初始状态 $x_0 \in \mathbb{R}^n$ 是固定的。注意，若引入新变量 $x_{n+1} = t$ ，则 $\frac{\mathrm{d}x_{n+1}}{\mathrm{d}t} = 1$ ，从而能将非定常问题化为定常问题。因此，为简化叙述，我们主要论及定常最优控制问题，即上面的函数 $f, g, k$ 和 $l$ 皆不显含时间 $t$ 。对于 $f, g, k$ 和 $l$ 显含时间 $t$ 的情况，仅列出相应结果。
