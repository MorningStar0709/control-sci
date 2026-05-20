\overline {{{A}}} _ {3} = \left[ \begin{array}{c c c c} {{a _ {1 \mu + 1}}} & {{a _ {1 \mu + 2}}} & {{\dots}} & {{a _ {1 n}}} \\ {{a _ {2 \mu + 1}}} & {{a _ {2 \mu + 2}}} & {{\dots}} & {{a _ {2 n}}} \\ {{\vdots}} & {{\vdots}} & {} & {{\vdots}} \\ {{a _ {\mu \mu + 1}}} & {{a _ {\mu \mu + 2}}} & {{\dots}} & {{a _ {\mu n}}} \end{array} \right], \quad \text {且} \quad \overline {{{A}}} = \left[ \begin{array}{c c} {{\overline {{{A}}} _ {1}}} & {{\overline {{{A}}} _ {3}}} \\ {{0}} & {{\overline {{{A}}} _ {2}}} \end{array} \right],
$$

则有 $AT = T\overline{A}$ , 即 $\overline{A} = T^{-1}AT$ . 由于 $B$ 的每一列都是能控子空间 $\chi_1$ 中的元, 而 $\chi_1$ 又是 $A$ 的不变子空间, 因此用与前面类似的方法可以证明

$$
\overline {{{{\boldsymbol {B}}}}} = \boldsymbol {T} ^ {- 1} \boldsymbol {B} = \left[ \begin{array}{c} \overline {{{{\boldsymbol {B}}}}} _ {1} \\ 0 \end{array} \right],
$$

其中 $\overline{B}_1$ 为一个 $\mu \times r$ 阶矩阵.

如果对系统 $(A, B, C)$ 取坐标变换 $\overline{x} = T^{-1}x$ , 那么系统 $(A, B, C)$ 将变成

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {\overline {{{x}}}} _ {1} (t) \\ \dot {\overline {{{x}}}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} \overline {{{A}}} _ {1} & \overline {{{A}}} _ {3} \\ 0 & \overline {{{A}}} _ {2} \end{array} \right] \left[ \begin{array}{c} \overline {{{x}}} _ {1} (t) \\ \overline {{{x}}} _ {2} (t) \end{array} \right] + \left[ \begin{array}{c} \overline {{{B}}} _ {1} \\ 0 \end{array} \right] u (t),} \\ y (t) = \overline {{{C}}} _ {1} \overline {{{x}}} _ {1} (t) + \overline {{{C}}} _ {2} \overline {{{x}}} _ {2} (t), \end{array} \right. \tag {1.3.16}
$$

其中 $\overline{x}_1(t)$ 为 $\mu$ 维状态变量， $\overline{x}_2(t)$ 为 $n - \mu$ 维状态变量，并且 $[\overline{C}_1, \overline{C}_2] = CT$ .

对系统 $(\overline{A},\overline{B},\overline{C})$ ，它的能控性矩阵为

$$
\overline {{{Q}}} _ {c} = [ \overline {{{B}}}, \overline {{{A B}}}, \dots , \overline {{{A}}} ^ {n - 1} \overline {{{B}}} ] = \left[ \begin{array}{c c c c} \overline {{{B}}} _ {1} & \overline {{{A}}} _ {1} \overline {{{B}}} _ {1} & \dots & \overline {{{A}}} _ {1} ^ {n - 1} \overline {{{B}}} _ {1} \\ 0 & 0 & \dots & 0 \end{array} \right] = T ^ {- 1} Q _ {c}
$$

由于假设 $\mathcal{X}_1$ 是 $\mu$ 维的，而它又是由 $Q_{c}$ 各列所构成的线性子空间，因此必有 $\operatorname{rank} Q_{c} = \mu$ 。同时，又因为 $T^{-1}$ 为非奇异矩阵，所以有 $\operatorname{rank} \overline{Q}_{c} = \operatorname{rank} Q_{c} = \mu$ 。从而有
