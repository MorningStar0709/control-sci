# 10.2 多项式矩阵描述的状态空间实现

PMD 的实现的定义 给定多项式矩阵描述为:

$$
\left\{ \begin{array}{c} P (s) \hat {\zeta} (s) = Q (s) \hat {u} (s) \\ \hat {y} (s) = R (s) \hat {\zeta} (s) + W (s) \hat {u} (s) \end{array} \right. \tag {10.29}
$$

则称如下的一个状态空间描述

$$
\left\{ \begin{array}{l} \dot {x} = A x + B u \\ y = C x + E (p) u \end{array} \right. \tag {10.30}
$$

为它的一个实现,如果两种描述给出同一的输出-输入关系,即成立

$$R (s) P ^ {- 1} (s) Q (s) + W (s) = C (s I - A) ^ {- 1} B + E (s) \tag {10.31}$$

对于给定的 PMD，其实现不是唯一的，而且可具有不同的维数。其中，维数最低的实现称为给定 PMD 的最小实现。最小实现就是 PMD 的同时为能控和能观测的实现。最小实现也不是唯一的，但不同的最小实现之间必定是代数等价的。

构造 PMD 的实现的算法 给定多项式矩阵描述 $(P(s), Q(s), R(s), W(s))$ ，则可运用 MFD 的实现问题的有关结果，来构造其各种形式的典型实现，诸如控制器形实现、观测器形实现、能控性形实现和能观测性形实现等。下面，我们限于观测器形实现，来

具体说明由给定 PMD 构造其实现的算法:

第1步：对给定 $\{P(s), Q(s), R(s), W(s)\}$ ，其中 $P(s), Q(s), R(s)$ 和 $W(s)$ 分别为 $m \times m, m \times p, q \times m$ 和 $q \times p$ 的多项式矩阵，判断 $P(s)$ 是否为行既约。如果 $P(s)$ 为行既约，则令 $P_r(s) = P(s)$ 和 $Q_r(s) = Q(s)$ ，且转入下一步。如果 $P(s)$ 不是行既约，则寻找一个 $m \times m$ 的单模矩阵 $M(s)$ ，使 $M(s)P(s)$ 为行既约，并且令

$$P _ {r} (s) = M (s) P (s), Q _ {r} (s) = M (s) Q (s) \tag {10.32}$$

考虑到

$$
\begin{array}{l} \hat {\boldsymbol {\zeta}} (s) = P ^ {- 1} (s) Q (s) \hat {\boldsymbol {u}} (s) = [ M (s) P (s) ] ^ {- 1} M (s) Q (s) \hat {\boldsymbol {u}} (s) \\ = P _ {r} ^ {- 1} (s) Q _ {r} (s) \hat {\boldsymbol {u}} (s) \tag {10.33} \\ \end{array}
$$

和

$$\deg \det P _ {r} (s) = \deg \det P (s) \tag {10.34}$$

所以进一步可知， $P_{r}^{-1}(s)Q_{r}(s)$ 和 $P^{-1}(s)Q(s)$ 具有等同的实现。

第2步：由于一般地说 $P_{r}^{-1}(s)Q_{r}(s)$ 不是严格真的，因此需采用矩阵除法使有

$$Q _ {r} (s) = P _ {r} (s) Y (s) + \bar {Q} _ {r} (s) \tag {10.35}$$

其中， $P_{r}^{-1}(s)\overline{Q}_{r}(s)$ 是严格真的， $Y(s)$ 为多项式矩阵。而且，由(10.33)和(10.35)，可进一步导出

$$\hat {\boldsymbol {\zeta}} (s) = \left[ P _ {r} ^ {- 1} (s) \bar {Q} _ {r} (s) + Y (s) \right] \hat {\boldsymbol {u}} (s) \tag {10.36}$$

第3步：对严格真 $P_{r}^{-1}(s)\overline{Q}_{r}(s)$ 来构造观测器形实现，表为 $(A_{o}, B_{o}, \overline{C}_{o})$ ，这可采用上一章中所指出的有关方法来完成计算。并且可知， $A_{o}$ 、 $B_{o}$ 和 $\overline{C}_{o}$ 分别为 $n \times n$ 、 $n \times p$ 和 $m \times n$ 常阵，同时成立

$$
\left\{ \begin{array}{l} \overline {{C}} _ {o} (s I - A _ {o}) ^ {- 1} B _ {o} = P _ {r} ^ {- 1} (s) \overline {{Q}} _ {r} (s) \\ \left\{A _ {o}, \overline {{C}} _ {o} \right\} \text {为完全能观测} \end{array} \right. \tag {10.37}
$$

其中 $n = \deg \det P(s)$ 。

第4步：对整个PMD，有
