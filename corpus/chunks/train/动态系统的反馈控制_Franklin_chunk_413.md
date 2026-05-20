给定一般形式的矩阵 A, B, C 和标量 D，我们想要找到变换矩阵 T 使得 $\overline{A}$ ， $\overline{B}$ ， $\overline{C}$ 和 $\overline{D}$ 为具有特殊形式的矩阵，例如能控标准形。为了找到这样的矩阵 T，我们首先假设 A, B, C 和 D 已经是所要求的形式，进一步假设变换矩阵 T 具有一般形式且能够匹配各个项。现在我们对一个三阶系统进行研究，通过推导过程将分析推广到更一般的情形。步骤如下。

首先改写式(7.21a)为

$$\overline {{{A}}} T ^ {- 1} = T ^ {- 1} A$$

如果 $\overline{A}$ 是能控标准形，将 $T^{-1}$ 按行分块为含 $t_1$ ， $t_2$ 和 $t_3$ 行矢量的矩阵，则有

$$
\left[ \begin{array}{c c c} - a _ {1} & - a _ {2} & - a _ {3} \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{l} t _ {1} \\ t _ {2} \\ t _ {3} \end{array} \right] = \left[ \begin{array}{l} t _ {1} A \\ t _ {2} A \\ t _ {3} A \end{array} \right] \tag {7.23}
$$

将第三行和第二行展开，可得到如下矩阵方程：

$$\boldsymbol {t} _ {2} = \boldsymbol {t} _ {3} \boldsymbol {A} \tag {7.24a}\boldsymbol {t} _ {1} = \boldsymbol {t} _ {2} \boldsymbol {A} = \boldsymbol {t} _ {3} \boldsymbol {A} ^ {2} \tag {7.24b}$$

在式(7.21b)中，假设 $\overline{B}$ 也是能控标准形，则有以下关系：

$$\boldsymbol {T} ^ {- 1} \boldsymbol {B} = \overline {{{\boldsymbol {B}}}}$$

或者

$$
\left[ \begin{array}{l} t _ {1} B \\ t _ {2} B \\ t _ {3} B \end{array} \right] = \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right] \tag {7.25}
$$

将式 $(7.24)$ 和式 $(7.25)$ 联立，得到

$$t _ {3} \boldsymbol {B} = 0t _ {2} \boldsymbol {B} = t _ {3} \boldsymbol {A B} = 0\boldsymbol {t} _ {1} \boldsymbol {B} = \boldsymbol {t} _ {3} \boldsymbol {A} ^ {2} \boldsymbol {B} = 1$$

这些方程依次可以写成如下矩阵形式

$$
\boldsymbol {t} _ {3} \left[ \begin{array}{l l l} \boldsymbol {B} & \boldsymbol {A B} & \boldsymbol {A} ^ {2} \boldsymbol {B} \end{array} \right] = \left[ \begin{array}{l l l} 0 & 0 & 1 \end{array} \right]
$$

或者

$$
\boldsymbol {t} _ {3} = \left[ \begin{array}{l l l} 0 & 0 & 1 \end{array} \right] \boldsymbol {C} ^ {- 1} \tag {7.26}
$$

其中：可控性矩阵为 $C=[B\ AB\ A^{2}B]$ 将 $t_{3}$ 代回到式(7.24)中，即可得到矩阵 $T^{-1}$ 的所有行矢量。

将 n 维的一般状态描述转化为能控标准形的步骤可归纳如下。

由 A 和 B 得到可控性矩阵为

$$
\mathbf {C} = \left[ \begin{array}{l l l l} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right] \tag {7.27}
$$

\- 计算变换矩阵的逆矩阵的最后一行，有

$$t _ {n} = [ 0 \quad 0 \quad \dots \quad 1 ] C ^ {- 1} \tag {7.28}$$

\- 求出整个变换矩阵为

$$
\mathbf {T} ^ {- 1} = \left[ \begin{array}{c} t _ {n} \mathbf {A} ^ {n - 1} \\ t _ {n} \mathbf {A} ^ {n - 2} \\ \vdots \\ t _ {n} \end{array} \right] \tag {7.29}
$$

\- 利用式(7.21a)，式(7.21b)和式(7.22)以及 $T^{-1}$ 求出新的矩阵。

如果可控性矩阵 C 是非奇异的，那么相应的 A 和 B 矩阵称为是能控的。能控性是物理系统的一种技术特性，在 7.5 节中我们考虑了状态反馈情形中系统的能控性，这种特性是很重要的。我们也将考虑几个不具有可控性的物理实例。
