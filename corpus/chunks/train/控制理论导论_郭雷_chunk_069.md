$$
\overline {{{A}}} = \left[ \begin{array}{c c c} \overline {{{A}}} _ {1 1} & \dots & \overline {{{A}}} _ {1 m} \\ \vdots & & \vdots \\ \overline {{{A}}} _ {m 1} & \dots & \overline {{{A}}} _ {m m} \end{array} \right], \quad \overline {{{C}}} = [ \overline {{{C}}} _ {1 1} \quad \overline {{{C}}} _ {2 2} \quad \dots \quad \overline {{{C}}} _ {m m} ];

\overline {{{A}}} _ {i i} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \ddots & \vdots \\ \vdots & & \ddots & \ddots & 0 \\ 0 & \dots & & 0 & 1 \\ * & * & \dots & * & * \end{array} \right] _ {r _ {i} \times r _ {i}},

\overline {{{A}}} _ {i j} = \left[ \begin{array}{c c c} 0 & \dots & 0 \\ \vdots & & \vdots \\ 0 & \dots & 0 \\ * & \dots & * \end{array} \right] _ {r _ {1} \times r _ {j}}, \quad i \neq j;

\overline {{{C}}} _ {i i} = \left[ \begin{array}{c c c c} {0} & {0} & {\dots} & {0} \\ {\vdots} & {\vdots} & & {\vdots} \\ {0} & {0} & {\dots} & {0} \\ {1} & {0} & {\dots} & {0} \\ {0} & {0} & {\dots} & {0} \\ {\vdots} & {\vdots} & & {\vdots} \\ {0} & {0} & {\dots} & {0} \end{array} \right] \leftarrow \text {第} i \text {行}; \qquad i = 1, 2, \dots , m; \sum_ {i = 1} ^ {m} r _ {i} = n.
$$

通常把系统 (1.4.23) 叫做系统 (1.4.16) 的 Luenberger 第一能观测标准形.

定理 1.4.8 设定常线性系统 (1.4.16) 是完全能观测的，则存在一个非奇异坐标变换 $\bar{x} = T_{4}x$ ，使得系统 (1.4.16) 在此坐标变换下变成如下标准形式：

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{B}}} u (t), \\ y (t) = \overline {{{C}}} \overline {{{x}}} (t), \end{array} \right. \tag {1.4.24}
$$

其中 $\overline{A} = T_4AT_4^{-1},\overline{B} = T_4B,\overline{C} = CT_4^{-1}$ ，并且

$$
\overline {{{A}}} = \left[ \begin{array}{c c c} \overline {{{A}}} _ {1 1} & \dots & \overline {{{A}}} _ {1 m} \\ \vdots & & \vdots \\ \overline {{{A}}} _ {m 1} & \dots & \overline {{{A}}} _ {m m} \end{array} \right];

\overrightarrow {A} _ {i i} = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & * \\ 1 & 0 & \ddots & 0 & * \\ 0 & 1 & \ddots & \vdots & * \\ \vdots & \ddots & \ddots & 0 & \vdots \\ 0 & \dots & 0 & 1 & * \end{array} \right] _ {r _ {i} \times r _ {i}},

\overline {{{A}}} _ {i j} = \left[ \begin{array}{c c c c} 0 & \dots & 0 & * \\ \vdots & & \vdots & \vdots \\ 0 & \dots & 0 & * \end{array} \right] _ {r _ {1} \times r _ {j}}, \quad i \neq j;
