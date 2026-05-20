$$Y _ {1} (s) = \frac {1 / (2 s + 1)}{1 + 1 / (2 s + 1)} U _ {1} (s) = \frac {1}{2 (s + 1)} U _ {1} (s)Y _ {2} (s) = \frac {1 / (s + 1)}{1 + 1 / (s + 1)} U _ {2} (s) + \frac {1}{1 + 1 / (s + 1)} \cdot \frac {1}{1 + 1 / (2 s + 1)} U _ {1} (s)= \frac {1}{s + 2} U _ {2} (s) + \frac {2 s + 1}{2 (s + 2)} U _ {1} (s)$$

其向量-矩阵形式为

$$
\mathbf {Y} (s) = \left[ \begin{array}{l} Y _ {1} (s) \\ Y _ {2} (s) \end{array} \right] = \left[ \begin{array}{c c} \frac {1}{2 (s + 1)} & 0 \\ \frac {2 s + 1}{2 (s + 2)} & \frac {1}{s + 2} \end{array} \right] \left[ \begin{array}{l} U _ {1} (s) \\ U _ {2} (s) \end{array} \right] = \boldsymbol {\Phi} ^ {\prime} (s) \mathbf {U} (s)
$$

原系统闭环传递矩阵为

$$
\boldsymbol {\Phi} ^ {\prime} (s) = \left[ \begin{array}{c c} \frac {1}{2 (s + 1)} & 0 \\ \frac {2 s + 1}{2 (s + 2)} & \frac {1}{s + 2} \end{array} \right]
$$

串联补偿器 $G_{c}(s)$ 的设计：由式(9-60)并考虑 $\pmb {H}(s) = \pmb{I}$ ，有

$$
\begin{array}{l} \mathbf {G} _ {c} (s) = \mathbf {G} _ {0} ^ {- 1} (s) \boldsymbol {\Phi} (s) [ \mathbf {I} - \boldsymbol {\Phi} (s) ] ^ {- 1} \\ = \left[ \begin{array}{c c} \frac {1}{2 s + 1} & 0 \\ 1 & \frac {1}{s + 1} \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} \frac {1}{s + 1} & 0 \\ 0 & \frac {1}{5 s + 1} \end{array} \right] \left[ \begin{array}{c c} \frac {s}{s + 1} & 0 \\ 0 & \frac {5 s}{5 s + 1} \end{array} \right] ^ {- 1} \\ = \left[ \begin{array}{c c} 2 s + 1 & 0 \\ - (2 s + 1) (s + 1) & s + 1 \end{array} \right] \left[ \begin{array}{c c} \frac {1}{s + 1} & 0 \\ 0 & \frac {1}{5 s + 1} \end{array} \right] \left[ \begin{array}{c c} \frac {s + 1}{s} & 0 \\ 0 & \frac {5 s + 1}{5 s} \end{array} \right] \\ = \left[ \begin{array}{c c} \frac {2 s + 1}{s} & 0 \\ - \frac {(2 s + 1) (s + 1)}{s} & \frac {s + 1}{5 s} \end{array} \right] = \left[ \begin{array}{l l} G _ {c 1 1} (s) & G _ {c 1 2} (s) \\ G _ {c 2 1} (s) & G _ {c 2 2} (s) \end{array} \right] \\ \end{array}
$$

式中， $G_{ij}(s)$ 表示 $U_{j}(s)$ 至 $Y_{i}(s)(i,j = 1,2)$ 通道的串联补偿器传递函数。可以验证这种解耦系统的开环传递矩阵 $\mathbf{G}_0(s)\mathbf{G}_c(s)$ 为对角阵：

$$
\mathbf {G} _ {0} (s) \mathbf {G} _ {c} (s) = \left[ \begin{array}{l l} \frac {1}{2 s + 1} & 0 \\ 1 & \frac {1}{s + 1} \end{array} \right] \left[ \begin{array}{l l} \frac {2 s + 1}{s} & 0 \\ - \frac {(2 s + 1) (s + 1)}{s} & \frac {s + 1}{5 s} \end{array} \right] = \left[ \begin{array}{l l} \frac {1}{s} & 0 \\ 0 & \frac {1}{5 s} \end{array} \right]
$$

用串联补偿器实现解耦的系统结构图如图 9-18 所示。

前馈补偿器 $G_{d}(s)$ 设计：由式(9-62)，有
