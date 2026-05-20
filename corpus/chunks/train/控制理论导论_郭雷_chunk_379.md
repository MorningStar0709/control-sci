由于 $X^{*}$ 中闭单位球在 $X^{*}$ 的弱 $-^{*}$ 拓扑下是紧的，所以集合 $\{z_{\lambda}^{*}\}$ 当 $\lambda \to \infty$ 时有弱 $-^{*}$ 聚点 $z^{*} \in X^{*}$ . 显然 $\| z^{*} \| \leqslant 1$ . 然后在式 (5.3.18) 和式 (5.3.19) 中让 $\lambda \to \infty$ 取极限，便得到

$$\operatorname{Re} \langle A x, z ^ {*} \rangle \leqslant 0, \quad \operatorname{Re} \langle x, z ^ {*} \rangle \geqslant \| x \|.$$

但 $\operatorname{Re}\langle x, z^* \rangle \leqslant \|x\|$ , 故 $\langle x, z^* \rangle = \|x\|$ . 令 $x^* = \|x\|z^*$ , 则我们得到 $x^* \in F(x)$ 和 $\operatorname{Re}\langle Ax, x^* \rangle \leqslant 0$ , 由此可知 $A$ 是耗散的.

定理5.3.7 (Lummer-Phillips) 设 $A$ 是Banach空间 $X$ 中一稠定线性算子.

(1) 如果 $A$ 是耗散的，并且存在 $\lambda_0 > 0$ 使得 $\mathcal{R}(\lambda_0 I - A) = X$ ，则 $A$ 是一 $C_0$ 压缩半群的生成算子；  
(2) 如果 $A$ 是某 $C_0$ 压缩半群的生成算子，则 $A$ 是耗散的，并且 $\mathcal{R}(\lambda I - A) = X, \forall \lambda > 0$ ; 此外

$$\operatorname{Re} \langle A x, x ^ {*} \rangle \leqslant 0, \quad \forall x \in \mathcal {D} (A), x ^ {*} \in F (x).$$

证明 (1) 对于 $\lambda > 0$ , 依据引理5.3.4, 我们有 $\|(\lambda I - A)x \| \geqslant \lambda \|x\|$ , $\forall x \in \mathcal{D}(A)$ . 由于 $\mathcal{R}(\lambda_0 I - A) = X$ , 我们有 $\lambda_0 \in \rho(A)$ . 因此 $A$ 是闭的. 可以证明 $\mathcal{R}(\lambda I - A) = X$ , $\forall \lambda > 0$ . (留作练习) 这样我们证明了 $(0, \infty) \subset \rho(A)$ 和 $\|R(\lambda; A)\| \leqslant 1/\lambda, \forall \lambda > 0$ .

因此根据Hille-Yosida定理，我们得出结论： $A$ 是 $X$ 上某 $C_0$ 压缩半群的生成算子；

(2) 下面设 $T(t)$ 是 $X$ 上由 $A$ 生成的 $C_0$ 压缩半群. 如果 $x \in \mathcal{D}(A), x^* \in F(x)$ , 则 $|\langle T(t)x, x^* \rangle| \leqslant \|T(t)x\| \|x^*\| \leqslant \|x\|^2$ . 因此

$$\operatorname{Re} \left\langle T (t) x - x, x ^ {*} \right\rangle \leqslant 0. \tag {5.3.20}$$

用 $t > 0$ 除式 (5.3.20) 式两端，然后令 $t \to 0$ ，我们得到 $\operatorname{Re}\langle Ax, x^* \rangle \leqslant 0$ 。证毕。

注5.3.1 从Lummer-Phillips定理我们知道，为了Banach空间 $X$ 上一稠定线性算子 $A$ 是 $X$ 上某一 $C_0$ 压缩半群的生成算子，必须且只需 $A$ 在 $X$ 中是 $\mathfrak{m}$ -耗散的.

推论5.3.1 设 $A$ 是Banach空间 $X$ 中的闭稠定线性算子. 如果 $A$ 和 $A^{*}$ 都是耗散的, 则 $A$ 生成 $X$ 上一 $C_0$ 压宿半群.

证明 留作练习.

下面给出 $C_0$ 半群生成算子的一些例子.

例5.3.6 设 $X$ 是Banach空间， $A \in \mathcal{L}(X)$ ，则半群 $\mathrm{e}^{At}$ 的生成算子恰好是 $A$ .

例5.3.7 例5.3.3中 $C_0$ 半群的生成算子是

$$A = \frac {\mathrm{d}}{\mathrm{d} x}, \quad \mathcal {D} (A) = \left\{f \in C [ 0, \infty ] \mid f ^ {\prime} \in C [ 0, \infty ] \right\}.$$

例5.3.8 例5.3.4中 $C_0$ 半群的生成算子是
