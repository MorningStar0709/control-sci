s
f(x₀)
H(x, s)
ω(s)
g(x₀)
(a)
</details>

![](image/bde4425ac2ad15e3c3206561bcd883226e09eace792a3cf17d65b49dcc7e5d84.jpg)

<details>
<summary>text_image</summary>

t
ω
f ∘ α
ω⁻¹
ω(4s)
ω(4 - 4s)
g ∘ α
(b)
s
</details>

图3.4.4 两个映射与路径的同伦

定理3.4.3 设 $X, Y$ 为两个路径连通的空间， $f: X \simeq Y$ 为一同伦映射，那么

$$f _ {*}: \pi_ {1} (X) \cong \pi_ {1} (Y).$$

证明 设 $x \in X$ 及 $y = f(x) \in Y$ , 而 $g: Y \to X$ 为 $f$ 的同伦. 记

$$F: g \circ f \simeq \mathrm{id} _ {X}, \quad G: f \circ g \simeq \mathrm{id} _ {Y}$$

为其相应的同伦．定义路径

$$\alpha (s) \stackrel {\mathrm{def}} {=} F (x, s), \quad \beta (s) \stackrel {\mathrm{def}} {=} G (x, s).$$

利用引理3.4.5，可得

$$
\left\{ \begin{array}{l} g _ {*} \circ f _ {*} = \alpha_ {*} (\mathrm{id} _ {X}) _ {*} = \alpha_ {*}, \\ f _ {*} \circ g _ {*} = \beta_ {*} (\mathrm{id} _ {Y}) _ {*} = \beta_ {*}. \end{array} \right.
$$

注意 $\alpha_{*}$ 及 $\beta_{*}$ 均为同构，因为比如说 $\alpha^{-1} = F(x, 1 - s)$ ，则 $\alpha_{*}\alpha_{*}^{-1} = (\mathrm{id})_{*}$ . 因此 $f_{*}$ 和 $g_{*}$ 均为同构.

最后，我们考虑另一个重要概念：复叠空间.

定义3.4.5 设 $X$ 为一拓扑空间. $(\widetilde{X}, p)$ 称为 $X$ 的一个复叠空间，如果

CS1. $\tilde{X}$ 是一个拓扑空间，且 $p: \tilde{X} \to X$ ，称为投影，是一个连续映上的映射；

CS2. 对每一点 $x \in X$ , 存在一个邻域 $U$ , 称为一个基本邻域, 使得 $p^{-1}(U)$ 由不相交的开集族 $\{V_{\lambda} \mid \lambda \in \Lambda\}$ 构成, 而且对每一个 $\lambda, p: V_{\lambda} \to U$ 是一个同胚.

$\Lambda$ 的个数 $|\Lambda|$ 称为 $\tilde{X}$ 的重数.

命题3.4.2 设 $(\tilde{X}, p)$ 为 $X$ 的一个复叠空间， $I = [0,1]$ ，且 $f: I \to X$ 是一条路径，起点为 $f(0) = x_0$ 。假定有一点 $\tilde{x}_0 \in p^{-1}(x_0)$ 。那么存在唯一的路径 $\tilde{f}: I \to \tilde{X}$ ，使得 $\tilde{f}(0) = \tilde{x}_0$ 且

$$p \circ \tilde {f} = f.$$

证明 如果 $f(I)$ 包含在一个基本邻域里，结论显见。否则，令 $\{U_{\lambda} \mid \lambda \in \Lambda\}$ 为一个由基本邻域构成的 $X$ 的覆盖，那么 $\{f^{-1}(U_{\lambda}) \mid \lambda \in \Lambda\}$ 是 $I$ 的一个开覆盖。设 $n$ 足够大使得 $\frac{1}{n}$ 小于覆盖Lebesgue数。令 $I_{i} = \left[\frac{i - 1}{n}, \frac{i}{n}\right], i = 1,2,\dots,n,$ 那么每一个 $f(I_{i})$ 包含在一个基本邻域里。由 $i = 1$ 开始，容易看出每一个 $f(I_{i})$ 具有唯一的提升，它的起点即前一个路径的终点。

从前面的证明可以看出 $I$ 可以用任何有穷维赋范空间的紧集来代替。因此立即可得到下面的命题：

命题3.4.3 设 $(\tilde{X}, p)$ 为 $X$ 的复叠空间，并且 $f: I \times I \to X$ 为一路径同伦， $f(0,0) = x_0, \tilde{x}_0 \in p^{-1}(x_0)$ ，那么存在唯一的路径同伦 $g: I \times I \to \tilde{X}, g(0,0) = \tilde{x}_0$ ，使得 $pg = f$ 。

命题3.4.4 设 $(\widetilde{X}, p)$ 为 $X$ 的复叠空间， $\widetilde{x}_0 \in p^{-1}(x_0)$ . 那么 $p_*: \pi(\widetilde{X}, \widetilde{x}_0) \to \pi(X, x_0)$ 是一个一对一的同态.
