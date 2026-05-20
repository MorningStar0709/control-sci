$$\| B ^ {*} T ^ {*} (\cdot) x \| _ {L ^ {2} (0, t _ {f}; H)} ^ {2} \geqslant t _ {f} \sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {- 2 \lambda_ {n} t _ {f}} | (x, \varphi_ {n}) | ^ {2} = t _ {f} \| T ^ {*} (t _ {f}) x \| _ {H} ^ {2}, \quad \forall x \in H.$$

因此系统 (10.2.14) 在任意有穷区间 $[0, t_f]$ 上精确零能控.

另一方面，显然系统(10.2.14)不可能在任意有穷区间 $[0, t_f]$ 上精确能控，这是因为不可能存在 $\delta > 0$ 使得

$$\sum_ {n = 1} ^ {\infty} \frac {1 - \mathrm{e} ^ {- 2 \lambda_ {n} t _ {f}}}{2 \lambda_ {n}} | (x, \varphi_ {n}) | ^ {2} \geqslant \delta \sum_ {n = 1} ^ {\infty} | (x, \varphi_ {n}) | ^ {2}, \quad \forall x \in H.$$

于是如果我们考虑系统 (10.2.14) 的对偶系统

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} z}{\mathrm{d} t} = - A z (t), \\ y (t) = z (t), \end{array} \right. \tag {10.2.15}
$$

则系统 (10.2.15) 在任意有穷区间 $[0, t_f]$ 上连续末态能观测，但不可能连续初态能观测。

类似地，系统 (10.2.14) 在任意有穷区间 $[0, t_f]$ 上近似能控，而系统 (10.2.15) 初态能观测。

例 10.2.3 设 H 是一 Hilbert 空间，A 是 H 中具有紧豫解式的正规线性算子。那么 $\sigma(A)=\left\{\lambda_{n}\mid n\geqslant1\right\}$ ，并且当 $n\to\infty$ 时 $|\lambda_{n}|\to\infty$ 。设 $\lambda_{n}$ 的重数是 $r_{n}$ ，而 $\varphi_{n1},\cdots,\varphi_{nr_{n}}$ 是 A 的对应于本征值 $\lambda_{n}$ 的 $r_{n}$ 个相互正交的规格化本征元，从而 $\left\{\varphi_{nk}\mid n\geqslant1,1\leqslant k\leqslant r_{n}\right\}$ 构成 H 的正交规格化基。假定 $\sup\left\{Re\lambda_{n}\mid n\geqslant1\right\}<\infty$ ，则 A 生成 H 的 $C_{0}$ 半群 $T(t)$

$$T (t) x = \sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {n} t} \sum_ {k = 1} ^ {r _ {n}} (x, \varphi_ {n k}) \varphi_ {n k}.$$

此外，我们假定数集 $\{\operatorname{Re} \lambda_k | k \geqslant 1\}$ 的任意非空子集中至少有一个最大数。现在我们考虑线性控制系统

$$\dot {x} = A x + B u, \tag {10.2.16}$$

其中 $B: \mathbb{R}^m \to H$ 为由下式给出的有界线性算子：

$$B u = \sum_ {j = 1} ^ {m} b _ {j} u _ {j}, \quad \forall u = [ u _ {1}, \dots , u _ {m} ] ^ {\mathbf {T}} \in \mathbb {R} ^ {m},$$

其中 $b_{1},\dots ,b_{m}$ 是 $H$ 中给定元，那么

$$B ^ {*} x = \left[ (x, b _ {1}), \dots , (x, b _ {m}) \right] ^ {\mathrm{T}}, \quad \forall x \in H.$$

因此系统 (10.2.16) 在 $[0, t_f]$ 上近似能控当且仅当

$$\sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {n} t} \sum_ {k = 1} ^ {r _ {n}} (x, \varphi_ {n k}) (\varphi_ {n k}, b _ {j}) = 0, j = 1, \dots , m, 0 \leqslant t \leqslant t _ {f} \Longrightarrow x = 0. \tag {10.2.17}$$

今证式 (10.2.17) 等价于

$$\operatorname{rank} B _ {n} = r _ {n}, \qquad \forall n \geqslant 1, \tag {10.2.18}$$

其中
