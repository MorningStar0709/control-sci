# 5.9 习题

1. 已知二阶系统的状态方程

$$
\left\{ \begin{array}{l l} \dot {x} _ {1} (t) & = x _ {2} (t) \\ \dot {x} _ {2} (t) & = u (t) \end{array} \right.
$$

性能泛函

$$J = \frac {1}{2} \left[ x _ {1} ^ {2} (3) + 2 x _ {2} ^ {2} (3) \right] + \frac {1}{2} \int_ {0} ^ {3} \left[ 2 x _ {1} ^ {2} (t) + \right.\left. 4 x _ {2} ^ {2} (t) + 2 x _ {1} (t) x _ {2} (t) + \frac {1}{2} u ^ {2} (t) \right] d t$$

求最优控制。

2. 能控的系统其状态方程为

$$
\left\{ \begin{array}{l l} \dot {x} _ {1} (t) & = x _ {2} (t) \\ \dot {x} _ {2} (t) & = u (t) \end{array} \right.
$$

这是一种双积分系统,其输出为 $x_{1}(t)$ , 其输入为 $u(t)$ , 其传递函数为

$$\frac {x _ {1} (s)}{u (s)} = \boldsymbol {G} (s) = \frac {1}{s ^ {2}}$$

其性能泛函为

$$J = \frac {1}{2} \int_ {0} ^ {\infty} \left[ x _ {1} ^ {2} (t) + 2 b x _ {1} (t) x _ {2} (t) + a x _ {2} ^ {2} (t) + u ^ {2} (t) \right] d t$$

其中 $a^2 - b^2 > 0$

求最优控制。

3. $\min J = \int_{0}^{\infty}\left(x_{2}^{2} + 0.1u^{2}\right)\mathrm{d}t$

$$\dot {x} _ {1} = - x _ {1} + u\dot {x} _ {2} = x _ {1}$$

求最优控制。

4. 线性系统的状态方程

$$\dot {x} (t) = - u (t), \quad x (0) = 1$$

性能泛函 $J = \int_{0}^{\infty}\left(x^{2}(t) + u^{2}(t)\right)\mathrm{d}t$

试求最优控制函数。

5. min $J = \sum_{k=0}^{2} (x_k^2 + u_k^2)$

$$x _ {k + 1} = x _ {k} + u _ {k}$$

试求最优控制函数。

6. 给定一阶系统 $\dot{x}(t) = u(t), x(1) = 3$ ，性能泛函

$$J = x ^ {2} (5) + \frac {1}{2} \int_ {0} ^ {5} u ^ {2} (t) d t$$

试求最优控制 $u^{*}$ ，使 J 取极小值。

7. 对一维线性系统

$$x (k + 1) = x (k) + 2 u (k), \quad k = 0, 1, \dots , N - 1.J = x ^ {2} (N) + 4 \beta \sum_ {k = 0} ^ {N - 1} u ^ {2} (k), (\beta \text {为正常数})$$

求使 J 取最小值的最优控制。

$$8. \min _ {u (k)} J = \frac {1}{2} \sum_ {0} ^ {9} u ^ {2} (k), s. t. x (k + 1) = x (k) + \alpha u (k), x (0) = 1,x (1 0) = 0$$

求最优控制 $u^{*}(k)$ 和最优轨迹 $x^{*}(k)$ 。

9. 上机作业：

a. 已知系统：

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & - \frac {1}{\tau} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ \frac {1}{\tau} \end{array} \right] u,
$$

其中： $\tau = 2$ 。设计控制系统使得目标函数

$$
J (x (t), u (t)) = \frac {1}{2} \int_ {0} ^ {\infty} \left\{\left[ h (t) \dot {h} (t) \ddot {h} (t) \right] \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} h (t) \\ \dot {h} (t) \\ \ddot {h} (t) \end{array} \right] + 2 u ^ {2} (t) \right\} d t
$$

最小。

(1) 求状态反馈增益阵。

（2）当系统的初始状态为 $x(0)=[10\quad0\quad0]^{T}$ 时，进行闭环仿真。画出控制变量和状态变量的变化曲线。

(3) 画出 Nyquist 曲线和找出稳定裕度.

(4) 当 Q 和 R 变化时, 即
