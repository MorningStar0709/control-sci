$$\| R (\lambda ; A) \| \leqslant \int_ {0} ^ {\infty} \exp \Big (- t \operatorname{Re} \left(\lambda \mathrm{e} ^ {- 3 \mathrm{i} \delta / 4}\right) \Big) M _ {3} \mathrm{d} t, \quad \forall \lambda \in \Sigma_ {\pi / 2 + \delta / 2} (0), \operatorname{Re} \lambda \geqslant 0.$$

注意到 $\lambda = |\lambda|\mathrm{e}^{\mathrm{i}\varphi}\in \Sigma_{\pi /2 + \delta /2}(0),\mathrm{Im}\lambda \geqslant 0,$ 我们有

$$- 3 \delta / 4 < \varphi - 3 \delta / 4 < \pi / 2 - \delta / 4,$$

这表明

$$\operatorname{Re} \left(\lambda \mathrm{e} ^ {- 3 \mathrm{i} \delta / 4}\right) = | \lambda | \cos (\varphi - 3 \delta / 4) \geqslant | \lambda | \mu_ {0},$$

其中 $\mu_0 = \min \{\cos (3\delta /4),\sin (\delta /4)\}$ .因此

$$\| R (\lambda ; A) \| \leqslant \frac {M _ {3}}{\mu_ {0} | \lambda |}, \quad \forall \lambda \in \Sigma_ {\pi / 2 + \delta / 2} (0), \operatorname{Im} \lambda \geqslant 0. \tag {5.3.51}$$

对于 $\operatorname{Im} \lambda < 0$ 在直线 $\{te^{-3i\delta/4} \mid t \geqslant 0\}$ 上重复上述论证，同样的不等式 (5.3.51) 成立，从而 (1) 也成立。证毕。

例5.3.13 设 $A$ 是Hlbert空间 $H$ 上的自伴算子．假定存在 $\omega \in \mathbb{R}$ 使得

$$(A x, x) \leqslant \omega \| x \| ^ {2}, \quad \forall x \in \mathcal {D} (A). \tag {5.3.52}$$

根据Lummer-Phillips定理， $A$ 是 $H$ 上 $C_0$ 半群 $T(t)$ 的生成算子，并且

$$\| T (t) \| \leqslant \mathrm{e} ^ {\omega t}, \quad \forall t \geqslant 0.$$

现在我们证明由 $A$ 生成的 $C_0$ 半群 $T(t)$ 是解析的。事实上，由于 $\sigma(A) \subset (-\infty, \omega]$ ，对于每一 $\lambda \in \mathbb{C} \setminus (-\infty, \omega]$ 和 $y \in H$ ，存在 $x \in \mathcal{D}(A)$ 使得

$$\lambda x - A x = y.$$

令 $\lambda = \omega +\rho e^{i\theta}$ ，我们把上式重新写成

$$\rho \mathrm{e} ^ {\mathrm{i} \theta} x - (A - \omega) x = y.$$

然后用 $\mathrm{e}^{-\mathrm{i}\theta /2x}$ 分别与两端作内积，并取实部，得到

$$\rho \cos (\theta / 2) \| x \| ^ {2} - \cos (\theta / 2) ((A - \omega I) x, x) = \operatorname{Re} \left(\mathrm{e} ^ {- \mathrm{i} \theta / 2} (x, y)\right).$$

利用式(5.3.52)，从上式我们得到 $\| x\| \leqslant (\rho \cos (\theta /2))^{-1}\| y\|$ ，从而

$$\| R (\lambda ; A) \| \leqslant \frac {1}{| \lambda - \omega | \cos (\theta / 2)}.$$

今取 $\theta_0$ 满足 $\pi / 2 < \theta_0 < \pi$ . 显然当 $0 \leqslant \theta < \theta_0$ 时, 我们有 $\cos(\theta / 2) > \cos(\theta_0 / 2)$ . 因此

$$\| R (\lambda ; A) \| \leqslant \frac {1}{| \lambda - \omega | \cos (\theta_ {0} / 2)}, \quad \forall \lambda \in \Sigma_ {\theta_ {0}}.$$

由此根据定理 5.3.21. 可知 $T(t)$ 是解析的.
