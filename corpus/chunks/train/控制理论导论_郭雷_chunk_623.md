$$\Delta = \Omega_ {1} ^ {\perp} = \operatorname{span} \left\{\left[ e ^ {x _ {4}}, x _ {3}, 0, 1 \right] ^ {T}, \left[ 1, 1, 0, e ^ {- x _ {4}} \right] ^ {T} \right\}.$$

这正是例8.4.1中的分布．因为 $p(x)\in \Delta$ ，故局部干扰解耦问题可解．反馈控制 $u = \alpha (x) + \beta (x)v$ 和平整坐标已在例8.4.1中得到．简单计算可知在平整坐标下有

$$p = [ 1, \mathrm{e} ^ {z _ {1} + z _ {3}} + 1, 0, 0 ] ^ {\mathrm{T}},h = - \mathrm{e} ^ {z _ {3}} + \frac {1}{2} (z _ {4} + 1) ^ {- 2}.$$

最后，反馈系统变为

$$
\left\{ \begin{array}{l} \dot {z} _ {1} = \mathrm{e} ^ {z _ {2} - z _ {3}} (z _ {4} + 1) ^ {- 1} + \mathrm{e} ^ {- z _ {2} - z _ {3}} - \mathrm{e} ^ {- z _ {3}} + 1 \\ \quad + \left((\mathrm{e} ^ {z _ {1} + z _ {3}} - 2) ^ {- 1} \mathrm{e} ^ {- z _ {3}} + z _ {2}\right) v + w, \\ \dot {z} _ {2} = \mathrm{e} ^ {z _ {2}} (z _ {4} + 1) - 1 + (\mathrm{e} ^ {z _ {1} + z _ {3}} - \mathrm{e} ^ {z _ {3}}) v + (\mathrm{e} ^ {z _ {1} + z _ {3}} + 1) w, \\ \dot {z} _ {3} = \mathrm{e} ^ {- z _ {3} - 1} - \mathrm{e} ^ {- z _ {3}} v, \\ \dot {z} _ {4} = (z _ {4} + 1) ^ {3} v, \\ y = - \mathrm{e} ^ {z _ {3}} + \frac {1}{2} (z _ {4} + 1) ^ {- 2}. \end{array} \right. \tag {8.4.27}
$$

方程 (8.4.27) 清楚地表明干扰被解耦了.

下面考虑能控不变分布.

给定一个有限向量场集合

$$X = \{X _ {1}, \dots , X _ {t} \},$$

及一个分布

$$\Delta_ {0} \subset \operatorname{span} \left\{X _ {1}, \dots , X _ {t} \right\}.$$

设包含 $\Delta_0$ 且 $X$ 不变的最小分布为 $\Delta$ , 记作

$$\Delta = \left\langle X _ {1}, \dots , X _ {\ell} \mid \Delta_ {0} \right\rangle .$$

设 $\{Y_1, \dots, Y_s\} \subset \operatorname{span}\{X_1, \dots, X_t\}$ , 且

$$\Delta_ {0} = \operatorname{span} \left\{Y _ {1}, \dots , Y _ {s} \right\}.$$

则 $\Delta$ 也可表示为

$$\Delta = \left\langle X _ {1}, \dots , X _ {t} \mid Y _ {1}, \dots , Y _ {s} \right\rangle .$$

为得到 $\Delta$ ，我们给出以下算法：

$$
\left\{ \begin{array}{l} \Delta_ {0} = \Delta_ {0}, \\ \Delta_ {k + 1} = \Delta_ {k} + \sum_ {i = 1} ^ {t} [ X _ {i}, \Delta_ {k} ], \quad k \geqslant 0. \end{array} \right. \tag {8.4.28}
$$

于是有

引理8.4.3 (1) $\Delta_{k} \subset \Delta, k \geqslant 0$ ; (2) 如果存在一个 $k^{*}$ 使得 $\Delta_{k^{*} + 1} = \Delta_{k^{*}}$ , 则 $\Delta = \Delta_{k^{*}}$ .

证明 结论 (1) 显然成立. 由结论 (1) 可得

$$\Delta_ {0} \subset \Delta_ {k ^ {*}} \subset \Delta .$$

但从方程 (8.4.28) 可知

$$\Delta_ {k ^ {*} + 1} = \Delta_ {k ^ {*}} + \sum_ {i = 1} ^ {t} [ X _ {i}, \Delta_ {k ^ {*}} ] = \Delta_ {k ^ {*}},$$

故

$$[ X _ {i}, \Delta_ {k ^ {*}} ] \subset \Delta_ {k ^ {*} + 1} = \Delta_ {k ^ {*}},$$

下面我们回答何时 $k^{*}$ 存在.

引理 8.4.4 设 $X_{1}, \cdots, X_{t} \in V^{\infty}(M)$ ，则存在一开稠子集 $U \subset M$ ，使得

$$\Delta (x) = \Delta_ {k ^ {*}} (x), \qquad x \in U. \tag {8.4.29}$$
