# Markov 过程

设对任意 Borel 集 $B$ , 任意 $n$ 及任意 $0 \leqslant t_1 < t_2 \cdots < t_n < t_{n+1}$ , 若

$$P \left(\xi_ {t _ {n + 1}} \in B \mid \xi_ {t _ {1}}, \dots , \xi_ {t _ {n}}\right) = P \left(\xi_ {t _ {n + 1}} \in B \mid \xi_ {t _ {n}}\right),$$

则称 $\{\xi_t\}$ 为Markov过程，这里 $t$ 可以是离散时间也可以是连续时间。换句话说，给定了现在状态，Markov过程将来的概率分布不依赖过去。

以后要用到下面事实，我们把它归结为如下定理：

定理 4.3.1 设 $f(\lambda,\mu)$ 为定义在 $(\mathbb{R}^{l}\times\mathbb{R}^{m},\mathcal{B}^{l}\times\mathcal{B}^{m})$ 上的可测函数。设 l 维随机向量 $\xi$ 和 m 维随机向量 $\eta$ 独立，如对 $\xi$ 值域中的任一 $\lambda\in\mathbb{R}^{l},Ef(\lambda,\eta)\stackrel{\mathrm{def}}{=}g(\lambda)$ 存在。那么

$$E (f (\xi , \eta) | \xi) = g (\xi).$$

特别，当 $f(\pmb {\xi},\pmb{\eta}) = \pmb{\eta}$ 时， $E(\pmb {\eta}|\pmb {\xi}) = E\pmb{\eta}$

例 4.3.4 设对 $t \geqslant 0, x \in R^{n}$ 及 $y \in R^{m}, \Phi(t, x, y)$ 是可测函数， $\xi_{0}, w_{1}, w_{2}, \cdots$ 相互独立．那么

$$\xi_ {k + 1} = \Phi (k + 1, \xi_ {k}, w _ {k + 1}). \quad k \geqslant 0$$

是 Markov 过程. 这是因为对任一 Borel 集 $B$ . 用定理 4.3.1 知

$$
\begin{array}{l} P (\Phi (k + 1. \xi_ {k}. w _ {k + 1}) \in B | \xi_ {0}, \dots , \xi_ {k}) \\ = P \left(\Phi (k + 1, x, w _ {k + 1}) \in B\right) | _ {x = \xi_ {k}} \\ = P \left(\Phi (k + 1, \xi_ {k}, w _ {k + 1}) \in B | \xi_ {k}\right). \\ \end{array}
$$

如果 $\xi_{t}$ 的取值为可列个，不妨用正整数来表示 $\xi_{t}$ 的取值，那么Markov过程称为Markov链.

对 $\forall s \leqslant t, p(s, t; i, j) \stackrel{\mathrm{def}}{=} P(\xi_t = j|\xi_s = i)$ , 称为 Markov 链的转移概率. $p(0, j) \stackrel{\mathrm{def}}{=} P(\xi_0 = j)$ 称为 Markov 链的初始分布.

显然

$$p (s, t; i, j) \geqslant 0, \quad \sum_ {j = 0} ^ {\infty} p (s, t; i, j) = 1.$$

对任意 $s \leqslant t \leqslant \tau$ ,

$$\sum_ {k = 0} ^ {\infty} p (s, t; j, k) p (t, \tau ; k, l) = p (s, \tau ; j, l) \tag {4.3.6}$$

称为 Kolmogorov-Chapman 方程.

记第 $j$ 行 $k$ 列的元为 $p(s, t; j, k)$ 的矩阵为 $P(s, t)$ . 那么 Kolmogorov-Chapman 方程可改写成

$$P (s, t) P (t, \tau) = P (s, \tau), \quad \forall s < t < \tau . \tag {4.3.7}$$

当 $\xi_t$ 平稳时： $P(s,s + t) = P(0,t),\forall s,t\geqslant 0.$ 记 $P(t)\stackrel {\mathrm{def}}{=}P(0,t).$

当 $t$ 为离散时间时， $P(k) = (P(1))^k, k$ 为正整数，这时把 $P(1)$ 记为 $P$ ，它的 $i$ 行 $j$ 列的元记为 $p_{ij}$ ，而 $P^n = P(n)$ 的 $i$ 行 $j$ 列元记为 $p_{ij}(n)$ ，对离散时间时齐 Markov 链，转移概率阵就是指 $P$ 。

如果存在 $n \geqslant 0$ , 使 $p_{ij}(n) > 0$ , 称状态 $i$ 可达 $j$ , 记为 $i \to j$ . 如果 $i \to j$ , 且 $j \to i$ , 称 $i$ 和 $j$ 互通, 记为 $i \leftrightarrow j$ . 设 $A$ 为状态集, 如果对任 $\cdot i \in A$ , $\sum_{j \in A} p_{ij} = 1$ , 则称 $A$ 为闭集. 如果 Markov 链的状态集不含真的闭子集, 则称 Markov 链为不可约.

如果从状态 $i$ 出发，在有限步内必回到 $i$ ，则称 $i$ 为常返的，也就是
