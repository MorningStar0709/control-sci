$$- \omega_ {n} ^ {2} w _ {n} + \rho^ {- 1} (K (\varphi_ {n} - w _ {n} ^ {\prime})) ^ {\prime} = f _ {n} \stackrel {\text { def }} {=} \widetilde {z} _ {n} - b _ {1} z _ {n} + \mathrm{i} \omega_ {n} \widetilde {w} _ {n}, \tag {10.4.32}- \omega_ {n} ^ {2} \varphi_ {n} - I _ {\rho} ^ {- 1} (E I \varphi_ {n} ^ {\prime}) ^ {\prime} + I _ {\rho} ^ {- 1} K (\varphi_ {n} - w _ {n} ^ {\prime}) = g _ {n} \stackrel {\text { def }} {=} \widetilde {\psi} _ {n} - b _ {2} \psi_ {n} + \mathrm{i} \omega_ {n} \widetilde {\varphi} _ {n}. \tag {10.4.33}$$

任取 $q \in C^{1}[0.\ell]$ 满足 $q(0) = 1$ . 今用 $\rho q\overline{w}_{n}^{\prime}$ 和 $I_{\rho}q\overline{\varphi}_{n}^{\prime}$ 分别乘式 (10.4.32) 和式 (10.4.33), 从 0 到 $x$ 积分, 再取实部并相加, 得到

$$
\begin{array}{l} K q \left| w _ {n} ^ {\prime} \right| ^ {2} (x) + E I q \left| \varphi_ {n} ^ {\prime} \right| ^ {2} (x) + \rho q \omega_ {n} ^ {2} \left| w _ {n} \right| ^ {2} (x) + \left(I _ {\rho} \omega_ {n} ^ {2} - K\right) q \left| \varphi_ {n} \right| ^ {2} (x) \\ = K (0) \left| w _ {n} ^ {\prime} (0) \right| ^ {2} + E I (0) \left| \varphi_ {n} ^ {\prime} (0) \right| ^ {2} + I _ {n} (x) + J _ {n} (x), \tag {10.4.34} \\ \end{array}
$$

其中

$$
\begin{array}{l} I _ {n} (x) = \omega_ {n} ^ {2} \int_ {0} ^ {x} (\rho q) ^ {\prime} | w _ {n} | ^ {2} \mathrm{d} s + \int_ {0} ^ {x} ((I _ {\rho} \omega_ {n} ^ {2} - K) q) ^ {\prime} | \varphi_ {n} | ^ {2} \mathrm{d} s \\ + \int_ {0} ^ {x} (K q ^ {\prime} - K ^ {\prime} q) | w _ {n} ^ {\prime} | ^ {2} \mathrm{d} s + \int_ {0} ^ {x} (E I q ^ {\prime} - E I ^ {\prime} q) | \varphi_ {n} ^ {\prime} | ^ {2} \mathrm{d} s, \\ \end{array}
J _ {n} (x) = 2 \operatorname{Re} \left[ \int_ {0} ^ {x} K ^ {\prime} q \varphi_ {n} \overline {{w}} _ {n} ^ {\prime} \mathrm{d} s - \int_ {0} ^ {x} f _ {n} \rho q \overline {{w}} _ {n} ^ {\prime} \mathrm{d} s - \int_ {0} ^ {x} g _ {n} I _ {\rho} q \overline {{\varphi}} _ {n} ^ {\prime} \mathrm{d} s \right].
$$

任取 $[\alpha, \beta] \subset [0, \ell]$ , 对式 (10.4.34) 从 $\alpha$ 到 $\beta$ 积分, 我们得到

$$
\begin{array}{l} \int_ {\alpha} ^ {\beta} \left(K q | w _ {n} ^ {\prime} | ^ {2} + E J q | \varphi_ {n} ^ {\prime} | ^ {2} + \rho q \omega_ {n} ^ {2} | w _ {n} | ^ {2} + (I _ {\rho} \omega_ {n} ^ {2} - K) q | \varphi_ {n} | ^ {2}\right) d s \\ = (\beta - \alpha) \left(K (0) \left| w _ {n} ^ {\prime} (0) \right| ^ {2} + E I (0) \left| \varphi_ {n} ^ {\prime} (0) \right| ^ {2}\right) \\ + \int_ {\alpha} ^ {\beta} (I _ {n} (x) + J _ {n} (x)) \mathrm{d} x. \tag {10.4.35} \\ \end{array}
$$

通过分部积分并利用 Cauchy 不等式，可以得到如下估计式：
