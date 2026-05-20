$$
\begin{array}{l} Q _ {o} A Q _ {c} = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] A [ B A B \dots A ^ {n - 1} B ] = \left[ \begin{array}{c} \bar {C} \\ \bar {C} \bar {A} \\ \vdots \\ \bar {C} \bar {A} ^ {n - 1} \end{array} \right] \bar {A} [ \bar {B} \bar {A} \bar {B} \dots \bar {A} ^ {n - 1} \bar {B} ] \\ - \overline {{Q}} _ {o} \overline {{A}} \overline {{Q}} _ {e} \tag {9.31} \\ \end{array}
$$

于是，由此即可导出

$$\overline {{A}} = (\overline {{Q}} _ {o} ^ {T} \overline {{Q}} _ {o}) ^ {- 1} \overline {{Q}} _ {o} ^ {T} Q _ {o} A Q _ {c} \overline {{Q}} _ {c} ^ {T} (\overline {{Q}} _ {c} \overline {{Q}} _ {c} ^ {T}) ^ {- 1}= T ^ {- 1} A T \tag {9.32}$$

从而就完成了证明。

实现的最小维数 在某些问题中,我们可能只对最小实现的维数(也即实现的最小维数)感兴趣。在这种情况下,没有必要定出最小实现的具体形式,而可根据给定传递函数矩阵 $G(s)$ 直接确定实现的最小维数。下面给出的一些结论,提供了计算最小维数的可能方法。

结论1 给定传递函数矩阵 $G(s)$ ，设其为严格真的，再将 $G(s)$ 表为

$$G (s) = \sum_ {i = 1} ^ {\infty} h _ {i} s ^ {- i} \tag {9.33}$$

其中 $\{h_{i}, i=1,2,\cdots\}$ 为马尔柯夫（Markov）参数矩阵。现定义如下的汉克尔（Hankel）矩阵

$$
H \triangleq \left[ \begin{array}{l l l} h _ {1} & h _ {2} & h _ {3} \dots \\ h _ {2} & h _ {3} & h _ {4} \dots \\ h _ {3} & h _ {4} & h _ {5} \dots \\ \vdots & \vdots & \vdots \end{array} \right] \tag {9.34}
$$

则 $G(s)$ 的任一状态空间实现的最小维数为

$$n _ {\min} = \operatorname{rank} H \tag {9.35}$$

证 令 $\{A, B, C\}$ 为给定 $G(s)$ 的一个最小实现, 其维数为 $n_{\min}$ 且简写为 $n_0$ 则由

$$\sum_ {i = 1} ^ {\infty} h _ {i} s ^ {i} = C (s I - A) ^ {- 1} B = \sum_ {i = 1} ^ {\infty} C A ^ {i - 1} B s ^ {- i} \tag {9.36}$$

可导出

$$h _ {i} = C A ^ {i - 1} B, i = 1, 2, \dots \tag {9.37}$$

再令

$$
Q _ {c} = \left[ \begin{array}{l l} B & A B \dots A ^ {n - 1} B \end{array} \right], Q _ {o} = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] \tag {9.38}
$$

又可得到

$$
\begin{array}{l} H (n, n) = \left[ \begin{array}{l l l} h _ {1} & h _ {2} & \dots h _ {n} \\ h _ {2} & h _ {3} & \dots h _ {n + 1} \\ \vdots & \vdots & \vdots \\ h _ {n} & h _ {n + 1} & \dots h _ {2 n - 1} \end{array} \right] = \left[ \begin{array}{c c c c} C B & C A B & \dots & C A ^ {n - 1} B \\ C A B & C A ^ {2} B & \dots & C A ^ {n} B \\ \vdots & \vdots & & \vdots \\ C A ^ {n - 1} B & C A ^ {n} B & \dots & C A ^ {2 n - 2} B \end{array} \right] \\ = Q _ {o} Q _ {c} \tag {9.39} \\ \end{array}
$$

并且，因 $(A, B, C)$ 为能控和能观测，故有

$$\operatorname{rank} Q _ {o} = \operatorname{rank} Q _ {c} = n \tag {9.40}$$

这样，由(9.39)可以导出

$$\operatorname{rank} H (n, n) \leqslant \min \left\{\operatorname{rank} Q _ {0}, \operatorname{rank} Q _ {c} \right\} = n \tag {9.41}$$

而因 $(Q_{o}^{\mathrm{T}}Q_{o})$ 为非奇异，故由(9.39)还可得到
