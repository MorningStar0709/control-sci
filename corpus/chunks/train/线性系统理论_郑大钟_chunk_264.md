的首1多项式，则上述最后得到的矩阵(6.106)就即为史密斯形 $\Lambda(s)$ 。如果不是的话，则将非首 $1\lambda_{i}^{*}(s)$ 的行用其首系数相除，且进而作相应的行和列交换使之满足整除性，从而可得到由式(6.99)所表述的史密斯形 $\Lambda(s)$ 。

例 确定下面给出的多项式矩阵 $Q(s)$ 为它的史密斯形。其确定过程如下：

$$
\begin{array}{l} Q (s) = \left[ \begin{array}{c c c} s ^ {2} + 9 s + 8 & 4 & s + 3 \\ 0 & s + 3 & s + 2 \end{array} \right] \xrightarrow {\text {交换列1与列2}} \\ \left[ \begin{array}{c c c} 4 & s ^ {2} + 9 s + 8 & s + 3 \\ s + 3 & 0 & s + 2 \end{array} \right] \xrightarrow {\text {行} 2 ^ {n} - \text {行} 1 \times 0 . 2 5 (s + 3) ^ {n}}: \\ \left[ \begin{array}{c c c} 4 & s ^ {2} + 9 s + 8 & s + 3 \\ 0 & - 0. 2 5 (s ^ {2} + 9 s + 8) (s + 3) & (s + 2) - 0. 2 5 (s + 3) ^ {2} \end{array} \right] \\ \frac {“ \text {列} 2 ” - “ \text {列} 1 \times 0 . 2 5 (s ^ {2} + 9 s + 8) ”}{“ \text {列} 3 ” - “ \text {列} 1 \times 0 . 2 5 (s + 3) ”} \\ \left[ \begin{array}{c c c} 4 & 0 & 0 \\ 0 & - 0. 2 5 (s ^ {2} + 9 s + 8) (s + 3) & (s + 2) - 0. 2 5 (s + 3) ^ {2} \end{array} \right] \\ \xrightarrow {\text {交换列} 2 \text {与列} 3} \left[ \begin{array}{c c c} 4 & 0 & 0 \\ 0 & - 0. 2 5 (s + 1) ^ {2} & - 0. 2 5 (s + 1) (s + 3) (s + 8) \end{array} \right] \\ \end{array}

\begin{array}{l} ^ {a} \text { 列 } 3 ^ {n} - ^ {a} \text { 列 } 2 \times (s + 1 0) ^ {n} \\ \left[ \begin{array}{c c c} 4 & 0 & 0 \\ 0 & - 0. 2 5 (s + 1) ^ {2} & - 3. 5 (s + 1) \end{array} \right] \xrightarrow {\text {交换列} 2 \text {与列} 3} \\ \left[ \begin{array}{c c c} 4 & 0 & 0 \\ 0 & - 3. 5 (s + 1) & - 0. 2 5 (s + 1) ^ {2} \end{array} \right] \xrightarrow {\text {“列 } 3 ” - “ \text {列} 2 \times (s + 1) / 1 4 ”} \\ \left[ \begin{array}{c c c} 4 & 0 & 0 \\ 0 & - 3. 5 (s + 1) & 0 \end{array} \right] \xrightarrow {“ \text {行} 1 ^ {n} \times 1 / 4 , “ \text {行} 2 ^ {n} \times (- 1 / 3 . 5)}: \\ \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & s + 1 & 0 \end{array} \right] = \Lambda (s) \\ \end{array}
$$

对史密斯形的一些讨论 下面,我们来指出史密斯形的如下一些基本属性:

（1）在多项式矩阵 $Q(s)$ 的史密斯形 $\Lambda(s)$ 中， $\lambda_{1}(s), \lambda_{2}(s), \cdots, \lambda_{r}(s)$ 就是 $Q(s)$ 的不变多项式。并且，若令 $\Delta_{i}(s) = \gcd\{Q(s) \text{ 的所有 } i \times i \text{ 子式 }\}, i = 1, 2, \cdots, r$ ，而规定 $\Delta_{0} = 1$ ，则成立

$$\lambda_ {1} (s) = \Delta_ {1} (s) / \Delta_ {0} (s), \quad \lambda_ {2} (s) = \Delta_ {2} (s) / \Delta_ {1} (s), \dots ,\lambda_ {r} (s) = \Delta_ {r} (s) / \Delta_ {r - 1} (s) \tag {6.108}$$

证 因为 $\gcd\{Q(s)$ 的所有 $i \times i$ 子式} 和对 $Q(s)$ 所施加的初等列和行运算无关，故有

$$\mathbf {g c d} \{Q (s) \text { 的所有 } i \times i \text { 子式 } \}= \operatorname * {g c d} \{\Lambda (s) \text { 的所有 } i \times i \text { 子式 } \} \tag {6.109}$$

由此，进而可导出
