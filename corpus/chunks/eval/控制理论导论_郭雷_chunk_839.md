这里 $\frac{1}{\lambda} A$ 表示 $A$ 的每个元减去 $\lambda$ . 记 $(A)_{ij}$ 为 $A$ 的 $i$ 行 $j$ 列元素, $(A)_{.j}, (A)_{i}$ 分别为 $A$ 的 $j$ 列, $i$ 行. $A_{IJ}$ 或 $\{A\}_{IJ}$ 表示 $A$ 的 $I$ 行 $J$ 列块, $A_I = A_{II}$ . 用 $n_0$ 表示充分大的正整数. $\mathcal{N}_t$ 表示 $G(A_t^d), 1 \leqslant t \leqslant \omega$ , 中所有临界回路上的点的集合, $\mathcal{N} = \cup_{t=1}^{\omega} \mathcal{N}_t \cdot \mathcal{N}_{ij}$ 表示 $G(A^d)$ 中 $i$ 到 $j$ 的全部路所经过的临界回路上的点集. $G(A_t)$ 中全部临界回路形成的图记为 $G_t$ 或 $G_t(A_t)$ . $G_t$ 可以有多个连通支, 每个支可以有多条回路, 所以任一条临界回路可记为 $\gamma_{rs}^t$ , 它表示 $G_t$ 中第 $r$ 个连通支的第 $s$ 条回路. 令 $\gamma_{rs}^t$ 的长为 $d_{rs}^t$ , 记

$$d _ {r} ^ {t} = \mathrm{g.c.d} \left\{d _ {r s} ^ {t} \right\}. \tag {11.4.3}$$

式(11.4.3)表示对所有s对应的 $d_{rs}^{t}$ 取最大公约。类似地记

$$d ^ {t} = \mathrm{l.c.m} \left\{d _ {r} ^ {t} \right\}, d = \mathrm{l.c.m} \left\{d ^ {t} \right\}, \tag {11.4.4}$$

这里 l.c.m 表示取最小公倍. 于是有

$$d = \mathrm{l.c.m} \left\{\mathrm{l.c.m} \left\{g. c. d \left\{d _ {r s} ^ {t} \right\} \right\} \right\}. \tag {11.4.5}$$

从应用角度出发，先给出两个较易检验的假设：

$H_{1}: A^{d}$ 的对角块 $A_{1}^{d}, \cdots, A_{\omega}^{d}$ 均为不可约阵或一阶方阵，这里 d 如式 (11.4.5) 所示.

$H_{2}$ ：每个 $G(A_{t}), 1 \leqslant t \leqslant \omega$ ，中都有一条长为1的回路。（注意，这种回路可以称为自回路）.

文献 [17] 指出，以柔性制造系统为背景的系统一般总满足 $H_{2}$ 。由 $\pmb{A}$ 不可约 $\Longleftrightarrow G(A)$ 强连通，易知从 $H_{2}$ 可推导出 $H_{1}$ 。

定义11.4.2 若 $\lambda \neq -\infty$ ，且存在正整数 $n_0$ 使得

$$\boldsymbol {A} ^ {d + n} = \lambda^ {d} \boldsymbol {A} ^ {n}, \quad \forall n > n _ {0}, \tag {11.4.6}$$

则称 A 是 d 阶 $\lambda$ 周期阵．这里 D 中乘法为普通加法， $\lambda^{d}$ 就是普通的 $d\lambda$ .

定理 11.4.2 $^{[13]}$ 在假设 $H_{1}$ 之下，(i) A 为 d 阶 $\lambda$ 周期阵的充要条件是：对 $A_{t}, 1 \leqslant t \leqslant \omega$ 的特征值 $\lambda_{t}$ 有 $\lambda_{t} = \lambda$ ，即 $A_{t}$ 有相同的特征值。当这个条件满足时，阶数 d 可由式 (11.4.5) 所示，且有以下 (ii)，(iii) 成立：

(ii) 令

$$Q _ {h} = \lim _ {n \rightarrow + \infty} A _ {\lambda} ^ {d n + h}, \quad 0 \leqslant h \leqslant d - 1. \tag {11.4.7}$$

则

$$\boldsymbol {Q} _ {0} = \sum_ {i _ {0} \in \mathcal {N}} (\boldsymbol {A} _ {\lambda} ^ {d}) _ {i _ {0}} ^ {+} \otimes (\boldsymbol {A} _ {\lambda} ^ {d}) _ {i _ {0}} ^ {+}, \quad \boldsymbol {Q} _ {h} = \boldsymbol {Q} _ {0} \boldsymbol {A} _ {\lambda} ^ {h}, \tag {11.4.8}$$

其中乘 $\otimes$ 定义为 $((x_{1}\dots x_{N})^{\mathrm{T}}\otimes (y_{1}\dots y_{N}))_{ij} = x_{i}y_{j};$

(iii) 动态方程 (11.4.2) 的解为

$$\boldsymbol {X} (k) = \lambda^ {k} \boldsymbol {X} (0) \boldsymbol {Q} _ {h}, \tag {11.4.9}$$
