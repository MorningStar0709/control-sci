其中 $\overline{A}_{ij}$ 是不能肯定为0的适当维数的矩阵．而这时式(1.3.19)可改写成

$$
\boldsymbol {A} \left[ \begin{array}{l l l l} e _ {1} & e _ {2} & \dots & e _ {n} \end{array} \right] = \left[ \begin{array}{l l l l} e _ {1} & e _ {2} & \dots & e _ {n} \end{array} \right] \overline {{\boldsymbol {A}}}.
$$

取

$$
\boldsymbol {T} = \left[ \begin{array}{c c c c} e _ {1} & e _ {2} & \dots & e _ {n} \end{array} \right].
$$

显然，它是一个非奇异矩阵．不难看出

$$\overline {{{A}}} = T ^ {- 1} A T.$$

由于 $\pmb{B}$ 的各列都在子空间 $\mathcal{X}_1$ 中，因此有

$$
\overline {{{B}}} = T ^ {- 1} B = \left[ \begin{array}{c} \overline {{{B}}} _ {1} \\ \overline {{{B}}} _ {2} \\ 0 \\ 0 \end{array} \right].
$$

又因为 $\mathcal{N}(C) \supset \mathcal{X}_{2}$ ，所以 $X_{2}$ 中的每个元都在 C 的零空间中，从而当 $i = n_{1} + 1$ ， $n_{1} + 2, \cdots, n_{1} + n_{2}$ ，或者 $i = n_{1} + n_{2} + n_{3} + 1, \cdots, n$ 时，必有 $Ce_{i} = 0$ 。所以有

$$
\overline {{{C}}} = C T = \left[ \begin{array}{l l l l} \overline {{{C}}} _ {1} & 0 & \overline {{{C}}} _ {3} & 0 \end{array} \right].
$$

不难发现，在矩阵 $\overline{A},\overline{B},\overline{C}$ 中， $\overline{A}_{11},\overline{A}_{22},\overline{A}_{33},\overline{A}_{44}$ 分别是 $n_1\times n_1,n_2\times n_2,n_3\times n_3,$ $n_4\times n_4$ 矩阵， $\overline{B}_1,\overline{B}_2,\overline{C}_1,\overline{C}_3$ 分别为 $n_1\times r,n_2\times r,m\times n_1,m\times n_3$ 矩阵，则其余的 $\overline{A}_{ij}$ 都有相应的阶数.

作坐标转换 $\overline{x} = T^{-1}x$ 于是 $\overline{x}(t)$ 按维数 $n_1, n_2, n_3, n_4$ 分成四组

$$
\overline {{{x}}} (t) = \left[ \begin{array}{l} \overline {{{x}}} _ {1} (t) \\ \overline {{{x}}} _ {2} (t) \\ \overline {{{x}}} _ {3} (t) \\ \overline {{{x}}} _ {4} (t) \end{array} \right].
$$

这时用所取的坐标转换可将系统 $(A, B, C)$ 化成所要求的代数等价形式.

最后，证明

(a) $\left(\left[ \begin{array}{cc}\overline{\pmb{A}}_{11} & 0\\ \overline{\pmb{A}}_{21} & \overline{\pmb{A}}_{22} \end{array} \right],\left[ \begin{array}{c}\overline{\pmb{B}}_1\\ \overline{\pmb{B}}_2 \end{array} \right]\right)$ 能控；

(b) $\left(\left[ \begin{array}{ll}\overline{A}_{11} & \overline{A}_{13}\\ 0 & \overline{A}_{33} \end{array} \right],[\overline{C}_1\quad \overline{C}_3]\right)$ 能观测；

(c) 子系统 $(\overline{A}_{11}, \overline{B}_1, \overline{C}_1)$ 既能控又能观测.

依定义有
