# 3.7 Lie导数

对一个给定流形 $M$ 及 $x \in M$ , 在 $x \in M$ 点的切空间 $T_x(M)$ 是一个有穷维向量空间. 由线性代数知道, 它有一个对偶空间, 记作 $T_x^*(M)$ . 然后定义 $M$ 的余切空间.

定义3.7.1 (1)流形 $M$ 的余切空间定义为

$$T ^ {*} (M) = \bigcup_ {x \in M} T _ {x} ^ {*} (M);$$

(2) 一个余向量场 $\phi$ 是一个规则, 它在每一点 $x \in M$ 指定一个余切向量 $\phi(x) \in T_x^*(M)$ ;

(3) 一个余分布 $\omega$ 是一个规则，它在每一点 $x \in M$ 指定一个子空间 $\omega(x) \subset T_x^*(M)$ . 称 $\omega$ 具有定常维数 $r$ , 如果 $\dim(\omega(x)) = r, \forall x \in M$ .

例3.7.1 (1) 在 $\mathbb{R}^3$ 上考虑两个光滑函数

$$h (x) = \cos (x _ {1}) + \sin (x _ {2}), \quad w (x) = - \sin (x _ {2}) + \cos (x _ {3}).$$

那么 $h(x)$ 的微分是

$$\mathrm{d} h (x) = \sum_ {i = 1} ^ {3} \frac {\partial h (x)}{\partial x _ {i}} \mathrm{d} x _ {i} = - \sin (x _ {1}) \mathrm{d} x _ {1} + \cos (x _ {2}) \mathrm{d} x _ {2}.$$

我们很自然地可将 $\{\mathrm{d}x_{i} \mid i = 1,2,3\}$ 看作一个基底。那么 $\mathrm{d}h(x)$ 可以简单地表示成一个行向量 $\mathrm{d}h(x) = (-\sin (x_1),\cos (x_2),0)$ 。点点看， $\mathrm{d}h(x)$ 是 $T_{x}^{*}(\mathbb{R}^{3})$ 中的余向量。因此我们说 $\mathrm{d}h \in T^{*}(\mathbb{R}^{3})$ 。同样我们有 $\mathrm{d}w \in T^{*}(\mathbb{R}^{3})$ 。

(2) 利用它们可定义一个余分布 $\Omega$ 如下:

$$\Omega = \operatorname{span} \{\mathrm{d} h, \mathrm{d} w \}.$$

准确地说，

$$\Omega (x) = \operatorname{span} \{\mathrm{d} h (x), \mathrm{d} w (x) \}, \quad \forall x \in \mathbb {R} ^ {3}.$$

由上述例子的启发，我们一般地选 $\{dx_{i} \mid i = 1, \cdots, n\}$ 为 $T^{*}(M)$ 在一个坐标卡下的基底。现在如果有一个向量场 $X(x) = \sum_{i=1}^{n} a_{i}(x) \frac{\partial}{\partial x_{i}}$ 和一个余向量 $dh(x) = \sum_{i=1}^{n} \frac{\partial h(x)}{\partial x_{i}} dx_{i}$ ，那么它们的“配对积”则为

$$\langle \mathrm{d} h (x), X (x) \rangle = \sum_ {i = 1} ^ {n} a _ {i} (x) \frac {\partial h (x)}{\partial x _ {i}}.$$

它就是 $X$ 对 $h(x)$ 的作用. 如果 $X$ 是单位向量, 则上式表示 $h$ 在 $X$ 方向的方向导数.

一个余向量场也称1-形式．利用 $\{dx_{i} \mid i = 1, \cdots, n\}$ 作为 $T^{*}(M)$ 在一个坐标卡下的基底，则一个余向量场可表示为 $\phi(x) = \sum_{i=1}^{n} \phi_{i}(x) dx_{i}$ .

定义3.7.2 一个1-形式 $\phi(x) = \sum_{i=1}^{n} \phi_i(x) \mathrm{d}x_i$ 称为闭1-形式，如果它满足

$$\frac {\partial \phi_ {i} (x)}{\partial x _ {j}} = \frac {\partial \phi_ {j} (x)}{\partial x _ {i}}, \quad i \neq j. \tag {3.7.1}$$

$\phi(x)$ 称为恰当 1- 形式，如果存在一个光滑函数 $h(x)$ 使得 $\phi(x) = \mathrm{d}h(x)$ .

定理 3.7.1(Poincaré 引理) $^{[1]}$ 一个闭 1-形式局部地说也是一个恰当形式。如果 M 是一个单连通的拓扑空间，则一个闭 1-形式全局地说也是一个恰当形式。

定义 3.7.3 设 $F: M \rightarrow N$ 为一微分同胚.

(1) 设 $f(x) \in C^{r}(N)$ , 则 $F$ 的一个导出映射 $F^{*}: C^{r}(N) \to C^{r}(M)$ 定义为

$$F ^ {*} (f) = f \circ F \in C ^ {r} (M);$$

(2) 设 $X \in V^{r}(M)$ , 则 $F$ 的一个导出映射 $F_{*}: V^{r}(M) \to V^{r}(N)$ 定义为
