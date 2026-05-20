其中 $\{\widetilde{P}(s),\widetilde{Q}(s)\}$ 为左互质。则考虑到

$$
\left\{ \begin{array}{l} [ P (s) \quad Q (s) ] = H (s) [ \bar {P} (s) \quad \bar {Q} (s) ] \\ \operatorname{rank} [ \bar {P} (s) \quad \bar {Q} (s) ] = m, \quad \forall s \in \mathcal {C} \end{array} \right. \tag {10.88}
$$

的同时可知， $\det H(s) = 0$ 的根等同于使 $[P(s), Q(s)]$ 行降秩的 $s$ 值，于是进一步又可导出

$$\text { 输 入 解 耦 零 点 } = \text { 使 } [ P (s) \quad Q (s) ] \text { 降 秩 的 所 有 } s \text { 值 } \tag {10.89}$$

为了更直观和更清晰地来阐明输入解耦零点的物理含义，我们把讨论扩展到状态空间描述的领域。设 $(A, B, C, E(p))$ 为给定 $\{P(s), Q(s), R(s), W(s)\}$ 的维数为 $n = \deg \det P(s)$ 的一个状态空间实现，则根据 PMD 的互质性和状态空间描述的能控性和能观测性间的等价关系，可知 $(A, C)$ 为能观测，但 $(A, B)$ 为不完全能控。因此，可对 $(A, B)$ 按能控性进行结构分解，得到

$$
\left[ \begin{array}{l} \dot {\bar {x}} _ {c} \\ \dot {\bar {x}} _ {s} \end{array} \right] = \left[ \begin{array}{l l} \bar {A} _ {c} & \bar {A} _ {1 2} \\ 0 & \bar {A} _ {s} \end{array} \right] \left[ \begin{array}{l} \bar {x} _ {c} \\ \bar {x} _ {s} \end{array} \right] + \left[ \begin{array}{l} \bar {B} _ {c} \\ 0 \end{array} \right] u \tag {10.90}
$$

这表明系统的模态即 $A$ 的特征值可分成两部分，一部分为能控模即能控阵 $\overline{A}_c$ 的特征值，而另一部分为不能控模即 $\overline{A}_t$ 的特征值，且不能控模的出现正是由 $\{P(s) Q(s)\}$ 的非左互质所引起的。所以，进一步可知 $\overline{A}_t$ 的特征值等同于 $\det H(s) = 0$ 的根，从而又有

$$\text { 输入解耦零点 } = \text { 实现 } (A, B, C, E (p)) \text { 的不能控模 } \tag {10.91}$$

由于， $\overline{A}_z$ 的特征值不受输入 $\pmb{u}$ 的影响，也即是和输入相解耦的，因此这类解耦零点被称之为输入解耦零点。

(2) 输出解耦零点：对应地，来考察 PMD 中 $\{P(s), Q(s)\}$ 为左互质但 $\{P(s), R(s)\}$ 不是右互质的情形。令 $P(s)$ 和 $R(s)$ 分别为 $m \times m$ 和 $q \times m$ 阵， $m \times m$ 的多项式矩阵 $F(s)$ 为它们的最大右公因子，且 $F(s)$ 不是单模阵。于是，定义

$$\text { 输 出 解 耦 零 点 为 } \det F (s) = 0 \text { 的 根 } \tag {10.92}$$

进一步，通过和前面类同的分析，又可导出

$$
\text { 输出解耦零点为使 } \left[ \begin{array}{l} P (s) \\ R (s) \end{array} \right] \text { 降秩的所有 } s \text { 值 } \tag {10.93}
$$

再令 $(A, B, C, E(p))$ 为给定 PMD 的维数等于 $n = \deg \det P(s)$ 的一个实现，那么还可有

$$\text { 输出解稠零点 } = \text { 实现 } (A, B, C, E (p)) \text { 的不能观测模 } \tag {10.94}$$

显然, 不能观测模将不能为输出 y 所反映, 也即和输出相解耦, 因此称这类解耦零点为输出解耦零点。

两点注记 在前述讨论的基础上,我们要指出两点注意之点,它们为:

第一,由于引入了解耦零点,因此可对多项式矩阵描述的广义极点和零点作如下的规定:

$$\{\text {PMD} \text {的极点} \} = \{\text {传递函数矩阵} G (s) \text {的极点} \} \cup \{\text {解耦零点} \} \tag {10.95}\{\text { PMD 的零点 } \} = \{\text { 传递函数矩阵 } G (s) \text { 的零点 } \} \cup \{\text { 解耦零点 } \} \tag {10.96}$$

这一点是由英国学者 H. H. 罗森布罗克在 70 年代初所指出的。

第二, 只有当传递函数矩阵 $G(s)$ 为非奇异时, 解耦零点和传输零点才组成了使可简约矩阵

$$
\left[ \begin{array}{c c} P (s) & Q (s) \\ - R (s) & W (s) \end{array} \right] \tag {10.97}
$$
