# 证明

(1) 设 $f: X \to Y$ 为一同胚映射。令 $g = f^{-1}: Y \to X$ ，那么 $g \circ f = \mathrm{id}_X$ 且 $f \circ g = \mathrm{id}_Y$ 。因此同伦映射退化为 $H(x, t) = \mathrm{id}_X$ ，及 $H(y, t) = \mathrm{id}_Y$ ；

(2) 利用极坐标，则

$$X \stackrel {\text { def }} {=} \mathbb {R} ^ {2} \backslash \{0 \} = \{(r, \theta) \mid r > 0, 0 \leqslant \theta < 2 \pi \}.Y \stackrel {\mathrm{def}} {=} S ^ {1} = \{(1, \theta) | 0 \leqslant \theta < 2 \pi \}.$$

选择 $f: X \to Y$ 为 $(r, \theta) \mapsto (1, \theta)$ , 及 $g: Y \to X$ 为 $(1, \theta) \mapsto (1, \theta)$ . 那么 $g \circ f: (r, \theta) \to (1, \theta)$ , 且 $f \circ g: (1, \theta) \to (1, \theta)$ . 因此 $f \circ g = \mathrm{id}_Y$ , 这样我们只要证明 $g \circ f \simeq \mathrm{id}_X$ 即可.

令 $H:M\times I\to M$ 为

$$H ((r, \theta), t) = (1 + (r - 1) t, \theta).$$

于是有

$$
\left\{ \begin{array}{l} H ((r, \theta), 0) = (1, \theta) = g \circ f, \\ H ((r, \theta), 1) = (r, \theta) = \mathrm{id} _ {X}; \end{array} \right.
$$

(3) 令 $Y = \{c\}$ . 定义 $f: S \to Y$ 为 $f(x) = c$ , 及 $g: Y \to S$ 为 $g(c) = c$ . 因此 $f \circ g = \mathrm{id}_Y$ , 我们只要证明 $g \circ f \simeq \mathrm{id}_X$ 即可. 设 $H(x, t) = (1 - t)c + tx$ , 那么 $H(x, 0) = c = g \circ f$ , 及 $H(x, 1) = \mathrm{id}_X$ . 于是可知 $S \simeq Y = \{c\}$ . 因此, $X$ 是可收缩的.

直观地说，如果两个映射同伦，则一个映射可以连续地转化为另一个映射。同样，如果两个空间同伦，则一个可以连续地变形为另一个。如果一个空间是可收缩的，它就可以连续地缩到一个点。例如， $\mathbb{R}$ 可以连续地缩到一个点。但是一个圆周不可能连续地缩到一个点。因为如果你想让一个圆周缩到一个点，那么至少要有一个点，它的左边往左缩，右边往右缩，于是在这一点收缩映射就不连续了。

下面考虑拓扑空间的基本群.

考察拓扑空间特征的一种方法就是看它上面的圆环。直观地说，例如，在 $S^1$ 上一个圆环不可能缩成一点。而在 $\mathbb{R}^2$ 上，任一圆环均可缩为一点。因此，它们的拓扑结构不同。这就是基本群的想法，我们从考虑路径着手。

定义 3.4.3 (1) 设 $f_{1}, f_{2}$ 为两路径，称它们为等价的，记作 $f_{1} \sim f_{2}$ ，如果它们关于两个端点同伦。换言之它们不仅同伦而且两个端点相同，即

$$f _ {1} \simeq_ {(\{0 \}, \{1 \})} f _ {2}.$$

记 $f$ 的等价类为 $[f]$ ;

(2) 如果 $f, g$ 为 $X$ 上的两个路径. $f(0) = x$ , $f(1) = y$ 且 $g(0) = y$ , $g(1) = z$ . 那么这两个路径的乘积是一条从 $x$ 到 $z$ 的路径, 定义为

$$
f \circ g = \left\{ \begin{array}{l l} f (2 t), & 0 \leqslant t \leqslant 1 / 2, \\ g (2 t - 1), & 1 / 2 \leqslant t \leqslant 1. \end{array} \right. \tag {3.4.3}
$$

直观地说，根据式(3.4.3)所定义的乘法。路径集可构成一个群，这个群的单位元是单点路径。而一条路径的逆元则是它的反向路径。不幸的是，式(3.4.3)定义的乘法不满足结合律。即， $(f \circ g) \circ h \neq f \circ (g \circ h)$ 。因此我们要考虑它们的等价类。

引理3.4.1 设 $f_{1}, f_{2}, g_{1}, g_{2}$ 为 $X$ 上的路径. 如果 $f_{1} \sim f_{2}$ 及 $g_{1} \sim g_{2}$ , 且 $f_{1}(1) = g_{1}(0)$ , 那么 $f_{1} \circ g_{1} \sim f_{2} \circ g_{2}$ .

证明 设 $H_{1}(s,t): I \times I$ 定义 $f_{1} \simeq_{(\{0\},\{1\})} f_{2}$ 的同伦，而 $H_{2}(s,t): I \times I$ 定义了 $g_{1} \simeq_{(\{0\},\{1\})} g_{2}$ 的同伦。记
