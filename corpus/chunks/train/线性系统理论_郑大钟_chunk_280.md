$$\bar {N} (s) \bar {D} ^ {- 1} (s) = N (s) W (s) \cdot W ^ {- 1} (s) D ^ {- 1} (s) = N (s) D ^ {- 1} (s) \tag {7.34}$$

表明它们分别也是 $N(s)D^{-1}(s)$ 为真的和严格真的充分必要条件。于是结论得证。

例 给定 $N(s)D^{-1}(s)$ ，其中 $N(s)$ 和 $D(s)$ 分别为

$$
N (s) = \left[ \begin{array}{c c} s & 0 \\ 2 & s + 1 \end{array} \right], D (s) = \left[ \begin{array}{c c} (s + 2) ^ {2} (s + 1) ^ {2} & - (s + 1) ^ {2} (s + 2) \\ 0 & s + 2 \end{array} \right]
$$

容易判断， $D(s)$ 为非奇异但不是列既约的，现引入单模阵 $W(s)$ 来使之为列既约，即有

$$
\bar {D} (s) = D (s) W (s) = \left[ \begin{array}{c c} (s + 2) ^ {2} (s + 1) ^ {2} & - (s + 1) ^ {2} (s + 2) \\ 0 & s + 2 \end{array} \right] \left[ \begin{array}{c c} 1 & 0 \\ s + 2 & 1 \end{array} \right]

= \left[ \begin{array}{c c} 0 & - (s + 1) ^ {2} (s + 2) \\ (s + 2) ^ {2} & s + 2 \end{array} \right]
$$

相应地，有

$$
\begin{array}{l} \bar {N} (s) = N (s) W (s) = \left[ \begin{array}{c c} s & 0 \\ 2 & s + 1 \end{array} \right] \left[ \begin{array}{c c} 1 & 0 \\ s + 2 & 1 \end{array} \right] \\ = \left[ \begin{array}{c c} s & 0 \\ s ^ {2} + 3 s + 4 & s + 1 \end{array} \right] \\ \end{array}
$$

那么，由于

$$\delta_ {c 1} \overline {{{N}}} (s) = 2 = \delta_ {c 1} \overline {{{D}}} (s) = 2\delta_ {c 2} \bar {N} (s) = 1 < \delta_ {c 2} \bar {D} (s) = 3$$

所以可知矩阵分式描述 $N(s)D^{-1}(s)$ 是真的。

对偶地, 相应于左 MFD 时判据 2 的形式则为: 令 $A(s)$ 和 $B(s)$ 分别为 $q \times q$ 和 $q \times p$ 的多项式矩阵, $A(s)$ 为非奇异但不是行既约的, 现寻找一个单模阵 $V(s)$ 使 $\overline{A}(s) = V(s)A(s)$ 为行既约, 且表 $\overline{B}(s) = V(s)B(s)$ 。则矩阵分式描述 $A^{-1}(s)B(s)$ 为真的和严格真的充分必要条件分别为

$$\delta_ {r i} \overline {{{B}}} (s) \leqslant \delta_ {r i} \overline {{{A}}} (s), j = 1, \dots , q \tag {7.35}$$

和

$$\delta_ {r i} \bar {B} (s) < \delta_ {r i} \bar {A} (s), j = 1, \dots , q \tag {7.36}$$
