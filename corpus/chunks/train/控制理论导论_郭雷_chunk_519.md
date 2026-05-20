# 仿射非线性系统快速控制

考虑仿射非线性系统快速控制的状态方程，初始条件，控制约束，目标集和性能指标分别为

$$
\left\{ \begin{array}{l} \dot {x} = f (x, t) + B (x, t) u, \\ x (0) = x _ {0}, \end{array} \right. \tag {7.2.1}
u \in \mathbb {U} _ {r} = \left\{u \mid | u _ {j} | \leqslant m _ {j}, \quad j = 1, 2, \dots , r \right\}, \tag {7.2.2}S \stackrel {\text { def }} {=} \left\{x \in \mathbb {R} ^ {n} \mid g (x, t _ {f}) = 0 \right\}, \tag {7.2.3}J [ u ] = \int_ {t _ {0}} ^ {t _ {f}} \mathrm{d} t = t _ {f} - t _ {0}, \tag {7.2.4}
$$

其中 $x \in R^{n}, f(x,t) = [f_{1}(x,t), \cdots, f_{n}(x,t)]^{\mathrm{T}}, g(x,t) = [g_{1}(x,t), \cdots, g_{p}(x,t)]^{\mathrm{T}}, p \leqslant n, B(x,t) = [b_{ij}(x,t)], m_{j} > 0$ 为常数， $j = 1, 2, \cdots, r, t_{f} > t_{0}, t_{f}$ 自由 (待求).

我们假定 (1) 所有分量 $f_{i}(x,t), b_{ij}(x,t), g_{k}(x,t)$ 皆是其变元的连续函数.

(2) 不失一般性取 $m_{1}=m_{2}=\cdots=m_{r}=1$ .

式 (7.2.1) 和式 (7.2.4) 的快速控制问题是指：求 $u(t) \in \mathcal{U}_{[t_0, t_f]}$ ，使得式 (7.2.4) 中的 $t_f - t_0$ 达到最小。我们利用 7.1 节中极大值原理讨论这一快速控制问题。相应的 Hamilton 函数为 $H(x, u, \psi, t)$ 为

$$
\begin{array}{l} H (x, u, \psi , t) \stackrel {\text { def }} {=} - 1 + \psi^ {\mathrm{T}} f (x, t) + \psi^ {\mathrm{T}} B (x, t) u \\ = - 1 + \sum_ {i = 1} ^ {n} \psi_ {i} f _ {i} (x, t) + \sum_ {j = 1} ^ {r} q _ {j} (x, \psi , t) u _ {j}, \\ \end{array}
$$

其中 $q_{j}(x,\psi,t)=\sum_{i=1}^{n}b_{ij}(x,t)\psi_{i},\quad j=1,2,\cdots,r.$

设 $u^{*}(t)=[u_{1}^{*}(t),u_{2}^{*}(t),\cdots,u_{r}^{*}(t)]^{\mathrm{T}}$ 是式 (7.2.1) 和式 (7.2.4) 的快速控制函数， $x^{*}(t)=[x_{1}^{*}(t),x_{2}^{*}(t),\cdots,x_{n}^{*}(t)]^{\mathrm{T}}$ 是相应的快速轨线， $t_{f}^{*}-t_{0}$ 是最短过渡时间。根据极大值原理，存在向量值函数 $\psi(t)=[\psi_{1}(t),\psi_{2}(t),\cdots,\psi_{n}(t)]^{\mathrm{T}}$ ，它和 $u^{*}(t),x^{*}(t)$ 同时满足

$$
\left\{ \begin{array}{l} \dot {x} _ {i} ^ {*} (t) = f _ {i} \left(x ^ {*} (t), t\right) + \sum_ {j = 1} ^ {r} b _ {i j} \left(x ^ {*} (t), t\right) u _ {j} ^ {*} (t), \quad x _ {i} ^ {*} \left(t _ {0}\right) = x _ {0}, \\ \dot {\psi} _ {i} (t) = - \sum_ {k = 1} ^ {n} \frac {\partial f _ {k} \left(x ^ {*} (t)\right)}{\partial x _ {i}} \psi_ {k} (t) - \sum_ {j = 1} ^ {r} u _ {j} ^ {*} (t) \left(\sum_ {k = 1} ^ {n} \frac {\partial b _ {k j} \left(x ^ {*} (t) , t\right)}{\partial x _ {i}} \psi_ {k} (t)\right), \\ \psi_ {i} \left(t _ {f} ^ {*}\right) = - \sum_ {l = 1} ^ {p} \frac {\partial g _ {l} \left(x ^ {*} \left(t _ {f} ^ {*}\right) , t _ {f} ^ {*}\right)}{\partial x _ {i}} \mu_ {l}, \quad i = 1, 2, \dots , n, \end{array} \right. \tag {7.2.5}
$$
