$$
\begin{array}{l} \Delta_ {i} = \operatorname{span} \left\{\mathrm{d} x _ {j} ^ {s} \mid s \neq i, j = 1, 2, \dots , n _ {s} \right\} ^ {\perp} \\ = \operatorname{span} \left\{\frac {\partial}{\partial x _ {j} ^ {i}} \mid j = 1, 2, \dots , n _ {i} \right\}. \\ \end{array}
$$

注意到 $\operatorname{rank}(\Delta_i) = n_i$ ，有

$$\Delta_ {i} = \operatorname{span} \left\{\frac {\partial}{\partial x _ {j} ^ {i}} \Bigg | j = 1, 2, \dots , n _ {i} \right\}, \quad i = 1, \dots , k.$$

本节余下的部分考虑一般非线性系统

$$\dot {x} = f (x, u), \quad x \in M, \tag {8.4.42}$$

这里 $M = \mathbb{R}^n$ 或 $n$ 维流形. 问何时它可通过坐标变换化成标准解耦形式？

定义 8.4.7 令 $u=(u^{1},\cdots,u^{k})$ 为 u 的一个分割。系统 (8.4.42) 称在 $x_{0}\in M$ 上有局部平行分解，如果存在 $x_{0}$ 的一个局部坐标卡 $(U,z)$ ，使得系统 (8.4.42) 能表示为

$$
\left\{ \begin{array}{l} \dot {z} ^ {0} = f ^ {0} (z ^ {0}), \\ \dot {z} ^ {1} = f ^ {1} (z ^ {0}, z ^ {1}, u ^ {1}), \\ \vdots \\ \dot {z} ^ {k} = f ^ {k} (z ^ {0}, z ^ {k}, u ^ {k}). \end{array} \right. \tag {8.4.43}
$$

系统 (8.4.42) 称在点 $x_0 \in M$ 上有一局部级联分解，如果系统 (8.4.42) 可局部表示为

$$
\left\{ \begin{array}{l} \dot {z} ^ {0} = f ^ {0} (z ^ {0}), \\ \dot {z} ^ {1} = f ^ {1} (z ^ {0}, z ^ {1}, u ^ {1}), \\ \dot {z} ^ {1} = f ^ {1} (z ^ {0}, z ^ {1}, z ^ {2}, u ^ {1}, u ^ {2}), \\ \vdots \\ \dot {z} ^ {k} = f ^ {k} (z, u). \end{array} \right. \tag {8.4.44}
$$

回忆8.1节，对系统(8.4.42)，定义一向量场集合

$$F = \{f (x, u) \mid u = \text { const } \}.$$

能控 Lie 代数 $\mathcal{F}$ 是由 $F$ 生成的 Lie 代数

$$\mathcal {F} = \{F \} _ {L A},$$

它的导出代数 $\mathcal{F}'$ 为

$$\mathcal {F} ^ {\prime} = \{[ X, Y ] \mid X, Y \in \mathcal {F} \} _ {L A}.$$

强能控 Lie 代数 $\mathcal{F}_0$ 定义为

$$\mathcal {F} _ {0} = \left\{\sum_ {i = 1} ^ {p} \lambda_ {i} X _ {i} + Y \mid p < \infty , \sum_ {i = 1} ^ {p} \lambda_ {i} = 0, X \in F, Y \in \mathcal {F} ^ {\prime} \right\}.$$

Lie 代数 $\mathcal{F}$ 的理想 $I$ 是 $\mathcal{F}$ 的一个子代数，使得

$$[ \mathcal {F}, I ] \subset I.$$

记 $u^{-i} = \{u^1, \dots, u^k\} / \{u^i\}$ , 即集 $u$ 除去 $u^i$ . 定义

$$F _ {i} := \left\{f (x, u _ {1} ^ {i}, u ^ {- i}) - f (x, u _ {2} ^ {i}, u ^ {- i}) \mid u _ {1} ^ {i} = \text { const }, u _ {2} ^ {i} = \text { const }, u ^ {- i} = \text { const } \right\}.$$

这里只有第 $i$ 块控制 $u^i$ 能取不同的常值。记 $I_i$ 为 $\mathcal{F}$ 的包含 $F_i$ 的最小理想。因此

$$F _ {i} \subset \mathcal {F} _ {0}, \quad i = 1, \dots , k.$$

容易验证 $\mathcal{F}_0$ 是 $\mathcal{F}$ 的一个理想，故

$$I _ {i} \subset \mathcal {F} _ {0}, \quad i = 1, \dots , k. \tag {8.4.45}$$

因此 $I_{i}$ 也是 $\mathcal{F}_0$ 的一个理想．下面我们考虑 $I_{i}$ 和 $\mathcal{F}_0$ 之间的关系．记

$$F _ {0} := \left\{f (x, u _ {1}) - f (x, u _ {2}) \mid u _ {1} = \text { const }, u _ {2} = \text { const } \right\}.$$
