# 估计和控制问题间的对偶性

从上述的讨论中，读者可能已经注意到估计和控制问题之间存在很多的相似之处。事实上，这两个问题在数学上是等价的。这种特性称为对偶性。表7.1给出了估计和控制问题之间的对偶关系。

例如，如果用表7.1给出的对偶关系进行替换，则阿克曼控制公式(7.88)就变换为式(7.146)表示的估计器公式。我们可以用矩阵代数的知识直接证明。控制问题是选择行矩阵 $K$ ，以得到系统矩阵 $\mathbf{A} - \mathbf{B}\mathbf{K}$ 极点的期望位置；估计器问题是选择列矩阵 $L$ ，以得到 $\mathbf{A} - \mathbf{LC}$ 极点的期望位置。然而， $\mathbf{A} - \mathbf{LC}$ 的极点等于 $(\mathbf{A} - \mathbf{LC})^{\mathrm{T}} = \mathbf{A}^{\mathrm{T}} - \mathbf{C}^{\mathrm{T}}\mathbf{L}^{\mathrm{T}}$ 的极点，对这种形式而言，设计 $\pmb{L}^{\mathrm{T}}$ 与设计 $\pmb{K}$ 的方法相同。因此，对于控制问题，使用如下形式的阿克曼公式或 place 算法：

$$\mathrm{K} = \text { acker } (\mathrm{A}, \mathrm{B}, \mathrm{pc}),K = \text { place } (A, B, p c),$$

对于估计器问题，则使用

$$\mathrm{Lt} = \text { acker } \left(\mathrm{A} ^ {\prime}, \mathrm{C} ^ {\prime}, \mathrm{pe}\right),\mathrm{Lt} = \text { place } \left(\mathrm{A} ^ {\prime}, \mathrm{C} ^ {\prime}, \mathrm{pe}\right),\mathrm{L} = \mathrm{Lt} ^ {\prime},$$

表 7.1

<table><tr><td colspan="2">对偶性</td></tr><tr><td>控制</td><td>估计</td></tr><tr><td>A</td><td> $A^T$ </td></tr><tr><td>B</td><td> $C^T$ </td></tr><tr><td>C</td><td> $B^T$ </td></tr></table>

其中： $p_{c}$ 为包含期望估计器误差极点的矢量。因此，对偶性允许我们在控制问题以及估计器问题上，使用相同的设计工具。通过比较 $(A_{c}, B_{c}, C_{c})$ 和 $(A_{0}, B_{0}, C_{0})$ ，这两个三元矩阵组，也可以看出这两种标准形具有对偶性。
