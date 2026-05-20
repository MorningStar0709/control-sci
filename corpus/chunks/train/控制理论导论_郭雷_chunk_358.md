定理5.1.14 设 $X, Y, Z$ 为三个Banach空间，并设 $F \in \mathcal{L}(Y, X), G \in \mathcal{L}(Z, X)$ . 那么

$$\mathcal {R} (F) \subset \overline {{{\mathcal {R} (G)}}} \Longleftrightarrow \mathcal {N} (G ^ {*}) \subset \mathcal {N} (F ^ {*}).$$

证明 首先假定 $\mathcal{N}(G^{*})\subset \mathcal{N}(F^{*})$ ，但 $\mathcal{R}(F)$ 并不包含在 $\overline{\mathcal{R}(G)}$ 中．那么必存在一元 $x_0\in \mathcal{R}(F)$ ，但 $x_0\notin \overline{\mathcal{R}(G)}$ ，于是存在 $x^{*}\in X^{*}$ 使得在 $\mathcal{R}(C)$ 上 $x^{*} = 0,$ 并且 $\langle x_0,x^*\rangle \neq 0.$ 由此

$$\langle G z, x ^ {*} \rangle = 0, \quad \forall z \in Z,$$

从而 $x^{*}\in \mathcal{N}(G^{*})$ .然而若 $x^{*}\in \mathcal{N}(F)$ ，则

$$\langle F y, x ^ {*} \rangle = 0, \quad \forall y \in Y,$$

这与 $\langle x_0, x^* \rangle \neq 0$ 相矛盾.

反之，假定 $\overline{\mathcal{R}(G)}\supset \mathcal{R}(F)$ 并且 $G^{*}x^{*} = 0$ ，则

$$\langle G z, x ^ {*} \rangle = 0, \quad \forall z \in Z,$$

由此推出在 $\mathcal{R}(G)$ 上 $x^{*} = 0$ 因此

$$\langle F y, x ^ {*} \rangle = 0, \quad \forall y \in Y,$$

即 $F^{*}x^{*} = 0$ ，定理证毕.

线性空间 $H$ 上的内积是指定义在 $H \times H$ 上取值在实或复数域 $K$ 的一个映射 $\langle \cdot, \cdot \rangle: H \times H \to K$ 满足

(1) $\langle x, x \rangle \geqslant 0$ , $\langle x, x \rangle = 0 \Longleftrightarrow x = 0$ ;   
(2) $\overline{\langle x, y \rangle} = \langle y, x \rangle, \quad \forall x, y \in H;$   
(3) $\langle \alpha x + \beta y, z \rangle = \alpha \langle x, z \rangle + \beta \langle y, z \rangle, \forall x, y, z \in H, \alpha, \beta \in K.$

定义内积 $\langle \cdot, \cdot \rangle$ 的线性空间 $H$ 叫做内积空间。在内积空间 $H$ 中定义范数 $\| x \| = \sqrt{\langle x, x \rangle}$ ，则 $H$ 也是一个 Banach 空间。一个完备的内积空间叫做 Hilbert 空间。

Hilbert 空间 $H$ 中两个向量 $x$ 和 $y$ 叫做直交的, 是指满足 $\langle x, y \rangle = 0$ , 这时我们记作 $x \perp y$ . $H$ 中两个集合 $M$ 和 $N$ 叫做直交的, 是指满足 $\langle x, y \rangle = 0$ , $\forall x \in M, y \in N$ , 记作 $M \perp N$ . 对于集合 $M \subset H$ , $M$ 的直交补 $M^{\perp}$ 定义成

$$M ^ {\perp} = \left\{x \in H \mid \langle x, y \rangle = 0, \forall y \in M \right\}.$$

显然 $M^{\perp}$ 是 $H$ 的一闭线性子空间，并且 $H$ 可以唯一地分解成直交和

$$H = \overline {{\operatorname{span}}} M \oplus M ^ {\perp},$$

其中 $\overline{\mathrm{span}} M$ 是由 $M$ 张成的闭线性子空间.

Hilbert 空间 $H$ 中一序列 $\{\varphi_n\}$ 叫做直交的，是指它满足 $\varphi_m \perp \varphi_n, \forall m \neq n;$ 叫做直交规范的，是指它满足

$$\langle \varphi_ {m}, \varphi_ {n} \rangle = \delta_ {m n}, \quad \forall m, n \geqslant 1,$$
