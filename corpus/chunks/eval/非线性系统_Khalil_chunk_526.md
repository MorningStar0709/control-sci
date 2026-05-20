$$\frac {\partial (P \eta) (y)}{\partial y} = \int_ {- \infty} ^ {0} \exp (- B s) \left[ \left(\frac {\partial G}{\partial y}\right) + \left(\frac {\partial G}{\partial z}\right) \left(\frac {\partial \eta}{\partial y}\right) \right] \pi_ {y} (s; y, \eta) d s$$

这样, 只要 $\varepsilon$ 和 $\alpha$ 足够小, 使 $\beta > \gamma$ , 就有

$$
\begin{array}{l} \left\| \frac {\partial (P \eta) (y)}{\partial y} \right\| \leqslant \int_ {- \infty} ^ {0} C \exp (\beta s) \left(1 + c _ {2}\right) \rho (\varepsilon) M (\alpha) \exp (- \gamma s) d s \\ = \frac {C (1 + c _ {2}) \rho (\varepsilon) M (\alpha)}{\beta - \gamma} \\ \end{array}
$$

当 $\varepsilon$ 足够小时， $(p\eta)(y)$ 的雅可比矩阵边界将小于 $c_{2}$ 。为证明雅可比矩阵 $[\partial (P\eta)(y) / \partial y]$ 是利普希茨常数为 $c_{3}$ 的利普希茨矩阵，注意到雅可比矩阵 $[\partial F / \partial y], [\partial F / \partial z], [\partial G / \partial y]$ 和 $[\partial G / \partial z]$ 对于所有 $x, y \in R^{k}, z, w \in B_{\varepsilon}$ ，都满足形如

$$\left\| \frac {\partial F}{\partial y} (y, z) - \frac {\partial F}{\partial y} (x, w) \right\| \leqslant L [ \| y - x \| + \| z - w \| ]$$

的利普希茨不等式。利用对于某个 $\varepsilon^{*} > 0$ ，有 $\varepsilon < \varepsilon^{*}$ ，可选择与 $\varepsilon$ 无关的利普希茨常数 $L$ ，而且 $L$ 可同时用于四个雅可比矩阵。利用这些不等式及Gronwall-Bellman不等式，重复前面的推导，可以证明对于所有 $x, y \in R^{k}$ 和 $t \leqslant 0$ ，有

$$\left\| \pi_ {y} (t; y, \eta) - \pi_ {y} (t; x, \eta) \right\| \leqslant L _ {1} \exp (- 2 \gamma t) \| y - x \|$$

其中 $L_{1} = \left[(1 + c_{2})^{2}L + \rho (\varepsilon)c_{3}\right]M^{3}(\alpha) / \gamma$ 。最后一个不等式可用于证明

$$\left\| \frac {\partial (P \eta)}{\partial y} (y) - \frac {\partial (P \eta)}{\partial y} (x) \right\| \leqslant \frac {C L _ {1} (2 \gamma - \alpha)}{M (\beta - 2 \gamma)} \| y - x \|$$

只要 $\beta - 2\gamma > 0$ 。选择 $\alpha$ 和 $\varepsilon$ 足够小，使得 $\beta - 2\gamma > \beta / 2$ ，则

$$y (t) \leqslant \lambda (t) + \int_ {t} ^ {a} \mu (s) y (s) d s$$

则 $y(t)\leqslant \lambda (t) + \int_t^a\lambda (s)\mu (s)\exp \left[\int_t^s\mu (\tau)d\tau \right]ds$

$$\left\| \frac {\partial (P \eta)}{\partial y} (y) - \frac {\partial (P \eta)}{\partial y} (x) \right\| \leqslant [ L _ {2} + \rho (\varepsilon) L _ {3} c _ {3} ] \| y - x \|$$
