图5.3.1 积分路径 $\Gamma_{\varepsilon, \theta} = \Gamma_{\varepsilon, \theta}^{1} \cup \Gamma_{\varepsilon, \theta}^{2} \cup \Gamma_{\varepsilon, \theta}^{3}$

定理 5.3.20 设 A 是 Banach 空间 X 中的闭稠定线性算子，并满足假设 (H). 假定 $T(t)$ 由式 (5.3.47) 定义，那么

(1) 存在常数 $M_{1} > 0$ 和 $M_{2} > 0$ 使得

$$\| T (t) \| \leqslant M _ {1} \mathrm{e} ^ {\omega t}, \quad \forall t \geqslant 0, \tag {5.3.48}\left\| (A - \omega I) T (t) \right\| \leqslant \frac {M _ {2}}{t} \mathrm{e} ^ {\omega t}, \quad \forall t > 0, \tag {5.3.49}$$

并且 $T(t)$ 是可微的， $T'(t) = AT'(t), \forall t > 0;$

(2) $T(t)$ 是由 $A$ 生成的 $C_0$ 半群；

(3) $T(t)$ 可以在扇形区域 $\Sigma_{\delta_0}$ 中开拓成一解析半群 $T(z)$

$$
\left\{ \begin{array}{l} T (z) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\epsilon , \theta}} \mathrm{e} ^ {\lambda z} R (\lambda ; A) \mathrm{d} \lambda , \qquad z \in \Sigma_ {\delta_ {0}}, \\ z = r \mathrm{e} ^ {\mathrm{i} \varphi}, \qquad | \varphi | <   \delta_ {0}, \theta = \pi / 2 + \delta , 0 <   \delta <   \delta_ {0}. \end{array} \right.
$$

证明 不失一般性，我们可以假设 $\omega = 0$ ，否则的话，我们可以把 $A$ 平移为 $A - \omega I$ ，而 $T(t)$ 改成 $\mathrm{e}^{-\omega t}T(t)$

(1) 从式 (5.3.47) 可知， $T(t)$ 相对 $t$ 在 $\Sigma_{\delta_0 + \pi/2}$ 中无限次可微，并且对于 $t > 0$ ，由于 $\int_{\Gamma_{\epsilon,\theta}} e^{\lambda t} \mathrm{d}\lambda = 0$ ，我们有

$$
\begin{array}{l} T ^ {\prime} (t) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\varepsilon , \theta}} \mathrm{e} ^ {\lambda t} \lambda R (\lambda ; A) \mathrm{d} \lambda \\ = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\epsilon , \theta}} \mathrm{e} ^ {\lambda t} I \mathrm{d} \lambda + \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\epsilon , \theta}} A \mathrm{e} ^ {\lambda t} R (\lambda ; A) \mathrm{d} \lambda \\ = A T (t). \\ \end{array}
$$

对于 $t > 0$ ，通过替换 $\mu = \lambda t$ ，式(5.3.47)变成
