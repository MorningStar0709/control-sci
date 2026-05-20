而由系统状态空间描述的能控性和多项式矩阵描述系数矩阵的互质性间的对应关系又可知， $S_{P}$ 的能控等价于(11.5)的 PMD 中

$$
\left\{\left[ \begin{array}{c c} D _ {1} (s) & 0 \\ 0 & D _ {2} (s) \end{array} \right], \left[ \begin{array}{l} I _ {p} \\ I _ {p} \end{array} \right] \right\} \tag {11.6}
$$

为左互质。现对(11.5)引入如下的严格系统等价变换：

$$
\begin{array}{l} \left[ \begin{array}{c c c} I _ {p} & - I _ {p} & \mathbf {0} \\ \mathbf {0} & I _ {p} & \mathbf {0} \\ \hline \mathbf {0} & \mathbf {0} & I _ {q} \end{array} \right] \left[ \begin{array}{c c c} D _ {1} (s) & \mathbf {0} & I _ {p} \\ \mathbf {0} & D _ {2} (s) & I _ {p} \\ \hline - N _ {1} (s) & - N _ {2} (s) & \mathbf {0} \end{array} \right] \left[ \begin{array}{c c c} I _ {p} & \mathbf {0} & \mathbf {0} \\ \mathbf {0} & - I _ {p} & \mathbf {0} \\ \hline \mathbf {0} & \mathbf {0} & I _ {p} \end{array} \right] \\ = \left[ \begin{array}{c c} D _ {1} (s) & D _ {2} (s) \\ \mathbf {0} & - D _ {2} (s) \\ \hline - N _ {1} (s) & N _ {2} (s) \end{array} \right] \tag {11.7} \\ \end{array}
$$

那么考虑到系统的能控性和 PMD 的互质性在严格系统等价变换下保持不变, 所以又可知 $S_{P}$ 能控等价于(11.7)中

$$
\left\{\left[ \begin{array}{c c} D _ {1} (s) & D _ {2} (s) \\ 0 & - D _ {2} (s) \end{array} \right], \left[ \begin{array}{l} 0 \\ I _ {p} \end{array} \right] \right\} \tag {11.8}
$$

为左互质或

$$
\left[ \begin{array}{c c c} D _ {1} (s) & D _ {2} (s) & 0 \\ 0 & - D _ {2} (s) & I _ {p} \end{array} \right] \text {为行满秩，} \forall s \in \mathcal {C} \tag {11.9}
$$

显然，由(11.9)可进而导出， $S_{P}$ 为能控等价于

$$\left[ D _ {1} (s) D _ {2} (s) \right] \text {为行满秩，} \forall s \in \mathcal {C} \tag {11.10}$$

或者是

$$\left\{D _ {1} (s), D _ {2} (s) \right\} \text {为左互质} \tag {11.11}$$

从而论断（i）证得。于是，证明完成。

应当指出，在结论1的 $S_{P}$ 为能控和能观测的论断（i）和（ii）中把 $G_{i}(s)$ 取为右MFD和左MFD的限制条件，并不是本质性的。从理论上讲，把 $G_{1}(s)$ 和 $G_{2}(s)$ 不管取为什么类型的不可简约MFD，如同时取成左或右MFD或分别取为右和左MFD，都不会对推导能控性和能观测性条件导致任何困难。但是，推导表明，只是在上述的限制条件下，才有可能使相应的能控性和能观测性条件表示为结论1中那样简单的形式。所以从为了应用上的简便性而言，引入这种限制条件又是完全必要的。

结论2 对于图11.1的并联系统 $S_{P}$ ，当其为多输入-多输出系统时， $S_{P}$ 为能控和能观测的一个充分条件是两个子系统的传递函数矩阵 $G_{1}(s)$ 和 $G_{2}(s)$ 不包含公共的极点。

证 已知对多输入-多输出系统，当其传递函数矩阵表为不可简约的 MFD $G(s) = N(s)D^{-1}(s) = D_{L}^{-1}(s)N_{L}(s)$ 时， $G(s)$ 的极点即为 $\det D(s) = 0$ 或 $\det D_{L}(s) = 0$ 的根。据此可知，必有

$$
\left\{ \begin{array}{l l} \operatorname{rank} D _ {1} (s) = p, & \text { 对除 } G _ {1} (s) \text { 的极点外所有 } s \in \mathcal {C} \\ \operatorname{rank} D _ {2} (s) = p, & \text { 对除 } G _ {2} (s) \text { 的极点外所有 } s \in \mathcal {C} \end{array} \right. \tag {11.12}
$$

这表明，当 $G_{1}(s)$ 和 $G_{2}(s)$ 没有公共极点时，必成立
