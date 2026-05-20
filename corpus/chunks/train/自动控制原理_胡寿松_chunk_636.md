$$
\begin{array}{l} \boldsymbol {x} _ {0} ^ {\mathrm{T}} \boldsymbol {W} (0, t _ {1}) \boldsymbol {x} _ {0} = \int_ {0} ^ {t _ {1}} \boldsymbol {x} _ {0} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B} \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {x} _ {0} \mathrm{d} t \\ = \int_ {0} ^ {t _ {1}} \left[ \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {x} _ {0} \right] ^ {\mathrm{T}} \left[ \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {x} _ {0} \right] \mathrm{d} t \\ = \int_ {0} ^ {t _ {1}} \| \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} ^ {\mathrm{T}} t} \bar {\boldsymbol {x}} _ {0} \| ^ {2} \mathrm{d} t = 0 \tag {9-87} \\ \end{array}
$$

其中 $\| \cdot \|$ 为范数，故其必非负。于是，欲使式(9-87)成立，应当有

$$\boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {x} _ {0} = \boldsymbol {0}, \quad \forall t \in [ 0, t _ {1} ] \tag {9-88}$$

另一方面，因系统完全可控，根据定义，对此非零向量 $x_{0}$ 应有

$$\boldsymbol {x} \left(t _ {1}\right) = \mathrm{e} ^ {\boldsymbol {A} t _ {1}} \bar {\boldsymbol {x}} _ {0} + \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} t _ {1}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B u} (t) \mathrm{d} t = \mathbf {0} \tag {9-89}$$

由此又可导出

$$
\boldsymbol {x} _ {0} = - \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B u} (t) \mathrm{d} t \tag {9-90}
\begin{array}{l} \left\| \boldsymbol {x} _ {0} \right\| ^ {2} = \boldsymbol {x} _ {0} ^ {\mathrm{T}} \boldsymbol {x} _ {0} \\ = \left[ - \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- A t} B u (t) \mathrm{d} t \right] ^ {\mathrm{T}} \boldsymbol {x} _ {0} \\ = - \int_ {0} ^ {t _ {1}} \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} ^ {\mathrm{T}} t} \boldsymbol {x} _ {0} \mathrm{d} t \tag {9-91} \\ \end{array}
$$

再利用式(9-88)，由式(9-91)可以得到

$$\left\| \mathbf {x} _ {0} \right\| ^ {2} = 0, \quad \text {即} \quad \mathbf {x} _ {0} = \mathbf {0} \tag {9-92}$$

显然，此结果与假设 $x_0 \neq 0$ 相矛盾，即 $\pmb{W}(0, t_1)$ 为奇异的反设不成立。因此，若系统完全可控，

$W(0,t_{1})$ 必为非奇异。必要性得证。至此格拉姆矩阵判据证毕。

可以看出，在应用格拉姆矩阵判据时需计算矩阵指数 $\mathbf{e}^{At}$ ，在 $\pmb{A}$ 的维数 $n$ 较大时计算 $\mathbf{e}^{At}$ 是困难的。所以格拉姆矩阵判据主要用于理论分析。线性定常连续系统可控性的常用判据是直接由矩阵 $\pmb{A}$ 和 $\pmb{B}$ 判断可控性的秩判据。由于在推导秩判据时要用到凯莱-哈密顿定理，所以下面先介绍凯莱-哈密顿定理，然后再给出秩判据。

凯莱-哈密顿定理 设 $n$ 阶矩阵 $\mathbf{A}$ 的特征多项式为
