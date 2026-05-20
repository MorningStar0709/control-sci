定义乘积 Hilbert 空间 $\mathcal{H} = D\left(A^{1/2}\right) \times H$ , 其中内积为

$$\langle w, \widetilde {w} \rangle_ {\mathcal {H}} = \langle A ^ {1 / 2} y, A ^ {1 / 2} \widetilde {y} \rangle_ {H} + \langle z, \widetilde {z} \rangle_ {H},$$

式中 $w = [y,z]^{\mathrm{T}},\tilde{w} = [\tilde{y},\tilde{z}]^{\mathrm{T}}$ .我们有

$$
\begin{array}{l} \langle \mathcal {A} w, w \rangle_ {\mathcal {H}} = \langle A y, z \rangle + \langle z, - A y - \bar {\alpha} z \rangle \\ = - \alpha \| z \| ^ {2}, \quad \forall w \in \mathcal {D} (\mathcal {A}) = \mathcal {D} (A) \times D \left(A ^ {1 / 2}\right). \\ \end{array}
$$

容易看出， $\mathcal{A}$ 在 $\mathcal{H}$ 中的伴随是

$$
\mathcal {A} ^ {*} \left[ \begin{array}{l} y \\ z \end{array} \right] = \left[ \begin{array}{c c} 0 & I \\ - A & - \alpha \end{array} \right] \left[ \begin{array}{l} y \\ z \end{array} \right], \qquad \mathcal {D} (\mathcal {A} ^ {*}) = \mathcal {D} (\mathcal {A}).
$$

因此

$$\langle \mathcal {A} ^ {*} w, w \rangle_ {\mathcal {H}} = - \alpha \| z \| ^ {2}, \quad \forall w \in \mathcal {D} (\mathcal {A} ^ {*}),$$

从而 A 生成 H 中某个 $C_{0}$ 半群 $T(t)$ .

进而我们假定 $A$ 有紧豫解式，故

$$\sigma (A) = \sigma_ {p} (A) = \left\{\lambda_ {n} \mid n \geqslant 1 \right\},$$

其中 $\lambda_{n} \to \infty (n \to \infty)$ . 为简单起见, 我们假定每个 $\lambda_{n}$ 都是单的. 于是 $A$ 的相应的规格化本征元序列 $\{\varphi_{n} \mid n \geqslant 1\}$ 构成 $H$ 的规范直交基. 现在我们给出 $\alpha = 0$ 时 $A$ 所生成的 $C_{0}$ 半群 $T(t)$ 的表达式.

不难验证 $\mathcal{A}$ 也有紧豫解式，并且

$$\sigma (\mathcal {A}) = \left\{\mu_ {n} \mid n = \pm 1, \pm 2, \dots \right\},$$

其中

$$
\mu_ {n} = \left\{ \begin{array}{l l} \mathrm{i} \sqrt {\lambda_ {n}}, & \quad \forall n \geqslant 1, \\ - \mathrm{i} \sqrt {\lambda_ {n}}, & \quad \forall n \leqslant - 1, \end{array} \right.
$$

$\mathbf{i} = \sqrt{-1}$ , 而当 $n \leqslant -1$ 时 $\lambda_{n} = \lambda_{-n}$ . 设 $\psi_{n}$ 是 $\mathcal{A}$ 的对应于 $\mu_{n}$ 的本征元, 则

$$\psi_ {n} = \left[ \varphi_ {n}, \mu_ {n} \varphi_ {n} \right] ^ {\mathrm{T}},$$

从而通过计算，我们得到

$$T (t) w = \sum_ {| n | = 1} ^ {\infty} \frac {1}{2 \lambda_ {n}} \mathrm{e} ^ {\mu_ {n} t} \langle w, \psi_ {n} \rangle \psi_ {n},$$

这里对于 $n \geqslant 1$ , 定义 $\psi_{-n} = \psi_n$ . 最后展开上式便得到

$$
T (t) w = \left[ \begin{array}{l} \sum_ {n = 1} ^ {\infty} \left[ \langle y, \varphi_ {n} \rangle_ {H} \cos \sqrt {\lambda_ {n}} t + \frac {1}{\sqrt {\lambda_ {n}}} \langle z, \varphi_ {n} \rangle_ {H} \sin \sqrt {\lambda_ {n}} t \right] \varphi_ {n} \\ \sum_ {n = 1} ^ {\infty} \left[ - \sqrt {\lambda_ {n}} \langle y, \varphi_ {n} \rangle_ {H} \sin \sqrt {\lambda_ {n}} t + \langle z, \varphi_ {n} \rangle_ {H} \cos \sqrt {\lambda_ {n}} t \right] \varphi_ {n} \end{array} \right],
$$

这里 $w = [y,z]^{\mathrm{T}}\in \mathcal{H}.$
