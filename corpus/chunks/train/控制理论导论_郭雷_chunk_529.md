$$\int_ {t _ {0}} ^ {t _ {f} ^ {*}} v _ {j _ {0}} (t) \left[ u _ {j _ {0}} ^ {*} (t) - u _ {j _ {0}} ^ {m} (t) \right] \mathrm{d} t = \int_ {\mathcal {M}} \left[ u _ {j _ {0}} ^ {*} (t) - u _ {j _ {0}} ^ {m} (t) \right] \mathrm{d} t, \quad \forall m \geqslant 1,$$

由此从不等式 (7.2.38) 得到

$$\int_ {t _ {0}} ^ {t _ {f} ^ {*}} v _ {j _ {0}} (t) \left[ u _ {j _ {0}} ^ {*} (t) - u _ {j 0} ^ {m} (t) \right] \mathrm{d} t \geqslant \int_ {\mathcal {M}} \left[ u _ {j _ {0}} ^ {*} (t) - 1 \right] \mathrm{d} t \geqslant 0.$$

令 $m \to +\infty$ ，可得

$$0 \geqslant \int_ {\mathcal {M}} \left[ u _ {j _ {0}} ^ {*} (t) - 1 \right] \mathrm{d} t \geqslant 0,$$

即有

$$\int_ {\mathcal {M}} \left[ u _ {j 0} ^ {*} (t) - 1 \right] \mathrm{d} t = 0.$$

由此依不等式 (7.2.36) 必有 $\operatorname{mes} \mathcal{M} = 0$ 。因此，对 $[t_0, t_f^*]$ 几乎所有的 $t$ 皆有 $u_{j_0}^* \leqslant 1$ 。同理可证，对 $[t_0, t_f^*]$ 上几乎所有 $t$ 皆有 $u_{j_0}^*(t) \geqslant -1$ 。

注意到，在 $[t_0, t_f^*]$ 的任一个零测集上改变 $u^m(t)$ 的值不影响其弱收敛于 $u^*(t)$ 的结论，所以不失一般性，不妨认为， $\forall t \in [t_0, t_f^*]$ ，成立

$$\left| u _ {j} ^ {*} (t) \right| \leqslant 1, \quad j = 1, 2, \dots , r,$$

即存在满足控制约束 (7.2.12) 的 $u^{*}(t) \in L_{[t_{0}, t_{f}^{*} ]}$ , 它把 $x_{0}$ 在 $t_{f}^{*}$ 时刻控制到零状态.

此外，根据方程(7.2.18)为正则系统的假设知，满足式(7.2.12)的快速控制函数是唯一的，且是Bang-Bang型的，从而 $u^{*}(t)$ 是分段常值的，即 $u^{*}(t) \in \mathcal{U}_{[t_{0}, t_{f}^{*} ]}$ .

例 7.2.1 考虑如下常见的双积分 (环节) 系统的快速控制:

$$m \ddot {y} = u (t).$$

卫星等航天器的单通道姿态运动常可简化为这类模型.

控制的目的是要求姿态角 $y$ 尽快地达到某标称值（不妨设为零），且角速度 $\dot{y}$ 也为零.

通过引入相坐标能得到双积分系统的状态方程

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2}, \\ \dot {x} _ {2} = u. \end{array} \right.
$$

相应的初态、控制约束、目标集、性能指标分别是

$$
\begin{array}{l} \left(x _ {1 0}, x _ {2 0}\right) ^ {\mathrm{T}} \in \mathbb {R} ^ {2}, | u | \leqslant 1, \\ S = \left\{\left(x _ {1} (t _ {f}), x _ {2} (t _ {f})\right) ^ {\mathrm{T}} \mid x _ {1} (t _ {f}) = x _ {2} (t _ {f}) = 0 \right\}, \\ J [ u ] = \int_ {0} ^ {t _ {f}} d t = t _ {f}. \\ \end{array}
$$

问题是求快速控制综合函数 $u^{*}(x)$

(1) 判别所控制问题的正则性和容许控制集的非空性. 由

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] = A \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + b u, \quad A = \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right], \quad b = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right]
$$

知 $\operatorname{rank}[b, Ab] = \operatorname{rank}\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = 2$ , 因此系统是正则的. 零是 $A$ 的二重特征值. 从系统的正则性和定理7.2.7可知容许控制集合非空. 因此双积分系统的快速控制存在唯一, 并可由极大值原理求得.

(2) 利用极大值原理求快速控制函数. Hamilton 函数为
