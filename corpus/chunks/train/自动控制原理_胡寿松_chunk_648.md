显然， $x_{0}$ 为状态空间中的不可观测状态。这和已知系统完全可观测相矛盾，所以反设不成立，必要性得证。至此格拉姆矩阵判据证毕。

秩判据 线性定常连续系统(9-124)完全可观测的充分必要条件是

$$
\operatorname{rank} \mathbf {V} \quad \operatorname{rank} \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ \vdots \\ \mathbf {C A} ^ {n - 1} \end{array} \right] = n \tag {9-129}
$$

或 $\operatorname{rank} V \quad \operatorname{rank}[C^T \quad A^T C^T \quad (A^T)^2 C^T \quad \cdots \quad (A^T)^{n-1} C^T] = n$ (9-130)

式(9-129)和式(9-130)中的矩阵均称为系统可观测性判别阵，简称可观测性阵。

证明 证明方法与可控性秩判据相似,在此不再详述。这里仅从式(9-126)出发,进一步论证秩判据的充分必要条件。

由式(9-126)，利用 $\mathbf{e}^{\mathbf{A}t}$ 的级数展开式(9-102)，可得

$$
\begin{array}{l} \mathbf {y} (t) = \mathbf {C e} ^ {\mathbf {A} t} \mathbf {x} _ {0} = \mathbf {C} \sum_ {m = 0} ^ {n - 1} \alpha_ {m} (t) \mathbf {A} ^ {m} \mathbf {x} _ {0} \\ = \left[ \mathbf {C} _ {\alpha_ {0}} (t) + \mathbf {C} _ {\alpha_ {1}} (t) \mathbf {A} + \dots + \mathbf {C} _ {\alpha_ {n - 1}} (t) \mathbf {A} ^ {n - 1} \right] \mathbf {x} _ {0} \\ = \left[ \begin{array}{l l l l} \alpha_ {0} (t) I _ {q} & \alpha_ {1} (t) I _ {q} & \dots & \alpha_ {n - 1} (t) I _ {q} \end{array} \right] \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] x _ {0} \tag {9-131} \\ \end{array}
$$

式中， $I_{q}$ 为 q 阶单位阵。已知 $\left[\alpha_{0}(t)\mathbf{I}_{q}\quad\cdots\quad\alpha_{n-1}(t)\mathbf{I}_{q}\right]$ 的 nq 列线性无关，于是根据测得的 $y(t)$ 可

唯一确定 $x_0$ 的充分必要条件是

$$
\operatorname{rank} \mathbf {V} = \operatorname{rank} \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ \vdots \\ \mathbf {C A} ^ {n - 1} \end{array} \right] = n
$$

这就是式(9-129)。

例 9-15 判断下列两个系统的可观测性。

$$\dot {x} = A x + B u, \quad y = C x$$

1) $A=\begin{bmatrix}-2 & 0 \\ 0 & -1\end{bmatrix}, \quad b=\begin{bmatrix}3 \\ 1\end{bmatrix}, \quad c=[1 \quad 0];$   
2) $A=\begin{bmatrix}1 & -1 \\ 1 & 1\end{bmatrix},$ $B=\begin{bmatrix}2 & -1 \\ 1 & 0\end{bmatrix},$ $C=\begin{bmatrix}1 & 0 \\ -1 & 1\end{bmatrix}.$

解 1) $\operatorname{rank} V = \operatorname{rank}[c^T - A^T c^T] = \operatorname{rank}\begin{bmatrix} 1 & -2 \\ 0 & 0 \end{bmatrix} = 1 < n = 2$ ，故系统不可观测。

2) $\operatorname{rank} V = \operatorname{rank}[C^T A^T C^T] = \operatorname{rank}\left[ \begin{array}{ccc}1 & -1 & 1 & 0 \\ 0 & 1 & -1 & 2 \end{array} \right] = 2 = n$ ，故系统可观测。

PBH 秩判据 线性定常连续系统(9-124) 完全可观测的充分必要条件是, 对矩阵 A 的所有特征值 $\lambda_{i}(i=1,2,\cdots,n)$ , 均有
