$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{B}}} u (t), \\ y (t) = \overline {{{C}}} \overline {{{x}}} (t), \end{array} \right. \tag {1.7.21}
$$

其中

$$
\begin{array}{l} \overline {{{A}}} = P A P ^ {- 1} = \left[ \begin{array}{c c c} 0 & \mu & \mu \\ - \mu & 0 & 0 \\ 0 & 0 & 0 \end{array} \right], \quad \overline {{{B}}} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 1 \end{array} \right], \\ \overline {{{C}}} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right]. \\ \end{array}
$$

令

$$
\overline {{{A}}} _ {1 1} = \left[ \begin{array}{l l} 0 & \mu \\ - \mu & 0 \end{array} \right], \quad \overline {{{A}}} _ {1 2} = \left[ \begin{array}{l} \mu \\ 0 \end{array} \right], \quad \overline {{{A}}} _ {2 1} = [ 0, 0 ], \quad \overline {{{A}}} _ {2 2} = 0,

\overline {{{C}}} _ {1} = I, \quad \overline {{{C}}} _ {2} = 0, \quad \overline {{{B}}} _ {1} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \end{array} \right], \quad \overline {{{B}}} _ {2} = \left[ \begin{array}{l l l} 0 & 0 & 1 \end{array} \right].
$$

于是系统 (1.7.21) 又可写成

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {\overline {{{x}}}} _ {1} (t) \\ \dot {\overline {{{x}}}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} \overline {{{A}}} _ {1 1} & \overline {{{A}}} _ {1 2} \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} \overline {{{x}}} _ {1} (t) \\ \overline {{{x}}} _ {2} (t) \end{array} \right] + \left[ \begin{array}{c} \overline {{{B}}} _ {1} \\ \overline {{{B}}} _ {2} \end{array} \right] u (t),} \\ y (t) = \overline {{{x}}} _ {1} (t). \end{array} \right. \tag {1.7.22}
$$

根据极小阶观测器的设计原则得到

$$
\left\{ \begin{array}{l} \overline {{{x}}} _ {2 e} (t) = z _ {c} (t) + G _ {2} y (t), \\ \dot {z} _ {c} (t) = - G _ {2} \overline {{{A}}} _ {1 2} z _ {c} (t) + (\overline {{{B}}} _ {2} - G _ {2} \overline {{{B}}} _ {1}) u (t) \\ - G _ {2} [ \overline {{{A}}} _ {1 1} + \overline {{{A}}} _ {1 2} G _ {2} ] y (t). \end{array} \right. \tag {1.7.23}
$$

由 $\overline{A}_{12}$ 的具体形式发现 $G_{2}$ 是一个二维行向量，令 $G_{2} = [g_{1}, g_{2}]$ ，则观测器方程(1.7.23)可写为

$$
\left\{ \begin{array}{l} \overline {{x}} _ {2 e} (t) = z _ {c} (t) + g _ {1} y _ {1} (t) + g _ {2} y _ {2} (t), \\ \dot {z} _ {c} (t) = - \mu g _ {1} z _ {c} (t) - g _ {1} u _ {1} (t) - g _ {2} u _ {2} (t) + (1 + g _ {2}) u _ {3} (t) \\ \qquad - \mu (g _ {1} ^ {2} - g _ {2}) y _ {1} (t) - g _ {1} \mu (1 + g _ {2}) y _ {2} (t). \end{array} \right.
$$
