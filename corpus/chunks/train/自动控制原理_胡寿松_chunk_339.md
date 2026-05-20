# (2) 无源滞后网络

无源滞后网络的电路图如图 6-14(a) 所示。如果输入信号源的内阻为零，负载阻抗为无穷大，滞后网络的传递函数为

$$G _ {c} (s) = \frac {1 + b T s}{1 + T s} \tag {6-23}$$

![](image/e8a265a3716025b81e0358e078d3d45718073d890017d5c3700a2ca37973f619.jpg)

<details>
<summary>text_image</summary>

R₁
U₁
R₂
C
U₂
(a)
</details>

![](image/d2fecc75544de216f525d4bc5e3454a265f60f3410f53357dab46afcde5372ea.jpg)

<details>
<summary>line</summary>

| Frequency ω | L(ω) | φ(ω) |
| --- | --- | --- |
| 0 | 0 | 0° |
| 1/T | 1/T | ~-5° |
| ωₘ | 1/bT | ~-85° |
| 201gb | 201gb | ~-5° |
| Phase Difference | -20dB/dec | -90° |
| Phase Difference | φₙ | ~-5° |
(b)
</details>

图 6-14 无源滞后网络(a)及其特性(b)

式中 $b = \frac{R_2}{R_1 + R_2} < 1, T = (R_1 + R_2)C$

通常，b 称为滞后网络的分度系数，表示滞后深度。

无源滞后网络的对数频率特性如图6-14(b)所示。由图可见，滞后网络在频率 $1 / T$ 至 $1 / bT$ 之间呈积分效应，而对数相频特性呈滞后特性。与超前网络类似，最大滞后角 $\varphi_{m}$ 发生在最大滞后角频率 $\omega_{m}$ 处，且 $\omega_{m}$ 正好是 $1 / T$ 与 $1 / bT$ 的几何中心。计算 $\omega_{m}$ 及 $\varphi_{m}$ 的公式分别为

$$\omega_ {m} = \frac {1}{T \sqrt {b}} \tag {6-24}\varphi_ {m} = \arcsin \frac {1 - b}{1 + b} \tag {6-25}$$

图 6-14(b) 还表明, 滞后网络对低频有用信号不产生衰减, 而对高频噪声信号有削弱作用, b 值越小, 通过网络的噪声电平越低。

采用无源滞后网络进行串联校正时，主要是利用其高频幅值衰减的特性，以降低系统的开环截止频率，提高系统的相角裕度。因此，力求避免最大滞后角发生在已校正系统开环截止频率 $\omega_{c}^{\prime\prime}$ 附近。选择滞后网络参数时，通常使网络的交接频率1/bT远小于 $\omega_{c}^{\prime\prime}$ ，一般取

$$\frac {1}{b T} = \frac {\omega_ {c} ^ {\prime \prime}}{1 0} \tag {6-26}$$

此时，滞后网络在 $\omega_{c}^{\prime \prime}$ 处产生的相角滞后按下式确定：

$$\varphi_ {c} \left(\omega_ {c} ^ {\prime \prime}\right) = \arctan b T \omega_ {c} ^ {\prime \prime} - \arctan T \omega_ {c} ^ {\prime \prime}$$

由两角和的三角函数公式, 得

$$\tan \varphi_ {c} (\omega_ {c} ^ {\prime \prime}) = \frac {b T \omega_ {c} ^ {\prime \prime} - T \omega_ {c} ^ {\prime \prime}}{1 + b T ^ {2} (\omega_ {c} ^ {\prime \prime}) ^ {2}}$$

代入式(6-26)及b<1关系，上式可化简为

$$\varphi_ {c} \left(\omega_ {c} ^ {\prime \prime}\right) \approx \arctan [ 0. 1 (b - 1) ] \tag {6-27}$$

b 与 $\varphi_{c}(\omega_{c}^{\prime\prime})$ 和 20lgb 的关系曲线如图 6-15 所示。为便于使用，图 6-15 曲线画在对数坐标系中。
