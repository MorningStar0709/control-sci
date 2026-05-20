$$J ^ {*} (x _ {0}, 0) = \int_ {0} ^ {t _ {f}} l (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t)) \mathrm{d} t. \tag {7.4.51}$$

另一方面，任取 $(u(t), v(t)) \in \mathcal{W}_{[0, t_f]}$ ，考虑方程

$$
\begin{array}{l} \dot {x} = f (x, u ^ {*} (t), v (t)), \quad x (0) = x _ {0}, \\ \dot {x} = f (x, u (t), v ^ {*} (t)). \quad x (0) = x _ {0}, \\ \end{array}
$$

这里 $(u^{*}(t), v^{*}(t))$ 由式 (7.4.49) 所定义。显然有 $(u^{*}, v) \in \mathcal{W}_{[0, t_{f}]}$ , $(u, v^{*}) \in \mathcal{W}_{[0, t_{f}]}$ 。设 $x_{1}(t)$ 和 $x_{2}(t)$ 分别为上两方程的解。

将 $(x_{1}(t), u^{*}(t), v(t))$ 和 $(x_{2}(t), u(t), v^{*}(t))$ 分别代入 (7.4.46) 和 (7.4.47) 得到

$$
\begin{array}{l} \left\{ \begin{array}{l} \frac {\partial J ^ {*} (x _ {1} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x _ {1} (t) , t)}{\partial x} f (x _ {1} (t), u ^ {*} (t), v (t)) + l (x _ {1} (t), u ^ {*} (t), v (t)) \leqslant 0, \\ J ^ {*} (x _ {1} (t _ {f}), t _ {f}) = 0, \forall t \in [ 0, t _ {f} ], \end{array} \right. \\ \left\{ \begin{array}{l} \frac {\partial J ^ {*} (x _ {2} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x _ {2} (t) , t)}{\partial x} f (x _ {2} (t), u (t), v ^ {*} (t)) + l (x _ {2} (t), u (t), v ^ {*} (t)) \geqslant 0, \\ J ^ {*} (x _ {2} (t _ {f}), t _ {f}) = 0. \end{array} \right. \tag {7.4.53} \\ \end{array}
$$

从 0 到 $t_{f}$ 积分不等式 (7.4.52) 和 (7.4.53)，并利用终值条件，容易得到

$$\int_ {0} ^ {t _ {f}} l (x _ {1} (t), u ^ {*} (t), v (t)) \mathrm{d} t \leqslant J ^ {*} (x _ {0}, 0) \leqslant \int_ {0} ^ {t _ {f}} l (x _ {2} (t), u (t), v ^ {*} (t)) \mathrm{d} t.$$

由于

$$
\begin{array}{l} J [ u ^ {*}, v ] = \int_ {0} ^ {t _ {f}} l (x _ {1} (t), u ^ {*} (t), v (t)) \mathrm{d} t, \\ J [ u, v ^ {*} ] = \int_ {0} ^ {t _ {f}} l (x _ {2} (t), u (t), v ^ {*} (t)) \mathrm{d} t, \\ J [ u ^ {*}, v ^ {*} ] = \int_ {0} ^ {t _ {f}} l (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t)) \mathrm{d} t = J ^ {*} (x _ {0}, 0), \\ \end{array}
$$

故 $\forall (u(t), v(t)) \in \mathcal{W}_{[0, t_f]}$ ，下列鞍点条件成立：

$$J [ u ^ {*}, v ] \leqslant J [ u ^ {*}, v ^ {*} ] \leqslant J [ u, v ^ {*} ].$$

综上所述我们得到

定理 7.4.2 假设 HJI 方程 (7.4.42) 存在古典解 $(J^{*}(x,t), u^{*}(x,t), v^{*}(x,t))$ ，则 $(u^{*}(x,t), v^{*}(x,t))$ 是定量微分对策问题 (7.4.30)\~(7.4.34) 的状态反馈形式的最优策略函数.

推论 7.4.1 对于终端状态 $x(t_{f})$ 固定或对策指标中包含有非积分项 $k(x(t_{f}))$ 的情况，同样能够得到类似于定理 7.4.2 中的结论.

推论7.4.2 对于对策结束时刻 $t_f = +\infty$ 的情况，可得到形如下的HJI方程

$$
\left\{ \begin{array}{l} \min _ {u \in U} \max _ {v \in V} \left\{\frac {\partial J}{\partial x} f (x, u, v) + l (x, u, v) \right\} = 0, \\ J (0) = 0, \end{array} \right. \tag {7.4.54}
$$

并且类似于定理7.4.2的结论成立.

在一般情况下，带边值条件 HJI 方程仅存在古典意义下的局部解。对于线性定常二次定量微分对策问题，其相应的 HJI 方程存在古典意义下的全局解。

注7.4.2 用类似于极大值原理与Bellman方程之间关系的讨论方法，能够得到双方极值原理与Hamilton-Jacobi-Issacs方程之间关系的有关结果.
