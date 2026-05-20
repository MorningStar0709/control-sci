$$\mathcal {R} (F) \subset \mathcal {R} (G) \Longrightarrow \| F ^ {*} x ^ {*} \| \leqslant \gamma \| G ^ {*} x ^ {*} \|, \quad \forall x ^ {*} \in X ^ {*},$$

其中 $\gamma$ 为一正常数.

证明 首先假定 $G$ 是一对一的，于是 $G^{-1}F \in \mathcal{L}(Y, Z)$ 。从而 $G^{-1}F$ 的伴随 $(G^{-1}F)^*$ 有界。注意到

$$F ^ {*} x ^ {*} = \left(G (G ^ {- 1} F)\right) ^ {*} x ^ {*} = \left(G ^ {- 1} F\right) ^ {*} G ^ {*} x ^ {*},$$

我们有

$$\| F ^ {*} x ^ {*} \| \leqslant \| G ^ {- 1} F \| \| G ^ {*} x ^ {*} \| = \gamma \| G ^ {*} x ^ {*} \|, \quad \forall x ^ {*} \in X ^ {*}.$$

对于 $G$ 不可逆的情形，我们定义商空间 $\tilde{Z} = Z / \mathcal{N}(G)$ 和由 $G$ 诱导的线性算子 $\tilde{G}: \tilde{Z} \to X,$

$$\widetilde {G} ([ z ]) = G z ^ {\prime}, \quad \forall z ^ {\prime} \in [ z ] \in \widetilde {Z}.$$

显然 $\widetilde{G}$ 是一对一的．于是对于任意 $[z] \in \widetilde{Z}$ ，根据上面已经证明的第一部分结论，我们有

$$\| F ^ {*} x ^ {*} \| \leqslant \gamma \| \widetilde {G} ^ {*} x ^ {*} \|, \quad \forall x ^ {*} \in X ^ {*}.$$

现在我们证明 $\| \widetilde{G}^* x^*\| = \| G^* x^*\|$ , $\forall x^* \in X^*$ . 事实上, 对于任意 $z \in Z$ 和 $x^* \in X^*$ , 我们有

$$\langle z, G ^ {*} x ^ {*} \rangle = \langle G z, x ^ {*} \rangle = \langle \widetilde {G} [ z ], x ^ {*} \rangle = \langle [ z ], \widetilde {G} ^ {*} x ^ {*} \rangle ,$$

由此容易得出 $\| \widetilde{G}^* x^*\| = \| G^* x^*\|$ . 证毕.

定理5.1.13 设 $X, Y, Z$ 为三个自反Banach空间，并设 $F \in \mathcal{L}(X, Y), G \in \mathcal{L}(X, Z)$ . 那么

$$\| F x \| \leqslant \gamma \| G x \|, \forall x \in X \Longrightarrow \mathcal {R} (F ^ {*}) \subset \mathcal {R} (G ^ {*}),$$

其中 $\gamma$ 为一正常数.

证明 取任一 $y^{*} \in Y^{*}$ , 并令 $x^{*} = F^{*}y^{*}$ . 今证存在 $z^{*} \in Z^{*}$ 使得 $x^{*} = G^{*}z^{*}$ . 为此我们只需证明存在 $z^{*} \in Z^{*}$ 使得

$$\langle G x, z ^ {*} \rangle = \langle F x, y ^ {*} \rangle , \quad \forall x \in X. \tag {5.1.1}$$

由于 $\| Fx\| \leqslant \gamma \| Gx\|$ , $\forall x \in X$ , 我们有 $\mathcal{N}(G) \subset \mathcal{N}(F)$ . 于是我们可以定义 $\mathcal{R}(G)$ 上线性泛函 $z_0^*$ 如下:

$$z _ {0} ^ {*} (z) = \langle F x, y ^ {*} \rangle , \quad \forall z = G x.$$

如果 $x_{n} \in X, Gx_{n} \to 0 (n \to \infty)$ , 那么 $Fx_{n} \to 0 (n \to \infty)$ , 这表明 $z_{0}^{*}$ 在 $\mathcal{R}(G)$ 上是连续的. 依据 Hahn-Banach 定理, $z_{0}^{*}$ 可以连续地延拓到整个 Banach 空间 $Z$ 上. 设 $z^{*}$ 就是 $z_{0}^{*}$ 的这样一个延拓, 则式 (5.1.1) 对该 $z^{*}$ 成立. 证毕.

推论 5.1.1 设 X, Y, Z 为三个自反的 Banach 空间，并设 $F \in \mathcal{L}(Y, X)$ , $G \in \mathcal{L}(Z, X)$ . 那么

$$\mathcal {R} (F) \subset \mathcal {R} (G) \Longleftrightarrow \| F ^ {*} x ^ {*} \| \leqslant \gamma \| G ^ {*} x ^ {*} \|, \quad \forall x ^ {*} \in X ^ {*},$$

其中 $\gamma$ 为一正常数.
