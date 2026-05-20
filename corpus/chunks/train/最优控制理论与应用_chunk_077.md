# 4.7 习题

1. min $J = t_{\mathrm{f}}$

$$\dot {x} _ {1} = x _ {2}, x _ {1} (0) = 1, x _ {2} (0) = 1,\dot {x} _ {2} = u, x _ {1} (t _ {\mathrm{f}}) = 0, x _ {2} (t _ {\mathrm{f}}) = 0,\mid u \mid \leqslant 1$$

求最优控制。

2. $\min_{u} J = \int_{0}^{t_{\mathrm{f}}} \mathrm{d}t$

s. t., $\dot{x}_1(t) = -x_1(t) + u$

$$\dot {x} _ {2} (t) = u$$

且有 $\left\{ \begin{array}{l} x_{1}(0) = x_{10} \\ x_{2}(0) = x_{20} \end{array} \right.$ $\left\{ \begin{array}{l} x_{1}(t_{\mathrm{f}}) = 0 \\ x_{2}(t_{\mathrm{f}}) = 0 \end{array} \right.\quad |u| \leqslant 1$ ，求最优控制。

3. $\min_{u} J = \int_{0}^{t_{\mathrm{f}}} \mathrm{d}t$

$$s. t., \dot {x} _ {1} = - x _ {2} \quad \dot {x} _ {2} = - \widetilde {\omega_ {0} ^ {2}} x _ {1} - 2 \xi \widetilde {\omega_ {0}} x _ {2} + u$$

且有 $\left\{ \begin{array}{l} x_{1}(0) = x_{10} \\ x_{2}(0) = x_{20} \end{array} \right.$ $\left\{ \begin{array}{l} x_{1}(t_{\mathrm{f}}) = 0 \\ x_{2}(t_{\mathrm{f}}) = 0 \end{array} \right.$ $|u| \leqslant 1$ ，求最优控制。

4. 存在恢复力时,求无阻尼运动的最小时间控制。如果忽略阻尼,

考虑恢复力,则无阻尼运动方程为

$$\ddot {y} + y = u$$

若令 $y = x_{1},\dot{x}_{1} = x_{2}$

则无阻尼运动的状态方程为

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) \\ \dot {x} _ {2} (t) = - x _ {1} (t) + u (t), x \left(t _ {0}\right) = x _ {0} \\ \end{array}
$$

无阻尼运动的最小时间控制问题提法如下：

$$
\begin{array}{l} \min _ {u} J = \int_ {t _ {0}} ^ {t _ {f}} \mathrm{d} t \\ \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - x _ {1} + u, x (t _ {0}) = x _ {0} \\ \mid u \mid \leqslant 1 \\ \end{array}
$$

5. 系统的状态方程为

$$
\left\{ \begin{array}{l l} \dot {x} _ {1} (t) = x _ {2} (t) \\ \dot {x} _ {2} (t) = u (t) & | u | \leqslant 1 \end{array} \right.
$$

寻求时间最优控制函数,使系统由任意初始状态到达下列终端状态:

$$x _ {1} \left(t _ {\mathrm{f}}\right) = 2 \quad x _ {2} \left(t _ {\mathrm{f}}\right) = 1$$

求出开关曲线的方程,并绘出开关曲线的图形。

6. 设已知系统的状态方程为

$$
\left\{ \begin{array}{l l} \dot {x} _ {1} (t) & = x _ {2} (t) \\ \dot {x} _ {2} (t) & = u (t) \end{array} \right.
$$

约束条件 $|u|\leqslant 1$

寻求最优控制 $u^{*}(t)$ ，使系统由任意初始状态 $(\xi_{1},\xi_{2})$ 到达原点 $(0,0)$ ，并使性能指标

$$J (u) = \int_ {t _ {0}} ^ {t _ {f}} [ k + | u (t) | ] d t$$

最小。其中加权系数 $k > 0$ ，末端时间 $t_{\mathrm{f}}$ 是自由的。

7. 设有一阶系统

$$\dot {x} (t) = - x (t) + u (t), \quad x (0) = 2$$

其控制函数 $u(t)$ 受的约束条件是 $-1 \leqslant u(t) \leqslant 1$ 。

试确定控制函数 $u(t)$ ，使泛函

$$J = \int_ {0} ^ {1} [ 2 x (t) - u (t) ] d t$$

取极小值。
