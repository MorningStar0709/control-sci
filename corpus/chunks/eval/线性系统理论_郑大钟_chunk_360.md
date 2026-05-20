PMD 中的基本假设 为保证多项式矩阵描述(10.6)有唯一解,常需假定多项式矩阵 $P(s)$ 是非奇异的,也即 $P^{-1}(s)$ 存在。这是采用 PMD 中的一个基本假设。对于从实际问题中简化得到的绝大多数线性系统而言,这个假设条件总是可以满足的。

PMD 和传递函数矩阵间的关系 给定多项式矩阵描述(10.6)，由它的第一个关系式可导出

$$\hat {\zeta} (s) = P ^ {- 1} (s) Q (s) \hat {u} (s) \tag {10.8}$$

再将其代入第二个关系式,可得到

$$\hat {\mathbf {y}} (s) = [ R (s) P ^ {- 1} (s) Q (s) + W (s) ] \hat {\mathbf {u}} (s) \tag {10.9}$$

于是，即可导出系统的传递函数矩阵 $G(s)$ 和其PMD之间的关系式为：

$$G (s) = R (s) P ^ {- 1} (s) Q (s) + W (s) \tag {10.10}$$

PMD 和状态空间描述间的关系 再来讨论系统的多项式矩阵描述和状态空间描述间的关系, 设已知状态空间描述为

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u} \\ \boldsymbol {y} = C \boldsymbol {x} + E (p) \boldsymbol {u} \end{array} \right. \tag {10.11}
$$

其中 $E(p)$ 为多项式矩阵， $p = d / dt$ 为微分算子。现令状态的初值 $\pmb{x}(0) = \pmb{0}$ 同时对(10.11)进行拉普拉斯变换，并表 $\hat{\zeta}(s) = \hat{\pmb{x}}(s)$ ，那么就可得到

$$
\left\{ \begin{array}{c} (s I - A) \hat {\zeta} (s) = B \hat {u} (s) \\ \hat {y} (s) = C \hat {\zeta} (s) + E (s) \hat {u} (s) \end{array} \right. \tag {10.12}
$$

这表明,可把状态空间描述看成为是 PMD 的一个特殊情况,其中

$$
\left\{ \begin{array}{l} P (s) = (s I - A), Q (s) = B \\ R (s) = C, W (s) = E (s) \end{array} \right. \tag {10.13}
$$

PMD 和矩阵分式描述间的关系 设系统的右 MFD 为 $N(s)D^{-1}(s) + E(s)$ , 其中 $N(s)D^{-1}(s)$ 为严格真的, 而 $E(s)$ 为多项式矩阵。于是, 由此就可导出:

$$
\begin{array}{l} \hat {\mathbf {y}} (s) = [ N (s) D ^ {- 1} (s) + E (s) ] \hat {\mathbf {u}} (s) \\ = N (s) D ^ {- 1} (s) I \hat {\boldsymbol {u}} (s) + E (s) \hat {\boldsymbol {u}} (s) \tag {10.14} \\ \end{array}
$$

现令广义状态 $\hat{\zeta}(s) = D^{-1}(s)I\hat{u}(s)$ ，那么可进一步得到：

$$
\left\{ \begin{array}{c} D (s) \hat {\zeta} (s) = \hat {\boldsymbol {u}} (s) \\ \hat {\boldsymbol {y}} (s) = N (s) \hat {\zeta} (s) + E (s) \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {10.15}
$$

表明, 右 MFD 也可看成为是 PMD 的一种特殊的形式, 其中

$$
\left\{ \begin{array}{l} P (s) = D (s), Q (s) = I \\ R (s) = N (s), W (s) = E (s) \end{array} \right. \tag {10.16}
$$

同理，对左 MFD $D_{L}^{-1}(s)N_{L}(s) + E(s)$ ，也可导出类似的 PMD 形式的表达式

$$
\left\{ \begin{array}{c} D _ {L} (s) \hat {\zeta} (s) = N _ {L} (s) \hat {\boldsymbol {u}} (s) \\ \hat {\boldsymbol {y}} (s) = \hat {\zeta} (s) + E (s) \hat {\boldsymbol {u}} (s) \end{array} \right. \tag {10.17}
$$

所以，对左 MFD，相应地有

$$
\left\{ \begin{array}{l} P (s) = D _ {L} (s), Q (s) = N _ {L} (s) \\ R (s) = I, W (s) = E (s) \end{array} \right. \tag {10.18}
$$

不可简约 PMD 称系统的多项式矩阵描述 $(P(s), Q(s), R(s), W(s))$ 是不可简约的，如果矩阵对 $\{P(s), Q(s)\}$ 为左互质，而矩阵对 $\{P(s), R(s)\}$ 为右互质。
