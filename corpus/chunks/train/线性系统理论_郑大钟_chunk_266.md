其中 $P(s)$ 和 $W(s)$ 为单模阵。用 $(sI - B)$ 左除 $P(s)$ ，用 $(sI - A)$ 右除 $W(s)$ ，又可得到

$$
\left\{ \begin{array}{l} P (s) = (s I - B) Q _ {1} (s) + U \\ W (s) = Q _ {2} (s) (s I - A) + V \end{array} \right. \tag {6.119}
$$

其中，因 $(sI - A)$ 和 $(sI - B)$ 的次数为1，故 $U$ 和 $V$ 为常数阵。现把(6.119)代入(6.118)，并将结果加以整理，进而有

$$(s I - B) \left[ Q _ {1} (s) - Q _ {2} (s) \right] (s I - A) = (s I - B) V - U (s I - A) \tag {6.120}$$

上式中，右边矩阵的次数 $\leqslant 1$ ，左边矩阵的次数 $\geqslant 2$ 。因此，欲(6.120)成立，必须 $Q_{1}(s) = Q_{2}(s)$ 。于是，可得

$$U (s I - A) = (s I - B) V \tag {6.121}$$

考虑到上式中 $s$ 和 $s^0$ 的系数阵应相等，所以还可导出

$$U = V, \quad U A = B V = B U. \tag {6.122}$$

不难看出, 如果可证得 $U$ 为非奇异, 则就即有 $A = U^{-1}BU$ , 也就是 $A$ 和 $B$ 相似。为证明 $U$ 为非奇异, 现用 $(sI - A)$ 左除 $P^{-1}(s)$ , 得到

$$P ^ {- 1} (s) = (s I - A) Q _ {3} (s) + \widetilde {U} \tag {6.123}$$

从而利用(6.118)、(6.119)和(6.123)，有

$$
\begin{array}{l} I = P (s) P ^ {- 1} (s) = P (s) \left(s I - A\right) Q _ {3} (s) + P (s) \widetilde {U} \\ = (s I - B) \left[ W (s) Q _ {3} (s) + Q _ {1} (s) \widetilde {U} \right] + U \widetilde {U} \tag {6.124} \\ \end{array}
$$

或表为

$$I - U \widetilde {U} = (s I - B) [ W (s) Q _ {3} (s) + Q _ {1} (s) \widetilde {U} ] \tag {6.125}$$

上式中，左边矩阵的次数 = 0，右边矩阵的次数 $\geqslant 1$ 。因此，欲(6.125)成立，必须等式两边均等于零阵。表明 $U\widetilde{U} = I$ ，即 U 为非奇异。由此证明完成。

利用史密斯形判断互质性 下面，我们给出根据史密斯形来判断互质性的一个结论。

结论 两个 $q \times p$ 和 $p \times p$ 的多项式矩阵 $N(s)$ 和 $D(s)$ 为右互质的充分必要条件是

$$
\left[ \begin{array}{l} {D (s)} \\ {N (s)} \end{array} \right] \text {的史密斯形为} \left[ \begin{array}{l} {I} \\ {\mathbf {0}} \end{array} \right] \tag {6.126}
$$

两个 $q \times q$ 和 $q \times p$ 的多项式矩阵 $A(s)$ 和 $B(s)$ 为左互质的充分必要条件是

$$[ A (s) B (s) ] \text { 的史密斯形为 } [ I 0 ] \tag {6.127}$$

证 限于证明右互质的结论。为此，根据最大右公因子（gcrd）的构造定理，有

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} R (s) \\ 0 \end{array} \right] = \left[ \begin{array}{l} I \\ 0 \end{array} \right] R (s) \tag {6.128}
$$

其中， $U(s)$ 为单模阵。

先证明必要性。已知 $N(s)$ 和 $D(s)$ 为右互质，故 $R(s)$ 为单模阵，而 $R^{-1}(s)$ 同样为单模阵。因此将(6.128)右乘 $R^{-1}(s)$ 即得

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] R ^ {- 1} (s) = U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] V (s) = \left[ \begin{array}{l} I \\ \mathbf {0} \end{array} \right] \tag {6.129}
$$

也即其史密斯形为

$$
\Lambda (s) = \left[ \begin{array}{l} I \\ 0 \end{array} \right] \tag {6.130}
$$

从而必要性得证。

再证明充分性。已知 $\Lambda(s) = \begin{bmatrix} I \\ 0 \end{bmatrix}$ ，表明存在单模阵 $U(s)$ 和 $V(s)$ 使成立

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] V (s) = \left[ \begin{array}{l} I \\ 0 \end{array} \right] \tag {6.131}
$$

考虑到 $V^{-1}(s)$ 也为单模阵，故将(6.131)右乘 $V^{-1}(s)$ 可得

$$
U (s) \left[ \begin{array}{l} D (s) \\ N (s) \end{array} \right] = \left[ \begin{array}{c} V ^ {- 1} (s) \\ \mathbf {0} \end{array} \right] = \left[ \begin{array}{c} R (s) \\ \mathbf {0} \end{array} \right] \tag {6.132}
$$

这意味着 $\gcd R(s) = V^{-1}(s)$ 为单模阵，因此 $D(s)$ 和 $N(s)$ 为右互质，充分性得证。

于是证明完成。
