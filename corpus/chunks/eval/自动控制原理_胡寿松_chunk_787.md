# 例 10-6 设一阶系统方程为

$$\dot {x} (t) = u (t)$$

已知 $x(0) = 1$ ，要求 $x(t_{f}) = 0$ ，试求使性能指标

$$J = t _ {f} + \frac {1}{2} \int_ {0} ^ {t _ {f}} u ^ {2} (t) d t$$

为极小的最优控制 $u^{*}(t)$ ，以及相应的最优轨线 $x^{*}(t)$ 、最优末端时刻 $t_f^*$ 、最小指标 $J^{*}$ 。其中，末端时刻 $t_f$ 未给定。

解 本例为复合型性能指标、 $t_{f}$ 自由、末端固定、控制无约束的泛函极值问题。

由已知的系统方程知，系统是可控的。令

$$H = \frac {1}{2} u ^ {2} + \lambda u$$

因 $\dot{\lambda}(t) = -\frac{\partial H}{\partial x} = 0$ ，故 $\lambda(t) = a = \mathrm{const}$ 。再由

$$\frac {\partial H}{\partial u} = u + \lambda = 0, \quad \frac {\partial^ {2} H}{\partial u ^ {2}} = 1 > 0u ^ {*} (t) = - \lambda (t) = - a$$

可使 $H = \min$ 。由状态方程

$$\dot {x} (t) = u = - a, \qquad \int_ {x (0)} ^ {x (t)} \mathrm{d} x = - \int_ {0} ^ {t} a \mathrm{d} t$$

代入 $x(0) = 1$ ，解出

$$x ^ {*} (t) = 1 - a t$$

利用已知的末态条件

$$x (t _ {f}) = 1 - a t _ {f} = 0, \quad t _ {f} = 1 / a$$

最后,根据 H 变化律条件

$$H (t _ {f}) = - \frac {\partial \varphi}{\partial t _ {f}} = - 1, \quad \frac {1}{2} u ^ {2} (t _ {f}) + \lambda (t _ {f}) u (t _ {f}) = - 1$$

求得 $\frac{1}{2} a^2 - a^2 = -1, \quad a = \sqrt{2}$

于是，本例最优解如下：

$$u ^ {*} = - \sqrt {2}, \quad x ^ {*} (t) = 1 - \sqrt {2} tt _ {f} ^ {*} = \sqrt {2} / 2, \quad J ^ {*} = \sqrt {2}$$
