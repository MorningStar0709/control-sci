$$\left\langle \mathrm{d} h _ {i}, \Delta_ {j} \right\rangle (x) = 0.$$

设上式在 $x_0$ 不成立，则存在 $x_0$ 的一个 $U$ 邻域使得

$$\langle \mathrm{d} h _ {i}, \Delta_ {j} \rangle (x) \neq 0, \quad x \in U.$$

由于 $\Delta_{j}$ 的正则点集为开稠集，故存在 $x \in U$ 使得 $\Delta_{j}$ 在 $x$ 邻域有定常维数。于是 $\Delta_{j}$ 能在一个局部坐标卡 $(V, z), V \subset U, z = (z^{1}, z^{2})$ 中表示为 $T(S)$ ，这里 $S = \{z \in V \mid z^{2} = 0\}$ 是 $\Delta_{j}$ 的积分流形。于是由 $g_{j}$ 生成的能控性李代数在 $S$ 上是满秩的，故 $v_{j}$ 的能达集包含 $S$ 的一个开集。但现在 $\langle \mathrm{d}h_i,\Delta_j\rangle (x)\neq 0,h_i(z)$ 只依赖于 $z^1$ ，所以显然 $u_{j}$ 不影响 $y_{i}$

(充分性) 定义

$$\Omega_ {i} = \operatorname{span} \left\{\mathrm{d} L _ {X _ {1}} \dots L _ {X _ {s}} h _ {i} (x) \mid X _ {t} \in F, \quad 1 \leqslant t \leqslant s \right\}.$$

于是存在 $M$ 的一个开稠集 $W$ 使得 $\Omega_{i}$ 在每一点 $x \in W$ 上是正则的。因此对每一点 $x \in W$ ，我们都能得到一个局部坐标卡 $(V, z)$ 使得

$$\Omega_ {i} ^ {\perp} = \operatorname{span} \left\{\frac {\partial}{\partial z ^ {1}} \right\}.$$

现在将系统 (8.5.1) 局部表示为

$$
\left\{ \begin{array}{l} \dot {z} ^ {1} = f ^ {1} (z) + \sum_ {k = 1} ^ {m} g _ {k} ^ {1} (z) u _ {k}, \\ \dot {z} ^ {2} = f ^ {2} (z) + \sum_ {k = 1} ^ {m} g _ {k} ^ {2} (z) u _ {k}, \\ y _ {i} = h _ {i}, \quad i = 1, \dots , p. \end{array} \right. \tag {8.5.8}
$$

由于 $\mathrm{d}h_{i}\in \Omega_{i}$ ，故有

$$y _ {i} = h _ {i} (z ^ {2}).$$

因为 $\Omega_{i}^{\perp}$ 是 f 和 $g_{k}, k=1,\cdots,m,$ 不变的，且 $g_{j}\in\Omega_{i}^{\perp}$ ，故

$$\dot {z} ^ {2} = f ^ {2} (z ^ {2}) + \sum_ {k = 1, k \neq j} ^ {m} g _ {k} ^ {2} (z ^ {2}) u _ {k}.$$

因此，系统(8.5.1)成为

$$
\left\{ \begin{array}{l} \dot {z} ^ {1} = f ^ {1} (z) + \sum_ {k = 1} ^ {m} g _ {k} ^ {1} u _ {k}, \\ \dot {z} ^ {2} = f ^ {2} (z ^ {2}) + \sum_ {k = 1, k \neq j} ^ {m} g _ {k} ^ {2} (z ^ {2}) u _ {k}, \\ y _ {i} = h _ {i} (z ^ {2}), \\ y _ {t} = h _ {t}, \quad t \neq i. \end{array} \right. \tag {8.5.9}
$$

很明显， $u_{j}$ 不影响 $y_{i}$ ，这可表示为

$$\frac {\partial h _ {i}}{\partial u _ {j}} = 0, \qquad x \in W. \tag {8.5.10}$$

对系统 (8.5.1) 我们可以将输入输出映射表示为

$$h _ {i} = (x _ {0}, u _ {1}, \dots , u _ {m}).$$

如果 $u_{j}$ 影响 $y_{i}$ , 那么至少有一个点 $x \in M$ 使得

$$\left. \frac {\partial h _ {i}}{\partial u _ {j}} \right| _ {x} \neq 0.$$

于是由连续性，存在 $x$ 的一个邻域，使在其上导数 $\frac{\partial h_i}{\partial u_j}$ 不为零，而这与式(8.5.10)矛盾.

局部输入输出解耦问题定义如下：

定义8.5.2 在 $x_0 \in M$ 的局部输入输出解耦问题是指找一个 $x_0$ 的邻域 $U$ 和一个正则反馈 $(\alpha(x), \beta(x))$ ，使得对局部反馈系统

$$\dot {x} = \tilde {f} + \sum_ {j = 1} ^ {m} \tilde {g} _ {j} v _ {j}, \qquad x \in U,$$

存在一个分割 $v = (v^{1}, \cdots, v^{p})$ ，使得当 $x \in U$ 时，每一个 $v^{i}$ 控制 $h_{i}$ 且不影响 $h_{j}, j \neq i$ .
