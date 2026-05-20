$$\theta^ {\mathrm{T}} \stackrel {{\text { def }}} {{=}} [ \beta^ {\mathrm{T}}, c _ {1}, \dots , c _ {r} ],$$

仍可用 LS 的递推公式 $(9.2.5)\sim(9.2.6)$ 来估计，但此时 $\phi_{t}$ 应为

$$\phi_ {t} ^ {\mathrm{T}} \stackrel {{\text { def }}} {{=}} [ \psi_ {t} ^ {\mathrm{T}}, \hat {w} _ {t}, \dots , \hat {w} _ {t - r + 1} ],\hat {w} _ {t} \stackrel {\text { def }} {=} y _ {t} - \theta_ {t} ^ {\mathrm{T}} \phi_ {t - 1}.$$

这时，相应的估计算法称为推广最小二乘（ELS）法。证明：若 $c^{-1}(z)-\frac{1}{2}$ 是 SPR 的（其中 $c(z)=1+c_{1}z+\cdots+c_{r}z^{r}$ ），则定理 9.2.1 的结论对 ELS 算法仍成立。进一步，当系统的阶数未知且噪声模型的 SPR 条件也不满足时，如何构造对参数 $\theta$ 及其维数的估计算法？

(提示: 记 $\xi_{t} = \hat{w}_{t} - w_{t}$ , 则 $c(z)\xi_{t} = \tilde{\theta}_{t}^{\mathrm{T}}\phi_{t-1}$ , 可参考文献 [19], [25].)
