其中 $\mu^{T}=\left[\mu_{1},\mu_{2},\cdots,\mu_{p}\right]$ 是待定的 Lagrange 乘子向量．此外， $H(x^{*}(t),u,\psi(t),t)$ 沿 $u^{*}(t)$ 达到极大，即

$$H (x ^ {*} (t), u ^ {*} (t), \psi (t), t) = \max _ {u \in \mathbb {U} _ {r}} H (x ^ {*} (t), u, \psi (t), t).$$

不难看出，求解极值问题

$$\max \left\{- 1 + \sum_ {i = 1} ^ {n} \psi_ {i} (t) f _ {i} (x ^ {*} (t), t) + \sum_ {j = 1} ^ {r} q _ {j} (x ^ {*} (t), \psi (t), t) u _ {j} \Bigg | | u _ {j} | \leqslant 1, 1 \leqslant j \leqslant r \right\},$$

等价于求极值问题

$$\sum_ {j = 1} ^ {r} \max \left\{q _ {j} (x ^ {*} (t), \psi (t), t) u _ {j} \mid | u _ {j} | \leqslant 1 \right\}.$$

但从后者容易得出， $\forall t\in[t_{0},t_{f}^{*}],j=1,2,\cdots,r,$ 有

$$
u _ {j} ^ {*} (t) = \left\{ \begin{array}{l l} 1, & \text {当} q _ {j} (x ^ {*} (t), \psi (t), t) > 0 \text {时}, \\ - 1, & \text {当} q _ {j} (x ^ {*} (t), \psi (t), t) <   0 \text {时}, \\ \text {任意值}, & \text {当} q _ {j} (x ^ {*} (t), \psi (t), t) = 0 \text {时}. \end{array} \right. \tag {7.2.6}
$$

或

$$
\left\{ \begin{array}{l l} u _ {j} ^ {*} (t) = \mathrm{sign} \left[ q _ {j} (x ^ {*} (t), \psi (t), t) \right], & j = 1, 2, \dots ; r, \\ u ^ {*} (t) = \mathrm{sign} \left[ B ^ {\mathrm{T}} (x ^ {*} (t), t) \psi (t) \right], \end{array} \right. \tag {7.2.7}
$$

而在最短过渡时刻 $t_{f}^{*}$ 成立下列等式：

$$
\begin{array}{l} - 1 + \sum_ {i = 1} ^ {n} \psi_ {i} (t _ {f} ^ {*}) f _ {i} (x ^ {*} (t _ {f} ^ {*}), t _ {f} ^ {*}) + \sum_ {j = 1} ^ {r} \left| q _ {j} (x ^ {*} (t _ {f} ^ {*}), \psi (t _ {f} ^ {*}), t _ {f} ^ {*}) \right| \\ = \sum_ {i = 1} ^ {n} \mu_ {l} \frac {\partial g _ {l} (x ^ {*} (t _ {f} ^ {*}) , t _ {f} ^ {*})}{\partial t _ {f}}. \tag {7.2.8} \\ \end{array}
$$

快速极值控制 $u(t)$ , 快速极值轨线 $x(t)$ 和相应的 Lagrange 向量值函数 $\psi(t)$ 满足

$$
\left\{ \begin{array}{l} \dot {\psi} ^ {\mathrm{T}} = - \psi^ {\mathrm{T}} \left[ \frac {\partial f (x (t) , t)}{\partial x} + \frac {\partial B (x (t) , t)}{\partial x} u (t) \right], \\ \psi^ {\mathrm{T}} (t _ {f}) = - \mu^ {\mathrm{T}} \frac {\partial g (x (t _ {f}) , t _ {f})}{\partial x _ {f}}. \end{array} \right. \tag {7.2.9}
$$

定义 7.2.1 设 $\psi(t)$ 是式 (7.2.9) 的任一非零解。如果在任意长度不为零的有限时间区间 $[t_{1}, t_{2}]$ 上， $\forall j = 1, 2, \cdots, r, q_{j}(x(t), \psi(t), t) = \sum_{i=1}^{n} b_{ij}(x(t), t) \psi_{i}(t)$ 只有有限多个零点，则式 (7.2.1) 和式 (7.2.4) 的快速控制问题是正则的，简称为正则快速控制问题，式 (7.2.1) 称为正则快速系统；如果至少存在一个 $j_{0}, 1 \leqslant j_{0} \leqslant r$ ，使得在某长度不为零的时间区间 $[\bar{t}_{1}, \bar{t}_{2}]$ 上， $q_{j_{0}}(x(t), \psi(t), t)$ 有无限多个零点，则称式 (7.2.1) 和式 (7.2.4) 的快速控制问题是奇异的，式 (7.2.1) 称为奇异快速系统， $[\bar{t}_1, \bar{t}_2]$ 称为奇异区间。
