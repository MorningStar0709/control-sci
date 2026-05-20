对一个微分流形 $M$ ，在 Lie 括号 $[\cdot, \cdot]$ 下， $V(M)$ 成为一个 Lie 代数。因此，将 $V(M)$ 看作一个 Lie 代数是方便的。

下面考虑 Lie 群的 Lie 代数.

给定一个 Lie 群 G, 令 $a \in G$ . 由前面讨论已知左乘 (或左平移): $L_{a}: G \to G$ 是一个微分同胚. 令 $X \in V(G)$ , X 称为一个左不变向量场, 如果

$$(L _ {a}) _ {*} X = X, \quad \forall a \in G.$$

类似地，我们可以定义右不变向量场。

我们将 $G$ 上的左不变向量场集合记作 $g(G)$ . 或简记为 $g$ , 即

$$g = \{X \in V (G) \mid (L _ {a}) _ {*} X = X, \forall a \in G \}.$$

$g$ 是 $V(M)$ 的一个Lie子代数．为证明这一结论，设 $X, Y \in g$ 及 $\alpha, \beta \in \mathbb{R}, a \in G.$ 那么

(1) $(L_{a})_{*}(\alpha X + \beta Y) = \alpha (L_{a})_{*}X + \beta (L_{a})_{*}Y = \alpha X + \beta Y;$   
(2) $(L_{a})_{*}[X,Y] = [(L_{a})_{*}X,(L_{a})_{*}Y] - [X,Y].$

定义3.9.3 给定一个Lie群 $G$ . 左不变向量场集合 $g = g(G)$ 称为Lie群 $G$ 的Lie代数.

命题3.9.1 设 $X \in g$ . 定义一个映射 $\Psi: g \to T_e(G)$ 为 $X \mapsto X_e$ . 那么 $\Psi$ 是一个线性同构.

证明 线性性是平凡的. 我们只要证明它是双向一对一的. 设 $X \neq Y$ , 那么在至少有一个点 $x \in G$ 满足 $X(x) \neq Y(x)$ . 于是

$$(L _ {x ^ {- 1}}) _ {*} X _ {x} \neq (L _ {x ^ {- 1}}) _ {*} Y _ {x},$$

从而 $X_{e} \neq Y_{e}$ . 因此 $\Psi$ 是一对一的.

要证明这个映射是映上的，设 $X_{e} \in T_{e}(G)$ ，我们定义一个向量场 $X(x) = (L_x)_* X_e$ 。因为 $L_x$ 是解析映射，故 $X(x)$ 显然是一个向量场。要证明 $X_{e} \in g$ ，我们只要证明它是左不变的即可：对任一 $b \in G$ ，

$$(L _ {b}) _ {*} X _ {x} = (L _ {b}) _ {*} ((L _ {a}) _ {*} X _ {e}) = (L _ {b x}) _ {*} X _ {e} = X _ {b x},$$

结论获证.

上述定理还说明 $\dim (g(G)) = \dim (G)$ .

由连续性不难看出 Lie 群上的左不变向量场是完备的。因此我们可以定义下面的指数映射：

定义3.9.4 设 $X \in g(G)$ . 定义指数映射 $\exp: g \to G$ 为

$$\exp (X) = \phi_ {1} ^ {X} (e). \tag {3.9.1}$$

于是显然有

$$\exp (t X) = \phi_ {t} ^ {X} (e).$$

而且如果 $G = \mathrm{GL}(n,\mathbb{R})$ 或其子群，则指数映射变为普通矩阵的指数映射.

例3.9.3 如果我们将左不变向量场 $X(x)$ 与它在单位元的值 $X(e)$ 等同，则我们得到：

(1) $\operatorname{GL}(n, \mathbb{R})$ 的 Lie 代数为 $\operatorname{gl}(n, \mathbb{R})$ ;  
(2) $\operatorname{SL}(n, \mathbb{R})$ 的 Lie 代数是 $\operatorname{sl}(n, \mathbb{R})$ , 这里 $\operatorname{sl}(n, \mathbb{R}) = \{X \in \operatorname{gl}(n, \mathbb{R}) \mid \operatorname{tr}(X) = 0\}$ ;  
(3) $O(n)$ 的Lie代数是 $o(n)$ , 这里 $o(n) = \{X \in \mathbf{gl}(n, \mathbb{R}) \mid X^{\mathrm{T}} = -X\}$ ;  
(4) $U(n)$ 的 Lie 代数是 $u(n)$ . 这里 $u(n) = \{X \in \operatorname{gl}(n, \mathbb{C}) \mid \overline{X}^{\mathrm{T}} = -X\}$ ;  
(5) $\operatorname{Sp}(2n, \mathbb{R})$ 的 Lie 代数是 $\operatorname{sp}(2n, \mathbb{R})$ , 这里 $\operatorname{sp}(2n, \mathbb{R}) = \{X \in \operatorname{gl}(2n, \mathbb{R}) \mid X^{\mathrm{T}}J + JX = 0\}$ ;

(6) 记

$$\mathrm{SO} (n) = \{A \in O (n) \mid \det (A) = 1 \},$$

它称为特殊正交群. 考虑 $\mathrm{SO}(n)$ 的 Lie 代数. 注意 Lie 群的 Lie 代数只依赖于 Lie 代数在单位元附近的值, 因此当 Lie 群作为一个拓扑空间具有几个连通块时, 它的 Lie 代数只由包含单位元的那个子块来决定. 因此 $O(n)$ 与 $\mathrm{SO}(n)$ 具有相同的 Lie 代数 $o(n)$ .

事实上，所有有穷维 Lie 代数本质上都是 $\operatorname{gl}(n, \mathbb{R})$ 的子代数.

定理 3.9.3(Ado 定理) 任意有穷维 Lie 代数都同构于 gl(n, R) 的一个子代数.
证明见文献 [12].

下面的定理给出 Lie 群及其 Lie 代数之间的基本关系.

定理3.9.4 每一个有穷维Lie代数 $g$ 对应于一个唯一的单连通的Lie群 $\tilde{G}$ , 并且任何其他以 $g$ 为Lie代数的连通Lie群 $G$ , 均同构于 $\tilde{G}$ 对其某个离散正规子群 $D$ 的商群, 即

$$G \simeq \tilde {G} / D.$$

证明及细节见文献 [16].

事实上，所有以 $g$ 为其 Lie 代数的连通 Lie 群 $G$ 具有一个共同的复叠空间 $\tilde{G}$ ，因而它们均局部同构。
