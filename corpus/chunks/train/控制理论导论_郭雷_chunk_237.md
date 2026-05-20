$$
\left[ \begin{array}{c} b _ {1} \\ \vdots \\ b _ {n} \end{array} \right] = \left[ \begin{array}{c c c} \frac {\partial f _ {1}}{\partial x _ {1}} & \dots & \frac {\partial f _ {1}}{\partial x _ {m}} \\ \vdots & & \vdots \\ \frac {\partial f _ {n}}{\partial x _ {1}} & \dots & \frac {\partial f _ {n}}{\partial x _ {m}} \end{array} \right] _ {p} \left[ \begin{array}{c} a _ {1} \\ \vdots \\ a _ {m} \end{array} \right], \tag {3.6.5}
$$

或缩写成

$$F _ {*} (X _ {p}) = J _ {F} (p) X _ {p}.$$

因为 $X_{p}$ 本质上是一个方向导数，所以它具有导数的特征。例如，由定义容易推知，如果 $f, g \in C^{r}(M, p)$ 且 $a, b \in \mathbb{R}$ ，则

$$
\left\{ \begin{array}{l} X _ {p} (a f + b g) = a X _ {p} (f) + b X _ {p} (g), \\ X _ {p} (f g) = X _ {p} (f) g + f X _ {p} (g). \end{array} \right. \tag {3.6.6}
$$

事实上， $T_{p}(M)$ 是所有 $C^{r}(M,p)\to\mathbb{R}$ 满足方程(3.6.6)映射的集合，细节见文献[2].

现在可以将 $M$ 上通过不同点的切空间放到一起，即得

$$T (M) = \bigcup_ {x \in M} \{(x, T _ {x} (M)) \}.$$

在 $M$ 上的每一个坐标卡 $(U, \phi)$ 中，可以定义一个映射 $\Psi: \phi(U) \times \mathbb{R}^n \to T(M)$ 为

$$\left[ x _ {1}, \dots , x _ {n} \right] ^ {\mathrm{T}} \times \left[ a _ {1}, \dots , a _ {n} \right] ^ {\mathrm{T}} \mapsto \left(q, \sum_ {i = 1} ^ {n} a _ {i} \frac {\partial}{\partial x _ {i}}\right),$$

这里 $[x_{1},\cdots,x_{n}]=\phi(q)$ .

现在 $\Psi$ 是 $\mathbb{R}^n\times \mathbb{R}^n$ 的一个开集到 $T(M)$ 的微分同胚，因此可将 $(\Psi (\phi (U)\times$ $\mathbb{R}^n),\Psi^{-1})$ 看作 $T(M)$ 的一个坐标卡．容易验证如下的事实：

(1) 所有这样的坐标卡形成 $T(M)$ 的一个开覆盖；  
(2) 如果 $M$ 是一个 $C^r$ 流形，那么这些坐标卡也是 $C^r$ 相容的.

因此如果 $M$ 是一个 $n$ 维 $C^r$ 流形，那么根据以上的结构， $T(M)$ 是一个 $2n$ 维 $C^r$ 流形.

设 $p: T(M) \to M$ 为一自然投影： $(p, T_p) \mapsto p$ 。那么 $(T(M), p, M)$ 成为一个向量丛。它称为 $M$ 的切丛。

在多数情况下我们只简单地使用 $T(M)$ 的另一种表达，它不直接包含第一个分量，而是隐含它

$$T (M) = \bigcup_ {x \in M} \{T _ {x} (M) \}.$$

除非要强调丛结构，我们总采用这个简单形式.

定义 3.6.3 M 上的一个向量场 X 是一个映射 $X: M \to T(M)$ . 它对每一点 $q \in M$ 指定 $T_{q}(M)$ 上的一个向量. 在局部坐标下 X 可表示为

$$X = \sum_ {i = 1} ^ {n} a _ {i} (x) \frac {\partial}{\partial x _ {i}}.$$

X 称为 $C^{T}$ 向量场，如果所有的 $a_{i}(x), i=1,\cdots,n$ 均为 $C^{T}$ 函数.

$M$ 上光滑向量场的集合记作 $V^{r}(M)$ , 这里 $\pmb{r}$ 可以是任何非负整数, 或 $\infty$ , 或 $\omega$ , 后者表示解析. 当光滑度不重要时, 它可以简单记作 $V(M)$ .

回顾前面的讨论，当 $M$ 和 $N$ 为两个光滑流形， $F: M \to N$ 为一光滑映射时， $F$ 可以将 $M$ 上的切向量映为 $N$ 上的切向量。准确地说，设 $q \in M$ 及 $F(q) \in N$ ， $X_q \in T_q(M)$ ，那么 $F_*(X_q) \in T_{F(q)}(N)$ 。由式 (3.6.4) 所定义，在局部坐标下它可用式 (3.6.5) 计算。

现在很自然要问： $F$ 能将 $M$ 上的一个向量场映为 $N$ 上的一个向量场吗？一般地说不能。请看以下的例子：

例3.6.1 考虑一个 $\mathbb{R}$ 上的向量场 $X = (t^2 + 1)\frac{\mathrm{d}}{\mathrm{d}t}$ . 设 $F: \mathbb{R} \to \mathbb{R}^2$ 定义为
