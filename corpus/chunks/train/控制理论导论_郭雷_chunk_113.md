# 2. 由状态反馈加极小观测器构成的动态补偿器

假设 $C = [C_1 \quad C_2]$ , 并且 $\operatorname{rank} C_1 = m, C_1$ 是一个 $m \times m$ 矩阵, 因而它是非奇异的. 如果对系统 (1.6.1) 做坐标变换

$$
\left[ \begin{array}{l} \overline {{x}} _ {1} (t) \\ \overline {{x}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} C _ {1} & C _ {2} \\ 0 & I _ {n - m} \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \end{array} \right], \tag {1.8.13}
$$

记

$$
x = \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right], \quad \overline {{x}} = \left[ \begin{array}{l} \overline {{x}} _ {1} \\ \overline {{x}} _ {2} \end{array} \right],
$$

则系统 (1.6.1) 变成

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{l} \dot {\overline {{{x}}}} _ {1} (t) \\ \dot {\overline {{{x}}}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{l l} \overline {{{A}}} _ {1 1} & \overline {{{A}}} _ {1 2} \\ \overline {{{A}}} _ {2 1} & \overline {{{A}}} _ {2 2} \end{array} \right] \left[ \begin{array}{l} \overline {{{x}}} _ {1} (t) \\ \overline {{{x}}} _ {2} (t) \end{array} \right] + \left[ \begin{array}{l} \overline {{{B}}} _ {1} \\ \overline {{{B}}} _ {2} \end{array} \right] u (t),} \\ y (t) = \overline {{{x}}} _ {1} (t), \end{array} \right. \tag {1.8.14}
$$

其中

$$
\overline {{{A}}} = \left[ \begin{array}{l l} \overline {{{A}}} _ {1 1} & \overline {{{A}}} _ {1 2} \\ \overline {{{A}}} _ {2 1} & \overline {{{A}}} _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} C _ {1} & C _ {2} \\ 0 & I _ {n - m} \end{array} \right] \left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] \left[ \begin{array}{c c} C _ {1} ^ {- 1} & - C _ {1} ^ {- 1} C _ {2} \\ 0 & I _ {n - m} \end{array} \right],

\overline {{\boldsymbol {B}}} = \left[ \begin{array}{c} \overline {{\boldsymbol {B}}} _ {1} \\ \overline {{\boldsymbol {B}}} _ {2} \end{array} \right] = \left[ \begin{array}{c c} \boldsymbol {C} _ {1} & \boldsymbol {C} _ {2} \\ 0 & \boldsymbol {I} _ {n - m} \end{array} \right] \left[ \begin{array}{c} \boldsymbol {B} _ {1} \\ \boldsymbol {B} _ {2} \end{array} \right],

\boldsymbol {A} = \left[ \begin{array}{l l} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} \\ \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {2 2} \end{array} \right] \quad \boldsymbol {B} = \left[ \begin{array}{l} \boldsymbol {B} _ {1} \\ \boldsymbol {B} _ {2} \end{array} \right].
$$

下面仍假设 $(A, B)$ 能控， $(A, C)$ 能观测。要设计系统 (1.6.1) 的一个动态补偿器，首先由定理 1.6.1 取状态反馈控制规律

$$u (t) = K x (t), \tag {1.8.15}$$
