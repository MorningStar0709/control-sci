# 10.4 平均化法

平均化法适用于形如

$$\dot {x} = \varepsilon f (t, x, \varepsilon)$$

的系统,其中 $\varepsilon$ 是一个很小的正参数, $f(t,x,\varepsilon)$ 对 t 的周期为 T, 也就是在定义域 $D \subset R^{n}$ 内

$$f (t + T, x, \varepsilon) = f (t, x, \varepsilon), \forall (t, x, \varepsilon) \in [ 0, \infty) \times D \times [ 0, \varepsilon_ {0} ]$$

这种方法就是通过一个“平均系统”的解逼近该系统的解。平均系统的解是通过在 $\varepsilon = 0$ 时对 $f(t,x,\varepsilon)$ 求平均得到的。为了导出平均化法，首先考察一个标量例子。

例10.7 设一阶线性系统为

$$\dot {x} = \varepsilon a (t, \varepsilon) x, \quad x (0) = \eta \tag {10.21}$$

其中， $\varepsilon$ 是正参数， $a$ 对其自变量足够光滑，且对于所有 $t \geqslant 0$ ，有 $a(t + T, \varepsilon) = a(t, \varepsilon)$ 。为了得到对于小的 $\varepsilon$ 成立的近似解，应用10.1节的扰动法。令 $\varepsilon = 0$ ，得到非扰动系统

$$\dot {x} = 0, \quad x (0) = \eta$$

它有一个常数解 $x_0(t) = \eta$ 。根据定理10.1，该逼近的误差在 $O(1)$ 时间区间上是 $O(\varepsilon)$ 。非扰动系统不满足定理10.2的条件。因此，不明确在大于 $O(1)$ 的时间区间上逼近是否有效。因为在本例中可以写出精确解的闭式表达式，所以我们通过直接计算来检验逼近误差。方程(10.21)的解为

$$x (t, \varepsilon) = \exp \left[ \varepsilon \int_ {0} ^ {t} a (\tau , \varepsilon) d \tau \right] \eta$$

因此，逼近误差为 $x(t,\varepsilon) - x_0(t) = \left\{\exp \left[\varepsilon \int_0^t a(\tau ,\varepsilon)d\tau \right] - 1\right\} \eta$

为了看出当 $t$ 增加时逼近误差的特性，需要计算上述表达式的积分项。 $a(t, \varepsilon)$ 是 $t$ 的周期函数，设其均值为

$$\bar {a} (\varepsilon) = \frac {1}{T} \int_ {0} ^ {T} a (\tau , \varepsilon) d \tau$$

$a(t,\varepsilon)$ 可以写为 $a(t,\varepsilon) = \bar{a} (\varepsilon) + [a(t,\varepsilon) - \bar{a} (\varepsilon)]$

括号里的项是 $t$ 的周期为 $T$ 的函数，均值为零。这样，积分

$$\int_ {0} ^ {t} [ a (\tau , \varepsilon) - \bar {a} (\varepsilon) ] d \tau \stackrel {\mathrm{def}} {=} \Delta (t, \varepsilon)$$

的周期为 $T$ ，且对于所有 $t \geqslant 0$ 是有界的。另一方面， $\bar{a}(\varepsilon)$ 一项在 $[0, t]$ 上的积分得到 $t \bar{a}(\varepsilon)$ ，这样有

$$x (t, \varepsilon) - x _ {0} (t) = \left\{\exp [ \varepsilon t \bar {a} (\varepsilon) ] \exp [ \varepsilon \Delta (t, \varepsilon) ] - 1 \right\} \eta$$

除了 $\bar{a} (\varepsilon) = 0$ 情况，逼近误差仅在 $O(1)$ 时间区间上是 $O(\varepsilon)$ 。仔细研究逼近误差可知，对 $x(t,\varepsilon)$ 较好的逼近是 $\exp [\varepsilon t\bar{a} (\varepsilon)]\eta$ ，甚至是 $\exp [\varepsilon t\bar{a}(0)]\eta$ ，因为 $\bar{a} (\varepsilon) - \bar{a} (0) = O(\varepsilon)$ 。试以 $\bar{x} (\varepsilon t) = \exp [\varepsilon t\bar{a}(0)]\eta$ 作为另一个逼近，逼近误差是
