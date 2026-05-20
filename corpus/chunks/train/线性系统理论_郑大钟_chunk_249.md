$$
\begin{array}{l} Q (s) = \left[ \begin{array}{c c} {s ^ {2}} & {0} \\ {0} & {s ^ {2}} \\ {1} & {s + 4} \end{array} \right] \xrightarrow [ E _ {a} ]{\text {行} 1 \text {和行} 3 \text {交换}} \left[ \begin{array}{c c} {1} & {s + 4} \\ {0} & {s ^ {2}} \\ {s ^ {2}} & {0} \end{array} \right] (- s ^ {2}) \times \text {行} 1 \text {加到行} 3 \\ \left[ \begin{array}{c c} {1} & {s + 4} \\ {0} & {s ^ {2}} \\ {0} & {- s ^ {2} (s + 4)} \end{array} \right] \xrightarrow [ E _ {e} ]{(s + 4) \times \text {行} 2 \text {加到行} 3} \left[ \begin{array}{c c} {1} & {s + 4} \\ {0} & {s ^ {2}} \\ {0} & {0} \end{array} \right] = Q _ {H} (s) \\ V (s) = E _ {c} E _ {b} E _ {a} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & s + 4 & 1 \end{array} \right] \left[ \begin{array}{l l l} 1 & 0 & 1 \\ 0 & 1 & 0 \\ - s ^ {2} & 0 & 1 \end{array} \right] \left[ \begin{array}{l l l} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \\ = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & s + 4 & - s ^ {2} \end{array} \right] \\ \end{array}
$$

作为验算, 将 $Q(s)$ 左乘 $V(s)$ ，可得出同样的结果:

$$
Q _ {H} (s) = V (s) Q (s) = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & s + 4 & - s ^ {2} \end{array} \right] \left[ \begin{array}{c c} s ^ {2} & 0 \\ 0 & s ^ {2} \\ 1 & s + 4 \end{array} \right] = \left[ \begin{array}{c c} 1 & s + 4 \\ 0 & s ^ {2} \\ 0 & 0 \end{array} \right]
$$

一个性质 下面我们来指出埃尔米特形的一个有用的性质,它可表述为如下的结论.

结论 设 $D(s)$ 为 $\pmb{p}$ 维非奇异多项式矩阵， $\overline{D}(s) = D(s)U(s)$ ， $U(s)$ 为任一 $\pmb{p}$ 维单模阵，则多项式矩阵 $D(s)$ 和 $\overline{D}(s)$ 具有相同的列埃尔米特形。

证 分成如下的三步来证明：

(1) 设 $D_{H}(s)$ 和 $\overline{D}_{H}(s)$ 分别为 $D(s)$ 和 $\overline{D}(s)$ 的列埃尔米特形, 则必存在单模阵 $V(s)$ 和 $\overline{V}(s)$ 使成立

$$D _ {H} (s) = D (s) V (s), \quad \overline {{{D}}} _ {H} (s) = \overline {{{D}}} (s) \overline {{{V}}} (s) \tag {6.12}$$

由此并注意到 $\overline{D}(s) = D(s)U(s)$ ，即有

$$\overline {{{D}}} _ {H} (s) = \overline {{{D}}} (s) \vec {V} (s) = D (s) U (s) \vec {V} (s) = D _ {H} (s) V ^ {- 1} (s) U (s) \vec {V} (s)$$

令 $W(s) = V^{-1}(s)U(s)\overline{V} (s)$ ，则它必为一个单模阵。因此，可得

$$\overline {{{D}}} _ {H} (s) = D _ {H} (s) W (s), W (s) \text {为单模阵} \tag {6.13}$$

(2) 考虑到 $\overline{D}_H(s)$ 和 $D_H(s)$ 均为下三角矩阵, 而由 (6.13) 可导出 $W(s) = D_H^{-1}(s) \times \overline{D}_H(s)$ , 表明 $W(s)$ 也为下三角矩阵。再注意到 $W(s)$ 为单模阵, $\det W(s)$ 为与 $s$ 无关的非零常数, 因此进一步可知 $W(s)$ 的对角元均为与 $s$ 无关的非零常数。由此, 可定出 $W(s)$ 的形式为:

$$
W (s) = \left[ \begin{array}{c c c c} c _ {1} & & & \\ w _ {2 1} (s) & c _ {2} \cdot & & \\ \vdots & & \ddots & \\ w _ {p 1} (s) & \dots \dots c _ {p} \end{array} \right] \tag {6.14}
$$

(3) 下面来证明 $W(s)$ 为单位阵, 为此由(6.13)先导出如下的关系式
