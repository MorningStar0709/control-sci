# 3.4.2 超调和峰值时间

我们将对超调 $M_{p}$ 进行更多的分析。当通过计算得出导数为零时，这个值才会存在。图 3.19b 所示曲线的时间函数可通过 $H(s)/s$ 的拉普拉斯反变换求得，即

$$y (t) = 1 - \mathrm{e} ^ {- \sigma t} \left(\cos (\omega_ {\mathrm{d}} t) + \frac {\sigma}{\omega_ {\mathrm{d}}} \sin (\omega_ {\mathrm{d}} t)\right) \tag {3.69}$$

其中： $\omega_{d}=\omega_{n}\sqrt{1-\zeta^{2}};\quad\sigma=\zeta\omega_{n}$

我们可以用三角恒等式重写前面的方程式，即

$$A \sin (\alpha) + B \cos (\alpha) = C \cos (\alpha - \beta)$$

其中： $\alpha$ 为 $\omega_{d}t$ 。

或者

$$C = \sqrt {A ^ {2} + B ^ {2}} = \frac {1}{\sqrt {1 - \zeta^ {2}}}\beta = \arctan \left(\frac {A}{B}\right) = \arctan \left(\frac {\zeta}{\sqrt {1 - \zeta^ {2}}}\right) = \operatorname{arc} \sin (\zeta)$$

其中： $A=\frac{\sigma}{\omega_{d}}$ ; B=1。

一个更简洁的表示方法为

$$y (t) = 1 - \frac {\mathrm{e} ^ {- \sigma t}}{\sqrt {1 - \zeta^ {2}}} \cos (\omega_ {\mathrm{d}} t - \beta) \tag {3.70}$$

当 $y(t)$ 达到它的最大值时，它的导数将为0，即

$$
\begin{array}{l} \dot {y} (t) = \sigma \mathrm{e} ^ {- \sigma t} \left(\cos \left(\omega_ {\mathrm{d}} t\right) + \frac {\sigma}{\omega_ {\mathrm{d}}} \sin \left(\omega_ {\mathrm{d}} t\right)\right) - \mathrm{e} ^ {- \sigma t} \left(- \omega_ {\mathrm{d}} \sin \left(\omega_ {\mathrm{d}} t\right) + \sigma \cos \left(\omega_ {\mathrm{d}} t\right)\right) = 0 \\ = \mathrm{e} ^ {- \sigma t} \left(\frac {\sigma^ {2}}{\omega_ {\mathrm{d}}} + \omega_ {\mathrm{d}}\right) \sin \left(\omega_ {\mathrm{d}} t\right) = 0 \\ \end{array}
$$

当 $\sin(\omega_{\mathrm{d}}t)=0$ 时，上式成立，所以

$$\omega_ {\mathrm{d}} t _ {\mathrm{p}} = \pi$$

因此

$$t _ {\mathrm{p}} = \frac {\pi}{\omega_ {\mathrm{d}}} \tag {3.71}$$

将式(3.71)代入到 $y(t)$ 的表达式中，我们计算

$$
\begin{array}{l} y \left(t _ {\mathrm{p}}\right) p \stackrel {\text { def }} {=} 1 + M _ {\mathrm{p}} = 1 - \mathrm{e} ^ {- \sigma \pi / \omega_ {\mathrm{d}}} \left(\cos \pi + \frac {\sigma}{\omega_ {\mathrm{d}}} \sin \pi\right) \\ = 1 + \mathrm{e} ^ {- \sigma \pi / \omega_ {\mathrm{d}}} \\ \end{array}
$$

因此，我们可得

$$M _ {\mathrm{p}} = \mathrm{e} ^ {- \pi \zeta / \sqrt {1 - \zeta^ {2}}}, \quad 0 \leqslant \zeta < 1 \tag {3.72}$$

该图绘制在图3.24中。从曲线图中可知，频繁使用的两组值分别为 $M_{\mathrm{p}} = 0.16$ ， $\zeta = 0.5$ 和 $M_{\mathrm{p}} = 0.05$ ， $\zeta = 0.7$ ，也就是说，超调分别为 $16\%$ 和 $5\%$ 。

![](image/f430d3ffaec56183b37fe888d9cd2197a7cb849ccbe80467851b209fb56830b2.jpg)

<details>
<summary>line</summary>

| ζ | Mp (%) |
| --- | --- |
| 0.5 | 16 |
| 0.7 | 5 |
</details>

图 3.24 二阶系统中超调与阻尼比的关系
