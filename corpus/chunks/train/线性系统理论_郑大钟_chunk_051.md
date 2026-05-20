# 1.5 由状态空间描述导出传递函数矩阵

对于多输入-多输出线性定常系统，传递函数矩阵是表征系统输出-输入特性的最基本的形式。本节中，我们从系统的状态空间描述出发，来导出系统的传递函数矩阵。也就是，从另一个角度，来揭示状态空间描述和输入-输出描述间的关系。但是，这两种描述间的更为深刻的关系，只有在研究了系统的能控性和能观测性后，才能得到完全的揭示。这方面的讨论，将在第3章中给出。

传递函数矩阵 考察多输入-多输出的线性定常系统，令输入变量组为 $\{u_{1}, u_{2}, \cdots, u_{p}\}$ ，输出变量组为 $\{y_{1}, y_{2}, \cdots, y_{q}\}$ ，且假设系统的初始条件为零。用 $\hat{y}_{i}(s)$ 和 $\hat{u}_{j}(s)$ 分别表示 $y_{i}$ 和 $u_{j}$ 的拉普拉斯变换， $g_{ij}(s)$ 表示系统的由第 j 个输入端到第 i 个输出端的传递函数，其中 $i = 1, 2, \cdots, q, j = 1, 2, \cdots, p$ ，那么由系统的线性属性（即满足叠加原理）可以导出：

$$
\left\{ \begin{array}{l} \hat {y} _ {1} (s) = g _ {1 1} (s) \hat {u} _ {1} (s) + g _ {1 2} (s) \hat {u} _ {2} (s) + \dots + g _ {1 p} (s) \hat {u} _ {p} (s) \\ \hat {y} _ {2} (s) = g _ {2 1} (s) \hat {u} _ {1} (s) + g _ {2 2} (s) \hat {u} _ {2} (s) + \dots + g _ {2 p} (s) \hat {u} _ {p} (s) \\ \dots \dots \\ \hat {y} _ {q} (s) = g _ {q 1} (s) \hat {u} _ {1} (s) + g _ {q 2} (s) \hat {u} _ {2} (s) + \dots + g _ {q p} (s) \hat {u} _ {p} (s) \end{array} \right. \tag {1.79}
$$

其向量方程的形式则为：

$$
\begin{array}{r l} \hat {\mathcal {Y}} (s) & \triangleq \left[ \begin{array}{c} \hat {\mathcal {Y}} _ {1} (s) \\ \vdots \\ \hat {\mathcal {Y}} _ {q} (s) \end{array} \right] = \left[ \begin{array}{c c c} g _ {1 1} (s) & \dots & g _ {1 p} (s) \\ \vdots & & \vdots \\ g _ {q 1} (s) & \dots & g _ {q p} (s) \end{array} \right] \left[ \begin{array}{c} ^ {1} \hat {u} _ {1} (s) \\ \vdots \\ \hat {u} _ {p} (s) \end{array} \right] \\ & = G (s) \hat {\boldsymbol {u}} (s) \end{array} \tag {1.80}
$$

我们称由上式所定义的 $G(s)$ 为系统的传递函数矩阵。容易看出， $G(s)$ 为 $q \times p$ 的一个有理分式矩阵。并且，当 $G(s)$ 的元传递函数 $g_{ij}(s) (i = 1, 2, \cdots, q, j = 1, 2, \cdots, p)$ 除严格真外还包含真有理分式时，即它的一个或一些元传递函数中分母和分子多项式具有相等的最高幂次时，称 $G(s)$ 为真有理分式矩阵；而当 $g_{ij}(s)$ 均为严格真有理分式时，即 $g_{ij}(s)$ 的分子多项式的最高幂次均小于分母多项式时，称 $G(s)$ 为严格真有理分式矩阵。通常，当且仅当 $G(s)$ 为真的或严格真的时，它才是物理上可以实现的。作为一个判别准则，当且仅当成立

$$\lim _ {s \rightarrow \infty} G (s) = \text {零阵} \tag {1.81}$$

或

$$\lim _ {s \rightarrow \infty} G (s) = \text { 非零常阵 } \tag {1.82}$$

时，相应的传递函数矩阵 $G(s)$ 为严格真的或真的。

传递函数矩阵的 $(A, B, C, D)$ 表示的基本关系式 现在，我们来导出由状态空间描述的系数矩阵所表示的 $G(s)$ 的关系式。

结论 对应于状态空间描述

$$
\left\{ \begin{array}{l} \dot {x} = A x + B u, x (0) = 0 \\ y = C x + D u \end{array} \right. \tag {1.83}
$$

的传递函数矩阵为

$$G (s) = C (s I - A) ^ {- 1} B + D \tag {1.84}$$

并且，当 $D \neq 0$ 时 $G(s)$ 为真的，而当 $D = 0$ 时 $G(s)$ 为严格真的，且有

$$\lim _ {s \rightarrow \infty} G (s) = D \tag {1.85}$$

证 对(1.83)作拉普拉斯变换,可导出
