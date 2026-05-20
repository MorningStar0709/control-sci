我们用一个例子说明此论断的正确性。设有能控对 $\{A, B\}$ 为：

$$
A = \left[ \begin{array}{c c c c} 3 & 1 & 0 & \\ 0 & 3 & 1 & \\ 0 & 0 & 3 & \\ \hdashline & & & 2 & 1 \\ & & & 0 & 2 \end{array} \right], \quad B = \left[ \begin{array}{c c} 0 & 4 \\ 0 & 0 \\ 2 & 1 \\ \hdashline 4 & 3 \\ 2 & 0 \end{array} \right], \quad B \rho = B \left[ \begin{array}{l} \rho_ {1} \\ \rho_ {2} \end{array} \right] = \left[ \begin{array}{l} * \\ * \\ \beta \\ * \\ \varphi \end{array} \right]
$$

显见，A 是循环的。表 $B\rho$ 如上所示，其中用 \* 表示的元讨论中无需用到。利用能控性的约当形判据可知， $\{A, B\rho\}$ 为能控的充分必要条件是：

$$\beta = 2 \rho_ {1} + \rho_ {2} \neq 0, \quad \varphi = 2 \rho_ {1} \neq 0$$

这表明，除了 $\rho_{1} / \rho_{1} = -2$ 和 $\rho_{1} = 0$ 以外的所有 $\pmb{\rho}$ ，也即几乎任意的 $\pmb{\rho}, \{A, B\pmb{\rho}\}$ 为能控。（5）若 $A$ 不是循环的，但 $\{A, B\}$ 为能控，则对几乎任意的 $p \times n$ 常阵 $K, A - BK$ 为循环。

现对此论断证明如下：令 $k_{ij}$ 为 $K$ 的元，且表 $A - BK$ 的特征多项式为：

$$\alpha (s) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {5.35}$$

其中， $\alpha_{i}(i=0,1,\cdots,n-1)$ 是 $k_{ij}$ 的函数。进而，有

$$\frac {d \alpha (s)}{d s} = n s ^ {n - 1} + (n - 1) \alpha_ {n - 1} s ^ {n - 2} + \dots + \alpha_ {1} \tag {5.36}$$

显然，当 $\alpha(s)$ 包含有重根时， $\alpha(s)$ 和 $d\alpha(s)/ds$ 为非互质，即

$$
\det \left[ \begin{array}{c c c c c c c} \alpha_ {0} & \alpha_ {1} & \dots & \alpha_ {n - 1} & 1 & 0 & \dots & 0 \\ 0 & \alpha_ {0} & \dots & \alpha_ {n - 2} & \alpha_ {n - 1} & 1 & \dots & 0 \\ \vdots & \vdots & & \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & \alpha_ {0} & \alpha_ {1} & \alpha_ {2} & \dots & 1 \\ \hline \alpha_ {1} & 2 \alpha_ {2} & \dots & n & 0 & 0 & \dots & 0 \\ 0 & \alpha_ {1} & \dots (n - 1) \alpha_ {n - 1} & n & 0 & \dots & 0 \\ \vdots & \vdots & & \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & 0 & \alpha_ {1} & 2 \alpha_ {2} & \dots & n \end{array} \right] \triangleq r (k _ {i j}) = 0 \tag {5.37}
$$

再注意到 $K$ 中总共有 $p \times n$ 个元 $k_{ij}$ , 因此可以将 $\{k_{ij}\}$ 看作为 $p \times n$ 的实向量空间 $\mathcal{R}^{p \times n}$ 中的一个向量。而满足 (5.37) 的解 $\{k_{ij}\}$ 只是 $\mathcal{R}^{p \times n}$ 中的一个子空间。这表明, 对几乎所有 $K$ , 有 $\gamma(k_{ij}) \neq 0$ , 即 $\alpha(s)$ 的所有根为两两相异, 从而 $A - BK$ 为循环。由此, 证明完成。

现在,我们就可来给出相对于状态反馈的极点可配置条件。

结论 线性定常系统(5.26)可通过线性状态反馈任意地配置其全部极点的充分必要条件,是此系统为完全能控。

证 必要性：已知可配置极点，欲证 $\{A, B\}$ 为能控。采用反证法，反设 $\{A, B\}$ 不完全能控，则必可通过结构分解而导出

$$
\bar {A} = P A P ^ {- 1} = \left[ \begin{array}{l l} \bar {A} _ {c} & \bar {A} _ {1 2} \\ 0 & \bar {A} _ {s} \end{array} \right], \quad \bar {B} = P B = \left[ \begin{array}{l} \bar {B} _ {e} \\ 0 \end{array} \right] \tag {5.38}
$$

并且对任一状态反馈增益矩阵 $K = [K_1, K_2]$ ，有
