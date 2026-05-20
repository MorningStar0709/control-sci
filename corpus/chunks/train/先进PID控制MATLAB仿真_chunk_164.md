# 2.3.3 离散 Ziegler-Nichols 方法的 PID 整定

Ziegler-Nichols 方法同样也适用于离散系统的 PID 整定。该方法整定比例系数的思想是：对于给定的被控对象传递函数，选择其离散系统的根轨迹图与 z 平面单位圆交点（共有两个点，任选其一），从而获得增益 $K_{m}$ 和该点的 $\omega$ 值即 $\omega_{m}$ 。整定公式如下：

$$K _ {\mathrm{p}} = 0. 6 K _ {\mathrm{m}}, \quad K _ {\mathrm{d}} = \frac {K _ {\mathrm{p}} \pi}{4 \omega_ {\mathrm{m}}}, \quad K _ {\mathrm{i}} = \frac {K _ {\mathrm{p}} \omega_ {\mathrm{m}}}{\pi} \tag {2.6}$$

式中， $K_{m}$ 为系统开始振荡时的 $K_{p}$ 值； $\omega_{m}$ 为振荡频率。振荡频率 $\omega_{m}$ 可以由极点位于单位圆上的角度 $\theta$ 得到， $\omega_{m} = \frac{\theta}{T}$ （T 为采样周期）。

![](image/98df3a080a0b0cb8a6edc3d90e764ae9a0ef1504bf836f072283043ff59ae489.jpg)
