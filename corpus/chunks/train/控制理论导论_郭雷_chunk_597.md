$$L _ {X _ {1}} h _ {j} (\phi_ {t _ {2}} ^ {X _ {2}} \dots \phi_ {t _ {k}} ^ {X _ {k}} (x _ {1})) = L _ {X _ {1}} h _ {j} (\phi_ {t _ {2}} ^ {X _ {2}} \dots \phi_ {t _ {k}} ^ {X _ {k}} (x _ {2})).$$

分别对 $t_{2}, t_{3}, \cdots, t_{k}$ 继续这个过程，最后可得

$$L _ {X _ {k}} L _ {X _ {k - 1}} \dots L _ {X _ {1}} h _ {j} (x _ {1}) = L _ {X _ {k}} L _ {X _ {k - 1}} \dots L _ {X _ {1}} h _ {j} (x _ {2}).$$

定理 8.2.1 的证明. 由于 $\operatorname{rank}\mathcal{H}=n$ ，故可选 n 个函数 $c_{i}(x), i=1,\cdots,n$ ，使得它们在 $x_{0}$ 点线性独立。定义映射

$$P (x) = \left[ c _ {1} (x), c _ {2} (x), \dots , c _ {n} (x) \right] ^ {T}.$$

由构造知存在 $x_0$ 的一个邻域 $U$ , 使得 $P: U \to P(U) \subset \mathbb{R}^n$ 为一微分同胚. 现在对任一 $x \in U, x \neq x_0$ , 因为 $P(x) \neq P(x_0)$ , 故由引理8.2.1得 $x \in U, x \neq x_0$ , 于是

$$I D _ {U} (x _ {0}) = \{x _ {0} \}.$$

一个自然的问题是：能观测性秩条件对局部弱能观测是否必要？我们有如下结果.

定理8.2.2 如果系统(8.1.1)是局部弱能观测的，那么能观测性秩条件在 $M$ 的一个开稠集上成立.

证明 使能观测性秩条件成立的点的集合显然是一个开集。因此只要证明它稠即可。

设存在一个非空开集 $U$ ，使得

$$\operatorname{rank} (\mathcal {H} (x)) = k < n, \qquad x \in U. \tag {8.2.5}$$

事实上, 不妨设 $k = \max_{x \in U} \operatorname{rank}(\mathcal{H}(x))$ , 于是存在一个开子集 $V \subset U$ , 使得 $\operatorname{rank}(\mathcal{H}(x) = k, x \in V$ .

于是可找到 $H$ 中的 $k$ 个函数，使所有 $\mathcal{H}$ 中的余向量场在 $V$ 上可表示为这个微分式 $\mathrm{d}c_{i}(x), i = 1, \dots, k,$ 的线性组合。构造一个局部坐标卡 $(U,z)$ ，这里 $z = [z^{1}, z^{2}]$ ，且 $z^{1} = [c_{1}, \dots, c_{k}]^{\mathrm{T}}$ 。将系统 (8.1.1) 表示为

$$
\left\{ \begin{array}{l l} \dot {z} ^ {1} = f ^ {1} (z, u), \\ \dot {z} ^ {2} = f ^ {2} (z, u), \\ y _ {j} = h _ {j} (z), & j = 1, \dots , p. \end{array} \right. \tag {8.2.6}
$$

由于 $\mathrm{d}h_j\in \mathcal{H}$ ，故 $h_j$ 只依赖于 $z^1$ ，即

$$h _ {j} (z) = h _ {j} \left(z ^ {1}\right).$$

可以证明 $f^1$ 也只依赖于 $z^1$ ，即

$$f ^ {1} (z, u) = f ^ {1} (z ^ {1}, u).$$

事实上，否则的话，例如，对某一对 $(i,j), 1 \leqslant i \leqslant k, k + 1 \leqslant j \leqslant n,$ 有

$$\frac {\partial f _ {i} ^ {1} (z , u)}{\partial z _ {j} ^ {2}} (x) \neq 0, \quad x \in U.$$

于是 $L_{f(z,u)}(c_i(x))$ 的第 $j$ 个分量为

$$\left. \mathrm{d} L _ {f (z, u)} (c _ {i} (x)) \right| _ {j} = \frac {\partial f _ {i} ^ {1} (z , u)}{\partial z _ {j} ^ {2}} (x) \neq 0.$$

因此存在 $x \in V$ 使

$$\mathrm{d} L _ {f (z, u)} \left(c _ {i} (x)\right) \notin \mathcal {H} (x),$$

这导致矛盾.

现在系统 (8.2.6) 可局部表示为

$$
\left\{ \begin{array}{l l} \dot {z} ^ {1} = f ^ {1} (z ^ {1}, u), \\ \dot {z} ^ {2} = f ^ {2} (z, u), \\ y _ {j} = h _ {j} (z ^ {1}), & j = 1, \dots , p. \end{array} \right. \tag {8.2.7}
$$

选择两点 $z_{1}, z_{2} \in U$ 使得
