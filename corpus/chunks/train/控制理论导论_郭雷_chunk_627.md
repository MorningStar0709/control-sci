$$\bar {\Delta} _ {k} \subset \Delta \cap \left(\mathrm{ad} _ {\bar {f}} \Delta_ {k - 1} + \sum_ {i = 1} ^ {m} \mathrm{ad} _ {\bar {g} _ {i}} \bar {\Delta} _ {k - 1} + G\right).$$

下面我们用归纳法证明

$$\bar {\Delta} _ {k} \subset \Delta_ {k}, \quad k = 0, 1, \dots . \tag {8.4.37}$$

对于 $k = 0$ 式(8.4.37)显然成立．设对于 $\pmb{k}$ 式(8.4.37）成立，则有

$$\bar {\Delta} _ {k + 1} \subset \Delta \cap \left(\mathrm{ad} _ {\bar {f}} \Delta_ {k} + \sum_ {i = 1} ^ {m} \mathrm{ad} _ {\bar {g} _ {i}} \Delta_ {k - 1} + G\right) = \Delta_ {k + 1}.$$

利用式 (8.4.36) 及式 (8.4.37), 我们有

$$
\begin{array}{l} D = \left\langle \bar {f}, \bar {g} _ {1}, \dots , \bar {g} _ {m} \mid D \cap G \right\rangle = \sum_ {i = 0} ^ {\infty} \hat {\Delta} _ {i} \\ \subset \sum_ {i = 0} ^ {\infty} \Delta_ {i} = \sum_ {i = 0} ^ {k _ {*}} \Delta_ {i} = \Delta_ {k ^ {*}}. \\ \end{array}
$$

最后，一个自然的问题是：给定一个分布 $\Delta$ ，怎样找到 $\Delta$ 中的最大能控不变分布？

设 $\Delta$ 是非奇异且对合的。于是可定义 $\Omega_0 = \Delta^{\perp}$ 。用算法 (8.4.22)，我们能得到含于 $\Delta$ 中的最大弱 $(f, g)$ 不变分布，记作 $\Delta_I$ 。在非奇异的假设下， $\Delta_I$ 成为 $\Delta$ 中的最大 $(f, g)$ 不变分布。然后用算法 (8.4.34) 得到包含于 $\Delta_I$ 的最大能控不变分布 $\Delta_C$ 。由于一个能控不变分布也是 $(f, g)$ 不变的，包含于 $\Delta_I$ 中的最大能控不变分布 $\Delta_C$ 也是包含于 $\Delta$ 中的最大能控不变分布。

利用连续性和分布的正则性，可以证明在一个开稠集 $U \subset M$ 上，上述两个算法是可行的。即有限步后（对每个算法最多 $n - 1$ 步）， $\Delta$ 中的最大能控不变分布在每个 $x \in U$ 的邻域内局部解可由算法获得。

下面考虑块分解问题.

为此需要考虑一族分布，其中每一个对应于一块子状态.

定义 8.4.6 M 上的一组分布 $\Delta_{1}, \cdots, \Delta_{k}$ 称为在 $x_{0} \in M$ 上同时可积，如果存在 $x_{0}$ 的一个坐标邻域，比如 $(U, x)$ ，这里

$$x = \left(x _ {1} ^ {0}, \dots , x _ {n _ {0}} ^ {0}, x _ {1} ^ {1}, \dots , x _ {n _ {1}} ^ {1}, \dots , x _ {1} ^ {k}, \dots , x _ {n _ {k}} ^ {k}\right),$$

使得

$$\Delta_ {i} = \operatorname{span} \left\{\frac {\partial}{\partial x _ {j} ^ {i}} \mid j = 1, \dots , n _ {i} \right\}, \quad i = 1, \dots , k. \tag {8.4.38}$$

为叙述方便，我们引入以下记号：令 I 为指标集 $\{1,2,\cdots,m\}$ 的子集，并记

$$\Delta_ {I} := \sum_ {i \in I} \Delta_ {i},$$

以及

$$\Delta^ {- i} = \sum_ {j \neq i} \Delta_ {j}.$$

定理8.4.5 以下4个命题彼此等价：

(1) $\Delta_1, \cdots, \Delta_k$ 在 $x_0 \in M$ 上同时可积;  
(2) $\Delta_1, \cdots, \Delta_k$ 在 $x_0 \in M$ 线性无关，而且对任意的 $I \subset \{1, 2, \cdots, m\}$ ， $\Delta_I$ 在 $x_0 \in M$ 上是非奇异且对合的；  
(3) $\Delta_1, \cdots, \Delta_k$ 在 $x_0 \in M$ 上线性无关，而且分布

$$\Delta_ {i} + \Delta_ {j}, \qquad 1 \leqslant i, j \leqslant k$$

是非奇异且对合的；

(4) $\Delta_1, \cdots, \Delta_k$ 在 $x_0 \in M$ 上线性无关，而且分布

$$\Delta^ {- i}, \qquad i = 1, \dots , k \qquad {\text {及}} \quad \Delta = \sum_ {i = 1} ^ {k} \Delta_ {i}$$

是非奇异且对合的.
