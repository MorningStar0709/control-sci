证明 由对偶原理可知，系统 $(A, B, C)$ 完全能观测性的充要条件是它的对偶系统 $(-A^{\mathrm{T}}, C^{\mathrm{T}}, B^{\mathrm{T}})$ 完全能控。由定理1.3.3知，对偶系统 $(-A^{\mathrm{T}}, C^{\mathrm{T}}, B^{\mathrm{T}})$ 完全能控的充要条件是对每个 $s \in \sigma(-A^{\mathrm{T}})$ 都有 $\operatorname{rank}[-A^{\mathrm{T}} - sI_n, C] = n$ 。这又等价于

$$
\operatorname{rank} \left[ \begin{array}{c} - A - s I _ {n} \\ C \end{array} \right] = \operatorname{rank} \left[ \begin{array}{c} A + s I _ {n} \\ C \end{array} \right] \left[ \begin{array}{c c} - I _ {n} & 0 \\ 0 & I _ {n} \end{array} \right] = n.
$$

可见，系统 $(A, B, C)$ 完全能观测性的充要条件是，对每个 $s \in \sigma(-A^{\mathrm{T}})$ 都有

$$
\operatorname{rank} \left[ \begin{array}{c} A + s I _ {n} \\ C \end{array} \right] = n.
$$

因为 $\sigma(-\mathbf{A}^{\mathrm{T}}) = -\sigma(\mathbf{A}^{\mathrm{T}}) = -\sigma(\mathbf{A})$ ，所以系统 $(\mathbf{A}, \mathbf{B}, \mathbf{C})$ 完全能观测的充要条件是，对每个 $s \in \sigma(\mathbf{A})$ 都有

$$
\operatorname{rank} \left[ \begin{array}{c} A - s I _ {n} \\ C \end{array} \right] = n.
$$

推论1.3.6 定常线性系统 $(A, B, C)$ 完全能观测的充要条件是它没有输出解耦零点.

根据系统的能观测性，可以对定常线性系统 $(A, B, C)$ 的矩阵 $A$ 的特征值（或系统的极点）进行分类。当 $s_0 \in \sigma(A)$ ，并且满足

$$
\operatorname{rank} \left[ \begin{array}{c} A - s _ {0} I _ {n} \\ C \end{array} \right] <   n
$$

时，系统 $(A, B, C)$ 是不完全能观测的。这样的 $s_0$ 叫做这个系统的一个不能观测振型。这和不能控振型相对应，它们都是系统的极点。同时容易看出，不能控振型必是系统的输入解耦零点，不能观测振型必是系统的输出解耦零点；反之亦然。

关于定常线性系统能观测性的判别定理1.3.6和1.3.7都是从代数观点出发的，其判据反映了系统的一种结构性质。通常说系统 $(A,B,C)$ 能观测也可以说 $(A,C)$ 能观测。关于 $(A,C)$ 能观测的判别定理1.3.6和1.3.7成为能观测性的代数判据。不过，在检验定常线性系统的能观测性，有时不一定需要计算能观测性矩阵 $Q_{o}$ 的秩，而只需计算它的前面若干行组成的矩阵的秩便可(见习题1.3).

上面对状态空间按照能控性和能观测性进行了划分，分为能控子空间、不能控子空间、能观测子空间和不能观测子空间。在这样的划分下，如果适当选取系统的一组状态变量，系统的结构具有哪些特征呢？这就是所要研究的定常线性系统的标准结构问题。

引理1.3.2 已知定常线性系统 $(A, B, C)$ . 取坐标变换 $\overline{x} = Tx, T$ 是一个 $n \times n$ 阶非奇异矩阵. 那么在这个坐标变换下, 系统 $(A, B, C)$ 的能控性和能观测性保持不变.

证明 在坐标变换 $\overline{x} = Tx$ 下，系统 $(A, B, C)$ 变成

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} x (t) + \overline {{{B}}} u (t), \\ y (t) = \overline {{{C}}} x (t), \end{array} \right.
$$

其中 $\overline{A} = TAT^{-1},\overline{B} = TB,\overline{C} = CT^{-1}$

由于
