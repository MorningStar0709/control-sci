$$V = \{\varphi_ {j} (s, P (t)) \mid t \in U \},$$

则 $V$ 是 $P(U)$ 在微分同胚: $z \mapsto \varphi_j(s, z)$ 下的像. 因此 $V$ 为开集. 又因为 $t_i \geqslant 0, s_j \geqslant 0$ , 且 $\|t\| + \|s\| < T$ , 故

$$V \subset \bigcup_ {0 \leqslant t \leqslant T} R (x _ {0}, t),$$

这表明 $V$ 中的点为能达集内点．现在可证明 $y \in \bar{V}$ 事实上，选一序列 $\{t_k\} \subset U$ ，使得 $t_k \to 0$ ，于是由连续性

$$\lim _ {k \rightarrow \infty} \varphi_ {j} (s, P (t _ {k})) = \varphi_ {j} (s, x _ {0}) = y,$$

定理获证.

下面讨论强能接近性，我们需要一些准备.

设 $L$ 为一Lie代数， $L$ 的导出Lie代数定义为

$$L ^ {\prime} = [ L, L ] = \{[ X, Y ] \mid X, Y \in L \}. \tag {8.1.13}$$

显然导出 Lie 代数不仅是一个子代数而且是一个理想。现在我们定义 $\mathcal{F}$ 的一个子代数 $\mathcal{F}_0$

$$\mathcal {F} _ {0} = \left\{\sum_ {i = 1} ^ {s} \lambda_ {i} X _ {i} + Y \mid \lambda_ {i} \in \mathbb {R}, s \geqslant 0, \sum_ {i = 1} ^ {s} \lambda_ {i} = 0, X _ {i} \in \mathcal {F}, Y \in \mathcal {F} ^ {\prime} \right\}. \tag {8.1.14}$$

容易检验 $F_{0}$ 是一个 Lie 子代数.

定义8.1.6 考虑系统(8.1.1). Lie代数 $\mathcal{F}_0$ 称为强能控Lie代数．如果对一个点 $x_0\in M$

$$\operatorname{rank} \left(\mathcal {F} _ {0} \left(x _ {0}\right)\right) = n,$$

则称强能控秩条件在 $x_0$ 点满足，如果强能控秩条件在每一点 $x \in M$ 均满足，则称系统满足强能控秩条件.

引理8.1.1 对任一点 $x \in M$

$$\operatorname{rank} (\mathcal {F} (x)) - \operatorname{rank} (\mathcal {F} _ {0} (x)) \leqslant 1.$$

证明 实际上， $\mathcal{F} = \{F, \mathcal{F}'\}$ 且 $\mathcal{F}_0 \supset \{\mathcal{F}'\}$ . 根据 $\mathcal{F}$ 和 $\mathcal{F}_0$ 的结构可知，如果存在一个向量场 $X \in F$ ，且 $X \in \mathcal{F}_0$ ，那么 $F \subset \mathcal{F}_0$ . 结论显见.

当考虑强能接近性时，由于必须考虑时间 $t$ ，因此我们考虑时间与状态的乘积空间 $\mathbb{R} \times M$ ，并构造 $V(\mathbb{R} \times M)$ 的一个子集如下：

$$\hat {F} = \left\{\frac {\partial}{\partial t} \oplus X \mid X \in F \right\}. \tag {8.1.15}$$

记 $\hat{\mathcal{F}} = \{\hat{F}\}_{LA}$ , 为由 $\hat{F}$ 生成的 Lie 代数. 简单计算可知, 其导出 Lie 代数为

$$\hat {\mathcal {F}} ^ {\prime} = \{0 \oplus Y \mid Y \in \mathcal {F} ^ {\prime} \}.$$

因此 Lie 代数 $\hat{\mathcal{F}}$ 可表示为

$$\hat {\mathcal {F}} = \left\{\sum_ {i = 1} ^ {s} \lambda_ {i} \left(\frac {\partial}{\partial t} \oplus X\right) + 0 \oplus Y \mid \lambda_ {i} \in \mathbb {R}, X \in F, Y \in \mathcal {F} ^ {\prime} \right\}. \tag {8.1.16}$$

考虑一个扩张系统

$$
\left[ \begin{array}{l} \dot {t} \\ \dot {x} \end{array} \right] = \hat {f} = \left[ \begin{array}{c} 1 \\ f (x, u) \end{array} \right]. \tag {8.1.17}
$$

注意 $f$ 的初值为 $x_0$ 的一条积分曲线对应于 $\hat{f}$ 初值为 $(0, x_0)$ 的一条积分曲线。因此 $y \in R(x_0, T)$ ，当且仅当 $(T, y) \in \hat{R}((0, x_0))$ 。
