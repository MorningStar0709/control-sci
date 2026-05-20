$$
\begin{array}{l} \mathbf {A} ^ {k} = k \mathbf {A} - (k - 1) \mathbf {I} \\ \boldsymbol {A} ^ {1 0 0} = 1 0 0 \boldsymbol {A} - 9 9 \boldsymbol {I} = \left[ \begin{array}{l l} 1 0 0 & 2 0 0 \\ 0 & 1 0 0 \end{array} \right] - \left[ \begin{array}{l l} 9 9 & 0 \\ 0 & 9 9 \end{array} \right] = \left[ \begin{array}{l l} 1 & 2 0 0 \\ 0 & 1 \end{array} \right] \\ \end{array}
$$

PBH 秩判据 线性定常连续系统(9-83)完全可控的充分必要条件是,对矩阵A的所有特征值 $\lambda_{i}(i=1,2,\cdots,n)$ ,有

$$\operatorname{rank} \left[ \lambda_ {i} \boldsymbol {I} - \boldsymbol {A} \quad \boldsymbol {B} \right] = n; \quad i = 1, 2, \dots , n \tag {9-112}$$

均成立，或等价地表示为

$$\operatorname{rank} [ s \boldsymbol {I} - \boldsymbol {A} \quad \boldsymbol {B} ] = n; \quad \forall s \in C \tag {9-113}$$

由于这一判据是由波波夫(Popov)和贝尔维奇(Belevitch)首先提出，并由豪塔斯(Hautus)最先指出其可广泛应用性，故称为PBH秩判据。

证明 必要性：已知系统完全可控，欲证式(9-112)成立。

采用反证法。反设对某个 $\lambda_{i}$ 有 $\operatorname{rank}[\lambda_i I - A \quad B] < n$ ，则意味着 $[\lambda_i I - A \quad B]$ 为行线性相关，因而必存在一个非零常数向量 $\alpha$ ，使

$$\boldsymbol {\alpha} ^ {T} \left[ \lambda_ {i} \boldsymbol {I} - \boldsymbol {A} \quad \boldsymbol {B} \right] = \boldsymbol {0} \tag {9-114}$$

成立。考虑到问题的一般性，由式(9-114)可导出

$$\boldsymbol {\alpha} ^ {T} \boldsymbol {A} = \lambda_ {i} \boldsymbol {\alpha} ^ {T}, \quad \boldsymbol {\alpha} ^ {T} \boldsymbol {B} = \mathbf {0} \tag {9-115}$$

进而可得

$$\boldsymbol {\alpha} ^ {\mathrm{T}} \boldsymbol {B} = \mathbf {0}, \quad \boldsymbol {\alpha} ^ {\mathrm{T}} \boldsymbol {A} \boldsymbol {B} = \lambda_ {i} \boldsymbol {\alpha} ^ {\mathrm{T}} \boldsymbol {B} = \mathbf {0}, \quad \dots , \quad \boldsymbol {\alpha} ^ {\mathrm{T}} \boldsymbol {A} ^ {n - 1} \boldsymbol {B} = \mathbf {0}$$

于是有

$$
\boldsymbol {\alpha} ^ {T} \left[ \begin{array}{l l l l} \boldsymbol {B} & \boldsymbol {A B} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {B} \end{array} \right] = \boldsymbol {\alpha} ^ {T} \boldsymbol {S} = \boldsymbol {0} \tag {9-116}
$$

因已知 $\pmb{\alpha} \neq \mathbf{0}$ , 所以欲使式(9-116)成立, 必有

$$\operatorname{rank} S < n$$

这意味着系统不可控，显然与已知条件相矛盾，因而此反设不成立，而式(9-112)成立。考虑到 $[sI-A-B]$ 为多项式矩阵，且对复数域C上除 $\lambda_{i}(i=1,2,\cdots,n)$ 以外的所有s均有 $\det(sI-A)\neq0$ ，所以式(9-112)等价于式(9-113)。必要性得证。

充分性: 已知式(9-112)成立, 欲证系统完全可控。

采用反证法。利用与上述相反的思路，即可证明充分性。至此，PBH秩判据证毕。

例 9-12 已知线性定常连续系统的状态方程为
