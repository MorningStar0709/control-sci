(1') $\{\lambda \in \mathbb{R} | \lambda > \omega\} \subset \rho(A)$ ;   
(2') $\| (\lambda I - A)^{-n}\| \leqslant M(\lambda -\omega)^{-n},\quad \forall \lambda >\omega ,\forall n\geqslant 1.$

定理5.3.6 设 $X$ 是一白反Banach空间， $T(t)$ 是 $X$ 上由 $A$ 生成的 $C_0$ 半群。那么 $T^{*}(t)$ 是 $X^{*}$ 上由 $A^{*}$ 生成的 $C_0$ 半群。

证明 留作练习.

设 $X$ 是一Banach空间，定义对偶性(集值)映射 $F:X\to X^{*}$ 如下：

$$F (x) = \left\{x ^ {*} \in X ^ {*} \mid \langle x, x ^ {*} \rangle = \| x \| ^ {2} = \| x ^ {*} \| ^ {2} \right\}, \quad x \in X.$$

根据 Hahn-Banach 定理， $F(x) \neq \varnothing, \forall x \in X.$

定义 5.3.3 Banach 空间 X 上一线性算子 A 叫做是耗散的，是指它满足： $\forall x \in \mathcal{D}(A)$ ，存在 $x^{*} \in F(x)$ 使得 $\operatorname{Re}\langle Ax, x^{*} \rangle \leqslant 0$ 。如果 A 还满足 $R(\lambda I - A) = X, \forall \lambda > 0$ ，则称 A 为 m-耗散的。

我们注意，对于 Hilbert 空间 $X$ ，如果把 $X$ 与其对偶 $X^{*}$ 等同，则 $X$ 上的对偶性映射可以看成是恒等映射。从而 Hilbert 空间 $X$ 上线性算子 $A$ 的耗散性意味着 $\operatorname{Re}(Ax, x) \leqslant 0, \forall x \in \mathcal{D}(A)$ 。

引理5.3.4 设 $A$ 是Banach空间 $X$ 中一线性算子，则为了 $A$ 是耗散的，必须且只需

$$\| (\lambda I - A) x \| \geqslant \lambda \| x \|, \quad \forall x \in \mathcal {D} (A), \quad \forall \lambda > 0. \tag {5.3.17}$$

证明 首先设 $A$ 是耗散的. 任取 $x \in \mathcal{D}(A)$ , $\lambda > 0$ 和 $x^{*} \in F(x)$ 使得 $\operatorname{Re}\langle Ax, x^{*} \rangle \leqslant 0$ , 那么

$$\| \lambda x - A x \| \| x \| \geqslant | \langle \lambda x - A x, x ^ {*} \rangle | \geqslant \operatorname{Re} \langle \lambda x - A x, x ^ {*} \rangle \geqslant \lambda \| x \| ^ {2},$$

由此推出式 (5.3.17) 成立。反之设式 (5.3.17) 满足，并任取 $x \in \mathcal{D}(A)$ 。对于每一 $\lambda > 0$ ，选择 $y_{\lambda}^{*} \in F(\lambda x - Ax)$ 并令 $z_{\lambda}^{*} = y_{\lambda}^{*} / \| y_{\lambda}^{*}\|$ 。于是 $\| z_{\lambda}^{*}\| = 1$ ，并且

$$
\begin{array}{l} \lambda \| x \| \leqslant \| \lambda x - A x \| = \left\langle \lambda x - A x, z _ {\lambda} ^ {*} \right\rangle \\ = \lambda \operatorname{Re} \left\langle x, z _ {\lambda} ^ {*} \right\rangle - \operatorname{Re} \left\langle A x, z _ {\lambda} ^ {*} \right\rangle \\ \leqslant \lambda \| x \| - \operatorname{Re} \left\langle A x, z _ {\lambda} ^ {*} \right\rangle , \quad \forall \lambda > 0. \\ \end{array}
$$

因此

$$\operatorname{Re} \left\langle A x, z _ {\lambda} ^ {*} \right\rangle \leqslant 0, \tag {5.3.18}\operatorname{Re} \left\langle x, z _ {\lambda} ^ {*} \right\rangle \geqslant \| x \| - \frac {1}{\lambda} \| A x \|. \tag {5.3.19}$$
