$$
\begin{array}{l} z (\tau) = \exp [ - B (t - \tau) ] z (t) \\ + \int_ {t - \tau} ^ {0} \exp (- B s) G (\pi (s; y (\tau), \eta), \eta (\pi (s; y (\tau), \eta))) d s \\ \end{array}
$$

该式对于任意 $t \in R$ 皆成立。积分项在 $t$ 趋于负无穷时的极限为

$$\int_ {- \infty} ^ {0} \exp (- B s) G (\pi (s; y (\tau), \eta), \eta (\pi (s; y (\tau), \eta))) d s \tag {C.60}$$

由于 $\eta$ 是有界的, G 是全局有界的, 其边界值为 $\pi$ , B 是赫尔维茨的, 故上面的极限有定义, 将式(C.60)中的 $y(\tau)$ 用 y 表示, 并将式(C.60)记为 $(P\eta)(y)$ , 得

$$(P \eta) (y) = \int_ {- \infty} ^ {0} \exp (- B s) G (\pi (s; y, \eta), \eta (\pi (s; y, \eta))) d s \tag {C.61}$$

利用上面的定义,可得

$$
\begin{array}{l} \exp [ B (t - \tau) ] [ z (\tau) - (P \eta) (y (\tau)) ] = \\ z (t) - \int_ {- \infty} ^ {t - \tau} \exp [ - B (s - t + \tau) ] G (\pi (s; y (\tau), \eta), \eta (\pi (s; y (\tau), \eta))) d s \\ \end{array}
$$

将 $\xi = s - t + \tau$ 代入积分中，并利用 $\pi (\xi +t - \tau ;y(\tau),\eta) = \pi (\xi ;y(t),\eta)$ ，得到

$$\exp [ B (t - \tau) ] [ z (\tau) - (P \eta) (y \tau)) ] = z (t) - (P \eta) (y (t))$$

上式说明对于任意 $t \in R$ ，如果 $z(\tau) = (P\eta)(y(\tau))$ ，则 $z(t) = (P\eta)(y(t))$ ，因此 $z = (P\eta)(y)$ 对于系统(C.58)～(C.59)定义了一个以 $\eta$ 为参数的不变流形。

考虑系统(C.56)\~(C.57)，如果 $\eta(y)$ 是映射 $(P\eta)(y)$ 的一个不动点，即

$$\eta (y) = (P \eta) (y)$$

则 $z = \eta(y)$ 是系统(C.56) \~ (C.57) 的中心流形。这一情况可理解为: 首先, 利用性质 $\eta \in S$ 及 y = 0 是方程(C.58) 的平衡点, 由式(C.61) 可看出

$$(P \eta) (0) = 0; \quad {\frac {\partial (P \eta)}{\partial y}} (0) = 0$$

其次，由于 $z = (P\eta)(y)$ 是系统(C.58)\~(C.59)的不变流形， $(P\eta)(y)$ 满足偏微分方程

$$\frac {\partial}{\partial y} (P \eta) (y) [ A y + F (y, (P \eta) (y)) ] = B (P \eta) (y) + G (y, (P \eta) (y))$$

如果 $\eta(y) = (P\eta)(y)$ ，显然 $\eta(y)$ 满足同样的偏微分方程，因此它是系统（C.56）～（C.57）的一个中心流形。现在只剩下证明映射 $(P\eta)$ 有一个不动点，这将应用压缩映射定理证明。我们想要证明 $P\eta$ 是 $S$ 到其自身的映射，且是 $S$ 上的压缩映射。根据 $F$ 和 $G$ 的定义，存在一个非负连续函数 $\rho(\varepsilon)$ ，且 $\rho(0) = 0$ ，使得对于所有 $y \in R^k, z \in R^m$ 且 $\|z\| < \varepsilon$ ，有

$$\| F (y, z) \| \leqslant \varepsilon \rho (\varepsilon); \left\| \frac {\partial F}{\partial y} (y, z) \right\| \leqslant \rho (\varepsilon); \left\| \frac {\partial F}{\partial z} (y, z) \right\| \leqslant \rho (\varepsilon) \tag {C.62}\| G (y, z) \| \leqslant \varepsilon \rho (\varepsilon); \left\| \frac {\partial G}{\partial y} (y, z) \right\| \leqslant \rho (\varepsilon); \left\| \frac {\partial G}{\partial z} (y, z) \right\| \leqslant \rho (\varepsilon) \tag {C.63}$$

由于 B 的特征值实部为负, 因此存在正常数 $\beta$ 和 C, 使得对于 $s \leqslant 0$ , 有

$$\| \exp (- B s) \| \leqslant C \exp (\beta s) \tag {C.64}$$
