注2.4.1 如果 $q_{n} = 1$ ，则 $q_{n}(\lambda)$ 的Routh矩阵 $\pmb{R}$ 的计算式中，分母均可去掉，此时定理2.4.4的条件变为第一列元素均为正数。

下面考虑线性时变微分方程

$$\dot {x} = A (t) x \tag {2.4.11}$$

的稳定性，其中 $x \in \mathbb{R}^n$ ， $A(t) = [a_{ij}(t)]_{n \times n}$ ， $a_{ij}(t)$ 是定义在 $[0, +\infty)$ 上的连续函数。

例2.4.2 考虑线性时变二维向量微分方程

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] = (\mathrm{e} ^ {\boldsymbol {B} t} \boldsymbol {A} \mathrm{e} ^ {- \boldsymbol {B} t} + \boldsymbol {B}) \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right], \tag {2.4.12}
$$

其中 $B = \begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}$ ， $A = \begin{bmatrix} -3 & 0 \\ 0 & 1 \end{bmatrix}$ 。通过线性时变变换

$$
\left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] = \mathrm{e} ^ {\boldsymbol {B} t} \left[ \begin{array}{l} z _ {1} \\ z _ {2} \end{array} \right], \tag {2.4.13}
$$

可将方程 (2.4.12) 化为线性定常二维向量微分方程

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} z _ {1} \\ z _ {2} \end{array} \right] = A \left[ \begin{array}{l} z _ {1} \\ z _ {2} \end{array} \right]. \tag {2.4.14}
$$

方程 (2.4.14) 的以任意 $z_0 \in \mathbb{R}^2$ 为初值的解 $z(t; 0, z_0)$ 可表示成

$$
z (t; 0, z _ {0}) = \left[ \begin{array}{c c} \mathrm{e} ^ {- 3} & 0 \\ 0 & \mathrm{e} ^ {t} \end{array} \right] z _ {0}.
$$

显然对任意 $z_0 \in \mathbb{R}^2, z(t; 0, z_0)$ 是无界的.

由于

$$
\mathrm{e} ^ {\boldsymbol {B} t} = \left[ \begin{array}{c c} \cos 2 t & \sin 2 t \\ - \sin 2 t & \cos 2 t \end{array} \right],
$$

所以从式 (2.4.13) 知方程 (2.4.12) 的平衡解是不稳定的.

另一方面，矩阵

$$
\boldsymbol {B} + \mathrm{e} ^ {\boldsymbol {B} t} \boldsymbol {A} \mathrm{e} ^ {- \boldsymbol {B} t} = \left[ \begin{array}{l l} 1 - 4 \cos^ {2} 2 t & 2 + 2 \sin 4 t \\ - 2 + 2 \sin 4 t & 1 - 4 \sin^ {2} 2 t \end{array} \right]
$$

的特征方程为

$$\lambda^ {2} + 2 \lambda + 1 = 0.$$

$\lambda = -1$ 是 $B + \mathrm{e}^{Bt}A\mathrm{e}^{-Bt}$ 的二重特征值，与时间无关，且有负实部。但是以该阵为系数矩阵的线性时变微分方程(2.4.12)的平衡解却是不稳定的。此例表明，对于线性时变微分方程(2.4.11)，当其系数矩阵 $A(t)$ 的特征值即使是不依赖于时间的负实数，也不能保证其平衡解的渐近稳定性，甚至不能保证稳定性。所以，一般来说，条件

$$\operatorname{Re} \tilde {\lambda} _ {+} (t) \leqslant - h < 0, \quad \forall t \in [ t _ {0}, + \infty)$$

不能保证线性时变向量微分方程 (2.5.11) 的平衡解的渐近稳定性，这里 $\tilde{\lambda}_{+}(t)$ 表示矩阵 $A(t)$ 的实部最大特征值.

定理2.4.5 对于线性时变微分方程(2.4.11)，如果矩阵 $A(t) + A^{\mathrm{T}}(t)$ 的最大特征值 $\lambda^{+}(t)$ 满足不等式

$$\lambda^ {+} (t) \leqslant - h < 0, \quad \forall t \in [ t _ {0}, + \infty),$$

其中 $h$ 为某正常数，那么微分方程 (2.4.11) 的平衡解是渐近稳定的.

证明 设 $x(t)$ 是微分方程 (2.4.11) 的任一非零解. 能够证明,
