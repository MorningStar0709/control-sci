$$R (x) = \left\langle \tilde {f}, \tilde {g} _ {1}, \dots , \tilde {g} _ {m} \mid \tilde {g} ^ {\Lambda} \right\rangle ,$$

即 $R(x)$ 是包含 $\tilde{g}^{\Lambda}$ 且 $\tilde{f},\tilde{g}_{1},\cdots,\tilde{g}_{m}$ 不变的最小分布，那么 $R(x)$ 称为一个能控不变子分布.

从定义明显可知能控不变子分布是 $(f,g)$ 不变分布，而且从引理8.4.5可见它也是对合的.

在某些解耦问题中, 找到包含于给定分布 $\Delta$ 中的最大能控不变分布是重要的. 设 $\Delta$ 给定, 我们给出下列算法:

$$
\left\{ \begin{array}{l} \Delta_ {0} = \Delta \cap G, \\ \Delta_ {k + 1} = \Delta \cap \left(\mathrm{ad} _ {f} \Delta_ {k} + \sum_ {i = 1} ^ {m} \mathrm{ad} _ {g _ {i}} \Delta_ {k} + G\right), \quad k \geqslant 0. \end{array} \right. \tag {8.4.34}
$$

算法 (8.4.34) 给出一个增列。事实上，显然 $\Delta_1 \supset \Delta_0$ 。设 $\Delta_k \supset \Delta_{k-1}$ 。由数学归纳法可证

$$
\begin{array}{l} \Delta_ {k + 1} = \Delta \cap \left(\operatorname{ad} _ {f} \Delta_ {k} + \sum_ {i = 1} ^ {m} \operatorname{ad} _ {g _ {i}} \Delta_ {k} + G\right) \\ \supset \Delta \cap \left(\operatorname{ad} _ {f} \Delta_ {k - 1} + \sum_ {i = 1} ^ {m} \operatorname{ad} _ {g _ {i}} \Delta_ {k - 1} + G\right) \\ = \Delta_ {k}. \\ \end{array}
$$

我们要证明在一定条件下，算法(8.4.34)给出了 $\Delta$ 中的最大能控不变子分布。为此，我们需要一些准备。

引理8.4.6 由算法(8.4.34)得出的分布列 $\{\Delta_k\}$ 与反馈 $(\alpha (x),\beta (x))$ 无关，换句话说，如果把正则反馈 $u = \alpha (x) + \beta (x)v$ 后的 $\tilde{f}$ 和 $\tilde{g}$ 代到算法(8.4.34)中，即

$$
\left\{ \begin{array}{l} \tilde {\Delta} _ {0} = \Delta \cap G, \\ \tilde {\Delta} _ {k + 1} = \Delta \cap \left(\mathrm{ad} _ {\tilde {f}} \tilde {\Delta} _ {k} + \sum_ {i = 1} ^ {m} \mathrm{ad} _ {\hat {g} _ {i}} \tilde {\Delta} _ {k} + G\right), \quad k \geqslant 0, \end{array} \right.
$$

那么 $\tilde{\Delta}_{k} = \Delta_{k}, k = 0, 1, 2, \cdots,$

证明 首先证明 $\tilde{\Delta}_{k} \subset \Delta_{k}, k = 0, 1, 2, \cdots$ 对 k = 0，显然成立。设 $\tilde{\Delta}_{k} \subset \Delta_{k}$ ，则

$$
\begin{array}{l} \tilde {\Delta} _ {k + 1} = \Delta \cap \left(\operatorname{ad} _ {\tilde {f}} \tilde {\Delta} _ {k} + \sum_ {i = 1} ^ {m} \operatorname{ad} _ {\tilde {g} _ {i}} \tilde {\Delta} _ {k} + G\right) \\ \subset \Delta \cap \left(\operatorname{ad} _ {\tilde {f}} \Delta_ {k} + \sum_ {i = 1} ^ {m} \operatorname{ad} _ {\tilde {g} _ {i}} \Delta_ {k} + G\right) \\ \subset \Delta \cap ([ f + g \alpha , \Delta_ {k} ] + [ g \beta , \Delta_ {k} ] + G) \\ \subset \Delta \cap ([ f, \Delta_ {k} ] + [ g, \Delta_ {k} ] + G) \\ = \Delta_ {k + 1}. \\ \end{array}
$$

这里 $f = \bar{f} - g\alpha$ ，及 $\tilde{g} = g(\beta)^{-1}$ . 同理可证 $\Delta_k \subset \bar{\Delta}_k, k = 0, 1, \dots$ .
