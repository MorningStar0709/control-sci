# (1)无源超前网络

图 6-12 是无源超前网络的电路图及其零、极点分布图。如果输入信号源的内阻为零，且输出端的负载阻抗为无穷大，则超前网络的传递函数可写为

$$a G _ {c} (s) = \frac {1 + a T s}{1 + T s} \tag {6-18}$$

式中 $a = \frac{R_1 + R_2}{R_2} > 1, T = \frac{R_1 R_2}{R_1 + R_2} C$

通常， $a$ 称为分度系数， $T$ 叫做时间常数。由式(6-18)见，采用无源超前网络(图 6-12(a))进行串联校正时，整个系统的开环增益要下降为原来的 $\frac{1}{a}$ ，因此需要提高放大器增益加以补偿。超前网络的零、极点分布图如图 6-12(b) 所示。由于 $a > 1$ ，故超前网络的负实零点总是位于其负实极点之右，两者之间的距离由常数 $a$ 决定。改变 $a$ 和 $T$ 的数值，超前网络的零、极点可在 $s$ 平面的负实轴上任意移动。

![](image/a745705afc753ec679e7b55b17b7773da6037cdfcd0bdf7e181aa0b904d129a7.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with resistors R1 and R2, capacitor C, and input/output terminals U1 and U2
</details>

(a)

![](image/600659f327db0d55f103ebaa73be6aae9c9a163a3fcef0325e45cfd6a23f4c88.jpg)

<details>
<summary>text_image</summary>

-1/T
-1/aT
j
0
</details>

(b)   
图 6-12 无源超前网络(a)及其零、极点分布(b)

根据式(6-18)，可以画出无源超前网络 $aG_{c}(s)$ 的对数频率特性，如图6-13(a)所示。显然，超前网络对频率在 $1 / aT$ 至 $1 / T$ 之间的输入信号有明显的微分作用，在该频率范围内，输出信号相角比输入信号相角超前，超前网络的名称由此而得。图6-13(a)表明，在最大超前角频率 $\omega_{m}$ 处，具有最大超前角 $\varphi_{m}$ ，且 $\omega_{m}$ 正好处于频率 $1 / aT$ 和 $1 / T$ 的几何中心。证明如下：

![](image/2d25da59da8595651dc9ff9b4821e094d247e35efb7ca4e1cc9505d43114eb48.jpg)  
图 6-13 无源超前网络特性

超前网络式(6-18)的相角为

$$\varphi_ {c} (\omega) = \arctan a T \omega - \arctan T \omega = \arctan \frac {(a - 1) T \omega}{1 + a T ^ {2} \omega^ {2}} \tag {6-19}$$

将上式对 $\omega$ 求导并令其为零, 得最大超前角频率

$$\omega_ {m} = \frac {1}{T \sqrt {a}} \tag {6-20}$$

将上式代入式(6-19)，得最大超前角

$$\varphi_ {m} = \arctan \frac {a - 1}{2 \sqrt {a}} = \arcsin \frac {a - 1}{a + 1} \tag {6-21}$$

上式表明：最大超前角 $\varphi_{m}$ 仅与分度系数 $a$ 有关。 $a$ 值选得越大，超前网络的微分效应越强。为了保持较高的系统信噪比，实际选用的 $a$ 值一般不超过20。此外，由图6-13(a)可以明显看出 $\omega_{m}$ 处的对数幅频值

$$L _ {c} (\omega_ {m}) = 2 0 \lg | a G _ {c} (\mathrm{j} \omega_ {m}) | = 1 0 \lg a \tag {6-22}$$

a 与 $\varphi_{m}$ 及 10 lg a 的关系曲线如图 6-13(b) 所示。

设 $\omega_{1}$ 为频率 1/aT 及 1/T 的几何中心，则应有

$$\lg \omega_ {1} = \frac {1}{2} \left(\lg \frac {1}{a T} + \lg \frac {1}{T}\right)$$

解得 $\omega_{1}=1/T\sqrt{a}$ ，正好与式(6-20)完全相同，故最大超前角频率 $\omega_{m}$ 确是 1/aT 和 1/T 的几何中心。
