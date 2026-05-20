这样，可将 $x^{1}$ 当作已知函数而考虑系统的第二部分，它满足能控性秩条件.

定理 8.4.8 设系统 (8.4.55) 在 $x_{0}$ 满足强能控秩条件. $\Delta_{i}, i = 1, \cdots, k$ 在 $x_{0}$ 是同时可积的且弱 $(f, g)$ 不变的. G 在 $x_{0}$ 非奇异，且

$$G = G \cap \Delta_ {1} + G \cap \Delta_ {2} + \dots + G \cap \Delta_ {k}. \tag {8.4.58}$$

则 $\Delta_{i}, i = 1, \cdots, k$ 是在 $x_{0}$ 同时 $(f, g)$ 不变的.

\- 证明 由于 $\Delta_{i}, i = 1, \cdots, k$ 是在 $x_{0}$ 点同时可积的，则存在 $x_{0}$ 的一个坐标邻域 $(U, z)$

$$z = \left\{z _ {j} ^ {i} \mid i = 0, 1, \dots , k, j = 1, \dots , n _ {i} \right\},$$

使得

$$\Delta_ {i} = \operatorname{span} \left\{\frac {\partial}{\partial z _ {j} ^ {i}} \Bigg | j = 1, \dots , n _ {i} \right\}, \quad i = 1, \dots , k.$$

令 $\Delta = \Delta_{1} + \cdots + \Delta_{k}$ ，则 $\Delta$ 也是弱 $(f, g)$ 不变的。可以证明

$$\mathcal {F} _ {0} \subset \Delta .$$

由于 $G \subset \Delta$ 及

$$[ f, \Delta ] \subset \Delta + G = \Delta ,$$

则有

$$\left\{\mathrm{ad} _ {f} ^ {s} g _ {j} \mid s \geqslant 0, j = 1, \dots , m \right\} \subset \Delta .$$

由于 $\Delta$ 也是对合的，故

$$\mathcal {F} _ {0} = \left\{\mathrm{ad} _ {f} ^ {s} g _ {j} \mid s \geqslant 0, j = 1, \dots , m \right\} _ {L A} \subset \Delta .$$

由于 $\operatorname{rank}(\mathcal{F}_0) = n$ ，所以 $\operatorname{rank}(\Delta_0) = 0$ 。利用式 (8.4.58)，我们能找到 $\beta_0$ 使得

$$g \beta_ {0} = (g ^ {1}, \dots , g ^ {k}), \quad g ^ {i} \in \Delta_ {i}.$$

因此在 $u = \beta_{0}v$ 作用下的反馈系统变为

$$
\dot {z} = f + g \beta_ {0} v = \left\{ \begin{array}{c} \dot {z} ^ {1} = f ^ {1} + g ^ {1} v ^ {1}, \\ \vdots \\ \dot {z} ^ {k} = f ^ {k} + g ^ {k} v ^ {k}. \end{array} \right.
$$

由于 $G$ 非奇异， $\Delta_{i}$ 同时可积，容易验证 $G \cap \Delta_{i}$ 也是非奇异的。记

$$\operatorname{rank} \left(\operatorname{span} \left\{g ^ {i} \right\}\right) - m _ {i}, \quad \sum_ {i = 1} ^ {k} m _ {i} = m.$$

于是在 $z$ 坐标下，我们有

$$
\left\{ \begin{array}{l} [ f, \Delta_ {i} ] \subset \Delta_ {i} + G, \\ [ g, \Delta_ {i} ] \subset \Delta_ {i} + G, \end{array} \right.
$$

这等价于

$$\frac {\partial}{\partial z _ {j} ^ {i}} f ^ {s} = g ^ {s} q _ {i j} ^ {s}, \quad i \neq s, \tag {8.4.59}\frac {\partial}{\partial z _ {j} ^ {i}} g ^ {s} = g ^ {s} F _ {i j} ^ {s}, \quad i \neq s, \tag {8.4.60}$$

这里 $q_{ij}^{s}$ 为 $m_i \times 1$ 函数向量， $F_{ij}^{s}$ 为 $m_i \times n_i$ 函数矩阵。根据定理8.4.1(Quaker引理)的证明，我们可构造

$$\beta_ {i} = \left(\left(g ^ {s} (x ^ {s})\right) ^ {\mathrm{T}} (g ^ {s} (x))\right) ^ {- 1},$$

和

$$\beta = \operatorname{diag} (\beta_ {1}, \dots , \beta_ {k}).$$

于是

$$g \beta_ {0} \beta = \operatorname{diag} (g ^ {1} \beta_ {1}, \dots , g ^ {k} \beta_ {k}) := \operatorname{diag} (\tilde {g} ^ {1}, \dots , \tilde {g} ^ {k}).$$

利用式 (8.4.60) 容易证明
