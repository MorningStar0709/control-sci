显然 $X(f) \in C^{r-1}(M)$ . 因此一个向量场 $X$ 可以看作一个映射 $X: C^r(M) \to C^{r-1}(M)$ . 特别是, 如果 $r = \infty$ 或 $r = \omega$ , 它变为 $C^\infty$ (或 $C^\omega$ ) 到自身的一个映射.

下面我们给 $V(M)$ 一个Lie代数结构. (Lie代数的概念见定义3.2.8)

现在考虑向量场集合 $V(M)$ . 定义 Lie 括号如下:

$$[ X, Y ] - X Y - Y X, \tag {3.6.9}$$

即对每一点 $p \in M$ 及 $h \in C_p^r(M)$ ,

$$[ X, Y ] _ {p} (h) = \left. X (Y (h)) \right| _ {p} - \left. Y (X (h)) \right| _ {p}.$$

首先要证明这是定义好的. 即 $[X, Y]_p \subset T_p(M)$ . 换言之, 我们必须证明 $[X, Y]$ 满足方程 (3.6.6). 这是容易验证的, 我们留给读者.

命题3.6.3 设 $X, Y \in V(M)$ , 且在局部坐标下,

$$X = \left[ a _ {1} (x), \dots , a _ {n} (x) \right] ^ {\mathrm{T}}, \dots , Y = \left[ b _ {1} (x), \dots , b _ {n} (x) \right] ^ {\mathrm{T}}.$$

那么

$$[ X, Y ] = \frac {\partial Y}{\partial x} X - \frac {\partial X}{\partial x} Y, \tag {3.6.10}$$

这里 $\frac{\partial Y}{\partial x}$ 和 $\frac{\partial X}{\partial x}$ 分别为 $X$ 和 $Y$ 的Jacobi矩阵，例如，

$$
\frac {\partial Y}{\partial x} = \left[ \begin{array}{c c c} \frac {\partial b _ {1}}{\partial x _ {1}} & \dots & \frac {\partial b _ {1}}{\partial x _ {n}} \\ \vdots & & \vdots \\ \frac {\partial b _ {n}}{\partial x _ {1}} & \dots & \frac {\partial b _ {n}}{\partial x _ {n}}. \end{array} \right]
$$

证明 记

$$[ X, Y ] = \sum_ {i = 1} ^ {n} c _ {i} (x) \frac {\partial}{\partial x _ {i}}. \tag {3.6.11}$$

选择 $h = x_{j}$ ，那么式(3.6.11)变为 $[X,Y](h) = c_j(x)$ .另一方面，根据定义，

$$
\begin{array}{l} [ X, Y ] (h) = X (Y (h)) - Y (X (h)) \\ = \sum_ {i = 1} ^ {n} a _ {i} (x) \frac {\partial}{\partial x _ {i}} \left(b _ {j} (x)\right) - \sum_ {i = 1} ^ {n} b _ {i} (x) \frac {\partial}{\partial x _ {i}} \left(a _ {j} (x)\right). \\ \end{array}
$$

因此

$$c _ {j} (x) = \sum_ {i = 1} ^ {n} a _ {i} (x) \frac {\partial b _ {j} (x)}{\partial x _ {i}} - \sum_ {i = 1} ^ {n} b _ {i} (x) \frac {\partial a _ {j} (x)}{\partial x _ {i}}, \qquad j = 1 \dots , n. \tag {3.6.12}$$

显见式 (3.6.10) 是式 (3.6.12) 的矩阵形式.

为理解两个向量场的 Lie 括号的几何意义，我们考虑如下的图形：设 $X, Y \in V(M)$ . 考虑复合的积分曲线

$$\phi_ {- t} ^ {Y} \dot {\phi} _ {- t} ^ {X} \phi_ {t} ^ {Y} \phi_ {t} ^ {X} (x _ {0}).$$

它的物理意义是：一个粒子从 $x_0$ 出发，沿 $X$ 方向走， $t$ 时间后，它从 $X$ 方向转到 $Y$ 方向，沿 $Y$ 方向再走时间 $t$ ，然后沿 $X$ 相反方向走同样时间。最后，沿 $Y$ 相反方向走同样时间。如果 $X$ 和 $Y$ 为定常向量，这个粒子显然会回到原来的出发点 $x_0$ 。但如果它们不是定常的，那么终点 $x_e$ 就可能不是初始点 $x_0$ 。粒子最后的位移方向是什么？粗略地说，从 $x_0$ 到 $x_e$ 的方向就是 Lie 括号 $[X, Y]_{|x_0}$ 的方向。准确地说，

$$\lim _ {t \rightarrow 0} \frac {1}{t ^ {2}} \left(\phi_ {t} ^ {Y} \phi_ {- t} ^ {X} \phi_ {t} ^ {Y} \phi_ {t} ^ {X} \left(x _ {0}\right) - x _ {0}\right) = [ X, Y ] _ {x _ {0}}. \tag {3.6.13}$$

利用Taylor展开式
