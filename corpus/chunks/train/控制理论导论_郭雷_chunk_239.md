$$\| X (x) - X (y) \| \leqslant \gamma \| x - y \|,$$

则它是完备的。在流形中，如果在每一个坐标卡中 Lipschitz 条件均成立，则 $X$ 是完备的。

引理3.6.1 设 $\phi_t^X (x_0)$ 为 $X$ 的积分曲线。如果存在 $x_0$ 的一个邻域 $U$ 使得 $\phi_t^X (x)$ 在 $U\times I$ 上有定义，那么对任何 $t_0\in I$ 存在一个邻域 $U_0\ni x_0$ 使得 $\phi_{t_0}^X: U_0\to \phi_{t_0}^X (U_0)$ 是一个微分同胚。

证明 我们从 $t = 0$ 出发. 因为 $\phi_0^X$ 是一个恒等映射, 故存在一个开邻域 $I_0 \ni 0$ 使得 $\phi_t^X$ 在 $x_0$ 的 Jacobi 矩阵非奇异, 即存在一个邻域 $U_{x_0} \ni x_0$ 及 $I_0 \ni 0$ 使得对每个 $t \in I_0$ , $\phi_t^X: U_{x_0} \to \phi_t^X(U_{x_0})$ 是一个微分同胚.

同样地，对每个 $t \in I$ 存在 $U_{x_t} \ni \phi_t^X(x_0)$ 和一个开邻域 $I_t \ni t$ 使得 $\phi_t^X: U_{x_t} \to \phi_t^X(U_{x_t})$ 是一个微分同胚。现在对任何 $T \in I, \{I_t | 0 \leqslant t \leqslant T\}$ 形成一个 $[0, T]$ 的开覆盖。因此有一个有限子覆盖 $\{I_{t_i} | i = 1, \cdots, k\}$ 。现在选

$$U _ {0} = \bigcap_ {i = 1} ^ {k} \phi_ {- t _ {1}} ^ {X} \dots \phi_ {- t _ {i - 1}} ^ {X} (U _ {x _ {t _ {i}}}).$$

于是不难看出 $\phi_T^X: U_0 \to \phi_T^X(U_0)$ 是一个微分同胚。因为 $T \in I$ 是任选的，结论获证。

上面的引理给出这样一个图像：对任何 $x_0 \in M$ ，存在一个邻域 $U_0$ 和一个区间 $0 \in I_0 \subset \mathbb{R}$ ，使得 $U_0$ 沿时间轴以微分同胚的形式移动。它看上去像一流动的管。因此积分曲线族称为 $X$ 的流。

命题3.6.1 设 $X$ 为一完备向量场。那么对任一固定的 $t \in \mathbb{R}$ , $\phi_t^X: M \to M$ , 定义为: $x \mapsto \phi_t^X(x)$ , 是一个微分同胚。

证明 我们已经证明过对任一向量场 $X$ ，只要对某个 $t, \phi_t^X$ 有定义，则它是一个局部微分同胚。现在 $\phi_t^X$ 对任何 $x \in M$ 及任何 $t \in \mathbb{R}$ 均有意义。所以我们只要证明映射是一对一且映上即可。映上是显然的，因为对任一 $y \in M, \phi_t^X(\phi_{-t}^X(y)) = y$ ，而一对一则是由于常微分方程解的唯一性。

命题3.6.2 设 $F: M \to N$ 为一微分同胚， $X \in V(M), \phi_t^X(x_0)$ 是 $X$ 的积分曲线且初值 $x(0) = x_0$ 。那么 $F_*(X)$ 的积分曲线为 $X$ 的积分曲线的象。准确地说，

$$\phi_ {t} ^ {F _ {*} (X)} \left(F \left(x _ {0}\right)\right) = F \circ \phi_ {t} ^ {X} \left(x _ {0}\right). \tag {3.6.8}$$

证明 我们对每一个坐标卡证明即可. 换言之, 在局部坐标形式下证明即可. 利用链式法则:

$$\frac {\mathrm{d}}{\mathrm{d} t} F \circ \phi_ {t} ^ {X} (x _ {0}) = J _ {F} \frac {\mathrm{d}}{\mathrm{d} t} [ \phi_ {t} ^ {X} (x _ {0}) ] = J _ {F} X (\circ F ^ {- 1}) = F _ {*} (X).$$

至于初值，它是 $\phi_0^{F_*(X)}(F(x_0)) = F(x_0)$

下面讨论向量场的 Lie 代数.

注意一个切向量 $X_{p}$ 是 $C^{r}(M,p)$ 上的一个算子. 如果 $X \in V(M)$ 且 $f \in C^{r}(M)$ , 则对任一 $p \in M$ , $X_{p} \in T_{p}(M)$ 且 $f \in C^{r}(M,p)$ . 因此我们可以自然地定义 $X$ 对 $f$ 的作用如下:

$$[ X (f) ] _ {p} \stackrel {\text { def }} {=} X _ {p} (f).$$

显然 $X(f)$ 是处处有定义的．而且，如果我们将上式关系表示在一个坐标系下，即

$$X = \sum_ {i = 1} ^ {n} v _ {i} (x) \frac {\partial}{\partial x _ {i}}, \quad f = f (x _ {1}, \dots , x _ {n}),$$

则其作用变为

$$X (f) = \sum_ {i = 1} ^ {n} v _ {i} (x) \frac {\partial f}{\partial x _ {i}}.$$
