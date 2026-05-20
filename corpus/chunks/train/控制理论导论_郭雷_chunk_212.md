$$S ^ {2} = \{(x, y, z) \in \mathbb {R} ^ {3} \mid x ^ {2} + y ^ {2} + z ^ {2} = 1 \},$$

且 $N$ 为北极，即 $N = (0,0,1)$ 。那么 $S^2 \backslash N$ ，带上它从 $\mathbb{R}^3$ 诱导的拓扑，同胚于 $\mathbb{R}^2$ 。一个同胚映射为

$$
\left\{ \begin{array}{l} X = x / (1 - z), \\ Y = x / (1 - z), \end{array} \right.
$$

这里 $(X,Y)$ 是 $\mathbb{R}^2$ 上的坐标.

现在设 $M$ 与 $N$ 为两个距离空间，且 $F: M \to N$ 为一映射。我们可以像微积分里那样用 $\varepsilon - \delta$ 语言定义连续性： $F$ 在 $x_0$ 点连续，如果任给 $\varepsilon > 0$ 存在 $\delta > 0$ 使得当 $d(x, x_0) < \delta$ 时总有 $d(F(x), F(x_0)) < \varepsilon$ 。 $F$ 是连续的如果它在任何点 $x \in M$ 均连续。

容易检验在距离空间中这个定义与一般拓扑空间上的连续性定义一致.

定义3.3.14 给定一个拓扑空间 $M$ (1) 一个集合 $U \subset M$ 称为闭开集，如果它既是闭集也是开集。一个拓扑空间 $M$ 称为一个连通空间 如果它只有两个闭开集： $M$ 和 $\varnothing$ ;

(2) 一个连续映射 $\pi: I = [0,1] \to M$ 称为 $M$ 上的一个路径. $M$ 称为是路径连通的, 如果对任意两点 $x, y \in M$ 总存在一条路径 $\pi$ 使得 $\pi(0) = x$ 及 $\pi(1) = y$ .

例3.3.15 (1) $\mathbb{R}$ 是连通的. 设 $U \neq \emptyset$ 且 $U \neq \mathbb{R}$ 是 $\mathbb{R}$ 上的一个闭开集. 选 $x \in U$ 及 $y \in U^c$ . 不妨设 $x < y$ . 考虑集合 $V = \{z \in U \mid z < y\}$ . 那么 $V$ 具有最小上确界 $m \leqslant y$ 。因为 $U$ 是闭的，则 $m \in U$ ，因此 $m < y$ 。但同时开区间 $(m, y) \subset U^c$ ，它也是闭集，因为 $U$ 是开的。因此 $m \in U^c$ ，这与 $m \in U$ 矛盾。

同样的讨论显示 $\mathbb{R}$ 中的任何区间都是连通的.

(2) 一个路径连通的空间 $M$ 也是连通的。设 $U \neq \emptyset$ 及 $U \neq M$ 是 $M$ 上的闭开集。选 $x \in U$ 及 $y \in U^c$ 。因为 $M$ 是路径连通的，故存在一条路径 $\pi: I \to M$ 使得 $\pi(0) = x$ 及 $\pi(1) = y$ 。由连续性， $\pi^{-1}(U)$ 及 $\pi^{-1}(U^c)$ 均为 $I$ 上的非空闭开集，这与 (1) 矛盾。

下面的例子表明例 3.3.15 中 (2) 的逆命题不成立.

例3.3.16 在 $\mathbb{R}^2$ 上定义一个拓扑子空间为 (图3.3.3)

$$S = \{(x, y) \in \mathbb {R} ^ {2} \mid y = \sin (x ^ {- 1}), x > 0 \} \cup \{(0, y) \mid y \in \mathbb {R} \},$$

它是连通的，因为 $Y$ 轴和曲线均不是开集。但是它不是路径连通的，因为没有一条路径能连接这样的两个点，一点在 $Y$ 轴上而另一点在曲线上。

![](image/60ba669f9a4330e6242c6b968cfaa01394e9e7ad90830f549c79aa2c97e1b885.jpg)

<details>
<summary>line</summary>
