# 3.3 拓扑空间

拓扑结构是一切几何结构的基础，它使空间从“混沌”变为有序.

一个拓扑空间是一个带有拓扑结构的集合。这些结构来自开集，闭集等。而这些概念最初都来自距离空间。因此，我们从距离空间的研究开始。

定义3.3.1 一个距离空间 $(M, d)$ 由两个部分组成：一个集合 $M$ 和一个映射 $d: M \times M \to \mathbb{R}$ ，它满足以下条件：

M1. $0 \leqslant d(x, y) < \infty, \quad \forall x, y \in M$ ;

M2. $d(x,y) = 0$ ，当且仅当 $x = y$

M3. $d(x,y) = d(y,x)$ ;

M4. (三角不等式)

$$d (x, z) \leqslant d (x, y) + d (y, z), \quad x, y, z \in M.$$

例3.3.1 通常 $\mathbb{R}^n$ 是一个距离空间，它有以下几种常见距离：

$$d _ {2} (x, y) = \sqrt {\sum_ {i = 1} ^ {n} (x _ {i} - y _ {i}) ^ {2}}, \tag {3.3.1}d _ {\infty} (x, y) = \max _ {1 \leqslant i \leqslant n} | x _ {i} - y _ {i} |, \tag {3.3.2}d _ {1} (x, y) = \sum_ {i = 1} ^ {n} | x _ {i} - y _ {i} |, \tag {3.3.3}d _ {P} (x, y) = \sqrt {(x - y) ^ {\mathrm{T}} P (x - y)}, \tag {3.3.4}$$

这里 P 是一个正定矩阵.

例3.3.2 考虑 $\mathbb{R}^n$ .定义

$$
d (x, y) = \left\{ \begin{array}{l l} 0, & x = y, \\ 1, & x \neq y. \end{array} \right.
$$

请读者自行检验这是一个距离．（实际上在这个例子里 $\mathbb{R}^n$ 可换成任意集合 $S$ ，对任意两点 $x,y\in S$ 定义如上的距离.）

后面我们将证明在例3.3.1中的距离导出的拓扑都一样，但它们与例3.3.2中的距离导出的拓扑不一样.

定义3.3.2 设 $V$ 为一线性距离空间，如果存在一个映射， $\| \cdot \| : V \to \mathbb{R}$ ，满足

N1. $||x|| \geqslant 0, \forall x \in V$ , 且 $||x|| = 0$ , 当且仅当 $x = 0$ ;

N2. $||rx|| = |r|||x||,$ $r\in \mathbb{R}, x\in V;$

N3. (三角不等式)

$$\left| \left| x + y \right| \right| \leqslant \left| \left| x \right| \right| + \left| \left| y \right| \right|, \quad x, y \in V,$$

则 $(V, ||\cdot||)$ 称为一个赋范空间， $\|x\|$ 称为 $x$ 的范数.

例3.3.3 考虑 $\mathbb{R}^n$ 。在普通加法及数乘下它是一个向量空间。定义几种范数如下：

$$\left| \left| x \right| \right| _ {2} = \sqrt {\sum_ {i = 1} ^ {n} x _ {i} ^ {2}}, \tag {3.3.5}\left| \left| x \right| \right| _ {\infty} = \max _ {1 \leqslant i \leqslant n} \left| x _ {i} \right|, \tag {3.3.6}\left| \left| x \right| \right| _ {1} = \sum_ {i = 1} ^ {n} \left| x _ {i} \right|. \tag {3.3.7}\left| \left| x \right| \right| _ {P} = \sqrt {x ^ {\mathrm{T}} P x}, \tag {3.3.8}$$

这里 P 是一个正定矩阵.

可以证明式 (3.3.5)\~(3.3.8) 定义的均为范数。我们将证明留给读者作练习。

例3.3.4 设 $L^2 [a,b]$ 是平方可积的复函数集合，即

$$L ^ {2} [ a, b ] = \left\{f (x) \left| \left| \int_ {a} ^ {b} \overline {{{f (x)}}} f (x) \mathrm{d} x \right| < \infty \right. \right\},$$

它是 $\mathbb{C}$ 上的一个向量空间. 定义

$$\left| \left| f (x) \right| \right| = \sqrt {\int_ {a} ^ {b} \overline {{{f (x)}}} f (x) \mathrm{d} x}. \tag {3.3.9}$$

不难检验式 (3.3.9) 定义了一个范数。因此， $L^2[a, b]$ 是一个赋范空间。除三角不等式外其他是显见的，而三角不等式同时也证明了式 (3.3.9) 是定义好的，即积分有限。这可由以下的 Schwarz 不等式得到：
