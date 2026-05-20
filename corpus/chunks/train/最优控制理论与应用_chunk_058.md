# 3.5 习题

1. $\min_{y} J(y) = \int_{0}^{2} \left[ \frac{1}{2} y'^{2} + yy' + y' + y \right] \mathrm{d}x$ ，若 $y(0)$ 与 $y(2)$ 任意，求 $y^{*}$ 及 $J(y^{*})$ 。

2. 电枢控制的直流电动机忽略阻尼时的运动方程为

$$\ddot {\theta} = u (t)$$

式中， $\theta$ 为转轴的角位移， $u(t)$ 为输入。

目标函数为

$$\min _ {u} J = \frac {1}{2} \int_ {0} ^ {2} (\ddot {\theta}) ^ {2} \mathrm{d} t$$

使初态 $\theta(0) = 1$ 及 $\dot{\theta}(0) = 1$ 转移到终态 $\theta(2) = 0$ 及 $\dot{\theta}(2) = 0$ ，求最优控制 $u^{*}(t)$ 及最优角位移 $\theta^{*}(t)$ ，最优角速度 $\dot{\theta}^{*}(t)$ 。

3. $\min_{u} J = \frac{s^{2}}{2} x^{2}(2) + \frac{1}{2} \int_{0}^{2} u^{2}(t) \, \mathrm{d}t$

$$s. t, \quad {\dot {x}} = u (t), x (0) = 1. \qquad (s \text {为常量})$$

试求出最优控制 $u^{*}(t)$ 及相应的轨线 $x^{*}(t)$ 。

4. 系统由三个串联积分环节组成

$\left\{ \begin{array}{l} \dot{x}_{1} = x_{2} \\ \dot{x}_{2} = x_{3} \\ \dot{x}_{3} = u \end{array} \right.$ 初态 $\left\{ \begin{array}{l} x_{1}(0) = 0 \\ x_{2}(0) = 0 \\ x_{3}(0) = 0 \end{array} \right.$ 该系统由初态转到终端约束函数

$x_{1}^{2}(1) + x_{2}^{2}(1) = 1$ ，目标函数 $\min_{u}J = \frac{1}{2}\int_0^1 u^2 (t)\mathrm{d}t$ ，求最优解。

5. 系统为 $\dot{x} = -x + u, x(0) = 10$ 转移到 $x(1) = 0$ ，目标函数为 $\min_{u} J = \frac{1}{2} \int_{0}^{1} u^{2}(t) \mathrm{d}t$ ，求最优控制 $u^{*}(t)$ 和最优轨迹 $x^{*}(t)$ 。  
6. 系统为 $\dot{x} = -x^3 + u, x(0) = 1$ ，目标为 $\min_{u} J = \frac{1}{2} \int_{0}^{1} (x^2 + u^2) \mathrm{d}t$ ，试列出两点边值问题。  
7. 系统为 $\dot{x} = -x + u, x(0) = 1$ ，目标为 $\min_{u} J = \int_{0}^{1} (x^2 + u^2) \, \mathrm{d}t$ ，求最优解 $u^*(t)$ 及 $x^*(t)$ 。
