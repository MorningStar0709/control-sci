结论1 对于有限时间LQ调节问题(5.174)和(5.175)， $\pmb{u}^{*}(\cdot)$ 为其最优控制的充分必要条件是其具有形式：

$$\boldsymbol {u} ^ {*} (t) = - K ^ {*} (t) \boldsymbol {x} ^ {*} (t), \quad K ^ {*} (t) = R ^ {- 1} B ^ {T} P (t) \tag {5.176}$$

最优轨线 $x^{*}(t)$ 为下述状态方程的解：

$$\dot {x} ^ {*} (t) = A x ^ {*} (t) + B u ^ {*} (t), \quad x ^ {*} (0) = x _ {0} \tag {5.177}$$

而最优性能值为:

$$J ^ {*} = \frac {1}{2} x _ {0} ^ {T} P (0) x _ {0}, \quad \forall x _ {0} \neq 0 \tag {5.178}$$

其中， $P(t)$ 为下述矩阵黎卡提（Riccati）微分方程的正半定对称解阵：

$$
\begin{array}{l} - \dot {P} (t) = P (t) A + A ^ {T} P (t) + Q - P (t) B R ^ {- 1} B ^ {T} P (t) \\ P (t) = S _ {1} t \in [ 0, t ] \end{array} \tag {5.179}
P \left(t _ {f}\right) = S, t \in [ 0, t _ {f} ]
$$

证 必要性：已知 $\boldsymbol{u}^{*}(\cdot)$ 为最优控制，欲证 $\boldsymbol{u}^{*}(t) = -R^{-1}B^{T}P(t)\boldsymbol{x}^{*}(t)$ 。

首先，将条件极值问题（5.174）和（5.175）化为无条件极值问题。为此，引入拉格朗日（Lagrange）乘子 $n \times 1$ 向量函数 $\lambda(t)$ ，将性能指标泛函表为

$$J = \frac {1}{2} x ^ {T} \left(t _ {f}\right) S x \left(t _ {f}\right) + \int_ {0} ^ {t _ {f}} \left\{\frac {1}{2} \left[ x ^ {T} Q x + u ^ {T} R u \right] + \lambda^ {T} [ A x + B u - \dot {x} ] \right\} d t \tag {5.180}$$

因而问题就化为对上述 $J$ 相对于 $\pmb{u}(\cdot)$ 求极值问题。进而，表哈密顿（Hamilton）函数

$$H (x, u, \lambda) = \frac {1}{2} \left(x ^ {T} Q x + u ^ {T} R u\right) + \lambda^ {T} (A x + B u) \tag {5.181}$$

则可把式 $(5.180)$ 进一步表示为:

$$
\begin{array}{l} J (u (\cdot)) = \frac {1}{2} x ^ {T} \left(t _ {f}\right) S x \left(t _ {f}\right) + \int_ {0} ^ {t _ {f}} [ H (x, u, \lambda) - \lambda^ {T} \dot {x} ] d t \\ = \frac {1}{2} x ^ {T} \left(t _ {f}\right) S x \left(t _ {f}\right) + \int_ {0} ^ {t _ {f}} \left[ H (x, u, \lambda) - \left(\frac {d}{d t} \lambda^ {T} x\right) + \dot {\lambda} ^ {T} x \right] d t \\ - \frac {1}{2} x ^ {T} \left(t _ {i}\right) S x \left(t _ {i}\right) - \lambda^ {T} \left(t _ {i}\right) x \left(t _ {i}\right) + \lambda^ {T} (0) x (0) \\ + \int_ {0} ^ {t _ {f}} [ H (x, u, \lambda) - \dot {\lambda} ^ {T} x ] d t \tag {5.182} \\ \end{array}
$$

为找出使 $J(\pmb{u}^{*}(\cdot))$ 取极小时 $\pmb{u}^{*}(\cdot)$ 应满足的条件，进而来找出由 $\pmb{u}(\cdot)$ 的变分 $\delta \pmb{u}(\cdot)$ 所引起的泛函 $J(\pmb{u}(\cdot))$ 的变分 $\delta J(\pmb{u}(\cdot))^{\mathrm{D}}$ 。由于这里 $\tau_{I}$ 为固定，因此 $\delta \pmb{u}(\cdot)$

只引起 $\delta x(\cdot)$ 和 $\delta x(t_f)$ 。表明，在确定 $\delta J(u(\cdot))$ 中应同时考虑 $\delta u(\cdot)$ ， $\delta x(\cdot)$ 和 $\delta x(t_f)$ 的影响，于是有：
