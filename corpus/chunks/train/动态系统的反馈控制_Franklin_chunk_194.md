(c) 求外加电压 $v_{h}$ 和轴角 $\theta_{m}$ 之间的传递函数。

(d) 设给(c)问中的系统加入一个反馈，使其成为一个位置伺服装置，外加电压为 $v_{\mathrm{a}} = K(\theta_{\mathrm{r}} - \theta_{\mathrm{m}})$ ，其中 K 为反馈增益，求 $\theta_{r}$ 和 $\theta_{m}$ 之间的传递函数。

(e) 如果期望超调 $M<20\%$ ，那么 K 所能取的最大值是多少？

(f) K 为何值时，上升时间小于 4s（忽略 $M_{p}$ 的约束）?

(g) 使用 Matlab 绘制增益 K=0.5、1 和 2 时该位置伺服系统的阶跃响应。通过检查所绘制的图，求这三个阶跃响应的超调和上升时间。这些图与 (e) 和 (f) 问中计算的结果是否一致？

3.36 欲控制图 3.60 和图 3.61 所示的卫星跟踪天线的仰角。天线和驱动部分的转动惯量为 J，阻尼为 B；在一定程度上，这些是由轴承和空气摩擦引起的，但大部分还是来自直流驱动电动机的反电动势。运动方程为

$$J \ddot {\theta} + B \dot {\theta} = T _ {c}$$

其中： $T_{c}$ 为该驱动电动机的转矩。设 J=600 000kg·m² 和 B=20000N·m·s。

![](image/7685adf04492eb20f0bb4bd4f90a39d0e675ab735bb93b932ef69eb9f8b3729a.jpg)

<details>
<summary>natural_image</summary>

Black-and-white photo of a large satellite dish antenna mounted on a stand, surrounded by trees and a road (no visible text or symbols)
</details>

图 3.60 卫星跟踪天线

![](image/50fe7da9a603485a8ad171887dafd2db546c82a08d9f5ffcc24e2730870bc190.jpg)

<details>
<summary>natural_image</summary>

Diagram of a telescope reflecting off a dish, showing light path and angle (no text or symbols)
</details>

图 3.61 习题 3.36 的天线示意图

(a) 求外加转矩 $T_{c}$ 和天线角度 $\theta$ 之间的传

递函数。

(b) 假设外加转矩已知，根据反馈定律可知， $\theta$ 跟踪基准命令 $\theta_{r}$ ： $T_{c}=K(\theta_{r}-\theta)$ ，其中：K 为反馈增益。求 $\theta_{r}$ 和 $\theta$ 之间的传递函数。

(c) 若希望超调 $M_{p}<10\%$ ，那么 K 所能取的最大值是多少？

(d) K 为何值时，上升时间小于 80s（忽略 $M_{p}$ 的约束）?

(e) 用 Matlab 绘制当 K=200, 40, 1000, 2000 时天线系统的阶跃响应。通过检查所画的图，求上述四个阶跃响应的超调和上升时间。所画的图是否与 (c) 和 (d) 问中计算的一致？

3.37 证明二阶系统

$$\ddot {y} + 2 \zeta \omega_ {\mathrm{n}} \dot {y} + \omega_ {\mathrm{n}} ^ {2} y = 0, \quad y (0) = y _ {0}, \quad \dot {y} (0) = 0$$

的响应为

$$y (t) = y _ {0} \frac {\mathrm{e} ^ {- \sigma t}}{\sqrt {1 - \zeta^ {2}}} \sin (\omega_ {\mathrm{d}} t + \operatorname{arc} \cos \zeta)$$

证明，在欠阻尼情况 $(\zeta<1)$ 下，响应振荡以预期速率即所谓的对数衰减率（见图3.62）衰减。

$$
\begin{array}{l} \delta = \ln \frac {y _ {0}}{y _ {1}} = \ln e ^ {\pi_ {d}} = \sigma_ {d} = \frac {2 \pi \zeta}{\sqrt {1 - \zeta^ {2}}} \\ = \ln \frac {\Delta y _ {1}}{y _ {1}} \approx \ln \frac {\Delta y _ {i}}{y _ {i}} \\ \end{array}
$$

其中：

$$\tau_ {\mathrm{d}} = \frac {2 \pi}{\omega_ {\mathrm{d}}} = \frac {2 \pi}{\omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}}}$$

为阻尼自振周期。根据对数衰减率得到阻尼系数为

$$\zeta = \frac {\delta}{\sqrt {4 \pi^ {2} + \delta^ {2}}}$$

![](image/514fd1ee32666abfbc30a46484bdcc49523669f2369635132a985be200c1f008.jpg)
