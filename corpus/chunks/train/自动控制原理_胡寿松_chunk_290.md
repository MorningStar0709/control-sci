-1
0
ω
j
</details>

(b) $K_{1}<K<K_{2}$

![](image/aa6412805f784d67945d30f94579f3d89b629408117ba542bdb3b00dbf04737a.jpg)

<details>
<summary>text_image</summary>

-1
0
ω
j
</details>

(c) $K_{2}<K<K_{3}$

![](image/44bdd4882ccc7d54f1f8f04688162b036612c571d2843cb2be6d26100a5a0843.jpg)

<details>
<summary>text_image</summary>

j
-1 0
ω
</details>

(d) $K > K_{3}$   
图5-35 例5-9系统在不同 $K$ 值条件下的开环幅相曲线及 $\Gamma_G$ 曲线

例 5-10 已知延迟系统开环传递函数为

$$G (s) H (s) = \frac {2 \mathrm{e} ^ {- s}}{s + 1}, \qquad \tau > 0$$

试根据奈氏判据确定系统闭环稳定时，延迟时间 $\tau$ 值的范围。

解 由图5-26可知，延迟系统开环幅相曲线即半闭合曲线 $\Gamma_{GH}$ 为螺旋线，且为顺时针方向，若开环幅相曲线与 $(-1, j0)$ 点左侧的负实轴有 $l$ 个交点，则 $\Gamma_{GH}$ 包围 $(-1, j0)$ 点的圈数为 $-2l$ ，由于 $P = 0$ ，故 $Z = 2l$ ，系统闭环不稳定。若系统闭环稳定，则必须有 $l = 0$ 。设 $\omega_x$ 为开环幅相曲线穿越负实轴时的频率，有

$$\varphi (\omega_ {x}) = - \pi \omega_ {x} - \arctan \omega_ {x} = - (2 k + 1) \pi ; \quad k = 0, 1, 2, \dots$$

鉴于

$$A (\omega_ {x}) = \frac {2}{\sqrt {1 + \omega_ {x} ^ {2}}}$$

当 $\omega_{x}$ 增大时， $A(\omega_{x})$ 减小。而在频率 $\omega$ 为最小的 $\omega_{xm}$ 时，开环幅相曲线第一次穿过负实轴，因此 $\omega_{xm}$ 求得为

$$\varphi \left(\omega_ {x m}\right) = - \tau \omega_ {x m} - \arctan \omega_ {x m} = - \pi$$

此时 $A(\omega_{xm})$ 达到最大，为使 $l = 0$ ，必须使 $A(\omega_{xm}) < 1$ ，即

$$\omega_ {x m} > \sqrt {3}$$

由 $\varphi (\omega_x) = -(2k + 1)\pi$ 解得

$$\tau = [ (2 k + 1) \pi - \arctan \omega_ {x} ] / \omega_ {x} > 0$$

注意到 $\frac{\mathrm{d}\tau}{\mathrm{d}\omega_x} = \frac{-\left[(2k + 1)\pi - \arctan\omega_x + \frac{\omega_x}{1 + \omega_x^2}\right]}{\omega_x^2} < 0$

$\tau$ 为 $\omega_{x}$ 的减函数，因此 $\omega_{xm}$ 亦为 $\tau$ 的减函数。当 $\tau = (\pi - \arctan \sqrt{3}) / \sqrt{3}$ 时， $\omega_{xm} = \sqrt{3}$ ，系统临界稳定；当 $\tau > (\pi - \arctan \sqrt{3}) / \sqrt{3}$ 时， $\omega_{xm} < \sqrt{3}$ ，系统不稳定。故系统闭环稳定时 $\tau$ 值的范围应为

$$\tau < \frac {\pi - \arctan \sqrt {3}}{\sqrt {3}} = \frac {2}{3 \sqrt {3}} \pi$$
