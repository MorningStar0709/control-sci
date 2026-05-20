$$
\begin{array}{l} \left[ \begin{array}{c c c} - U _ {1 1} (s) & U _ {1 2} (s) & \mathbf {0} \\ P (s) & M ^ {- 1} (s) \Psi_ {L} (s) & \mathbf {0} \\ - R (s) & - X (s) & I _ {q} \end{array} \right] \left[ \begin{array}{c c c} I _ {m} & \mathbf {0} & \mathbf {0} \\ \mathbf {0} & s I - A & B \\ \mathbf {0} & - C & E (s) \end{array} \right] \\ = \left[ \begin{array}{c c c} I _ {n} & 0 & 0 \\ 0 & P (s) & Q (s) \\ 0 & - R (s) & W (s) \end{array} \right] \left[ \begin{array}{c c c} - U _ {1 2} (s) & U _ {1 2} (s) (s I - A) & U _ {1 2} (s) B \\ I _ {m} & \bar {C} _ {\bullet} & - Y (s) \\ 0 & 0 & I _ {p} \end{array} \right] \tag {10.66} \\ \end{array}
$$

而且，式(10.66)中最左边和最右边的矩阵都为单模阵。

③ 现在就可来证明左互质性和能控性间的等价性。为此，从（10.66）中取出如下的等式：

$$
\begin{array}{l} \left[ \begin{array}{c c} - U _ {1 1} (s) & U _ {1 2} (s) \\ P (s) & M ^ {- 1} (s) \Psi_ {L} (s) \end{array} \right] \left[ \begin{array}{c c c} I _ {m} & \mathbf {0} & \mathbf {0} \\ \mathbf {0} & s I - A & B \end{array} \right] \\ - \left[ \begin{array}{c c c} I _ {n} & 0 & 0 \\ 0 & P (s) & Q (s) \end{array} \right] \left[ \begin{array}{c c c} - U _ {1 2} (s) & U _ {1 1} (s) (s I - A) & U _ {1 2} (s) B \\ I _ {m} & \bar {C} _ {\bullet} & - Y (s) \\ 0 & 0 & I _ {p} \end{array} \right] \tag {10.67} \\ \end{array}
$$

那么，考虑到上式中最左边和最右边的矩阵均为单模阵，所以即知：

$$
\operatorname{rank} \left[ \begin{array}{c c c} I _ {m} & 0 & 0 \\ 0 & s I - A & B \end{array} \right] = m + n, \forall s \in \mathcal {C} \tag {10.68}
$$

等价于

$$
\operatorname{rank} \left[ \begin{array}{c c c} I _ {n} & 0 & 0 \\ 0 & P (s) & Q (s) \end{array} \right] = n + m, \forall s \in \mathcal {C} \tag {10.69}
$$

而这又意味着

$$\operatorname{rank} [ s I - A \quad B ] = n, \forall s \in \mathcal {C} \tag {10.70}$$

等价于

$$\operatorname{rank} [ P (s) Q (s) ] = m, \forall s \in \mathcal {C} \tag {10.71}$$

于是，再根据能控性的PBH秩判据和左互质性的秩判据，就证得了 $\{A, B\}$ 的完全能控等价于 $\{P(s), Q(s)\}$ 的左互质。从而，就完成了对结论的证明。

几点推论 上面给出的结论,以一般的形式,指出了多项式矩阵描述的左和右互质性与状态空间描述的能控性和能观测性间的等价关系。下面,我们将给以某些物理解释,并将其用于一些特殊的情况,来给出如下的几点推论。

推论1 正如把一个完全能控和完全能观测的状态空间描述称为系统的最小描述一样，一个不可简约的多项式矩阵描述，也即 $\{P(s), Q(s)\}$ 为左互质和 $\{P(s), R(s)\}$ 为右互质的多项式矩阵描述，同样是系统的一种最小描述。

推论2 对于矩阵分式描述而言, 将可从上述结论出发, 而得到类同的论断。设有右 MFD $N(s)D^{-1}(s)$ , 进而将其表为

$$N (s) D ^ {- 1} (s) = \bar {N} (s) D ^ {- 1} (s) I + E (s) \tag {10.72}$$

其中 $\bar{N}(s)D^{-1}(s)$ 为严格真的；同时，再表其能控类实现为

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u} \\ \boldsymbol {y} = C \boldsymbol {x} + E (p) \boldsymbol {u}, p = d / d t \end{array} \right. \tag {10.73}
$$
