# 鞅及收敛定理

鞅比独立变量和更广，应用也更广泛.

下面总设 $\{\mathcal{F}_k\}$ 为非降 $\sigma$ -代数族，即 $\mathcal{F}_i \subset \mathcal{F}_j, \forall i < j$ .

设 $\xi_{k}$ 为随机变量序列，如果对每个 $k, \xi_{k}$ 都对 $\mathcal{F}_{k}$ 可测： $\xi_{k} \in \mathcal{F}_{k}$ ，那么称 $(\xi_{k}, \mathcal{F}_{k})$ 为适应过程。

对任意 $j \leqslant k$ ，如果 $E(\xi_k | \mathcal{F}_j) = \xi_j$ a.s.，则适应过程 $(\xi_k, \mathcal{F}_k)$ 叫鞅。如果 $E'(\xi_k | \mathcal{F}_j) \leqslant \xi_j$ a.s.，则 $(\xi_k, \mathcal{F}_k)$ 叫上鞅，如果 $E(\xi_k | \mathcal{F}_j) \geqslant \xi_j$ a.s.，则 $(\xi_k, \mathcal{F}_k)$ 叫下鞅。

例 4.2.1 设 $\{X_{j}\}$ 为 iid 序列， $EX_{j}=0,\forall j,$ 记 $\xi_{k}\stackrel{\operatorname{def}}{=} \sum_{j=1}^{k}X_{j},\mathcal{F}_{k}\stackrel{\operatorname{def}}{=} \sigma\{X_{1},\cdots,X_{k}\}$ ，那么 $(\xi_{k},\mathcal{F}_{k})$ 为适应序列。现证它是鞅

$$E (\xi_ {k} | \mathcal {F} _ {j}) = E (X _ {k} + X _ {k - 1} + \dots + X _ {j + 1} + \xi_ {j} | \mathcal {F} _ {j}),$$

注意到 $X_{j + s}$ 和 $\mathcal{F}_j$ 之间的独立性，用注4.2.2，便知 $E(X_{j + s}|\mathcal{F}_j) = EX_{j + s} = 0,$ $\forall s\geqslant 1$ ，所以

$$E (\xi_ {k} | \mathcal {F} _ {j}) = \xi_ {j}.$$

例4.2.2 设 $\xi_{k}$ 仍由例4.2.1定义，那么 $\eta_{k} \stackrel{\mathrm{def}}{=} \xi_{k}^{2}$ 为下鞅.

这是因为对 $k \geqslant j$ ,

$$
\begin{array}{l} E \left(\eta_ {k} \mid \mathcal {F} _ {j}\right) = E \left\{\left. \left[ \eta_ {j} + \left(\sum_ {i = j + 1} ^ {k} X _ {i}\right) ^ {2} + 2 \xi_ {j} \sum_ {i = j + 1} ^ {k} X _ {i} \right] \right| \mathcal {F} _ {j} \right\} \\ = \eta_ {j} + E \left(\sum_ {i = j + 1} ^ {k} X _ {i}\right) ^ {2} + 2 \xi_ {j} E \left(\sum_ {i = j + 1} ^ {k} X _ {i} \mid \mathcal {F} _ {j}\right) \\ = \eta_ {j} + \sum_ {i = j + 1} ^ {k} E X _ {i} ^ {2} \geqslant \eta_ {j} \quad \text { a   .   s   . } \\ \end{array}
$$

设随机变量 $\tau$ 取值整数集 $\{0,1,2,\cdots,\infty\}$ . 如果 $\{\tau=n\}\in\mathcal{F}_{n},\forall n,$ 那么称 $\tau$ 为 Markov 时间. 如果进一步, $P(\tau<\infty)=1,$ 那么 $\tau$ 叫停时.

引理4.2.1 设 $\{\xi_k, \mathcal{F}_k\}$ 为适应过程， $\tau$ 为Markov时间， $B$ 为Borel集．那么 $\tau$ 以后首达 $B$ 的时间

$$
\tau_ {B} = \left\{ \begin{array}{l l} {\inf \big \{n: \tau <   n,   \xi_ {n} \in B \big \},} \\ {\infty , \qquad \text {如}   \xi_ {n} \not \in B,   \forall n > \tau} \end{array} \right.
$$

为 Markov 时间.

证明 只要把 $\{\tau_B = n\}$ 表达出来

$$\{\tau_ {B} = n \} = \bigcup_ {i = 0} ^ {n - 1} \{\{\tau = i \} \bigcap \{\xi_ {i + 1} \not \in B, \dots , \xi_ {n - 1} \not \in B, \xi_ {n} \in B \} \} \in \mathcal {F} _ {n}, \quad \forall n \geqslant 0.$$
