$$
\begin{array}{l} 2 \int_ {\alpha} ^ {\beta} \rho q \omega_ {n} ^ {2} | w _ {n} | ^ {2} \mathrm{d} x + 2 \int_ {\alpha} ^ {\beta} (I _ {\rho} \omega_ {n} ^ {2} - K) q | \varphi_ {n} | ^ {2} \mathrm{d} x \\ = - K q w _ {n} ^ {\prime} \bar {w} _ {n} \left| _ {\alpha} ^ {\beta} - E I q \varphi_ {n} ^ {\prime} \bar {\varphi} _ {n} \right| _ {\alpha} ^ {\beta} + \int_ {\alpha} ^ {\beta} (I _ {n} (x) + J _ {n} (x)) d x \\ + (\beta - \alpha) (K (0) | w _ {n} ^ {\prime} (0) | ^ {2} + E I (0) | \varphi_ {n} ^ {\prime} (0) | ^ {2}) + P _ {n} + Q _ {n}. \tag {10.4.47} \\ \end{array}
$$

通过分部积分，并利用 Cauchy 不等式，对于任意 $\varepsilon > 0$ ，我们有

$$
\begin{array}{l} \left| \int_ {0} ^ {x} \mathrm{i} \omega_ {n} \widetilde {w} _ {n} \rho q \overline {{w}} _ {n} ^ {\prime} \mathrm{d} s \right| \leqslant | \mathrm{i} \omega_ {n} \widetilde {w} _ {n} (x) \rho (x) q (x) \overline {{w}} _ {n} (x) | \\ + \left| \int_ {0} ^ {x} \mathrm{i} \omega_ {n} \rho q \widetilde {w} _ {n} ^ {\prime} \overline {{w}} _ {n} \mathrm{d} s \right| + \left| \int_ {0} ^ {x} \mathrm{i} \omega_ {n} (\rho q) ^ {\prime} \widetilde {w} _ {n} \overline {{w}} _ {n} \mathrm{d} s \right| \\ \leqslant \varepsilon | \omega_ {n} w _ {n} (x) | ^ {2} + C _ {\varepsilon} | \tilde {w} _ {n} (x) | ^ {2} + C \| \omega_ {n} w _ {n} \| _ {L ^ {2}} \| \tilde {w} _ {n} \| _ {H ^ {1}}. \tag {10.4.48} \\ \end{array}
$$

这里及下面， $C_{\varepsilon}$ 表示仅依赖于 $\varepsilon$ 的常数。此外，依据Sobolev嵌入定理，存在常数 $C$ 使得

$$\left| \tilde {w} _ {n} (x) \right| \leqslant C \| \tilde {w} _ {n} \| _ {H ^ {1}}, \quad \forall x \in [ 0, \ell ]. \tag {10.4.49}$$

由此我们得到

$$\left| \int_ {0} ^ {x} \mathrm{i} \omega_ {n} \widetilde {w} _ {n} \rho q \overline {{{w}}} _ {n} ^ {\prime} \mathrm{d} s \right| \leqslant \varepsilon | \omega_ {n} w _ {n} (x) | ^ {2} + C _ {\varepsilon}. \tag {10.4.50}$$

综合式 (10.4.37), (10.4.38) 和式 (10.4.50), 可得到

$$\left| \int_ {0} ^ {x} f _ {n} \rho q \overline {{w}} _ {n} ^ {\prime} \mathrm{d} s \right| \leqslant \varepsilon | \omega_ {n} w _ {n} (x) | ^ {2} + C _ {\varepsilon}. \tag {10.4.51}$$

类似地，我们可得到

$$\left| \int_ {0} ^ {x} g _ {n} I _ {\rho} q \overline {{{\varphi}}} _ {n} ^ {\prime} \mathrm{d} s \right| \leqslant \varepsilon | \omega_ {n} \varphi_ {n} (x) | ^ {2} + C _ {\varepsilon}. \tag {10.4.52}$$

于是利用式 (10.4.40), (10.4.41), (10.4.51) 和式 (10.4.52), 得到

$$J _ {n} (x) \leqslant 2 \varepsilon \left(\left| \omega_ {n} w _ {n} (x) \right| ^ {2} + \left| \omega_ {n} \varphi_ {n} (x) \right| ^ {2}\right) + C _ {\varepsilon}. \tag {10.4.53}$$
