# 8.4 解耦

$(f, g)$ 不变分布与 Quaker 引理在解耦问题中起关键作用。我们先介绍这些概念。

考虑一个仿射非线性系统

$$\dot {x} = f (x) + g (x) u, \quad x \in \mathbb {R} ^ {n}, u \in \mathbb {R} ^ {m}. \tag {8.4.1}$$

定义8.4.1 一个分布 $\Delta(x)$ 称为 $(f, g)$ 不变的，如果存在一个反馈控制

$$u = \alpha (x) + \beta (x) v,$$

这里 $\beta (x)$ 非奇异，使得

$$
\left\{ \begin{array}{l} {[ f (x) + g (x) \alpha (x), \Delta (x) ] \subset \Delta (x),} \\ {[ g (x) \beta (x), \Delta (x) ] \subset \Delta (x).} \end{array} \right. \tag {8.4.2}
$$

定义8.4.2 一个分布 $\Delta(x)$ 称为弱 $(f, g)$ 不变的，如果

$$
\left\{ \begin{array}{l} {[ f (x), \Delta (x) ] \subset \Delta (x) + G (x),} \\ {[ g (x), \Delta (x) ] \subset \Delta (x) + G (x),} \end{array} \right. \tag {8.4.3}
$$

这里

$$G (x) = \operatorname{span} \{g (x) \} = \operatorname{span} \left\{g _ {1} (x), \dots , g _ {m} (x) \right\}.$$

多数情况下我们考虑局部 $(f, g)$ 不变分布。\$\Delta\$ 称为在 $x_0 \in M$ 的弱 $(f, g)$ 不变分布或 $(f, g)$ 不变分布，如果存在一个 $x_0$ 的邻域 $U$ ，使得式 (8.4.3)，或相对应的式 (8.4.2) 对 $x \in U$ 成立。

下面我们考虑弱 $(f, g)$ 不变分布与 $(f, g)$ 不变分布之间的关系。由于弱 $(f, g)$ 不变很容易检验，而 $(f, g)$ 不变在控制设计中很重要，我们希望它们能等价。事实上，在一定的非奇异的假设下，它们是等价的。

定理 8.4.1(Quaker 引理) 设 $\Delta$ 和 $\Delta\cup G$ 在 $x_{0}$ 点是非奇异的，则局部弱 $(f,g)$ 不变等价于局部 $(f,g)$ 不变.

证明 $(\Leftarrow)$ 由等式

$$[ \alpha g, X ] = - L _ {X} (\alpha) g + \alpha [ g, X ], \quad X \in \Delta ,$$

显然由式 (8.4.2) 可得出式 (8.4.3).

$(\Rightarrow)$ 选择 $x_0$ 的一个局部坐标卡 $(U, x)$ , 使得

$$\Delta = \operatorname{span} \left\{\frac {\partial}{\partial x _ {1}}, \dots , \frac {\partial}{\partial x _ {k}} \right\}.$$

相应地，可将 $f$ 和 $\pmb{g}$ 表示为

$$
f = \left[ \begin{array}{l} f ^ {1} \\ f ^ {2} \end{array} \right], \quad g = \left[ \begin{array}{l} g ^ {1} \\ \gamma^ {2} \end{array} \right], \quad f + g \alpha = \left[ \begin{array}{l} \tilde {f} ^ {1} \\ \tilde {f} ^ {2} \end{array} \right], \quad g \beta = \left[ \begin{array}{l} \tilde {g} ^ {1} \\ \tilde {g} ^ {2}, \end{array} \right].
$$

于是式 (8.4.2) 变成

$$
\left\{ \begin{array}{l} \frac {\partial}{\partial x _ {i}} \bar {f} ^ {2} = 0, \\ \frac {\partial}{\partial x _ {i}} \tilde {g} ^ {2} = 0, \quad i = 1, \dots , k, \end{array} \right. \tag {8.4.4}
$$

而式 (8.4.3) 则变成

$$
\left\{ \begin{array}{l} \frac {\partial}{\partial x _ {i}} f ^ {2} = \operatorname{span} \left\{g ^ {2} \right\}, \\ \frac {\partial}{\partial x _ {i}} g ^ {2} = \operatorname{span} \left\{g ^ {2} \right\}, \quad i = 1, \dots , k. \end{array} \right. \tag {8.4.5}
$$
