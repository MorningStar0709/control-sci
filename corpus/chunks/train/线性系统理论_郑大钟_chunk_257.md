由 $D(s)$ 和 $N(s)$ 为非右互质，表明其 $\gcd R(s)$ 不是单模阵，因而有 $\deg \det R(s) > 0$ 。再由(6.53)还可导出

$$\det D (s) = \det V _ {1 1} (s) \det R (s) \tag {6.62}$$

且相应地有

$$\deg \det D (s) = \deg \det V _ {1 1} (s) + \deg \det R (s) \tag {6.63}$$

但前已证得 $\deg \det V_{\mathbb{R}}(s) = \deg \det A(s)$ ，且注意到 $\deg \det R(s) > 0$ ，故由(6.63)即可得到(6.49)。

(4) 已知式(6.49)成立, 欲证 $D(s)$ 和 $N(s)$ 为非右互质。

已知 $\deg \det D(s) > \deg \det A(s)$ ，且前已导出 $\deg \det A(s) = \deg \det V_{11}(s)$ 和 $\deg \det D(s) = \deg \det V_{11}(s) + \deg \det R(s)$ ，故即可得到

$$\deg \det R (s) = \deg \det D (s) - \deg \det A (s) > 0 \tag {6.64}$$

这表明 $R(s)$ 不是单模阵，从而证明了 $D(s)$ 和 $N(s)$ 为非右互质。由此证明完成。

举例 给定多项式矩阵 $D(s)$ 和 $N(s)$ 如下:

$$
D (s) = \left[ \begin{array}{c c} s + 1 & 0 \\ (s - 1) (s + 2) & s - 1 \end{array} \right], N (s) = [ s - 1 ]
$$

现应用秩判据来判断它们是否为右互质。为此，先组成下述判别矩阵：

$$
\left[ \begin{array}{c} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c c} s + 1 & 0 \\ (s - 1) (s + 2) & s - 1 \\ s & 1 \end{array} \right]
$$

进而，分别来定出使上述矩阵中各个 $2 \times 2$ 的多项式矩阵降秩的 $s$ 值：

对 $\left[ \begin{array}{cc}s + 1 & 0\\ (s - 1)(\epsilon +2) & s - 1 \end{array} \right]$ ，使其降秩的 $s$ 值为-1，1

对 $\left[ \begin{array}{cc}(s - 1)(s + 2) & s - 1\\ s & 1 \end{array} \right],$ 使其降秩的 $s$ 值为1

对 $\left[ \begin{array}{cc} s + 1 & 0 \\ s & 1 \end{array} \right]$ ，使其降秩的 $s$ 值为-1

这表明,不存在一个 $s$ 值,同时使上述3个 $2 \times 2$ 的多项式矩阵均降秩。由此,即知对给定的 $D(s)$ 和 $N(s)$ ,满足条件

$$
\operatorname{rank} \left[ \begin{array}{c} D (s) \\ N (s) \end{array} \right] = p = 2, \forall s \in \mathcal {C}
$$

因而，它们是右互质的。

gcrd 构造关系式的一个性质 根据上面的讨论结果,我们还可以进一步来导出 gcrd 的构造关系式的一个有意义的性质。现将其表述为如下的结论:

结论 对 gcrd 的构造关系式

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{l l} U _ {1 1} (s) & U _ {1 2} (s) \\ U _ {2 1} (s) & U _ {2 2} (s) \end{array} \right] \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] \tag {6.65}
$$

其中设 $D(s)$ 为非奇异，则下列论断必成立：

(1) $U_{22}(s)$ 和 $U_{21}(s)$ 为左互质。

(2) $U_{22}(s)$ 为非奇异，且成立 $N(s)D^{-1}(s) = -U_{22}^{-1}(s)U_{21}(s)$ .

(3) $D(s)$ 和 $N(s)$ 为右互质，当且仅当 $\deg \det D(s) = \deg \det U_{2}(s)$ .

证 (1) 设 $D(s)$ 和 $N(\varepsilon)$ 分别为 $p \times p$ 和 $q \times p$ 的多项式矩阵, 则 $U(s)$ 为 $(p + q) \times (p + q)$ 的单模阵, 因此必有

$$\operatorname{rank} U (s) = p + q, \quad \forall s \in \mathcal {C} \tag {6.66}$$

这意味着进而又有

$$\operatorname{rank} \left[ U _ {2 1} (s) U _ {2 2} (s) \right] = q, \forall s \in \mathcal {C} \tag {6.67}$$
