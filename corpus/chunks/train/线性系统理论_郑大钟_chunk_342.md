也即矩阵 $\begin{bmatrix} D(s) \\ \Psi(s) \end{bmatrix}$ 对所有复数平面上的 $s$ 值均为列满秩。因此，根据互质性的秩判据可知， $\Psi(s)$ 和 $D(s)$ 为右互质。于是，(9.116)得证。

(3) 最后证明(9.117)。前已证得 $(A_{c}, B_{c})$ 为完全能控，故由 PBH 秩判据可知：

$$\operatorname{rank} \left[ s I - A _ {c} \quad B _ {c} \right] = \sum_ {i = 1} ^ {p} k _ {i} = n, \forall s \in \mathcal {C} \tag {9.122}$$

也即对所有 $s \in \mathcal{C}$ , $[sI - A_c, B_c]$ 为行满秩。因此，即证得了 $\{sI - A_c, B_c\}$ 为左互质。至此，就完成了整个证明过程。

性质3 控制器形实现 $(A_{c}, B_{c}, C_{c})$ 和右MFD $N(s)D^{-1}(s)$ 之间，成立如下的关系式：

$$\det (s I - A _ {c}) = (\det D _ {b c}) ^ {- 1} \det D (s) \tag {9.123}\dim (A _ {c}) = \deg \det D (s) \tag {9.124}$$

证 由性质2知， $\{sI - A_c, B_c\}$ 为左互质， $\{\Psi(s), D(s)\}$ 为右互质。因此，根据互质性的贝佐特等式判据可知，存在多项式矩阵对 $\{X(s), Y(s)\}$ 和 $\{\bar{X}(s), \bar{Y}(s)\}$ ，使成立

$$(s I - A _ {c}) X (s) + B _ {c} Y (s) = I _ {s} \tag {9.125}\bar {X} (s) \Psi (s) + \bar {Y} (s) D (s) = I _ {p} \tag {9.126}$$

这样, 将(9.125) 和 (9.126) 连同等式

$$(s I - A _ {c}) \Psi (s) = B _ {c} D (s) \tag {9.127}$$

表示为分块矩阵形式,即有

$$
\left[ \begin{array}{c c} s I - A _ {e} & B _ {e} \\ - \bar {X} (s) & \bar {Y} (s) \end{array} \right] \left[ \begin{array}{c c} X (s) & - \Psi (s) \\ Y (s) & D (s) \end{array} \right] = \left[ \begin{array}{l l} I & 0 \\ Q (s) & I \end{array} \right] \tag {9.128}
$$

其中

$$- \bar {X} (s) X (s) + \bar {Y} (s) Y (s) \triangleq Q (s) \text {为多项式矩阵} \tag {9.129}$$

现将(9.128)左乘

$$
\left[ \begin{array}{l l} I & 0 \\ Q (s) & I \end{array} \right] ^ {- 1} = \left[ \begin{array}{l l} I & 0 \\ - Q (s) & I \end{array} \right] \tag {9.130}
$$

并定义多项式矩阵

$$\tilde {X} (s) = \bar {X} (s) + Q (s) \left(s I - A _ {c}\right) \tag {9.131}\widetilde {Y} (s) = \overline {{{Y}}} (s) - Q (s) B _ {c} \tag {9.132}$$

又可得到

$$
\left[ \begin{array}{c c} s I - A _ {c} & B _ {c} \\ - \widetilde {X} (s) & \widetilde {Y} (s) \end{array} \right] \left[ \begin{array}{l l} X (s) & - \Psi (s) \\ Y (s) & D (s) \end{array} \right] = \left[ \begin{array}{l l} I & 0 \\ 0 & I \end{array} \right] \tag {9.133}
$$

通常称(9.133)为广义贝佐特等式。而且，由(9.133)可看出，等式左边的两个矩阵均为单模矩阵。于是，进而可引入如下的单模变换

$$
\left[ \begin{array}{c c} s I - A _ {c} & B _ {c} \\ 0 & I \end{array} \right] \left[ \begin{array}{l l} X (s) & - \Psi (s) \\ Y (s) & D (s) \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ Y (s) & D (s) \end{array} \right] \tag {9.134}
$$

这表明

$$
\left[ \begin{array}{c c} s I - A _ {c} & B _ {c} \\ \mathbf {0} & I \end{array} \right] \underset {\sim} {\mathrm{s}} \left[ \begin{array}{c c} I & \mathbf {0} \\ Y (s) & D (s) \end{array} \right] \tag {9.135}
$$
