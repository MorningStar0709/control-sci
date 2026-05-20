(3) 一个拓扑空间 $(X, T)$ 称为 $T_{2}$ 空间，如果对任何两个点 $x, y \in X$ 存在两个开集 $U_{x} \in T$ 及 $U_{y} \in T$ ，使得 $x \in U_{x}, y \in U_{y}$ 并且 $U_{x} \cap U_{y} = \varnothing$ . $T_{2}$ 空间也称 Hausdorff 空间.

由定义可知 $T_{2} \Rightarrow T_{1} \Rightarrow T_{0}$ .

例3.3.13 考虑 $\mathbb{R}^1$ . (1) 定义一个子集族 $T$ 为射线族

$$\mathcal {T} = \{(- \infty , r) \mid r \in \mathbb {R} \}.$$

那么 $(\mathbb{R}^1, T)$ 是一个拓扑空间。并且，容易检验这是一个 $T_0$ 空间；

(2) 定义一个子集族 $\pmb{T}$ 如下:

$$\mathcal {T} = \{U \subset \mathbb {R} \mid U ^ {c} \text {为有限集} \},$$

那么 $(\mathbb{R}^1, T)$ 是一个拓扑空间。容易检验这是一个 $T_1$ 空间；

(3) 依普通拓扑，容易证明 $\mathbb{R}^1$ 是一个 $T_2$ 空间.

定义3.3.10 设 $(X, T)$ 为一拓扑空间， $S \subset X$ 。 $S$ 称为 $X$ 的一个拓扑子空间，如果 $S$ 上的拓扑定义如下：

$$\mathcal {T} _ {S} = \{U \cap S \mid U \in \mathcal {T} \}.$$

需要证明 $T_{S}$ 的确是一个拓扑空间. 我们将它留给读者.

定义3.3.11 设 $(X_{i}, T_{i})$ , $i = 1,2$ 为两个拓扑空间. 考虑Cartesian乘积 $X_{1} \times X_{2} = \{(x, y) \mid x \in X_{1}, y \in X_{2}\}$ . 设

$$\left\{U _ {1} \times U _ {2} \mid U _ {1} \in \mathcal {T} _ {1}, U _ {2} \in \mathcal {T} _ {2} \right\}$$

为一个拓扑基，记由这个拓扑基生成的拓扑为 $\mathcal{T}_1\times \mathcal{T}_2$ 那么 $(X_{1}\times X_{2},\mathcal{T}_{1}\times \mathcal{T}_{2})$ 为一个拓扑空间，它称为 $X_{1}$ 和 $X_{2}$ 的乘积拓扑空间.

下面的定理十分有用.

定理3.3.2 拓扑空间 $(X, T)$ 是Hausdorff空间，当且仅当在乘积空间 $(X \times X, T \times T)$ 中对角线

$$D = \{(x, x) \mid x \in X \}$$

是乘积空间中的闭集.

证明 必要性. 设 $X$ 为 Hausdorff 空间. 令 $(x, y) \in X \times X$ 且 $(x, y) \notin D$ , 即 $x \neq y$ , 则存在两开集 $U_x \ni x$ 和 $U_y \ni y$ , 使得 $U_x \cap U_y = \varnothing$ . 现在 $U_x \times U_y \subset X \times X$ , $U_x \times U_y$ 是开集且 $U_x \times U_y \cap D = \varnothing$ . 因此, $D^c$ 为开集, 即 $D$ 是闭集.

充分性. 设 $D$ 为闭集. 给定任意两点 $x, y \in X$ 且 $x \neq y$ , 我们知道 $(x, y) \in D^c$ , 后者为开集. 因此, 存在开集 $U \subset X \times X$ 使得 $(x, y) \in U \subset D^c$ . 但是 $\{U \times V \mid U, V \in T\}$ 是 $\mathcal{T} \times \mathcal{T}$ 的拓扑基，因此存在 $U_x, V_y \in \mathcal{T}$ 使得

$$(x, y) \in U _ {x} \times V _ {y} \subset U \subset D ^ {c},$$

即有 $x \in U_x$ 及 $y \in V_y$ 并且 $U_x \cap V_y = \emptyset$ . 这就证明了 $X$ 是 Hausdorff 空间.

下面考虑拓扑空间之间的连续映射.

定义3.3.12 设 $M, N$ 为两个拓扑空间。一个映射 $\pi: M \to N$ 称为连续的，如果下面两个等价条件之一成立：

(1) 对任一开集 $U \subset N$ , 它的逆象 $\pi^{-1}(U) \stackrel{\mathrm{def}}{=} \{x \in M \mid \pi(x) \in U\}$ 是开的;  
(2) 对任一闭集 $C \subset N$ , 它的逆象 $\pi^{-1}(C)$ 是闭的.

检验这两个条件的等价性，我们留给读者.

定义3.3.13 设 $M, N$ 为两个拓扑空间。 $M$ 和 $N$ 称为是同胚的，如果存在一个映射 $\pi: M \to N$ ，它是一对一，映上和连续的。并且它的逆 $\pi^{-1}$ 也是连续的。 $\pi$ 称为一个同胚映射。

如果一个映射是一对一且映上的，则称为双向一一映射.

例3.3.14 设 $S^2$ 为一球面
