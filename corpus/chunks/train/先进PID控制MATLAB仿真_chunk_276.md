$$S (s) = \lim _ {\Delta G _ {\mathrm{p}} (s) \rightarrow 0} \frac {\Delta G _ {\mathrm{uy}} (s) / G _ {\mathrm{uy}} (s)}{\Delta G _ {\mathrm{p}} (s) / G _ {\mathrm{p}} (s)} = \lim _ {\Delta G _ {\mathrm{p}} (s) \rightarrow 0} \frac {G _ {\mathrm{n}} (s) (1 - Q (s))}{G _ {\mathrm{n}} (s) + [ G _ {\mathrm{p}} (s) + \Delta G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) ] Q (s)} \tag {5.24}= \frac {G _ {\mathrm{n}} (s) (1 - Q (s))}{G _ {\mathrm{n}} (s) + [ G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) ] Q (s)}$$

在低频段，认为 $G_{\mathrm{p}}(s) = G_{\mathrm{n}}(s)$ ，将上式中的 $G_{\mathrm{p}}(s)$ 用 $G_{\mathrm{n}}(s)$ 来替代，则有

$$S (s) = 1 - Q (s) \tag {5.25}$$

则补灵敏度函数 $T(s)$ 为

$$T (s) = 1 - S (s) = Q (s) \tag {5.26}$$

则由鲁棒稳定性定理 $^{[4]}$ ，系统鲁棒稳定的充分必要条件是

$$\left\| \Delta (\mathrm{j} \omega) T (\mathrm{j} \omega) \right\| _ {\infty} = \left\| \Delta (\mathrm{j} \omega) Q (\mathrm{j} \omega) \right\| _ {\infty} \leqslant 1 \tag {5.27}$$

式中， $\|\cdot\|_{\infty}$ 为 $H_{\infty}$ 范数。

通过 $Q(s)$ 的设计，可实现鲁棒性要求。式（5.27）可为

$$\left\| Q (\mathrm{j} w) \right\| _ {\infty} \leqslant \frac {1}{\| \Delta (\mathrm{j} w) \| _ {\infty}} \tag {5.28}$$

式（5.28）是 $Q(s)$ 设计的基础。以 $Q(s)=\frac{3\tau s+1}{\tau^{3}s^{3}+3\tau^{2}s^{2}+3\tau s+1}$ 为例，假设延迟是唯一不

确定部分，此时取 $G_{\mathrm{p}}(s) = \frac{B(s)}{A(s)}\mathrm{e}^{-\tau s}$ ， $G_{\mathrm{n}}(s) = \frac{B(s)}{A(s)}$ ， $\Delta (s) = \mathrm{e}^{-\tau s} - 1$ ，分别取 $\tau_{1} = 0.00035$ 、 $\tau_{2} = 0.00125$ 和 $\tau_{3} = 0.00425$ ，对应的低通滤波器分别为 $Q_{1}(s)$ 、 $Q_{2}(s)$ 和 $Q_{3}(s)$ ，仿真程序见 chap5\_5Q.m，仿真结果如图 5-13 所示。可见 $Q_{2}(s)$ 和 $Q_{3}(s)$ 满足式（5.28）要求。

![](image/026d94e0ae0b06a39800646c9e67d96d724354c4b161cd543cafdc53ccf4e16d.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Magnitude (dB) - 1/Delta | Magnitude (dB) - Q1 | Magnitude (dB) - Q2 | Magnitude (dB) - Q3 | Phase (deg) - 1/Delta | Phase (deg) - Q1 | Phase (deg) - Q2 | Phase (deg) - Q3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10^1 | ~50 | ~-50 | ~-50 | ~-50 | ~-180 | ~-180 | ~-180 | ~-180 |
| 10^2 | ~20 | ~-20 | ~-20 | ~-20 | ~-360 | ~-360 | ~-360 | ~-360 |
| 10^3 | ~5 | ~-5 | ~-5 | ~-5 | ~-720 | ~-720 | ~-720 | ~-720 |
| 10^4 | ~0 | ~0 | ~0 | ~0 | ~-540 | ~-540 | ~-540 | ~-540 |
| 10^5 | ~-50 | ~-50 | ~-50 | ~-50 | ~-720 | ~-720 | ~-720 | ~-720 |
</details>

图5-13 $Q(s)$ 的选择

![](image/5487c74ccdb953be6a424cf45c386ac23728da3742ea52786d477227ab606483.jpg)
