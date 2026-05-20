注：对于定常系统，当 $t_f$ 固定时，最优解的必要条件同本表中 $t_f$ 的固定情况；当 $t_f$ 自由时，除 $H$ 变化律均为 $H^{*}(t_{f}^{*}) = 0$ 外，其余同本表中 $t_f$ 的自由情况。

例 10-9 设宇宙飞船登月舱的质量为 $m(t)$ ，高度为 $h(t)$ ，垂直速度为 $v(t)$ ，发动机推力为 $u(t)$ ，月球表面重力加速度为常数 g，不含燃料时登月舱质量为 M，初始燃料的总质量为 F。已知登月舱的状态方程为

$$
\begin{array}{l} \dot {h} (t) = v (t), \quad h (0) = h _ {0} \\ \dot {v} (t) = \frac {u (t)}{m (t)} - g, \quad v (0) = v _ {0} \\ \dot {m} (t) = - k u (t), \quad m (0) = M + F \\ \end{array}
$$

要求登月舱在月球表面实现软着陆，即目标集为

$$\psi_ {1} = h (t _ {f}) = 0, \quad \psi_ {2} = v (t _ {f}) = 0$$

发动机推力 $u(t)$ 的约束为

$$u (t) \in \Omega , \quad \Omega = \{u (t) \mid 0 \leqslant u (t) \leqslant \alpha \}, \quad \forall t \in [ 0, t _ {f} ]$$

试确定最优控制 $u^{*}(t)$ ，使登月舱由已知初态转移到要求的目标集，并使登月舱燃料消耗

$$J = - m (t _ {f}) = \min$$

解 本例为时变系统、末值型性能指标、 $t_{f}$ 自由、末端约束、控制受约束的最优控制问题。构造哈密顿函数

$$H = \lambda_ {1} v + \lambda_ {2} \left(\frac {u}{m} - g\right) - \lambda_ {3} k u$$

式中， $\lambda_1(t), \lambda_2(t)$ 和 $\lambda_3(t)$ 为待定的拉格朗日乘子。根据题意

$$\varphi = - m (t _ {f})$$

由协态方程

$$
\begin{array}{l} \dot {\lambda} _ {1} (t) = - \frac {\partial H}{\partial h} = 0 \\ \dot {\lambda} _ {2} (t) = - \frac {\partial H}{\partial v} = - \lambda_ {1} (t) \\ \dot {\lambda} _ {3} (t) = - \frac {\partial H}{\partial m} = \frac {\lambda_ {2} (t) u (t)}{m ^ {2} (t)} \\ \end{array}
$$

由横截条件

$$
\begin{array}{l} \lambda_ {1} (t _ {f}) = \frac {\partial \varphi}{\partial h (t _ {f})} + \frac {\partial \psi_ {1}}{\partial h (t _ {f})} \gamma_ {1} = \gamma_ {1} \\ \lambda_ {2} (t _ {f}) = \frac {\partial \varphi}{\partial v (t _ {f})} + \frac {\partial \psi_ {2}}{\partial v (t _ {f})} \gamma_ {2} = \gamma_ {2} \\ \lambda_ {3} (t _ {f}) = \frac {\partial \varphi}{\partial m (t _ {f})} = - 1 \\ \end{array}
$$

式中， $\gamma_{1}$ 和 $\gamma_{2}$ 为待定的拉格朗日乘子。

将哈密顿函数整理成

$$H = (\lambda_ {1} v - \lambda_ {2} g) + \left(\frac {\lambda_ {2}}{m} - k \lambda_ {3}\right) u$$

由极小值条件，H 相对 $u^{*}(t)$ 取绝对极小值。因此，最优控制

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} \alpha , & \frac {\lambda_ {2}}{m} - k \lambda_ {3} <   0 \\ 0, & \frac {\lambda_ {2}}{m} - k \lambda_ {3} > 0 \end{array} \right.
$$

上述结果表明,只有登月舱发动机推力在其最大值和零值之间进行开关控制,才有可能在软着陆的同时,保证登月舱的燃料消耗最少。
