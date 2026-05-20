$$
\left[ \begin{array}{c c} D _ {2} (s) & I _ {p} \\ - N _ {2} (s) & E (s) \end{array} \right] \sim \left[ \begin{array}{c c} D _ {1} (s) & I _ {p} \\ - N _ {1} (s) & E (s) \end{array} \right] \tag {10.168}
$$

从而，由严格系统等价变换的传递性，即可进一步证得

$$
\left[ \begin{array}{l l} D _ {1} (s) & I _ {p} \\ - \bar {N} _ {1} (s) & \mathbf {0} \end{array} \right] \sim \left[ \begin{array}{l l} D _ {2} (s) & I _ {p} \\ - \bar {N} _ {2} (s) & \mathbf {0} \end{array} \right] \tag {10.169}
$$

也即 $\overline{N}_1(s)D_1^{-1}(s)$ 和 $\overline{N}_2(s)D_2^{-1}(s)$ 的系统矩阵 $S_{1}(s)$ 和 $S_{2}(s)$ 是严格系统等价的。类似地，也可证得， $G(s)$ 的任意两个非真的不可简约左MFD的系统矩阵间也为严格系统等价。

③ 证明 $G(s)$ 的不可简约的右 MFD 和左 MFD 间也是严格系统等价的。设 $N(s) D^{-1}(s)$ 和 $D_{L}^{-1}(s) N_{L}(s)$ 为 $G(s)$ 的任意两个不可简约的 MFD，那么必存在单模阵 $U(s)$ 使成立

$$
U (s) \left[ \begin{array}{c} - N (s) \\ D (s) \end{array} \right] = \left[ \begin{array}{l l} U _ {1 1} (s) & U _ {1 2} (s) \\ U _ {2 1} (s) & U _ {2 2} (s) \end{array} \right] \left[ \begin{array}{c} - N (s) \\ D (s) \end{array} \right] = \left[ \begin{array}{l} I _ {p} \\ 0 \end{array} \right] \tag {10.170}
$$

再考虑到

$$N (s) D ^ {- 1} (s) = D _ {L} ^ {- 1} (s) N _ {L} (s) \text {或} D _ {L} (s) N (s) = N _ {L} (s) D (s) \tag {10.171}$$

则必可适当选取 $U_{11}(s)$ 和 $U_{12}(s)$ 使有

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{l l} U _ {1 1} (s) & U _ {1 2} (s) \\ D _ {L} (s) & N _ {L} (s) \end{array} \right] \text {为单模阵}} \\ {\left[ \begin{array}{l l} U _ {1 1} (s) & U _ {1 2} (s) \\ D _ {L} (s) & N _ {L} (s) \end{array} \right] \left[ \begin{array}{c} - N (s) \\ D (s) \end{array} \right] = \left[ \begin{array}{l} I _ {p} \\ 0 \end{array} \right]} \end{array} \right. \tag {10.172}
$$

于是，由此就可建立起如下的等式：

$$
\begin{array}{l} \left[ \begin{array}{c c c} U _ {1 1} (s) & U _ {1 2} (s) & \mathbf {0} \\ D _ {L} (s) & N _ {L} (s) & \mathbf {0} \\ \hline - I _ {q} & \mathbf {0} & I _ {q} \end{array} \right] \left[ \begin{array}{c c c} I _ {q} & \mathbf {0} & \mathbf {0} \\ \hline \mathbf {0} & D (s) & I _ {p} \\ \mathbf {0} & - N (s) & \mathbf {0} \end{array} \right] \\ = \left[ \begin{array}{c c c} I _ {p} & 0 & 0 \\ \hline 0 & D _ {L} (s) & N _ {L} (s) \\ 0 & - I _ {q} & 0 \end{array} \right] \left[ \begin{array}{c c c} U _ {1 1} (s) & U _ {1 2} (s) D (s) & U _ {1 2} (s) \\ I _ {q} & N (s) & 0 \\ \hline 0 & 0 & I _ {p} \end{array} \right] \tag {10.173} \\ \end{array}
$$

其中，左起第二个和第三个矩阵分别为 $N(s)D^{-1}(s)$ 和 $D_{L}^{-1}(s)N_{L}(s)$ 的增广系统矩阵 $\overline{S}(s)$ 和 $\overline{S}_L(s)$ ，而左起第一个矩阵必为单模阵。再注意到由(10.172)可导出

$$- U _ {1 1} (s) N (s) + U _ {1 2} (s) D (s) = I _ {p} \tag {10.174}$$

从而，进而又有
