$$- \operatorname{Re} \langle \mathcal {B} y, y \rangle \geqslant c \| \mathcal {B} y \| ^ {2}, \quad \forall y \in \mathcal {H}, \tag {10.4.16}$$

其中 $c > 0$ 是某个常数. 易见当条件 (10.4.16) 满足时, 有关 $\pmb{\beta}$ 的假设 (H2) 成立.

例10.4.1 一维弦振动系统

$$
\left\{ \begin{array}{l} \ddot {y} (x, t) - y ^ {\prime \prime} (x, t) + b (x) \dot {y} (x, t) = 0, \\ y (0, t) = 0, \quad y ^ {\prime} (\ell , t) = 0, \end{array} \right. \tag {10.4.17}
$$

其中 $\ell$ 为弦的长度，字母上方的点表示对时间变量 $t$ 的导数，而字母右上方的撇则表示对空间变量 $x$ 的导数。假定 $b(\cdot)$ 在 $[0, \ell]$ 上非负有界连续，并且存在一子区间 $J \subset (0, \ell)$ 和一常数 $b_0 > 0$ 使得 $b(x) \geqslant b_0, \forall x \in J$ 。取状态 Hilbert 空间 $\mathcal{H}$ 为

$$\mathcal {H} = \left\{\left[ \varphi , \psi \right] ^ {\mathrm{T}} \mid \varphi \in H ^ {1} (0, \ell), \psi \in L ^ {2} (0, \ell) \right\},$$

$\mathcal{H}$ 中内积为

$$\langle [ \varphi_ {1}, \psi_ {1} ] ^ {\mathrm{T}}, [ \varphi_ {2}, \psi_ {2} ] ^ {\mathrm{T}} \rangle = \int_ {0} ^ {\ell} \varphi_ {1} ^ {\prime} \varphi_ {2} ^ {\prime} \mathrm{d} x + \int_ {0} ^ {\ell} \psi_ {1} \psi_ {2} \mathrm{d} x.$$

定义 $\mathcal{H}$ 中线性算子 $\pmb{A}$ 和 $\pmb{B}$ 为

$$\mathcal {A} [ \varphi , \psi ] ^ {\mathrm{T}} = [ \psi , \varphi^ {\prime \prime} ] ^ {\mathrm{T}}, \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {D} (\mathcal {A}),\mathcal {D} (\mathcal {A}) = \left\{\left[ \varphi , \psi \right] ^ {\mathrm{T}} \in \mathcal {H} \mid \varphi \in H ^ {2} (0, \ell), \psi \in H ^ {1} (0, \ell), \right.\varphi (0) = 0, \varphi^ {\prime} (\ell) = 0, \psi (0) = 0 \},\boldsymbol {\mathcal {B}} [ \varphi , \psi ] ^ {\mathrm{T}} = [ 0, - b \psi ] ^ {\mathrm{T}}, \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {H}.$$

不难看出 $\mathcal{A}$ 是 $\mathcal{H}$ 中具有紧豫解式的斜自伴算子，满足定理10.4.3的假设。 $\pmb{B}$ 显然是耗散的。 $\mathcal{A}$ 的本征值序列为

$$\mathrm{i} \omega_ {n} = \mathrm{i} \frac {n + \frac {1}{2}}{\ell} \pi , \quad n = \pm 1, \pm 2, \dots .$$

易见谱间隙条件满足

$$\left| \mathrm{i} \frac {n + \frac {1}{2}}{\ell} \pi - \mathrm{i} \frac {n + 1 + \frac {1}{2}}{\ell} \pi \right| = \frac {\pi}{\ell} \stackrel {\text { def }} {=} \gamma > 0.$$

$\pmb{A}$ 的相应的规范本征元是

$$
y _ {n} = \frac {\sqrt {\ell}}{\left(n + \frac {1}{2}\right) \pi} \left[ \begin{array}{c} \sin \frac {\left(n + \frac {1}{2}\right) \pi}{\ell} x \\ \mathrm{i} \frac {\left(n + \frac {1}{2}\right) \pi}{\ell} \sin \frac {\left(n + \frac {1}{2}\right) \pi}{\ell} \end{array} \right], \qquad n = \pm 1, \pm 2, \dots .
$$
