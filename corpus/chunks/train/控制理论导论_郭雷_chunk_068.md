由 $q_{1}^{T}$ 的定义推知 $\alpha_{1r_{1}-1}q_{1}^{T}A^{r_{1}-1}b_{1}=0$ 。因为 $q_{1}^{T}A^{r_{1}-1}b_{1}\neq0$ ，所以 $\alpha_{1r_{1}-1}=0$ 。用类似方法可以证明 $\alpha_{2r_{2}}= \cdots = \alpha_{rr_{r}-2}=0$ 。然后继续在式 (1.4.21) 的两边左乘 $q_{i}^{T}A^{2}, i=2,3,\cdots,r$ ，可以证明，式 (1.4.21) 中的诸系数全为零。于是 $x_{0}=0$ 。这表明 $T_{2}$ 是非奇异的。现在取坐标变换 $\overline{x}=T_{2}x$ 。则在此坐标变换下，系统 (1.4.16) 可以化成如下标准形式：

$$
\left\{ \begin{array}{l} \overline {{{x}}} (t) = \overline {{{A}}} _ {2} \overline {{{x}}} (t) + \overline {{{B}}} _ {2} u (t), \\ y (t) = \overline {{{C}}} _ {2} \overline {{{x}}} (t), \end{array} \right. \tag {1.4.22}
$$

其中 $\overline{A}_2 = T_2AT_2^{-1}$ , $\overline{B}_2 = T_2B$ , $\overline{C}_2 = CT_2^{-1}$ . 而且 $\overline{A}_2$ 和 $\overline{B}_2$ 有如下具体形式:

$$
\overline {{{A}}} _ {2} = \left[ \begin{array}{c c c} \overline {{{A}}} _ {1 1} & \dots & \overline {{{A}}} _ {1 r} \\ \vdots & & \vdots \\ \overline {{{A}}} _ {r 1} & \dots & \overline {{{A}}} _ {r r} \end{array} \right], \quad \overline {{{B}}} _ {2} = \left[ \begin{array}{c} \overline {{{B}}} _ {1 1} \\ \vdots \\ \overline {{{B}}} _ {r r} \end{array} \right];

\overline {{{A}}} _ {i i} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \ddots & \vdots \\ \vdots & \ddots & \ddots & 1 & 0 \\ 0 & & \dots & 0 & 1 \\ * & * & \dots & * & * \end{array} \right] _ {r _ {i} \times r _ {j}}. \quad \overline {{{A}}} _ {i j} = \left[ \begin{array}{c c c} 0 & \dots & 0 \\ \vdots & & \vdots \\ 0 & \dots & 0 \\ * & \dots & * \end{array} \right] _ {r _ {i} \times r _ {j}}, \quad i \neq j;

\overline {{{\boldsymbol {B}}}} _ {i i} = \left[ \begin{array}{c c c c c c c} 0 & \dots & 0 & 0 & 0 & \dots & 0 \\ \vdots & & \vdots & \vdots & \vdots & & \vdots \\ 0 & \dots & 0 & 0 & 0 & \dots & 0 \\ * & \dots & * & 1 & * & \dots & * \end{array} \right] _ {r _ {i} \times r}, \quad i = 1, 2, \dots , r.
$$

第 $i$ 列

定理 1.4.6 设定常线性系统 (1.4.16) 是能控的, 则在坐标变换 (1.4.19) 下, 系统 (1.4.16) 变成标准形 (1.4.22). 通常把这种标准形式称为系统 (1.4.16) 的 Luenberger 第二能控标准形, 也称 Brounovsky 标准形.

和单输入单输出系统一样，依照对偶引理也有 Luenberger 能观测标准形.

定理1.4.7 设定常线性系统(1.4.16)是完全能观测的，则存在一个非奇异坐标变换 $\overline{x} = T_{3}x$ 使得系统(1.4.16)在这个坐标变换下变成如下标准形式：

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{B}}} u (t), \\ y (t) = \overline {{{C}}} \overline {{{x}}} (t), \end{array} \right. \tag {1.4.23}
$$

其中 $\overline{A} = T_3AT_3^{-1},\overline{B} = T_3B,\overline{C} = CT_3^{-1}$ ，并且
