$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \min _ {u \in \mathbb {U} _ {r}} \left\{\frac {\partial J}{\partial x} f (x, u) + l (x, u) \right\} = 0, \\ J (x (t _ {f}), t _ {f}) = k (x (t _ {f})). \end{array} \right.
$$

Bellman 方程与极大值原理. 考察带边值条件的 Bellman 方程

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \min _ {u \in U _ {r}} \left\{\frac {\partial J}{\partial x} f (x, u) + l (x, u) \right\} = 0, \\ J (0, t _ {f}) = 0. \end{array} \right. \tag {7.1.65}
$$

Bellman 方程 (7.1.65) 的古典意义下解的含义如下:

(1) 存在满足方程 (7.1.65) 的 $C^1$ (或分片 $C^1$ ) 向量值函数 $u\left(x, \frac{\partial J}{\partial x}\right)$ , 使得

$$
\begin{array}{l} \frac {\partial J}{\partial t} + \min _ {v \in \mathbf {U} _ {r}} \left\{\frac {\partial J}{\partial x} f (x, v) + l (x, v) \right\} \\ = \frac {\partial J}{\partial t} + \frac {\partial J}{\partial x} f (x, u (x, \frac {\partial J}{\partial x})) + l (x, u (x, \frac {\partial J}{\partial x})) = 0; \\ \end{array}
$$

(2) 偏微分方程边值问题

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \frac {\partial J}{\partial x} f (x, u (x, \frac {\partial J}{\partial x})) + l (x, u (x, \frac {\partial J}{\partial x})) = 0, \\ J (0, t _ {f}) = 0, \end{array} \right. \tag {7.1.66}
$$

存在古典解 $J(x,t)$ , 即 $J(x,t)$ 是 $\mathbb{R}^n \times [t_0, t_f]$ (或 $\Omega_n \times [t_0, t_f]$ , $\Omega_n$ 为含 $\mathbb{R}^n$ 中含原点的某开区域) 上的 $C^1$ 函数, 其混合导数连续, 并且满足方程 (7.1.66).

记 $u(x,t)\stackrel {\mathrm{def}}{=}u\left(x,\frac{\partial J(x,t)}{\partial x}\right)$ ，则 $(J(x,t),u(x,t))$ 称为带边值条件的Bellman方程(7.1.65)在 $\mathbb{R}^n\times [t_0,t_f^* ]$ 上的古典解.

假设方程 (7.1.65) 在 $\mathbb{R}^n \times [t_0, t_f^*]$ 上存在古典意义下解 $(J^*(x,t), u^*(x,t))$ 。将 $u^*(x,t)$ 代入系统 (7.1.1) 得到闭环系统

$$\dot {x} = f (x, u ^ {*} (x, t)). \tag {7.1.67}$$

如果式(7.1.67)的 $t_0$ 时刻初值为 $x_0$ 的解 $x^{*}(t)$ 在 $[t_0, t_f^*]$ 存在且满足 $x^{*}(t_{f}^{*}) = 0$ , 并记

$$u ^ {*} (t) \stackrel {\text { def }} {=} u ^ {*} (x ^ {*} (t), t) = u \left(x ^ {*} (t), \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x}\right), \tag {7.1.68}$$

则根据方程 (7.1.66), $\forall t \in [t_0, t_f^*)$ , 有

$$
\left\{ \begin{array}{l} \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t} + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u ^ {*} (t)) + l (x ^ {*} (t), u ^ {*} (t)) = 0, \\ J ^ {*} (0, t _ {f} ^ {*}) = 0. \end{array} \right. \tag {7.1.69}
$$

令
