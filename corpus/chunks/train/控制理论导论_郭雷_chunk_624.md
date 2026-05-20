证明 首先，可以证明存在一个开稠集 $U_{k} \subset M$ ，使得 $\Delta_{k}$ 在 $U_{k}$ 上是非奇异的。令 $O$ 是非空开集，且 $\Delta_{k}$ 在 $O$ 的最大维数是 $p$ 。于是由连续性，点集 $\{x \in O \mid \operatorname{rank}(\Delta_{k}(x)) = p\}$ 是开的非空集。由于 $O$ 是任意的，故非奇异点集形成一个开稠集 $U_{k}$ 。因此

$$U = \bigcap_ {i = 0} ^ {n - 1} U _ {k}$$

仍然是开稠的．现对每一个 $x \in U$ ，由于 $\operatorname{rank}(\Delta_k(x)) = \operatorname{const}$ ，故有 $k^* \leqslant n - 1$ 。因此式 (8.4.29) 成立。

事实上，我们还可以证明 $\Delta$ 是对合的.

引理 8.4.5 设 $X_{1}, \cdots, X_{t} \in V^{\infty}(M)$ ，则 $\Delta$ 是对合的.

证明 令 $U$ 为在引理8.4.4中定义的开稠集，则在 $U$ 上， $\Delta = \Delta_k$ 。是 $\mathrm{ad}_{X_{i_1}} \cdots \mathrm{ad}_{X_{i_k}} Y_j, k \leqslant n - 1, 1 \leqslant j \leqslant s$ 的线性组合。可以证明

$$\left[ \mathrm{ad} _ {X _ {i _ {1}}} \dots \mathrm{ad} _ {X _ {i _ {k}}} Y _ {j}, \Delta_ {n - 1} \right] \subset \Delta_ {k ^ {*}}. \tag {8.4.30}$$

当 $k = 0$ 时

$$\left[ Y _ {j}, \Delta_ {k ^ {*}} \right] \subset \Delta_ {k ^ {*} + 1} = \Delta_ {k ^ {*}}.$$

利用 Jacobi 恒等式，可知对于任意两个向量场 $X, Y$ 和一个分布 $\Delta$ ，有

$$[ [ X, Y ], \Delta ] \subset [ X, [ Y, \Delta ] ] + [ Y, [ X, \Delta ] ]. \tag {8.4.31}$$

现设式 (8.4.30) 对于 $k$ 成立，则对于 $k + 1$ 有

$$
\begin{array}{l} \left[ \mathrm{ad} _ {X _ {i _ {1}}} \dots \mathrm{ad} _ {X _ {i _ {k + 1}}} Y _ {j}, \Delta_ {k ^ {*}} \right] = \left[ \left[ X _ {i _ {1}}, \mathrm{ad} _ {X _ {i _ {2}}} \dots \mathrm{ad} _ {X _ {i _ {k + 1}}} Y _ {j} \right], \Delta_ {k ^ {*}} \right] \\ \subset \left[ X _ {i _ {1}}, \Delta_ {k ^ {*}} \right] + \left[ \operatorname{ad} _ {X _ {i _ {2}}} \dots \operatorname{ad} _ {X _ {i _ {k + 1}}} Y _ {j}, \Delta_ {k ^ {*}} \right] \subset \Delta_ {k ^ {*}}. \\ \end{array}
$$

因此，我们证明了式(8.4.30)，这说明 $\Delta_{k^*} = \Delta$ 是对合的。现在考虑对任一 $x \in M$ ，由于 $U \subset M$ 是稠的，故存在一序列 $\{x_k\} \subset U$ ，使得 $\lim_{k \to \infty} x_k = x$ 。对于任意两个向量场 $X, Y \in \Delta$ ，有

$$[ X, Y ] (x _ {k}) \in \Delta (x _ {k}), \quad k = 1, 2, \dots .$$

另一方面，由连续性又有

$$[ X, Y ] (x) \in \Delta (x),$$

即 $\Delta$ 是对合的.

考虑仿射非线性系统

$$\dot {x} = f (x) + \sum_ {i = 1} ^ {m} g _ {i} (x) u _ {i}. \tag {8.4.32}$$

利用正则反馈 $u = \alpha (x) + \beta (x)v$ ，我们有

$$
\left\{ \begin{array}{l} \tilde {f} = f (x) + g (x) \alpha (x), \\ \tilde {g} = g (x) \beta (x). \end{array} \right. \tag {8.4.33}
$$

式 (8.4.33) 可以是局部定义的，这时下列讨论也是指局部的情况.

令 $\Lambda\subset\{1,2,\cdots,m\}$ 为指标集的一个子集。我们表示相应的输入通道为

$$\tilde {g} ^ {\Lambda} = \{\tilde {g} _ {i} \mid i \in \Lambda \}.$$

定义 8.4.5 对系统 (8.4.32), 如果存在一个正则反馈 $u = \alpha(x) + \beta(x)v$ 和一个子集 $\Lambda \subset \{1,2,\dots,m\}$ , 使得
