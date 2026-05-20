# 2.3.1 连续 Ziegler-Nichols 方法的 PID 整定

Ziegler-Nichols 频域整定方法是基于稳定性分析的频域响应 PID 整定方法。该方法整定的思想是：对于给定的被控对象传递函数，可以得到其根轨迹，对应穿越 $j\omega$ 轴的点，增益即为 $K_{m}$ ，而此点的 $\omega$ 值即为 $\omega_{m}$ 。

整定公式如下 $^{[3]}$ :

$$K _ {\mathrm{p}} = 0. 6 K _ {\mathrm{m}}, \quad K _ {\mathrm{d}} = \frac {K _ {\mathrm{p}} \pi}{4 \omega_ {\mathrm{m}}}, \quad K _ {\mathrm{i}} = \frac {K _ {\mathrm{p}} \omega_ {m}}{\pi} \tag {2.5}$$

式中， $K_{m}$ 为系统开始振荡时的增益 K 值； $\omega_{m}$ 为振荡频率。

![](image/a2d24cbcc0850248e03107c775bdfde30c2b9decfbfb5268ba87555b94e1aa15.jpg)
