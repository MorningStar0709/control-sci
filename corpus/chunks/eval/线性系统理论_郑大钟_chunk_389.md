结论1 考虑图11.2所示的串联系统 $S_{T}$ ，设子系统的传递函数矩阵 $G_{i}(s)$ 以不可简约的矩阵分式描述的形式给出，则对 $S_{T}$ 的能控性和能观测性有如下的论断：

(i) $S_{T}$ 能控的充分必要条件为：当 $G_{i}(s) = N_{i}(s)D_{i}^{-1}(s)(i = 1,2)$ 时，是 $\{D_2(s),$ $N_{1}(s)\}$ 为左互质；当 $G_{1}(s) = D_{L1}^{-1}(s)N_{L1}(s), G_{2}(s) = N_{2}(s)D_{2}^{-1}(s)$ 时，是 $\{D_{L1}(s)D_2(s),$ $N_{L1}(s)\}$ 为左互质；当 $G_{1}(s) = N_{1}(s)D_{1}^{-1}(s), G_{2}(s) = D_{L2}^{-1}(s)N_{L2}(s)$ 时，是 $\{D_{L2}(s),$ $N_{L2}(s)N_{1}(s)\}$ 为左互质。

(ii) $S_{T}$ 能观测的充分必要条件为：当 $G_{i}(s) = D_{Li}^{-1}(s)N_{Li}(s)$ ( $i = 1,2$ ) 时，是 $\{D_{L1}(s), N_{L2}(s)\}$ 为右互质；当 $G_{1}(s) = D_{Li}^{-1}(s)N_{Li}(s)$ ， $G_{2}(s) = N_{2}(s)D_{2}^{-1}(s)$ 时，是 $\{D_{L1}(s)D_{2}(s), N_{2}(s)\}$ 为右互质；当 $G_{1}(s) = N_{1}(s)D_{1}^{-1}(s)$ ， $G_{2}(s) = D_{L2}^{-1}(s)N_{L2}(s)$ 时，是 $\{D_{1}(s), N_{L2}(s)N_{1}(s)\}$ 为右互质。

证 我们只来证明有关 $S_{T}$ 的能控性的论断 (i)，关于 $S_{T}$ 的能观测性的论断 (ii) 可根据对偶原理直接由论断 (i) 导出。下面，分别三种情况，来推证 $S_{T}$ 能控的条件。

第一种情况： $G_{i}(s) = N_{i}(s)D_{i}^{-1}(s), i = 1,2$ ，则可将其表为PMD的形式为：

$$
\left[ \begin{array}{l l} D _ {i} (s) & I _ {p i} \\ - N _ {i} (s) & 0 \end{array} \right] \left[ \begin{array}{l l} \zeta & \hat {\zeta} _ {i} (s) \\ - \hat {u} _ {i} (s) \end{array} \right] = \left[ \begin{array}{l} 0 \\ - \hat {y} _ {i} (s) \end{array} \right] \tag {11.19}
$$

考虑到串联时有 $\hat{\pmb{u}}(s) = \hat{\pmb{u}}_1(s)$ ， $\hat{\pmb{u}}_2(s) = \hat{\pmb{y}}_1(s)$ ， $\hat{\pmb{y}}(s) = \hat{\pmb{y}}_2(s)$ ，所以据此和子系统的PMD可导出串联系统 $S_T$ 的PMD方程为：

$$
\left[ \begin{array}{c c c c} D _ {1} (s) & 0 & 0 & I _ {p _ {1}} \\ 0 & D _ {2} (s) & I _ {p _ {2}} & 0 \\ - N _ {1} (s) & 0 & - I _ {p _ {2}} & 0 \\ \hdashline 0 & - N _ {2} (s) & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \hat {\zeta} _ {1} (s) \\ \hat {\zeta} _ {2} (s) \\ - \hat {\mathbf {y}} _ {1} (s) \\ - \hat {\mathbf {u}} (s) \end{array} \right] = \left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ - \hat {\mathbf {y}} (s) \end{array} \right] \tag {11.20}
$$

这表明， $S_{T}$ 为能控，当且仅当

$$
\left[ \begin{array}{c c c c} {D _ {1} (s)} & {\mathbf {0}} & {\mathbf {0}} & {I _ {p _ {1}}} \\ {\mathbf {0}} & {D _ {2} (s)} & {I _ {p _ {2}}} & {\mathbf {0}} \\ {- N _ {1} (s)} & {\mathbf {0}} & {- I _ {p 2}} & {\mathbf {0}} \end{array} \right] \text {行满秩,} \forall s \in \mathcal {C} \tag {11.21}
$$

现对上式的分块矩阵作严格系统等价变换，即作初等运算：将块列1右乘一 $I_{p_{1}}$ ，将块行2加于块行3。那么， $S_{T}$ 能控的充分必要条件就化为
