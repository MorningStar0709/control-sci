# 2.4.1 基本原理

针对二阶系统传递函数，采用频域分析方法 $^{[7]}$ ，可实现 PD 的整定。二阶系统传递函数的标准形式为

$$\phi (s) = \frac {\omega_ {\mathrm{n}} ^ {2}}{s ^ {2} + 2 \xi \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2}} \tag {2.7}$$

二阶系统的动态特性可用系统阻尼比 $\xi$ 和固有频率 $\omega_{n}$ 来描述，它的动态特性为

$$s ^ {2} + 2 \xi \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2} = 0 \tag {2.8}$$

下面以二阶系统为例来说明 PD 控制机理。被控对象为

$$G (s) = \frac {K}{s (\tau s + 1)} \tag {2.9}$$

闭环控制器采用 PD 控制:

$$D (s) = K _ {\mathrm{p}} + K _ {\mathrm{d}} s \tag {2.10}$$

则闭环系统的传递函数为 $\frac{D(s)G(s)}{1+D(s)G(s)}$ ，其特征方程为 $1+D(s)G(s)=0$ ，即

$$\tau s ^ {2} + \left(1 + K K _ {\mathrm{d}}\right) s + K K _ {\mathrm{p}} = 0 \tag {2.11}$$

根据式（2.11），可得系统的固有频率为

$$\omega_ {\mathrm{n}} = \sqrt {K K _ {\mathrm{p}} / \tau} \tag {2.12}$$

由上式可见，PD 控制律中的比例项 $K_{p}$ 决定了系统的固有频率，即响应速度。

根据式（2.11），可得系统的阻尼比 $\xi$ 为

$$\xi = \frac {1 + K K _ {\mathrm{d}}}{2 \tau} \sqrt {\frac {\tau}{K K _ {\mathrm{p}}}} \tag {2.13}$$

由上式可见，系统的阻尼特性取决于微分项 $K_{d}$ 。

由上述分析可见：在 PD 控制中，当增加 $K_{p}$ 提高系统的响应速度时，系统的阻尼将下降。微分项 $K_{d}$ 起到增加阻尼的作用，提高了系统的相对稳定性。

![](image/6e3825510e34760d77cf9ef2bfa6ed62a2b084cd4238b7f1ca8e819d369fe154.jpg)
