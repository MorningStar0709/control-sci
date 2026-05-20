这里 $x(t)$ 是式 (2.2.1) 过点 $(t_0, x_0)$ 并在 $(t_0 - \alpha, t_0 + \beta)$ 定义的解， $\bar{y}(t)$ 和 $\underline{y}(t)$ 分别是式 (2.2.2) 过点 $(t_0, x_0)$ 并在 $(t_0 - \alpha, t_0 + \beta)$ 定义的最大解和最小解.

证明 设不等式 (2.2.7) 不成立，于是存在 $t_1 > t_0$ 及适当小正数 $\alpha_0$ ，使得

$$x (t _ {1}) = \bar {y} (t _ {1}), \quad x (t) > \bar {y} (t), \quad t \in (t _ {1}, t _ {1} + \alpha_ {0}).$$

引入辅助方程

$$\dot {x} = g (t, x) + \frac {1}{m}, \qquad m \text {为自然数.} \tag {2.2.9}$$

能够证明，式(2.2.9)过点 $(t_1, x(t_1))$ 的解 $y_m(t)$ 在区间 $[t_1, t_1 + \delta](\delta$ 为确定数)上收敛于式(2.2.2)过点 $(t_0, x_0)$ 的最大解 $\bar{y}(t)$ ，即

$$\lim _ {m \rightarrow \infty} y _ {m} (t) = \bar {y} (t).$$

由此不难推得

$$x (t) > y _ {m} (t), \quad t \in [ t _ {1}, t _ {1} + \delta ].$$

而根据定理2.2.1, 应有

$$x (t) < y _ {m} (t), \quad t \in [ t _ {1}, t _ {1} + \delta ],$$

导致矛盾，从而不等式(2.2.7)成立．同理可证不等式(2.2.8)成立.

定理2.2.3 设 $\varphi(t)$ 是定义在区间 $(a, b)$ 内的连续函数， $f(t, x)$ 是定义在区域 $\Omega_2$ 上的连续函数，且 $\forall t \in (a, b), (t, \varphi(t))$ 属于 $\Omega_2$ 内部.

(1) 如果当 $t \in [t_0, b)$ ( $t_0 \in (a, b)$ ) 时， $\varphi(t)$ 满足

$$\overline {{{D}}} _ {+} \varphi (t) \leqslant f (t, \varphi (t)) \quad (\text {或} \underline {{{D}}} _ {+} \varphi (t) \geqslant f (t, \varphi (t))), \tag {2.2.10}$$

则当 $t \in [t_0, b)$ 时有

$$\varphi (t) \leqslant \bar {x} (t) \quad (\text {或} \varphi (t) \geqslant \underline {{x}} (t));$$

(2) 如果当 $t \in (a, t_0]$ 时， $\varphi(t)$ 满足

$$\overline {{{D}}} _ {-} \varphi (t) \geqslant f (t, \varphi (t)) \quad (\text {或} \underline {{{D}}} _ {-} \varphi (t) \leqslant f (t, \varphi (t))), \tag {2.2.11}$$

则当 $t \in (a, t_0]$ 时有

$$\varphi (t) \leqslant \bar {x} (t) \quad (\text {或} \varphi (t) \geqslant \underline {{x}} (t)),$$

其中 $\bar{x}(t)$ 及 $\underline{x}(t)$ 分别是微分方程 (2.2.1) 过点 $(t_0, \varphi(t_0))$ 在区间 $(a, b)$ 的最大解及最小解。记号 $\overline{D}_+$ 、 $\underline{D}_+$ 和 $\overline{D}_-$ 、 $\underline{D}_-$ 分别表示右上、右下和左上、左下导数。例如

$$\overline {{{D}}} _ {+} \varphi (t) = \varlimsup_ {h \rightarrow 0 ^ {+}} \frac {\varphi (t + h) - \varphi (t)}{h}.$$

它们统称为Dini导数.

证明 首先把条件 (2.2.10) 加强为

$$\overline {{{D}}} _ {+} \varphi (t) < f (t, \varphi (t)), \quad t \in [ t _ {0}, b). \tag {2.2.12}$$

于是设 $x(t)$ 是方程(2.2.1)过点 $(t_0,\varphi (t_0))$ 在区间 $[t_0,b)$ 上的任一解 $x(t)$ ，则

$$\overline {{{D}}} _ {+} \varphi (t _ {0}) < f (t _ {0}, \varphi (t _ {0})) = \dot {x} (t _ {0}).$$

因此在 $t_0$ 的某右邻域内成立不等式 $\varphi(t) < x(t)$ . 如果存在 $\tilde{t} \in (t_0, b)$ 使得

$$\varphi (\tilde {t}) \geqslant x (\tilde {t}),$$
