# 6.14 矩阵束和克罗内克尔形

矩阵束 令 $A$ 和 $E$ 为 $p \times m$ 常数矩阵, 则形为 $(sE - A)$ 的多项式矩阵称为矩阵束。在某些系统分析问题中, 都会遇到矩阵束形式的多项式矩阵。如果 $(sE - A)$ 为正则, 当且仅当

$$p = m \text {和} \det (s E - A) \neq 0 \tag {6.145}$$

否则，就称矩阵束为奇异。对于 $p \times m$ 的两个矩阵束 $(sE - A)$ 和 $(sE - B)$ ，如果存在 $p \times p$ 和 $m \times m$ 的非奇异常数矩阵 $U$ 和 $V$ 使成立

$$U (s E - A) V = (s E - B) \tag {6.146}$$

则称 $(sE-A)$ 和 $(sE-B)$ 是严格等价的。

克罗内克尔规范形 任一矩阵束 $(sE - A)$ ，都可通过选择合适的非奇异常数变换阵 $U$ 和 $V$ ，使之化为克罗内克尔（Kronecker）形：

$$
U (s E - A) V = \left[ \begin{array}{c c c c c} L _ {\mu_ {1}} & & & & \\ & L _ {\mu_ {2}} & & & \\ & & \tilde {L} _ {\nu_ {1}} & & \\ & & & \tilde {L} _ {\nu_ {\beta}} & \\ & & & s J - I & \\ & & & & s I - F \end{array} \right] \tag {6.147}
$$

其中， $\{F,J,\{L_{\mu_i}\} ,\{\widetilde{L}_{\nu_j}\} \}$ 是唯一的，且有

① $F$ 为若当形，例如

$$
F = \left[ \begin{array}{c c c c c c} * & 1 & & & & \\ & * & 1 & & & \\ & & * & & & \\ \hline & & & \# & 1 \\ & & & & \# \end{array} \right] \tag {6.148}
$$

② $J$ 是零特征值若当形，例如

$$
J = \left[ \begin{array}{c c c c c} 0 & 1 & & & \\ & 0 & & & \\ \hline & & 0 & 1 & \\ & & & 0 & 1 \\ & & & & 0 \end{array} \right] \tag {6.149}
$$

③ $L_{\mu_i}$ 为 $\mu_i\times (\mu_i + 1)$ 矩阵，具有形式

$$
L _ {\mu_ {i}} = \left[ \begin{array}{c c c c} s & - 1 & & \\ \ddots & \ddots & & \\ & \ddots & \ddots & \\ & & s & - 1 \end{array} \right] \tag {6.150}
$$

④ $\tilde{L}_{\nu_{j}}$ 为 $(\nu_{j} + 1)\times \nu_{j}$ 矩阵，具有形式

$$
\widetilde {L} _ {y _ {j}} = \left[ \begin{array}{c c c c c c c c} & s & & & & & \\ & - 1 & \ddots & & & & \\ & & \ddots & \ddots & & & \\ & & & \ddots & \ddots & & \\ & & & & \ddots & \ddots & s \\ & & & & & \ddots & - 1 \end{array} \right] \tag {6.151}
$$

例 下列矩阵束已为克罗内克尔规范形：

![](image/8023778a851eaeb03a154a885b800994ec922a3d3b7c971676e79f91cc518019.jpg)

<details>
<summary>text_image</summary>

0 0 |s -1
    s -1 0
    0 s -1
        0 0
            s 0 0
            -1 s 0
            0 -1 s
            0 0 -1
            -1
            -1 | s
            -1
            s -2
            s -3 1
            0 s -3
</details>

几点讨论 下面,对矩阵束的克罗内克尔规范形的各组成部分,给以更深入的分析,并指出它们的直观含义。

(1) 在矩阵束的克罗内克尔形中， $\{L_{\mu_{i}},\tilde{L}_{\nu_{j}}\}$ 表征了矩阵束 $(sE-A)$ 的奇异性。并且，称 $\{\mu_{i},i=1,2,\cdots,\alpha\}$ 为右克罗内克尔指数，称 $\{\nu_{i},j=1,2,\cdots,\beta\}$ 为左克罗内克尔指数。

这个特性表明，对于 $L_{\mu_i}$ 和 $\tilde{L}_{\nu_j}$ ，分别存在非零的多项式，使成立

$$
\left[ \begin{array}{c c c c c} s & - 1 & & & \\ & s & - 1 & & \\ & \ddots & \ddots & & \\ & & \ddots & \ddots & \\ & & & s & - 1 \end{array} \right] \left[ \begin{array}{l} 1 \\ s \\ \vdots \\ s ^ {\mu_ {i}} \end{array} \right] = 0 \tag {6.152}

[ 1 s \dots s ^ {p _ {i}} ] \left[ \begin{array}{c c c c c} s & & & & \\ - 1 & s & & & \\ & - 1 & \ddots & & \\ & & \ddots & \ddots & s \\ & & & \ddots & - 1 \end{array} \right] = 0 \tag {6.153}
$$
