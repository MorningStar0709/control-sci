注意到 $J^{*}(x,t), u^{*}(x,t), x^{*}(t), u^{*}(t)$ 的意义，易知 $\forall u \in \mathbb{U}_r, t \in [t_0, t_f]$ 有

$$
\begin{array}{l} \frac {\partial J ^ {*} \left(x ^ {*} (t) , t\right)}{\partial t} + \frac {\partial J ^ {*} \left(x ^ {*} (t) , t\right)}{\partial x} \cdot f \left(x ^ {*} (t), u\right) + l \left(x ^ {*} (t), u\right) \\ \geqslant \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} \cdot f (x ^ {*} (t), u ^ {*} (t)) + l (x ^ {*} (t), u ^ {*} (t)) = 0, \\ \end{array}
$$

或 $\forall u\in \mathbb{U}_r,t\in [t_0,t_f]$ 有

$$
\begin{array}{l} \psi_ {n + 1} (t) + \psi^ {\mathrm{T}} (t) f \left(x ^ {*} (t), u\right) - l \left(x ^ {*} (t), u\right) \\ \leqslant \psi_ {n + 1} (t) + \psi^ {\mathrm{T}} (t) f (x ^ {*} (t), u ^ {*} (t)) - l (x ^ {*} (t), u ^ {*} (t)) = 0. \tag {7.1.73} \\ \end{array}
$$

记 $H(x,u,\psi) = -l(x,u) + \psi^{\mathrm{T}}f(x,u)$ , 由方程 (7.1.71), (7.1.72) 和式 (7.1.73) 知

$$H (x ^ {*} (t), u ^ {*} (t), \psi (t)) = \max _ {u \in \mathbf {U} _ {\tau}} H (x ^ {*} (t), u, \psi (t)), \quad \forall t \in [ t _ {0}, t _ {f} ^ {*} ],$$

且

$$
H (x ^ {*} (t), u ^ {*} (t), \psi (t)) = \left\{ \begin{array}{l l} {0,} & {\quad t _ {f} \text {自由时},} \\ {\text {常数},} & {\quad t _ {f} \text {固定时}.} \end{array} \right.
$$

综上所述得到如下结论：当带边值条件的Bellman方程(7.1.64)在 $\mathbb{R}^n\times [t_0,t_f]$ 上存在的古典意义下解 $(J^{*}(x,t),u^{*}(x,t))$ ，且闭环系统(7.1.67)存在满足 $x^{*}(t_{f}) = 0$ 的解 $x^{*}(t)$ 时，由式(7.1.68)确定的 $u^{*}(t)$ 和由方程(7.1.70)定义的 $\psi (t)$ 及 $x^{*}(t)$ 正好满足极大值原理中的必要条件.

最优控制的充分条件. 考察下列带边值条件的 Bellman 方程:

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \min _ {u \in \mathbb {U} _ {r}} \left\{\frac {\partial J}{\partial x} f (x, u) + l (x, u) \right\} = 0, \\ J (x (t _ {f}), t _ {f}) = 0. \end{array} \right. \tag {7.1.74}
$$

方程 (7.1.74) 的定义在 $[t_0, t_f] \times \mathbb{R}^n$ 上古典意义下 $C^1$ “非零解”是指：

(1) 存在 $C^1$ (分片 $C^1$ ) 向量值函数 $u\left(x, \frac{\partial J}{\partial x}\right)$ , 它满足

$$
\begin{array}{l} \frac {\partial J}{\partial t} + \min _ {v \in \mathbf {U} _ {r}} \left\{\frac {\partial J}{\partial x} f (x, v) + l (x, v) \right\} \\ = \frac {\partial J}{\partial t} + \frac {\partial J}{\partial x} f (x, u (x, \frac {\partial J}{\partial x})) + l (x, u (x, \frac {\partial J}{\partial x})) = 0; \\ \end{array}
$$

(2) 偏微分方程边值问题
