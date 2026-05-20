# C. 10 证明定理 5.4

我们通过证明 $\mathcal{L}_2$ 增益等于 $\sup_{\omega \in R}\| G(j\omega)\|_2$ 完成定理5.4的证明。设 $c_{1}$ 是 $\mathcal{L}_2$ 增益， $c_{2} = \sup_{\omega \in R}\| G(j\omega)\|_2$ ，我们知道 $c_{1} \leqslant c_{2}$ 。假设 $c_{1} < c_{2}$ ，并设定 $\varepsilon = (c_{2} - c_{1}) / 3$ ，则对于任意 $u \in \mathcal{L}_2$ ，当 $\|\mu\|_{\mathcal{L}_2} \leqslant 1$ 时，有 $\|y\|_{\mathcal{L}_2} \leqslant c_2 - 3\varepsilon$ 。我们要通过找一个信号 $u$ ，满足 $\|u\|_{\mathcal{L}_2} \leqslant 1$ ，使 $\|y\|_{\mathcal{L}_2} \geqslant c_2 - 2\varepsilon$ 成立，即与上式矛盾。如果在整个实数轴 $R$ 上定义信号，则容易构造这样的信号。这样做不失一般性，由于（见习题5.19）无论信号定义在 $[0, \infty)$ 上还是定义在 $R$ 上， $\mathcal{L}_2$ 增益都是一样的。现在选择 $\omega_0 \in R$ ，使 $\|G(j\omega_0)\|_2 \geqslant c_2 - \varepsilon$ 。设 $v \in C^m$ 是归一化向量 $(v^* v = 1)$ ，对应于埃尔米特矩阵 $G^{\mathrm{T}}(-j\omega_0)G(j\omega_0)$ 的最大特征值，因此 $v^* G^{\mathrm{T}}(-j\omega_0)G(j\omega_0)v = \|G(j\omega_0)\|_2^2$ 。把 $v$ 表示为

$$v = \left[ \alpha_ {1} e ^ {j \theta_ {1}}, \alpha_ {2} e ^ {j \theta_ {2}}, \dots , \alpha_ {m} e ^ {j \theta_ {m}} \right] ^ {\mathrm{T}}$$

其中 $\alpha_{i} \in R$ ，使 $\theta_{i} \in (-\pi, 0]$ 。取 $0 \leqslant \beta_{i} \leqslant \infty$ ，使 $\theta_{i} = -2\arctan (\omega_{0} / \beta_{i})$ ，如果 $\theta_{i} = 0$ ，则 $\beta_{i} = \infty$ 。定义 $m \times 1$ 传递函数矩阵 $H(s)$ 为

$$H (s) = \left[ \alpha_ {1} \frac {\beta_ {1} - s}{\beta_ {1} + s}, \alpha_ {2} \frac {\beta_ {2} - s}{\beta_ {2} + s}, \dots , \alpha_ {m} \frac {\beta_ {m} - s}{\beta_ {m} + s} \right] ^ {\mathrm{T}}$$

如果 $\theta_{i} = 0$ ，则用1代替 $(\beta_{i} - s) / (\beta_{i} + s)$ 。容易看出，对于所有 $\omega \in R$ ，有 $H(j\omega_0) = v$ 和 $H^{\mathrm{T}}(-j\omega)H(j\omega) = \sum_{i = 1}^{m}\alpha_{i}^{2} = v^{*}v = 1$ ，取 $u_{\sigma}(t)$ 作为 $H(s)$ 的输出， $H(s)$ 由标量函数

$$z _ {\sigma} (t) = \left(\frac {1}{1 + e ^ {- \omega_ {0} ^ {2} \sigma / 2}}\right) ^ {1 / 2} \left(\frac {8}{\pi \sigma}\right) ^ {1 / 4} e ^ {- t ^ {2} / \sigma} \cos (\omega_ {0} t), \quad \sigma > 0, \quad t \in R$$

驱动。可以验证 $z_{\sigma} \in \mathcal{L}_2$ 和 $\| z_{\sigma}\|_{\mathcal{L}_2} = 1^{\text{①}}$ ，因而有 $u_{\sigma} \in \mathcal{L}_2$ 和 $\| u_{\sigma}\|_{\mathcal{L}_2} \leqslant 1, z_{\sigma}(t)$ 的傅里叶变换为

$$Z _ {\sigma} (j \omega) = \left(\frac {1}{1 + e ^ {- \omega_ {0} ^ {2} \sigma / 2}}\right) ^ {1 / 2} \left(\frac {\pi \sigma}{2}\right) ^ {1 / 4} \left[ e ^ {- (\omega - \omega_ {0}) ^ {2} \sigma / 4} + e ^ {- (\omega + \omega_ {0}) ^ {2} \sigma / 4} \right]$$
