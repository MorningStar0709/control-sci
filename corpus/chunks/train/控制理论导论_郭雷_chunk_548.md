$$\frac {1}{2} x _ {0} ^ {\mathrm{T}} P ^ {*} x _ {0} = \frac {1}{2} \int_ {0} ^ {+ \infty} \left[ x ^ {* \mathrm{T}} (t) Q x ^ {*} (t) + u ^ {* \mathrm{T}} (t) R u ^ {*} (t) \right] \mathrm{d} t,\frac {1}{2} x _ {0} ^ {\mathrm{T}} P _ {1} ^ {*} x _ {0} = \frac {1}{2} \int_ {0} ^ {+ \infty} \left[ x ^ {* \mathrm{T}} (t) Q x ^ {*} (t) + u ^ {* \mathrm{T}} (t) R u ^ {*} (t) \right] d t.$$

从而

$$\frac {1}{2} x _ {0} ^ {\mathrm{T}} P ^ {*} x _ {0} = \frac {1}{2} x _ {0} ^ {\mathrm{T}} P _ {1} ^ {*} x _ {0}, \quad \forall x _ {0} \in \mathbb {R} ^ {n}.$$

所以 $P^{*} = P_{1}^{*}$

推论 7.3.1 设 $(A, B)$ 完全能控，如果 Q 是正定对称矩阵，则 Riccati 代数方程 (7.3.29) 存在唯一正定对称解矩阵.

定理7.3.5 设线性定常系统(7.3.1)完全能控，如果Riccati矩阵代数方程(7.3.29)存在正定对称解矩阵，则对 $Q$ 的任何分解 $Q = CC^{\mathrm{T}}$ 都使得 $(A,C^{\mathrm{T}})$ 完全能观测.

证明 用反证法，由完全观测性定义易知定理结论正确.

定理 7.3.6 设定常线性系统 (7.3.1) 中 $(A, B)$ 完全能控，且式 (7.3.19) 中常阵 Q 的分解 $Q = CC^{T}$ 使得 $(A, C^{T})$ 完全能观测，则最优闭环系统

$$\dot {x} (t) = A x (t) - R ^ {- 1} B ^ {\mathrm{T}} P ^ {*} x (x) \tag {7.3.33}$$

是全局渐近稳定的，其中 $P^{*}$ 是Riccati矩阵代数方程(7.3.29)的正定对称解矩阵.

证明 取 $V(x) = x^{\mathrm{T}}P^{*}x$ ，由 $P^{*} > 0$ 知 $V(x)$ 是 $x$ 的正定函数。利用 $P^{*}$ 满足式 (7.3.29) 不难得到

$$\frac {\mathrm{d}}{\mathrm{d} t} V (x (t)) = - x ^ {\mathrm{T}} (t) \left(C C ^ {\mathrm{T}} + P ^ {*} B R ^ {- 1} B ^ {\mathrm{T}} P ^ {*}\right) x (t) \leqslant 0, \tag {7.3.34}$$

这里 $x(t)$ 为式 (7.3.33) 的解. 如果

$$\frac {\mathrm{d}}{\mathrm{d} t} V (x (t)) = - x ^ {\mathrm{T}} (t) \left[ C C ^ {\mathrm{T}} + P ^ {*} B R ^ {- 1} B ^ {\mathrm{T}} P ^ {*} \right] x (t) \equiv 0,$$

则

$$\boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {C C} ^ {\mathrm{T}} \boldsymbol {x} (t) \equiv 0, \quad \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {P} ^ {*} \boldsymbol {B R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {P} ^ {*} \boldsymbol {x} (t) \equiv 0.$$

由此，不难得到

$$C ^ {T} x (t) \equiv 0,C ^ {T} A x (t) \equiv 0,$$

:

$$C ^ {T} A ^ {n - 1} x (t) \equiv 0.$$

这与 $(A, C^{\mathrm{T}})$ 完全能观测相矛盾。于是从式 (7.3.34) 并利用定理 2.4.12(LaSalle 不变原理) 即知定理 7.3.6 结论成立。

下面考察具有指定衰减度的二次最优调节器。给定由线性定常齐次 $n$ 阶向量微分方程描述的自由系统

$$\dot {x} (t) = G x (t). \tag {7.3.35}$$

熟知当 $G$ 为稳定阵时， $\forall x_0\neq 0$ ，必定存在常数 $\alpha >0,$ 使得式(7.3.35）初值为 $x(0) = x_0$ 的解 $x(t;0,x_0)$ 满足

$$\lim _ {t \rightarrow + \infty} x (t; 0, x _ {0}) \mathrm{e} ^ {\alpha t} = 0. \tag {7.3.36}$$

$\alpha$ 称为自由系统 (7.3.35) 的衰减度。显然，衰减度并不是唯一的。对于定常线性二次最优调节问题 (7.3.1) 和 (7.3.19)，在一定条件下，能够使最优闭环系统具有事先指定的衰减度。

给定 $\beta > 0$ , 考察如下定常线性二次最优调节问题 (控制无约束, 即 $\mathbb{U}_r = \mathbb{R}^r$ ):
