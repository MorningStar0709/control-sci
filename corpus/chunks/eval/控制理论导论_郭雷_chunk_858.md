证明 必要性显然. 现证充分性. 记 $b_{ij}, k_{ij}$ 为 $\pmb{B}, \pmb{K}$ 的 $i$ 行 $j$ 列元, 令 $b_{i_0j_0} \neq \varepsilon, K$ 中除 $k_{s_0i_0} \neq \varepsilon$ 外其余元都为 $\varepsilon$ . 于是, $\pmb{A} \oplus \pmb{KB}$ 仅把 $\pmb{A}$ 的第 $s_0$ 行加上行 $[k_{s_0i_0} b_{i_01}, \dots, k_{s_0i_0} b_{i_0n}]$ , 也就是 $G(A)$ 中 $s_0$ 点到各点 $j, 1 \leqslant j \leqslant n$ , 的弧上加权重 $k_{s_0i_0} b_{i_0j}$ . 由此而在 $G(\tilde{A})$ 中新增的回路记为 $\mu_k, G(A)$ 中所有过 $s_0, j$ 的回路在 $G(\tilde{A})$ 中记为 $\mu_a$ ; 用 $W(\mu)$ 表示 $\mu$ 的平均权重, $d_k, d_a$ 表示 $\mu_k, \mu_a$ 的长度, $W_{ki}$ 表示 $\mu_k$ 原有的 $d_k - 1$ 条有向弧的权重, $W_{ai}$ 表示 $\mu_a$ 的 $d_a$ 条弧的权重, 但其中 $W_{a1}$ 为 $s_0$ 到 $j$ 的弧在 $G(A)$ 中的原有权重. 我们有

$$
W \left(\mu_ {k}\right) = \frac {1}{d _ {k}} k _ {s _ {0} i _ {0}} + \frac {1}{d _ {k}} \left(\sum_ {i = 2} ^ {d _ {k}} W _ {k _ {i}} + b _ {i _ {0} j _ {s}}\right), \tag {11.6.3}
W (\mu_ {a}) = \left\{ \begin{array}{l l} \frac {1}{d _ {a}} k _ {s _ {0} i _ {0}} + \frac {1}{d _ {a}} \left(\sum_ {i = 2} ^ {d _ {a}} W _ {a i} + b _ {i _ {0} j _ {r}}\right), & \text {当} k _ {s _ {0} i _ {0}} > W _ {a i} - b _ {i _ {0} j _ {r}}, \\ \frac {1}{d _ {a}} \sum_ {i = 1} ^ {d _ {a}} W _ {a i}, & \text {否则或} \mu_ {a} \text {中} s _ {0} \text {到} j _ {r} \text {无弧}, \end{array} \right. \tag {11.6.4}
$$

式 (11.6.4) 中所有运算都是普通算术运算。式 (11.6.3) 为 $k_{s_0i_0}$ 的线性函数，式 (11.6.4) 为 $k_{s_0i_0}$ 的连续函数，是由一条水平线与向上斜线接成的折线。由于 $\tilde{\lambda}$ 是

$G(\tilde{A})$ 中临界回路的平均权重，所以

$$\widetilde {\lambda} = \max _ {k, a} \left\{W \left(\mu_ {k}\right), W \left(\mu_ {a}\right), \lambda \right\} \stackrel {\text { def }} {=} f \left(k _ {s _ {0} i _ {0}}\right), \tag {11.6.5}$$

其中 $\lambda$ 为 $A$ 的特征值。由 $A$ 不可约，可知 $f(k_{s_0i_0})$ 确实含自由参数 $k_{s_0i_0}$ 而不是常数， $f(k_{s_0i_0})$ 是取极大值后形成的折线，是连续的分段（有限段）增线性函数。当 $k_{s_0i_0} = \varepsilon$ 时，由式(11.6.3)\~(11.6.5)可知 $\tilde{\lambda} = \lambda$ ；而当 $k_{s_0i_0} \to +\infty$ 时 $\tilde{\lambda} \to +\infty$ 。所以 $f(k_{s_0i_0})$ 的值域为 $[\lambda, +\infty)$ 。对任意指定的 $\tilde{\lambda} \in [\lambda, +\infty)$ ，总可以找到 $k_{s_0i_0} = f^{-1}(\tilde{\lambda})$ ，由这个 $k_{s_0i_0}$ 形成的 $K$ 就能使 $A \oplus KB$ 的周期配置为 $\tilde{\lambda}$ 。

定理 11.6.2 $^{[10]}$ 系统 (11.5.1) 能用状态反馈配置周期的充要条件是，存在一个标准序，使得系统 (11.5.1) 的凝网中

(1) 恰有 $\omega$ 条弧 $u_{i}X_{i}, 1 \leqslant i \leqslant \omega$ ;   
(2) 没有 $u_{i}X_{j}$ 弧， $1 \leqslant j < i \leqslant \omega$ .
