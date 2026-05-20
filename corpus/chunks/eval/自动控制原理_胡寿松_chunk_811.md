# (2) 正常情况与奇异情况

对于问题 10-1, 构造哈密顿函数

$$H (x, u, \lambda) = 1 + \lambda^ {\mathrm{T}} A x + \lambda^ {\mathrm{T}} B u$$

根据极小值条件 $H^{*} = \min_{u\in \Omega}H$ ，有

$$1 + \boldsymbol {\lambda} ^ {T} \mathbf {A} \mathbf {x} ^ {*} (t) + \boldsymbol {\lambda} ^ {T} (t) \mathbf {B} \mathbf {u} ^ {*} (t) = \min _ {| u _ {j} | \leqslant 1} \{1 + \boldsymbol {\lambda} ^ {T} (t) \mathbf {A} \mathbf {x} ^ {*} (t) + \boldsymbol {\lambda} ^ {T} (t) \mathbf {B} \mathbf {u} (t) \}$$

上式又可表示为

$$\boldsymbol {\lambda} ^ {\mathrm{T}} (t) \boldsymbol {B u} ^ {*} (t) = \min _ {| u _ {j} | \leqslant 1} \{\boldsymbol {\lambda} ^ {\mathrm{T}} (t) \boldsymbol {B u} (t) \} \tag {10-76}$$

设 $B=\left[b_{1}\quad b_{2}\quad\cdots\quad b_{m}\right]$ (10-77)

$$\boldsymbol {g} _ {j} (t) = \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \boldsymbol {b} _ {j} \tag {10-78}$$

式中， $b_{j}\in\mathbb{R}^{n},j=1,2,\cdots,m$ ，则式(10-76)可用下列符号函数表示：

$$
u _ {j} ^ {*} (t) = - \operatorname{sgn} \{g _ {j} (t) \} = \left\{ \begin{array}{l l} + 1, & g _ {j} (t) <   0 \\ - 1, & g _ {j} (t) > 0 \\ \text {不定}, & g _ {j} (t) = 0 \end{array} \right.
$$

显见, 若 $g_{j}(t) \neq 0, \forall t \in [0, t_{f}]$ , 则可用极小值原理确定 $u_{j}^{*}(t), j = 1, 2, \cdots, m$ 。这种情况称为正常(平凡)情况, 相应的系统(10-74)称为正常系统。

若 $g_{j}(t) = 0, \forall t \in [t_{1}, t_{2}] \subset [0, t_{f}]$ ，则因 $u_{j}^{*}(t)$ 不定，无法应用极小值原理确定 $u_{j}^{*}(t)$ ，只能取满足约束条件 $|u_{j}(t)| \leqslant 1$ 的任意值。这种情况称为奇异（非平凡）情况，相应的系统(10-74)称为奇异系统。
