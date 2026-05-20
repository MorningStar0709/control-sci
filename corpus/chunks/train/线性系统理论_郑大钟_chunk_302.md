# 8.2 结构指数

上一节中曾经指出，多变量系统的极点和零点的一个重要特征，是极点和零点可位于复数平面上的同一位置而不构成对消。引入结构指数的目的之一，就是要以更为直观和清晰的方式来反映多变量系统的极点和零点的这一特征。这也有利于进一步研究传递函数矩阵的其他特性。

结构指数 如前所知，一个秩为 r 的传递函数矩阵 $G(s)$ 的史密斯-麦克米伦形为

$$
M (s) = \left[ \begin{array}{c c c c} \frac {\varepsilon_ {1} (s)}{\psi_ {1} (s)} & & & \\ & \ddots & & 0 \\ & & \frac {\varepsilon_ {r} (s)}{\psi_ {r} (s)} & \\ - & 0 & - & 0 \end{array} \right] = \left[ \begin{array}{c c c c} \operatorname{diag} \left\{\frac {\varepsilon_ {i} (s)}{\psi_ {i} (s)} \right\} & 0 \\ - & 0 & - & 0 \end{array} \right] \tag {8.30}
$$

其中， $G(s)$ 的极点和零点是由 $\mathrm{diag}\left\{\frac{\varepsilon_i(s)}{\psi_i(s)}\right\}$ 所定义的，它构成了 $M(s)$ 的实质性部分。进一步，用 $S_{sp}$ 表示 $G(s)$ 的有限极点和零点的集合，其定义式为

$$S _ {x p} = \{s | s \in \mathcal {C}, \varepsilon_ {i} (s) = 0 \text {或} \psi_ {i} (s) = 0, i = 1, 2, \dots , r \} \tag {8.31}$$

那么,还可将 $M(s)$ 的实质性部分表示成为

$$\operatorname{diag} \left\{\varepsilon_ {i} (s) / \psi_ {i} (s) \right\} = \prod_ {a} M _ {a} (s) \tag {8.32}$$

其中， $\alpha \in S_{zp}$ ，而

$$M _ {\alpha} (s) = \operatorname{diag} \left\{\left(s - \alpha\right) ^ {\sigma_ {1} (\alpha)}, \dots , (s - \alpha) ^ {\sigma_ {r} (\alpha)} \right\} \tag {8.33}$$

$\sigma_{i}(\alpha)$ 则是包括0在内的整数。而且，由整除性 $\varepsilon_{i}(s)|\varepsilon_{i + 1}(s)$ 和 $\psi_{i + 1}(s)|\psi_i(s)$ 进一步可知，指数 $\{\sigma_i(\alpha)\}$ 是一个非降序列：

$$\sigma_ {1} (\alpha) \leqslant \sigma_ {2} (\alpha) \leqslant \dots \leqslant \sigma_ {r} (\alpha) \tag {8.34}$$

于是，我们称集合 $\{\sigma_{1}(\alpha),\sigma_{2}(\alpha),\cdots,\sigma_{r}(\alpha)\}$ 为 $G(s)$ 在 $\alpha$ 处的结构指数。

例 已知传递函数矩阵

$$
G (s) = \left[ \begin{array}{c c} \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}} & \frac {s}{(s + 2) ^ {2}} \\ \frac {- s}{(s + 2) ^ {2}} & \frac {- s}{(s + 2) ^ {2}} \end{array} \right]
$$

的史密斯-麦克米伦形为

$$
M (s) = \left[ \begin{array}{c c} \frac {s}{(s + 1) ^ {2} (s + 2) ^ {2}} & 0 \\ 0 & \frac {s ^ {2}}{(s + 2)} \end{array} \right]
$$

易知， $S_{zp} = \{-2, -1, 0\}$ ，且可将 $M(s)$ 表为

$$
\begin{array}{l} M (s) = \operatorname{diag} \left\{\varepsilon_ {i} (s) / \psi_ {i} (s) \right\} \\ = \left[ \begin{array}{l l} (s + 2) ^ {- 2} & \\ & (s + 2) ^ {- 1} \end{array} \right] \left[ \begin{array}{l l} (s + 1) ^ {- 2} & \\ & (s + 1) ^ {0} \end{array} \right] \left[ \begin{array}{l l} s ^ {1} & \\ & s ^ {2} \end{array} \right] \\ \end{array}
$$

这表明：

$G(s)$ 在-2处的结构指数为 $\{-2, -1\}$ ,

$G(s)$ 在-1处的结构指数为 $\{-2,0\}$ ,

$G(s)$ 在 0 处的结构指数为 $\{1, 2\}$ 。

几点讨论 （1）引入结构指数的结果，使得能以统一的方式，来表征传递函数矩阵 $G(s)$ 的极点和零点。
