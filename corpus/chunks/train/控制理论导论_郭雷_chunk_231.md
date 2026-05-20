设 $X, Y \in F(k, n)$ . $X$ 与 $Y$ 生成同一个子空间，当且仅当存在一个 $A \in \mathrm{GL}(k, \mathbb{R})$ 使得 $X = YA$ . 在 $F(k, n)$ 上定义一个等价关系如下：

$$X \sim Y \Longleftrightarrow X \in Y \mathrm{GL} (k, \mathbb {R}).$$

于是我们可以定义商空间

$$G (k, n) = F (k, n) / \sim .$$

于是 $G(k, n)$ 是一个定义好的拓扑空间. 我们在 $G(k, n)$ 上建立一个微分结构如下: 对于 $X \in F(k, n)$ , 它有一个 $k \times k$ 非奇异子矩阵, 例如它由前 $k$ 行构成, 那么

$$
\boldsymbol {X} \sim \left[ \begin{array}{c c c} & I _ {k} & \\ \left[ \begin{array}{c c c} x _ {k + 1} ^ {1} & \dots & x _ {k + 1} ^ {k} \\ \vdots & & \vdots \\ x _ {n} ^ {1} & \dots & x _ {n} ^ {k} \end{array} \right] \end{array} \right]. \tag {3.5.1}
$$

现在在 $G(k, n)$ 上定义一个坐标卡为等价类 $[X]$ 这里 $X$ 的前 $k$ 行线性无关. 对每个等价类中取一个形为 (3.5.1) 的代表元. 注意在这个卡中每一个等价类 $[X]$ 有唯一表示, 因此我们可以选择

$$\phi ([ X ]) = x _ {k + 1} ^ {1}, x _ {k + 2} ^ {1}, \dots , x _ {n - 1} ^ {k}, x _ {n} ^ {k}$$

作为它的局部坐标。这样总共有

$$N = \binom {n} {k} = \frac {n !}{k ! (n - k) !}$$

个坐标卡 $U^i$ ，它对应于等价类 $[X]$ 集合，每个集合有特定的 $k$ 个线性无关行。最后，我们还要证明这个结构是解析的：设 $[X] \in U_i \cap U_j$ ，那么在 $U_i$ 中 $X$ 的某 $k$ 个特定行形成 $\phi_i$ ，即 $\tilde{\phi}_i = X A_i^{-1}$ 且 $\tilde{\phi}_i$ 的 $k$ 个特别指定行形成 $\phi_i$ 的坐标，而在 $U_j$ 中 $X$ 的特别指定行形成 $\phi_j$ ，即 $\tilde{\phi}_j = X A_j^{-1}$ 且 $\tilde{\phi}_j$ 的某 $k$ 个特定指定行形成 $\phi_j$ 。于是 $\phi_i \to \phi_j$ 的坐标变换由以下的映射确定：

$$\widetilde {\phi} _ {j} = \widetilde {\phi} _ {i} A _ {i} A _ {j} ^ {- 1},$$

而这个映射是解析的。由以上的讨论可知 Grassman 流形的维数是 $\dim(G(k, n)) = k(n - k)$ 。

定义3.5.2 设 $M, N$ 为两个 $C^r$ 流形，其维数分别为 $m, n, F: M \to N$ 称为一个 $C^r$ 映射，如果对每一点 $x \in M$ 和 $y = F(x) \in N$ 存在 $x$ 的局部坐标卡 $(U, \phi)$ 和 $y$ 的局部坐标卡 $(V, \psi)$ ，使得

$$\tilde {F} = \psi \circ F \circ \phi^ {- 1}$$

是 $C^r$ 的. 此外, $\pmb{F}$ 在 $\pmb{x}$ 点的秩定义为 $\tilde{\pmb{F}}$ 在 $\phi(x)$ 的秩.

注意，如果 $F:\mathbb{R}^m\to \mathbb{R}^n$ 可以表示为

$$y _ {i} = y _ {i} \left(x _ {1}, \dots , x _ {m}\right), \quad i = 1, \dots , n,$$

那么 $F$ 在 $\pmb{x}$ 点的秩定义为

$$
\operatorname{rank} (F) | _ {x} = \operatorname{rank} \left[ \begin{array}{c c c} \frac {\partial y _ {1}}{\partial x _ {1}} & \dots & \frac {\partial y _ {1}}{\partial x _ {m}} \\ \vdots & & \vdots \\ \frac {\partial y _ {n}}{\partial x _ {1}} & \dots & \frac {\partial y _ {n}}{\partial x _ {m}} \end{array} \right] _ {x}. \tag {3.5.2}
$$

今后，在多数情况下，如果不发生混淆我们就将 $\tilde{F}$ 等同于 $F$ .

定义3.5.3 设 $N = \mathbb{R}$ . 那么一个从 $M$ 到 $N = \mathbb{R}$ 的 $C^r (C^\infty, C^\omega)$ 映射称为一个 $C^r$ 函数 (相应地 $C^\infty$ 函数, 或解析函数), 记作 $C^r(M)$ (相应地 $C^\infty(M)$ , 或 $C^\omega(M)$ ) 为 $M$ 上的 $C^r (C^\infty$ , 解析) 函数集合.
