# 8.5 输入输出结构解耦

本节考虑仿射非线性系统的输入输出解耦。首先，对仿射非线性系统

$$
\left\{ \begin{array}{l l} \dot {x} = f (x) + \sum_ {i = 1} ^ {m} g _ {i} (x) u _ {i}, & x \in \mathbb {R} ^ {n}, \\ y _ {j} = h _ {j} (x), & j = 1, \dots , p, \end{array} \right. \tag {8.5.1}
$$

我们定义它的解耦矩阵.

定义 8.5.1 对于仿射非线性系统 (8.5.1), 如果存在 $\rho_{j} \geqslant 0, j = 1, \cdots, p$ , 使得在 $x_{0}$ 的一个邻域 U

$$
\left\{ \begin{array}{l l} L _ {g} L _ {f} ^ {k} h _ {j} (x) = 0, & x \in U, k <   \rho_ {j} - 1, \\ L _ {g} L _ {f} ^ {\rho_ {j} - 1} h _ {j} (x _ {0}) \neq 0. \end{array} \right. \tag {8.5.2}
$$

则向量 $(\rho_{1}(x_{0}),\cdots,\rho_{p}(x_{0}))$ 称为系统在 $x_{0}$ 的相对阶向量。如果相对阶向量在 $x\in M$ 的每一点有定义且定常，则它们可简单地记作 $(\rho_{1},\cdots,\rho_{p})$ 。

设系统 (8.5.1) 在 $x_0$ 点的相对阶向量有定义。于是我们可局部定义一个 $p \times m$ 矩阵

$$A (x) = \left(a _ {i j} (x)\right), \quad x \in U, \tag {8.5.3}$$

这里

$$a _ {i j} = L _ {g _ {j}} L _ {f} ^ {\rho_ {i} - 1} h _ {i} (x), \quad i = 1, \dots , p, j = 1, \dots , m;$$

及一个 $p$ 维向量

$$b (x) = \left(b _ {i} (x)\right), \quad x \in U, \tag {8.5.4}$$

这里

$$b _ {i} (x) = L _ {f} ^ {\rho_ {i}} h _ {i} (x), \quad i = 1, \dots , p.$$

$A(x)$ 称为解耦矩阵，而 $b(x)$ 称为解耦向量.

解耦矩阵及解耦向量在正则反馈下的变化十分重要.

命题8.5.1 设 $(\alpha(x), \beta(x))$ 为一正则反馈，并记 $\tilde{f}(x) = f(x) + g(x)\alpha(x)$ 及 $\tilde{g}(x) = g(x)\beta(x)$ . 我们构造 $\tilde{A} = (\tilde{a}_{ij})$ 及 $\tilde{b}$ 如下：

$$\tilde {a} _ {i j} (x) = L _ {\tilde {g} _ {j}} L _ {\tilde {f}} ^ {\rho_ {i} - 1} h _ {i} (x),\tilde {b} _ {i} (x) = L _ {\hat {f}} ^ {\rho_ {i}} h _ {i} (x).$$

那么

$$
\left\{ \begin{array}{l} \tilde {A} (x) = A (x) \beta (x), \\ \tilde {b} (x) = A (x) \alpha (x) + b (x). \end{array} \right. \tag {8.5.5}
$$

证明 首先证明

$$L _ {f} ^ {s} h _ {i} (x) = L _ {f} ^ {s} h _ {i} (x), \quad s < \rho_ {i}, x \in U. \tag {8.5.6}$$

对 $s = 0$ 它显然成立．设其对 $s < \rho_{i} - 1$ 成立，那么

$$
\begin{array}{l} L _ {\tilde {f}} ^ {s + 1} h _ {i} (x) = L _ {\tilde {f}} L _ {f} ^ {s} h _ {i} (x) \\ = \left(L _ {f} + \sum_ {j = 1} ^ {m} \alpha_ {j} L _ {g _ {j}}\right) L _ {f} ^ {s} h _ {i} (x) \\ = L _ {f} ^ {s + 1} h _ {i} (x). \\ \end{array}
$$

利用式 (8.5.6), 可得

$$\tilde {a} _ {i j} (x) = L _ {\bar {g} _ {i}} L _ {f} ^ {\rho_ {i} - 1} (x) = \sum_ {k = 1} ^ {m} L _ {g _ {k}} L _ {f} ^ {\rho_ {i} - 1} \beta_ {k j},$$

它证明了式 (8.5.5) 的第一个方程.

类似地，式(8.5.5)的第二个方程也可由式(8.5.6)直接得到.

命题8.5.1及其证明的一个直接推论是：

推论 8.5.1 相对阶向量在正则反馈下不变.

引理8.5.1 设

$$X _ {1}, \dots , X _ {s} \in F := \{f, g _ {1}, \dots , g _ {m} \},$$

则输入 $u_{j}$ 不影响 $y_{i}$ 的充要条件是对任意 $s > 0$

$$L _ {g _ {j}} L _ {X _ {1}} \dots L _ {X _ {s}} h _ {i} (x) = 0. \tag {8.5.7}$$

证明 (必要性) 令

$$\Delta_ {j} = \left\langle f, g _ {1}, \dots , g _ {m} \mid g _ {j} \right\rangle .$$

显然式 (8.5.7) 等价于
