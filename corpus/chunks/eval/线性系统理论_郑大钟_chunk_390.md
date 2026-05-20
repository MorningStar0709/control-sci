$$
\left[ \begin{array}{c c c c} {- D _ {1} (s)} & {\mathbf {0}} & {\mathbf {0}} & {I _ {p _ {1}}} \\ {\mathbf {0}} & {D _ {2} (s)} & {I _ {p _ {2}}} & {\mathbf {0}} \\ {N _ {1} (s)} & {D _ {2} (s)} & {\mathbf {0}} & {\mathbf {0}} \end{array} \right] \text {行满秩,} \forall s \in \mathcal {C} \tag {11.22}
$$

而这显然又等价于

$$\left[ N _ {1} (s) D _ {2} (s) \right] \text {行满秩，} \forall s \in \mathcal {C} \tag {11.23}$$

于是证得 $S_{T}$ 能控的充分必要条件是 $\{D_2(s), N_1(s)\}$ 为左互质。

第二种情况： $G_{1}(s) = N_{1}(s)D_{1}^{-1}(s), G_{2}(s) = D_{L2}^{-1}(s)N_{L2}(s)$ ，则类同于上述推导可得到 $S_{T}$ 的PMD方程为：

$$
\left[ \begin{array}{c c c c} D _ {1} (s) & 0 & 0 & I _ {p _ {1}} \\ - N _ {1} (s) & 0 & - I _ {p _ {2}} & 0 \\ 0 & D _ {L 2} (s) & N _ {L 2} (s) & 0 \\ 0 & - I _ {q _ {2}} & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \hat {\zeta} _ {1} (s) \\ \hat {\zeta} _ {2} (s) \\ - \hat {y} _ {1} (s) \\ - \hat {u} (s) \end{array} \right] = \left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ - \hat {y} (s) \end{array} \right] \tag {11.24}
$$

现对上式的系统矩阵引入初等运算：将块行2左乘 $N_{L2}(s)$ 后加于块行3，将块列1右乘一 $I_{p_1}$ 。那么可得到严格系统等价变换后的系统矩阵为：

$$
\left[ \begin{array}{c c c c} - D _ {1} (s) & 0 & 0 & I _ {p _ {1}} \\ N _ {1} (s) & 0 & - I _ {p _ {2}} & 0 \\ N _ {L 2} (s) N _ {1} (s) & D _ {L 2} (s) & 0 & 0 \\ \hdashline 0 & - I _ {q _ {2}} & 0 & 0 \end{array} \right] \tag {11.25}
$$

这表明， $S_{T}$ 能控的充分必要条件是

$$\left[ N _ {L 2} (s) N _ {1} (s) \quad D _ {L 2} (s) \right] \text {行满秩，} \forall s \in \mathcal {C} \tag {11.26}$$

也即 $\{D_{L2}(s), N_{L2}(s)N_1(s)\}$ 为左互质。

第三种情况： $G_{1}(s) = D_{L1}^{-1}(s)N_{L1}(s)$ ， $G_{2}(s) = N_{2}(s)D_{2}^{-1}(s)$ ，这时的推证过程和上述第二种情况相类同，故具体证明过程略去，结论是 $S_{T}$ 能控当且仅当 $\{D_{L1}(s)D_2(s), N_{L1}(s)\}$ 为左互质。由此，就完成了整个证明。

结论2 设 $p_1 \geqslant q_1 = p_2, q_2 \geqslant p_2 = q_1$ ，则对图11.2所示的多输入-多输出串联系统， $S_T$ 为能控的一个充分条件是 $G_2(s)$ 没有一个极点等同于 $G_1(s)$ 的传输零点， $S_T$ 为能观测的一个充分条件是 $G_1(s)$ 没有一个极点等同于 $G_2(s)$ 的传输零点。

证 限于证明能控性条件,能观测性条件可由对偶原理导出。表 $G_{i}(s)$ 的不可简约 MFD 为

$$G _ {i} (s) = N _ {i} (s) D _ {i} ^ {- 1} (s), i = 1, 2 \tag {11.27}$$

且知

$$
\left\{ \begin{array}{l} G _ {i} (s) \text {的极点} = \det D _ {i} (s) = 0 \text {的根} \\ G _ {i} (s) \text {的传输零点} = \text {使} N _ {i} (s) \text {降秩的} s \text {值} \end{array} \right. \tag {11.28}
$$

于是，由此即知，当 $G_{2}(s)$ 没有一个极点等同于 $G_{3}(s)$ 的传输零点时，有

$$\operatorname{rank} N _ {1} (s) = q _ {1} = p _ {2}, \text {对} G _ {2} (s) \text {的极点} \tag {11.29}$$

而一般地又有

$$\operatorname{rank} D _ {2} (s) = p _ {2}, \text {对除} G _ {2} (s) \text {的极点外} s \in \mathcal {C} \tag {11.30}$$

这样，由(11.29)和(11.30)就可导出
