$$
H (s, 0) = \left\{ \begin{array}{l l} x, & s \leqslant 1 / 2, \\ \alpha (2 s - 1), & s \geqslant 1 / 2. \end{array} \right.
$$

这是乘积 $e_x \circ \alpha$ . 同时 $H(s, 1) = \alpha(s)$ . 并且 $H(0, t) = x$ , $H(1, t) = \alpha(1) = y$ . 因此 $e_x \circ \alpha \sim \alpha$ .

当同伦构造出来后这类问题的证明就很简单了。因此关键是怎么构造同伦？我们以以上的证明为例作一点解释。参见图3.4.1，对于正方形，在 $t = 0$ 我们需要两段：前一半是 $x$ 而后一半是 $\alpha(s)$ 。而在 $t = 1$ 我们只需 $\alpha$ 。在左边， $s = 0$ 它是 $x$ ，而在右边 $s = 1$ ，我们需要 $y$ 。建立 $H$ 的一个方法是将正方形分为两部分： $t \leqslant 1 - 2s$ 和 $t \geqslant 1 - 2s$ 。在左半边区域设 $H = x$ ，在右边梯形内的任意一点 $(s, t)$ ，设 $H(s, t) = H(s^*, 1)$ ，这里 $s^* = \frac{2s + t - 1}{t + 1}$ 。这样我们就得到了所要求的 $H$ 。

![](image/c8474d875b27018eb96af0fe3552df53f327bb1d19068427e223b4a5398890bb.jpg)

<details>
<summary>text_image</summary>

t
1
α
s*
H(s, t)
x
y
x
0
α
1 s
</details>

图3.4.1 id-同伦

$\alpha(t)$ 的逆 $\alpha^{-1}(t)$ 可以简单地定义为 $\alpha^{-1}(t) = \delta(1 - t)$ . 显然当 $\alpha$ 从 $x$ 走到 $y$ , $\alpha^{-1}$ 从 $y$ 走到 $x$ . 它们必须满足以下引理:

引理3.4.4 设 $\alpha$ 为一路径， $\alpha(0) = x$ 且 $\alpha(1) = y$ 。那么 $[\alpha][\alpha^{-1}] = [e_x]$ 且 $[\alpha^{-1}][\alpha] = \{e_y\}$ .

证明 我们证 $\alpha \circ \alpha^{-1} \sim e_x$ : 利用图3.4.2, 设 $H(s,t) = H(s^*,0) (s < t)$ , 则得

同伦

$$
H (s, t) = \left\{ \begin{array}{l l} x, & 0 \leqslant s \leqslant t, \\ \alpha \left(\frac {2 (s - t)}{1 - t}\right), & t <   s \geqslant \frac {t + 1}{2}, \\ \alpha \left(\frac {2 (1 - s)}{1 - t}\right), & \frac {t + 1}{2} <   s \leqslant 1. \end{array} \right.
$$

同样我们可以证明 $\alpha^{-1} \circ \alpha \sim e_y$ .

![](image/c6593e2df0305afcf0652253604db39ebaf2ccb398768274078da7b3558d8698.jpg)

<details>
<summary>text_image</summary>

t
1
x
x
0 x y s* x s
H(s,t)
1
</details>

图3.4.2 路径 $\alpha$ 及 $\alpha^{-1}$

由引理 3.4.2\~3.4.4 可得到完整的群结构。因此我们有以下定理：

定理3.4.1 设 $x \in X$ . 记以 $x$ 为基点的所有环路的等价类为 $\Omega(X, x)$ . 利用由式(3.4.3)\~(3.4.4)定义的乘法, 则 $\Omega(X, x)$ 为一个群. 它称为基于 $x$ 的基本群, 记作 $\pi_1(X, x)$ .

下面的定理指出当空间 $X$ 是路径连通时，基本群不依赖于基点.

定理3.4.2 设 $X$ 为一道路连通的空间， $x_{1}, x_{2} \in X$ ，那么

$$\pi_ {1} (X, x _ {1}) \cong \pi_ {2} (X, x _ {2}).$$

证明 设 $f(s)$ 为一路径 $f(0) = x_{1}$ 且 $f(1) = x_{2}$ , 而 $\alpha(s)$ 为一基点为 $x_{2}$ 的环路. 那么 $f \circ \alpha \circ f^{-1}$ 是一基点为 $x_{1}$ 的环路. 现在我们定义一个映射 $f_{*}: \pi_{1}(X, x_{2}) \to$

$\pi_{1}(X, x_{1})$ 如下：

$$f _ {*}: [ \alpha ] \mapsto [ f ] [ \alpha ] [ f ^ {- 1} ]. \tag {3.4.5}$$

只要证明 $f_{*}$ 是一个群同构即可．因为
