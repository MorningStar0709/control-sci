$$v _ {\alpha_ {i}} ^ {(r)} (G) = \sum \sigma_ {k} ^ {+} (\alpha_ {i}) + \sum \sigma_ {k} ^ {-} (\alpha_ {i}) = \{G (s) \text {在} \alpha_ {i} \text {处的零点数} \}- \{G (s) \text {在} \alpha_ {i} \text {处的极点数} \} \tag {8.104}$$

上式中， $\alpha_{i}$ 既可为有限极点零点，也可为无穷远处极点零点。于是，根据(8.104)和亏数的定义，就即得

$$\operatorname{def} G (s) = - \sum_ {a _ {i} \in \mathcal {V}} v _ {a _ {i}} ^ {(r)} (G) = - \sum_ {a _ {i} \in \mathcal {V}} \{[ G (s) \text {在} a _ {i} \text {处的零}\text { 点数 } ] - [ G (s) \text { 在 } a _ {i} \text { 处的极点数 } ] \}= \{G (s) \text {的有限和无穷远处极点总数} \}- \{G (s) \text {的有限和无穷远处零点总数} \} \tag {8.105}$$

由此，就完成了证明。

此外，由上述结论，不难进一步导出如下的一个推论。

推论 对于多输入-多输出系统, 其传递函数矩阵 $G(s)$ 保持具有结构性质(8.98), 即其极点的全部个数等于其零点的全部个数的充分必要条件是 $G(s)$ 的亏数 $\operatorname{def} G(s) = 0$ 。

亏数和克罗内克尔指数间的关系 下面，我们进一步把传递函数矩阵的亏数和传递函数矩阵的奇异性联系起来。对此，有如下的一个结论。

结论 给定 $q \times p$ 的传递函数矩阵 $G(s)$ , $\operatorname{rank} G(s) = r$ , 则必成立

$$\mathrm{def} G (s) = \{G (s) \text {的右克罗内克尔指数之和} \} + \{G (s)\text { 的左克罗内克尔指数之和 } \} \tag {8.106}$$

证 分成三步来证明。

① 将 $q \times p$ 传递函数矩阵 $G(s)$ 表示为

$$G (s) = G _ {1} (s) G _ {2} (s) \tag {8.107}$$

其中 $G_{1}(s)$ 为满列秩的 $q \times r$ 有理分式矩阵，即有 $\operatorname{rank} G_{1}(s) = r$ ， $G_{2}(s)$ 为满行秩的 $r \times p$ 有理分式矩阵，即有 $\operatorname{rank} G_{2}(s) = r$ 。现要来证明

$$\operatorname{def} G (s) = \operatorname{def} G _ {1} (s) + \operatorname{def} G _ {2} (s) \tag {8.108}$$

根据评价值的定义,并考虑到(8.107),有

$$v _ {a} ^ {(r)} (G) = \min \left\{G _ {1} (s) G _ {2} (s) \text { 的所有 } r \times r \text { 子式的评价值 } \right\}= \min \left\{\text {所有} \left(G _ {1} (s) \text {的} r \times r \text {子式}\right) \left(G _ {2} (s) \text {的} \right. \right.r \times r \text {子式}) \text {的评价值} \} \tag {8.109}$$

显然，最小的评价值出现于次数最小的 $G_{1}(s)$ 的 $\pmb{r} \times \pmb{r}$ 子式和次数最小的 $G_{2}(s)$ 的 $\pmb{r} \times \pmb{r}$ 子式相乘的情况，因此(8.109)可进一步写成为

$$\nu_ {a} ^ {(r)} (G) = \min \{G _ {1} (s) \text { 的所有 } r \times r \text { 子式的评价值 } \}+ \min \left\{G _ {2} (s) \text { 的所有 } r \times r \text { 子式的评价值 } \right\}= \nu_ {a} ^ {(r)} (G _ {1}) + \nu_ {a} ^ {(r)} (G _ {2}) \tag {8.110}$$

然后，对所有的 $\alpha$ 求和，即得

$$\sum_ {a \in \mathcal {G}} v _ {a} ^ {(r)} (G) = \sum_ {a \in \mathcal {G}} v _ {a} ^ {(r)} \left(G _ {1}\right) + \sum_ {a \in \mathcal {G}} v _ {a} ^ {(r)} \left(G _ {2}\right) \tag {8.111}$$

从而，就证明了(8.108)。

② 要证明

$$\text { def } G _ {1} (s) = \sum_ {k = 1} ^ {\beta} v _ {k}, \text { def } G _ {2} (s) = \sum_ {l = 1} ^ {\eta} \mu_ {l} \tag {8.112}$$
