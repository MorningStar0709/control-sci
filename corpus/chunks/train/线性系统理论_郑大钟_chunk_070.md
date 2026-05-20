方法4：对给定 $n \times n$ 常阵 $A$ ，先求出预解矩阵 $(sI - A)^{-1}$ ，则就有

$$e ^ {A t} = \mathscr {L} ^ {- 1} (s I - A) ^ {- 1} \tag {2.43}$$

对 $e^{A}$ 的定义关系式(2.31)取拉普拉斯变换可得

$$\mathscr {L} [ e ^ {A t} ] = \frac {I}{s} + \frac {A}{s ^ {2}} + \frac {A ^ {2}}{s ^ {3}} + \dots = (s I - A) ^ {- 1} \tag {2.44}$$

于是，对上式等式两边求拉普拉斯反变换，就可证得(2.43)。

例 给定线性定常系统的自治方程为

$$
\dot {x} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] x
$$

现采用上述四种方法来定出其矩阵指数函数 $e^{A t}$ 。

方法1:

$$
\begin{array}{l} e ^ {A t} = I + A t + \frac {1}{2 !} A ^ {2} t ^ {2} + \dots \\ = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] + \left[ \begin{array}{c c} 0 & t \\ - 2 t & - 3 t \end{array} \right] + \left[ \begin{array}{c c} - t ^ {2} & - \frac {3}{2} t ^ {2} \\ 3 t ^ {2} & \frac {7}{2} t ^ {2} \end{array} \right] + \dots \\ = \left[ \begin{array}{c c} 1 - t ^ {2} + \dots & t - \frac {3}{2} t ^ {2} + \dots \\ - 2 t + 3 t ^ {2} + \dots & 1 - 3 t + \frac {7}{2} t ^ {2} + \dots \end{array} \right] \\ \end{array}
$$

方法2:

先求出 $A$ 的特征值 $\lambda_{1} = -1$ 和 $\lambda_{2} = -2$ ，再求出使 $A$ 实现对角线化的变换阵 $P$ 和其逆 $P^{-1}$ 为：

$$
P = \left[ \begin{array}{c c} 1 & 1 \\ - 1 & - 2 \end{array} \right], P ^ {- 1} = \left[ \begin{array}{c c} 2 & 1 \\ - 1 & - 1 \end{array} \right]
$$

则矩阵指数函数 $e^{As}$ 可定出为：

$$
\begin{array}{l} e ^ {A t} = P \left[ \begin{array}{c c} e ^ {\lambda_ {1} t} & 0 \\ 0 & e ^ {\lambda_ {2} t} \end{array} \right] P ^ {- 1} \\ = \left[ \begin{array}{l l} 1 & 1 \\ - 1 & - 2 \end{array} \right] \left[ \begin{array}{c c} e ^ {- t} & 0 \\ 0 & e ^ {- 2 t} \end{array} \right] \left[ \begin{array}{l l} 2 & 1 \\ - 1 & - 1 \end{array} \right] \\ = \left[ \begin{array}{c c} 2 e ^ {- t} - e ^ {- 2 t} & e ^ {- t} - e ^ {- 2 t} \\ - 2 e ^ {- t} + 2 e ^ {- 2 t} & - e ^ {- t} + 2 e ^ {- 2 t} \end{array} \right] \\ \end{array}
$$

方法 3:

先定出 $A$ 的特征值 $\lambda_{1} = -1$ 和 $\lambda_{2} = -2$ ，则有

$$
\begin{array}{l} \left[ \begin{array}{l} \alpha_ {0} (t) \\ \alpha_ {1} (t) \end{array} \right] = \left[ \begin{array}{c c} 1 & \lambda_ {1} \\ 1 & \lambda_ {2} \end{array} \right] ^ {- 1} \left[ \begin{array}{l} e ^ {\lambda_ {1} t} \\ e ^ {\lambda_ {2} t} \end{array} \right] = \left[ \begin{array}{c c} 1 & - 1 \\ 1 & - 2 \end{array} \right] ^ {- 1} \left[ \begin{array}{l} e ^ {- t} \\ e ^ {- 2 t} \end{array} \right] \\ = \left[ \begin{array}{l l} 2 & - 1 \\ 1 & - 1 \end{array} \right] \left[ \begin{array}{l} e ^ {- t} \\ e ^ {- 2 t} \end{array} \right] = \left[ \begin{array}{l} 2 e ^ {- t} - e ^ {- 2 t} \\ e ^ {- t} - e ^ {- 2 t} \end{array} \right] \\ \end{array}
$$

从而即可定出：
