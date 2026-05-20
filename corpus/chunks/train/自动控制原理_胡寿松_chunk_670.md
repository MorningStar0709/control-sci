# (4) 线性定常系统的结构分解

系统中只要有一个状态变量不可控便称系统不可控，因而不可控系统便含有可控和不可控两种状态变量。类似地，系统中只要有一个状态变量不可观测便称系统不可观测，不可观测系统含有可观测和不可观测两种状态变量。从可控性和可观测性出发，状态变量便可分为可控可观测 $x_{\omega}$ 、可控不可观测 $x_{\omega}$ 、不可控可观测 $x_{\omega}$ 、不可控不可观测 $x_{\omega}$ 四类。由对应状态变量构成的子空间也分为四类，因而系统也对应分成了四类子系统，称为系统的结构分解，也有的参考文献称此为系统的规范分解。研究结构分解可以更明显地揭示系统的结构特性、传递特性。研究方法是选取一种特殊的线性变换，使原来的状态向量x变换成 $\left[x_{\omega}^{\mathrm{T}}\quad x_{\omega}^{\mathrm{T}}\quad x_{\omega}^{\mathrm{T}}\quad x_{\omega}^{\mathrm{T}}\right]^{\mathrm{T}}$ ，相应地使原动态方程中的A,B,C矩阵变换成某种标准构造的形式。结构分解过程可先从整个系统的可控性分解开始，将可控与不可控的状态变量分离开，继而分别对可控和不可控子系统进行可观测性分解，便可以分离出四类状态变量及四类子系统。当然，结构分解的过程也可以从系统的可观测性分解开始。下面着重介绍结构分解的方法，有关证明略去。

1）系统按可控性的结构分解。设不可控系统的动态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u}, \quad \boldsymbol {y} = \boldsymbol {C} \boldsymbol {x} \tag {9-192}$$

式中，x 为 n 维状态向量；u 为 p 维输入向量；y 为 q 维输出向量；A, B, C 为具有相应维数的矩阵。若系统可控性矩阵的秩为 $r(r < n)$ ，则可从可控性矩阵中选出 r 个线性无关的列向量 $s_{1}, s_{2}, \cdots, s_{r}$ ，另外再任意选取尽可能简单的 n - r 个 n 维列向量 $s_{r+1}, s_{r+2}, \cdots, s_{n}$ ，使它们与 $\{s_{1}, s_{2}, \cdots, s_{r}\}$ 线性无关，这样就可以构成 $n \times n$ 非奇异变换矩阵。

$$
\boldsymbol {P} ^ {- 1} = \left[ \begin{array}{l l l l l l l} s _ {1} & s _ {2} & \dots & s _ {r} & s _ {r + 1} & \dots & s _ {n} \end{array} \right]
$$

对式(9-192)进行非奇异线性变换

$$
\boldsymbol {x} = \boldsymbol {P} ^ {- 1} \left[ \begin{array}{l} \boldsymbol {x} _ {c} \\ \boldsymbol {x} _ {r} \end{array} \right] \tag {9-193}
$$

式(9-192)便变换为下列的规范形式：

$$
\left[ \begin{array}{l} \dot {\boldsymbol {x}} _ {c} \\ \dot {\boldsymbol {x}} _ {c} \end{array} \right] = \boldsymbol {P A P} ^ {- 1} \left[ \begin{array}{l} \boldsymbol {x} _ {c} \\ \boldsymbol {x} _ {c} \end{array} \right] + \boldsymbol {P B u}, \quad \boldsymbol {y} = \boldsymbol {C P} ^ {- 1} \left[ \begin{array}{l} \boldsymbol {x} _ {c} \\ \boldsymbol {x} _ {c} \end{array} \right] \tag {9-194}
$$

式中， $x_{c}$ 为 r 维可控状态子向量； $x_{\bar{c}}$ 为 n-r 维不可控状态子向量，并且

$$
\pmb {P A P} ^ {- 1} = \left[ \begin{array}{c c} {\overline {{{\pmb {A}}}} _ {1 1}} & {\overline {{{\pmb {A}}}} _ {1 2}} \\ {\overline {{{\pmb {0}}}}} & {\overline {{{\pmb {A}}}} _ {2 2}} \end{array} \right] _ {n - r \text {行}}, \quad \pmb {P B} = \left[ \begin{array}{c} {\overline {{{\pmb {B}}}} _ {1}} \\ {\overline {{{\pmb {0}}}}} \end{array} \right] _ {n - r \text {行}}
$$

$r$ 列 $n - r$ 列

p列
