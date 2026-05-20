# 11.4 慢流形和快流形

本节给出方程(11.1)和方程(11.2)的解的二时间尺度特性的几何解释,该解是用 $R^{n+m}$ 上的轨线表示的。为了运用不变流形的概念②,我们只讨论自治系统。为了进一步简化概念,取f和g与 $\varepsilon$ 无关。这样,就可以考虑奇异扰动系统(11.1)\~(11.2)的简单形式

$$\dot {x} = f (x, z) \tag {11.26}\varepsilon \dot {z} = g (x, z) \tag {11.27}$$

设 $z = h(x)$ 是 $0 = g(x,z)$ 的孤立根，并假设其满足定理11.1的条件。方程 $z = h(x)$ 描述了一个在 $(x,z)$ 的 $n + m$ 维状态空间中的 $n$ 维流形，它是系统

$$\dot {x} = f (x, z) \tag {11.28}0 = g (x, z) \tag {11.29}$$

的一个不变流形,因为方程(11.28)和方程(11.29)的始于流形 $z=h(x)$ 的轨线在所有未来时刻(解在其内有定义)都将保持在该流形内。系统在此流形内的运动可用降阶模型

$$\dot {x} = f (x, h (x))$$

描述。定理11.1表明方程(11.26)和方程(11.27)的始于 $z = h(x)$ 的 $O(\varepsilon)$ 邻域内的轨线，继续保留在 $z = h(x)$ 的 $O(\varepsilon)$ 邻域内。由此引发了下列问题：当 $\varepsilon > 0$ 时是否有类似于不变流形 $z = h(x)$ 的流形存在？也就是说在定理11.1假设的条件下，方程(11.26)和方程(11.27)在 $z = h(x)$ 的 $O(\varepsilon)$ 邻域内有一个邻近的不变流形。对于方程(11.26)和方程(11.27)，寻找形如

$$z = H (x, \varepsilon) \tag {11.30}$$

的不变流形,其中 H 是 x 和 $\varepsilon$ 的足够光滑(即足够多次连续可微)函数。表达式(11.30)在 $(x,z)$ 的 $n+m$ 维状态空间上定义了一个与 $\varepsilon$ 有关的 n 维流形。因为 $z=H(x,\varepsilon)$ 是方程(11.26)\~方程(11.27)的不变流形,因此一定有

$$z (0, \varepsilon) - H (x (0, \varepsilon), \varepsilon) = 0 \Rightarrow z (t, \varepsilon) - H (x (t, \varepsilon), \varepsilon) \equiv 0, \forall t \in J \subset [ 0, \infty)$$

其中， $J$ 是解 $[x(t,\varepsilon),z(t,\varepsilon)]$ 存在的整个时间区间。将方程(11.30)两边对 $t$ 进行微分，再乘以 $\varepsilon$ ，并分别把方程(11.26)、方程(11.27)和方程(11.30)中的 $\dot{x},\varepsilon \dot{z}$ 和 $z$ 代入，得流形条件

$$0 = g (x, H (x, \varepsilon)) - \varepsilon \frac {\partial H}{\partial x} f (x, H (x, \varepsilon)) \tag {11.31}$$

在所讨论的区域内及所有 $\varepsilon \in [0, \varepsilon_0]$ , $H(x, \varepsilon)$ 都必须满足该流形条件。当 $\varepsilon = 0$ 时，偏微分方程(11.31)退化为 $0 = g(x, H(x, 0))$

它表明 $H(x,0) = h(x)$ 。由于 $0 = g(x,0)$ 可能有多个孤立根 $z = h(x)$ ，故可能要在每个根的邻域内都寻找方程(11.26)\~方程(11.27)的一个不变流形。可以证明①，存在 $\varepsilon^{*} > 0$ 和对于所有 $\varepsilon \in [0,\varepsilon^{*}]$ 都满足流形条件(11.31)的函数 $H(x,\varepsilon)$ ，且有

$$H (x, \varepsilon) - h (x) = O (\varepsilon)$$

其中 $x$ 有界。不变流形 $z = H(x, \varepsilon)$ 称为方程(11.26)～方程(11.27)的慢流形。每个慢流形都对应于一个慢模型 $\dot{x} = f(x, H(x, \varepsilon))$ (11.32)

它精确地描述了系统在流形上的运动。

在多数情况下,不能精确地解出流形条件(11.31),但可以用在 $\varepsilon=0$ 展开的泰勒级数任意近地逼近 $H(x,\varepsilon)$ 。该逼近的步骤是,首先将 $H(x,\varepsilon)$ 的泰勒级数,即

$$H (x, \varepsilon) = H _ {0} (x) + \varepsilon H _ {1} (x) + \varepsilon^ {2} H _ {2} (x) + \dots$$
