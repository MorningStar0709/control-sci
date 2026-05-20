由于 $A$ 的特征值实部为零, 因此对于每个 $\alpha > 0$ , 存在一个正常数 $M(\alpha)$ (当 $\alpha$ 趋于零时, 它可能趋于无穷), 使得对于 $s \in R$ , 有

$$\| \exp (A s) \| \leqslant M (\alpha) \exp (\alpha | s |) \tag {C.65}$$

为了证明 $P\eta$ 是 $S$ 到其自身的映射，需要证明存在正常数 $c_{1}, c_{2}$ 和 $c_{3}$ ，使得如果对于所有 $x, y \in R^{k}, \eta(y)$ 是连续可微的，且满足

$$\| \eta (y) \| \leqslant c _ {1}; \quad \left\| \frac {\partial \eta}{\partial y} (y) \right\| \leqslant c _ {2}; \quad \left\| \frac {\partial \eta}{\partial y} (y) - \frac {\partial \eta}{\partial y} (x) \right\| \leqslant c _ {3} \| y - x \|$$

那么 $(P\eta)(y)$ 是连续可微的,且满足同一不等式。由式(C.61)很容易看出 $(P\eta)(y)$ 的连续可微性。为了验证不等式,需要用到式(C.62)和式(C.63)给出的F和G的估计值,因此选择 $c_{1}$ 满足 $0.5\varepsilon<c_{1}<\varepsilon$ 。利用式(C.64)及G和 $\eta$ 的估计值,由式(C.61)得

$$\| (P \eta) (y) \| \leqslant \int_ {- \infty} ^ {0} \| \exp (- B s) \| \| G \| d s \leqslant \int_ {- \infty} ^ {0} C \exp (\beta s) \varepsilon \rho (\varepsilon) d s = \frac {C \varepsilon \rho (\varepsilon)}{\beta}$$

对于足够小的 $\varepsilon,(P\eta)(y)$ 的上界小于 $c_{1}$ 。设 $\pi_{y}(t;y,\eta)$ 表示 $\pi(t;y,\eta)$ 对 y 的雅可比矩阵，它满足变分方程

$$\dot {\pi} _ {y} = \left[ A + \left(\frac {\partial F}{\partial y}\right) + \left(\frac {\partial F}{\partial z}\right) \left(\frac {\partial \eta}{\partial y}\right) \right] \pi_ {y}, \quad \pi_ {y} (0; y, \eta) = I$$

其中 $\left(\frac{\partial F}{\partial y}\right) = \left(\frac{\partial F}{\partial y}\right)(\pi (t;y,\eta),\eta (\pi (t;y,\eta)))$

$\partial F / \partial z$ 和 $\partial \eta /\partial y$ 也具有相似的表达式。因此当 $t\leqslant 0$ 时，有

$$\pi_ {y} (t; y, \eta) = \exp (A t) - \int_ {t} ^ {0} \exp [ A (t - s) ] \left[ \left(\frac {\partial F}{\partial y}\right) + \left(\frac {\partial F}{\partial z}\right) \left(\frac {\partial \eta}{\partial y}\right) \right] \pi_ {y} (s; y, \eta) d s$$

利用式(C.65)及 $F$ 和 $\eta$ 的估计值，得

$$\| \pi_ {y} (t; y, \eta) \| \leqslant M (\alpha) \exp (- \alpha t) + \int_ {t} ^ {0} M (\alpha) \exp [ \alpha (s - t) ] (1 + c _ {2}) \rho (\varepsilon) \| \pi_ {y} (s; y, \eta) \| d s$$

用 $\exp (\alpha t)$ 遍乘各项，并应用Gronwall-Bellman不等式，证明①

$$\left\| \pi_ {y} (t; y, \eta) \right\| \leqslant M (\alpha) \exp (- \gamma t)$$

这里 $\gamma = \alpha + M(\alpha)(1 + c_2)\rho(\varepsilon)$ 。利用此边界，以及式(C.64)与 $G$ 和 $\eta$ 的估计值，继续计算雅可比矩阵 $[\partial(P\eta)(y)/\partial y]$ 的边界。由式(C.61)，得
