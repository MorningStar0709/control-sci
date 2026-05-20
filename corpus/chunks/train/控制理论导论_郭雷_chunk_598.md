$$z _ {1} = (z _ {1} ^ {1}, z _ {1} ^ {2}), \quad z _ {2} = (z _ {2} ^ {1}, z _ {2} ^ {2}), \quad z _ {1} ^ {1} = z _ {2} ^ {1}, \quad z _ {1} ^ {2} \neq z _ {2} ^ {2}.$$

那么

$$y (z _ {1}, u (t)) \equiv y (z _ {2}, u (t)), \quad z \in U.$$

因此系统在 $x_0$ 点不局部能观测.

注意在上述证明中，我们假定容许控制是分段定常的。如果容许控制是状态反馈。证明需要作一些小修改。

最后考虑解析系统.

定理 8.2.3 设系统 (8.1.1) 解析且满足能控性秩条件，则系统局部弱能观测当且仅当能观测性秩条件满足.

证明 注意由能控性秩条件知系统为局部弱能控的，即对任意两点 $x, y \in M$ ， $x \in WR(y)$ 。因此利用定理8.2.1，我们仅需证明必要性。为此，利用定理8.2.2，只要证明 $\mathcal{H}$ 处处维数相同即可。利用局部弱能控性，只要证明 $\operatorname{rank}(\mathcal{H})$ 在被一条 $\mathcal{F}$ 的积分曲线连接的两点上相等即可。设对某个 $X \in \mathcal{F}$ ， $x_2 = \phi_t^X(x_1)$ 。对任一 $\omega \in \mathcal{H}$ ，利用 Campbell-Baker-Hausdorff 公式可得

$$(\phi_ {t} ^ {X}) ^ {*} \omega (x _ {2}) = \sum_ {k = 0} ^ {\infty} L _ {X} ^ {k} \omega (x _ {1}) \frac {t ^ {k}}{k !}.$$

上式左边属于 $\mathcal{H}(x_1)$ 而 $(\phi_t^X)^*$ 是一个同胚．由此可知

$$\operatorname{rank} (\mathcal {H} (x _ {2})) \leqslant \operatorname{rank} (\mathcal {H} (x _ {1})).$$

同样，对逆时间利用 $(\phi_{-t}^{X})^{*}$ ，可得

$$\operatorname{rank} (\mathcal {H} (x _ {1})) \leqslant \operatorname{rank} (\mathcal {H} (x _ {2})).$$

例8.2.1 考虑线性系统

$$
\left\{ \begin{array}{l} \dot {x} = A x + B u, \\ y = C x. \end{array} \right.
$$

由8.1节习题8.1.1可知

$$\mathcal {F} = \operatorname{span} \{A x, B, A B, \dots , A ^ {n - 1} B \}.$$

那么

$$H = \operatorname{span} _ {\mathbb {R}} \left\{C _ {j} A x, C _ {j} B, \dots , C _ {j} A ^ {n - 1} B \mid 1 \leqslant j \leqslant m \right\},$$

其中下标 $\mathbb{R}$ 表示在实数域展开．容易验证能观测性对偶分布为

$$\mathcal {H} = \operatorname{span} \{C, C A, \dots , C A ^ {n - 1} \}, \tag {8.2.8}$$

即对线性系统能观测性等价于能观测性对偶分布满足秩条件.

例8.2.2 考虑时变线性系统 (8.1.29). 利用扩展系统 (8.1.30), 可以验证其能观测性秩条件等价于

$$
\operatorname{rank} \left[ \begin{array}{c} C (t) \\ \Delta_ {o} C (t) \\ \Delta_ {o} ^ {2} C (t) \\ \vdots \end{array} \right] = n,
$$

这里

$$\Delta_ {o} C (t) = \frac {\mathrm{d}}{\mathrm{d} t} C (t) + C (t) A (t),$$

且

$$\Delta_ {o} ^ {k + 1} C (t) = \frac {\mathrm{d}}{\mathrm{d} t} \Delta_ {o} ^ {k} C (t) + \Delta_ {o} ^ {k} C (t) A (t), \quad k \geqslant 1.$$

本节最后考虑非线性系统的标准分解.

给定一个动态系统

$$\dot {x} = f (x), \quad x \in M. \tag {8.2.9}$$

设 $\Delta$ 为一个分布，且对一给定点 $x_0 \in M$ 存在 $x_0$ 的一个邻域 $U$ ，使得 $\Delta$ 在 $U$ 上对合且 $\operatorname{rank}(\Delta(x)) = k, \forall x \in U$ 。那么由 Frobenius 定理存在一个局部坐标卡 $(V, z)$ ， $x_0 \in V \subset U$ ，使得

$$\Delta = \operatorname{span} \left\{\frac {\partial}{\partial z _ {1}}, \dots , \frac {\partial}{\partial z _ {k}} \right\}. \tag {8.2.10}$$
