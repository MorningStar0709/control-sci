定理 11.5.5 系统 (11.5.1) 的强凝网可具有以下标准结构：标准序下的 $X_{i}$ 从左到右分为四组： $X_{I}=\{X_{1},X_{2},\cdots,X_{n_{1}}\}$ 包含的分量为能观测不能达， $X_{II}=\{X_{n_{1}+1},\cdots,X_{n_{1}+n_{2}}\}$ 为能达能观测， $X_{III}=\{X_{n_{1}+n_{2}+1},\cdots,X_{n_{1}+n_{2}+n_{3}}\}$ 为不能达不能观测， $X_{IV}=\{X_{n_{1}+n_{2}+n_{2}+1},\cdots,X_{n_{1}+n_{2}+n_{3}+n_{4}}\}$ 为能达不能观测，且 U 到 $X_{I},X_{III}$ 无弧， $X_{III},X_{IV}$ 到 Y 无弧， $X_{II}$ 到 $X_{III}$ 无弧，这里 $n_{1}+n_{2}+n_{3}+n_{4}=\omega$ .

从定理11.5.5可立即得出 $D$ 上矩阵语言描述的以下定理：

定理11.5.6 系统(11.5.1)经坐标换后，其 $\hat{A},\hat{B},\hat{C}$ 可具有以下标准结构：

$$
\widehat {\boldsymbol {A}} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} & \boldsymbol {A} _ {1 3} & \boldsymbol {A} _ {1 4} \\ \phi & \boldsymbol {A} _ {2 2} & \phi & \boldsymbol {A} _ {2 4} \\ \phi & \phi & \boldsymbol {A} _ {3 3} & \boldsymbol {A} _ {3 4} \\ \phi & \phi & \phi & \boldsymbol {A} _ {4 4} \end{array} \right], \quad \widehat {\boldsymbol {B}} = [ \phi \boldsymbol {B} _ {2} \phi \boldsymbol {B} _ {4} ], \quad \widehat {\boldsymbol {C}} = \left[ \begin{array}{c} \boldsymbol {C} _ {1} \\ \boldsymbol {C} _ {2} \\ \phi \\ \phi \end{array} \right]. \tag {11.5.4}
$$

对应于式(11.5.4)，如果把 $\pmb{X}$ 也分成与其匹配的四块： $X = [X_{1}X_{2}X_{3}X_{4}]$ ，则由定理11.5.6的证明易知

$$\left\{\left[ X _ {1} \phi \phi \phi \right] \right\} = \mathcal {R} ^ {\perp} \cap \mathcal {N} ^ {\perp},\left\{\left[ \phi X _ {2} \phi \phi \right] \right\} = \mathcal {R} \cap \mathcal {N} ^ {\perp},\left\{\left[ \phi \phi X _ {3} \phi \right] \right\} = \mathcal {N} \cap \mathcal {R} ^ {\perp},\{[ \phi \phi \phi X _ {4} ] \} = \mathcal {N} \cap \mathcal {R}. \tag {11.5.5}$$

另外，由引理11.5.3易知

$$\mathcal {N} = \bigcap_ {i = 0} ^ {n - 1} \ker A ^ {i} C.$$

由定理11.5.3易知

$$\mathcal {R} ^ {\perp} = \bigcap_ {i = 0} ^ {n - 1} \ker (B A ^ {i}) ^ {\mathbf {T}},$$

这里 $\ker C$ 表示 $XC = \phi$ 的所有 $D$ 上向量 $X$ 的集合。式(11.5.5)中四个子模依次可称为：能观测但不能达子模；能观测且能达子模；不能观测且不能达子模；不能观测但能达子模。

最后来讨论第三种也是最困难的一种能达能观测性。众所周知，环上的线性系统理论比域上的困难，因为没有除法；如今，极大代数上没有减法，极大代数上的线性代数理论还不够成熟，因而与传统线性系统理论类似的能达能观测性的研究比较困难。例如，我们可以定义与能达性有关的矩阵

$$\boldsymbol {Q} _ {N} \stackrel {\text { def }} {=} [ \boldsymbol {B} ^ {\mathrm{T}} (\boldsymbol {B A}) ^ {\mathrm{T}} \dots (\boldsymbol {B A} ^ {N - 1}) ^ {\mathrm{T}} ] ^ {\mathrm{T}}. \tag {11.5.6}$$

在 $N \to +\infty$ 时是一个 $\infty$ 行的阵，不像传统线性系统中，取 $N = n$ 就可以了。为此，我们考虑 $[1, N]$ 区间上的能达性。
