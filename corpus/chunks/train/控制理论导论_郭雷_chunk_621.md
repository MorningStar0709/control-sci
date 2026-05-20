这里 $g_0 := f$ . 根据 Jacobi 等式可知

$$
\begin{array}{l} \left[ g _ {i}, \left[ X _ {1}, X _ {2} \right] \right] = \left[ X _ {1}, \left[ g _ {i}, X _ {2} \right] \right] - \left[ X _ {2}, \left[ g _ {i}, X _ {1} \right] \right], \\ = \left[ X _ {1}, Z _ {2} ^ {i} + Y _ {2} ^ {i} \right] - \left[ X _ {2}, Z _ {1} ^ {i} + Y _ {1} ^ {i} \right], \\ = \left[ X _ {1}, Z _ {2} ^ {i} \right] - \left[ X _ {2}, Z _ {1} ^ {i} \right] + \left[ X _ {1}, Y _ {2} ^ {i} \right] - \left[ X _ {2}, Y _ {1} ^ {i} \right] \\ \in \bar {\Delta} + \bar {\Delta} + \bar {\Delta} + G + \bar {\Delta} + G = \bar {\Delta} + G. \\ \end{array}
$$

因此 $\bar{\Delta}$ 也是弱 $(f,g)$ 不变的.

定理8.4.2 设 $\Delta$ 是 $\ker(h)$ 中最大的弱 $(f, g)$ 不变分布，且 $\Delta$ 和 $\Delta \cup G$ 均在 $x_0$ 点非奇异，则系统 (8.4.18) 在 $x_0$ 点是局部干扰可解耦的，当且仅当

$$p _ {i} \in \Delta , \quad i = 1, \dots , p.$$

证明 （充分性）设 $\Delta$ 为 $\ker(h)$ 中最大的弱 $(f, g)$ 不变分布。可以证明 $\Delta$ 是对合的。根据引理8.4.2, $\bar{\Delta}$ 也是弱 $(f, g)$ 不变分布，故我们只需证明如果 $\Delta \subset \ker(h)$ ，那么 $\bar{\Delta} \subset \ker(h)$ 。注意若 $\ker(h)$ 是对合的，则断言显然成立。实际上， $\ker(h)$ 确实是对合的，因为设 $X, Y \in \ker(h)$ ，那么

$$\langle \mathrm{d} h, [ X, Y ] \rangle = L _ {X} L _ {Y} h - L _ {Y} L _ {X} h = 0,$$

从而由引理8.4.1可得 $\ker (h)$ 的对合性.

(必要性) 由方程 (8.4.19) 可知

$$\Delta_ {0} = \operatorname{span} \left\{\frac {\partial}{\partial z _ {i} ^ {1}} \mid i = 1, \dots , k \right\}$$

是 $(f,g)$ 不变的对合分布，并且

$$p _ {i} \in \Delta_ {0} \subset \ker (h).$$

那么对包含在 $\ker (h)$ 中的最大弱 $(f,g)$ 不变分布 $\Delta$ ，我们有

$$p _ {i} \in \Delta_ {0} \subset \Delta \subset \ker (h).$$

下面考虑如何得到 $\ker (h)$ 中的最大弱 $(f,g)$ 不变分布．定义一族余分布

$$
\left\{ \begin{array}{l} \Omega_ {0} = \operatorname{span} \{\mathrm{d} h _ {i} \mid i = 1, \dots , p \}, \\ \Omega_ {k + 1} = \Omega_ {k} + L _ {f} (G ^ {\perp} \cap \Omega_ {k}) + \sum_ {j = 1} ^ {m} L _ {g _ {j}} (G ^ {\perp} \cap \Omega_ {k}), \quad k \geqslant 0. \end{array} \right. \tag {8.4.22}
$$

定理8.4.3 假定由方程(8.4.22)定义的余分布增列 $\{\Omega_k\}$ 中，存在一个整数 $k^{*}$ 使得

$$\Omega_ {k ^ {*} + 1} = \Omega_ {k ^ {*}},$$

则其消去分布

$$\Delta = \Omega_ {k ^ {*}} ^ {\perp}$$

为 $\ker (h)$ 中的最大弱 $(f,g)$ 不变分布.

证明 首先证明 $\Delta$ 是弱 $(f, g)$ 不变的. 由方程 (8.4.22) 可知

$$L _ {g _ {i}} (G ^ {\perp} \cap \Omega_ {k ^ {*}}) \subset \Omega_ {k ^ {*}}, \quad i = 0, 1, \dots , m,$$

这里仍记 $f := g_0$ . 令 $X \in \Delta$ , 且 $\omega \in \Omega_{k_*} \cap G^\perp$ , 则

$$\langle L _ {g _ {i}} \omega , X \rangle = L _ {g _ {i}} \langle \omega , X \rangle - \langle \omega , \mathrm{ad} _ {g _ {i}} X \rangle . \tag {8.4.23}$$

式 (8.4.23) 左边与右边第一项均为零，故

$$\langle \omega , \mathrm{ad} _ {g _ {i}} X \rangle = 0,$$

这说明
