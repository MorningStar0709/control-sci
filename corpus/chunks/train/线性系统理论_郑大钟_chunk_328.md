我们来证明这一点：已知 $d(s)$ 和 $n(s)$ 不为互质，则两者有非1的公因子，设为 $(s - \lambda)$ 。于是，由此有

$$d (\lambda) = \lambda^ {n} + \alpha_ {n - 1} \lambda^ {n - 1} + \dots + \alpha_ {1} \lambda + \alpha_ {0} = 0 \tag {9.57}n (\lambda) = \beta_ {s - 1} \lambda^ {s - 1} + \dots + \beta_ {1} \lambda + \beta_ {0} = 0 \tag {9.58}$$

再定义非零列向量 $\alpha\triangleq[1,\lambda,\cdots,\lambda^{a-1}]^{T}$ ，其中“ $T^{*}$ ”表示取转置。那么，由（9.53）、(9.57)和(9.58)，可以导出：

$$
\left\{ \begin{array}{l} c \alpha = \left[ \beta_ {0}, \beta_ {1}, \dots , \beta_ {n - 1} \right] \left[ \begin{array}{c} 1 \\ \lambda \\ \vdots \\ \lambda^ {n - 1} \end{array} \right] = 0 \\ A \alpha = \left[ \begin{array}{c c c c c} 0 & 1 & \ddots & & \\ & & & 1 \\ - & - & - & - & - \\ - \alpha_ {0} & - \alpha_ {1} & \dots & - \alpha_ {n - 1} \end{array} \right] \left[ \begin{array}{c} 1 \\ \lambda \\ \vdots \\ \lambda^ {n - 1} \end{array} \right] = \lambda \left[ \begin{array}{c} 1 \\ \lambda \\ \vdots \\ \lambda^ {n - 1} \end{array} \right] = \lambda \alpha \\ A ^ {2} \alpha = \lambda A \alpha = \lambda^ {2} \alpha \\ \dots\dots\\ A ^ {n - 1} \alpha = \lambda^ {n - 1} \alpha \end{array} \right. \tag {9.59}
$$

而由(9.59)，则可进一步导出

$$
\left[ \begin{array}{c} c \\ c A \\ \vdots \\ c A ^ {n - 1} \end{array} \right] a = \left[ \begin{array}{c} c a \\ \lambda c a \\ \vdots \\ \lambda^ {n - 1} c a \end{array} \right] = 0 \tag {9.60}
$$

但 a 为非零向量, 所以(9.60)意味着, 实现(9.53)的能观测性判别阵降秩, 也即 $(A, c)$ 为不完全能观测。

④ 传递函数 $g(s)$ 的能控规范形实现可用图9.1的方块图来表述。

能观测规范形实现 给定传递函数 $g(s)$ 如（9.52）所示，则其能观测规范形实现 $(\overline{A}, \overline{b}, \overline{c})$ 为

$$
\overline {{{A}}} = \left[ \begin{array}{c c c c} 0 & - \alpha_ {0} \\ \hline 1 & & & - \alpha_ {1} \\ & \ddots & & \vdots \\ & & 1 & - \alpha_ {s - 1} \end{array} \right], \quad \overline {{{b}}} = \left[ \begin{array}{c} \beta_ {0} \\ \beta_ {!} \\ \vdots \\ \beta_ {s - 1} \end{array} \right], \quad \bar {c} = [ 0, \dots , 0, 1 ] \tag {9.61}
$$

其证明过程和能控规范形实现的证明相类同，故略去。

![](image/d06533f883d25a2e4cb7bb00bae9377502e4e3d139bc382c9a4fd5d1970b0695.jpg)

<details>
<summary>flowchart</summary>
