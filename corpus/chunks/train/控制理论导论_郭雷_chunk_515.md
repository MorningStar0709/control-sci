$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \frac {\partial J}{\partial x} f \left(x, u \left(x, \frac {\partial J}{\partial x}\right)\right) + l \left(x, u \left(x, \frac {\partial J}{\partial x}\right)\right) = 0, \\ J (x (t _ {f}), t _ {f}) = 0. \end{array} \right.
$$

存在定义在 $\mathbb{R}^n\times [t_0,t_f]$ (或 $\Omega_{n}\times [t_{0},t_{f}]$ ) 上的 $C^1$ 且具混合导数连续的函数 $J(x,t)$ , 仅当 $x = 0$ 时 $J(x,t) = 0$ , 且和 $u(x,t)\stackrel {\mathrm{def}}{=}u\left(x,\frac{\partial J(x,t)}{\partial x}\right),\forall (x,t)\in \mathbb{R}^n\times [t_0,t_f]$ 同时满足

$$
\left\{ \begin{array}{l} \frac {\partial J (x , t)}{\partial t} + \frac {\partial J (x , t)}{\partial x} f (x, u (x, t)) + l (x, u (x, t)) = 0, \\ J (x \left(t _ {f}\right), t _ {f}) = 0. \end{array} \right. \tag {7.1.75}
$$

$(J(x,t),u(x,t))$ 称为方程 (7.1.74) 在 $\mathbb{R}^n\times [t_0,t_f]$ 上的古典 $C^1$ 非零解.

假设方程(7.1.74)存在定义在 $\mathbb{R}^n\times [t_0,t_f^* ]$ 上的古典 $C^1$ 非零解 $(J^{*}(x,t),u^{*}(x,t))$

下面证明 $u^{*}(x,t)$ 是最优控制问题 (7.1.52), (7.1.53) 和 (7.1.54) 的综合函数, $J^{*}(x,t)$ 是相应的最优性能指标值.

事实上，由假设知， $\forall v\in \mathbb{U}_r$ ，当 $\forall (x,t)\in \mathbb{R}^n\times [t_0,t_f]$ 时，成立

$$\frac {\partial J ^ {*} (x , t)}{\partial t} + \frac {\partial J ^ {*} (x , t)}{\partial x} f (x, v) + l (x, v)\geqslant \frac {\partial J ^ {*} (x , t)}{\partial t} + \frac {\partial J ^ {*} (x , t)}{\partial x} f (x, u ^ {*} (t)) + l (x, u ^ {*} (t)) = 0. \tag {7.1.76}$$

将 $u^{*}(x,t)$ 代入式(7.1.52)得到闭环系统

$$\dot {x} = f (x, u ^ {*} (x, t)). \tag {7.1.77}$$

注意到 $\forall x_0 \in \mathbb{R}^n$ , 式 (7.1.77) 的 $t_0$ 时刻初值为 $x_0$ 的轨线 $x^*(t)$ 存在且唯一, 其定义区间记为 $[t_0, t_f^*]$ . (当方程 (7.1.74) 中 $t_f$ 固定时, $t_f^* = t_f$ ).

记

$$u ^ {*} (t) = u ^ {*} \left(x ^ {*} (t), t\right). \tag {7.1.78}$$

于是在 $[t_0, t_f^*]$ 上 $x^*(t), u^*(t)$ 满足

$$\dot {x} ^ {*} (t) = f \left(x ^ {*} (t), u ^ {*} (t)\right), \quad x ^ {*} \left(t _ {0}\right) = x _ {0}. \tag {7.1.79}$$

从方程 (7.1.75) 得到

$$
\left\{ \begin{array}{l} \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u ^ {*} (t)) + l (x ^ {*} (t), u ^ {*} (t)) = 0, \\ J ^ {*} (x ^ {*} (t _ {f}), t _ {f}) = 0. \end{array} \right. \tag {7.1.80}
$$

依 $J^{*}(t,x)$ 的“非零性”有

$$x ^ {*} (t _ {f} ^ {*}) = 0.$$

该式表明， $U_{[t_{0},t_{f}]} \neq \varnothing$ . 从 $t_{0}$ 到 $t_{f}^{*}$ 积分方程 (7.1.80) 第一式并利用第二式即得

$$J ^ {*} (x _ {0}, t _ {0}) = \int_ {t _ {0}} ^ {t _ {f}} l (x ^ {*} (t), u ^ {*} (t)) \mathrm{d} t. \tag {7.1.81}$$
