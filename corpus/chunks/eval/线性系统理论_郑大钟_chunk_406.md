$$
\begin{array}{l} K = - D _ {h c} ^ {- 1} \left[ \mathbf {g} _ {1}, \mathbf {g} _ {2}, \mathbf {g} _ {3}, \mathbf {g} _ {4} \right] \left[ f _ {1}, f _ {2}, f _ {3}, f _ {4} \right] ^ {- 1} \\ = \left[ \begin{array}{c c} - 1 & 0 \\ 0 & - \frac {1}{4} \end{array} \right] \left[ \begin{array}{l l l l} - 1 6 & 1 1 - j 2 & 1 1 + j 2 & 0 \\ - 2 5 & 3 + j 1 8 & 3 - j 1 8 & - 1 9 \end{array} \right] \\ \end{array}

\left[ \begin{array}{c c c c} \frac {1}{1 0} & \frac {1}{5} & \frac {1}{2} & 0 \\ - \frac {1}{1 0} - j \frac {1}{2 0} & - \frac {1}{5} - j \frac {7}{2 0} & - j \frac {1}{2} & 0 \\ - \frac {1}{1 0} + j \frac {1}{2 0} & - \frac {1}{5} + j \frac {7}{2 0} & j \frac {1}{2} & 0 \\ \frac {1}{1 0} & \frac {1}{5} & - \frac {1}{2} & 1 \end{array} \right]

= \left[ \begin{array}{c c c c} 4 & 9 & 1 0 & 0 \\ \frac {4}{5} & - \frac {1 3}{2 0} & - \frac {1 5}{4} & \frac {1 9}{4} \end{array} \right]
$$

而输入变换阵为

$$
H = D _ {h c} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 4 \end{array} \right]
$$

并且，还可导出状态反馈系统的传递函数矩阵为：

$$G _ {H} (s, K) = N (s) D _ {K H} ^ {- 1} (s)$$

其中

$$
N (s) = \left[ \begin{array}{c c} s ^ {2} + s & 0 \\ 2 s + 1 & - 1 \end{array} \right]

D _ {K H} (s) = \left[ \begin{array}{c c} s ^ {3} + 4 s ^ {2} + 9 s + 1 0 & 0 \\ \frac {3}{1 0} s ^ {2} - \frac {2}{5} s - \frac {7}{2} & s + 5 \end{array} \right]
$$
