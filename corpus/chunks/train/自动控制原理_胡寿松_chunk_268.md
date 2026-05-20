# (4) 对数幅频渐近特性曲线

在控制工程中，为简化惯性环节、一阶微分环节、振荡环节和二阶微分环节的对数幅频曲线的作图，常用低频和高频渐近线近似表示对数幅频曲线，称之为对数幅频渐近特性曲线。

对于惯性环节，对数幅频特性为

$$L (\omega) = - 2 0 \lg \sqrt {1 + \omega^ {2} T ^ {2}} \tag {5-40}$$

当 $\omega \ll \frac{1}{T}$ 时， $\omega^2 T^2 \approx 0$ ，有

$$L (\omega) \approx - 2 0 \lg 1 = 0 \tag {5-41}$$

当 $\omega \gg \frac{1}{T}$ 时， $\omega^2 T^2 \gg 1$ ，有

$$L (\omega) \approx - 2 0 \mathrm{lg} \omega T \tag {5-42}$$

因此惯性环节的对数幅频渐近特性为

$$
L _ {a} (\omega) = \left\{ \begin{array}{l l} 0, & \omega <   \frac {1}{T} \\ - 2 0 \lg \omega T, & \omega > \frac {1}{T} \end{array} \right. \tag {5-43}
$$

惯性环节的对数幅频渐近特性曲线如图 5-15 所示, 低频部分是零分贝线, 高频部分是斜率为 -20dB/dec 的直线, 两条直线交于 $\omega=\frac{1}{T}$ 处, 称频率 $\frac{1}{T}$ 为惯性环节的交接频率。用渐近特性近似表示对数幅频特性存在误差

$$\Delta L (\omega) = L (\omega) - L _ {a} (\omega) \tag {5-44}$$

误差曲线如图 5-16 所示。在交接频率处误差最大，约为 -3dB。根据误差曲线，可修正渐近特性曲线获得准确曲线。

由于非最小相位惯性环节的对数幅频特性与惯性环节相同，故其对数幅频渐近特性亦相同。根据一阶微分环节和非最小相位一阶微分环节的对数幅频特性相等，且与惯性环节对数幅频特性互为倒数的特点，可知一阶微分环节和非最小相位一阶微分环节与惯性环节的对数幅频渐近

![](image/76fde0db9649a2bc6b8d609ba113d2bb94b169a8ddf66a60405ab69cf713d05d.jpg)

<details>
<summary>line</summary>

| ωT | Lσ(ω)/dB |
| --- | --- |
| 0 | 0 |
| 10 | -20 |
</details>

图 5-15 惯性环节的对数幅频渐近特性曲线  
$\Delta L(\omega) / \mathrm{dB}$   
![](image/dfb36972e4fdb958b72921828ed1a636da8626b0d21c603fecf8988f6b998548.jpg)

<details>
<summary>line</summary>

| ωT | dB |
| --- | --- |
| 0.1 | 0.0 |
| 0.5 | -1.0 |
| 1.0 | -3.0 |
| 2.0 | -1.0 |
| 5.0 | 0.0 |
</details>

图 5-16 惯性环节的误差曲线

特性曲线以 0dB 线互为镜像。

振荡环节的对数幅频特性为

$$L (\omega) = - 2 0 \lg \sqrt {\left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) ^ {2} + 4 \zeta^ {2} \frac {\omega^ {2}}{\omega_ {n} ^ {2}}} \tag {5-45}$$

当 $\omega \ll \omega_{n}$ 时， $L(\omega) \approx 0$ ，低频渐近线为 $0\mathrm{dB}$ 线。而当 $\omega \gg \omega_{n}$ 时， $L(\omega) = -40\lg \frac{\omega}{\omega_{n}}$ ，高频渐近线为过 $(\omega_{n}, 0)$ 点，斜率为 $-40\mathrm{dB / dec}$ 的直线。振荡环节的交接频率为 $\omega_{n}$ ，对数幅频渐近特性为

$$
L _ {a} (\omega) = \left\{ \begin{array}{l l} 0, & \omega <   \omega_ {n} \\ - 4 0 \lg \frac {\omega}{\omega_ {n}}, & \omega > \omega_ {n} \end{array} \right. \tag {5-46}
$$

由于 $L_{a}(\omega)$ 与阻尼比 $\zeta$ 无关，用渐近线近似表示对数幅频曲线存在误差，误差的大小不仅和 $\omega$ 有关，而且也和 $\zeta$ 有关，误差曲线 $\Delta L(\omega, \zeta)$ 为一曲线簇，如图5-17所示。根据误差曲线可以修正渐近特性曲线而获得准确曲线。

![](image/b72cf3de0a2b9ad1896ecc64375c75d649dc4eae72aa91357a29407f23121f8c.jpg)

<details>
<summary>line</summary>
