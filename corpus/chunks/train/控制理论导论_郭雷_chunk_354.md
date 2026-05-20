# 5.1 Banach 空间和 Hilbert 空间

设 $X$ 是标量场 $K$ (实数域 $\mathbb{R}$ 或复数域 $\mathbb{C}$ ) 上的一线性空间, 映射 $\| \cdot \|: X \to \mathbb{R}_+$ 叫做 $X$ 上的一个范数, 是指它满足

(1) $\| x\| \geqslant 0$ ，并且 $\| x\| = 0\Longleftrightarrow x = 0,\forall x\in X;$   
(2) $\| \alpha x \| = |\alpha| \| x\|$ , $\forall x \in X, \alpha \in K$ ;   
(3) $\| x + y \| \leqslant \| x \| + \| y \|$ (三角形不等式).

赋以范数 $\| \cdot \|$ 的线性空间 $X$ 叫做赋范线性空间，有时也简称赋范空间。对于 $X$ 中的序列 $\{x_{n}\}$ ，如果存在元 $x \in X$ ，使得 $\lim_{n \to \infty} \| x_{n} - x \| = 0$ ，则 $x$ 叫做序列 $\{x_{n}\}$ 的极限，记作 $\lim_{n \to \infty} x_{n} = x$ ，或 $x_{n} \to x (n \to \infty)$ 。赋范空间 $X$ 叫做完备的，是指 $X$ 中任意 Cauchy 序列都收敛于 $X$ 中某个点。完备的赋范空间叫做 Banach 空间。

线性空间 $X$ 上的两个范数 $\| \cdot \|_1$ 和 $\| \cdot \|_2$ 叫做是等价的，是指存在两个正常数 $c_{1}$ 和 $c_{2}$ 使得

$$c _ {1} \| x \| _ {1} \leqslant \| x \| _ {2} \leqslant c _ {2} \| x \| _ {1}, \quad \forall x \in X.$$

赋范线性空间 $X$ 上的集合 $M$ 叫做是相对紧的，是指 $M$ 中的任意无穷序列都含有一收敛的子序列。一个闭的相对紧集叫做紧集。

设 $M$ 是Banach空间 $X$ 中一闭子空间。对于任意 $x \in X$ ，集合 $[x] = \{y \in X \mid x - y \in M\}$ 叫做陪集。设 $X / M$ 表示所有陪集的全体，叫做商空间。如果在 $X / M$ 中定义加法和数乘，以及范数如下：

$$[ x ] + [ y ] = [ x + y ], \quad \alpha [ x ] = [ \alpha x ],\| [ x ] \| = \inf \left\{\| y \| \mid y \in [ x ] \right\},$$

则 $X / M$ 成为一新的Banach空间.

定理 5.1.1 设 M 是赋范线性空间 X 的一子集. 如果 M 是相对紧的, 则 M 是全有界的, 即对于任意 $\varepsilon > 0$ , 存在有穷多个点 $x_{1}, x_{2}, \cdots, x_{n} \in X$ 使得

$$M \subset \bigcup_ {k = 1} ^ {n} B (x _ {k}; \varepsilon),$$

其中 $B(x_{k};\varepsilon)\stackrel {\mathrm{dof}}{=}\left\{x\in X\mid \| x - x_{k}\| <  \varepsilon \right\}$ 表示 $X$ 中中心在 $x_{k}$ 半径为 $\varepsilon$ 的开球. 反之，如果 $X$ 是完备的，则集合的全有界性隐含相对紧性.

定理 5.1.2 为了 Banach 空间 X 中的子集 M 是紧的，必须且只需 M 的任意开覆盖都含有 M 的有穷子开覆盖。这里 X 中的集族 $\{O_{\nu} \mid \nu \in \Lambda\}$ 叫做 M 的一个覆盖，是指 $M \subset \bigcup_{\nu \in \Lambda} O_{\nu}$ 。

设 $X$ 是一赋范线性空间， $X$ 上的连续 (即有界) 线性泛函全体记作 $X^{*}$ ，叫做 $X$ 的对偶空间。在对偶空间 $X^{*}$ 中，我们定义加法和标量乘法为

$$(f + g) (x) \stackrel {\mathrm{def}} {=} f (x) + g (x). \quad f, g \in X ^ {*}, x \in X;(\alpha f) (x) \stackrel {\text { def }} {=} \overline {{\alpha}} f (x), \quad f \in X ^ {*}, \alpha \in K, x \in X,$$

则 $X^{*}$ 成为一线性空间. 对于每个 $f \in X^{*}$ , 我们定义 $f$ 的范数

$$\| f \| = \sup \left\{\left| f (x) \right| \mid \| x \| = 1, x \in X \right\},$$

则 $X^{*}$ 也是一个Banach空间．为了简单起见，通常我们把 $f\in X^{*}$ 在 $\pmb {x}\in X$ 的值记作

$$\langle x, f \rangle \stackrel {\mathrm{def}} {=} f (x),$$

也叫做 $f$ 与 $\pmb{x}$ 的配对.

定理5.1.3 (Hahn-Banach定理) 设 $X_0$ 是赋范线性空间 $X$ 的一子空间, $f_0$ 是 $X_0$ 上一有界线性泛函, 则存在 $f \in X^*$ 使得

$$f (x) = f _ {0} (x), \quad \forall x \in X _ {0},\| f \| = \| f _ {0} \| x _ {0}.$$
