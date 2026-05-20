$$
\begin{array}{l} f _ {*} ([ \alpha ] [ \beta ]) = [ f ] [ \alpha ] [ \beta ] [ f ] = [ f ] [ \alpha ] [ f ^ {- 1} ] [ f ] [ \beta ] [ f ^ {- 1} ] \\ = f _ {*} ([ \alpha ]) f _ {*} ([ \beta ]), \\ \end{array}
$$

则 $f_{*}$ 为一同态. 现在设 $g$ 为第一个联系 $x_{2}$ 到 $x_{3}$ 的路径, 且 $[\gamma] \in \pi_1(X, x_3)$ . 我们证明

$$(f \circ g) _ {*} ([ \gamma ]) = f _ {*} (g _ {*} ([ \gamma ])). \tag {3.4.6}$$

事实上，

$$
\begin{array}{l} (f \circ g) _ {*} ([ \gamma ]) = [ f \circ g ] [ \gamma ] [ (f \circ g) ^ {- 1} ] = [ f ] [ g ] [ \gamma ] [ g ^ {- 1} ] [ f ^ {- 1} ] \\ = [ f ] [ g ] [ \gamma ] [ g ] ^ {- 1} [ f ] ^ {- 1} = f _ {*} (g _ {*} ([ \gamma ])), \\ \end{array}
$$

这就证明了式 (3.4.6). 利用式 (3.4.6), 我们有

$$(e _ {x _ {1}}) _ {*} = (f \circ f ^ {- 1}) _ {*} = f _ {*} \circ f _ {*} ^ {- 1}.$$

但是 $(e_{x_1})_*$ 是单位映射．因此 $f_*$ 是一个同构.

根据以上的定理，当空间 $X$ 是路径连通时，我们可以不管基点而将基本群 $\pi(X, x)$ 简单记作 $\pi(X)$ .

例3.4.2 (1) 设 $S \subset \mathbb{R}^n$ 为一星形集， $x$ 为“中心”，而 $\alpha(s)$ 为以 $x$ 为基点的环路。定义同伦

$$H (s, t) = t \alpha (s) + (1 - t) x.$$

显然 $\alpha \sim e_x$ 。进而因为 $S$ 是路径连通的，基本群与基点无关。因此

$$\pi_ {1} (X) = \{e \},$$

这个群称为平凡群.

对一个路径连通的拓扑空间，如果它的基本群是平凡群，则称其为简单连通空间；

(2) 设 $X = S^1$ . 直观地, 我们可以想像它的基本群为 $\pi_1(S^1) \cong \mathbb{Z}$ , 这里 $\mathbb{Z}$ 是整数的加法群. 实际上, 一个路径绕圆周 $n$ 次对应 $n \in \mathbb{Z}$ . 当路径反向绕圆周走时, 则有 $n < 0$ . 这里略去过细的讨论;

(3) 设 $X, Y$ 为两个拓扑空间， $f: X \to Y$ 为连续映射，且 $f(x) = y$ . 定义映射 $f_{*}: \pi_{1}(X, x) \to \pi_{1}(Y, y)$ 为

$$f _ {*} ([ \alpha ]) = [ f \circ \alpha ], \tag {3.4.7}$$

它是一个群同态.

首先，我们证明式(3.4.7)是定义好的．设有 $\alpha \sim \beta$ 于是有一个同伦 $h(s,t)$ 使得

$$h (s, 0) = \alpha (s); \quad h (s, 1) = \beta (s).$$

那么

$$f \circ h (s, 0) = f \circ \alpha (s), \quad f \circ h (s, 1) = f \circ \beta (s),$$

这说明 $f \circ \alpha(s) \sim f \circ \beta(s)$ . 因此 $f_*$ 是定义好的. 其次

$$
\begin{array}{l} f _ {*} ([ \alpha ] [ \beta ]) = f _ {*} ([ \alpha \circ \beta ]) = [ f \circ (\alpha \circ \beta) ] \\ = [ (f \circ \alpha) \circ (f \circ \beta) ] = [ f \circ \alpha ] [ f \circ \beta ] \\ = f _ {*} [ \alpha ] f _ {*} [ \beta ]. \\ \end{array}
$$

因此， $f_{*}$ 是一个群同态.

粗略地说，乘积空间的基本群是其基本群的乘积.

命题3.4.1 设 $X, Y$ 为两个路径连通的拓扑空间。那么

$$\pi_ {1} (X \times Y) \cong \pi_ {1} (X) \times \pi_ {1} (Y). \tag {3.4.8}$$

证明 设 $x_0 \in X$ 及 $y_0 \in Y$ , 而 $p: X \times Y \to X$ 及 $q: X \times Y \to Y$ 为自然投影. 设 $\alpha(s) = (x(s), y(s))$ 为乘积空间基于 $(x_0, y_0)$ 的一个环路. 那么 $p_*: \pi_1(X \times Y) \to \pi_1(X)$ 是一个同态, 而且 $q_*([\alpha]) = [x(s)]$ . 同样, $q_*: \pi_1(X \times Y) \to \pi_1(Y)$ 也是一个同态, 而且 $q_*([\alpha]) = [y(s)]$ .
