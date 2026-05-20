其中 $\delta_{mn}$ 是 Kronecker delta 符号 (当 $m \neq n$ 时 $\delta_{mn} = 0$ , 而 $\delta_{mm} = 1$ ). 一可分 Hilbert 空间 $H$ 中的直交规范序列 $\{\varphi_n\}$ 叫做 $H$ 的一个直交规范基, 是指它满足 $\overline{\operatorname{span}}\left\{\varphi_n \mid n \geqslant 1\right\} = H$ . 于是对于任意 $x \in H$ , 我们有 Fourier 展开

$$x = \sum_ {n = 1} ^ {\infty} \langle x, \varphi_ {n} \rangle \varphi_ {n},$$

以及 Paserval 公式

$$\| x \| ^ {2} = \sum_ {n = 1} ^ {\infty} | \langle x, \varphi_ {n} \rangle | ^ {2}.$$

上式中的项 $\langle x, \varphi_n \rangle$ 称作 $x$ 的 Fourier 系数.

设 $A$ 是Hilbert空间 $H$ 中的线性算子，假定 $A$ 的定义域 $\mathcal{D}(A)$ 在 $H$ 中稠。我们定义 $A$ 的伴随 $A^{*}$ 如下：

$$\langle A x, y \rangle = \langle x, A ^ {*} y \rangle , \quad \forall x \in \mathcal {D} (A), y \in \mathcal {D} (A ^ {*}),$$

其中

$$\mathcal {D} (A ^ {*}) = \left\{y \in H \mid \exists z \in H \text {使得} \langle A x, y \rangle = \langle x, z \rangle , \forall x \in \mathcal {D} (A) \right\}.$$

Hilbert 空间 $H$ 上的一无界线性算子 $A$ 称为对称的，是指它满足 $A^{*} \supseteq A$ ，即

$$\text { 在 } \mathcal {D} (A) \text { 上 } A ^ {*} = A, \text { 并且 } \mathcal {D} (A ^ {*}) \supseteq \mathcal {D} (A).$$

一个对称算子 $A$ 称为自伴的，是指它满足 $\mathcal{D}(A^{*}) = \mathcal{D}(A)$ ，即 $A^{*} = A$ 。 $H$ 中的稠定线性算子 $A$ 叫做正规的，是它满足 $AA^{*} = A^{*}A$ 。

在结束本节之前，我们简单地介绍一下抽象函数的 Fourier 变换。对于任意 $p \geqslant 1$ ，令

$$L ^ {p} (\mathbb {R}; H) = \left\{f: \mathbb {R} \rightarrow H \left| \int_ {\mathbb {R}} \| f (t) \| ^ {p} \mathrm{d} t < \infty \right.\right\}.$$

在 $L^p (\mathbb{R};H)$ 中定义范数 $\| f\|_{L^p (\mathbb{R};H)} = \int_{\mathbb{R}}\| f(t)\| ^p\mathrm{d}t)^{1 / p},\| \cdot \|$ 为 $H$ 中范数，则 $L^p (\mathbb{R};H)$ 成为Banach空间，而 $L^2 (\mathbb{R};H)$ 为Hilbert空间，内积为 $\langle f,g\rangle_{L^2 (\mathbb{R};H)} =$ $\int_{\mathbb{R}}\langle f(t),g(t)\rangle \mathrm{d}t,$ 相应的诱导范数记作 $\| f\|_{L^2 (\mathbb{R};H)}.$

设 $f \in L^{2}(\mathbb{R}; H) \cap L^{1}(\mathbb{R}; H)$ , 定义 $f$ 的 Fourier 变换为

$$F (f) (s) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} t s} f (t) \mathrm{d} t.$$

仿照有穷维情形，上述变换 $F$ 可以延拓成整个 $H$ 上的酉变换，其逆变换为

$$F ^ {- 1} (f) (s) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t s} f (t) \mathrm{d} t.$$

如果记 $g = F(f)$ ，则 $\| f\|_{L^2 (\mathbb{R};H)} = \| g\|_{L^2 (\mathbb{R};H)}$ ，即

$$\int_ {\mathbb {R}} \| f (t) \| ^ {2} \mathrm{d} t = \int_ {\mathbb {R}} \| g (s) \| ^ {2} \mathrm{d} s.$$
