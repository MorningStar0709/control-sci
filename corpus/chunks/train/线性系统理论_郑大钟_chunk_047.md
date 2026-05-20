$$
\left\{ \begin{array}{l} (A - \lambda_ {i} I) ^ {k - 1} v _ {i} ^ {(k - 1)} = (A - \lambda_ {i} I) ^ {k} v _ {i} = 0 \\ (A - \lambda_ {i} I) ^ {k - 1} v _ {i} ^ {(k - 2)} = (A - \lambda_ {i} I) (A - \lambda_ {i} I) ^ {k} v _ {i} = 0 \\ \dots \dots \\ (A - \lambda_ {i} I) ^ {k - 1} v _ {i} ^ {(1)} = (A - \lambda_ {i} I) ^ {k - 2} (A - \lambda_ {i} I) ^ {k} v _ {i} = 0 \end{array} \right. \tag {1.72}
$$

就可由(1.71)导出

$$\beta_ {k} (A - \lambda_ {i} I) ^ {k - 1} v _ {i} ^ {(k)} = \beta_ {k} (A - \lambda_ {i} I) ^ {k - 1} v _ {i} = 0 \tag {1.73}$$

但已知 $(A - \lambda_{i}I)^{k - 1}\pmb{v}_{i}\neq \mathbf{0}$ ，从而只能有 $\beta_{k} = 0$ 。利用同样的步骤，当将(1.71)乘以 $(A - \lambda_{i}I)^{k - 2}$ 时可以导出 $\beta_{k - 1} = 0$ ，当将(1.71)乘以 $(A - \lambda_{i}I)^{k - 3}$ 时可以导出 $\beta_{k - 2} = 0$ 如此等等。这样，就证得了 $\beta_{k} = \beta_{k - 1} = \dots = \beta_{k} = 0$ 。于是，证明完成。

性质 2 设 $\lambda_{i}$ 为 A 的代数重数为 $\sigma_{i}$ 的特征值, 计算秩

$$\operatorname{rank} (A - \lambda_ {i} I) ^ {m} = n - v _ {m}, m = 0, 1, 2, \dots \tag {1.74}$$

直到 $m = m_0$ 且 $\nu_{m_0} = \sigma_i$ 为止。再按如下方式生成广义特征向量链（为不使符号过于复杂，假定 $n = 10, \sigma_i = 8, m_0 = 4$ ，且设 $\nu_0 = 0, \nu_1 = 3, \nu_2 = 6, \nu_3 = 7, \nu_4 = 8)$ ：

<table><tr><td> $\nu_{4}-\nu_{3}=1$ </td><td> $\nu_{3}-\nu_{2}=1$ </td><td> $\nu_{2}-\nu_{1}=3$ </td><td> $\nu_{1}-\nu_{0}=3$ </td></tr><tr><td rowspan="3"> $v_{i1}^{(4)}\triangleq v_{i1}$ </td><td rowspan="3"> $v_{i1}^{(3)}\triangleq(A-\lambda_{i}l)v_{i1}$ </td><td> $v_{i3}^{(2)}\triangleq v_{i3}$ </td><td> $v_{i3}^{(1)}\triangleq(A-\lambda_{i}l)v_{i3}$ </td></tr><tr><td> $v_{i2}^{(2)}\triangleq v_{i2}$ </td><td> $v_{i2}^{(1)}\triangleq(A-\lambda_{i}l)v_{i2}$ </td></tr><tr><td> $v_{i1}^{(2)}\triangleq(A-\lambda_{i}l)^{2}v_{i1}$ </td><td> $v_{i1}^{(1)}\triangleq(A-\lambda_{i}l)^{2}v_{i1}$ </td></tr></table>

其中， $v_{i1}$ 为满足

$$(A - \lambda_ {i} I) ^ {4} v _ {i 1} = 0 \text {和} (A - \lambda_ {i} I) ^ {3} v _ {i 1} \neq 0$$

的非零列向量， $v_{i2}$ 和 $v_{i3}$ 为满足

$\{v_{i1}^{(2)}, v_{i2}, v_{i3}\}$ 线性无关

$$(A - \lambda_ {i} I) ^ {2} v _ {i 2} = 0 \text {和} (A - \lambda_ {i} I) v _ {i 2} \neq 0(A - \lambda_ {i} I) ^ {2} v _ {i 3} = 0 \text {和} (A - \lambda_ {i} I) v _ {i 3} \neq 0$$

的列向量。则如表所生成的 $\sigma_{i}$ 个广义特征向量

$$\left\{\boldsymbol {v} _ {i 1} ^ {(k)}, k = 1, 2, 3, 4, \boldsymbol {v} _ {i 2} ^ {(j)}, \boldsymbol {v} _ {i 3} ^ {(j)}, j = 1, 2 \right\}$$

必是线性无关的；或推广为更一般的情况， $\sigma_{i}$ 个广义特征向量
