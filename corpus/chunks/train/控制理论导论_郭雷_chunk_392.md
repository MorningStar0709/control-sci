$$
\begin{array}{l} \left\| R (\lambda ; A) x \right\| \leqslant | \tau | ^ {- 1} \mathrm{e} ^ {- \sigma t _ {1}} \left[ \mu (t _ {1}) \| R (\lambda ; A) x \| + \| T (t _ {1}) \| \| x \| \right] \\ + \left\| \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- \lambda s} T (s) x \mathrm{d} s \right\|. \\ \end{array}
$$

但当 $\lambda \in \Sigma$ 时， $|\tau|^{-1}\mathrm{e}^{-\sigma t_1}\mu(t_1) \leqslant (1 + \delta)^{-1}$ . 另一方面，若 $\sigma \leqslant \omega$ ，则 $|\tau|^{-1} \leqslant \mu(t_1)^{-1}(1 + \delta)^{-1}\mathrm{e}^{\omega t_1}$ . 从而

$$
\begin{array}{l} \| R (\lambda ; A) x \| \leqslant \frac {1 + \delta}{\delta} \left(| \tau | ^ {- 1} e ^ {(\omega - \sigma) t _ {1}} M \| x \| + \left\| \int_ {0} ^ {t _ {1}} e ^ {- \lambda s} T (s) x d s \right\|\right) \\ \leqslant M \delta^ {- 1} \mu (t _ {1}) ^ {- 1} \left(t _ {1} + \mu (t _ {1}) ^ {- 1} (1 + \delta) ^ {- 1} e ^ {\omega t _ {1}}\right) e ^ {\omega t _ {1}} | \tau | \| x \| \\ = C | \tau | \| x \|. \\ \end{array}
$$

这表明 $\| R(\lambda; A) \| \leqslant C|\operatorname{Im} \lambda|$ , $\forall \lambda \in \Sigma$ , $\operatorname{Re} \lambda \leqslant \omega$ , 即式 (5.3.42) 成立. 证毕.

定理5.3.19 设 $T(t)$ 是Banach空间 $X$ 中由 $A$ 生成的 $C_0$ 半群，满足 $\| T(t)\| \leqslant Me^{\omega t}, t\geqslant 0$ 如果存在常数 $a\in \mathbb{R},b > 0$ 和 $C > 0$ 使得式(5.3.41）和式(5.3.42）成立，则 $T(t)$ 对于 $t > 3 / b$ 可微，并且当 $t > 2 / b$ 时有

$$T (t) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} \mathrm{e} ^ {\lambda t} R (\lambda ; A) \mathrm{d} \lambda .$$

这里积分路径 $\Gamma$ 位于 $\Sigma$ 中，由三部分组成： $\Gamma = \Gamma_{1} \cup \Gamma_{2} \cup \Gamma_{3}$ ，其中

$$\Gamma_ {1} = \left\{\lambda \in \mathbb {C} \mid \operatorname{Re} \lambda = 2 a - b \log (- \operatorname{Im} \lambda), - \infty < \operatorname{Im} \lambda < - L \right\},\Gamma_ {2} = \left\{\lambda \in \mathbb {C} \mid \lambda = \omega + L e ^ {i \theta}, \theta \in [ - \pi / 2, \pi / 2 ] \right\},\Gamma_ {3} = \left\{\lambda \in \mathbb {C} \mid \operatorname{Re} \lambda = 2 a - b \log (\operatorname{Im} \lambda), L < \operatorname{Im} \lambda < \infty \right\},$$

$L = \mathrm{e}^{(2a - \omega ') / b},\omega ' > \omega$ 为某个固定常数，而 $\Gamma$ 的定向使得 $\operatorname {Im}\lambda$ 沿着 $\Gamma$ 是增加的.

证明 令

$$S _ {j} (t) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {j}} \mathrm{e} ^ {\lambda t} R (\lambda ; A) \mathrm{d} \lambda , \quad j = 1, 2, 3, \tag {5.3.43}$$

以及 $S(t) = S_{1}(t) + S_{2}(t) + S_{3}(t)$ . 于是

$$S (t) = \frac {1}{2 \pi \mathbf {i}} \int_ {\Gamma} \mathrm{e} ^ {\lambda t} R (\lambda ; A) \mathrm{d} \lambda .$$
