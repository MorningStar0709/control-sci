# 8.7 传递函数矩阵的亏数

在单输入-单输出系统的分析中曾经指出过，对于标量传递函数 $g(s)$ ，满足一个很好的结构性质：

$g(s)$ 在有限处和无穷远处的极点总数

$$= g (s) \text {在有限处和无穷远处的零点总数} \tag {8.98}$$

著名的根轨迹法正是由于这一性质而变得比较简单和易于分析。但是，对于多输入-多输出系统，其传递函数矩阵一般不再有上述结构性质（8.98）；传递函数矩阵的奇异性，是导致特性(8.98)不再成立的原因。本节中，我们通过引入亏数的概念，使得仍可对传递函数矩阵建立起类似于(8.98)的平衡关系式。

亏数的定义 给定 $q \times p$ 的传递函数矩阵 $G(s)$ , 令其秩为 $\operatorname{rank} G(s) = r$ , 则 $G(s)$ 的亏数定义为 $G(s)$ 在复数平面 $\mathcal{C}$ 上的有限处和无穷远处的第 $r$ 阶评价值 $\nu_{\alpha}^{(r)}(G)$ 的代数和取负值, 即

$$G (s) \text {的亏数} = \mathrm{def} G (s) \triangleq - \sum_ {a \in \mathcal {V}} v _ {a} ^ {(r)} (G) \tag {8.99}$$

考虑到在 $\mathcal{C}$ 的非极点和非零点处，必有评价值为零，因此 $G(s)$ 的亏数实际上也就是 $G(s)$ 在其有限极点零点和无穷远处极点零点上的第 $r$ 阶评价值的代数和取负值。

关于亏数的一个基本结论 在下面给出的结论中，我们把传递函数矩阵的亏数与其极点和零点的个数联系起来，建立了类似于(8.98)的一个平衡关系式。

结论 给定 $q \times p$ 的传递函数矩阵 $G(s)$ , $\operatorname{rank} G(s) = r$ , 则必成立

$$\mathrm{def} G (s) = \{G (s) \text {的有限极点和无穷远极点的总数} \}- \{G (s) \text {的有限零点和无穷远零点的总数} \} \tag {8.100}$$

证 对给定 $G(s)$ ，可导出其史密斯-麦克米伦形为

$$
M (s) = U (s) G (s) V (s) = \left[ \prod_ {i = 1} ^ {l} \left[ \begin{array}{c c c c} (s - \alpha_ {i}) ^ {\sigma_ {1} (\alpha_ {i})} & & & \\ & \ddots & & \\ & & \ddots & \\ & & & (s - \alpha_ {i}) ^ {\sigma_ {r} (\alpha_ {i})} \end{array} \right] \left| \begin{array}{l} 0 \\ 0 \end{array} \right. \right] \tag {8.101}
$$

并且， $G(s)$ 在 $\alpha_{i}$ 处的结构指数 $\{\sigma_k(\alpha_i)\}$ 和 $G(s)$ 在 $\alpha_{i}$ 处的评价值 $\{\nu_{\alpha_i}^{(k)}(G)\}$ 之间，有如下的关系式：

$$
\left\{ \begin{array}{l} \sigma_ {1} (\alpha_ {i}) = v _ {\alpha_ {i}} ^ {(1)} (G) \\ \sigma_ {2} (\alpha_ {i}) = v _ {\alpha_ {i}} ^ {(2)} (G) - v _ {\alpha_ {i}} ^ {(1)} (G) \\ \dots \dots \\ \sigma_ {r} (\alpha_ {i}) = v _ {\alpha_ {i}} ^ {(r)} (G) - v _ {\alpha_ {i}} ^ {(r - 1)} (G) \end{array} \right. \tag {8.102}
$$

现将其改写之，又有

$$
\left\{ \begin{array}{l} v _ {a _ {i}} ^ {(1)} (G) = \sigma_ {1} (\alpha_ {i}) \\ v _ {a _ {i}} ^ {(2)} (G) = \sigma_ {1} (\alpha_ {i}) + \sigma_ {2} (\alpha_ {i}) \\ \dots \dots \\ v _ {a _ {i}} ^ {(r)} (G) = \sum_ {k = 1} ^ {r} \sigma_ {k} (\alpha_ {i}) \end{array} \right. \tag {8.103}
$$

但据结构指数的含义知， $\sigma_{k}(\alpha_{i})$ 为正整数表示 $G(s)$ 在 $\alpha_{i}$ 处的零点个数， $\sigma_{k}(\alpha_{i})$ 为负整数表示 $G(s)$ 在 $\alpha_{i}$ 处的极点个数。因此，用 $\sigma_{k}^{+}(\alpha_{i})$ 和 $\sigma_{k}^{-}(\alpha_{i})$ 分别表示为正整数和负整数的结构指数，则由(8.103)可进一步导出
