现在由连续性，存在 $x_0$ 的一个邻域 $U$ ，使得

$$\operatorname{rank} (I _ {i} (x)) \geqslant s _ {i}, \quad x \in U, \quad i = 1, \dots , k.$$

这样式 (8.4.49) 就保证了

$$\operatorname{rank} (I _ {i} (x)) = s _ {i}, \quad x \in U, \quad i = 1, \dots , k.$$

于是也就证明了 $I_{i}$ 的非奇异性.

选择 $X \in I_i$ 及 $Y \in I_j$ , 因为 $I_i$ 及 $I_j$ 均为理想, 我们有

$$[ X, Y ] \in I _ {i} \cap I _ {j}, \quad 1 \leqslant i, j \leqslant k.$$

这说明 $I_{i} + I_{j}$ 是对合的。因此 $I_{1}, \cdots, I_{k}$ 是同时可积的。

定理 8.4.6 设 $F_{0}$ 在 $x_{0}$ 非奇异。那么系统 (8.4.42) 在 $x_{0}$ 的局部平行解耦问题可解，当且仅当存在控制 u 的一个分割，使得对应的理想 $I_{1}, \cdots, I_{k}$ 作为 $x_{0}$ 的分布是线性无关的。

证明 (必要性) 定义一列分布

$$\Delta_ {i} = \operatorname{span} \left\{\frac {\partial}{\partial z _ {j} ^ {i}} \Bigg | j = 1, \dots , n _ {i} \right\}, \quad i = 1, \dots , k.$$

由式 (8.4.44) 可得

$$F _ {i} \subset \Delta_ {i}, \quad i = 1, \dots , k.$$

对任意 $f \in F$ , 我们有

$$\left[ f, \frac {\partial}{\partial z _ {j} ^ {i}} \right] = - \frac {\partial}{\partial z _ {j} ^ {i}} f \in \Delta_ {i}.$$

即 $\Delta_{i}$ 是 $f$ 不变的．利用Jacobi等式容易得到

$$[ X, \Delta_ {i} ] \subset \Delta_ {i}, \quad \forall X \in \mathcal {F}.$$

因此 $\Delta_{i}$ 是 F 的一个理想. 由于 $F_{i} \in \Delta_{i}, I_{i}$ 是包含 $F_{i}$ 的最小的理想, 故 $I_{i} \subset \Delta_{i}$ . 注意到 $\Delta_{i}, i = 1, \cdots, k$ 线性无关, 故 $I_{1}, \cdots, I_{k}$ 也线性无关.

(充分性) 设 $I_{1}, \cdots, I_{k}$ 是线性无关的。利用引理 8.4.8 和引理 8.4.9 可知，存在 $x_{0}$ 的一个局部坐标卡 $(U, z)$ ，使得

$$I _ {i} = \operatorname{span} \left\{\frac {\partial}{\partial z _ {j} ^ {i}} \mid j = 1, \dots , n _ {i} \right\}, \quad i = 1, \dots , k.$$

利用坐标 $z$ ，系统(8.4.42)可表示为

$$
\left\{ \begin{array}{l} \dot {z} ^ {0} = f ^ {0} (z, u), \\ \dot {z} ^ {1} = f ^ {1} (z, u), \\ \vdots \\ \dot {z} ^ {k} = f ^ {k} (z, u). \end{array} \right. \tag {8.4.50}
$$

由于 $I_{i}$ 是 $f$ 不变的，即 $[f, I_{i}] \subset I_{i}$ ，从而可得

$$\frac {\partial f ^ {j}}{\partial x _ {s} ^ {i}} = 0, \quad i = 1, \dots , k, s = 1, \dots , n _ {i}, j \neq i. \tag {8.4.51}$$

今证在 $x_0$ 的邻域 $V$ , 我们有

$$\frac {\partial f ^ {j}}{\partial u _ {t} ^ {i}} = 0, \quad i = 1, \dots , k, s = 1, \dots , m _ {i}, j \neq i. \tag {8.4.52}$$

这是因为，否则的话，对于任意给定的邻域 $V_{0}$ ，可找到 $z \in V_{0}$ 和 $u = u_{0}$ ，使得

$$\frac {\partial f ^ {j}}{\partial u _ {t} ^ {i}} \mid_ {z, u _ {0}} \neq 0.$$

因此存在足够小的 $\varepsilon > 0$ ，使得

$$f ^ {j} (z, \bar {u}) - f ^ {j} (z, u) \neq 0, \tag {8.4.53}$$

这里

$$\tilde {u} _ {j} ^ {r} = (u _ {0}) _ {j} ^ {r}, \quad (r, j) \neq (i, t); \quad \tilde {u} _ {t} ^ {i} = (u _ {0}) _ {t} ^ {i} + \varepsilon .$$

但根据定义

$$f (z, \tilde {u}) - f (z, u _ {0}) \in I _ {i},$$

这和式 (8.4.53) 矛盾.
