$$
E (s) = \left[ \begin{array}{c c c c} \varepsilon_ {1} (s) & & & \\ & \varepsilon_ {2} (s) & & 0 \\ & & \ddots & \\ & & \varepsilon_ {r} (s) & \\ - & 0 & & 0 \end{array} \right], \quad \Psi_ {r} (s) = \left[ \begin{array}{c c c c} \psi_ {1} (s) & & & \\ & \psi_ {2} (s) & & 0 \\ & & \ddots & \\ & & \psi_ {r} (s) & \\ - & 0 & & I \end{array} \right] \tag {8.7}
$$

再据史密斯-麦克米伦形的性质可知,若取

$$N _ {0} (s) = U ^ {- 1} (s) E (s), D _ {0} (s) = V (s) \Psi_ {r} (s) \tag {8.8}$$

则 $N_0(s)D_0^{-1}(s)$ 为 $G(s)$ 的一个不可简约的右MFD。而根据两个不可简约MFD间的关系的结论又可知， $G(s)$ 的不可简约的MFD $N(s)D^{-1}(s)$ 和 $N_0(s)D_0^{-1}(s)$ 之间成

立关系式:

$$N (s) = N _ {0} (s) W (s), \quad D (s) = D _ {0} (s) W (s) \tag {8.9}$$

其中 $W(s)$ 为单模阵。于是，将(8.8)代入(8.9)，可以导出

$$N (s) = U ^ {- 1} (s) E (s) W (s), D (s) = V (s) \Psi_ {r} (s) W (s) \tag {8.10}$$

进一步，则又可得到

$$\operatorname{rank} N (s) = \operatorname{rank} E (s), \det D (s) = c \det \Psi_ {r} (s) \tag {8.11}$$

其中 $c$ 为非零常数。这样，由(8.2)和(8.3)，就有

$G(s)$ 的零点 $=\varepsilon_{i}(s)=0$ 的根， $i=1,2,\cdots,r=$ 使 $E(s)$ 降秩的 s 值 = 使 $N(s)$ 降秩的 s 值
(8.12)

$G(s)$ 的极点 $= \psi_{i}(s) = 0$ 的根， $i = 1,2,\dots ,r = \operatorname {det}\Psi_r(s) = 0$ 的根 $= \operatorname {det}D(s) = 0$ 的根 (8.13)

对于左不可简约 $\mathbf{MFD}A^{-1}(s)B(s)$ 的情况也可同理证明。从而就证得了结论。

例1 给定传递函数矩阵 $G(s) = N(s)D^{-1}(s)$ ，其中 $N(s)$ 和 $D(s)$ 分别为

$$
N (s) = \left[ \begin{array}{c c} s (s + 1) & 0 \\ 2 s + 1 & - 1 \end{array} \right], \quad D (s) = \left[ \begin{array}{c c} s ^ {3} & 0 \\ (- s + 1) (2 s + 1) & - s + 1 \end{array} \right]
$$

根据互质性的秩判据, 可判定 $\{D(s), N(s)\}$ 为右互质, 即 $N(s)D^{-1}(s)$ 为 $G(s)$ 的不可简约 MFD。因此, 可利用上述结论 1 定出: $G(s)$ 的极点为

$$\det D (s) = s ^ {3} (- s + 1) = 0$$

的根，即在 $s = 0$ 上有三个极点， $s = 1$ 上有一个极点。 $G(s)$ 的零点为使 $N(s)$ 降秩的 $s$ 值，即在 $s = 0$ 上有一个零点， $s = -1$ 上有一个零点。

例2 给定传递函数矩阵 $G(s) = A^{-1}(s)B(s)$ ，其中 $A(s)$ 和 $B(s)$ 分别为

$$
A (s) = \left[ \begin{array}{c c} s ^ {3} & 0 \\ (- s + 1) (s + 1) & - s + 1 \end{array} \right], \quad B (s) = \left[ \begin{array}{c c c} s + 1 & 0 & s - 2 \\ 0 & s - 2 & s + 1 \end{array} \right]
$$

容易判断， $A^{-1}(s)B(s)$ 为不可简约的。因此，根据上述结论1，即可定出： $G(s)$ 在 $s = 0$ 上有三个极点， $s = 1$ 上有一个极点；但是，由于不存在使 $B(s)$ 降秩的 $s$ 值，所以 $G(s)$ 没有零点。

结论2 设给定多变量系统的传递函数矩阵 $G(s)$ 是严格真的，而系统的状态空间描述为 $(A, B, C)$ ，且 $(A, B)$ 为完全能控和 $(A, C)$ 为完全能观测，则必成立

$$
G (s) \text {的极点} = \det (s I - A) = 0 \text {的根} \tag {8.14}
G (s) \text {   的零点   } = \text {   使   } \left[ \begin{array}{c c} s I - A & B \\ - C & 0 \end{array} \right] \text {   降秩的   } s \text {   值   } \tag {8.15}
$$

证 设 $N(s)D^{-1}(s)$ 为 $G(s)$ 任一不可简约 MFD, 则有 $C(sI - A)^{-1}B = N(s)D^{-1}(s)$ 。由此, 根据实现理论可知, $(sI - A)$ 和 $D(s)$ 具有相同的不变多项式, 即可以导出
