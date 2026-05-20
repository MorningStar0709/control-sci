\boldsymbol {x} (3) = \boldsymbol {G x} (2) + \boldsymbol {h u} (2) = \left[ \begin{array}{l} 2 \\ 1 2 \\ 4 \end{array} \right] + \left[ \begin{array}{l} 1 \\ - 2 \\ - 3 \end{array} \right] \boldsymbol {u} (0) + \left[ \begin{array}{l} 1 \\ - 2 \\ - 1 \end{array} \right] \boldsymbol {u} (1) + \left[ \begin{array}{l} 1 \\ 0 \\ 1 \end{array} \right] \boldsymbol {u} (2)
$$

令 $x(3) = 0$ ，则有

$$
\left[ \begin{array}{c c c} 1 & 1 & 1 \\ - 2 & - 2 & 0 \\ - 3 & - 1 & 1 \end{array} \right] \left[ \begin{array}{l} u (0) \\ u (1) \\ u (2) \end{array} \right] = \left[ \begin{array}{l} - 2 \\ - 1 2 \\ - 4 \end{array} \right]
$$

其系数矩阵即可控性矩阵 $S_{1}$ ，是非奇异的，因而可得

$$
\left[ \begin{array}{l} u (0) \\ u (1) \\ u (2) \end{array} \right] = \left[ \begin{array}{c c c} 1 & 1 & 1 \\ - 2 & - 2 & 0 \\ - 3 & - 1 & 1 \end{array} \right] ^ {- 1} \left[ \begin{array}{l} - 2 \\ - 1 2 \\ - 4 \end{array} \right] = \left[ \begin{array}{c c c} \frac {1}{2} & \frac {1}{2} & - \frac {1}{2} \\ - \frac {1}{2} & - 1 & \frac {1}{2} \\ 1 & \frac {1}{2} & 0 \end{array} \right] \left[ \begin{array}{l} - 2 \\ - 1 2 \\ - 4 \end{array} \right] = \left[ \begin{array}{l} - 5 \\ 1 1 \\ - 8 \end{array} \right]
$$

若令 $x(2) = 0$ ，即解方程组

$$
\left[ \begin{array}{l l} 1 & 1 \\ - 2 & 0 \\ - 1 & 1 \end{array} \right] \left[ \begin{array}{l} u (0) \\ u (1) \end{array} \right] = \left[ \begin{array}{l} - 2 \\ - 6 \\ 0 \end{array} \right]
$$

容易看出其系数矩阵的秩为 2, 但增广矩阵

$$
\left[ \begin{array}{c c c} 1 & 1 & - 2 \\ - 2 & 0 & - 6 \\ - 1 & 1 & 0 \end{array} \right]
$$

的秩为 3, 两个秩不等, 方程组无解, 意味着不能在两个采样周期内使系统由初始状态转移至原点。若该两个秩相等, 则可用两步完成状态转移。
