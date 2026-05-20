# 习题

2.1 对于下列给出的常阵 A，定出它们的矩阵指数函数 $e^{At}$ :

(i) $A = \begin{bmatrix} -2 & 0 \\ 0 & -3 \end{bmatrix}$

(ii) $A = \begin{bmatrix} -2 & 1 \\ 0 & -2 \end{bmatrix}$

(iii) $A=\begin{bmatrix}0&0\\ 1&0\end{bmatrix}$

(iv) $A = \begin{bmatrix} 0 & -1 \\ 4 & 0 \end{bmatrix}$

(v) $A = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}$

2.2 用三种方法计算下列矩阵 A 的矩阵指数函数 $e^{A t}$ :

(i) $A = \left[ \begin{array}{ll}0 & 1\\ -2 & -3 \end{array} \right]$

(ii) $A = \begin{bmatrix} 0 & 1 & 0\\ 0 & 0 & 1\\ -6 & -11 & -6 \end{bmatrix}$

2.3 试求下列各系统的状态变量解 $x_{1}(t)$ 和 $x_{2}(t)$ :

(i) $\begin{bmatrix}\dot{x}_{1}\\ \dot{x}_{2}\end{bmatrix}=\begin{bmatrix}0&1\\ -3&-2\end{bmatrix}\begin{bmatrix}x_{1}\\ x_{2}\end{bmatrix},\begin{bmatrix}x_{1}(0)\\ x_{2}(0)\end{bmatrix}=\begin{bmatrix}1\\ 1\end{bmatrix}$

(ii) $\left[ \begin{array}{c} x_{1} \\ x_{2} \end{array} \right] = \left[ \begin{array}{cc} 0 & 1 \\ -2 & -3 \end{array} \right]\left[ \begin{array}{c} x_{1} \\ x_{2} \end{array} \right] + \left[ \begin{array}{c} 2 \\ 0 \end{array} \right] u, \left[ \begin{array}{c} x_{1}(0) \\ x_{2}(0) \end{array} \right] = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]$

$$u (t) = e ^ {- t}, t \geqslant 0$$

2.4 对于给定的系统,已知

$$
\Phi (t) = \left[ \begin{array}{c c} e ^ {- t} & 0 \\ 0 & e ^ {- 2 t} \end{array} \right], b = \left[ \begin{array}{l} 1 \\ 1 \end{array} \right], x (0) = \left[ \begin{array}{l} 2 \\ 3 \end{array} \right]
$$

试定出相对于下列各个 $u(t)$ 时的状态响应 $x(t)$ :

(i) $u(t) = \delta(t)$ (单位脉冲函数)

(ii) $u(t) = 1(t)$ （单位阶跃函数）

(iii) $u(t) = t$

(iv) $u(t) = \sin t$

2.5 已知某系统的状态转移矩阵 $\Phi(t)$ 为:

$$
\Phi (t) = \left[ \begin{array}{l l} \frac {1}{2} \left(e ^ {- t} + e ^ {3 t}\right) & \frac {1}{4} \left(- e ^ {- t} + e ^ {3 t}\right) \\ - e ^ {- t} + e ^ {3 t} & \frac {1}{2} \left(e ^ {- t} + e ^ {3 t}\right) \end{array} \right]
$$

试定出其系统矩阵 A。

2.6 利用拉普拉斯变换证明：线性定常系统 $\dot{x} = Ax + Bu, x(0) = x_0$ 的状态运动的一般表达式为：

$$x (t) = e ^ {A t} x _ {0} + \int_ {0} ^ {t} e ^ {A (t - \tau)} B u (\tau) d \tau$$

2.7 给定矩阵微分方程为:

$$\dot {X} = A X + X A ^ {T}, \quad X (0) = P _ {0}$$

其中 $X$ 为 $n \times n$ 变量阵。试证明：此矩阵方程的解为：

$$X (t) = e ^ {A t} P _ {0} e ^ {A T t}$$

2.8 给定 $\dot{x} = A(t)x$ 和其伴随方程 $\dot{z} = -A^T (t)z$ ，表 $\Phi (t,t_0)$ 和 $\Phi_{s}(t,t_0)$ 分别为它们的状态转移矩阵，证明： $\Phi (t,t_0)\Phi_s^T (t,t_0) = I$ 。

2.9 给定线性时变系统

$$
\dot {x} = \left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] x + \left[ \begin{array}{l} B _ {1} \\ B _ {2} \end{array} \right] u, \quad t \geqslant t _ {0}
$$

设其状态转移矩阵为：
