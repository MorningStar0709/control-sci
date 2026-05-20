\left. \begin{array}{c c c} \beta_ {1 7} - \gamma \beta_ {2 7} & \beta_ {1 8} - \gamma \beta_ {2 8} & \beta_ {1 9} - \gamma \beta_ {2 9} \\ \beta_ {2 7} & \beta_ {2 8} & \beta_ {2 9} \\ \alpha_ {3 1} ^ {*} - \alpha_ {3 1} & \alpha_ {3 2} ^ {*} - \alpha_ {3 2} & \alpha_ {3 3} ^ {*} - \alpha_ {3 3} \end{array} \right]
$$

且由此即可导出

$$
\overline {{A}} - \overline {{B}} \overline {{K}} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - \alpha_ {1 0} ^ {*} & - \alpha_ {1 1} ^ {*} & - \alpha_ {1 2} ^ {*} \\ \hline & & 0 & 1 \\ & & - \alpha_ {2 0} ^ {*} & - \alpha_ {2 1} ^ {*} \\ \hline & & 0 & 1 & 0 & 0 \\ & & 0 & 0 & 1 & 0 \\ & & 0 & 0 & 0 & 1 \\ & & - \alpha_ {3 0} ^ {*} & - \alpha_ {3 1} ^ {*} & - \alpha_ {3 2} ^ {*} & - \alpha_ {3 3} ^ {*} \end{array} \right]
$$

和

$$\det (s I - \overline {{{A}}} + \overline {{{B}}} \overline {{{K}}}) = \alpha_ {1} ^ {*} (s) \alpha_ {2} ^ {*} (s) \alpha_ {3} ^ {*} (s) = \prod_ {i = 1} ^ {9} (s - \lambda_ {i} ^ {*})$$

第4步：根据(3.204)-(3.206)，由给定的矩阵对 $\{A, B\}$ ，计算出变换矩阵 $S^{-1}$ 。

第5步：所求的状态反馈增益矩阵即为 $K = \bar{K}S^{-1}$ 。

这种算法的计算过程是很规范化的。计算过程中，主要的计算工作为计算变换阵 $S^{-1}$ 和导出龙伯格能控规范形 $\{\overline{A},\overline{B}\}$ 。而且，由这一算法所求得的 $K$ 中，各反馈增益元的值常比由算法I定出的结果要小很多，这是这个算法的一个优点。并且，如果龙伯格规范形 $\overline{A}$ 中对角线块阵的个数愈多，即子块的维数愈小，则这个优点就愈明显。

算法 III 已知条件和计算要求同前。但需引入一个限制条件，即 $\lambda_{i}(A) \neq \lambda_{i}^{*}, i = 1, 2, \cdots, n$ 。

第1步：任选一个 $n \times n$ 常阵 $F$ ，使得满足 $\lambda_i(F) = \lambda_i^*, i = 1, 2, \dots, n$ 。

第2步：选取一个 $p \times n$ 常阵 $\vec{K}$ ，使 $\{F, \vec{K}\}$ 为能观测。一般地说，如任意地取 $\vec{K}$ ，则可使 $\{F, \vec{K}\}$ 为能观测的概率几乎等于1。

第3步：求解矩阵方程 $AT - TF = B\bar{K}$ 。当 $A$ 和 $F$ 不具有等同的特征值时，对任意的矩阵 $\overline{K}$ , 此方程的 $n \times n$ 解阵 $T$ 存在且唯一。并且, 对于多输入情形, 解阵 $T$ 为非奇异的必要条件是 $\{A, B\}$ 为能控且 $\{F, \overline{K}\}$ 为能观测; 对于单输入情形, 则此条件也是充分的 $^{1)}$ 。

第 4 步：判断 T 是否为非奇异。如果为非奇异，转入下一步。若为奇异，返回第一步或第二步，即重新选取一个不同的 F 或 $\bar{K}$ ，且重复以上计算过程。

第5步：所求的状态反馈增益矩阵为 $K = \overline{K} T^{-1}$ 。而且，在 $T$ 为非奇异的前提下，由方程 $AT - TF = B\overline{K}$ 即可导出 $TFT^{-1} = A - B\overline{K} T^{-1} = A - BK$ ，从而成立

$$\lambda_ {i} (A - B K) = \lambda_ {i} (T F T ^ {- 1}) = \lambda_ {i} (F) = \lambda_ {i} ^ {*}, i = 1, 2, \dots , n$$

也即实现了期望的闭环极点配置。

这一算法的特点是避免了将 $\{A, B\}$ 化为能控规范形 $\{\overline{A}, \overline{B}\}$ 的过程。其主要计算步骤是找到矩阵方程 $AT - TF = B\overline{K}$ 的非奇异解阵 T。对于单输入问题，这一非奇异的解 T 将可保证求得。对于多输入问题，则常需经过几次计算，才可求得非奇异的 T。

例 给定多输入线性定常系统为规范形:
