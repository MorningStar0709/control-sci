由于 $T(t)$ 在任意有界区间内是一致有界的，故式(10.1.23)对于所有的 $x \in H$ 成立。因此

$$(P x, x) \geqslant \int_ {0} ^ {\infty} \| T (t) x \| ^ {2} \mathrm{d} t, \quad \forall x \in H. \tag {10.1.24}$$

由此从定理 10.1.1 推出 $T(t)$ 是指数稳定的.

今证必要性. 设 $T(t)$ 是指数稳定的. 根据定理10.1.1, 我们有

$$\int_ {0} ^ {\infty} \| T (t) x \| ^ {2} \mathrm{d} t < \infty , \quad \forall x \in H.$$

于是我们可以定义 $H$ 中线性算子 $P$ :

$$P x = \int_ {0} ^ {\infty} T ^ {*} (s) T (s) x \mathrm{d} s, \quad x \in H.$$

容易验证

$$(P x, y) = (x, P y), \quad \forall x, y \in H, \tag {10.1.25}(P x, x) \geqslant 0, \quad \forall x \in H, \tag {10.1.26}\left| (P x, y) \right| ^ {2} \leqslant \int_ {0} ^ {\infty} \| T (t) x \| ^ {2} \mathrm{d} s \int_ {0} ^ {\infty} \| T (t) y \| ^ {2} \mathrm{d} s, \tag {10.1.27}$$

这表明 $P$ 是 $H$ 中有界非负对称算子.

现在我们定义函数 $V:H\times (0,\infty)\to \mathbb{R}$ 如下：

$$V (x, t) = (P T (t) x, T (t) x) = \int_ {0} ^ {\infty} \| T (t + s) x \| ^ {2} d s.$$

对于 $x \in \mathcal{D}(A), V(x, t)$ 相对 $t$ 是可微的，并且

$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} V (x, t) = (P A T (t) x, T (t) x) + (T (t) x, P A T (t) x) \\ = \int_ {0} ^ {\infty} [ (A T (t + \tau) x, T (t + \tau) x) + (T (t + \tau) x, A T (t + \tau) x) ] d \tau \\ = \int_ {0} ^ {\infty} \frac {\mathrm{d}}{\mathrm{d} \tau} \| T (t + \tau) x \| ^ {2} \mathrm{d} \tau = - \| T (t) x \| ^ {2}. \\ \end{array}
$$

让 $t \to 0$ 取极限便得到式 (10.1.21). 证毕.

现在我们考虑 Banach 空间 $X$ 中线性系统 (10.1.1) 的强稳定性。下面的主要结果见文献 [23].

定理10.1.10 设 $T(t)$ 是Banach空间 $X$ 中闭稠定线性算子 $A$ 生成的 $C_0$ 半群．如果 $T(t)$ 强稳定甚至弱稳定，则(1) $T(t)$ 一致有界；(2) $\operatorname{Re} \lambda \leqslant 0, \forall \lambda \in \sigma(A)$ ，并且所有纯虚数不可能属于 $A$ 的点谱和剩余谱.

证明 我们只需证明最后一个结论．显然我们有 $\mathbf{i}\beta \notin \sigma_p(A), \forall \beta \in \mathbb{R}$ ．今若存在一 $\beta \in \mathbb{R}$ 使得 $\mathbf{i}\beta \in \sigma_r(A)$ ，则 $\overline{\mathcal{R}(\mathrm{i}\beta I - A)} \neq X$ ．于是依据定理5.1.3，存在 $x^{*} \in X^{*}, \| x^{*} \| = 1$ 使得

$$\langle \mathrm{i} \beta x - A x, x ^ {*} \rangle = 0, \quad \forall x \in \mathcal {D} (A),$$

由此可见 $x^{*} \in \mathcal{D}(A^{*})$ 并且 $A^{*}x^{*} = -\mathrm{i}\beta x^{*}$ . 因此对于任意 $x \in \mathcal{D}(A)$ , 我们有

$$\frac {\mathrm{d}}{\mathrm{d} t} \langle T (t) x, x ^ {*} \rangle = \langle T (t) x, A ^ {*} x ^ {*} \rangle = \mathrm{i} \beta \langle T (t) x, x ^ {*} \rangle , \quad \forall t \geqslant 0.$$

考虑到 $\langle T(0)x, x^{*} \rangle = \langle x, x^{*} \rangle$ , 我们得到 $\langle T(t)x, x^{*} \rangle = \mathrm{e}^{\mathrm{i}\beta t} \langle x, x^{*} \rangle$ . 由于 $\mathcal{D}(A)$ 在 $X$ 中稠密, 这与 $T(t)$ 的弱稳定性假设矛盾. 定理证毕.
