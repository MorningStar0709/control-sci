# Hamilton-Jacobi-Issacs 方程的解

HJI 方程 (7.4.42) 的古典意义下解的含义为

(1) 存在满足 (7.4.42) 的 $C^1$ (或分片 $C^1$ ) 向量值函数对 $\left(u\left(x, \frac{\partial J}{\partial x}\right), v\left(x, \frac{\partial J}{\partial x}\right)\right)$ , 满足

$$
\begin{array}{l} \frac {\partial J}{\partial t} + \min _ {\bar {u} \in \mathrm{U} _ {r _ {1}}} \max _ {\bar {v} \in \mathbf {V} _ {r _ {2}}} \left\{\frac {\partial J}{\partial x} f (x, u, \bar {v}) + l (x, \bar {u}, \dot {v}) \right\} \\ = \frac {\partial J}{\partial t} + \frac {\partial J}{\partial x} f (x, u (x, \frac {\partial J}{\partial x}), v (x, \frac {\partial J}{\partial x})) + l (x, u (x, \frac {\partial J}{\partial x}), v (x, \frac {\partial J}{\partial x})) = 0; \\ \end{array}
$$

(2) 偏微分方程边值问题

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \frac {\partial J}{\partial x} f (x, u (x, \frac {\partial J}{\partial x}), v (x, \frac {\partial J}{\partial x})) + l (x, u (x, \frac {\partial J}{\partial x}), v (x, \frac {\partial J}{\partial x})) = 0, \\ J (x (t _ {f}), t _ {f}) = 0, \end{array} \right. \tag {7.4.43}
$$

存在古典解，即存在定义在 $\mathbb{R}^n\times [0,t_f]$ 上的 $C^1$ 且其混合导数连续的标量函数 $J(x,t)$ ，满足

$$
\left\{ \begin{array}{l} \frac {\partial J (x , t)}{\partial t} + \frac {\partial J (x , t)}{\partial x} f (x, u (x, t), v (x, t)) + l (x, u (x, t), v (x, t)) = 0, \\ J (x \left(t _ {f}\right), t _ {f}) = 0, \end{array} \right. \tag {7.4.44}
$$

$\forall (x,t)\in \mathbb{R}^n\times [0,t_f]$ ，其中 $u(x,t)\stackrel {\mathrm{def}}{=}\left(u\left(x,\frac{\partial J(x,t)}{\partial x}\right),v(x,t)\stackrel {\mathrm{def}}{=}v\left(x,\frac{\partial J(x,t)}{\partial x}\right). \right.$ （ $J(x,t),u(x,t),v(x,t))$ 简称为HJI方程的古典解.

设 HJI 方程 (7.4.42) 在 $\mathbb{R}^n \times [0, t_f]$ 上存在古典解 $(J^*(x, t), u^*(x, t), v^*(x, t))$ . 下面证明， $(u^*(x, t), v^*(x, t))$ 是对策问题 (7.4.8)\~(7.4.11) 的反馈形式的最优策略， $J^*(x, t)$ 是相应的最优对策值.

事实上，由假设知， $\forall (u,v)\in \mathbb{U}_{r_1}\times \mathbb{V}_{r_2}$ ，当 $(x,t)\in \mathbb{R}^n\times [0,t_f]$ 时，有
