# 3.8 线性系统的结构分解

这一节里,我们转而来讨论不完全能控和不完全能观测的系统。对于这类系统,一个重要的问题,是研究其结构按能控性、能观测性、或者同时按两者进行分解的方法和途径。通过分解,将可把系统的结构以明显的形式,区分为能控的部分和不能控的部分,能观测的部分和不能观测的部分,或者同时地表为能控且能观测、能控不能观测、不能控能观测、以及不能控且不能观测四个部分。研究系统结构的分解,有助于更深刻地了解系统的结构特性,也能有助于更深入地揭示状态空间描述和输入-输出描述间的本质差别。下面的讨论中,将重点研究线性定常系统,随后再把有关结论推广于线性时变系统。

能控性和能观测性在线性非奇异变换下的属性 对系统进行结构分解是通过引入适当的线性非奇异变换来实现的。因此，有必要首先对系统的能控性和能观测性在线性非奇异变换下的属性作一些讨论。

结论1 设 $(\bar{A}, \bar{B}, \bar{C})$ 为对 $(A, B, C)$ 进行线性非奇异变换所导出的结果，即两者之间成立：

$$A = P ^ {- 1} \bar {A} P, \quad B = P ^ {- 1} \bar {B}, \quad C = \bar {C} \bar {P} \tag {3.219}$$

其中 $P$ 为非奇异常阵。则必成立

$$\operatorname{rank} \bar {Q} _ {\bullet} = \operatorname{rank} Q _ {\bullet} \tag {3.220}$$

和

$$\operatorname{rank} \bar {Q} _ {o} = \operatorname{rank} Q _ {o} \tag {3.221}$$

其中， $\overline{Q}_c$ 和 $Q_c$ 为两者的能控性矩阵， $\overline{Q}_o$ 和 $Q_o$ 为两者的能观测性矩阵。

证 利用(3.219)，即有

$$\bar {Q} _ {\bullet} = [ \bar {B} | \bar {A} \bar {B} | \dots | \bar {A} ^ {n - 1} \bar {B} ] = [ P B | P A B | \dots | P A ^ {n - 1} B ] = P Q _ {\bullet} \tag {3.222}$$

考虑到 $\operatorname{rank} P = n$ 和 $\operatorname{rank} Q_{c} \leqslant n$ ，故由此可导出

$$\operatorname{rank} \bar {Q} _ {e} \leqslant \min \left\{\operatorname{rank} P, \operatorname{rank} Q _ {e} \right\} = \operatorname{rank} Q _ {e} \tag {3.223}$$

再因 P 为非奇异, 由 (3.222) 还可得到

$$Q _ {e} = P ^ {- 1} \overline {{{Q}}} _ {e} \tag {3.224}$$

而由（3.224）又可导出

$$\operatorname{rank} Q _ {e} \leqslant \min \left\{\operatorname{rank} P ^ {- 1}, \operatorname{rank} \bar {Q} _ {e} \right\} = \operatorname{rank} \bar {Q} _ {e} \tag {3.225}$$

于是，由(3.223)和(3.225)就可证得(3.220)。同理，也可证得(3.221)。从而，证明完成。

结论2 对线性时变系统 $\dot{x} = A(t)x + B(t)u, y = C(t)x, t \in J$ （时间定义区间），作可微非奇异变换 $\hat{x} = R^{-1}(t)x$ ，其中 $R(t)$ 的元是对 $t$ 的绝对连续函数，且 $R(t)$ 对一切 $t \in [t_0, t_1]$ 均不降秩， $t_0 \in J, t_1 > t_0, t_1 \in J$ 。则系统的格拉姆矩阵在变换后的秩不变，即成立

$$\operatorname{rank} \hat {W} _ {c} \left[ t _ {0}, t _ {1} \right] = \operatorname{rank} W _ {c} \left[ t _ {0}, t _ {1} \right] \tag {3.226}$$

和

$$\operatorname{rank} \hat {W} _ {o} \left[ t _ {0}, t _ {1} \right] = \operatorname{rank} W _ {o} \left[ t _ {0}, t _ {1} \right] \tag {3.227}$$

证 表系统在变换后的状态空间描述为:

$$
\begin{array}{l} \dot {\hat {x}} = \hat {A} (t) \hat {x} + \hat {B} (t) u \\ \mathbf {y} = \hat {C} (t) \hat {\mathbf {x}} \tag {3.228} \\ \end{array}
$$

其中
