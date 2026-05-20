# 1) 泛函极值的定义。

定义10-2 设 $J[x]$ 是线性赋范空间 $\mathbb{R}^n$ 上某个子集 $D$ 中的线性连续泛函，点 $x_0 \in D$ ，若存在某一正数 $\sigma$ 以及集合

$$U (x _ {0}, \sigma) = \{x \mid \| x - x _ {0} \| < \sigma , x \in \mathbf {R} ^ {n} \}$$

在 $x \in U(x_0, \sigma) \subset D$ 时，均有

$$\Delta J [ \pmb {x} ] = J [ \pmb {x} ] - J [ \pmb {x} _ {0} ] \geqslant 0 \tag {10-19}$$

或者

$$\Delta J [ \pmb {x} ] = J [ \pmb {x} ] - J [ \pmb {x} _ {0} ] \leqslant 0 \tag {10-20}$$

则称泛函 $J[\pmb{x}]$ 在 $\pmb{x} = \pmb{x}_0$ 处达到极小值（或极大值）。

2) 泛函极值的必要条件。

定理10-2 设 $J[x]$ 是在线性赋范空间 $\mathbf{R}^n$ 上某个开子集 $D$ 中定义的可微泛函，且在 $x = x_0$ 处达到极值，则泛函 $J[x]$ 在 $x = x_0$ 处必有

$$\delta J \left[ \boldsymbol {x} _ {0}, \delta \boldsymbol {x} \right] = 0 \tag {10-21}$$

定理表明，泛函一次变分为零，是泛函达到极值的必要条件。

3）变分预备定理。为了深入研究无约束泛函极值条件和有约束泛函极值条件，以及用变分法求解控制无约束的最优控制问题，需要应用变分预备定理。

定理 10-3(变分预备定理) 设 $\zeta(t)$ 是时间区间 $[t_{0}, t_{1}]$ 上连续的 n 维向量函数, $\boldsymbol{\eta}(t)$ 为任意的 n 维连续向量函数, 且有 $\boldsymbol{\eta}(t_{0}) = \boldsymbol{\eta}(t_{1}) = \mathbf{0}$ 。若满足

$$\int_ {t _ {0}} ^ {t _ {1}} \boldsymbol {\zeta} ^ {\mathrm{T}} (t) \boldsymbol {\eta} (t) \mathrm{d} t = 0$$

则必有

$$\zeta (t) \equiv 0, \quad \forall t \in [ t _ {0}, t _ {1} ]$$
