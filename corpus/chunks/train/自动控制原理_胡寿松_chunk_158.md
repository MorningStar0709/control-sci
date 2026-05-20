# 1. 三阶系统的单位阶跃响应

下面以在 $s$ 左半平面具有一对共轭复数极点和一个实极点的分布模式为例，分析三阶系统的单位阶跃响应。其闭环传递函数的一般形式为

$$\Phi (s) = \frac {C (s)}{R (s)} = \frac {\omega_ {n} ^ {2} s _ {0}}{(s + s _ {0}) (s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2})} \tag {3-58}$$

式中， $(-s_0)$ 为三阶系统的闭环负实数极点。当输入为单位阶跃函数，且 $0 < \zeta < 1$ 时，输出量的拉氏变换为

$$C (s) = \frac {1}{s} + \frac {A}{s + s _ {0}} + \frac {B}{s + \zeta \omega_ {n} - \mathrm{j} \omega_ {n} \sqrt {1 - \zeta^ {2}}} + \frac {C}{s + \zeta \omega_ {n} + \mathrm{j} \omega_ {n} \sqrt {1 - \zeta^ {2}}}$$

式中 $A = \frac{-\omega_n^2}{s_0^2 - 2\zeta\omega_ns_0 + \omega_n^2}$

$$B = \frac {s _ {0} (2 \zeta \omega_ {n} - s _ {0}) - \mathrm{j} s _ {0} (2 \zeta^ {2} \omega_ {n} - \zeta s _ {0} - \omega_ {n}) / \sqrt {1 - \zeta^ {2}}}{2 [ (2 \zeta^ {2} \omega_ {n} - \zeta s _ {0} - \omega_ {n}) ^ {2} + (2 \zeta \omega_ {n} - s _ {0}) ^ {2} (1 - \zeta^ {2}) ]}C = \frac {s _ {0} (2 \zeta \omega_ {n} - s _ {0}) + \mathrm{j} s _ {0} (2 \zeta^ {2} \omega_ {n} - \zeta s _ {0} - \omega_ {n}) / \sqrt {1 - \zeta^ {2}}}{2 [ (2 \zeta^ {2} \omega_ {n} - \zeta s _ {0} - \omega_ {n}) ^ {2} + (2 \zeta \omega_ {n} - s _ {0}) ^ {2} (1 - \zeta^ {2}) ]}$$

对上式取拉氏反变换，且令 $b=s_{0}/\zeta\omega_{n}$ ，则有

$$
\begin{array}{l} c (t) = 1 + A \mathrm{e} ^ {- s _ {0} t} + 2 \operatorname{Re} B \cdot \mathrm{e} ^ {- \zeta \omega_ {n} t} \cos \omega_ {n} \sqrt {1 - \zeta^ {2}} t \\ - 2 \mathrm{Im} B \cdot \mathrm{e} ^ {- \zeta \omega_ {n} t} \sin \omega_ {n} \sqrt {1 - \zeta^ {2}} t, \quad t \geqslant 0 \\ \end{array}
$$

式中 $A = -\frac{1}{b\zeta^2(b - 2) + 1}$

$$\mathrm{Re} B = - \frac {b \zeta^ {2} (b - 2)}{2 [ b \zeta^ {2} (b - 2) + 1 ]}, \quad \mathrm{Im} B = \frac {b \zeta [ \zeta^ {2} (b - 2) + 1 ]}{2 [ b \zeta^ {2} (b - 2) + 1 ] \sqrt {1 - \zeta^ {2}}}$$

将上述系数代入 $c(t)$ 表达式，经整理得式(3-58)所示三阶系统在 $0 < \zeta < 1$ 时的单位阶跃响应：

$$
\begin{array}{l} c (t) = 1 - \frac {1}{b \zeta^ {2} (b - 2) + 1} \mathrm{e} ^ {- s _ {0} t} - \frac {\mathrm{e} ^ {- \zeta \omega_ {n} t}}{b \zeta^ {2} (b - 2) + 1} \left[ b \zeta^ {2} (b - 2) \cos \omega_ {n} \sqrt {1 - \zeta^ {2}} t \right. \\ + \frac {b \zeta [ \zeta^ {2} (b - 2) + 1 ]}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {n} \left. \sqrt {1 - \zeta^ {2}} t \right], \quad t \geqslant 0 \tag {3-59} \\ \end{array}
$$

当 $\zeta = 0.5, b \geqslant 1$ 时，三阶系统的单位阶跃响应曲线如图3-26所示。在式(3-59)中，由于

$$b \zeta^ {2} (b - 2) + 1 = \zeta^ {2} (b - 1) ^ {2} + (1 - \zeta^ {2}) > 0$$

所以，不论闭环实数极点在共轭复数极点的左边或右边，即 $b$ 不论大于1或是小于 $1, \mathrm{e}^{-s_0 t}$ 项的系数总是负数。因此，实数极点 $s = -s_0$ 可使单位阶跃响应的超调量下降，并使调节时间增加。
