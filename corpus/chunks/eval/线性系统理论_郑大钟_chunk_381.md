$$
\begin{array}{l} \left[ \begin{array}{c c} U _ {1 1} (s) & U _ {1 2} (s) D (s) \\ I _ {q} & N (s) \end{array} \right] = \left[ \begin{array}{c c} U _ {1 1} (s) & I _ {p} + U _ {1 1} (s) N (s) \\ I _ {q} & N (s) \end{array} \right] \\ = \left[ \begin{array}{c c} U _ {1 1} (s) & I _ {p} \\ I _ {q} & 0 \end{array} \right] \left[ \begin{array}{c c} I _ {q} & N (s) \\ 0 & I _ {p} \end{array} \right] \tag {10.175} \\ \end{array}
$$

上式中，等式右边的第二个矩阵显然为单模阵，而第一个矩阵由于

$$
\left[ \begin{array}{c c} U _ {1 1} (s) & I _ {p} \\ I _ {q} & \mathbf {0} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \mathbf {0} & I _ {q} \\ I _ {p} & - U _ {1 1} (s) \end{array} \right] = \text {多项式矩阵} \tag {10.176}
$$

故也为单模阵。这表明，(10.175)的最左边的矩阵为单模阵。于是，可知(10.173)中，右起第一个矩阵也为单模阵。由此，就证明了

$$\bar {S} (s) \sim \bar {S} _ {L} (s) \tag {10.177}$$

也即不可简约的左 MFD 和右 MFD 间是严格系统等价的。至此，证明完成。

结论7 具有同样传递函数矩阵 $G(s)$ 的所有不可简约的多项式矩阵描述都是严格系统等价的。

证 表 $\{P_i(s), Q_i(s), R_i(s), W_i(s)\}$ , $i = 1, 2$ , 为 $G(s)$ 的任意两个不可简约的 PMD, $(A_i, B_i, C_i, E_i(p))$ , $i = 1, 2$ , 为它们的最小实现即不可简约实现。考虑到, $(A_1, B_1, C_1, E_1(p))$ 和 $(A_2, B_2, C_2, E_2(p))$ 是代数等价的, 所以由结论 5 可导出

$$
\left[ \begin{array}{c c} s I - A _ {2} & B _ {2} \\ - C _ {2} & E _ {2} (s) \end{array} \right] \sim \left[ \begin{array}{c c} s I - A _ {1} & B _ {1} \\ - C _ {1} & E _ {1} (s) \end{array} \right] \tag {10.178}
$$

再根据(10.62)，又可得到

$$
\left[ \begin{array}{c c c} I _ {m} & \mathbf {0} & \mathbf {0} \\ \mathbf {0} & P _ {2} (s) & Q _ {2} (s) \\ \mathbf {0} & - R _ {2} (s) & W _ {2} (s) \end{array} \right] \sim \left[ \begin{array}{c c c} I _ {m} & \mathbf {0} & \mathbf {0} \\ \mathbf {0} & s I - A _ {2} & B _ {2} \\ \mathbf {0} & - C _ {2} & E _ {2} (s) \end{array} \right] \tag {10.179}
$$

和

$$
\left[ \begin{array}{c c c} I _ {m} & 0 & 0 \\ 0 & s I - A _ {1} & B _ {1} \\ 0 & - C _ {1} & E _ {1} (s) \end{array} \right] \sim \left[ \begin{array}{c c c} I _ {n} & 0 & 0 \\ 0 & P _ {1} (s) & Q _ {1} (s) \\ 0 & - R _ {1} (s) & W _ {1} (s) \end{array} \right] \tag {10.180}
$$

于是，由严格系统等价变换的传递性，进一步可证得

$$
\left[ \begin{array}{c c c} I _ {n} & 0 & 0 \\ 0 & P _ {2} (s) & Q _ {2} (s) \\ 0 & - R _ {2} (s) & W _ {2} (s) \end{array} \right] \sim \left[ \begin{array}{c c c} I _ {n} & 0 & 0 \\ 0 & P _ {1} (s) & Q _ {1} (s) \\ 0 & - R _ {1} (s) & W _ {1} (s) \end{array} \right] \tag {10.181}
$$

也即 $\{P_2(s), Q_2(s), R_2(s), W_2(s)\}$ 和 $\{P_1(s), Q_1(s), R_1(s), W_1(s)\}$ 是严格系统等价的。从而，证明完成。

结论8 给定传递函数矩阵 $G(s)$ ，表 $\Delta(G(s))$ 为它的特征多项式。则由于 $G(s)$ 的不可简约实现、不可简约 MFD、以及不可简约 PMD 间各都是严格系统等价的，所以必成立如下的关系式：

$$\Delta (G (s)) \sim \det (s I - A) \sim \det D (s) \sim \det P (s) \tag {10.182}$$
