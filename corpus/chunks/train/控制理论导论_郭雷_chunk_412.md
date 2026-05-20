# 广义函数和 Sobolev 空间定义

设 $\Omega$ 为 $\mathbb{R}^N$ 中带充分光滑边界 $\Gamma$ 的开集. $\mathcal{D}(\Omega) = C_0^\infty (\Omega)$ 表示定义在 $\Omega$ 上取值在 $\mathbb{R}$ 或 $\mathbb{C}$ 中无穷次可微且具紧支集的函数空间. 这里对于 $\Omega$ 上一个连续函数 $\varphi$ , 将 $\varphi(x) \neq 0$ 的点全体的闭包称为 $\varphi$ 的支集, 即

$$\operatorname{supp} \varphi = \overline {{\{x \in \Omega | \varphi (x) \neq 0 \}}}.$$

$\mathcal{D}(\Omega)$ 上定义如下拓扑：序列 $\{\varphi_n\} \subset \mathcal{D}(\Omega)$ 收敛于0是指它满足

(1) 诸 $\varphi_{n}$ 的支集位于 $\Omega$ 的一固定紧集中；

(2) $\varphi_{n}$ 及其各阶导数均一致收敛于0.

$\mathcal{D}'(\Omega)$ 表示 $\mathcal{D}(\Omega)$ 上的连续线性泛函空间. $\mathcal{D}'(\Omega)$ 中的元叫做 $\Omega$ 上的广义函数或分布.

对于 $\alpha=(\alpha_{1},\cdots,\alpha_{N})$ ， $\alpha_{k}$ 为任意非负整数，记 $|\alpha|=\alpha_{1}+\cdots+\alpha_{N}$

$$D ^ {\alpha} = D _ {1} ^ {\alpha_ {1}} \dots D _ {N} ^ {\alpha^ {N}}, \quad D _ {k} = \frac {\partial}{\partial x _ {k}}.$$

我们定义 $f \in \mathcal{D}'(\Omega)$ 的任意阶导数 $D^{\alpha}f$

$$\langle D ^ {\alpha} f, \varphi \rangle = (- 1) ^ {| \alpha |} \langle f, D ^ {\alpha} \varphi \rangle , \quad \forall \varphi \in \mathcal {D} (\Omega),$$

这里 $\langle \cdot, \cdot \rangle$ 表示 $\mathcal{D}'(\Omega)$ 与 $\mathcal{D}(\Omega)$ 之间的标量积，即 $\langle f, \varphi \rangle = f(\varphi)$ 为 $f$ 在 $\varphi$ 处的取值。对于定义在 $\Omega$ 上的局部可积函数 $f$ ，由

$$\langle \tilde {f}, \varphi \rangle = \int_ {\Omega} f (x) \varphi (x) \mathrm{d} x, \quad \forall \varphi \in \mathcal {D} (\Omega)$$

定义的 $\tilde{f}$ 是 $\Omega$ 上的分布，通常我们把 $\tilde{f}$ 等同于 $f$ .

例5.4.1 对于 $x_0 \in \Omega, \delta_{x_0}(x) = \delta(x - x_0)$ 表示Dirac $\delta$ -函数，定义为

$$\langle \delta_ {x _ {0}}, \varphi \rangle = \int_ {\Omega} \delta (x - x _ {0}) \varphi (x) \mathrm{d} x = \varphi (x _ {0}).$$

不难看出， $\delta_{x_{0}}\in\mathcal{D}^{\prime}(\Omega)$ .

例5.4.2 设Heviside函数 $H(x)$ 定义为

$$
H (x) = \left\{ \begin{array}{l l} 1, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.
$$

函数 $H(x)$ 当 $x \neq 0$ 时是可微的，并且 $H'(x) = 0$ 。但在 $x = 0$ 处是间断的，从而在常义下在 $x = 0$ 处不可微。但是，在广义下 $H$ 的导数存在，并且 $H'(x) = \delta(x)$ ，这是因为对于任意 $\varphi \in \mathcal{D}(\mathbb{R})$ 。依据广义函数导数的定义

$$\langle H ^ {\prime}, \varphi \rangle = - \langle H, \varphi^ {\prime} \rangle = - \int_ {0} ^ {\infty} \varphi^ {\prime} (x) \mathrm{d} x = \varphi (0).$$

广义函数序列 $\{f_n\} \subset \mathcal{D}'(\Omega)$ 称为 (弱) 收敛于 $f \in \mathcal{D}'(\Omega)$ , 是指它满足
