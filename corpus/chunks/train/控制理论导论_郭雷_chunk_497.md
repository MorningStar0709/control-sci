仍取方程 (7.1.16) 的解 $\psi(t)$ 作为 Lagrange 乘子函数，由式 (7.1.28) 有

$$H (x ^ {*} (t _ {f} ^ {*}), u ^ {*} (t _ {f} ^ {*}), \psi (t _ {f} ^ {*})) \delta t _ {f} + \int_ {t _ {0}} ^ {t _ {f} ^ {*}} \frac {\partial H}{\partial u} \Big | _ {*} \delta u (t) \mathrm{d} t = 0. \tag {7.1.29}$$

由此考虑到 $\delta t_f$ 和 $\delta u(t)$ 的任意性，根据引理7.1.1容易得到

$$H (x ^ {*} (t _ {f} ^ {*}), u ^ {*} (t _ {f} ^ {*}), \psi (t _ {f} ^ {*})) = 0, \tag {7.1.30}\frac {\partial H \left(x ^ {*} (t) , u ^ {*} (t) , \psi (t)\right)}{\partial u} = 0, \quad \forall t \in \left[ t _ {0}, t _ {f} ^ {*} \right]. \tag {7.1.31}$$

由于 $\Delta J_{3}(\varepsilon) = J_{3}(\varepsilon) - J_{3}(0)\geqslant 0,$ 利用证明不等式(7.1.18)相同的方法能够证明

$$\frac {\partial^ {2} H (x ^ {*} (t) , u ^ {*} (t) . \psi (t))}{\partial u ^ {2}} \leqslant 0, \quad \forall t \in \Omega (t _ {0}, t _ {f}; u ^ {*}),$$

即 $\frac{\partial^2H}{\partial u^2}\bigg|_*$ 在使 $u^{*}(t)$ 连续的任意时刻 $t\in [t_0,t_f]$ 都是半负定的.

利用 $u^{*}(t), x^{*}(t)$ 和 $\psi(t)$ 满足Hamilton正则方程组(7.1.21)和等式(7.1.30)，(7.1.31)，可以证在使 $u^{*}$ 连续的任意时刻 $t \in [t_0, t_f]$ ，有 $H(x^{*}(t), u^{*}(t), \psi(t)) = 0$ 。（上式的严格证明将在下面给出）

对于 $t_f$ 自由，系统终端状态受形如式 (7.1.2) 约束的情况，其最优控制 $u^*(t)$ ，最优轨线 $x^*(t)$ 和相应 $\psi(t)$ 满足的条件中仅 $\psi(t)$ 在终端时刻 $t_f$ 不相同，其余均与 $x(t_f)$ 自由时完全相同，即当 $x(t_f)$ 受式 (7.1.2) 约束时， $\psi(t)$ 在 $t_f^*$ 时满足横截条件

$$\psi^ {\mathrm{T}} (t _ {f}) = - \frac {\partial k (x ^ {*} (t _ {f} ^ {*}))}{\partial x} - \mu^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f} ^ {*}))}{\partial x},$$

这里 $\mu$ 为待定的Lagrange乘子向量．综上所述，得到控制变量无约束定常情况下的极大值原理如下：

定理 7.1.1 设定义在 $[t_{0}, t_{f}]$ 上的 $u^{*}(t)$ 是控制无约束定常最优控制问题 (7.1.1), (7.1.3) 的最优控制， $x^{*}(t)$ 是相应的最优轨线，则必定存在向量值函数 $\psi(t)$ ，它和 $x^{*}(t)$ , $u^{*}(t)$ 在 $[t_{0}, t_{f}]$ 上同时满足

(1)

$$
\left\{ \begin{array}{l l} {\dot {x} ^ {*} (t) = \left(\frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial \psi}\right) ^ {\mathrm{T}},} & {\quad x ^ {*} (t _ {0}) = x _ {0},} \\ {\dot {\psi} ^ {\mathrm{T}} (t) = - \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial x},} \\ {\psi^ {\mathrm{T}} (t _ {f}) = \left\{ \begin{array}{l l} {- \frac {\partial k (x ^ {*} (t _ {f}))}{\partial x},} & {\quad x (t _ {f}) \text {自由},} \\ {- \frac {\partial k (x ^ {*} (t _ {f}))}{\partial x} - \mu^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f}))}{\partial x},} & {\quad x (t _ {f}) \text {受约束} g (x (t _ {f})) = 0,} \end{array} \right.} \end{array} \right.
$$
