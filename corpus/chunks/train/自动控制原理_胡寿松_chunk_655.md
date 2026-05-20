# (2) 线性离散系统的可观测性

设离散系统为

$$\boldsymbol {x} (k + 1) = \boldsymbol {G} (k) \boldsymbol {x} (k) + \boldsymbol {H} (k) \boldsymbol {u} (k), \quad k \in T _ {k}\mathbf {y} (k) = \mathbf {C} (k) \mathbf {x} (k) + \mathbf {D} (k) \mathbf {u} (k) \tag {9-152}$$

若对初始时刻 $l \in T_k$ 的任一非零初始状态 $\pmb{x}(l) = \pmb{x}_0$ ，都存在有限时刻 $m \in T_k, m > l$ ，且可由 $[l, m]$ 上的输出 $\pmb{y}(k)$ 唯一地确定 $\pmb{x}_0$ ，则称系统在时刻 $l$ 是完全可观测的。

线性定常离散系统的可观测性判据 设线性定常离散系统的动态方程为

$$\boldsymbol {x} (k + 1) = \boldsymbol {G x} (k) + \boldsymbol {H u} (k), \quad \boldsymbol {y} (k) = \boldsymbol {C x} (k) + \boldsymbol {D u} (k) \tag {9-153}$$

式中， $x(k)$ 为 n 维状态向量； $y(k)$ 为 q 维输出向量，其解为

$$\pmb {x} (k) = \pmb {G} ^ {k} \pmb {x} (0) + \sum_ {i = 0} ^ {k - 1} \pmb {G} ^ {k - 1 - i} \pmb {H u} (i) \tag {9-154}\mathbf {y} (k) = \mathbf {C G} ^ {k} \mathbf {x} (0) + \mathbf {C} \sum_ {i = 0} ^ {k - 1} \mathbf {G} ^ {k - 1 - i} \mathbf {H u} (i) + \mathbf {D u} (k) \tag {9-155}$$

研究可观测性问题时， $u(k),G,H,C,D$ 均为已知，故不失一般性，可将动态方程简化为

$$\pmb {x} (k + 1) = \pmb {G x} (k), \quad \pmb {y} (k) = \pmb {C x} (k) \tag {9-156}$$

对应的解为

$$\boldsymbol {x} (k) = \boldsymbol {G} ^ {k} \boldsymbol {x} (0), \quad \boldsymbol {y} (k) = \boldsymbol {O G} ^ {k} \boldsymbol {x} (0) \tag {9-157}$$

将 $y(k)$ 写成展开式

$$
\left. \begin{array}{l} \mathbf {y} (0) = \mathbf {C x} (0) \\ \mathbf {y} (1) = \mathbf {C G x} (0) \\ \vdots \\ \mathbf {y} (n - 1) = \mathbf {C G} ^ {n - 1} \mathbf {x} (0) \end{array} \right\} \tag {9-158}
$$

其向量-矩阵形式为

$$
\left[ \begin{array}{c} \mathbf {y} (0) \\ \mathbf {y} (1) \\ \vdots \\ \mathbf {y} (n - 1) \end{array} \right] = \left[ \begin{array}{c} \boldsymbol {C} \\ \boldsymbol {C G} \\ \vdots \\ \boldsymbol {C G} ^ {n - 1} \end{array} \right] \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \\ \vdots \\ x _ {n} (0) \end{array} \right] \tag {9-159}
$$

令 $V_{1}^{T}=\begin{bmatrix}C\\ \alpha G\\ \vdots\\ \alpha G^{n-1}\end{bmatrix}$ (9-160)

$V_{1}^{T}$ 称为线性定常离散系统的可观测性矩阵，为 $nq \times n$ 矩阵。式(9-159)含有nq个方程，若其中有n个独立方程，便可确定唯一的一组 $x_{1}(0), x_{2}(0), \cdots, x_{n}(0)$ 。当独立方程个数大于n时，解会出现矛盾；当独立方程个数小于n时，便有无穷多解。故系统可观测的充分必要条件为

$$\operatorname{rank} \boldsymbol {V} _ {1} ^ {\mathrm{T}} = n \tag {9-161}$$

由于 $\mathrm{rank}\mathbf{V}_1^{\mathrm{T}} = \mathrm{rank}\mathbf{V}_1$ ，故线性定常离散系统的可观测性判据常表示为
