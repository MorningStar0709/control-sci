$$\int_ {a} ^ {b} \overline {{{f (x)}}} g (x) \mathrm{d} x \leqslant \sqrt {\int_ {a} ^ {b} \overline {{{f (x)}}} f (x) \mathrm{d} x} \sqrt {\int_ {a} ^ {b} \overline {{{g (x)}}} g (x) \mathrm{d} x}. \tag {3.3.10}$$

定义 3.3.3 给定一个向量空间 V. 如果存在一个映射 $\langle\cdot,\cdot\rangle:V\times V\to C$ ，满足：

11: $\langle x, x \rangle \geqslant 0$ , $\forall x \in V$ . 且 $\langle x, x \rangle = 0$ , 当且仅当 $x = 0$ ;

I2: $\langle x, y \rangle = \overline{\langle y, x \rangle}$ , $x, y \in V$ ;

I3: $\langle ax + by, z \rangle = a\langle x, z \rangle + b\langle y, z \rangle, x, y, z \in V, a, b \in \mathbb{C}$ ;

那么 $(V, \langle \cdot, \cdot \rangle)$ 称为内积空间，而 $\langle x, y \rangle$ 则称为 $x, y$ 的内积.

例3.3.5 设 $l_{2}$ 为平方收敛序列的集合，即

$$l _ {2} = \left\{\{x _ {i} \} \mid \sum_ {i = 1} ^ {\infty} \overline {{{x}}} _ {i} x _ {i} < \infty \right\},$$

定义内积

$$\langle \{x _ {i} \}, \{y _ {i} \} \rangle = \sum_ {i = 1} ^ {\infty} \overline {{{x}}} _ {i} y _ {i}. \tag {3.3.11}$$

则 $l_{2}$ 为一内积空间.

命题3.3.1 (1) 设 $V$ 为一内积空间. 定义 $V$ 上的范数为

$$\left| \left| x \right| \right| = \sqrt {\langle x , x \rangle}, \tag {3.3.12}$$

那么 $H$ 成为一个赋范空间。这种范数称为由内积导出的范数；

(2) 设 $M$ 为一赋范空间. 定义距离 $d$ 为

$$d (x, y) = | | x - y | |, \tag {3.3.13}$$

那么 M 成为一个距离空间.

需要证明式 (3.3.12) 是范数而式 (3.3.13) 是距离，我们将它留作练习.

在一个内积空间中，向量 X, Y 称为直交的，记作 $X \perp Y$ ，如果 $\langle X, Y \rangle = 0$ .

例3.3.6 如图3.3.1所示，设 $X, Y$ 为内积空间 $H$ 中的两个向量。向量 $Z$ 称为 $X$ 在 $Y$ 上的投影，如果(1) $Z = cY$ ，这里 $c \in \mathbb{C}$ ，(2) $(X - Z) \perp Y$ 。

![](image/e2b49a42ffb07a2fb9c77458e8f48aa4f7cf00c87671f4e0b59841872e99bea2.jpg)

<details>
<summary>text_image</summary>

X
X - Z
Z
Y
</details>

图3.3.1 向量的投影

容易检验 $\pmb{X}$ 在 $\pmb{Y}$ 上的投影为

$$\mathbf {Z} = \frac {\langle \mathbf {X} , \mathbf {Y} \rangle}{\langle \mathbf {Y} , \mathbf {Y} \rangle} \mathbf {Y}.$$

由于 $\langle X - Z, X - Z \rangle \geqslant 0$ , 由此可知

$$\langle \boldsymbol {X}, \boldsymbol {Y} \rangle \leqslant \| \boldsymbol {X} \| \| \boldsymbol {Y} \|, \tag {3.3.14}$$

而且等式成立当且仅当 $X - Z = 0$ ，即 $X = cY, c \in \mathbb{C}$ .

式 (3.3.14) 是 Schwarz 不等式的一般形式. 将它用于 $\mathbb{R}^2, L^2[a, b], l_2$ , 则分别得到不同的具体形式.

基于命题3.3.1，在本书中内积空间及赋范空间均看作距离空间，除非另有说明，其距离总认为是由内积或范数导出.

在一个距离空间 $(M, d)$ 中，设 $x \in M, r > 0$ 。我们记 $B_r(x)$ 为一个半径为 $r$ 球心为 $x$ 的球，即

$$B _ {r} (x) = \{y \in X \mid d (y, x) < r \}.$$

注意球的形状依赖于距离。例如，在 $\mathbb{R}^2$ 中相应于距离 $d_2, d_1, d_\infty$ 和 $d_P$ 的球 $B_1(0)$ 在图3.3.2中给出。对于 $d_P$ 选矩阵 $\pmb{P} = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}$ 。
