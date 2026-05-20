这里有几点需要说明。对给定的坐标卡 $(U,\phi)$ ，将 $p\in U$ 与 $\phi(p)=(x_{1}^{p},\cdots,x_{n}^{p})\in\mathbb{R}^{n}$ 等同。例如，当我们说 $\theta(t)=(\theta_{1}(t),\cdots,\vartheta_{n}(t))$ ，实际上它应该是 $\phi\circ(\theta(t))$ ，因为只有在 $\phi(U)\subset\mathbb{R}^{n}$ 坐标才有意义。当不会发生混淆时这个等同很方便，以后我们经常这样做，它称为局部坐标表示。同样， $h=h(x_{1},\cdots,x_{n})$ 是 $h\circ\phi^{-1}$ 的局部坐标表示。

因为切空间是在局部坐标系下定义的，要使它有意义我们必须证明它独立于局部坐标架的选择，即同一个 $\theta$ 在不同坐标架下起相同的作用。证明不难，我们留给读者。

在一个给定的坐标卡下，一个切向量 $X_{p} \in T_{p}(M)$ 可以表示为

$$\boldsymbol {X} _ {p} = \sum_ {i = 1} ^ {n} v _ {i} \frac {\partial}{\partial x _ {i}}.$$

如同在线性代数中一样，基底可以省略，因此 $X_{p}$ 可以简单地写成一个向量

$$\boldsymbol {X} _ {p} = \left[ v _ {1}, \dots , v _ {n} \right] ^ {\mathrm{T}}.$$

即对任一 $h \in C^{r}(M, p)$ , $X$ 对它的作用为

$$\boldsymbol {X} _ {p} (h) = \sum_ {i = 1} ^ {n} v _ {i} \frac {\partial}{\partial x _ {i}} h.$$

定义 3.6.2 设 M, N 为两个光滑流形，且 $F: M \rightarrow N$ 为一光滑映射。对一点 $p \in M$ 及 $F(p) \in N$ ，我们定义一个映射 $F_{*}: T_{p}(M) \rightarrow T_{F(p)}(N)$ 如下：

$$F _ {*} (X _ {p}) h = X _ {p} (h \circ F), \quad X _ {p} \in T _ {p} (M), h \in C ^ {r} (N, F (p)). \tag {3.6.4}$$

下面给出 $F_{*}(X_{p})$ 的一个局部坐标表示，它在应用上非常重要.

设 $x$ 和 $y$ 分别为 $p \in M$ 和 $F(p) \in N$ 附近的局部坐标， $X_p, F_*(X_p)$ 分别表示为

$$X _ {p} = a _ {1} \frac {\partial}{\partial x _ {1}} + \dots + a _ {n} \frac {\partial}{\partial x _ {n}},F _ {*} (X _ {p}) = b _ {1} \frac {\partial}{\partial y _ {1}} + \dots + b _ {n} \frac {\partial}{\partial y _ {n}},$$

并且 $F: M \to N$ , 即 $x \mapsto y$ , 表示为

$$y _ {i} = f _ {i} \left(x _ {1}, \dots , x _ {m}\right), \quad i = 1, \dots , n.$$

那么式 (3.6.4) 可表示成

$$F _ {*} (X _ {p}) h = X _ {p} (h \circ F) = \sum_ {i = 1} ^ {m} a _ {i} \frac {\partial}{\partial x _ {i}} (h \circ F) = \sum_ {i = 1} ^ {m} a _ {i} \left(\sum_ {j = 1} ^ {n} \frac {\partial}{\partial y _ {j}} h \frac {\partial f _ {j}}{\partial x _ {i}}\right)= \sum_ {j = 1} ^ {n} \left(\sum_ {i = 1} ^ {m} \frac {\partial f _ {j}}{\partial x _ {i}} a _ {i}\right) \left. \frac {\partial}{\partial y _ {j}} h \right| _ {F (p)} \stackrel {{\text { def }}} {{=}} \sum_ {j = 1} ^ {n} b _ {j} \left. \frac {\partial}{\partial y _ {j}} h (y) \right| _ {F (p)},$$

即

$$b _ {j} = \sum_ {i = 1} ^ {m} \frac {\partial f _ {j}}{\partial x _ {i}} a _ {i}, \quad j = 1, \dots , n.$$

将它写成矩阵形式，即
