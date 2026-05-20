# 圆判据

1949年，苏联科学家艾泽尔曼(Aizermann)猜想：如果由任意介于 $k_{1} < k < k_{2}$ 的线性增益替代 $f$ ，则Lur'e系统是稳定的，那么此增益被一个位于扇形区 $[k_1, k_2]$ 的非线性增益替代后，系统仍将是稳定的。这意味着，如果一个如图9.50所示的具有线性前向通路（A，B，C)的单环(严格正则)连续时间反馈系统，对任意 $k_{1} < k < k_{2}$ 的固定线性反馈增益都是稳定的，即可使得所得的闭环系统矩阵 $\mathbf{A} + k\mathbf{BC}$ 稳定，那么如图9.50所示的这个带有无记忆非线性时变反馈项的非线性系统也是稳定的，其中反馈项处于扇形区 $[k_1, k_2]$ 中。不幸的是，因为有反例存在 $^{\ominus}$ ，这种猜想是不正确的。然而，艾泽尔曼猜想的一种变体是正确的就是圆判据。

对圆判据我们不给出严格的证明，只描述一个有助于深入了解此问题和如何进行证明的启发性结论。一个带有线性阻抗 $Z(\mathrm{j}\omega) = R(\omega) + \mathrm{j}X(\omega)$ 的电路，被欧姆(Ohm)定律描述为 $V = IZ(s)$ 。假定 $Z$ 由真实元件构成，这就是说，实部 $R$ 是偶性的，虚部 $X$ 是奇性的；也就是 $R(-\omega) = R(\omega)$ 以及 $X(-\omega) = -X(\omega)$ 。如果对于所有的 $\omega$ ，有 $R(\omega) \geqslant \delta > 0$ ，此阻抗称为严格无源阻抗。它将消耗能量。进入电路的瞬时功率是 $p = v(t)i(t)$ ，且电路吸收的全部能量为 $e = \int_{0}^{+\infty} v(t)i(t)\mathrm{d}t$ 。参照图形，欧姆定律等同于系统方程 $Y = UG(s)$ ，其中： $Y$ 为电压； $U$ 为电流； $G(s) = R + \mathrm{j}X$ 为阻抗。将这种对能量的表达应用到系统方程，并利用 Parseval 提出的定理，将此研究转到频域就得到

$$\int_ {0} ^ {+ \infty} y (t) u (t) \mathrm{d} t = \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} U (\mathrm{j} \omega) Y (- \mathrm{j} \omega) \mathrm{d} \omega \tag {9.94}= \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} U (\mathrm{j} \omega) U (- \mathrm{j} \omega) G (- \mathrm{j} \omega) \mathrm{d} \omega \tag {9.95}= \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} | U (\mathrm{j} \omega) | ^ {2} (R - \mathrm{j} X) \mathrm{d} \omega \tag {9.96}= \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} | U (\mathrm{j} \omega) | ^ {2} R (\omega) \mathrm{d} \omega \tag {9.97}$$

最后一步，用到了 X 是奇性的这一条件。在此，使用一些常规记号将大大简化方程。我们定义内积和范数为：

$$\int_ {0} ^ {+ \infty} y (t) u (t) \mathrm{d} t = < y, u > \tag {9.98}\| u \| ^ {2} = \int_ {0} ^ {+ \infty} [ u (t) ] ^ {2} \mathrm{d} t = < u, u > \tag {9.99}$$

用这样的记法，以及 $R \geqslant \delta > 0$ 的假设，式(9.97)可简化为

$$< y, u > \geqslant \delta \| u \| ^ {2} \tag {9.100}$$

现在转向非线性部分，使用相同的“能量”概念，并假设 $f$ 在扇形区 $[0, K]$ 中，可得

$$\int_ {0} ^ {\infty} y (t) f (y, t) \mathrm{d} t = \int_ {0} ^ {+ \infty} \frac {[ f (y , t) ] ^ {2}}{f (y , t) / y (t)} \mathrm{d} t \tag {9.101}\geqslant \frac {\left\| f (y , t) \right\| ^ {2}}{K} \tag {9.102}\geqslant \frac {\left\| u (t) \right\| ^ {2}}{K} \tag {9.103}$$

假设由式(9.100)和式(9.102)的和所供给的全部能量是正的，那么由于能量稳步衰减，系统必然是稳定的。损失能量的实际值将等于存储在系统中元件的初始能量。由此我们可得出：如果 $\delta \| u\|^2 +\frac{\|u(t)\|^2}{K} >0$ ，那么系统是稳定的。因此，判据为：
