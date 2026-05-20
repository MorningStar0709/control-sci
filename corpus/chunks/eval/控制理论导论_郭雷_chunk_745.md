# 10.2 无穷维线性系统的能控性和能观测性

对于一个实际的工程或社会系统来说，控制的目的就是把系统引导到某个期望的状态。我们考虑如下线性控制系统：

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} x}{\mathrm{d} t} = A x (t) + B u (t), \\ x (0) = x _ {0} \in X, \end{array} \right. \tag {10.2.1}
$$

其中 $A$ 是Banach空间 $X$ (称为状态空间) 中 $C_0$ 半群 $T(t)$ 的生成算子， $x(t) \in X$ 为状态变量， $u(t)$ 属于另一个Banach空间 $U$ (控制空间)，而 $B \in \mathcal{L}(U, X)$ ，这里 $\mathcal{L}(U, X)$ 是 $U$ 到 $X$ 的有界线性算子构成的Banach空间。

今后方程 (10.2.1) 的解总是理解为温和解

$$x (t) \stackrel {\text { def }} {=} x (t; x _ {0}, u) = T (t) x _ {0} + \int_ {0} ^ {t} T (t - s) B u (s) \mathrm{d} s, \tag {10.2.2}$$

其中 $u \in L^{p}(0, t_{f}; U)$ , $t_{f} > 0$ 和 $p > 1$ 为固定的两个正常数。方程 (10.2.1) 或方程 (10.2.2) 叫做状态方程。

当 $X = \mathbb{R}^n$ 和 $U = \mathbb{R}^m$ 时， $A$ 和 $B$ 是适当阶数的矩阵。我们说系统 (10.2.1) 完全能控，是指对于任意给定的两个状态 $x_0$ 和 $x_f \in \mathbb{R}^n$ ，必存在有限时间 $t_f > 0$ 和控制 $u \in L^1(0, t_f; \mathbb{R}^m)$ 使得 $x(t_f; x_0, u) = x_f$ 。对于大多数实际的无穷维系统来说，这样的能控性定义是很难满足的。实际上，我们可以证明如果 $B$ 是一列有穷秩线性算子 $B_n$ 在一致算子拓扑下的极限，则系统 (10.2.1) 在上述意义下是不能控的。由于我们始终假定 $X$ 是无穷维空间，根据紧算子的 Riesz-Shauder 理论，紧线性算子的值域不可能是闭的。因此为了看出系统 (10.2.1) 在上述意义下不能控，我们只需证明由

$$\Lambda u = \int_ {0} ^ {t _ {f}} T (t) B u (t) \mathrm{d} t$$

定义的算子 $\Lambda: L^{1}(0, t_{f}; U) \to X$ 是一紧算子。这里对于任意 $p \geqslant 1, L^{p}(a, b; U)$ 为所有满足 $\| \varphi(\cdot) \| \in L^{p}(a, b)$ 的抽象可测函数 $\varphi: [a, b] \to U$ 全体构成的 Banach 空间，范数定义为 $\| \varphi \| = \left( \int_{a}^{b} \| \varphi(t) \|^{p} \mathrm{d}t \right)^{1/p}$ .

首先我们假定 $B$ 是有穷维的，即 $B$ 可以表示成形式

$$B u = \sum_ {j = 1} ^ {m} \langle u, u _ {j} ^ {*} \rangle b _ {j}, \quad u \in U,$$

其中 $u_{1}^{*},\cdots,u_{m}^{*}\in U^{*},b_{1},\cdots,b_{m}\in X$ 是给定元。对于任意固定的正整数 n，令

$$t _ {k} = k t _ {f} / n, \quad k = 0, 1, \dots , n,$$

并定义算子 $F_{n}: L^{1}(0, t_{f}; U) \to X$ ,

$$F _ {n} u = \sum_ {k = 1} ^ {n} \sum_ {j = 1} ^ {m} T (t _ {k}) b _ {j} \int_ {t _ {k - 1}} ^ {t _ {k}} \langle u (t), u _ {j} ^ {*} \rangle \mathrm{d} t.$$

显然 $F_{n}$ 是一紧线性算子，现在我们证明 $F_{n}$ 按一致算子拓扑收敛于 $F$

$$F u = \int_ {0} ^ {t _ {f}} T (t) B u (t) \mathrm{d} t, \quad u \in L ^ {1} (0, t _ {f}; U).$$

事实上，由于 $T(t)b_{j}$ 对于 $t \geqslant 0$ 是连续的，故对于任意给定的 $\varepsilon > 0$ ，我们可选择一充分大的自然数 $n_{0}$ ，使得当 $n > n_{0}$ 时有

$$\| T (t) b _ {j} - T \left(t _ {k}\right) b _ {j} \| < \varepsilon , \quad \forall t \in \left(t _ {k - 1}, t _ {k}\right), 1 \leqslant k \leqslant n, 1 \leqslant j \leqslant m.$$

于是当 $n > n_0$ 时，成立
