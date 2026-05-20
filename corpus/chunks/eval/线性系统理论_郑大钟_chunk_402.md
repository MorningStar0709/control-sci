$$a _ {1} (s) = 9 s ^ {2} + 2 9 s + 5 5, \quad a _ {2} (s) = 5 0$$

并进而求出：

$$
\left[ \begin{array}{c c} a _ {1} (s) & a _ {2} (s) \\ - 1 & 0 \end{array} \right] = \left[ \begin{array}{c c} 9 s ^ {2} + 2 9 s + 5 5 & 5 0 \\ - 1 & 0 \end{array} \right]

D _ {h c} ^ {- 1} D _ {l c} \Psi (s) = \left[ \begin{array}{c c} 0 & 0 \\ - \frac {1}{2} s ^ {2} + \frac {1}{4} s + \frac {1}{4} & \frac {1}{4} \end{array} \right]
$$

于是，可导出方程：

$$
K _ {1} \left[ \begin{array}{l} s ^ {2} \\ s \\ 1 \end{array} \right] = \left[ \begin{array}{l} \beta_ {1 1} s ^ {2} + \beta_ {1 2} s + \beta_ {1 3} \\ \beta_ {2 1} s ^ {2} + \beta_ {2 2} s + \beta_ {2 3} \end{array} \right] = \left[ \begin{array}{c} 9 s ^ {2} + 2 9 s + 5 5 \\ - 1 \end{array} \right]

- \left[ \begin{array}{c} 0 \\ - \frac {1}{2} s ^ {2} + \frac {1}{4} s + \frac {1}{4} \end{array} \right] = \left[ \begin{array}{l} 9 s ^ {2} + 2 9 s + 5 5 \\ \frac {1}{2} s ^ {2} - \frac {1}{4} s - \frac {5}{4} \end{array} \right]

K _ {2} \cdot 1 = \left[ \begin{array}{l} \beta_ {1 4} \\ \beta_ {2 4} \end{array} \right] = \left[ \begin{array}{l} 5 0 \\ 0 \end{array} \right] - \left[ \begin{array}{l} 0 \\ \frac {1}{4} \end{array} \right] = \left[ \begin{array}{l} 5 0 \\ - \frac {1}{4} \end{array} \right]
$$

由此，采用系数比较法就可求出：

$$
K _ {1} = \left[ \begin{array}{c c c} 9 & 2 9 & 5 5 \\ \frac {1}{2} & - \frac {1}{4} & - \frac {5}{4} \end{array} \right], \quad K _ {2} = \left[ \begin{array}{c} 5 0 \\ - \frac {1}{4} \end{array} \right]
$$

从而，求得状态反馈矩阵为

$$
K = \left[ K _ {1}, K _ {2} \right] = \left[ \begin{array}{c c c c} 9 & 2 9 & 5 5 & 5 0 \\ \frac {1}{2} & - \frac {1}{4} & - \frac {5}{4} & - \frac {1}{4} \end{array} \right]
$$

而输入变换阵则为

$$
H = D _ {b c} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 4 \end{array} \right]
$$

至此，就完成了此极点配置问题的综合过程，并且状态反馈系统的传递函数矩阵为：

$$G _ {H} (s, K) = N (s) D _ {K H} ^ {- 1} (s)$$

其中

$$
N (s) = \left[ \begin{array}{c c} s ^ {2} + s & 0 \\ 2 s + 1 & - 1 \end{array} \right]

\begin{array}{l} D _ {K H} (s) = S (s) + \left(D _ {k c} ^ {- 1} D _ {l c} + K\right) \Psi (s) = S (s) + \left[ \begin{array}{c c} a _ {1} (s) & a _ {2} (s) \\ - 1 & 0 \end{array} \right] \\ = \left[ \begin{array}{c c} s ^ {3} & 0 \\ 0 & s \end{array} \right] + \left[ \begin{array}{c c} 9 s ^ {2} + 2 9 s + 5 5 & 5 0 \\ - 1 & 0 \end{array} \right] \\ = \left[ \begin{array}{c c} s ^ {3} + 9 s ^ {2} + 2 9 s + 5 5 & 5 0 \\ - 1 & s \end{array} \right] \\ \end{array}
$$

特征值一特征向量配置问题 对于给定的开环系统的传递函数矩阵

$$G _ {o} (s) = N (s) D ^ {- 1} (s),$$

确定一个状态反馈阵K和一个输入变换阵H，使得所导出的状态反馈系统同时满足事先指定的期望特征值组和期望特征向量组，这样的问题称为特征值一特征向量配置问题。下面，我们来给出有关这一问题的一个基本结论。
