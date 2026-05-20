$$\lim _ {t \rightarrow \infty} N _ {l c} (s) H _ {c} ^ {- 1} (s) = 0, \quad \lim _ {t \rightarrow \infty} D _ {l c} (s) H _ {c} ^ {- 1} (s) = 0 \tag {7.27}$$

因此，由(7.26)可进一步导出

$$\lim _ {t \rightarrow \infty} G (s) = N _ {h c} D _ {h c} ^ {- 1} \tag {7.28}$$

其中，因已假定 $D(s)$ 为列既约，故 $D_{hc}^{-1}$ 存在。此外，由已知 $\delta_{ci}N(s) \leqslant \delta_{ci}D(s)$ 可看出 $N_{bc}$ 为非零常阵，表明

$$\lim _ {s \rightarrow \infty} G (s) = N _ {b c} D _ {h c} ^ {- 1} = G _ {0} (\text {非零常阵}) \tag {7.29}$$

于是据定义即知 $N(s)D^{-1}(s)$ 为真的。类似地，也可证明在(7.19)成立下 $N(s)D^{-1}(s)$ 为严格真的。所以充分性得证。证明完成。

例 给定 $N(s)D^{-1}(s)$ ，其中 $N(s)$ 和 $D(s)$ 为

$$
N (s) = \left[ \begin{array}{c c} s ^ {2} + 2 s + 1 & 4 \\ s + 7 & 3 s ^ {2} + 7 s \\ 4 s ^ {2} + s + 2 & 6 s - 1 \end{array} \right], \quad D (s) = \left[ \begin{array}{c c} 0 & s ^ {3} + 2 s ^ {2} + s + 1 \\ s ^ {2} + 2 s + 4 & s + 2 \end{array} \right].
$$

易知 $D(s)$ 为列既约，且有

$$\delta_ {e 1} N (s) = 2 = \delta_ {e 1} D (s) = 2\delta_ {c 2} N (s) = 2 < \delta_ {c 2} D (s) = 3$$

表明给定 $N(s)D^{-1}(s)$ 为真的，但不是严格真的。

需要指出，在上述判据1中， $D(s)$ 为列既约是一个不可缺少的条件。否则，(7.18)和(7.19)就只是一个必要条件，而不是充分条件。也就是说，这时尽管(7.18)或(7.19)成立，但所要判断的 $N(s)D^{-1}(s)$ 也可能是非真的。

例 给定 $N(s)D^{-1}(s)$ ，其中 $N(s)$ 和 $D(s)$ 为

$$
N (s) = \left[ \begin{array}{l l} 1 & 2 \end{array} \right], D (s) = \left[ \begin{array}{c c} s ^ {2} & s - 1 \\ s + 1 & 1 \end{array} \right]
$$

不难看出， $D(s)$ 为非列既约。所以，尽管有

$$\delta_ {e 1} N (s) = 0 < \delta_ {e 1} D (s) = 2\delta_ {c 2} N (s) = 0 < \delta_ {c 2} D (s) = 1$$

但事实上

$$
N (s) D ^ {- 1} (s) = [ 1 \quad 2 ] \left[ \begin{array}{c c} s ^ {2} & s - 1 \\ s + 1 & 1 \end{array} \right] ^ {- 1} = [ - 2 s - 1 \quad 2 s ^ {2} - s + 1 ]
$$

显然是非真的。

对偶地, 相应于左 MFD 时判据 1 的形式则为: 令 $A(s)$ 和 $B(s)$ 分别为 $q \times q$ 和 $q \times p$ 的多项式矩阵, $A(s)$ 为行既约, 则矩阵分式描述 $A^{-1}(s)B(s)$ 为真的和严格真的充分必要条件分别为

$$\delta_ {r j} B (s) \leqslant \delta_ {r j} A (s), j = 1, \dots , q \tag {7.30}$$

和

$$\delta_ {r j} B (s) < \delta_ {r j} A (s), j = 1, \dots , q \tag {7.31}$$

判据2 $[D(s)$ 为非列既约的情况] 令 $N(s)$ 和 $D(s)$ 分别为 $q \times p$ 和 $p \times p$ 的多项式矩阵, $D(s)$ 为非奇异但不是列既约的, 现寻找一个单模阵 $W(s)$ 使 $\overline{D}(s) = D(s)W(s)$ 为列既约, 且表 $\overline{N}(s) = N(s)W(s)$ 。则矩阵分式描述 $N(s)D^{-1}(s)$ 为真的和严格真的, 当且仅当分别满足式

$$\delta_ {c i} \overline {{{N}}} (s) \leqslant \delta_ {c i} \overline {{{D}}} (s), i = 1, \dots , p \tag {7.32}$$

和

$$\delta_ {c i} \overline {{{N}}} (s) < \delta_ {c i} \overline {{{D}}} (s), i = 1, \dots , p \tag {7.33}$$

证 由判据1，可知(7.32)和(7.33)分别为 $\overline{N}(s)\overline{D}^{-1}(s)$ 为真的和严格真的充分必要条件。进而，有
