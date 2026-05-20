# 9.5 习题

1. 对于系统 $\left[ \begin{array}{c} \dot{x}_1 \\ \dot{x}_2 \end{array} \right] = \left[ \begin{array}{cc} 0 & 1 \\ 0 & 0 \end{array} \right]\left[ \begin{array}{c} x_1 \\ x_2 \end{array} \right] + \left[ \begin{array}{c} 1 \\ -1 \end{array} \right] u$ ，求控制使性能指标 $J = \int_{t_0}^{t_f} x_1^2 \mathrm{d}t$ 最小，且适合约束 $|u| \leqslant 1$ ，并证明相应的可控性和可观测性条件得到满足。

2. 对于系统 $\begin{bmatrix}\dot{x}_{1}\\ \dot{x}_{2}\\ \dot{x}_{3}\end{bmatrix}=\begin{bmatrix}0&1&0\\ 0&0&1\\ 0&0&0\end{bmatrix}\begin{bmatrix}x_{1}\\ x_{2}\\ x_{3}\end{bmatrix}+\begin{bmatrix}0\\ 0\\ 1\end{bmatrix}u$ ，求控制使性能指标

$J = \int_{t_0}^{t_f}(x_1^2 + x_2^2 + x_3^2)\mathrm{d}t$ 最小，且适合约束 $\left|u\right|\leqslant 1$ 。

3. 已知二阶受控系统 $\dot{x}_1(t) = x_2(t), \dot{x}_2(t) = u(t)$ ，试求系统由已知初态 $x_1(0) = 0, x_2(0) = 1$ ，且使性能指标 $J = \frac{1}{2} \int_{0}^{\frac{3}{2}\pi} [-x_1^2(t) + x_2^2(t)] \mathrm{d}t$ 为极小的最优控制，并判断奇异弧段是否是最优的，并给出奇异弧段是非最优解时的条件。
