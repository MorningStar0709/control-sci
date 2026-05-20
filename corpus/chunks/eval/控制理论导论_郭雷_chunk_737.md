其中 $a$ 为某个给定的数．事实上，否则的话，存在两个实数列 $\{\sigma_n\}$ 和 $\{\tau_n\}$ ，其中 $0 \leqslant \sigma_n \leqslant a \forall n \geqslant 1$ ，以及 $H$ 中一规范序列 $\{z_n\}$ ，使得

$$\lim _ {\tau \rightarrow \infty} \| (\sigma_ {n} + \mathrm{i} \tau_ {n}) z _ {n} - A z _ {n} \| = 0.$$

不失一般性，我们可以假定 $\lim_{n\to \infty}\sigma_n = \sigma^* \in [0,\sigma_0]$ . 于是

$$\lim _ {\tau \rightarrow \infty} \| (\sigma^ {*} + \mathrm{i} \tau_ {n}) z _ {n} - A z _ {n} \| = 0.$$

由此可见

$$\sup \left\{\| R (\sigma^ {*} + \mathrm{i} \tau ; A) \| \mid \tau \in \mathbb {R} \right\} = + \infty ,$$

这与假设 (2) 相矛盾.

今若 $T(t)$ 一致有界，则根据Hille-Yosida定理我们有

$$\| R (\sigma + \mathrm{i} \tau ; A) \| \leqslant \frac {M}{\sigma}, \quad \forall \sigma > 0.$$

因此在这种情形下，当条件(3)满足时条件(2)自然成立．证毕.

基于上面几个定理的证明，并利用Hille-Yosida定理，我们可直接得到如下的Hilbert空间中 $C_0$ 半群增长阶的表达式：

定理10.1.7 设 $T(t)$ 是Hilbert空间 $H$ 中闭稠定线性算子 $A$ 生成的 $C_0$ 半群．那么 $T(t)$ 的增长阶是

$$\omega (A) = \inf \left\{\sigma \mid \sigma > s (A), \sup _ {\operatorname{Re} \lambda \geqslant \sigma} \| R (\lambda ; A) \| < + \infty \right\}.$$

下一定理表明，Hilbert 空间 $H$ 中 $C_0$ 半群的弱 $L^p$ -稳定性和指数稳定性是等价的。但在一般的 Banach 空间中，这种等价性未必成立。

定理10.1.8 设 $T(t)$ 是Hilbert空间 $H$ 上闭稠定线性算子 $A$ 生成的 $C_0$ 半群．那么 $T(t)$ 指数稳定当且仅当对某个 $p \geqslant 1, T(t)$ 是弱 $L^p$ -稳定的，即

$$\int_ {0} ^ {\infty} | \langle T (t) x, y \rangle | ^ {p} \mathrm{d} t < + \infty , \quad \forall x, y \in H. \tag {10.1.13}$$

证明 必要性是显然的，故只需证明充分性。于是假定对某个 $p \geqslant 1, T(t)$ 是弱 $L^p$ -稳定的。对任意固定的 $x \in H$ ，我们定义线性算子 $\varphi_x: H \to L^p(\mathbb{R}_+)$ 如下：

$$\varphi_ {x} (y) (t) = \langle T (t) x, y \rangle , \quad \forall y \in H, \forall t \geqslant 0.$$

显然 $\mathcal{D}(\varphi_x) = H$ ，并且容易看出 $\varphi_x$ 是闭的。事实上，设 $y_n \in H, f_n = \varphi_x(y_n)$ 使得当 $n \to \infty$ 时在 $H$ 中有 $y_n \to y$ ，并且在 $L^p(\mathbb{R}_+)$ 中有 $f_n \to f$ 。从内积的连续性可知

$$\lim _ {n \rightarrow \infty} \varphi_ {x} (y _ {n}) (t) = \lim _ {n \rightarrow \infty} \langle T (t) x, y _ {n} \rangle = \langle T (t) x, y \rangle = \varphi_ {x} (y) (t), \quad \forall t > 0.$$

但是在 $L^p (\mathbb{R}_+)$ 中有 $\lim_{n\to \infty}\varphi_x(y_n) = f$ ，于是 $\varphi_{x}(y)(t) = f(t)$ ，a.e. $\forall t\geqslant 0$ .这表明 $\varphi_{x}$ 是闭的．从闭图像定理可知 $\varphi_{x}$ 是有界的，由此存在正常数 $M_{x}$ 使得

$$\left(\int_ {0} ^ {\infty} | \langle T (t) x, y \rangle | ^ {p} \mathrm{d} t\right) ^ {1 / p} \leqslant M _ {x} \| y \|, \quad \forall y \in H.$$

同理，对于任意固定的 $y \in H$ ，由

$$\psi_ {y} (x) = \langle T (t) x, y \rangle , \quad \forall x \in H, \forall t \geqslant 0$$
