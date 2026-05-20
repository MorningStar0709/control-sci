# 2) 边界条件

$$\boldsymbol {x} (0) = \boldsymbol {x} _ {0}, \quad \boldsymbol {x} (t _ {f}) = \mathbf {0}$$

3）极小值条件

$$
u _ {j} ^ {*} (t) = - \operatorname{sgn} \left(\boldsymbol {b} _ {j} ^ {\mathrm{T}} \boldsymbol {\lambda}\right) = \left\{ \begin{array}{l l} + 1, & \boldsymbol {b} _ {j} ^ {\mathrm{T}} \boldsymbol {\lambda} <   0 \\ - 1, & \boldsymbol {b} _ {j} ^ {\mathrm{T}} \boldsymbol {\lambda} > 0 \end{array} \quad (j = 1, 2, \dots , m) \right.
$$

式中， $b_{j}\in R^{n}$ ，为矩阵B的列向量。

4) 沿最优轨线 H 变化律

$$H ^ {*} \left(t _ {f} ^ {*}\right) = 0$$

例10-11 设系统状态方程为

$$\dot {x} _ {1} (t) = x _ {2} (t), \quad \dot {x} _ {2} (t) = u (t)$$

边界条件为

$$x _ {1} (0) = x _ {1 0}, \quad x _ {2} (0) = x _ {2 0}, \quad x _ {1} (t _ {f}) = x _ {2} (t _ {f}) = 0$$

控制变量的不等式约束为 $|u(t)|\leqslant1$ ，性能指标

$$J = \int_ {0} ^ {t _ {f}} \mathrm{d} t = t _ {f}$$

求最优控制 $u^{*}(t)$ ，使 J 极小。

解 本例为二次积分模型的最小时间控制问题。不难验证，系统可控，因而正常，故时间最优控制必为 Bang-Bang 控制，可用极小值原理求解。构造哈密顿函数

$$H = 1 + \lambda_ {1} x _ {2} + \lambda_ {2} u$$

由定理 10-17 知, 最优控制

$$
u ^ {*} (t) = - \operatorname{sgn} \{\lambda_ {2} (t) \} = \left\{ \begin{array}{l l} + 1, & \lambda_ {2} (t) <   0 \\ - 1, & \lambda_ {2} (t) > 0 \end{array} \right.
$$

由协态方程

$$
\begin{array}{l} \lambda_ {1} (t) = - \frac {\partial H}{\partial x _ {1}} = 0, \qquad \qquad \lambda_ {1} (t) = c _ {1} \\ \lambda_ {2} (t) = - \frac {\partial H}{\partial x _ {2}} = - \lambda_ {1} (t), \qquad \lambda_ {2} (t) = - c _ {1} t + c _ {2} \\ \end{array}
$$

式中， $c_{1}$ 和 $c_{2}$ 为待定常数。

若令 $u^{*} = 1$ ，状态方程的解为

$$
\begin{array}{l} \dot {x} _ {2} (t) = 1, \quad x _ {2} (t) = t + x _ {2 0} \\ \dot {x} _ {1} (t) = t + x _ {2 0}, \quad x _ {1} (t) = \frac {1}{2} t ^ {2} + x _ {2 0} t + x _ {1 0} \\ \end{array}
$$

在解 $\{x_{1}(t), x_{2}(t)\}$ 中，消去 $t$ ，求得相应的最优轨线方程

$$x _ {1} = \frac {1}{2} x _ {2} ^ {2} + \left(x _ {1 0} - \frac {1}{2} x _ {2 0}\right)$$

上式表示一簇抛物线，如图10-5中实线所示。图中曲线上的箭头表示时间 $t$ 的增加方向，由于 $x_{2}(t) = t + x_{20}$ ，故 $x_{2}(t)$ 随 $t$ 的增加而增大。显然，满足末态要求的最优轨线为 $\widehat{AO}$ ，表示为

$$\gamma_ {+} = \left\{(x _ {1}, x _ {2}) \mid x _ {1} = \frac {1}{2} x _ {2} ^ {2}, x _ {2} \leqslant 0 \right\} \tag {10-87}$$

若令 $u^{*} = -1$ ，状态方程的解为

$$\dot {x} _ {2} (t) = - 1, \quad x _ {2} (t) = - t + x _ {2 0}\dot {x} _ {1} (t) = - t + x _ {2 0}, \quad x _ {1} (t) = - \frac {1}{2} t ^ {2} + x _ {2 0} t + x _ {1 0}$$

相应的最优轨线方程为

$$x _ {1} = - \frac {1}{2} x _ {2} ^ {2} + \left(x _ {1 0} + \frac {1}{2} x _ {2 0}\right)$$

上式也描绘了一簇抛物线,如图 10-5 中虚线所示。显然满足末态要求的最优轨线为 $\widehat{BO}$ ,可以表示为
