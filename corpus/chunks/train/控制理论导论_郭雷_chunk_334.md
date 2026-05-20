# 条件正态过程的递推滤波

上一节式 (4.4.6) 给出了用 $y$ 对 $x$ 的线性无偏最小方差估计。现在要问，当允许用 $y$ 的非线性函数 $g(y)$ 来估计 $x$ 时，无偏最小方差估计是什么？我们把它作为引理叙述如下：

引理 4.4.2 设 x, y 分别是 n 维和 m 维随机向量， $E\|x\|^{2}<\infty$ 。记 $F \stackrel{\operatorname{def}}{=} \{g : R^{m} \to R^{n}, E\|g(y)\|^{2}<\infty\}$ 。那么 $E(x|y)$ 是用 y 对 x 的最小方差估计

$$E [ x - E (x | y) ] [ x - E (x | y) ] ^ {*} = \min _ {g \in F} E [ x - g (y) ] [ x - g (y) ] ^ {*}.$$

证明

$$
\begin{array}{l} E [ x - g (y) ] [ x - g (y) ] ^ {*} \\ = E [ x - E (x \mid y) + E (x \mid y) - g (y) ] [ x - E (x \mid y) + E (x \mid y) - g (y) ] ^ {*} \\ = E \left\{E ^ {y} [ x - E (x | y) + E (x | y) - g (y) ] [ x - E (x | y) + E (x | y) - g (y) ] ^ {*} \right\} \\ = E (x - E (x | y)) (x - E (x | y)) ^ {*} + E (E (x | y) - g (y)) (E (x | y) - g (y)) ^ {*} \\ \geqslant E (x - E (x | y)) (x - E (x | y)) ^ {*}. \\ \end{array}
$$

上面不等式由于 $E(x|y) - g(y)$ 对 $y$ 可测，所以交叉项为0.由此便知引理成立.

一般来说，最小方差估计不一定是线性估计，那么能否得到最小方差估计的递推形式？

在讨论正态过程和条件正态过程之前，我们先引进条件独立的概念。设 $x = [x_{1}, \cdots, x_{n}]^{T}$ ， $y = [y_{1}, \cdots, y_{m}]^{T}$ ，z 为随机向量。如果对 $(\lambda_{1}, \cdots, \lambda_{n})$ 及 $(\mu_{1}, \cdots, \mu_{m})$

$$
\begin{array}{l} P \left(x _ {1} <   \lambda_ {1}, \dots , x _ {n} <   \lambda_ {n}, y _ {1} <   \mu_ {1}, \dots , y _ {m} <   \mu_ {m} | z\right) \\ = P \left(x _ {1} <   \lambda_ {1}, \dots , x _ {n} <   \lambda_ {n} \mid z\right) \cdot P \left(y _ {1} <   \mu_ {1}, \dots , y _ {m} <   \mu_ {m} \mid z\right), \\ \end{array}
$$

那么称在 $z$ 条件下， $x$ 和 $y$ 条件独立.

引理 4.4.3 设 y 和 $(x,z)$ 独立，那么在 z 条件下，x 和 y 条件独立。这时 $P(x\in B|z,y)=P(x\in B|z)$ ， $E(x|z,y)=E(x|z)$ ，这里 B 表示 $R^{n}$ 中的 Borel 集。

证明 对任一 $C \in \mathcal{F}^z$ (由 $z$ 生成的 $\sigma$ -代数，即 $z$ 对之可测的最小 $\sigma$ -代数)，及任一 $A \in \mathbb{R}^n, B \in \mathbb{R}^m$ ，用 $y$ 和 $(x, z)$ 的独立性知

$$
\begin{array}{l} \int_ {C} I _ {[ x \in A ]} I _ {[ y \in B ]} \mathrm{d} P = \int I _ {[ x \in A ]} \cdot I _ {C} \mathrm{d} P \int I _ {[ y \in B ]} \mathrm{d} P \\ = \int_ {C} E (I _ {[ x \in A ]} | z) \mathrm{d} P E I _ {[ y \in B ]} = \int_ {C} E (I _ {[ x \in A ]} | z) E I _ {[ y \in B ]} \mathrm{d} P. \\ \end{array}
$$

但 $EI_{[y\in B]} = E(I_{[y\in B]}|z)$ ，所以

$$\int_ {C} I _ {[ x \in A ]} I _ {[ y \in B ]} \mathrm{d} P = \int_ {C} E (I _ {[ x \in A ]} | z) E (I _ {[ y \in B ]} | z) \mathrm{d} P,$$

从 $C$ 的任意性及条件期望的唯一性知，在 $z$ 条件， $x$ 和 $y$ 条件独立.

注意到

$$
\begin{array}{l} \int_ {C \cap [ y \in B ]} E (I _ {[ x \in A ]} | z, y) \mathrm{d} P = \int_ {C \cap [ y \in B ]} I _ {[ x \in A ]} \mathrm{d} P \\ = \int_ {C} I _ {[ x \in A ]} \cdot I _ {[ y \in B ]} \mathrm{d} P = \int_ {C} E \left(I _ {[ x \in A ]} \cdot I _ {[ y \in B ]} | z\right) \mathrm{d} P. \\ \end{array}
$$

用条件独立性，继续上面的等式
