# 例 7.4 状态变量形式的扬声器电路

试对图 2.30 所示的扬声器电路以及图 2.31 所示的驱动电路，找到输入电压 $v_{a}$ 到输出锥体位移 x 的状态空间方程。假设电路电阻是 R，电感是 L。

解答。回顾互相耦合的式(2.54)和式(2.58)所组成的扬声器动态模型：

$$
\begin{array}{l} M \ddot {x} + b \dot {x} = 0. 6 3 i \\ L \frac {\mathrm{d} i}{\mathrm{d} t} + R i = v _ {\mathrm{a}} - 0. 6 3 \dot {x} \\ \end{array}
$$

这个三阶系统的逻辑状态矢量将是 $X \stackrel{\mathrm{def}}{=} [x \dot{x} i]^{\mathrm{T}}$ ，由此得出标准矩阵分别为

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & - b / M & 0. 6 3 / M \\ 0 & - 0. 6 3 / L & - R / L \end{array} \right]
$$

439

440

$$
\begin{array}{l} \boldsymbol {B} = \left[ \begin{array}{c} 0 \\ 0 \\ 1 / L \end{array} \right] \\ \boldsymbol {C} = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \\ D = 0 \\ \end{array}
$$

此时，输入为 $u \stackrel{\operatorname{def}}{=} v_{a}$ 。
