# 4.4 最少燃料控制问题

在人类的经济活动、军事行动以及其他活动中无时无刻不在消耗着形形色色的燃料，减少燃料消耗，节省能源成了当今世界科研的重要课题。特别在宇宙航行中，所消耗的燃料十分昂贵，而且如果需要的燃料多了，会减少运送的有效载荷（如卫星、空间站等），因此在宇宙航行中最早提出了最少燃料消耗的最优控制问题。一般来说，控制物体运动的推力或力矩的大小，是和单位时间内燃料消耗量成正比的，因而在某一过程中所消耗的燃料总量可用下面的积分指标来表示

$$J (u) = \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} | u (t) | \mathrm{d} t$$

其中 $u(t)$ 是单位时间内的燃料消耗量。

值得指出的是,在最少燃料控制问题中,终端时间 $t_{f}$ 一般应给定,或者是考虑响应时间和最少燃料的综合最优问题。因为若考虑纯粹的最少燃料控制问题，则将导致系统的响应时间过长，理论上要经过无穷长时间，系统才转移到所要求的状态。这是很显然的，因为燃料消耗得少，推力就小，系统的运动加速度和速度就小。另一方面所指定的时间 $t_{f}$ 必须大于同一问题的最短时间控制所解出的最短时间 $t_{f}^{*}$ ，否则最少燃料控制将会无解。这里还是以重积分系统为例来说明最少燃料控制的解法。

例4-3 重积分系统的最少燃料控制

系统状态方程

$$\dot {x} _ {1} = x _ {2} \quad \dot {x} _ {2} = u \tag {4-56}$$

初始条件

$$x _ {1} \left(t _ {0}\right) = x _ {1 0} \quad x _ {2} \left(t _ {0}\right) = x _ {2 0} \tag {4-57}$$

终端条件

$$x _ {1} \left(t _ {\mathrm{f}}\right) = 0 \quad x _ {2} \left(t _ {\mathrm{f}}\right) = 0 \tag {4-58}$$

控制约束

$$\mid u (t) \mid \leqslant 1 \quad t _ {0} \leqslant t \leqslant t _ {\mathrm{f}} \tag {4-59}$$

求出使性能指标

$$J = \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} | u (t) | \mathrm{d} t \tag {4-60}$$

取极小的最优控制。

解 用极小值原理求解,哈密顿函数为

$$H = | u (t) | + \lambda_ {1} (t) x _ {2} (t) + \lambda_ {2} (t) u (t) \tag {4-61}$$

协态方程为

$$\dot {\lambda} _ {1} = - \frac {\partial H}{\partial x _ {1}} = 0 \tag {4-62}\dot {\lambda} _ {2} = - \frac {\partial H}{\partial x _ {2}} = - \lambda_ {1}$$

积分上面两个方程可得

$$\lambda_ {1} (t) = c _ {1} \tag {4-63}\lambda_ {2} (t) = c _ {2} - c _ {1} t$$

这里哈密顿函数 H 与最短时间控制的 H 不同, 考察 H 的表达式可知, 无论 $\lambda_{1}(t)x_{2}(t)$ 为何值, 使 H 极小等价于求下式的极小:

$$\min _ {u (t) \in \Omega} [ | u (t) | + \lambda_ {2} (t) u (t) ]$$

考察上面的表达式，当 $|\lambda_2(t)| < 1$ 时，如 $u(t) \neq 0$ ，则 $[|u(t)| + \lambda_2(t) \cdot u(t)] > 0$ ，故应取 $u(t) = 0$ ；当 $|\lambda_2(t)| > 1$ 时，则应取 $u(t) = -\operatorname{sgn}[\lambda_2(t)]$ ，使 $[|u(t)| + \lambda_2(t)u(t)] < 0$ ，于是可得出使 $H$ 极小的最优控制规律为

$$u (t) = 0 \quad \text {当} | \lambda_ {2} (t) | < 1 \quad (4 - 6 4)u (t) = - \operatorname{sgn} [ \lambda_ {2} (t) ] \qquad \text {当} | \lambda_ {2} (t) | > 1 \tag {4-65}0 \leqslant u (t) \leqslant 1 \quad \text {当} \lambda_ {2} (t) = - 1 \tag {4-66}- 1 \leqslant u (t) \leqslant 0 \quad \text {当} \lambda_ {2} (t) = + 1 \tag {4-67}$$
