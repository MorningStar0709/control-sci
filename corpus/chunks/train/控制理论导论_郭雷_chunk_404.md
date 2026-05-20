# 等距 $C_0$ 半群的某些性质

Banach 空间 X 上的 $C_{0}$ 半群 (群) $T(t)$ 叫作等距的, 是指它满足 $\|T(t)x\|=\|x\|$ , $\forall x\in X,\forall t\geqslant0(\forall t\in\mathbb{R})$ .

现在我们来刻画 Banach 空间上 $C_{0}$ 等距半群 (群) 的特征. 为了清楚起见, 有时我们用 $T^{A}(t)$ 表示由 A 生成的 $C_{0}$ 半群.

对于 $X$ 上的闭稠定线性算子 $A$ , 我们说

(1) $A$ 是守恒的，是指它满足 $\sup \left\{\operatorname{Re}\langle Ax, x^*\rangle \mid x^* \in F(x), x \in \mathcal{D}(A)\right\} = 0;$   
(2) $A$ 是强守恒的，是指它满足 $\operatorname{Re}\langle Ax, x^* \rangle = 0, \forall x^* \in F(x), x \in \mathcal{D}(A)$ ,

这里 $F: X \to X^{*}$ 是前面定义的 $X$ 上的集值对偶性映射。容易看出，(1) 中的 sup 可以用 max 代替。

引理5.3.12 设 $X$ 是Banach空间，而 $f: \mathbb{R} \to X$ . 假定 $f$ 在 $s \in [a, b]$ 弱可微，即存在 $f'(s) \in X$ 使得

$$\frac {\mathrm{d}}{\mathrm{d} s} \langle f (s), x ^ {*} \rangle = \langle f ^ {\prime} (s), x ^ {*} \rangle , \quad \forall x ^ {*} \in X ^ {*}.$$

如果 $\| f(t)\|$ 在 $t = s$ 可微，则

$$\| f (s) \| \frac {\mathrm{d}}{\mathrm{d} s} \| f (s) \| = \operatorname{Re} \left\langle f ^ {\prime} (s), x ^ {*} \right\rangle , \quad \forall x ^ {*} \in F (f (s)).$$

证明 对于 $t > s$ ，我们有

$$\operatorname{Re} \left\langle f (t) - f (s), x ^ {*} \right\rangle \leqslant (\| f (t) \| - \| f (s) \|) \| f (s) \|, \quad \forall x ^ {*} \in F (f (s)).$$

由于 $f(t)$ 在 $t = s$ 弱可微，并且 $\| f(t)\|$ 在 $s$ 可微，从上述不等式可得

$$\operatorname{Re} \left\langle f ^ {\prime} (s), x ^ {*} \right\rangle \leqslant \| f (s) \| \frac {\mathrm{d}}{\mathrm{d} s} \| f (s) \|, \quad \forall x ^ {*} \in F (f (s)).$$

对于 $t < s$ ，同理可得

$$\operatorname{Re} \left\langle f ^ {\prime} (s), x ^ {*} \right\rangle \geqslant \| f (s) \| \frac {\mathrm{d}}{\mathrm{d} s} \| f (s) \|, \quad \forall x ^ {*} \in F (f (s)),$$

证毕.

定理5.3.24 设 $A$ 是 $X$ 中的闭稠定线性算子，则 $A$ 是一 $C_0$ 等距半群 $T(t)$ 的充分必要条件为 $A$ 是守恒的，并且 $\mathcal{R}(I - A) = X$ .

证明 必要性. 假定 $A$ 是 $C_0$ 等距半群 $T(t)$ 的生成算子, 则 $T(t)$ 是压缩的, 从而 $A$ 是耗散的, 即 $\operatorname{Re}\langle Ax, x^* \rangle \leqslant 0$ , $\forall x \in \mathcal{D}(A)$ , $x^* \in F(x)$ , 并且对于任意 $\lambda$ , $\operatorname{Re} \lambda > 0$ , 有 $\lambda \in \rho(A)$ , 因而 $\mathcal{R}(I - A) = X$ .

此外，当 $x \in \mathcal{D}(A)$ 和 $s > 0$ 时， $T(s)x \in \mathcal{D}(A)$ ，而当 $0 < t < s$ 和 $x^{*} \in F(T(s)x)$ 时，成立
