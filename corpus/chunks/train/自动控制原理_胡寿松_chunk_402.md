# (2) 采样信号的频谱

由于采样信号的信息并不等于连续信号的全部信息,所以采样信号的频谱与连续信号的频谱相比,要发生变化。研究采样信号的频谱,目的是找出 $E^{*}(s)$ 与 $E(s)$ 之间的相互联系。

式(7-2)表明,理想单位脉冲序列 $\delta_{T}(t)$ 是一个周期函数,可以展开为如下傅氏级数形式:

$$\delta_ {T} (t) = \sum_ {n = - \infty} ^ {\infty} c _ {n} \mathrm{e} ^ {\mathrm{j} n \omega_ {s} t} \tag {7-6}$$

式中， $\omega_{s} = 2\pi /T$ ，为采样角频率； $c_{n}$ 是傅氏系数，其值为

$$c _ {n} = \frac {1}{T} \int_ {- T / 2} ^ {T / 2} \delta_ {T} (t) \mathrm{e} ^ {- \mathrm{j} n \omega_ {s} t} \mathrm{d} t$$

由于在 $[-T / 2, T / 2]$ 区间中， $\delta_T(t)$ 仅在 $t = 0$ 时有值，且 $\mathrm{e}^{-\mathrm{j}\omega_t t}|_{t = 0} = 1$ ，所以

$$c _ {n} = \frac {1}{T} \int_ {0 _ {-}} ^ {0 _ {+}} \delta (t) \mathrm{d} t = \frac {1}{T} \tag {7-7}$$

将式(7-7)代入式(7-6)，得

$$\delta_ {T} (t) = \frac {1}{T} \sum_ {n = - \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{j} n \omega_ {s} t} \tag {7-8}$$

再把式(7-8)代入式(7-1)，有

$$e ^ {*} (t) = \frac {1}{T} \sum_ {n = - \infty} ^ {\infty} e (t) \mathrm{e} ^ {\mathrm{j} n \omega_ {s} t} \tag {7-9}$$

上式两边取拉氏变换，由拉氏变换的复数位移定理，得到

$$E ^ {*} (s) = \frac {1}{T} \sum_ {n = - \infty} ^ {\infty} E (s + j n \omega_ {s}) \tag {7-10}$$

式(7-10)在描述采样过程的性质方面是非常重要的,因为该式提供了理想采样器在频域中的特点。在式(7-10)中,如果 $E^{*}(s)$ 没有右半 s 平面的极点,则可令 $s=j\omega$ ,得到采样信号 $e^{*}(t)$ 的傅氏变换

$$E ^ {*} (\mathrm{j} \omega) = \frac {1}{T} \sum_ {n = - \infty} ^ {\infty} E [ \mathrm{j} (\omega + n \omega_ {s}) ] \tag {7-11}$$

其中， $E(\mathrm{j}\omega)$ 为连续信号 $e(t)$ 的傅氏变换。

一般说来，连续信号 $e(t)$ 的频谱 $\left|E(\mathrm{j}\omega)\right|$ 是单一的连续频谱，如图7-12所示，其中 $\omega_{h}$ 为连续频谱 $\left|E(\mathrm{j}\omega)\right|$ 中的最大角频率；而采样信号 $e^{*}(t)$ 的频谱 $\left|E^{*}(\mathrm{j}\omega)\right|$ ，则是以采样角频率 $\omega_{s}$ 为周期的无穷多个频谱之和，如图7-13所示。在图7-13中， $n = 0$ 的频谱称为采样频谱的主分量，如曲线1所示，它与连续频谱 $\left|E(\mathrm{j}\omega)\right|$ 形状一致，仅在幅值上变化为 $1 / T$ ；其余频谱 $(n = \pm 1, \pm 2, \dots)$ 都是由于采样而引起的高频频谱，称为采样频谱的补分量，如曲线2所示。图7-13表明的是采样角频率 $\omega_{s}$ 大于两倍 $\omega_{h}$ 这一情况。如果加大采样周期 $T$ ，采样角频率 $\omega_{s}$ 相应减小，当 $\omega_{s} < 2\omega_{h}$ 时，采样频谱中的补分量相互交叠，致使采样器输出信号发生畸变，如图7-14所示。在这种情况下，就是用图7-15所示的理想滤波器也无法恢复原来连续信号的频谱。因此不难看出，要想从采样信号 $e^{*}(t)$ 中完全复现出采样前的连续信号 $e(t)$ ，对采样角频率 $\omega_{s}$ 应有一定的要求。

![](image/c5305274dfbcf68ae49bc0e3a8e051b085f1c7f0a8267ebdbecc6892e9bb59fe.jpg)  
图 7-12 连续信号频谱

![](image/abcbc3663392d56adb5a889a7eeafc81d5b6ffa6148d8507c0a31bd831ce8b20.jpg)

<details>
<summary>line</summary>

| Frequency (ω) | Magnitude | Label |
| --- | --- | --- |
| -3ωs | ~0 |  |
| -2ωs | ~0 | 2 |
| -ωs | ~0 |  |
| 0 | ~0 | 1/1T |
| -ωh | ~0 |  |
| ωh | ~0 |  |
| ωs | ~0 |  |
| 2ωs | ~0 | 2 |
| 3ωs | ~0 |  |
</details>

图 7-13 采样信号频谱( $\omega_{s}>2\omega_{h}$ )

![](image/e7ddb768e38b0b5d01d61d0190d1cf63406e0e39677870dbf217b461033ed240.jpg)  
图 7-14 采样信号频谱( $\omega_{s}<2\omega_{h}$ )

![](image/c17a49afa039b0c66089acc5732f9fa775fec8372f847feecabff87c998167f5.jpg)  
图 7-15 理想滤波器的频率特性
