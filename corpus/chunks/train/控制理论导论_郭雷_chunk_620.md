$$\boldsymbol {u} = \alpha (\boldsymbol {x}) + \beta (\boldsymbol {x}) \boldsymbol {v},$$

(这里“正则”指 $\beta$ 是非奇异的) 以及一个局部坐标卡 $(U, z)$ , $z = (z^1, z^2)$ , 使得系统 (8.4.18) 局部可表示为

$$
\left\{ \begin{array}{l} \dot {z} ^ {1} = f ^ {1} (z) + \sum_ {i = 1} ^ {m} g _ {i} ^ {1} (z) v _ {i} + \sum_ {j = 1} ^ {s} p _ {j} (z) w _ {j}, \\ \dot {z} ^ {2} = f ^ {2} \left(z ^ {2}\right) + \sum_ {i = 1} ^ {m} g _ {i} ^ {2} \left(z ^ {2}\right) v _ {i}, \\ y = h \left(z ^ {2}\right). \end{array} \right. \tag {8.4.19}
$$

由方程(8.4.19)显见干扰 $w$ 不影响 $z^2$ , 而同时输出 $y$ 只依赖于 $z^2$ . 因此, 干扰不影响输出, 这就是干扰解耦的物理意义.

定义

$$\ker (h) := \operatorname{span} \{X \mid L _ {X} h = \langle \mathrm{d} h, X \rangle = 0 \}.$$

引理8.4.1 如果存在一个分布 $\Delta$ ，它在 $x_0$ 的一个邻域内是非奇异且对合的，并且

$$p _ {i} (x) \in \Delta \subset \ker (h), \tag {8.4.20}$$

则干扰解耦问题在 $x_0$ 点可解.

证明 首先找 一个平整坐标 $(U, z), z = (z^1, z^2)$ 使得

$$\Delta = \operatorname{span} \left\{\frac {\partial}{\partial z _ {1} ^ {1}}, \dots , \frac {\partial}{\partial z _ {k} ^ {1}} \right\},$$

这里 $k = \mathrm{rank}(\Delta) = \dim (z^1)$ .

由于 $\Delta$ 是 $(f, g)$ 不变的，故存在控制 $u = \alpha(z) + \beta(z)v$ ，使得

$$[ f + g \alpha , \Delta ] \subset \Delta ,[ g \beta , \Delta ] \subset \Delta .$$

因为 $p \in \Delta$ , 所以

$$
p (z) = \left[ \begin{array}{c} p ^ {1} (z) \\ 0 \end{array} \right].
$$

利用前面的讨论可知

$$
f + g \alpha = \left[ \begin{array}{l} f ^ {1} (z) \\ f ^ {2} (z ^ {2}) \end{array} \right], \qquad g \beta = \left[ \begin{array}{l} g ^ {1} (z) \\ \gamma^ {2} (z ^ {2}) \end{array} \right].
$$

此外，由于

$$\langle \mathrm{d} h, \Delta \rangle = 0,$$

故显然 $h(z) = h(z_{2})$ ，于是得到方程(8.4.19).

定义 8.4.4 设 $\Delta$ 为一个给定分布。所谓 $\Delta$ 的对合闭包，记作 $\bar{\Delta}$ ，是指包含 $\Delta$ 的最小对合分布。也就是说， $\Delta$ 的对合闭包是包含 $\Delta$ 的所有对合分布的交。

引理8.4.2 如果 $\Delta$ 是弱 $(f, g)$ 不变分布，那么它的对合闭包 $\bar{\Delta}$ 也是弱 $(f, g)$ 不变分布.

证明 用 $\Delta^{(k)}$ 表示 $\Delta$ 向量场的第 $k$ 重李括号集合，即

$$\Delta^ {(1)} = \Delta , \quad \Delta^ {(k + 1)} = [ \Delta^ {(k)}, \Delta^ {(k)} ], \quad k \geqslant 1.$$

则显然

$$\tilde {\Delta} = \bigcup_ {k = 0} ^ {\infty} \operatorname{span} \{\Delta^ {(k)} \}.$$

故我们只需证明

$$[ g _ {i}, X ] \in \bar {\Delta} + G, \quad \forall X \in \Delta^ {(k)}, k = 1, 2, \dots . \tag {8.4.21}$$

用归纳法证 (8.4.21). 当 $k = 1$ 时显然成立. 设其对 $k$ 也成立. 注意任一 $X \in \Delta^{(k+1)}$ 可表示为 $X \in [\Delta^{(k)}, \Delta^{(k)}]$ . 因此我们只要证明, 如果 $X_i \in \Delta^{(k)}, i = 1, 2$ 满足式 (8.4.21) 则 $[X_1, X_2]$ 也满足此式. 设

$$[ g _ {i}, X _ {j} ] = Z _ {j} ^ {i} + Y _ {j} ^ {i}, \quad Z _ {j} ^ {i} \in \bar {\Delta}, Y _ {j} ^ {i} \in G, i = 0, 1, \dots , m, j = 1, 2,$$
