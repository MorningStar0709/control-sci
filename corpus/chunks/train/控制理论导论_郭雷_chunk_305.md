# 鞅差局部收敛及 Borel-Cantelli 引理

设 $(x_{k},\mathcal{F}_{k})$ 为适应序列，且 $E(x_{k}|\mathcal{F}_{k - 1}) = 0,\forall k\geqslant 1,$ 则 $(x_{k},\mathcal{F}_{k})$ 叫鞅差列(m.d.s.).

实际上，如果 $(x_{k},\mathcal{F}_{k})$ 为鞅差列，那么 $\xi_{k}\stackrel {\mathrm{def}}{=}\sum_{j = 1}^{k}x_{j}$ 为鞅.

引理4.2.2 设 $(\xi_k, \mathcal{F}_k)$ 为适应序列， $\xi_k \in \mathbb{R}^m$ ， $G$ 是 $\mathbb{R}^m$ 中的Borel集，那么，从 $G$ 初出时间 $\tau$ 为Markov时间

$$
\tau = \left\{ \begin{array}{l l} {\inf \{k: \xi_ {k} \not \in G \},} \\ {\infty , \qquad \text {如} \xi_ {k} \in G, \forall k.} \end{array} \right.
$$

证明 注意到

$$\{\tau = k \} = \left\{\xi_ {0} \in G, \xi_ {1} \in G, \dots , \xi_ {k - 1} \in G, \xi_ {k} \notin G \right\} \in \mathcal {F} _ {k},$$

所以 $\tau$ 是Markov时间.

引理4.2.3 设 $\tau$ 为Markov时间， $(\xi_k, \mathcal{F}_k)$ 为鞅(上鞅或下鞅)，那么 $(\xi_{\tau \wedge k}, \mathcal{F}_k)$ 仍是鞅(上鞅或下鞅)，这里 $\tau \wedge k \stackrel{\mathrm{def}}{=} \min(\tau, k)$ ，所以 $\xi_{\tau \wedge k}$ 表示停止在 $\tau$ 的过程 $\xi_k$ 。

证明 从下面的表达

$$\xi_ {\tau} I _ {\{\tau \leqslant k - 1 \}} = \xi_ {0} I _ {\{\tau = 0 \}} + \dots + \xi_ {k - 1} I _ {\{\tau = k - 1 \}}$$

中可看出， $\xi_{\tau}I_{\{\tau \leqslant k - 1\}}$ 为 $\mathcal{F}_{k - 1}$ 可测.

设 $(\xi_k, \mathcal{F}_k)$ 为鞅，那么

$$
\begin{array}{l} E \left(\xi_ {\tau \wedge k} \mid \mathcal {F} _ {k - 1}\right) = E \left\{\left(\xi_ {\tau} I _ {\{\tau \leqslant k - 1 \}} + \xi_ {k} I _ {\{\tau > k - 1 \}}\right) \mid \mathcal {F} _ {k - 1} \right\} \\ = \xi_ {\tau} I _ {\{\tau \leqslant k - 1 \}} + E \left(\xi_ {k} I _ {\{\tau \leqslant k - 1 \} ^ {c}} \mid \mathcal {F} _ {k - 1}\right) \\ = \xi_ {\tau} I _ {\{\tau \leqslant k - 1 \}} + I _ {\{\tau > k - 1 \}} E (\xi_ {k} | \mathcal {F} _ {k - 1}) \\ = \xi_ {\tau} I _ {\{\tau \leqslant k - 1 \}} + I _ {\{\tau > k - 1 \}} \xi_ {k - 1} \\ = \xi_ {\tau \wedge (k - 1)}. \\ \end{array}
$$

所以 $(\xi_{\tau \wedge k},\mathcal{F}_k)$ 是鞅．对上鞅和下鞅也类似证明.

定理4.2.6 设 $(x_{k},\mathcal{F}_{k})$ 为一维鞅差列，那么当 $n\to \infty$ 时， $\xi_{n} = \sum_{k = 1}^{n}x_{k}$ 在

$$A \stackrel {\mathrm{def}} {=} \left\{\sum_ {k = 1} ^ {\infty} E (x _ {k} ^ {2} | \mathcal {F} _ {k - 1}) < \infty \right\}$$

上收敛.

证明 注意到 $\sum_{k=1}^{n+1} E(x_k^2 | \mathcal{F}_{k-1})$ 为 $\mathcal{F}_n$ 可测，根据引理4.2.2, 初出时间

$$
\tau_ {M} \stackrel {\mathrm{def}} {=} \left\{ \begin{array}{l l} {\min \Bigg \{n: n \geqslant 1,  \sum_ {k = 1} ^ {n + 1} E (x _ {k} ^ {2} | \mathcal {F} _ {k - 1}) > M \Bigg \}} \\ {\infty , \text {若}    \sum_ {k = 1} ^ {n + 1} E (x _ {k} ^ {2} | \mathcal {F} _ {k - 1}) \leqslant M} \end{array} \right.
$$
