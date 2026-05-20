设 $P_{1}, P_{2}$ 是 $X$ 中两个投影，满足 $P_{1} + P_{2} = I$ . 那么 $X = X_{1} + X_{2}, X_{j} = P_{j}X, j = 1, 2$ . $X$ 中的一闭线性算子 $A$ 叫做被 $X_{1}$ 和 $X_{2}$ 完全约化，是指它满足

$$A (X _ {j} \cap \mathcal {D} (A)) \subset X _ {j}, \quad P _ {j} (\mathcal {D} (A)) \subset \mathcal {D} (A), \quad j = 1, 2.$$

定理5.2.2 设 $A$ 是 $X$ 中闭线性算子，并设 $\mu$ 是 $\sigma(A)$ 中的孤立点。那么

$$R (\lambda ; A) = \sum_ {k = - \infty} ^ {\infty} (\lambda - \mu) ^ {k} A _ {k}, \tag {5.2.4}$$

其中对于每一个整数 $k$

$$A _ {k} \stackrel {\text { def }} {=} \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} (\lambda - \mu) ^ {- k - 1} R (\lambda ; A) \mathrm{d} \lambda , \tag {5.2.5}$$

而 $\Gamma$ 是中心在 $\mu$ 的半径充分小的正向圆周，使得 $\Gamma \subset \rho(A)$ ，并且在 $\Gamma$ 内部除了 $\mu$ 外不再有 $\sigma(A)$ 的点。此外， $A_{-1}$ 是 $X$ 上的投影。如果 $\mu$ 是 $R(\lambda; A)$ 的 $m$ 阶极点（即 $A_{-m} \neq 0$ ，并且对于 $k < -m$ ，有 $A_k = 0$ ），则 $\mu$ 是 $A$ 的指标为 $m$ 的本征值， $\mathcal{R}(A_{-1}) = \mathcal{N}((\mu I - A)^m), \mathcal{R}(I - A_{-1}) = \mathcal{R}((\mu I - A)^k), k \geqslant m, X = \mathcal{N}((\mu I - A)^m) + \mathcal{R}((\mu I - A)^m)$ ，并且 $A$ 被此直和中出现的两个闭子空间完全约化。另外， $A$ 限制于 $\mathcal{R}(A_{-1})$ 上是有界的，其谱为单点集 $\{\mu\}$ 。最后，若 $\mathcal{R}(A_{-1})$ 是有穷维的，则 $\mu$ 是 $R(\lambda; A)$ 的极点。

对于 $X$ 中的一有界线性算子 $A, A$ 的谱半径 $\tau(A)$ 定义作

$$r (A) \stackrel {\text { def }} {=} \sup \left\{| \lambda | \mid \lambda \in \sigma (A) \right\}. \tag {5.2.6}$$

我们有

$$r (A) = \lim _ {n \rightarrow \infty} \| A ^ {n} \| ^ {1 / n}. \tag {5.2.7}$$

对于 $X$ 中的闭线性算子 $\Lambda, A$ 的本质谱 $\sigma_{e}(A)$ 是指 $\sigma(A)$ 中的至少满足如下三个条件之一的 $\lambda$ 所组成的集合：

(1) $\mathcal{R}(\lambda I - A)$ 在 $X$ 中是闭的；

(2) $\lambda$ 是 $\sigma(A)$ 的极限点;

(3) $N_{\lambda}(A)$ 是无穷维的.

对于 $X$ 中的有界线性算子 $A, A$ 的本质谱半径定义为

$$r _ {e} (A) \stackrel {\text { def }} {=} \sup \left\{| \lambda | \mid \lambda \in \sigma_ {e} (A) \right\}. \tag {5.2.8}$$

对于 $X$ 中的有界集 $M, M$ 的非紧性测度 $\gamma[M]$ 定义为

$$\gamma [ M ] \stackrel {\mathrm{def}} {=} \inf \Big \{\varepsilon > 0 | \exists \text {有穷个点} x _ {1}, \dots , x _ {m} \in X, \text {使得} M \subset \bigcup_ {k = 1} ^ {m} B (x _ {k}, \varepsilon) \Big \}.$$

对于 $A \in \mathcal{L}(X)$ , $\Lambda$ 的非紧性测度 $\gamma[A]$ 则是指这样一些 $\varepsilon > 0$ 的下确界，使得对于 $X$ 中的任意有界集 $M$ , 有 $\gamma[AM] \leqslant \varepsilon \gamma[M]$ .

非紧性测度的基本性质如下 (其中 $A, B \in \mathcal{L}(X)$ ) :
