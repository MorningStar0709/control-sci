采用反证法。反设对某个 $\lambda_{i}$ ，有 $\operatorname{rank}[\lambda_{i}I - A, B] < n$ ，则意味着 $[\lambda_{i}I - A, B]$ 为行线性相关。由此，必存在一个非零常向量 $a$ ，使成立

$$\boldsymbol {\alpha} ^ {T} \left[ \lambda_ {i} I - A, B \right] = 0 \tag {3.32}$$

考虑到问题的一般性，由上式可导出

$$\boldsymbol {\alpha} ^ {T} \boldsymbol {A} = \lambda_ {i} \boldsymbol {\alpha} ^ {T}, \quad \boldsymbol {\alpha} ^ {T} \boldsymbol {B} = 0 \tag {3.33}$$

利用(3.33)，进而有

$$\alpha^ {T} B = 0, \alpha^ {T} A B = \lambda_ {i} \alpha^ {T} B = 0, \dots , \alpha^ {T} A ^ {n - 1} B = 0 \tag {3.34}$$

于是，进一步得到

$$\boldsymbol {a} ^ {T} [ B \mid A B \mid \dots \mid A ^ {n - 1} B ] = \boldsymbol {a} ^ {T} Q _ {e} = 0 \tag {3.35}$$

但已知 $\alpha \neq 0$ ，所以欲上式成立必有

$$\operatorname{rank} Q _ {s} < n \tag {3.36}$$

这意味着系统为不完全能控，显然和已知条件相矛盾。因此，反设不成立，即(3.30)成立。考虑到 $[sI - A, B]$ 为多项式矩阵，且对复数域 $\mathcal{C}$ 上除 $\lambda_i (i = 1, 2, \cdots, n)$ 以外的所有 $\pmb{s}$ 都有 $\det(sI - A) \neq 0$ ，所以(3.30)等价于(3.31)。必要性得证。

充分性：(3.30) 成立，欲证系统为完全能控。

采用反证法,利用和上述相反的思路,即可证得论断的正确性。至此,整个结论的证明完成。

例 给定线性定常系统的状态方程为:

$$
\dot {x} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & - 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 5 & 0 \end{array} \right] x + \left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \\ 0 & 1 \\ - 2 & 0 \end{array} \right] u, n = 4
$$

可直接导出

$$
[ s I - A, B ] = \left[ \begin{array}{c c c c c c} s & - 1 & 0 & 0 & 0 & 1 \\ 0 & s & 1 & 0 & 1 & 0 \\ 0 & 0 & s & - 1 & 0 & 1 \\ 0 & 0 & - 5 & s & - 2 & 0 \end{array} \right]
$$

考虑到 $A$ 的特征值为： $\lambda_{1} = \lambda_{2} = 0, \lambda_{3} = \sqrt{5}, s_{4} = -\sqrt{5}$ ，所以只需对它们来检验上述矩阵的秩。为此，可通过计算，有：

当 $s = \lambda_1 - \lambda_2 = 0$

$$
\operatorname{rank} [ s I - A, B ] = \operatorname{rank} \left[ \begin{array}{c c c c} - 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & - 1 & 0 \\ 0 & - 5 & 0 & - 2 \end{array} \right] = 4
$$

当 $s = \lambda_{3} = \sqrt{5}$

$$
\operatorname{rank} [ s I - A, B ] = \operatorname{rank} \left[ \begin{array}{c c c c} \sqrt {5} & - 1 & 0 & 1 \\ 0 & \sqrt {5} & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & - 2 & 0 \end{array} \right] = 4
$$

当 $s = \lambda_{4} = -\sqrt{5}$

$$
\operatorname{rank} [ s I - A, B ] = \operatorname{rank} \left[ \begin{array}{c c c c} - \sqrt {5} & - 1 & 0 & 1 \\ 0 & - \sqrt {5} & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & - 2 & 0 \end{array} \right] = 4
$$

表明条件(3.30)成立,即系统为完全能控。

结论 4 [PBH 特征向量判据] 线性定常系统(3.7)为完全能控的充分必要条件是, A 不能有与 B 的所有列相正交的非零左特征向量。也即对 A 的任一特征值 $\lambda_{i}$ ，使同时满足

$$\boldsymbol {a} ^ {T} \boldsymbol {A} = \lambda_ {i} \boldsymbol {a} ^ {T}, \boldsymbol {a} ^ {T} \boldsymbol {B} = 0 \tag {3.37}$$

的特征向量 $\alpha \equiv 0$ 。

证 必要性：反设存在一个向量 $\alpha \neq 0$ ，使成立
