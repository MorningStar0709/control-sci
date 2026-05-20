$$
\begin{array}{l} x (t, \varepsilon) - \bar {x} (\varepsilon t) = \left\{\exp [ \varepsilon t \bar {a} (\varepsilon) ] \exp [ \varepsilon \Delta (t, \varepsilon) ] - \exp [ \varepsilon t \bar {a} (0) ] \right\} \eta \\ = \exp [ \varepsilon t \bar {a} (0) ] \left\{\exp \left[ \varepsilon t (\bar {a} (\varepsilon) - \bar {a} (0)) \right] \exp \left[ \varepsilon \Delta (t, \varepsilon) \right] - 1 \right\} \eta \\ \end{array}
$$

注意到对于任意有限的 $b > 0$ ，有

$$\exp [ \varepsilon \Delta (t, \varepsilon) ] = 1 + O (\varepsilon), \forall t \geqslant 0\exp [ \varepsilon t (\bar {a} (\varepsilon) - \bar {a} (0)) ] = \exp [ t O \left(\varepsilon^ {2}\right) ] = 1 + O (\varepsilon), \forall t \in [ 0, b / \varepsilon ]\exp [ \varepsilon t \bar {a} (0) ] = O (1), \forall t \in [ 0, b / \varepsilon ]$$

可以得出,在数量级为 $O(1/\varepsilon)$ 的时间区间上有 $x(t,\varepsilon)-\bar{x}(\varepsilon t)=O(\varepsilon)$ 。这样就证实了逼近 $\bar{x}(\varepsilon t)=\exp[\varepsilon t\bar{a}(0)]\eta$ 是比 $x_{0}(t)=\eta$ 更好的假设。注意， $\bar{x}(\varepsilon t)$ 是平均系统

$$\dot {x} = \varepsilon \bar {a} (0) x, \quad x (0) = \eta \tag {10.22}$$

的解,其右边是方程(10.21)的右边在 $\varepsilon=0$ 条件下的平均。

在这个例子中,利用方程(10.21)精确解的闭式表达式得出了平均系统(10.22),这种闭式表达式仅在非常特殊的情况下才成立,但平均化法的可取性与该例的特殊性无关。现在我们用不同的方式解释平均化这一概念。将方程(10.21)右边乘以一个正常数 $\varepsilon$ ,当 $\varepsilon$ 很小时,解x随着t相对于 $a(t,\varepsilon)$ 的周期性波动“缓慢地”变化。直觉上讲,显然如果系统的响应比激励慢得多,则响应主要由激励的平均决定。这种直觉来源于线性系统理论,我们知道,如果系统带宽比输入带宽小得多,则系统将作为一个低通滤波器,抑制输入信号的高频分量。如果方程(10.21)的解主要由波动 $a(t,\varepsilon)$ 的平均决定,为了获得 $O(\varepsilon)$ 逼近,我们有理由用函数 $a(t,\varepsilon)$ 的平均代替函数 $a(t,\varepsilon)$ 。这种平均化法的二时间尺度(two-time-scale)解释不依赖于例10.7的特殊性,也不依赖于系统的线性化。这是一个似是而非的概念,出现在更一般的结构中,在本章其余部分将看到这一点。

设系统为

$$\dot {x} = \varepsilon f (t, x, \varepsilon) \tag {10.23}$$

对于每个紧集 $D_0 \subset D$ ，以及 $(t, x, \varepsilon) \in [0, \infty) \times D_0 \times [0, \varepsilon_0]$ ， $f$ 及其关于 $(x, \varepsilon_0)$ 的一阶和二阶偏导数连续且有界，其中 $D \subset R^n$ 是定义域。此外， $f(t, x, \varepsilon)$ 对于 $t$ 的周期为 $T, T > 0, \varepsilon$ 为正。联立方程(10.23)和自治平均系统

$$\dot {x} = \varepsilon f _ {\mathrm{av}} (x) \tag {10.24}$$

其中 $f_{\mathrm{av}}(x)=\frac{1}{T}\int_{0}^{T}f(\tau,x,0)d\tau$ (10.25)

平均化法的基本问题是确定在什么意义下自治系统(10.24)的特性逼近非自治系统(10.23)的特性。我们用变量代换通过证明非自治系统(10.23)可表示为自治系统(10.24)的扰动来说明这个问题。定义

$$u (t, x) = \int_ {0} ^ {t} h (\tau , x) d \tau \tag {10.26}$$
