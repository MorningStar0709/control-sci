$$t _ {2} \overline {{{G}}} _ {o} (s) = D ^ {- 1} (s) N (s) = \frac {1}{s ^ {3} + 3} [ s + 1, s (s + 1) 1 ]$$

并且，显然成立 $\Delta [t_2\overline{G}_o(s)] = \Delta [\overline{G}_o(s)]$ 。再之，由上式可导出：

$$D (s) = D _ {3} s ^ {3} + D _ {2} s ^ {2} + D _ {1} s + D _ {0} = s ^ {3} + 3N (s) = N _ {3} s ^ {3} + N _ {2} s ^ {2} + N _ {1} s + N _ {0} = [ 0 \quad 1 \quad 0 ] s ^ {2} + [ 1 \quad 1 \quad 0 ] s + [ 1 \quad 0 \quad 1 ]$$

然后，按 $S_{l}$ 的块转置形式来组成系数矩阵 $\bar{S}_{l}$ ，而整数 l 的值可从零取起，直至系数矩阵 $\bar{S}_{l}$ 为行满秩。对于此处情况，试算结果有 l=0，即系数矩阵 $\bar{S}_{0}$ 为：

$$
\overline {{S}} _ {0} = \left[ \begin{array}{l l} D _ {0} & N _ {0} \\ D _ {1} & N _ {1} \\ D _ {2} & N _ {2} \\ D _ {3} & N _ {3} \end{array} \right] = \left[ \begin{array}{l l l l} 3 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \end{array} \right]
$$

从而可知能控性指数 $\mu = l + 1 = 1$ ，而补偿器的次数应为 $m = \mu - 1 = 0$ 。现进一步来指定 $n + m = 3 + 0 = 3$ 个期望的闭环极点，设为 $\lambda_1^* = -1, \lambda_2^* = -1, \lambda_3^* = -2$ 。由此，可得

$$D _ {F} (s) = (s + 1) ^ {2} (s + 2) = s ^ {3} + 4 s ^ {2} + 5 s + 2$$

再由求解方程

$$
\tilde {S} _ {o} \left[ \begin{array}{l} D _ {c o} \\ N _ {c o} \end{array} \right] = \left[ \begin{array}{l} F _ {0} \\ F _ {1} \\ F _ {2} \\ F _ {3} \end{array} \right] - \left[ \begin{array}{l} 2 \\ 5 \\ 4 \\ 1 \end{array} \right]
$$

可以定出

$$
\left[ \begin{array}{l} D _ {c o} \\ N _ {c o} \end{array} \right] = \overline {{S}} _ {o} ^ {- 1} \left[ \begin{array}{l} F _ {0} \\ F _ {1} \\ F _ {2} \\ F _ {3} \end{array} \right] = \left[ \begin{array}{r r r r} 0 & 0 & 0 & 1 \\ 0 & 1 & - 1 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & - 1 & 1 & - 3 \end{array} \right] \left[ \begin{array}{l} 2 \\ 5 \\ 4 \\ 1 \end{array} \right] = \left[ \begin{array}{l} 1 \\ 1 \\ 4 \\ - 2 \end{array} \right]
$$

也即

$$
D _ {c o} = 1, N _ {c o} = \left[ \begin{array}{l} 1 \\ 4 \\ - 2 \end{array} \right]
$$

于是，可进而得到

$$
\bar {C} (s) = D _ {e} ^ {- 1} (s) N _ {c} (s) = \left[ \begin{array}{l} 1 \\ 4 \\ - 2 \end{array} \right]

C (s) = \widetilde {C} (s) t _ {2} = \left[ \begin{array}{c} 1 \\ 4 \\ - 2 \end{array} \right] [ 1 0 ] = \left[ \begin{array}{c c} 1 & 0 \\ 4 & 0 \\ - 2 & 0 \end{array} \right]
$$

此外，为工程实施上的简单起见，通常将图11.16的输出反馈系统结构化为图11.17所示的形式，其中 $\tilde{C}(s) = C(s) + K$ 为正向通道的补偿器的传递函数矩阵。对于所讨论的这个例子，有

$$
\widetilde {C} (s) = C (s) + K = \left[ \begin{array}{l l} 1 & 0 \\ 4 & 0 \\ - 2 & 0 \end{array} \right] + \left[ \begin{array}{r r} 1 & - 1 \\ - 1 & 0 \\ 2 & 1 \end{array} \right] = \left[ \begin{array}{l l} 2 & - 1 \\ 3 & 0 \\ 0 & 1 \end{array} \right]
$$
