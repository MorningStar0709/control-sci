定义的线性算子 $\psi_y: H \to L^p(\mathbb{R}_+)$ 也是有界的。于是对任意 $x \in H$ ，成立

$$\| \psi_ {y} (x) \| _ {L ^ {p}} = \| \varphi_ {x} (y) \| _ {L ^ {p}} \leqslant M _ {x} \| y \|, \quad \forall y \in H.$$

由此根据线性算子的一致有界性原理，存在正常数 $M$ 使得

$$\| \psi_ {y} (x) \| _ {L ^ {p}} \leqslant M \| x \|, \quad \forall \| y \| \leqslant 1,$$

从而

$$\left(\int_ {0} ^ {\infty} | \langle T (t) x, y \rangle | ^ {p} \mathrm{d} t\right) ^ {\frac {1}{p}} \leqslant M \| x \| \| y \|, \quad \forall x, y \in H. \tag {10.1.14}$$

对于任意 $\lambda \in \mathbb{C}$ , $\operatorname{Re} \lambda > 0$ , 今定义线性算子 $R(\lambda): H \to H$ ,

$$\langle R (\lambda) x, y \rangle = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} \langle T (t) x, y \rangle \mathrm{d} t, \quad \forall x, y \in H.$$

从式 (10.1.14) 和熟知的 Hölder 不等式得到

$$
| \langle R (\lambda) x, y \rangle | \leqslant \left\{ \begin{array}{l l} {M (q \mathrm{Re}   \lambda) ^ {- \frac {1}{q}} \| x \|   \| y \|,} & {\quad \text {如果} p > 1,} \\ {M \| x \|   \| y \|,} & {\quad \text {如果} p = 1,} \end{array} \right.
$$

其中 $\frac{1}{p} +\frac{1}{q} = 1$ ，由此 $R(\lambda)\in \mathcal{L}(H)$ ，并且

$$
\| R (\lambda) \| \leqslant \left\{ \begin{array}{l l} {M (q \mathrm{Re}   \lambda) ^ {- \frac {1}{q}},} & {\text {如果} p > 1,} \\ {M,} & {\text {如果} p = 1.} \end{array} \right. \tag {10.1.15}
$$

此外 $R(\lambda)$ 在半平面 $\{\lambda \in \mathbb{C} \mid \operatorname{Re}\lambda > 0\}$ 中是解析的。另一方面，对于 $\lambda \in \mathbb{C}$ ， $\operatorname{Re}\lambda > \omega(A)$ ，我们有

$$R (\lambda ; A) x = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) x \mathrm{d} t, \quad \forall x \in H.$$

由此从解析延拓的唯一性得到

$$R (\lambda ; A) = R (\lambda), \quad \forall \operatorname{Re} \lambda > 0.$$

当 $p > 1$ 时，令 $\sigma_0 = M^{-p} / q$ ，则从不等式(10.1.15)得到

$$\| R (\lambda ; A) \| \leqslant M M ^ {\frac {p}{q}} = M ^ {p}, \quad \forall \operatorname{Re} \lambda \geqslant \sigma_ {0}. \tag {10.1.16}$$

对于 $\lambda = \sigma +\mathrm{i}\tau ,\sigma \in [0,\sigma_0)$ 和 $\tau \in \mathbb{R},$ 我们有

$$\left\| \left(\sigma - \sigma_ {0}\right) R \left(\sigma_ {0} + \mathrm{i} \tau ; A\right) \right\| \leqslant M M ^ {p / q} M ^ {- p} / q = 1 / q.$$

因此 $I - (\sigma_0 - \sigma)R(\sigma_0 + \mathrm{i}\tau;A)$ 有有界逆，并且

$$\left\| \left[ I - (\sigma_ {0} - \sigma) R (\sigma_ {0} + \mathrm{i} \tau ; A)) \right] ^ {- 1} \right\| \leqslant q / (q - 1).$$

这表明当 $0 \leqslant \operatorname{Re} \lambda < \sigma_0$ 时 $\lambda = \sigma + \mathrm{i}\tau \in \rho(A)$ , 并且
