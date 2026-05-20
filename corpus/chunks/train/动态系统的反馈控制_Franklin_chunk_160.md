$$a (s) = (s + \sigma - \mathrm{j} \omega_ {\mathrm{d}}) (s + \sigma + \mathrm{j} \omega_ {\mathrm{d}}) = (s + \sigma) ^ {2} + \omega_ {\mathrm{d}} ^ {2} \tag {3.62}$$

从二阶微分方程中求出传递函数，且通常将结果写成多项式的形式，即

$$H (s) = \frac {\omega_ {\mathrm{n}} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2}} \tag {3.63}$$

将式(3.62)展开，并且将它与式(3.63)中 $H(s)$ 的分母系数作比较，找到两者系数之间的对应关系为

$$\sigma = \zeta \omega_ {\mathrm{n}}, \quad \omega_ {\mathrm{d}} = \omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}} \tag {3.64}$$

其中：参数 $\zeta$ 是阻尼比 $^{\ominus}$ ; $\omega_{n}$ 是无阻尼自然频率。

这个传递函数的极点位于 s 平面上半径为 $\omega_{n}$ ，角度为 $\theta = \arcsin \zeta$ 处，如图 3.18 所示。因此，阻尼比是用极点为实数时的临界阻尼值分量来反映阻尼水平的。在矩形坐标中，极点位于 $s = -\sigma \pm j \omega_{d}$ 处。当 $\zeta = 0$ 时，系统为无阻尼， $\theta = 0$ ，阻尼自然频率等于无阻尼自然频率，即 $\omega_{d} = \omega_{n}$ 。

为了从表 A.2 中找出复传递函数对应的时间响应，最简单的方法是，处理 $H(s)$ 以使复极点满足式(3.62)的形式，因为该形式的时间响应可以直接从表中得出。式(3.63)可以改写成

$$H (s) = \frac {\omega_ {\mathrm{n}} ^ {2}}{(s + \zeta \omega_ {\mathrm{n}}) ^ {2} + \omega_ {\mathrm{n}} ^ {2} (1 - \zeta^ {2})} \tag {3.65}$$

因此，从表 A.2 中第 20 条以及式(3.64)的定义，我们可得脉冲响应为

![](image/6151ce641eabe85ea17d33a5fea9a553286ecff314514319678183076576a7fe.jpg)

<details>
<summary>text_image</summary>

θ = arc sinζ
ωₙ
Im(s)
Re(s)
s
ω_d
</details>

图3.18 一对复极点的 $s$ 平面图

$$h (t) = \frac {\omega_ {\mathrm{n}}}{\sqrt {1 - \zeta^ {2}}} \mathrm{e} ^ {- \sigma t} (\sin (\omega_ {\mathrm{d}} t)) 1 (t) \tag {3.66}$$

图 3.19a 绘制了不同 $\zeta$ 值时的 $h(t)$ 曲线图，时间已经归一化为无阻尼自然频率 $\omega_{n}$ 。注意实际频率 $\omega_{d}$ 会随着阻尼比的增加而略微降低。也要注意，对于过低的阻尼来说，其响应是振荡的，然而对于大阻尼 ( $\zeta$ 接近于 1) 来说，其响应没有振荡。这些响应中的一部分绘制在图 3.16 中，定性的描述了 s 平面内极点位置的变化是如何影响脉冲响应的。作为一个控制系统设计者，牢牢记住图 3.16 所示的图像将是非常有用的，这样就可以能够快速理解极点位置的变化是如何影响时间响应的。

![](image/f0349aec327eedc3c1f6ea69f657aa33ecbfaee165bcd65bde09684fadf4d42f.jpg)

<details>
<summary>line</summary>
