于是，根据定义，可知由(6.23)所导出的 $R(s)$ 为 $D(s)$ 和 $N(s)$ 的一个 $\mathbf{gcrd}_{\circ}$ 证明完成。

考虑到对一个多项式矩阵左乘单模阵等价于对其进行一系列的行初等运算，因此由结构定理可知，多项式矩阵 $D(s)$ 和 $N(s)$ 的一个 $\gcd R(s)$ 可通过对矩阵 $[D^T(s), N^T(s)]^T$ 的行初等变换来得到，而相应于各初等运算的初等矩阵按逆顺序的乘积阵则为所找的单模阵 $U(s)$ 。

例 给定两个多项式矩阵如下

$$
D (s) = \left[ \begin{array}{c c} s & 3 s + 1 \\ - 1 & s ^ {2} + s - 2 \end{array} \right], N (s) = [ - 1, s ^ {2} + 2 s - 1 ]
$$

则其 $\gcd R(s)$ 可按如下的方式来定出：

$$
\left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c c} s & 3 s + 1 \\ - 1 & s ^ {2} + s - 2 \\ - 1 & s ^ {2} + 2 s - 1 \end{array} \right] \xrightarrow [ E _ {a} ]{\text {交换行} 1 \text {和行} 2} \left[ \begin{array}{c c} - 1 & s ^ {2} + s - 2 \\ s & 3 s + 1 \\ - 1 & s ^ {2} + 2 s - 1 \end{array} \right]

\frac {s \times \text {行} 1 \text {加到行} 2 , (E _ {b})}{(- 1) \times \text {行} 1 , (E _ {d})} \xrightarrow [ (- 1) \times \text {行} 1 \text {加到行} 3 , (E _ {c}) ]{} \left[ \begin{array}{l l} 1 & - s ^ {2} - s + 2 \\ 0 & s ^ {3} + s ^ {2} + s + 1 \\ 0 & s + 1 \end{array} \right] \xrightarrow [ E _ {e} ]{\text {交换行} 2 \text {和行} 3}

\left[ \begin{array}{c c} 1 & - s ^ {2} - s + 2 \\ 0 & s + 1 \\ 0 & s ^ {3} + s ^ {2} + s + 1 \end{array} \right] \xrightarrow [ E _ {f} ]{- (s ^ {2} + 1) \times \text {行} 2 \text {加到行} 3} \left[ \begin{array}{c c} 1 & - s ^ {2} - s + 2 \\ 0 & s + 1 \\ \hline 0 & 0 \end{array} \right]
$$

由此，可得

$$
R (s) = \left[ \begin{array}{c c} 1 & - s ^ {2} - s + 2 \\ 0 & s + 1 \end{array} \right]
$$

而相应的单模变换阵则为

$$
\begin{array}{l} U (s) = E _ {f} E _ {c} E _ {d} E _ {c} E _ {b} E _ {a} \\ = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & - (s ^ {2} + 1) & 1 \end{array} \right] \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c c c} - 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \\ \times \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} 1 & 0 & 0 \\ s & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right] \\ \end{array}

= \left[ \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & - 1 & 1 \\ 1 & s ^ {2} + s + 1 & - (s ^ {2} + 1) \end{array} \right]
$$

gcrd 的性质 从 gcrd 的定义和构造定理出发, 可以导出 gcrd 具有如下一些重要属性。

性质1 gcrd 的不唯一性：设 $R(s)$ 为具有相同列数 $\pmb{p}$ 的两个多项式矩阵 $D(s)$ 和 $N(s)$ 的一个 gcrd, $W(s)$ 为任一 $\pmb{p}$ 维单模阵，则 $W(s)R(s)$ 也必是 $D(s)$ 和 $N(s)$ 的一个 gcrd。

证 根据构造定理,有

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] \tag {6.30}
$$

其中 $R(s)$ 为 $\mathbf{gcd}$ 。现构造如下的单模阵
