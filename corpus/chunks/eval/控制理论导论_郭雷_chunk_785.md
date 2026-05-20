容易验证假设 (H1) 和 (H2) 满足. 今证 B 也满足 (H3). 事实上, 设 J 为区间 $(c, d)$ . 我们有

$$
\begin{array}{l} \| B y _ {n} \| ^ {2} \geqslant \int_ {c} ^ {d} b (x) ^ {2} \frac {1}{\ell} \sin^ {2} \frac {\left(n + \frac {1}{2}\right) \pi}{\ell} x \mathrm{d} x \\ \geqslant \frac {b _ {0} ^ {2}}{\ell} \int_ {c} ^ {d} \sin^ {2} \frac {\left(n + \frac {1}{2}\right) \pi}{\ell} x \mathrm{d} x \\ = \left. \frac {b _ {0} ^ {2}}{2 \ell} \left(x - \frac {\ell}{(2 n + 1) \pi} \sin \frac {(2 n + 1) \pi}{\ell} x\right) \right| _ {x = c} ^ {x = d} \\ \rightarrow \frac {b _ {0} ^ {2}}{2 \ell} (d - c), \quad \text {当} n \rightarrow \infty . \\ \end{array}
$$

由此可见存在 $\delta_0 > 0$ 使得

$$\| \mathcal {B} y _ {n} \| \geqslant \delta_ {0}, \quad \forall n = \pm 1, \pm 2, \dots .$$

于是根据定理 10.4.3, 阻尼弦振动系统指数稳定. 再根据定理 10.4.1, 相应的局部分布控制系统

$$
\left\{ \begin{array}{l} \ddot {y} (x, t) - y ^ {\prime \prime} (x, t) + b (x) u (x, t) = 0, \\ y (0, t) = 0, \quad y ^ {\prime} (\ell , t) = 0, \end{array} \right.
$$

则是精确能控的.

例10.4.2 一维Euler-Bernoulli梁振动系统

$$
\left\{ \begin{array}{l} \ddot {y} (x, t) + y ^ {\prime \prime \prime \prime} (x, t) + b (x) \dot {y} (x, t) = 0, \\ y (0, t) = 0 = y (\ell , t), y ^ {\prime \prime} (0, t) = 0 = y ^ {\prime \prime} (\ell , t), \end{array} \right. \tag {10.4.18}
$$

其中 $\ell$ 为梁的长度，阻尼函数 $b(x)$ 的假设与上例相同．取状态Hilbert空间 $\mathcal{H}$ 为

$$\mathcal {H} = \left\{\left[ \varphi , \psi \right] ^ {\mathrm{T}} \mid \varphi \in H ^ {2} (0, \ell), \psi \in L ^ {2} (0, \ell), \varphi (0) = 0, \varphi (\ell) = 0 \right\},$$

内积为

$$\langle [ \varphi_ {1}, \psi_ {1} ] ^ {\mathrm{T}}, [ \varphi_ {2}, \psi_ {2} ] ^ {\mathrm{T}} \rangle = \int_ {0} ^ {\ell} \varphi_ {1} ^ {\prime \prime} \overline {{{{\varphi}}}} _ {2} ^ {\prime \prime} \mathrm{d} x + \int_ {0} ^ {\ell} \psi_ {1} \overline {{{{\psi}}}} _ {2} \mathrm{d} x.$$

定义 $\mathcal{H}$ 中线性算子 $\pmb{A}$ 和 $\pmb{B}$ 为

$$\mathcal {A} [ \varphi , \psi ] ^ {\mathrm{T}} = [ \psi , - \varphi^ {\prime \prime \prime \prime} ] ^ {\mathrm{T}}, \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {D} (\mathcal {A}),\mathcal {D} (\mathcal {A}) = \left\{\left[ \varphi , \psi \right] ^ {\mathrm{T}} \in \mathcal {H} \mid \varphi \in H ^ {4} (0, \ell), \psi \in H ^ {2} (0, \ell), \right.\varphi (0) = \varphi (\ell) = 0. \psi (0) = \psi (\ell) = 0, \varphi^ {\prime \prime} (0) = 0, \varphi^ {\prime \prime} (\ell) = 0 \},\mathcal {B} [ \varphi , \psi ] ^ {\mathrm{T}} = [ 0, - b \psi ] ^ {\mathrm{T}}, \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {H}.$$
