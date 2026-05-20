$$
\Phi (t) = \left[ \begin{array}{l l} \Phi_ {1 1} (t, t _ {0}) & \Phi_ {1 2} (t, t _ {0}) \\ \Phi_ {2 1} (t, t _ {0}) & \Phi_ {2 2} (t, t _ {0}) \end{array} \right]
$$

试证明：当 $A_{21} = 0$ 时必有 $\Phi_{21}(t,t_0)\equiv 0$ 。

2.10 给定二维线性定常系统

$$\dot {x} = A x, \quad t \geqslant 0$$

现知对应于两个不同初态时的状态响应为：

$$
\pmb {x} (0) = \left[ \begin{array}{c} 1 \\ - 4 \end{array} \right] \text {时} \pmb {x} (t) = \left[ \begin{array}{c} e ^ {- 3 t} \\ - 4 e ^ {- 3 t} \end{array} \right]

\pmb {x} (0) = \left[ \begin{array}{c c} & 2 \\ - & 1 \end{array} \right] \text {时} \pmb {x} (t) = \left[ \begin{array}{c c} 2 e ^ {- 2 t} \\ - e ^ {- 2 t} \end{array} \right]
$$

试据此定出系统的矩阵 A。

2.11 设 A 为方常阵且其特征值两两相异, trA 表示 A 的迹, 证明必成立:

$$\det \left(e ^ {A t}\right) = e ^ {(\operatorname{tr} A) t}$$

2.12 试求下列连续时间状态方程的离散化状态方程:

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u
$$

其中采样周期取为 T = 2。

2.13 给定人口流动的状态方程如下:

$$
\left[ \begin{array}{l} x _ {1} (k + 1) \\ x _ {2} (k + 1) \end{array} \right] = \left[ \begin{array}{c c} 1. 0 1 (1 - 0. 0 4) & 1. 0 1 (0. 0 2) \\ 1. 0 1 (0. 0 4) & 1. 0 1 (1 - 0. 0 2) \end{array} \right] \left[ \begin{array}{l} x _ {1} (k) \\ x _ {2} (k) \end{array} \right]
x _ {1} (0) = 1 0 ^ {7}, \quad x _ {2} (0) = 9 \times 1 0 ^ {7}
$$

其中， $x_{1}$ 表示城市人口， $x_{2}$ 表示乡村人口，令 k=0 表示 1988 年，应用计算机分析 1988—2010 年城市和乡村人口的分布态势，并绘出相应的分布曲线。

2.14 给定离散系统如下:

$$
\left[ \begin{array}{l} x _ {1} (k + 1) \\ x _ {2} (k + 1) \end{array} \right] = \left[ \begin{array}{l l} 1 & 2 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} (k) \\ x _ {2} (k) \end{array} \right] + \left[ \begin{array}{l} 1 \\ 2 \end{array} \right] u (k), \quad \left[ \begin{array}{l} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] = \left[ \begin{array}{l} 1 \\ 1 \end{array} \right]
$$

再取控制 $u(k)$ 为

$$
u (k) = \left\{ \begin{array}{l l} 1, & \text {当} k = 0, 2, 4, \dots \\ 0, & \text {当} k = 1, 3, 5, \dots \end{array} \right.
$$

计算 $x_{1}(k)$ 和 $x_{2}(k)$ 当 $k=1,2,\cdots,10$ 时的值(利用计算机进行计算)。

2.15 对于上题的离散系统, 计算 k = 10 时的状态转移矩阵 $\Phi(k)$ 。
