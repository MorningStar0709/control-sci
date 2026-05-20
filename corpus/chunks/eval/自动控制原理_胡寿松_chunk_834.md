2) 在定理 10-21 中, 要求阵对 $\{A, D\}$ 完全可观, 是为了保证最优闭环系统 (10-124) 渐近稳定性。如果强化性能指标中权阵 Q 的条件, 要求 $Q = Q^{T} > 0$ , 则可去掉 $\{A, D\}$ 可观的要求。至于 $\bar{P}$ 矩阵的正定性, 卡尔曼曾经指出: 系统可控的假设和取权阵 F = 0, 意味着 $t_{f} \to \infty$ 时, $\bar{P}$ 为正定矩阵。  
3）对于无限时间状态调节器，通常在性能指标中不考虑终点指标，取权阵 $F = 0$ ，其原因有二：一是希望 $t_f \to \infty$ 时， $x(t_f) = 0$ ，即要求稳态误差为零，因而在性能指标中不必加入体现终点指标的末值项；二是工程上仅考虑系统在有限时间内的响应，因而 $t_f \to \infty$ 时的终点指标将失去工程意义。

例 10-14 设系统状态方程及初始条件为

$$\dot {x} _ {1} (t) = u (t), \quad x _ {1} (0) = 0\dot {x} _ {2} (t) = x _ {1} (t), \quad x _ {2} (0) = 1$$

性能指标

$$J = \int_ {0} ^ {\infty} \left[ x _ {2} ^ {2} (t) + \frac {1}{4} u ^ {2} (t) \right] \mathrm{d} t$$

试求最优控制 $u^{*}(t)$ 和最优性能指标 $J^{*}$ 。

解 本例为无限时间状态调节器问题。因

$$
\begin{array}{l} J = \frac {1}{2} \int_ {0} ^ {\infty} \left(2 x _ {2} ^ {2} + \frac {1}{2} u ^ {2}\right) d t \\ = \frac {1}{2} \int_ {0} ^ {\infty} \left\{\left[ x _ {1} x _ {2} \right] \left[ \begin{array}{l l} 0 & 0 \\ 0 & 2 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \frac {1}{2} u ^ {2} \right\} d t \\ \end{array}
$$

故由题意

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 0 \\ 1 & 0 \end{array} \right], \quad \boldsymbol {b} = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right], \quad \boldsymbol {Q} = \left[ \begin{array}{l l} 0 & 0 \\ 0 & 2 \end{array} \right], \quad r = \frac {1}{2}, \quad \boldsymbol {d} ^ {\mathrm{T}} = [ 0 \sqrt {2} ]
$$

检验可控性与可观性：

$$
\begin{array}{l} \operatorname{rank} [ \boldsymbol {b} \boldsymbol {A b} ] = \operatorname{rank} \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] = 2 \\ \operatorname{rank} \left[ \begin{array}{c} \boldsymbol {d} ^ {\mathrm{T}} \\ \boldsymbol {d} ^ {\mathrm{T}} \boldsymbol {A} \end{array} \right] = \operatorname{rank} \left[ \begin{array}{c c} 0 & \sqrt {2} \\ \sqrt {2} & 0 \end{array} \right] = 2 \\ \end{array}
$$

故 $u^{*}(t)$ 存在且最优闭环系统渐近稳定。

解里卡蒂方程:令

$$
\bar {\boldsymbol {P}} = \left[ \begin{array}{c c} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right]
$$

由 $\overline{\pmb{P}}\pmb{A} + \pmb{A}^{\mathrm{T}}\overline{\pmb{P}} - \overline{\pmb{P}}\pmb{b}\pmb{r}^{-1}\pmb{b}^{\mathrm{T}}\overline{\pmb{P}} + \pmb{Q} = \mathbf{0}$

得代数方程组

$$2 P _ {1 2} - 2 P _ {1 1} ^ {2} = 0P _ {2 2} - 2 P _ {1 1} P _ {1 2} = 0- 2 P _ {1 2} ^ {2} + 2 = 0$$

联立求解，得

$$
\bar {\boldsymbol {P}} = \left[ \begin{array}{l l} 1 & 1 \\ 1 & 2 \end{array} \right] > 0
$$

求最优解：
