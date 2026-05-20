# 9.6 慢变系统

在系统

$$\dot {x} = f (x, u (t)) \tag {9.38}$$

中， $x \in R^{n}$ ，且对于所有 $t \geqslant 0, u(t) \in \Gamma \subset R^{m}$ ，如果 $u(t)$ 连续可微，且 $\| \dot{u}(t) \|$ “足够”小，则认为该系统是慢变系统。 $u(t)$ 的各分量可能是输入变量或时变参数。在分析系统(9.38)时，通常把 u 看成“冻结”参数，并假设对于每个固定的 $u = \alpha \in \Gamma$ ，冻结系统有一个由 $x = h(\alpha)$ 定义的孤立平衡点。如果 $x = h(\alpha)$ 的性质是对 $\alpha$ 一致，则有理由希望慢变系统(9.38)具有相似的性质。这类系统的根本特征是由初始条件变化引起的运动比由输入或时变参数引起的运动快得多。本节将说明如何用李雅普诺夫稳定性分析慢变系统。

假设 $f(x,u)$ 在 $R^n\times \Gamma$ 是局部利普希茨的，且对于每个 $u\in \Gamma$ ，方程

$$0 = f (x, u)$$

有一个连续可微的孤立根 $x = h(u)$ ，即

$$0 = f (h (u), u)$$

进一步假设 $\left\|\frac{\partial h}{\partial u}\right\|\leqslant L,\quad\forall u\in\Gamma$ (9.39)

为了分析冻结平衡点 $x = h(\alpha)$ 的稳定特性，通过变量代换 $z = x - h(\alpha)$ ，将其平移到原点，以得到方程 $\dot{z} = f(z + h(\alpha),\alpha)\stackrel {\mathrm{def}}{=}g(z,\alpha)$ (9.40)

现在寻找一个李雅普诺夫函数,证明 z=0 是渐近稳定的。由于 $g(z,\alpha)$ 取决于参数 $\alpha$ ,一般来讲,该系统的李雅普诺夫函数也可能与 $\alpha$ 有关。假设可以找到一个李雅普诺夫函数 $V(z,\alpha)$ ,对于所有 $z\in D=\{z\in R^{n}\mid\|z\|<r\}$ 和 $\alpha\in\Gamma$ ,满足条件

$$c _ {1} \| z \| ^ {2} \leqslant V (z, \alpha) \leqslant c _ {2} \| z \| ^ {2} \tag {9.41}\frac {\partial V}{\partial z} g (z, \alpha) \leqslant - c _ {3} \| z \| ^ {2} \tag {9.42}\left\| \frac {\partial V}{\partial z} \right\| \leqslant c _ {4} \| z \| \tag {9.43}\left\| \frac {\partial V}{\partial \alpha} \right\| \leqslant c _ {5} \| z \| ^ {2} \tag {9.44}$$

其中 $c_{i}, i=1,2,\cdots,5$ 是独立于 $\alpha$ 的正常数。不等式(9.41)和不等式(9.42)指出了对 V 的一般要求，即 V 是正定递减的，且沿系统(9.40)轨线的导数是负定的。这些不等式进一步证明原点 z=0 是指数稳定的。这里的特殊要求是这些不等式对 $\alpha$ 一致成立。不等式(9.43)和不等式(9.44)要处理方程(9.40)的扰动，这是因为 $u(t)$ 不是常数，而是时变函数。以 $V(z,u)$ 作为备选李雅普诺夫函数，继续分析系统(9.38)。进行变量代换 $z=x-h(u)$ ，系统(9.38)转换为

$$\dot {z} = g (z, u) - \frac {\partial h}{\partial u} \dot {u} \tag {9.45}$$

其中， $u$ 的时变效应以冻结系统(9.40)的扰动形式出现。 $V(z,u)$ 沿系统(9.45)轨线的导数为

$$
\begin{array}{l} \dot {V} = \frac {\partial V}{\partial z} \dot {z} + \frac {\partial V}{\partial u} \dot {u} (t) \\ = \frac {\partial V}{\partial z} g (z, u) + \left[ \frac {\partial V}{\partial u} - \cdot \frac {\partial V}{\partial z} \frac {\partial h}{\partial u} \right] \dot {u} (t) \\ \leqslant - c _ {3} \| z \| ^ {2} + c _ {5} \| z \| ^ {2} \| \dot {u} (t) \| + c _ {4} L \| z \| \| \dot {u} (t) \| \\ \end{array}
$$

令

$$\gamma (t) = \frac {c _ {5}}{c _ {4}} \| \dot {u} (t) \|, \quad \delta (t) = L \| \dot {u} (t) \|$$
