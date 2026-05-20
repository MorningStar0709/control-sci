设 $(\xi_{k},\mathcal{F}_{k})$ 为下鞅，我们来定义 $\{\xi_{k}\},k=1,\cdots,N,$ 从左到右穿越区间 $(a,b)$ 的次数 $N<\infty$ . 先定义序列 $\{\tau_{i}\}$

$$
\begin{array}{l} \tau_ {0} = 0, \\ \tau_ {1} = \left\{ \begin{array}{l l} {\min \{k: 0 <   k <   N,   \xi_ {k} \leqslant a \},} \\ {N,   \text {若}    \xi_ {k} > a, \forall k = 1,   \dots , N,} \end{array} \right. \\ \tau_ {2} = \left\{ \begin{array}{l l} {\min \{k: \tau_ {1} <   k \leqslant N,   \xi_ {k} \geqslant b \},} \\ {N,    \text {若}    \xi_ {k} <   b, \forall k = \tau_ {1} + 1, \dots , N,} \end{array} \right. \\ \begin{array}{c} \bullet \\ \bullet \\ \bullet \end{array} \\ \tau_ {2 m - 1} = \left\{ \begin{array}{l l} {\min \{k: \tau_ {2 m - 2} <   k \leqslant N,   \xi_ {k} \geqslant a \},} \\ {N,   \text {若}    \xi_ {k} > a,   \forall k \in \tau_ {2 m - 2} + 1, \dots , N,} \end{array} \right. \\ \tau_ {2 m} = \left\{ \begin{array}{l l} {\min \{k: \tau_ {2 m - 1} <   k \leqslant N,   \xi_ {k} \geqslant b \},} \\ {N,    \text {若}    \xi_ {k} <   b,   \forall k \in \tau_ {2 m - 1} + 1, \dots , N.} \end{array} \right. \\ \end{array}
$$

这样使 $\xi_{r_{2m}} \geqslant b$ 的最大的 m 称为 $\{\xi_{k}\}, k = 1, \cdots, N$ 从左穿越 $(a, b)$ 的次数，记为 $\beta(a, b)$ .

从引理4.2.1知对 $k < N, \{\tau_1 = k\} \in \mathcal{F}_k$ ，而 $\{\tau_1 = N\} = \left\{\bigcup_{i=1}^{N-1} \{\tau_1 = i\}\right\}^c \in \mathcal{F}_N$ ，所以 $\tau_1$ 是Markov时间.

设 $\tau_{i}$ 为 Markov 时间，再用引理 4.2.1 知，对 k < N, $\{\tau_{i+1} = k\} \in F_{k}$ ，并且 $\{\tau_{i+1} = N\} = \left\{\bigcup_{j=0}^{N-1} \{\tau_{i+1} = j\}\right\}^{c} \in F_{N}$ ，所以 $\tau_{i}, i = 0, 1, \cdots, 2m$ 全是 Markov 时间.

定理 4.2.4 (Doob) 对下鞅 $(\xi_{k}, \mathcal{F}_{k})$ 成立下面不等式：

$$E \beta (a, b) \leqslant \frac {E (\xi_ {N} - a) ^ {+}}{b - a} \leqslant \frac {E \xi_ {N} ^ {+} + | a |}{b - a}. \tag {4.2.1}$$

这里 $\xi^{+} = \left\{ \begin{array}{ll}\xi ,\text{若} & \xi >0\\ 0, \text{若} & \xi \leqslant 0. \end{array} \right.$

证明 由于 $\{\xi_k, \mathcal{F}_k\}$ 是下鞅，所以 $(\xi_k - a, \mathcal{F}_k)$ 也是下鞅，进而从下面的一串不等式看出， $((\xi_k - a)^+, \mathcal{F}_k)$ 也是下鞅.

对 $j \leqslant k$ ,

$$
\begin{array}{l} (\xi_ {j} - a) ^ {+} \leqslant [ E ((\xi_ {k} - a) | \mathcal {F} _ {j}) ] ^ {+} = \{E [ (\xi_ {k} - a) ^ {+} - (\xi_ {k} - a) ^ {-} | \mathcal {F} _ {j} ] \} ^ {+} \\ \leqslant E ((\xi_ {k} - a) ^ {+} | \mathcal {F} _ {j}). \\ \end{array}
$$

注意到 $\{\xi_k\}$ 从左穿越 $(a, b)$ 的次数 $\beta(a, b)$ 等于 $\{\xi_k - a\}$ 从左穿越 $(0, b - a)$ 的次数 $\beta(0, b - a)$ ，而这也是 $((\xi_k - a)^+, \mathcal{F}_k)$ 从左穿越 $(0, b - a)$ 的次数。所以不失一般性，为证定理只要证明，对非负下鞅 $\{\xi_k, \mathcal{F}_k\}$ 穿越 $(0, b)$ 的次数 $\beta(0, b)$ 有如下估计：
