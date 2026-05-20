# 4.7 扩张状态观测器与系统的时间尺度

大量的数值仿真试验表明,对被观测的对象

$$
\left\{ \begin{array}{l} x _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}) + b u \\ y = x _ {1} \end{array} \right.
$$

来说，在估计它的状态和总和扰动的扩张状态观测器中，当非线性函数 $\operatorname{fal}(\varepsilon, \alpha_{i}, \delta)$ 中的参数 $\alpha_{i} = 1/2^{i-1}, \delta = h$ 确定时，参数 $\beta_{0i}$ 基本上是与积分步长 h 有关，而积分步长 h 决定于被估计对象的函数 f 的作用范围，即加速度函数 f 的作用范围大小。如果系统的变化比较灵敏而且快,那么要描述快速灵敏变化的运动,当然需要比较小的积分步长 h 了.系统变化快慢程度是与加速度 f 的大小有关,因而加速度 f 的大小决定着计算此系统运动的积分步长 h.

对系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = M \mathrm{sign} (\sin (\omega t)) \\ y = x _ {1} \end{array} \right. \tag {4.7.1}
$$

我们用扩张状态观测器

$$
\left\{ \begin{array}{l} e = z _ {1} - y \\ \dot {z} _ {1} = z _ {2} - \beta_ {0 1} e \\ \dot {z} _ {2} = z _ {3} - \beta_ {0 2} \text {fal} (e, 0. 5, \delta) + b u \\ \dot {z} _ {3} = - \beta_ {0 3} \text {fal} (e, 0. 0 5, \delta) \end{array} \right. \tag {4.7.2}
$$

来跟踪其状态和被扩张的状态 $x_{3} = M\mathrm{sign}(\sin (\omega t))$ 的情况来探讨加速度的幅值 $M$ 和积分步长 $h$ 之间的关系以及步长 $h$ 和参数 $\beta_{01},\beta_{02},\beta_{03}$ 之间的关系.这里将用性能指标

$$J = \frac {1}{M} \int_ {0} ^ {T} | x _ {3} (t) - z _ {3} (t) | \mathrm{d} t \tag {4.7.3}$$

的大小来衡量跟踪的好坏.

在数字积分中采用最简单的微分近似

$$\dot {z} (t) = \frac {z (t + h) - z (t)}{h}$$

把它代到式(4.4.2)，得扩张状态观测器如下递推公式

$$
\left\{ \begin{array}{l} e = z _ {1} - y, \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 5, \delta), \mathrm{fe} _ {2} = \operatorname{fal} (e, 0. 2 5, \delta) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} \mathrm{fe} _ {1} + b u\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {2}\right) \end{array} \right. \tag {4.7.4}
$$

这是把微分方程(4.7.2)用欧拉法积分的递推公式.

下面用扩张状态观测器(4.7.4)来跟踪系统(4.7.1)的状态 $x_{1}(t),x_{2}(t)$ 和被扩张的状态 $x_{3}(t)=M\mathrm{sign}(\sin(\omega t))$ 的情况.

先固定 $\omega = 0.005$ fal函数中的 $\delta = h$ . 然后考察步长 $h = 1$ 时, 扩张状态观测器(4.7.4)能跟踪多大 $M$ 的系统(4.7.1)的轨线和被扩张的状态? 能够跟踪这个轨线时的扩张状态观测器(4.7.4)的参数 $\beta_{01}, \beta_{02}, \beta_{03}$ 是多少?

按上述性能指标优化的结果为

$$h = 1. 0, \delta = h, \beta_ {0 1} = 1. 0, \beta_ {0 2} = 0. 5 5, \beta_ {0 3} = 0. 1.$$

而在这个参数下幅值 M 和指标 J 之间关系见表 4.7.1.

表4.7.1
