# 1. 控制系统的频带宽度

设 $\Phi (\mathrm{j}\omega)$ 为系统闭环频率特性，当闭环幅频特性下降到频率为零时的分贝值以下3分贝，即 $0.707|\Phi (\mathrm{j}0)|(\mathrm{dB})$ 时，对应的频率称为带宽频率，记为 $\omega_{b}$ 。即当 $\omega >\omega_{b}$ 时

$$2 0 \lg | \Phi (\mathrm{j} \omega) | < 2 0 \lg | \Phi (\mathrm{j} 0) | - 3 \tag {5-88}$$

![](image/fec91238de7c89369b1ffb90beb9a084ad4f38e4ebb27cc3a99e573e579d94e8.jpg)

<details>
<summary>line</summary>

| Frequency (ω) | Gain (dB) |
| --- | --- |
| 0 | 0 |
| ω_b | 3 |
</details>

图 5-44 系统带宽频率与带宽

而频率范围 $(0, \omega_{b})$ 称为系统的带宽，如图5-44所示。带宽定义表明，对高于带宽频率的正弦输入信号，系统输出将呈现较大的衰减。对于I型和I型以上的开环系统，由于 $|\Phi(j0)| = 1, 20\lg |\Phi(j0)| = 0$ ，故

$$2 0 \lg | \Phi (\mathrm{j} \omega) | < - 3 (\mathrm{dB}), \quad \omega > \omega_ {b} \tag {5-89}$$

带宽是频域中一项非常重要的性能指标。对于一阶和二阶系统，带宽频率和系统参数具有解析关系。

设一阶系统的闭环传递函数为

$$\Phi (s) = \frac {1}{T s + 1}$$

因为开环系统为 I 型, $\Phi(j0)=1$ ,按带宽定义

$$2 0 \lg | \Phi (\mathrm{j} \omega_ {b}) | = 2 0 \lg \frac {1}{\sqrt {1 + T ^ {2} \omega_ {b} ^ {2}}} = 2 0 \lg \frac {1}{\sqrt {2}}$$

可求得带宽频率

$$\omega_ {b} = \frac {1}{T} \tag {5-90}$$

对于二阶系统,闭环传递函数为

$$\Phi (s) = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}$$

系统幅频特性

$$\mid \Phi (\mathrm{j} \omega) \mid = \frac {1}{\sqrt {\left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) ^ {2} + 4 \zeta^ {2} \frac {\omega^ {2}}{\omega_ {n} ^ {2}}}}$$

因为 $|\Phi (\mathrm{j}0)| = 1$ ，由带宽定义得

$$\sqrt {\left(1 - \frac {\omega_ {b} ^ {2}}{\omega_ {n} ^ {2}}\right) ^ {2} + 4 \zeta^ {2} \frac {\omega_ {b} ^ {2}}{\omega_ {n} ^ {2}}} = \sqrt {2}$$

于是

$$\omega_ {b} = \omega_ {n} \left[ (1 - 2 \zeta^ {2}) + \sqrt {(1 - 2 \zeta^ {2}) ^ {2} + 1} \right] ^ {\frac {1}{2}} \tag {5-91}$$

由式(5-90)知，一阶系统的带宽频率和时间常数 $T$ 成反比。由式(5-91)知，二阶系统的带宽频率和自然频率 $\omega_{n}$ 成正比。令 $A = \left(\frac{\omega_b}{\omega_n}\right)^2$ ，由于

$$\frac {\mathrm{d} A}{\mathrm{d} \zeta} = \frac {- 4 \zeta}{\sqrt {(1 - 2 \zeta^ {2}) ^ {2} + 1}} [ \sqrt {(1 - 2 \zeta^ {2}) ^ {2} + 1} + (1 - 2 \zeta^ {2}) ] < 0$$

A 为 $\zeta$ 的减函数, 故 $\omega_{b}$ 为 $\zeta$ 的减函数, 即 $\omega_{b}$ 与阻尼比 $\zeta$ 成反比。根据第三章中一阶系统和二阶系统上升时间和调节时间与参数的关系可知, 系统的单位阶跃响应的速度和带宽成正比。对于任意阶次的控制系统, 这一关系仍然成立。

设两个控制系统存在以下关系：

$$\Phi_ {1} (s) = \Phi_ {2} \left(\frac {s}{\lambda}\right) \tag {5-92}$$

其中 $\lambda$ 为任意正常数。两个系统的闭环频率特性亦有

$$\Phi_ {1} (\mathrm{j} \omega) = \Phi_ {2} \left(\mathrm{j} \frac {\omega}{\lambda}\right)$$
