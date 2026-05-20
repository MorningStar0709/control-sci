$$\frac {\partial}{\partial z _ {j} ^ {i}} \tilde {g} ^ {s} = 0, \quad i \neq s. \tag {8.4.61}$$

令

$$D = \operatorname{diag} (\bar {g} ^ {1}, \dots , \tilde {g} ^ {k}).$$

我们构造

$$\alpha = - \operatorname{diag} (\beta_ {1}, \dots , \beta_ {k}) (D ^ {\mathrm{T}} D) ^ {- 1} D ^ {\mathrm{T}} f,$$

并令

$$\tilde {f} = f + g \beta_ {0} \alpha = \left[ \tilde {f ^ {1}} ^ {\mathrm{T}}, \dots , \tilde {f ^ {k}} ^ {\mathrm{T}} \right] ^ {\mathrm{T}}.$$

于是式 (8.4.59) 和式 (8.4.61) 表明

$$\frac {\partial}{\partial z _ {j} ^ {i}} \tilde {f} ^ {s} = 0, \quad i \neq s. \tag {8.4.62}$$

回忆 $\Delta_{i}$ 的构造，从式(8.4.61)和式(8.4.62)可分别推出如下两式：

$$\left[ \tilde {f}, \Delta_ {i} \right] \subset \Delta_ {i}, \quad i = 1, \dots , k, \tag {8.4.63}\left[ \tilde {g} _ {j}, \Delta_ {i} \right] \subset \Delta_ {i}, \quad j = 1, \dots , m, \quad i = 1, \dots , k. \tag {8.4.64}$$

定义8.4.9 给定系统(8.4.55)和点 $x_0 \in M$ . 所谓在 $x_0$ 的局部反馈块解耦问题，是指找出一个正则控制 $u = \alpha(x) + \beta(x)v$ 和一个局部坐标变换 $z = z(x)$ ，使得反馈系统有如下解耦形式：

$$
\left\{ \begin{array}{l} \dot {z} ^ {1} = f ^ {1} (z ^ {1}) + g ^ {1} (z ^ {1}) v ^ {1}, \\ \vdots \\ \dot {z} ^ {k} = f ^ {k} (z ^ {k}) + g ^ {k} (z ^ {k}) v ^ {k}. \end{array} \right. \tag {8.4.65}
$$

对局部反馈块解耦问题，我们有如下结论：

定理 8.4.9 设系统 (8.4.55) 在 $x_{0} \in M$ 是强可接近的，那么局部反馈块解耦问题是可解的，当且仅当存在 k 个同时可积的弱 $(f, g)$ 不变分布 $\Delta_{1}, \cdots, \Delta_{k}$ ，使得

$$G = G \cap \Delta_ {1} + \dots + G \cap \Delta_ {k}.$$

证明 (必要性) 令

$$\Delta_ {i} = \operatorname{span} \left\{\frac {\partial}{\partial z _ {j} ^ {i}} \Big | j = 1, \dots , n _ {i} \right\}, \quad i = 1, \dots , k.$$

利用等式 (8.4.65)，显然 $\Delta_1, \dots, \Delta_k$ 满足定理的条件.

(充分性) 根据定理 8.4.8, $\Delta_1, \cdots, \Delta_k$ 是同时 $(f, g)$ 不变的。因此我们能找到正则反馈 $(\alpha(x), \beta(x))$ 使得

$$
\left\{ \begin{array}{l} [ f + g \alpha , \Delta_ {i} ] \subset \Delta_ {i}, \\ [ g \beta , \Delta_ {i} ] \subset \Delta_ {i}. \end{array} \right.
$$

当 $\Delta_{1},\cdots,\Delta_{k}$ 同时可积时，在平整坐标下，容易证明系统 (8.4.55) 具有式 (8.4.65) 的形式.
