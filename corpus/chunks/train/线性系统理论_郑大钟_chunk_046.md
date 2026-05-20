$$
J _ {i k} = \left[ \begin{array}{c c c c} \lambda_ {i} & 1 & & \\ & \ddots & \ddots & 1 \\ & & & \lambda_ {i} \end{array} \right], - r _ {i k} \times r _ {i k} \text {阵} k = 1, 2, \dots , \alpha_ {i} \tag {1.63}
$$

这个结论表明,当系统矩阵A的特征值为各种重数的重值时,通常不可能通过变换而实现状态变量间的完全解耦,约当规范形是可能达到的最简耦合形式。在这种规范形中,每一个状态变量的方程只多和下一序号的状态变量构成耦合。

(2) 特征值的代数重数和几何重数 设 $\lambda_{i}$ 为矩阵 A 的一个特征值, 且有

$$
\left\{ \begin{array}{l} \det (\lambda I - A) = (\lambda - \lambda_ {i}) ^ {\sigma_ {i}} \beta_ {i} (\lambda) \\ \beta_ {i} \left(\lambda_ {i}\right) \neq 0 \end{array} \right. \tag {1.64}
$$

则称 $\sigma_{i}$ 为 $\lambda_{i}$ 的代数重数。再设

$$\operatorname{rank} \left(A - \lambda_ {i} I\right) = n - \alpha_ {i} \tag {1.65}$$

那么称 $\alpha_{i}$ 为 $\lambda_{i}$ 的几何重数。从约当规范形(1.61)—(1.63)可以看出， $\lambda_{i}$ 的几何重数 $\alpha_{i}$ 即为其约当小块的个数，而 $\lambda_{i}$ 的代数重数 $\sigma_{i}$ 则是所有属于 $\lambda_{i}$ 的约当小块的阶数之和即

$$\sigma_ {i} = \sum_ {k = 1} ^ {a _ {i}} r _ {i k} \tag {1.66}$$

进一步，由(1.65)可知， $\alpha_{i}$ 即为 $(A-\lambda_{i}I)$ 的零空间的维数，而 $(A-\lambda_{i}I)$ 的零空间定义为使

$$(A - \lambda_ {i} I) h = 0 \tag {1.67}$$

成立的非零向量 $\pmb{h}$ 的集合，这也就是称 $\alpha_{i}$ 为 $\lambda_{i}$ 的几何重数的由来。显然，只有当所有特征值的几何重数等于其代数重数，即

$$\alpha_ {i} = \sigma_ {i}, \quad i = 1, 2, \dots , l \tag {1.68}$$

时，由(1.61)—(1.63)给出的规范形才具有对角线规范形的形式。

（3）广义特征向量 称一个非零向量 $v_{i}$ 是矩阵 A 的属于 $\lambda_{i}$ 的 k 级广义特征向量，当且仅当

$$
\left\{ \begin{array}{l} (A - \lambda_ {i} l) ^ {k} v _ {i} = 0 \\ (A - \lambda_ {i} l) ^ {k - 1} v _ {i} \neq 0 \end{array} \right. \tag {1.69}
$$

不难看出, 当 $k = 1$ 时, 广义特征向量就等同于通常所定义的特征向量。广义特征向量有三个基本的性质:

性质1 设 $v_{i}$ 是 A 的属于 $\lambda_{i}$ 的 k 级广义特征向量，则如下定义的 k 个向量必是线性无关的：

$$
\left\{ \begin{array}{l} \boldsymbol {v} _ {i} ^ {(k)} \triangleq \boldsymbol {v} _ {i} \\ \boldsymbol {v} _ {i} ^ {(k - 1)} \triangleq (A - \lambda_ {i} I) \boldsymbol {v} _ {i} \\ \dots \dots \\ \boldsymbol {v} _ {i} ^ {(1)} \triangleq (A - \lambda_ {i} I) ^ {k - 1} \boldsymbol {v} _ {\dot {2}} \end{array} \right. \tag {1.70}
$$

并且称此向量组为长度是 k 的广义特征向量链。

证 只需证明使下式

$$\beta_ {1} \boldsymbol {v} _ {i} ^ {(1)} + \beta_ {2} \boldsymbol {v} _ {i} ^ {(2)} + \dots + \beta_ {k - 1} \boldsymbol {v} _ {i} ^ {(k - 1)} + \beta_ {k} \boldsymbol {v} _ {i} ^ {(k)} = 0 \tag {1.71}$$

成立的常数必全为零，即 $\beta_{k} = \beta_{k-1} = \cdots = \beta_{1} = 0$ 。为此，将（1.71）等式两边乘以

$(A - \lambda_{i}I)^{k - 1}$ ，并注意到
