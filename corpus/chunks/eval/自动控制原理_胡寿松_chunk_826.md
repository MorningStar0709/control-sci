# 2) $P(t)$ 是对称的。

命题10-1 若矩阵 $P(t)$ 是里卡蒂方程(10-99)及其边界条件(10-100)的唯一解，则

$$\boldsymbol {P} (t) = \boldsymbol {P} ^ {\mathrm{T}} (t) \tag {10-113}$$

证明 对里卡蒂方程(10-99)及其边界条件(10-100)取转置,可得

$$- \dot {\boldsymbol {P}} ^ {\mathrm{T}} (t) = \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {P} ^ {\mathrm{T}} (t) + \boldsymbol {P} ^ {\mathrm{T}} (t) \boldsymbol {A} (t) - \boldsymbol {P} ^ {\mathrm{T}} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- \mathrm{T}} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} ^ {\mathrm{T}} (t) + \boldsymbol {Q} ^ {\mathrm{T}} (t) \tag {10-114}$$

以及

$$\boldsymbol {P} ^ {\mathrm{T}} \left(t _ {f}\right) = \boldsymbol {F} ^ {\mathrm{T}} \tag {10-115}$$

因为 $\pmb {R}(t) = \pmb{R}^{\mathrm{T}}(t),\pmb {Q}(t) = \pmb{Q}^{\mathrm{T}}(t),\pmb {F} = \pmb{F}^{\mathrm{T}}$ ，于是式(10-114)及式(10-115)可写为

$$- \dot {\boldsymbol {P}} ^ {\mathrm{T}} (t) = \boldsymbol {P} ^ {\mathrm{T}} (t) \boldsymbol {A} (t) + \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {P} ^ {\mathrm{T}} (t) - \boldsymbol {P} ^ {\mathrm{T}} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} ^ {\mathrm{T}} (t) + \boldsymbol {Q} (t) \tag {10-116}\boldsymbol {P} ^ {\mathrm{T}} \left(t _ {f}\right) = \boldsymbol {F} \tag {10-117}$$

比较式(10-99)、式(10-100)与式(10-116)、式(10-117)可见， $P(t)$ 与 $P^{\mathrm{T}}(t)$ 是在同一边界条件下的同一矩阵微分方程的解。因为 $P(t)$ 是唯一的，故式(10-113)必然成立。

3) $P(t)$ 是非负的。

命题 10-2 对于性能指标(10-94)，如果在区间 $\left[t_{0},t_{f}\right]$ 上，有 $F\geqslant0,Q(t)\geqslant0,R(t)>0$ ，则对于任意的 $u(t)$ 和相应的 $x(t)$ ，总有 $J[x(t),u(t),t]\geqslant0$ 。

证明 由命题假设,二次型函数

$$\boldsymbol {x} ^ {\mathrm{T}} \left(t _ {f}\right) \boldsymbol {F x} \left(t _ {f}\right) \geqslant 0, \quad \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {x} (t) \geqslant 0, \quad \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {u} (t) > 0$$

从而，对任意的 $u(t)$ 和相应的 $\pmb{x}(t)$ ，由式(10-94)描述的性能指标，总有

$$J [ \boldsymbol {x} (t), \boldsymbol {u} (t), t ] \geqslant 0, \quad \forall t \in [ t _ {0}, t _ {f} ]$$

命题10-3 若矩阵 $P(t)$ 是里卡蒂方程(10-99)及其边界条件(10-100)的唯一解，则

$$\boldsymbol {P} (t) \geqslant \mathbf {0}, \quad \forall t \in [ t _ {0}, t _ {f} ] \tag {10-118}$$

证明 由命题10-2, 对任意的 $\pmb{u}(t)$ 和相应的 $\pmb{x}(t)$ , 有

$$J [ \boldsymbol {x} (t), \boldsymbol {u} (t), t ] \geqslant 0, \quad \forall t \in [ t _ {0}, t _ {f} ]$$
