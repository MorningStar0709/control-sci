$$
\left[ \begin{array}{l} \dot {u} _ {c} \\ \dot {i} _ {L} \end{array} \right] = \left[ \begin{array}{c c} - \frac {1}{(R _ {1} + R _ {2}) C} & - \frac {R _ {1}}{(R _ {1} + R _ {2}) C} \\ \frac {R _ {1}}{L (R _ {1} + R _ {2})} & - \frac {R _ {1} R _ {2}}{L (R _ {1} + R _ {2})} \end{array} \right] \left[ \begin{array}{l} u _ {e} \\ i _ {L} \end{array} \right] + \left[ \begin{array}{c} \frac {1}{(R _ {1} + R _ {2}) C} \\ \frac {R _ {2}}{L (R _ {1} + R _ {2})} \end{array} \right] e (t)
$$

导出输出方程：根据电路关系式，有

$$u _ {R 2} = R _ {2} i _ {c} = R _ {2} C \frac {d u _ {c}}{d t} = \frac {- R _ {2}}{R _ {1} + R _ {2}} u _ {c} + \frac {- R _ {1} R _ {2}}{R _ {1} + R _ {2}} i _ {L} + \frac {R _ {2}}{R _ {1} + R _ {2}} e (t)$$

将其改写后即得到此电路的输出方程为：

$$
u _ {R 2} = \left[ - \frac {R _ {2}}{R _ {1} + R _ {2}} - \frac {R _ {1} R _ {2}}{R _ {1} + R _ {2}} \right] \left[ \begin{array}{l} u _ {e} \\ i _ {L} \end{array} \right] + \left[ \frac {R _ {2}}{R _ {1} + R _ {2}} \right] e (t)
$$

例 2 考虑人口分布问题。设某国 1988 年的人口分布为：城市人口为 $10^{7}$ ，农村人口为 $9 \times 10^{7}$ 。人口的流动情况为：每年有 4% 的上一年城市人口迁去农村，同时有 2% 的上一年农村人口迁到城市。整个国家的人口自然增长率为 1%。

确定状态变量：城市人口 $x_{1}$ 和农村人口 $x_{20}$

建立人口按年分布方程：取1988年为 $k = 0$ ，则 $k + 1$ 年时城市人口和农村人口的分布方程，可以定出为

$$
\begin{array}{l} x _ {1} (k + 1) = 1. 0 1 \left[ (1 - 0. 0 4) x _ {1} (k) + 0. 0 2 x _ {2} (k) \right] \\ x _ {2} (k + 1) = 1. 0 1 \left[ 0. 0 4 x _ {1} (k) + (1 - 0. 0 2) x _ {2} (k) \right] \\ \end{array}
$$

导出状态方程：把上述联立方程表为向量方程的形式，即得到人口分布的状态方程为：

$$
\left[ \begin{array}{l} x _ {1} (k + 1) \\ x _ {2} (k + 1) \end{array} \right] = \left[ \begin{array}{l l} 0. 9 6 9 6 & 0. 0 2 0 2 \\ 0. 0 4 0 4 & 0. 9 8 9 8 \end{array} \right] \left[ \begin{array}{l} x _ {1} (k) \\ x _ {2} (k) \end{array} \right], k = 0, 1, 2, \dots

\left[ \begin{array}{l} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] = \left[ \begin{array}{c} 1 0 ^ {7} \\ 9 \times 1 0 ^ {7} \end{array} \right]
$$
