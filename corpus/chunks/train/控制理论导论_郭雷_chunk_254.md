# 3.9 Lie 群

Lie 群是代数与几何结合的产物。它的代数结构是群，几何结构是微分流形。两种结构相容，使 Lie 群有特殊的美。它对数学及物理学的许多学科，特别是对动力系统（包括控制系统）的研究起着重大作用。

定义3.9.1 一个集合 $G$ 称为Lie群，如果

LG1. $G$ 是一个群；

LG2. $G$ 是一个解析的微分流形；

LG3. 乘法映射 $\otimes: G \times G \to G$ 是解析的；逆映射 $G \to G: g \mapsto g^{-1}$ ，也是解析的。

设 $M_{n}$ 为 $n \times n$ 矩阵集合. 记

$$V (\boldsymbol {A}) = \left[ \boldsymbol {A} _ {1}, \dots , \boldsymbol {A} _ {n} \right] ^ {\mathbf {T}}, \quad \boldsymbol {A} \in M _ {n},$$

这里 $A_{i}$ 是 $\pmb{A}$ 的第 $i$ 行. 那么 $V$ 是双向一一映射. 通过 $V$ 到 $V^{-1}$ 我们可将 $M_{n}$ 等同于 $\mathbb{R}^{n\times n}$ . 以后我们将赋 $M_{n}$ 予 $\mathbb{R}^{n\times n}$ 上的普通拓扑.

例3.9.1 考虑 $\operatorname{GL}(n, \mathbb{R}) \subset M_n$ . 它是 $M_n$ 上的一个开集, 因此它是一个 $n \times n$ 解析流形. 我们已经知道在矩阵乘法下它是一个群. 将矩阵的元作为它的坐标, 显然乘法 $A \times B \to AB$ 及逆 $A \to A^{-1}$ 是解析的. 因此 $\operatorname{GL}(n, \mathbb{R})$ 是一个 Lie 群. 实际上, 它是一个非常重要的 Lie 群, 称为一般线性群.

定义3.9.2 给定一个Lie群 $G$ . 一个子集 $S \subset G$ 称为Lie子群，如果

LSG1. $S$ 为 $G$ 的一个子群；

LSG2. S 为 G 的正规子流形;

LSG3. 在子群结构与子流形结构下， $S$ 是一个Lie群.

注3.9.1 在有些参考书中Lie子群 $H \subset G$ 是一个嵌入子流形。因此， $H$ 可能不是 $G$ 的闭子流形。除非特殊说明，我们只考虑闭子Lie群以避免不必要的复杂。

定理3.9.1 设 $H \subset G$ 为Lie群 $G$ 的子群。同时它又是一个正规子流形。那么

(1) $H$ 本身是一个Lie群；(2) $H$ 是 $G$ 的闭子群.

证明 (1) 设 $g_{i} \in H, i = 1,2,3, g_{1}g_{2} = g_{3}$ , 且 $(U_{i}, \phi_{i}), i = 1,2,3$ , 分别为 $g_{i}, i = 1,2,3$ . 邻域的平整坐标. 令 $\dim(G) = m$ 及 $\dim(H) = n$ , 那么在平整坐标下记 $g_{1} = (x_{1}, \cdots, x_{n}, 0, \cdots, 0), g_{2} = (y_{1}, \cdots, y_{n}, 0, \cdots, 0), g_{3} = (z_{1}, \cdots, z_{n}, 0, \cdots, 0)$ . 于是乘积 $U_{1} \times U_{2} \to U_{3}$ (如需要, 可缩小 $U_{1}$ 和 $U_{2}$ ) 可表示为

$$z _ {i} = z _ {i} \left(x _ {1}, \dots , x _ {m}, y _ {1}, \dots , y _ {m}\right), \quad i = 1, \dots , m.$$

将它限制到 $H$ 上，有

$$\widetilde {z} _ {i} = z _ {i} \left(x _ {1}, \dots , x _ {n}, 0, \dots , 0, y _ {1}, \dots , y _ {n}, 0, \dots , 0\right), \quad i = 1, \dots , n.$$

它显然是解析的.

类似的讨论可知 $g \mapsto g^{-1}$ 也是解析的。因此 $H$ 是一个 Lie 群。

(2) 设 $h_i \in H$ 且 $i \to \infty$ 时 $h_i \to h_0$ , $(U, x)$ 是 $h_0$ 邻域的一个平整坐标。那么存在 $N > 0$ 使当 $i > N$ 时， $h_i \in U$ 。记 $h_i = (x_1^i, \cdots, x_n^i, 0, \cdots, 0)$ 。因为 $h_i \to h_0$ , $x_j^i \to x_0^i (i \to \infty)$ , $j = 1, \cdots, m$ ，所以显见 $h_j^0 = 0$ , $j = n + 1, \cdots, m$ ，从而 $h_0 \in H$ 。因此 $H$ 是闭集。

事实上，上述(2)的逆也对，即Lie群的闭子群是一个Lie子群[16].

定理3.9.2 设 $F: G_1 \to G_2$ 为一个Lie群同态，则 $F$ 的秩为定常值，而且其核 $K = \ker(F)$ 是 $G_1$ 的一个Lie子群，其余维数 $\operatorname{codim}(K) = \operatorname{rank}(F)$ .
