$$\lim _ {n \rightarrow \infty} \langle f _ {n}, \varphi \rangle = \langle f, \varphi \rangle , \quad \forall \varphi \in \mathcal {D} (\Omega).$$

例5.4.3 函数序列 $f_{n}(x) = \frac{1}{\pi}\frac{\sin nx}{x}$ 当 $n\to \infty$ 时收敛于 $\delta (x) = \delta_0(x)$ . 这是因为对于任意 $\varphi \in \mathcal{D}(\mathbb{R})$ ，我们有

$$\lim _ {n \rightarrow \infty} \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {\sin n x}{x} \varphi (x) = \varphi (0).$$

对于正整数 $m$ 和实数 $p \geqslant 1$ , 我们定义

$$W ^ {m, p} (\Omega) = \left\{f \in L ^ {p} (\Omega) \mid D ^ {\alpha} f \in L ^ {p} (\Omega), \forall \alpha , | \alpha | \leqslant m \right\},$$

在 $W^{m,p}(\Omega)$ 中赋以范数

$$\| f \| _ {W ^ {m, p} (\Omega)} = \left(\sum_ {| \alpha | \leqslant m} \| D ^ {\alpha} f \| _ {L ^ {p} (\Omega)} ^ {p}\right) ^ {1 / p},$$

$W^{m,p}(\Omega)$ 是一Banach空间，叫做 $(L^p (\Omega)$ 上的 $m$ 阶)Sobolev空间．当 $p = 2$ 时，记 $H^{m}(\Omega) = W^{m,2}(\Omega)$ .我们在 $H^{m}(\Omega)$ 中定义内积

$$(f, g) _ {H ^ {m} (\Omega)} = \sum_ {| \alpha | \leqslant m} (D ^ {\alpha} f, D _ {g} ^ {\alpha}) _ {L ^ {2} (\Omega)},$$

$H^{m}(\Omega)$ 是一Hilbert空间.

类似地，我们可以在流形 $\Gamma$ 上定义 $\mathcal{D}(\Gamma), \mathcal{D}'(\Gamma), L^p(\Gamma), W^{m,p}(\Gamma)$ ，和 $H^m(\Gamma)$ 等.

特别当 $n = 1, \Omega = (a, b)$ 时，我们有

$$H ^ {m} (a, b) = \{f \in L ^ {2} (a, b) \mid f, f ^ {\prime}, \dots , f ^ {(m - 1)} \text {绝对连续},\text { 并且 } f ^ {\prime}, \dots , f ^ {(m - 1)} \in L ^ {2} (a, b) \}.$$

通过插值空间方法，对于任意实数 $s$ ，可以定义非整数阶Sobolev空间 $H^{s}(\Omega)$
