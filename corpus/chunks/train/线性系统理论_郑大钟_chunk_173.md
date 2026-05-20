$$
\det (s I - A) = \det \left[ \begin{array}{c c c} s & 0 & 0 \\ - 1 & s + 6 & 0 \\ 0 & - 1 & s + 1 2 \end{array} \right] = s ^ {3} + 1 8 s ^ {2} + 7 2 s
$$

进而计算

$$\alpha^ {*} (s) = \prod_ {i = 1} ^ {3} (s - \lambda_ {i} ^ {*}) = (s + 2) (s + 1 - j) (s + 1 + j) = s ^ {3} + 4 s ^ {2} + 6 s + 4$$

于是，可求得

$$\bar {k} = \left[ \alpha_ {0} ^ {*} - \alpha_ {0}, \alpha_ {1} ^ {*} - \alpha_ {1}, \alpha_ {2} ^ {*} - \alpha_ {2} \right] = [ 4, - 6 6, - 1 4 ]$$

再来计算变换阵

$$
\begin{array}{l} P = \left[ A ^ {2} \boldsymbol {b}, A \boldsymbol {b}, \boldsymbol {b} \right] \left[ \begin{array}{c c c} 1 & & \\ \alpha_ {2} & 1 & \\ \alpha_ {1} & \alpha_ {2} & 1 \end{array} \right] = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ - 6 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 1 8 & 1 & 0 \\ 7 2 & 1 8 & 1 \end{array} \right] \\ = \left[ \begin{array}{c c c} 7 2 & 1 8 & 1 \\ 1 2 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \\ \end{array}
$$

并求出其逆

$$
Q = P ^ {- 1} = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & - 1 2 \\ 1 & - 1 8 & 1 4 4 \end{array} \right]
$$

从而，所要确定的反馈增益阵 $\pmb{k}$ 即为：

$$
k = \bar {k} Q = [ 4, - 6 6, - 1 4 ] \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & - 1 2 \\ 1 & - 1 8 & 1 4 4 \end{array} \right] = [ - 1 4, 1 8 6, - 1 2 2 0 ]
$$

多输入极点配置问题的算法 对于多输入情形,通常可有多种算法,用以确定极点配置问题的状态反馈增益矩阵。下面,只择其中的三种常用算法,来加以介绍。

算法Ⅰ 给定能控矩阵对 $\{A, B\}$ 和一组所期望的闭环特征值 $\{\lambda_{1}^{*}, \lambda_{2}^{*}, \cdots, \lambda_{n}^{*}\}$ ，要确定 $p \times n$ 的反馈增益矩阵 K，使成立 $\lambda_{i}(A - BK) = \lambda_{i}^{*}, i = 1, 2, \cdots, n.$

第1步：判断 $A$ 是否为循环矩阵。若否，选取一个 $p \times n$ 常阵 $K_{1}$ 使 $A - BK_{1}$ 为循环，并表 $\overline{A} = A - BK_{1}$ ；若是，则直接表 $\overline{A} = A$ 。

第2步：对循环矩阵 $\overline{A}$ ，通过适当选取一个 $p \times 1$ 实常向量 $\rho$ ，表 $b = B\rho$ 且 $\{\overline{A}, b\}$ 为能控。

第3步：对于等价单输入问题 $\{\vec{A},\pmb {b}\}$ ，利用单输入极点配置问题的算法，求出增益向量 $\pmb{k}_{\circ}$

第4步：当 $A$ 为循环时，所求的增益矩阵 $K = \rho k$ ；当 $A$ 为非循环时，所求的增益矩阵则为 $K = \rho k + K_{10}$ 。

容易看出，在这一算法中， $K_{1}$ 和 $\rho$ 的选取不是唯一的，有着一定的任意性。从工程实现的角度而言，通常总是希望使得 $K_{1}$ 和 $\rho$ 的选取以达到 K 的各个元素为尽可能地小。但是，总的来说，由这种算法得到的 K 的各反馈增益值往往偏大。

算法Ⅱ 给定条件和计算要求同前。并且为了叙述上的简便，将结合 $n = 9$ 和 $p = 3$ 的一个一般性例子，来说明算法的步骤。

第1步：把能控矩阵对 $\{A, B\}$ 化成为龙伯格规范形，例如
