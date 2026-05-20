# 附录B 压缩映射

假定有方程 $x = T(x)$ , 称解 $x^{*}$ 为映射 $T$ 的不动点, 因为 $T$ 使得解 $x^{*}$ 不变。求解不动点的典型方法是逐次逼近法, 首先从一个初始测试向量 $x_{1}$ 开始, 计算 $x_{2} = T(x_{1})$ , 连续进行这样的迭代计算, 计算出下一个向量 $x_{k+1} = T(x_{k})$ , 压缩映射定理给出了方程 $x = T(x)$ 具有不动点 $x^{*}$ 和序列 $\{x_{k}\}$ 收敛到 $x^{*}$ 的充分条件, 这是证明方程 $x = T(x)$ 解存在的有力工具。这个定理不仅在欧氏空间中是成立的, 而且在 Banach 空间中也是成立的, 我们将在一般的背景下使用压缩映射定理。首先介绍 Banach 空间①。

向量空间: 在域 R 上的线性向量空间 X 是一个集合, 其元素为向量 x, y, z, $\cdots$ , 这些元素要满足下面的条件: 对于任意两个向量 $x, y \in X$ , 它们的求和运算满足: $x + y \in X, x + y = y + x$ 及 $(x + y) + z = x + (y + z)$ ; 存在一个零向量 $0 \in X$ , 使得对于所有 $x \in X$ , 有 $x + 0 = x$ ; 对于任意的数 $\alpha, \beta \in R$ , 数乘运算 $\alpha x$ 满足: $\alpha x \in X, 1 \cdot x = x, 0 \cdot x = 0, (\alpha \beta) x = \alpha (\beta x), \alpha (x + y) = \alpha x + \alpha y, (\alpha + \beta) x = \alpha x + \beta x$ , 其中 $x, y \in X$ 。

线性赋范空间: 线性空间 X 为线性赋范空间, 如果对于每个向量 $x \in X$ , 存在一个实值范数 $\|x\|$ , 且满足:

\- 对于所有 $x \in \mathcal{X}$ , $\| x \| \geqslant 0$ , 当且仅当 $x = 0$ 时, $\| x \| = 0$ 。

\- 对于所有 $x, y \in \mathcal{X}$ , $\| x + y \| \leqslant \| x \| + \| y \|$ 。

\- 对于所有 $\alpha \in R$ 和 $x \in \mathcal{X}$ , $\| \alpha x \| = |\alpha| \| x \|$ 。

如果在上下文中不能判断 $\|\cdot\|$ 是在 X 上的范数还是 $R^{n}$ 上的范数,那么我们将在 X 上的范数表示为 $\|\cdot\|_{X}$ 。

收敛性: 如果当 k 趋于无穷时, $\|x_{k}-x\|$ 趋于零, 则序列 $\{x_{k}\}\in\mathcal{X}$ (X为线性赋范空间) 收敛到 $x\in\mathcal{X}$ 。

闭集:集合 $S \subset X$ 是闭集, 当且仅当每个收敛序列(序列中的每一项在 S 内)的极限仍在 S 内。

Cauchy 序列: 序列 $\{x_{k}\} \in X$ 是 Cauchy 序列, 如果当 k, m 趋于无穷时, 有 $\|x_{k}-x_{m}\|$ 趋于零, 则每个收敛序列都是 Cauchy 序列, 但反之则不成立。

Banach 空间: 如果 X 中的每个 Cauchy 序列收敛到 X 中的一个向量, 则线性赋范空间 X 是完备的。完备的线性赋范空间称为 Banach 空间。

例 B.1 设所有连续函数 $f: [a, b] \rightarrow R^{n}$ 的集合为 $C[a, b]$ ，这个集合形成了 R 中的一个向量，加法 $x + y$ 定义为 $(x + y)(t) = x(t) + y(t)$ ，数乘定义为 $(\alpha x)(t) = \alpha x(t)$ ，零向量定义为 $[a, b]$ 上恒等于零的函数，定义范数为

$$\| x \| _ {C} = \max _ {t \in [ a, b ]} \| x (t) \|$$

其中等式右边的范数是指 $R^n$ 上任意的 $p$ 范数，显然， $\| x \|_C \geqslant 0$ ，并且只有 $x$ 是零向量时才等于零，三角不等式为

$$\max \| x (t) + y (t) \| \leqslant \max [ \| x (t) \| + \| y (t) \| ] \leqslant \max \| x (t) \| + \max \| y (t) \|$$

和 $\max \| \alpha x(t) \| = \max |\alpha| \| x(t) \| = |\alpha| \max \| x(t) \|$

其中所有的最大值都出现在 $[a, b]$ 上，因此， $C[a, b]$ 连同范数 $\| \cdot \|_c$ 是一个线性赋范空间。 $C[a, b]$ 也是一个Banach空间。为了证明这一点，我们首先需要证明 $C[a, b]$ 上的每个Cauchy序列都收敛到 $C[a, b]$ 上的某个向量。设 $\{x_k\}$ 是 $C[a, b]$ 上的Cauchy序列，对于每个确定的 $t \in [a, b]$ ，

$$\| x _ {k} (t) - x _ {m} (t) \| \leqslant \| x _ {k} - x _ {m} \| _ {C} \to 0 \quad {\text {当}} k, m \to \infty$$
