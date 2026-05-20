其中 $\vec{N}(s)\triangle N(s)C_o\tilde{I}_n$ 。但是，一般 $\vec{N}(s)(sI - A_{co})^{-1}$ 将不是严格真的，因而可采用矩阵除法，有

$$\bar {N} (s) = Q (s) \left(s I - A _ {c o}\right) + \bar {N} \left(A _ {c o}\right) \tag {9.183}$$

把(9.183)代入(9.182)，又可得到

$$N (s) D ^ {- 1} (s) = \bar {N} \left(A _ {c o}\right) \left(s I - A _ {c o}\right) ^ {- 1} B _ {c o} + Q (s) B _ {c o} \tag {9.184}$$

上式中，依假定等式左边是严格真的；所以，欲等式成立，就只可能有

$$Q (s) B _ {c o} = 0 \tag {9.185}$$

于是，由

$$C _ {c o} (s I - A _ {c o}) ^ {- 1} B _ {c o} = N (s) D ^ {- 1} (s) = \bar {N} (A _ {c o}) (s I - A _ {c o}) ^ {- 1} B _ {c o} \tag {9.186}$$

即可导出

$$C _ {c o} = \bar {N} (A _ {c o}) = [ N (s) C _ {o} \tilde {I} _ {s} ] _ {s \rightarrow A _ {c o}} \tag {9.187}$$

从而，就证得式(9.175)。

(2) 再来证明(9.176)。分别表

$$
A _ {c o} = \left[ \begin{array}{l l l} A _ {1 1} & \dots & A _ {1 p} \\ \vdots & & \vdots \\ A _ {p 1} & \dots & A _ {p p} \end{array} \right], B _ {c o} = \left[ \begin{array}{l} B _ {1} \\ \vdots \\ B _ {p} \end{array} \right] \tag {9.188}

A _ {o} = \left[ \begin{array}{c c c} \widetilde {A} _ {1 1} & \dots & \widetilde {A} _ {1 p} \\ \vdots & & \vdots \\ \widetilde {A} _ {p 1} & \dots & \widetilde {A} _ {p p} \end{array} \right], \quad B _ {o} = \left[ \begin{array}{c} \widetilde {B} _ {1} \\ \vdots \\ \widetilde {B} _ {p} \end{array} \right] \tag {9.189}
$$

再表

$$
\tilde {I} _ {n} = \left[ \begin{array}{c c c} \tilde {I} _ {n 1} & & \\ & \ddots & \\ & & \tilde {I} _ {n p} \end{array} \right], \quad \tilde {I} _ {n i} = \left[ \begin{array}{c c c} & & 1 \\ & \ddots & \\ 1 & & \end{array} \right] \tag {9.190}
$$

则根据(9.175)可以导出

$$A _ {i j} = \widetilde {I} _ {n i} \widetilde {A} _ {i j} \widetilde {I} _ {n j}, B _ {i} = \widetilde {I} _ {n i} \widetilde {B} _ {i} \tag {9.191}(i, j = 1, 2, \dots , p)$$

这表明， $A_{ij}$ 是由对 $\tilde{A}_{ij}$ 同时作列和行的颠倒顺序的初等变换所得到的，而 $B_{i}$ 是由对 $\tilde{B}_{i}$ 只作行的颠倒顺序的初等变换所得到的。因此，在这种初等运算下，就即可由（9.172）所示的 $\{A_{o}, B_{o}\}$ 的形式导出（9.176）的 $\{A_{co}, B_{co}\}$ 的形式。

(3) 此结论的论断②可由对 $A_{0}$ 的\*列的有关论断和(9.191)直接得出, 具体推证过程略去。至此, 我们就完成了整个证明。

例 给定右 MFD $N(s)D^{-1}(s)$ ，其中

$$
N (s) = \left[ \begin{array}{l l} s & 0 \\ - s & s ^ {2} \end{array} \right], \quad D (s) = \left[ \begin{array}{c c} 0 & - (s ^ {3} + 4 s ^ {2} + 5 s + 2) \\ (s + 2) (s + 1) & s + 2 \end{array} \right]
$$

容易判断， $N(s)D^{-1}(s)$ 是严格真的，且 $D(s)$ 是行既约的。现定出 $D(s)$ 的系数矩阵：

$$
D _ {k r} = \left[ \begin{array}{l l} 0 & - 1 \\ 1 & 0 \end{array} \right], \quad D _ {l r} = \left[ \begin{array}{c c} 0 & - 4 \\ 0 & - 5 \\ 0 & - 2 \\ - & - \\ 3 & 1 \\ 2 & 2 \end{array} \right]
$$

且通过计算可得到:
