$$F (t) = \left(2 \cos \left(g (t) + \frac {\pi}{2}\right), \sin \left(2 \left(g (t) + \frac {\pi}{2}\right)\right)\right).$$

现在 $F(t)$ 只画一个“8”字．这回它是一对一的．因此 $F(\mathbb{R})$ 是一个嵌入子流形. (图3.5.2(b))

但 $F(\mathbb{R})$ 不是一个浸入子流形. 如果给 $F(\mathbb{R})$ 以 $\mathbb{R}^2$ 的子空间拓扑, 那么当 $t = n \to \infty$ , $F(n) \to F(0) = 0$ . 显然 $F^{-1}$ 不连续.

(3) $S^2$ 作为 $\mathbb{R}^3$ 的子空间是一个浸入子流形。要证明这一点只要找一个平整坐标卡即可。显然普通坐标框架不行。对每一点 $p \in S^2$ ，至少有 $p$ 的一个坐标，例如坐标 $z_p \neq 0$ 。设 $p_z > 0$ ，由连续性，存在 $p$ 的一个邻域 $U$ ，使得 $z_x \neq 0, \forall x \in U$ 。定义一个映射 $\phi: U \to \mathbb{R}^3$ 如下：

$$
\left\{ \begin{array}{l} X = x, \\ Y = y, \\ Z = z - \sqrt {1 - x ^ {2} - y ^ {2}}. \end{array} \right.
$$

容易检验 $\phi$ 的 Jacobi 阵在 $p$ 点非奇异，因此它是个局部微分同胚。因此当 $U$ 足够小时， $\phi: U \to \phi(U) \subset \mathbb{R}^3$ 是一个微分同胚。于是考虑 $(U, \phi)$ 作为一个局部坐标卡，有

$$S ^ {2} \cap U = \{p \in U \mid Z (p) = 0 \}.$$

嵌入子流形与浸入子流形的根本区别在于子空间拓扑。嵌入子流形将自己的拓扑带入原空间。浸入子流形则不然，它用原空间的诱导拓扑（即子空间拓扑）作为自己的拓扑。

不难发现，嵌入子流形局部地看是一个浸入子流形。而浸入子流形则是正规子流形。

定理3.5.1 设 $N, M$ 为维数分别为 $n, m$ 的两个光滑流形。一个光滑映射 $F: N \to M$ 具有定常维数， $\operatorname{rank}(F) = k$ 。那么对每一点 $q \in F(N), F^{-1}(q)$ 是一个 $n - k$ 维闭正规子流形。

证明 因为 $F$ 的秩为 $k$ . 设 $p \in N$ 及 $q = F(p) \in M$ . 在 $p$ 点假定 Jacobi 矩阵 $J_{F}$ 的左上 $k \times k$ 子矩阵非奇异. 那么可改变 $p \in N$ 附近的局部坐标为

$$
\left\{ \begin{array}{l} X ^ {1} = F ^ {1} (x), \\ X ^ {2} = x ^ {2}, \quad \dim (X ^ {1}) = k, \dim (X ^ {2}) = n - k. \end{array} \right.
$$

这是一个局部坐标变换. 因为变换的 Jacobi 矩阵局部非奇异. 在这个新坐标架下 $F$ 变为

$$
\left\{ \begin{array}{l} F ^ {1} = X ^ {1}, \\ F ^ {2} = F ^ {2} (X ^ {1}). \end{array} \right. \tag {3.5.4}
$$

注意 $F^2$ 只依赖于 $X^1$ , 否则它就会与 $F$ 的秩的假定矛盾. 现在在 $q = F(p)$ 附近将局部坐标改为

$$
\left\{ \begin{array}{l} Y ^ {1} = y ^ {1}, \\ Y ^ {2} = y ^ {2} - F ^ {2} (X ^ {1} (y _ {1}, y _ {2})), \quad \dim (X ^ {1}) = k, \dim (X ^ {2}) = n - k, \end{array} \right. \tag {3.5.5}
$$

这里 $X^{1} = X^{1}(y_{1},y_{2})$ 由隐函数存在定理保证．现在可以看到方程(3.5.4）说明在 $F(N)$ 象上 $F^2$ 只依赖于 $X^{1} = y_{1}$ 因此

$$\frac {\partial F ^ {2}}{\partial y _ {2}} = o (\| y \|),$$

它表示方程 (3.5.5) 是一个局部坐标变换。利用两边的局部坐标，可把 $F$ 表示为

$$
F _ {i} (X _ {1}, \dots , X _ {n}) = \left\{ \begin{array}{l l} X _ {i}, & i \leqslant k, \\ 0, & i > k. \end{array} \right. \tag {3.5.6}
$$

现在在 $q$ 和 $p \in F^{-1}(q)$ 邻域的新坐标基下有

$$F ^ {- 1} (q) \cap U = \{X \in U \mid X _ {1} = \dots = X _ {k} = 0 \}.$$

因此 $F^{-1}(q)$ 是一个 $n - k$ 维正规子流形.

实际上表达式 (3.5.6) 本身也很有用。详细的构造方法读者可参考文献 [15].

例3.5.5 设 $F: \mathbb{R}^3 \to \mathbb{R}$ 定义为

$$F (x, y, z) = \frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} + \frac {z ^ {2}}{c ^ {2}}.$$

因为 $J_{F} = (2x, 2y, 2z)$ , 对每一点 $p \in F^{-1}(1)$ , 秩 $\operatorname{rank}(J_{F}) = 1$ . 因为 $x, y, z$ 在 $p$ 点不可能同时为零, 故椭球 $F^{-1}(1)$ 是一个 $\mathbb{R}^{3}$ 的正规子流形, 其维数为 $3 - 1 = 2$ .
