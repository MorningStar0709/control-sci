# 无穷时间区间上的线性二次最优控制问题

无穷时间区间上的线性二次最优控制是指终端时刻 $t_f = +\infty$ ，状态方程和性能指标分别为

$$
\begin{array}{l} \dot {x} (t) = A (t) x (t) + B (t) u (t), \quad x (t _ {0}) = x _ {0}, \\ \mathbb {U} _ {r} = \mathbb {R} ^ {r} \\ \end{array}
J [ u ] = \frac {1}{2} \int_ {t _ {0}} ^ {+ \infty} \left[ x ^ {\mathrm{T}} (t) Q (t) x (t) + u ^ {\mathrm{T}} (t) R (t) u (t) \right] \mathrm{d} t. \tag {7.3.19}
$$

这里 $A(t), B(t), Q(t)$ 和 $R(t)$ 皆是定义在 $[t_0, +\infty)$ 上的连续或分段连续矩阵函数.

定义7.3.1 称线性控制系统(7.3.1)在每个有限时刻 $t \geqslant 0$ 都是完全零能控的，如果对每个时刻 $t \geqslant 0$ 和任意状态 $x(\neq 0) \in \mathbb{R}^n$ ，必定存在控制函数 $\tilde{u}(s)$ 和有限时刻 $\bar{t}$ ，使得(7.3.1)在 $\tilde{u}(s)$ 的作用下，从 $t$ 时刻状态 $x$ 出发的轨线 $\tilde{x}(s)$ 满足 $\tilde{x}(\bar{t}) = 0$ .

考察如下 Riccati 矩阵微分方程的终值问题:

$$
\left\{ \begin{array}{l} \dot {P} + P A (t) + A ^ {\mathrm{T}} (t) P + Q (t) - P B (t) R ^ {- 1} (t) B ^ {\mathrm{T}} (t) P = 0, \\ P \left(t _ {f}\right) = 0. \end{array} \right. \tag {7.3.20}
$$

由定理7.3.1知，对任意固定 $t_f > t_0$ ，方程(7.3.20）在 $[t_0, t_f)$ 上存在唯一正定对称矩阵解 $P(t; t_f, 0) = [p_{ij}(t; t_f, 0)]$ .

引理7.3.1 设 $P(t; t_f, 0)$ 为方程 (7.3.20) 在 $[t_0, t_f]$ 上的唯一对称解阵，且 $P(t; t_f, 0) > 0, \forall t \in [t_0, t_f)$ ，如果系统 (7.3.1) 在每个时刻 $t \geqslant 0$ 都是完全零能控的，则有极限

$$\lim _ {t _ {f} \rightarrow + \infty} P (t; t _ {f}, 0) = \bar {P} (t), \quad \forall t \geqslant t _ {0}, \tag {7.3.21}$$

而 $\dot{P}(t)$ 在 $[t_0, +\infty)$ 上满足方程 (7.3.20) 中的矩阵微分方程.

证明 先证 $\bar{P}(t)$ 的存在性. 由假设知, 对于任意 $t \geqslant 0$ 和 $x \in \mathbb{R}^n$ , 存在 $\bar{u}(s)$ 和 $t_2 > t$ , 使得在 $\bar{u}(s)$ 的作用下, 系统 (7.3.1) 从 $t$ 时刻状态 $x$ 出发的轨线 $\tilde{x}(s)$ 满足 $\tilde{x}(t_2) = 0$ . 现定义控制函数 $\bar{u}(s)$

$$
\bar {u} (s) = \left\{ \begin{array}{l l} {\bar {u} (s),} & {\text {当} s \in [ t, t _ {2} ],} \\ {0,} & {\text {当} s \in [ t _ {2}, + \infty).} \end{array} \right.
$$

于是在 $\bar{u}(s)$ 作用下，系统(7.3.1)从 $\bar{x} (t) = x$ 出发的轨线 $\bar{x} (s)$ 为

$$
\bar {x} (s) = \left\{ \begin{array}{l l} {\bar {x} (s),} & {\text {当} s \in [ t, t _ {2} ],} \\ {0,} & {\text {当} s \in [ t _ {2}, + \infty).} \end{array} \right.
$$

显然，相应于 $(\bar{u}(s),\bar{x} (s))$ 的性能指标值 $J[\bar{u} (\cdot)] <   + \infty$ 因此无穷时间区间上线性二次最优控制问题的容许控制集 $\mathcal{U}_{[t_0, + \infty)}$ 非空.

对任意固定 $t_f > t_0$ ，记

$$J [ u; t, x, t _ {f} ] = \frac {1}{2} \int_ {t} ^ {t _ {f}} \left[ x ^ {\mathrm{T}} (\tau) Q (\tau) x (\tau) + u ^ {\mathrm{T}} (\tau) R (\tau) u (\tau) \right] \mathrm{d} \tau , \quad \forall u (\tau) \in \mathcal {U} _ {[ t, t _ {f} ]},$$

其中 $x(\tau)$ 是式 (7.3.1) 从 $x(t) = x$ 出发的轨线。根据定理7.3.1和 $\bar{u}(s)$ 的形式得到
