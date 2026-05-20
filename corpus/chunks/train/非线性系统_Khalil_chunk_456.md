# 14.5.2 稳定性

考虑多输入-多输出非线性系统

$$\dot {x} = A x + B \phi (x, z, u) \tag {14.103}\dot {z} = \psi (x, z, u) \tag {14.104}y = C x \tag {14.105}\zeta = q (x, z) \tag {14.106}$$

其中 $u \in R^{p}$ 是控制输入, $y \in R^{m}$ 和 $\zeta \in R^{s}$ 是被测输出, $x \in R^{\rho}$ 和 $z \in R^{\ell}$ 构成了状态向量, $\rho \times \rho$ 矩

阵 $A, \rho \times m$ 矩阵 $B$ 和 $m \times \rho$ 矩阵 $C$ 分别为

$$
A = \text { block   diag } [ A _ {1}, \dots , A _ {m} ], \quad A _ {i} = \left[ \begin{array}{c c c c c} 0 & 1 & \dots & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & & & & \vdots \\ 0 & \dots & \dots & 0 & 1 \\ 0 & \dots & \dots & \dots & 0 \end{array} \right] _ {\rho_ {i} \times \rho_ {i}}

B = \text { block   diag } [ B _ {1}, \dots , B _ {m} ], \quad B _ {i} = \left[ \begin{array}{c} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] _ {\rho_ {i} \times 1}

C = \text { block   diag } [ C _ {1}, \dots , C _ {m} ], \quad C _ {i} = \left[ \begin{array}{c c c c c} 1 & 0 & \dots & \dots & 0 \end{array} \right] _ {1 \times \rho_ {i}}
$$

其中 $1 \leqslant i \leqslant m, \rho = \rho_{1} + \cdots + \rho_{m}$ , 代表 $m$ 个积分器链, 函数 $\phi, \psi$ 和 $q$ 对其自变量 $(x, z, u) \in D_{x} \times D_{z} \times R^{p}$ 是利普希茨的, $D_{x} \subset R^{p}$ 和 $D_{z} \subset R^{s}$ 为包含各自原点的定义域, 此外 $\phi(0, 0, 0) = 0$ , $\psi(0, 0, 0) = 0, q(0, 0) = 0$ 。我们的目标是设计一个输出反馈控制器, 以稳定原点。

系统(14.103)～(14.106)的模型主要来自输入-输出可线性化系统的标准形和机械及机电系统的模型。在这些系统中，位移变量一般是可测的，但其导数（速度、加速度等）不可测。单输入-单输出系统的标准形由式(13.16)至式(13.18)给出，容易看出当 $x=\xi,z=\eta$ 时系统取方程(14.103)至方程(14.105)的形式①。如果只有y是被测变量，即可去掉方程(14.106)，但是在许多问题中，除了积分器链端口的状态变量可测外，还可测得其他一些状态变量。例如，习题1.18中磁悬浮系统的模型为

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = g - \frac {k}{m} x _ {2} - \frac {L _ {0} a x _ {3} ^ {2}}{2 m (a + x _ {1}) ^ {2}} \\ \dot {x} _ {3} = \frac {1}{L \left(x _ {1}\right)} \left[ - R x _ {3} + \frac {L _ {0} a x _ {2} x _ {3}}{\left(a + x _ {1}\right) ^ {2}} + u \right] \\ \end{array}
$$

其中 $x_{1}$ 是球的位置， $x_{2}$ 是其速度， $x_{3}$ 是电磁体电流(electromagnet current)。通常我们可以测得球的位置 $x_{1}$ 和电流 $x_{3}$ ，当 $(x_{1}, x_{2})$ 作为 $x$ 分量， $x_{3}$ 作为 $z$ 分量时，该模型就是方程(14.103)至方程(14.106)的形式，被测输出为 $y = x_{1}$ 和 $\zeta = x_{3}$ 。模型(14.103)～(14.106)的另一来源出现在通过附加积分器扩展动态特性的系统中，此时方程(14.106)是有意义的。例13.8是一个 $n$ 阶微分方程表示的系统，在输入端附加 $m$ 个积分器后扩展了动态特性。观察得到的状态模型说明，当 $z$ 作为 $m$ 个积分器的状态， $x$ 作为输出及其直到 $(n - 1)$ 阶导数时，该模型与模型(14.103)～(14.106)的形式相同，在这种情况下，全部向量 $z$ 是可测的，且方程(14.106)为 $\zeta = z$ 。

下面用两步法设计输出状态反馈控制器。首先用 $x$ 和 $\zeta$ 的测量值设计部分状态反馈控制器，使原点实现渐近稳定，然后采用高增益观测器由 $y$ 估计 $x$ 。状态反馈控制器可以是如下形式的动力学系统
