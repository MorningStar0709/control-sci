令 $S_{0}=\left[\begin{array}{ccc}CB & CAB & \cdots & CA^{n-1}B & D\end{array}\right]$ (9-122)

$S_{0}$ 为 $q \times (n + 1)p$ 矩阵，称为输出可控性矩阵。输出可控的充分必要条件是，输出可控性矩阵的秩等于输出向量的维数 $q$ ，即

$$\operatorname{rank} \mathbf {S} _ {0} = q \tag {9-123}$$

需要注意的是,状态可控性与输出可控性是两个不同的概念,二者没有什么必然的联系。

例 9-14 已知系统的状态方程和输出方程为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c} 1 \\ - 1 \end{array} \right] u

y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] x
$$

试判断系统的状态可控性和输出可控性。

解 系统的状态可控性矩阵为

$$
\boldsymbol {S} = \left[ \begin{array}{l l} \boldsymbol {b} & \boldsymbol {A b} \end{array} \right] = \left[ \begin{array}{c c} 1 & - 1 \\ - 1 & 1 \end{array} \right]
$$

$|S|=0,\operatorname{rank}S<2$ ，故状态不完全可控。

输出可控性矩阵为

$$
\boldsymbol {S} _ {0} = \left[ \begin{array}{l l l} \boldsymbol {c b} & \boldsymbol {c A b} & d \end{array} \right] = \left[ \begin{array}{l l l} 1 & - 1 & 0 \end{array} \right]
$$

$\mathrm{rank}S_0 = 1 = q$ ，故输出可控。
