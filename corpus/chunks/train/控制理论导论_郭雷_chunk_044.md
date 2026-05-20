$$\boldsymbol {W} (t _ {1}, t _ {0}) = \int_ {t _ {0}} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} (t _ {1} - \tau)} \boldsymbol {B} \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} (t _ {1} - \tau)} \mathrm{d} \tau$$

是正定的．对任意的实数 $s \geqslant -t_0$ ，令 $\sigma = \tau + s$ 。则对 $W(t_1, t_0)$ 的被积函数作变量替换得

$$\boldsymbol {W} (t _ {1}, t _ {0}) = \int_ {t _ {0} + s} ^ {t _ {1} + s} \mathrm{e} ^ {\boldsymbol {A} (t _ {1} + s - \sigma)} \boldsymbol {B} \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} (t _ {1} + s - \sigma)} \mathrm{d} \sigma = \boldsymbol {W} (t _ {1} + s, t _ {0} + s) > 0.$$

由 $s$ 的任意性并由定理1.3.1知，系统 $(A, B)$ 在任意时刻 $t \geqslant 0$ 都是完全能控的，因此它在 $[0, \infty)$ 上完全能控.

引理1.3.1表明，对于定常线性系统，只要它在某时刻完全能控，则它必定在整个时间轴上完全能控。因此，对定常系统只说它能控或不能控就够了。如果定常线性系统 $(A, B)$ 能控，可简称 $(A, B)$ 能控，或说 $(A, B)$ 为能控对。

定理1.3.2 定常线性系统 $(A, B)$ 能控的充分必要条件是

$$\operatorname{rank} Q _ {c} = n.$$

这里，

$$\boldsymbol {Q} _ {c} = [ \boldsymbol {B}, \boldsymbol {A B}, \dots , \boldsymbol {A} ^ {n - 1} \boldsymbol {B} ]. \tag {1.3.4}$$

称 $Q_{c}$ 为定常线性系统的能控性矩阵。它是一个 $n \times nr$ 矩阵，在线性系统理论中它起着很重要的作用。

证明 充分性. 用反证法. 设 $\operatorname{rank} Q_c = n$ . 若系统不能控, 则由定理1.3.1和引理1.3.1知, 对任意的 $t_1 > 0$ , $\int_0^{t_1} e^{-A\tau} BB^T e^{-A^T\tau} d\tau$ 总是奇异的. 因此, 存在非零向量 $z$ 使得

$$\int_ {0} ^ {t _ {1}} \left\| \boldsymbol {z} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} \tau} \boldsymbol {B} \right\| ^ {2} \mathrm{d} \tau = \boldsymbol {z} ^ {\mathrm{T}} \left(\int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- A \tau} \boldsymbol {B} \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {- A ^ {\mathrm{T}} \tau} \mathrm{d} \tau\right) \boldsymbol {z} = 0,$$

从而有

$$\boldsymbol {z} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} _ {\tau}} \boldsymbol {B} \equiv 0, \quad \tau \in [ 0, t _ {1} ].$$

上式对 $\tau$ 分别求 1, 2, $\cdots$ , n - 1 阶导数得

$$\boldsymbol {z} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} \tau} \boldsymbol {A} ^ {i} \boldsymbol {B} \equiv 0, \quad \tau \in [ 0, t _ {1} ], i = 0, 1, \dots , n - 1,$$

即

$$z ^ {T} c ^ {- A \tau} Q _ {c} \equiv 0, \quad \tau \in [ 0, t _ {1} ].$$

特别地，取 $\tau = 0$ ，则有 $z^{\mathrm{T}}Q_{c} = 0$ 。由此及 $\operatorname{rank}Q_c = n$ 知 $z = 0$ 。这与 $z$ 为非零向量的假设矛盾。所以系统能控。

必要性．由于 $(A,B)$ 能控，因此它在 $t_{0}=0$ 时刻能控．于是对任意初始状态 $x_{0}$ ，都有 $t_{1}>0$ ，以及定义在 $[0,t_{1}]$ 上的容许控制 $u(\cdot)$ ，使得
