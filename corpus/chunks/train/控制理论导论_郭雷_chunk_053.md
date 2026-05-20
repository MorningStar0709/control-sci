$$\operatorname{rank} \left[ \overline {{{B}}} _ {1}, \overline {{{A}}} _ {1} \overline {{{B}}} _ {1}, \dots , \overline {{{A}}} _ {1} ^ {\mu - 1} \overline {{{B}}} _ {1} \right] = \mu .$$

即 $(A_{1}, B_{1})$ 能控.

定理1.3.8 假设定常线性系统 $(A, B, C)$ 不完全能控，它的能控性矩阵的秩为 $\mu < n$ ，那么存在一个坐标的变换 $\overline{x} = T^{-1}x, T$ 是 $n \times n$ 非奇异矩阵，使得在这个坐标变换下，系统 $(A, B, C)$ 变成代数等价的标准结构 (1.3.16)，同时 $(A_1, B_1)$ 是完全能控的。

系统 $(A, B, C)$ 的传递函数阵为

$$\boldsymbol {W} (s) = \overline {{\boldsymbol {C}}} (s \boldsymbol {I} _ {n} - \overline {{\boldsymbol {A}}}) ^ {- 1} \overline {{\boldsymbol {B}}} = \overline {{\boldsymbol {C}}} _ {1} (s \boldsymbol {I} _ {\mu} - \overline {{\boldsymbol {A}}} _ {1}) ^ {- 1} \overline {{\boldsymbol {B}}} _ {1}$$

其中坐标变换保持系统的传递函数矩阵不变，因此，若令 $\overline{\pmb{W}}(s)$ 为系统(1.3.16)的传递函数矩阵，那么

$$\boldsymbol {W} (s) = \overline {{{\boldsymbol {W}}}} (s) = \overline {{{\boldsymbol {C}}}} _ {1} (s \boldsymbol {I} _ {\mu} - \overline {{{\boldsymbol {A}}}} _ {1}) ^ {- 1} \overline {{{\boldsymbol {B}}}} _ {1}.$$

因为 $(\overline{A}_1, \overline{B}_1)$ 能控，而 $\overline{W}(s)$ 恰好是在系统 $(\overline{A}, \overline{B}, \overline{C})$ 中不能控状态变量 $\bar{x}_2(t)$ 不出现时，子系统 $(\overline{A}_1, \overline{B}_1, \overline{C}_1)$ 的传递函数矩阵。这表明系统的传递函数矩阵不能反映系统的不能控子系统的特性。

对任给 $\pmb{A} \in \mathbb{R}^{n \times n}$ , 用 $\mathcal{N}(A)$ 记 $X$ 的零子空间

$$\mathcal {N} (A) = \{x: A x = 0, x \in \mathbb {R} ^ {n} \}.$$

如果系统 $(A, B, C)$ 不完全能观测，那么它的不能观测子空间

$$
\mathcal {X} _ {2} = \mathcal {N} \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right]
$$

是一个非零子空间．设该子空间的维数为 $n - \nu$ ，于是状态空间可作如下分解：

$$\mathbb {R} ^ {n} = \chi_ {2} \oplus \chi_ {2} ^ {\perp}.$$

这里直交补空间 $\mathcal{X}_2^{\perp}$ 的维数为 $\nu$ . 应用对偶原理和定理1.3.8, 可以获得系统 $(A, B, C)$ 的又一种代数等价的结构形式.

定理1.3.9 设定常线性系统 $(A, B, C)$ 是不完全能观测的，它的能观测矩阵的秩为 $\nu, \nu < n$ 。那么，存在一个坐标变换 $\tilde{x} = Tx, T$ 为一个 $n \times n$ 非奇异矩阵，使得在这个坐标变换下，系统 $(A, B, C)$ 变成如下代数等价的标准结构：

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {\tilde {x}} _ {1} (t) \\ \dot {\tilde {x}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} \tilde {A} _ {1} & 0 \\ \tilde {A} _ {4} & \tilde {A} _ {2} \end{array} \right] \left[ \begin{array}{c} \tilde {x} _ {1} (t) \\ \tilde {x} _ {2} (t) \end{array} \right] \left[ \begin{array}{c} \tilde {B} _ {1} \\ \tilde {B} _ {2} \end{array} \right] u (t),} \\ y (t) = \tilde {C} _ {1} \tilde {x} _ {1} (t). \end{array} \right. \tag {1.3.17}
$$
