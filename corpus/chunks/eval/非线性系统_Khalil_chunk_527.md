$L_{2}$ 和 $L_{3}$ 与 $\varepsilon$ 和 $c_{3}$ 无关。选取 $c_{3} > L_{2}$ ，可选择足够小的 $\varepsilon$ ，使得 $L_{2} + \rho(\varepsilon)L_{3}c_{3} < c_{3}$ 。这样就证明了对于足够小的 $c_{1}$ 和足够大的 $c_{3}$ ，映射 $P\eta$ 是 S 到其自身的映射。为了证明它是 S 上的压缩映射，设 $\eta_{1}(y)$ 和 $\eta_{2}(y)$ 是 S 内的两个函数。另设 $\pi_{1}(t)$ 和 $\pi_{2}(t)$ 是相应于方程 (C.58) 始于 y 的解，即 $\pi_{i}(t) = \pi(t; y, \eta_{i}), i = 1, 2$

用式(C.62)和式(C.63)给出的估计,可证明

$$\| F \left(\pi_ {2}, \eta_ {2} \left(\pi_ {2}\right)\right) - F \left(\pi_ {1}, \eta_ {1} \left(\pi_ {1}\right)\right) \| \leqslant (1 + c _ {2}) \rho (\varepsilon) \| \pi_ {2} - \pi_ {1} \| + \rho (\varepsilon) \sup _ {y \in R ^ {k}} \| \eta_ {2} - \eta_ {1} \|\| G (\pi_ {2}, \eta_ {2} (\pi_ {2})) - G (\pi_ {1}, \eta_ {1} (\pi_ {1})) \| \leqslant (1 + c _ {2}) \rho (\varepsilon) \| \pi_ {2} - \pi_ {1} \| + \rho (\varepsilon) \sup _ {y \in R ^ {k}} \| \eta_ {2} - \eta_ {1} \|$$

根据式(C.58)， $\|\pi_2 - \pi_1\|$ 满足

$$
\begin{array}{l} \| \pi_ {2} (t) - \pi_ {1} (t) \| \leqslant \int_ {t} ^ {0} M (\alpha) \exp [ \alpha (s - t) ] [ \rho (\varepsilon) \sup _ {y \in R ^ {k}} \| \eta_ {2} - \eta_ {1} \| \\ \left. + \left(1 + c _ {2}\right) \rho (\varepsilon) \| \pi_ {2} (s) - \pi_ {1} (s) \| \right] d s \\ \leqslant \frac {1}{\alpha} M (\alpha) \rho (\varepsilon) \sup _ {y \in R ^ {k}} \| \eta_ {2} - \eta_ {1} \| \exp (- \alpha t) \\ + \int_ {t} ^ {0} (\gamma - \alpha) \exp [ \alpha (s - t) ] \| \pi_ {2} (s) - \pi_ {1} (s) \| d s \\ \end{array}
$$

其中用到 $\gamma = \alpha + M(\alpha)(1 + c_{2})\rho(\varepsilon)$ 以及 $\pi_{1}(0) = \pi_{2}(0)$ 。用 $\exp(\alpha t)$ 遍乘各项，并应用 Gronwall-Bellman 不等式证明

$$\| \pi_ {2} (t) - \pi_ {1} (t) \| \leqslant \frac {1}{\alpha} M (\alpha) \rho (\varepsilon) \sup _ {y \in R ^ {k}} \| \eta_ {2} - \eta_ {1} \| \exp (- \gamma t)$$

把上述不等式用于

$$
(P \eta_ {2}) (y) - (P \eta_ {1}) (y) = \int_ {- \infty} ^ {0} \exp (- B s) [ G (\pi_ {2}, \eta_ {2} (\pi_ {2})) - G (\pi_ {1}, \eta_ {1} (\pi_ {1})) ] d s
\begin{array}{l} + \rho (\varepsilon) \sup _ {y \in R ^ {k}} \| \eta_ {2} - \eta_ {1} \| ] d s \\ \leqslant C \rho (\varepsilon) \sup _ {y \in R ^ {k}} \| \eta_ {2} - \eta_ {1} \| \left[ \frac {1}{\beta} \right. \\ \left. + \int_ {- \infty} ^ {0} e ^ {\beta s} \left(1 + c _ {2}\right) \frac {1}{\alpha} M (\alpha) \rho (\varepsilon) e ^ {- \gamma s} d s \right] \\ \leqslant b \sup _ {y \in R ^ {k}} \| \eta_ {2} - \eta_ {1} \| \\ \end{array}
$$

得 $\| (P\eta_2)(y) - (P\eta_1)(y)\| \leqslant \int_{-\infty}^{0}Ce^{\beta s}[(1 + c_2)\rho (\varepsilon)\| \pi_2(s) - \pi_1(s)\|$
