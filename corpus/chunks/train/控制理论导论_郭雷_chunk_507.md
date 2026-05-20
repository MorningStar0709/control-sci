$$
\begin{array}{r} {\left\{ \begin{array}{l l} {\dot {x} ^ {*} (t) = \left[ \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t) , t)}{\partial \psi} \right] ^ {\mathrm{T}}, \qquad x ^ {*} (t _ {0}) = x _ {0},} \\ {\dot {\psi} ^ {\mathrm{T}} (t) = - \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t) , t)}{\partial x},} \\ {\psi^ {\mathrm{T}} (t _ {f}) = \left\{ \begin{array}{l l} {- \frac {\partial k (x ^ {*} (t _ {f}) , t _ {f})}{\partial x}, \qquad x (t _ {f}) \text {自由},} \\ {- \frac {\partial k (x ^ {*} (t _ {f}) , t _ {f})}{\partial x} - \mu^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f}) , t _ {f})}{\partial x},} \\ {\qquad \qquad \qquad \qquad \qquad \qquad x (t _ {f}) \text {受约束} g (x (t _ {f}), t _ {f}) = 0,} \end{array} \right.} \end{array} \right.} \end{array} \tag {1}
$$

$\mu \in \mathbb{R}^p$ 为待求常向量；

(2) $H(x^{*}(t),u^{*}(t),\psi (t),t) = \max_{u\in \mathbf{U}_{r}}H(x^{*}(t),u,\psi (t),t),\quad \forall t\in \Omega (t_0,t_f;u^*)$   
(3) 当 $t_f$ 自由时， $\forall t \in \Omega(t_0, t_f; u^*)$ ，有

$$H (x ^ {*} (t), u ^ {*} (t), \psi (t), t) = H (x ^ {*} (t _ {f}), u ^ {*} (t _ {f}), \psi (t _ {f}), t _ {f})+ \int_ {t _ {f}} ^ {t} \frac {\partial H (x ^ {*} (\tau) , u ^ {*} (\tau) , \psi (\tau) , \tau)}{\partial t} d \tau ,H (x ^ {*} (t _ {f}), u ^ {*} (t _ {f}), \psi (t _ {f}), t _ {f}) = \frac {\partial k (x ^ {*} (t _ {f}) , t _ {f})}{\partial t _ {f}} + \mu^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f}) , t _ {f})}{\partial t _ {f}};$$

而当 $t_f$ 固定时， $\forall t\in \Omega (t_0,t_f;u^*)$ ，有

$$
\begin{array}{l} H (x ^ {*} (t), u ^ {*} (t), \psi (t), t) = H (x ^ {*} (t _ {f}), u ^ {*} (t _ {f}), \psi (t _ {f}), t _ {f}) \\ + \int_ {t _ {f}} ^ {t} \frac {\partial H (x ^ {*} (\tau) , u ^ {*} (\tau) , \psi (\tau) , \tau)}{\partial t} d \tau . \\ \end{array}
$$

这里 $H(x,u,\psi ,t)\stackrel {\mathrm{def}}{=} - l(x,u,t) + \psi^{\mathrm{T}}(t)f(x,u,t)$ 为 (7.1.1), (7.1.3) 的Hamilton函数.

注7.1.1 当取定义在 $[t_0, t_f]$ 上的有界可测 $r$ 维向量值函数 $u(t)$ 为容许控制函数时，极大值原理亦成立 [1].

注7.1.2 当讨论系统(7.1.1)的性能指标(7.1.3)取极大的最优控制问题时，相应的必要条件叫做“极小值原理”，指最优控制函数使哈密顿函数达到极小.
