| x1 | x2 |
| --- | --- |
| -1.5 | 0.0 |
| -1.0 | 0.5 |
| -0.5 | 0.8 |
| 0.0 | 1.0 |
| 0.5 | 0.8 |
| 1.0 | 0.5 |
| 1.5 | 0.0 |
</details>

图 14.20 在 $x_{1}-x_{2}$ 相平面内, 状态反馈下的吸引区(实线)与输出反馈下 $\varepsilon=0.1$ (虚线) 和 $\varepsilon=0.05$ (点划线) 时的吸引区的交点

只用任意全局有界的稳定函数 $\gamma(x)$ 就能实现图14.18和图14.20的特性。在出现峰值的时间内，控制 $\gamma(\hat{x})$ 是饱和的。由于当 $\varepsilon$ 趋于零时，峰值的持续时间也趋于零，所以对于足够小的 $\varepsilon$ ，峰值持续时间变得非常小，以至于使设备状态 $x$ 接近初始值。峰值过后，估计误差变为 $O(\varepsilon)$ ，反馈控制 $\gamma(\hat{x})$ 接近 $\gamma(x)$ 。因此，当 $\varepsilon$ 趋于零时，闭环系统在输出反馈下的轨线逼近状态反馈下的轨线，这就恢复了在状态反馈下系统所达到的性能。通过在感兴趣的紧区域外使状态反馈控制或状态估计饱和，总可以实现 $\gamma(x)$ 的全局有界性。

分析输出反馈下闭环系统的步骤为:把系统表示为奇异扰动形式

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = \phi (x, \gamma (\hat {x})) \\ \varepsilon \dot {\eta} _ {1} = - \alpha_ {1} \eta_ {1} + \eta_ {2} \\ \varepsilon \dot {\eta} _ {2} = - \alpha_ {2} \eta_ {1} + \varepsilon \delta (x, \tilde {x}) \\ \end{array}
$$

其中 $\hat{x}_1 = x_1 - \varepsilon \eta_1, \hat{x}_2 = x_2 - \eta_2$ 。令 $\varepsilon = 0$ 得到的慢变模型逼近慢变量 $(x_1, x_2)$ 的运动。由于 $\varepsilon = 0$ 时， $\eta = 0$ ，所以式(14.91)和式(14.92)给出的慢变模型就是状态反馈下的闭环系统。 $(\eta_1, \eta_2)$ 的快速运动可由快变模型

$$
\varepsilon \dot {\eta} = \left[ \begin{array}{l l} {- \alpha_ {1}} & {1} \\ {- \alpha_ {2}} & {0} \end{array} \right] \eta \stackrel {\mathrm{def}} {=} A _ {0} \eta
$$
