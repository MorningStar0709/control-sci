从而 $\beta_0(x)$ 是非奇异的，而且简单的计算可得

$$
g (x) \beta_ {0} (x) = \left[ \begin{array}{c c} * & * \\ 0 & b (x) \end{array} \right], \tag {8.4.10}
$$

这里 \* 表示无关紧要的元素. 利用 $g(x)\beta_0(x)$ 的最后 $s$ 个向量场可以张出分布 $B(x)$ 如下:

$$B (x) = \operatorname{span} \{(g (x) \beta_ {0} (x)) _ {j} \mid j = m - s + 1, m - s + 2, \dots , m \}.$$

由式 (8.4.3) 可知

$$
\left\{ \begin{array}{l} {[ f, \Delta ] \subset \Delta + B,} \\ {[ B, \Delta ] \subset \Delta + B.} \end{array} \right. \tag {8.4.11}
$$

现在，因为 $B \cap \Delta = \{0\}$ ，所以我们可利用前面得到的结果构造 $\beta_{1}(x)$ ，使得

$$[ B (x) \beta_ {1} (x), \Delta ] \subset \Delta (x). \tag {8.4.12}$$

令

$$
\beta (x) = \beta_ {0} (x) \left[ \begin{array}{c c} I _ {m - s} & 0 \\ 0 & \beta_ {1} (x) \end{array} \right],
$$

则

$$
g (x) \beta (x) = \left[ \left[ \begin{array}{c} * \\ 0 \end{array} \right] B (x) \beta_ {1} (x) \right].
$$

于是 $g(x)\beta (x)$ 的前 $m - s$ 向量场属于 $\Delta$ , 而其最后 $s$ 个向量场满足式 (8.4.12). 因此式 (8.4.2) 的第二个方程可由式 (8.4.12) 导出.

为证明式 (8.4.2) 的第一个方程，我们构造 $\alpha(x)$ . 令

$$
\left\{ \begin{array}{l} D (x) = b (x) \beta_ {1} (x), \\ \alpha (x) = - L (z) \beta_ {1} (x) (D ^ {\mathbf {T}} (x) D (x)) ^ {- 1} D ^ {\mathbf {T}} (x) f ^ {2} (x), \end{array} \right. \tag {8.4.13}
$$

这里 $L(x)$ 与式 (8.4.9) 中一样. 那么

$$
\tilde {f} = f + g \alpha = \left[ \begin{array}{c} f ^ {1} \\ f ^ {2} \end{array} \right] - \left[ \begin{array}{c} * \\ b (x) \beta_ {1} (x) (D ^ {\mathrm{T}} (x) D (x)) ^ {- 1} D ^ {\mathrm{T}} (x) f ^ {2} (x) \end{array} \right].
$$

利用式 (8.4.12), 有

$$\frac {\partial \tilde {f} ^ {2}}{\partial x _ {i}} = \frac {\partial f ^ {2}}{\partial x _ {i}} - D (x) (D ^ {\mathrm{T}} (x) D (x)) ^ {- 1} D ^ {\mathrm{T}} (x) \frac {\partial f ^ {2}}{\partial x _ {i}}. \tag {8.4.14}$$

利用式 (8.4.11), 存在 $\Gamma_{i}$ 使得

$$\frac {\partial f ^ {2}}{\partial x _ {i}} = b (x) \Gamma_ {i} (x), \quad i = 1, \dots , k.$$

因此

$$
\begin{array}{l} \frac {\partial \tilde {f} ^ {2}}{\partial x _ {i}} = b (x) \Gamma_ {i} - D (x) (D ^ {\mathrm{T}} (x) D (x)) ^ {- 1} D ^ {\mathrm{T}} (x) b (x) \Gamma_ {i} (x) \\ = b (x) \Gamma_ {i} - D (x) \left(D ^ {\mathrm{T}} (x) D (x)\right) ^ {- 1} D ^ {\mathrm{T}} (x) D (x) \beta^ {- 1} (x) \Gamma_ {i} (x) \\ = b (x) \Gamma_ {i} - D (x) \beta^ {- 1} (x) \Gamma_ {i} (x) \\ = 0. \\ \end{array}
$$

这就证明了式 (8.4.2) 的第一个方程.

例8.4.1 考虑系统
