# 例 2.19 水箱液位和流出量的线性化

列写图 2.38 所描述水箱水位高度的非线性微分方程。假定在出口存在短时节流，设

$\alpha=2$ ，并在运算点 $h_{0}$ 附近对方程进行线性化。

解答。应用式(2.91)得到流出水箱的流量与水位高度的函数关系为

$$w _ {\text {out}} = \frac {1}{R} (p _ {1} - p _ {a}) ^ {1 / 2} \tag {2.93}$$

其中： $p_{1}=\rho gh+p_{a}$ 为液体压强； $p_{a}$ 为节流外部环境压强。

将式 $(2.93)$ 代入式 $(2.89)$ 得到关于水位高度的非线性微分方程为

$$\dot {h} = \frac {1}{A \rho} \left(w _ {\mathrm{in}} - \frac {1}{R} \sqrt {p _ {1} - p _ {\mathrm{a}}}\right) \tag {2.94}$$

64

选取工作点 $p_{0} = \rho gh_{0} + p_{a}$ ，对方程进行线性化，并将 $p_{1} = p_{0} + \Delta p$ 代入式(2.93)。然后根据下面关系式将非线性项展开：

$$(1 + \varepsilon) ^ {\beta} \approx 1 + \beta \varepsilon \tag {2.95}$$

其中： $\varepsilon\ll0$ 。因此式(2.93)可变为

$$
\begin{array}{l} w _ {\text {out}} = \frac {\sqrt {p _ {0} - p _ {\mathrm{a}}}}{R} \left(1 + \frac {\Delta p}{p _ {0} - p _ {\mathrm{a}}}\right) ^ {1 / 2} \\ \approx \frac {\sqrt {p _ {0} - p _ {\mathrm{a}}}}{R} \left(1 + \frac {1}{2} \frac {\Delta p}{p _ {0} - p _ {\mathrm{a}}}\right) \tag {2.96} \\ \end{array}
$$

只要 $\Delta p \ll p_{0} - p_{a}$ ，式(2.96)的近似线性关系就是合理的；即系统压强距选定的工作点偏差非常小。

合并式(2.89)和式(2.96)，得到水箱水位运动的线性化方程为

$$\Delta \dot {h} = \frac {1}{A \rho} \left[ w _ {i n -} \frac {\sqrt {p _ {0} - p _ {\mathrm{a}}}}{R} \left(1 + \frac {1}{2} \frac {\Delta p}{p _ {\mathrm{o}} - p _ {\mathrm{a}}}\right) \right]$$

由于 $\Delta p = \rho g\Delta h$ ，该方程演化为

$$\Delta \dot {h} = - \frac {g}{2 A R \sqrt {p _ {0} - p _ {\mathrm{a}}}} \Delta h + \frac {w _ {\mathrm{in}}}{A \rho} - \frac {\sqrt {p _ {0} - p _ {\mathrm{a}}}}{\rho A R} \tag {2.97}$$

这是关于 $\Delta h$ 的线性微分方程。工作点并不是平衡点，因为若要维持在该点，需要有一定的控制输入。也就是说，当系统无输入 $(w_{\mathrm{in}}=0)$ 且处于工作点 $(\Delta h=0)$ 时，它将因为 $\Delta h \neq 0$ 而偏离该点。因此，如果没有水流入水箱，那么水箱中的水会被耗尽，从而会偏离设定点。为了设定工作点是平衡点，要求有一额定流量，即

$$\frac {w _ {i n _ {0}}}{A \rho} = \frac {\sqrt {p _ {0} - p _ {\mathrm{a}}}}{\rho A R}$$

且把已线性化的输入流量作为此额定值的扰动。

液压执行机构同样遵循我们在水箱实例中看到的基本关系：连续性[式(2.88)]、力平衡性[式(2.90)]和流阻[式(2.91)]。尽管上述推导过程中假设液体是完全不可压缩的，然而实际上液体由于内部的传输携入空气而具有一定的压缩性。因为液体的可压缩性作用类似刚性弹簧，所以该特性导致液压执行机构具有一定的谐振性，此谐振会限制其响应速度。
