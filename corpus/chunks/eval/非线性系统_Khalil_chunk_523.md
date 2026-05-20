$$
\begin{array}{l} \left[ \frac {\partial \eta_ {i}}{\partial y} (y) - \frac {\partial \eta_ {j}}{\partial y} (y) \right] \mu v = \left[ \frac {\partial \eta_ {i}}{\partial y} (y) - \frac {\partial \eta_ {i}}{\partial y} (y + \alpha_ {i} \mu v) \right] \mu v \\ - \left[ \frac {\partial \eta_ {j}}{\partial y} (y) - \frac {\partial \eta_ {j}}{\partial y} (y + \alpha_ {j} \mu v) \right] \mu v \\ + \left[ \eta_ {i} (y + \mu v) - \eta_ {j} (y + \mu v) \right] - \left[ \eta_ {i} (y) - \eta_ {j} (y) \right] \\ \end{array}
$$

给定 $\varepsilon > 0$ ，求足够大的 $i_{0}$ 和 $j_{0}$ ，使得对于所有 $i > i_{0}$ 和 $j > j_{0}$ ，有

$$\sup _ {y \in R ^ {k}} \| \eta_ {i} (y) - \eta_ {j} (y) \| < \frac {\varepsilon^ {2}}{1 6 c _ {3}}$$

这是可能的,因为 $\{\eta_{i}\}$ 收敛。利用前述不等式及

$$\psi (y) = 1 - \frac {1}{b} \int_ {1} ^ {| y |} \exp \left(\frac {- 1}{x - 1}\right) \exp \left(\frac {- 1}{2 - x}\right) d x, \quad 1 < | y | < 2$$

其中 $b=\int_{1}^{2}\exp\left(\frac{-1}{x-1}\right)\exp\left(\frac{-1}{2-x}\right)dx$

$$\left\| \left[ \frac {\partial \eta_ {\ell}}{\partial y} (y) - \frac {\partial \eta_ {\ell}}{\partial y} (y + \alpha_ {\ell} \mu v) \right] \mu v \right\| \leqslant c _ {3} \alpha_ {\ell} \mu^ {2} \| v \| ^ {2} < c _ {3} \mu^ {2}, \quad \ell = i \text {或} j$$

可以证明 $\left\| \left[\frac{\partial\eta_i}{\partial y}(y) - \frac{\partial\eta_j}{\partial y}(y)\right]v\right\| < 2c_3\mu +\frac{\varepsilon^2}{8c_3\mu}$

取 $\mu = \varepsilon / (4c_3)$ ，可得 $\left\| \frac{\partial \eta_i}{\partial y}(y) - \frac{\partial \eta_j}{\partial y}(y) \right\| < \varepsilon$

因此, $\partial\eta_{i}/\partial y$ 是 Banach 空间的 Cauchy 序列,该空间由 $R^{k}$ 到 $R^{k}$ 的全局有界连续函数组成,因而该序列收敛到连续函数 $J(y)$ ,即 $\eta(y)$ 是可微的,且 $\partial\eta/\partial y=J(y)^{①}$ 。

对于给定的 $\eta \in S$ ，考虑系统

$$\dot {y} = A y + F (y, \eta (y)) \tag {C.58}\dot {z} = B z + G (y, \eta (y)) \tag {C.59}$$

由于 $\eta(y)$ 和 $[\partial \eta / \partial y]$ 的有界性, 方程(C.58)的右边对 $y$ 是全局利普希茨的。因此, 对每个初值 $y_0 \in R^k$ , 方程(C.58)有唯一解, 对于所有 $t$ 都有定义, 且以固定函数 $\eta$ 为参数, 记为 $y(t) = \pi(t; y_0, \eta)$ , 其中 $\pi(0; y_0, \eta) = y_0$ 。方程(C.59)关于 $z$ 是线性的, 因此其解为

$$
\begin{array}{l} z (t) = \exp [ B (t - \tau) ] z (\tau) \\ + \int_ {\tau} ^ {t} \exp [ B (t - \lambda) ] G (\pi (\lambda - \tau ; y (\tau), \eta), \eta (\pi (\lambda - \tau ; y (\tau), \eta))) d \lambda \\ \end{array}
$$

用 $\exp [-B(t - \tau)]$ 遍乘，将积分项移到另一边，并把积分变量 $\lambda$ 代换为 $s = \lambda -\tau$ ，可得
