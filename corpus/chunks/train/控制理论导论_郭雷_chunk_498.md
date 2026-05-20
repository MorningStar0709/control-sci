其中 $H(x,u,\psi)\stackrel {\mathrm{def}}{=} - l(x,u) + \psi^{\mathrm{T}}(t)f(x,u)$ 为Hamilton函数， $\mu \in \mathbb{R}^p$ 为待求常向量；

(2) 在使 $u^{*}(t)$ 连续的所有时刻 $t \in [t_{0}, t_{f}]$ 有

$$
\begin{array}{l} \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial u} = 0, \\ \frac {\partial^ {2} H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial u ^ {2}} \leqslant 0; \\ \end{array}
$$

(3) $H(x^{*}(t), u^{*}(t), \psi(t)) =$ 常数，当 $t_f$ 固定时，此常数可能不为零，而当 $t_f$ 自由 (待求) 时，此常数一定为零.

对于 $f, g, k, l$ 显含时间 $t$ 的情况，其最优控制问题的极大值原理如下：

定理7.1.2 设 $u^{*}(t) \in \mathcal{U}_{[t_{0}, t_{f} ]}$ 是式(7.1.1)，(7.1.2)和式(7.1.3)的最优控制， $x^{*}(t)$ 是相应的最优轨线，则必定存在向量值函数 $\psi(t)$ ，它和 $x^{*}(t), u^{*}(t)$ 在 $[t_{0}, t_{f}]$ 上同时满足

(1)

$$
\left\{ \begin{array}{l l} {\dot {x} ^ {*} (t) = \left[ \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t) , t)}{\partial \psi} \right] ^ {\mathrm{T}},} & {x ^ {*} (t _ {0}) = x _ {0}} \\ {\dot {\psi} ^ {\mathrm{T}} (t) = - \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t) , t)}{\partial x}} \\ {\psi^ {\mathrm{T}} (t _ {f}) = \left\{ \begin{array}{l l} {- \frac {\partial k (x ^ {*} (t _ {f} ^ {*}) , t _ {f})}{\partial x},} & {x (t _ {f}) \text {自由},} \\ {- \frac {\partial k (x ^ {*} (t _ {f}) , t _ {f})}{\partial x} - \mu^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f}) , t _ {f})}{\partial x},} \\ & {x (t _ {f}) \text {受约束} g (x (t _ {f}), t _ {f}) = 0,} \end{array} \right.} \end{array} \right.
$$

其中 $H(x,u,\psi ,t)\stackrel {\mathrm{def}}{=}\sim l(x,u,t) + \psi^{\mathrm{T}}(t)f(x,u,t)$ 为Hamilton函数， $\mu \in \mathbb{R}^p$ 为待定常向量；

(2) 在使 $u^{*}(t)$ 连续的所有时刻 $t \in [t_{0}, t_{f}]$ , 有

$$\frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t) , t)}{\partial u} = 0,\frac {\partial^ {2} H \left(x ^ {*} (t) , u ^ {*} (t) , \psi (t) , t\right)}{\partial u ^ {2}} \leqslant 0;$$

(3) 当 $t_f$ 自由时，对使 $u^*(t)$ 连续的所有时刻 $t \in [t_0, t_f]$ ，有

$$H \left(x ^ {*} (t), u ^ {*} (t), \psi (t), t\right) = H \left(x ^ {*} \left(t _ {f}\right), u ^ {*} \left(t _ {f}\right), \psi \left(t _ {f}\right), t _ {f}\right),+ \int_ {t _ {f}} ^ {t} \frac {\partial H (x ^ {*} (\tau) , u ^ {*} (\tau) , \psi (\tau) , \tau)}{\partial t} d \tau ,H (x ^ {*} (t _ {f}), u ^ {*} (t _ {f}), \psi (t _ {f}), t _ {f}) = \frac {\partial k (x ^ {*} (t _ {f} ^ {*}) , t _ {f})}{\partial t _ {f}} + \mu^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f}) , t _ {f})}{\partial t _ {f}};$$

而当 $t_f$ 固定时，则有

$$H (x ^ {*} (t), u ^ {*} (t), \psi (t), t) = H (x ^ {*} (t _ {f}), u ^ {*} (t _ {f}), \psi (t _ {f}), t _ {f})+ \int_ {t _ {f}} ^ {t} \frac {\partial H (x ^ {*} (\tau) , u ^ {*} (\tau) , \psi (\tau) , \tau)}{\partial t} d \tau .$$
