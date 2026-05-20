$$
\mathbf {y} = \left[ \begin{array}{l l} \mathbf {C} & \mathbf {0} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {x} - \hat {\mathbf {x}} \end{array} \right] \tag {9-243b}
$$

由于线性变换后系统传递函数矩阵具有不变性，由式(9-23)可导出系统传递函数矩阵

$$
\mathbf {G} (s) = \left[ \begin{array}{l l} \mathbf {C} & \mathbf {0} \end{array} \right] \left[ \begin{array}{c c} s \mathbf {I} - (\mathbf {A} - \mathbf {B K}) & - \mathbf {B K} \\ \mathbf {0} & s \mathbf {I} - (\mathbf {A} - \mathbf {H C}) \end{array} \right] ^ {- 1} \left[ \begin{array}{l} \mathbf {B} \\ \mathbf {0} \end{array} \right] \tag {9-244}
$$

利用分块矩阵求逆公式

$$
\left[ \begin{array}{l l} \boldsymbol {R} & \boldsymbol {S} \\ \boldsymbol {0} & \boldsymbol {T} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} \boldsymbol {R} ^ {- 1} & - \boldsymbol {R} ^ {- 1} \boldsymbol {S T} ^ {- 1} \\ \boldsymbol {0} & \boldsymbol {T} ^ {- 1} \end{array} \right] \tag {9-245}
$$

可得 $\mathbf{G}(s) = \mathbf{C}[s\mathbf{I} - (\mathbf{A} - \mathbf{B}\mathbf{K})]^{-1}\mathbf{B}$ (9-246)

式(9-246)正是引入真实状态 x 作为反馈的状态反馈系统

$$\dot {x} = A x + B (v - K x) = (A - B K) x + B v\mathbf {y} = \mathbf {C x} \tag {9-247}$$

的传递函数矩阵。这说明复合系统与状态反馈子系统具有相同的传递特性，与观测器部分无关，可用估值状态 $\pmb{x}$ 代替真实状态 $\pmb{x}$ 作为反馈。2n维复合系统导出了 $n\times n$ 传递矩阵，这是由于 $(x - \hat{x})$ 的不可控造成的。

由于线性变换后特征值具有不变性，由式(9-243)易导出其特征值满足关系式

$$
\left| \begin{array}{c c} s I - (A - B K) & - B K \\ 0 & s I - (A - H C) \end{array} \right| = | s I - (A - B K) | \cdot | s I - (A - H C) | \tag {9-248}
$$

该式表明复合系统特征值是由状态反馈子系统和全维状态观测器的特征值组合而成，且两部分特征值相互独立，彼此不受影响，因而状态反馈矩阵 K 和输出反馈矩阵 H 可根据各自的要求来独立进行设计，故有下述分离定理。

定理 9-8(分离定理) 若被控系统(A,B,C) 可控可观测,用状态观测器估值形成状态反馈时,其系统的极点配置和观测器设计可分别独立进行,即 K 和 H 阵的设计可分别独立进行。
