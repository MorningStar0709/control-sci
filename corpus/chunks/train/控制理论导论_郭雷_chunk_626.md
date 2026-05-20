引理8.4.7 设 $\Delta$ 是对合，并且是 $(f, g)$ 不变分布， $G \cap \Delta$ 是非奇异的，而且对于算法(8.4.34)，存在一个 $k^*$ 使得 $\Delta_{k^*} = \Delta_{k^{*} + 1}$ ，则 $\Delta_{k^*}$ 是一个包含于 $\Delta$ 的能控不变分布。

证明 由于 $\Delta$ 是 $(f,g)$ 不变的，故存在一个反馈使得对系统(8.4.33)有

$$
\left\{ \begin{array}{l} {[ \tilde {f}, \Delta ] \subset \Delta} \\ {[ \tilde {g}, \Delta ] \subset \Delta .} \end{array} \right. \tag {8.4.35}
$$

设 $\{\bar{g}_{1},\cdots,\bar{g}_{s}\}$ 为 $G\cap\Delta$ 的一组基。由于 $\Delta$ 是对合的，则

$$[ \bar {g} _ {i}, \Delta ] \subset \Delta , \quad i = 1, \dots , s.$$

现在我们从 $\{\tilde{g}_{1},\cdots,\tilde{g}_{m}\}$ 选择 m-s 个向量场，设为 $\{\tilde{g}_{s+1},\cdots,\tilde{g}_{m}\}$ ，使得

$$\{\bar {g} _ {1}, \dots , \bar {g} _ {s}, \quad \bar {g} _ {s + 1}, \dots , \bar {g} _ {m} \}$$

成为 G 的一个基底，而且对这组基 (8.4.35) 仍然成立。因此我们简单地记 $\tilde{g}_{i} = \bar{g}_{i}, i = 1, \cdots, s$ 。利用这组基，我们可构造一个分布列

$$
\left\{ \begin{array}{l} \bar {\Delta} _ {0} = \Delta \cap G, \\ \bar {\Delta} _ {k + 1} = \mathrm{ad} _ {\bar {f}} \bar {\Delta} _ {k} + \sum_ {i = 1} ^ {m} \mathrm{ad} _ {\bar {g} _ {i}} \bar {\Delta} _ {k} + \bar {\Delta} _ {0}, \quad k \geqslant 0. \end{array} \right.
$$

式 (8.4.35) 保证了

$$\bar {\Delta} _ {k} \subset \Delta .$$

于是

$$\Delta_ {k} = \Delta_ {k}.$$

由此可见存在 $k^{*}$ 使得 $\bar{\Delta}_{k^{*}} = \bar{\Delta}_{k^{*} + 1}$ . 再由 $\bar{\Delta}_k$ 的构造可知

$$\Delta_ {k ^ {*}} = \bar {\Delta} _ {k ^ {*}} = \left\langle \tilde {f}, \tilde {g} _ {1}, \dots , \tilde {g} _ {m} \mid G \cap \Delta \right\rangle .$$

定理 8.4.4 设 $\Delta$ 是对合且是 $(f,g)$ 不变分布， $G \cap \Delta$ 是非奇异的，而且对于算法 (8.4.34)，存在一个 $k^{*}$ ，使得 $\Delta_{k^{*}} = \Delta_{k^{*}+1}$ ，则 $\Delta_{k^{*}}$ 是包含于 $\Delta$ 的最大能控不变子分布。

证明 从引理8.4.7易知 $\Delta_k$ 是一个能控不变子分布。因此我们只需证明它是最大的一个。设存在另一个反馈对 $(\bar{\alpha},\bar{\beta})$ ，及 $\bar{f} = f + g\bar{\alpha}$ ， $\bar{g} = g\bar{\beta}$ ，使得

$$D = \left\langle \bar {f}, \bar {g} _ {1}, \dots , \bar {g} _ {m} \mid g ^ {\Lambda} \right\rangle$$

是另一个能控不变子分布， $D$ 能等价地表示为

$$D = \left\langle \bar {f}, \bar {g} _ {1}, \dots , \bar {g} _ {m} \mid D \cap G \right\rangle .$$

构造一组分布列

$$
\left\{ \begin{array}{l} \bar {\Delta} _ {0} = D \cap G, \\ \bar {\Delta} _ {k + 1} = \mathrm{ad} _ {\tilde {f}} \bar {\Delta} _ {k} + \sum_ {i = 1} ^ {m} \mathrm{ad} _ {\tilde {g} _ {i}} \bar {\Delta} _ {k} + \bar {\Delta} _ {0}, \quad k \geqslant 0. \end{array} \right. \tag {8.4.36}
$$

由于

$$\bar {\Delta} _ {k} \subset D \subset \Delta ,$$

故
