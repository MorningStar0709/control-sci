# 3. 欠阻尼二阶系统的动态过程分析

在控制工程中,除了那些不容许产生振荡响应的系统外,通常都希望控制系统具有适度的阻尼、较快的响应速度和较短的调节时间。因此,二阶控制系统的设计,一般取 $\zeta=0.4\sim0.8$ , 其各项动态性能指标,除峰值时间、超调量和上升时间可用 $\zeta$ 与 $\omega_{n}$ 准确表示外, 调节时间很难用 $\zeta$ 与 $\omega_{n}$ 准确描述, 不得不采用工程上的近似计算方法。

为了便于说明改善系统动态性能的方法，图3-11表示了欠阻尼二阶系统各特征参量之间的关系。由图可见，衰减系数 $\sigma$ 是闭环极点到虚轴之间的距离；阻尼振荡频率 $\omega_{\mathrm{d}}$ 是闭环极点到实轴之间的距离；自然频率 $\omega_{\mathrm{n}}$ 是闭环极点到坐标原点之间的距离； $\omega_{\mathrm{n}}$ 与负实轴夹角的余弦正好是

阻尼比，即

$$\zeta = \cos \beta \tag {3-18}$$

故 $\beta$ 称为阻尼角。下面推导式(3-11)所描述的无零点欠阻尼二阶系统的动态性能指标计算公式。

![](image/d16bca0ecbc1ef4d1391b3b6123536703d861f3bc27c466a8e773570c2d14a77.jpg)

<details>
<summary>text_image</summary>

s₁
ωₙ
β
0
σ=ζωₙ
s₂
j
ωₐ=ωₙ√(1-ζ²)
</details>

图 3-11 欠阻尼二阶系统的特征参量

(1) 上升时间 $t_{r}$ 的计算

在式(3-14)中，令 $c(t_{r})=1$ ，求得

$$\frac {1}{\sqrt {1 - \zeta^ {2}}} \mathrm{e} ^ {- \zeta \omega_ {n} t _ {r}} \sin (\omega_ {d} t _ {r} + \beta) = 0$$

由于 $e^{-\zeta \omega_{n}t_{r}}\neq 0$ ，所以有

$$t _ {r} = \frac {\pi - \beta}{\omega_ {d}} \tag {3-19}$$

由式(3-19)可见，当阻尼比 $\zeta$ 一定时，阻尼角 $\beta$ 不变，系统的响应速度与 $\omega_{\mathrm{n}}$ 成正比；而当阻尼振荡频率 $\omega_{\mathrm{d}}$ 一定时，阻尼比越小，上升时间越短。

(2) 峰值时间 $t_{p}$ 的计算

将式(3-14)对 t 求导, 并令其为零, 求得

$$\zeta \omega_ {n} \mathrm{e} ^ {- \zeta \omega_ {n} t _ {p}} \sin (\omega_ {d} t _ {p} + \beta) - \omega_ {d} \mathrm{e} ^ {- \zeta \omega_ {n} t _ {p}} \cos (\omega_ {d} t _ {p} + \beta) = 0$$

整理得

$$\tan (\omega_ {d} t _ {p} + \beta) = \frac {\sqrt {1 - \zeta^ {2}}}{\zeta}$$

由于 $\tan\beta=\sqrt{1-\zeta^{2}}/\zeta$ ，于是上列三角方程的解为 $\omega_{d}t_{p}=0,\pi,2\pi,3\pi,\cdots$ 。根据峰值时间定义，应取 $\omega_{d}t_{p}=\pi$ ，于是峰值时间

$$t _ {p} = \frac {\pi}{\omega_ {d}} \tag {3-20}$$

上式表明,峰值时间等于阻尼振荡周期的一半。或者说,峰值时间与闭环极点的虚部数值成反比。当阻尼比一定时,闭环极点离负实轴的距离越远,系统的峰值时间越短。

(3) 超调量 $\sigma\%$ 的计算

因为超调量发生在峰值时间上,所以将式(3-20)代入式(3-14),得输出量的最大值

$$c (t _ {p}) = 1 - \frac {1}{\sqrt {1 - \zeta^ {2}}} \mathrm{e} ^ {- \pi \zeta / \sqrt {1 - \zeta^ {2}}} \sin (\pi + \beta)$$

由于 $\sin(\pi+\beta)=-\sqrt{1-\zeta^{2}}$ ，故上式可写为 $c(t_{p})=1+e^{-\pi\zeta/\sqrt{1-\zeta^{2}}}$ 。按超调量定义式(3-1)，并考虑到 $c(\infty)=1$ ，求得

$$\sigma \% = \mathrm{e} ^ {- \pi \zeta / \sqrt {1 - \zeta^ {2}}} \times 100 \% \tag{3 - 21}$$

上式表明，超调量 $\sigma \%$ 仅是阻尼比 $\zeta$ 的函数，而与自然频率 $\omega_{\mathrm{n}}$ 无关。超调量与阻尼比的关系曲线，如图3-12所示。由图可见，阻尼比越大，超调量越小，反之亦然。一般，当选取 $\zeta = 0.4\sim 0.8$ 时， $\sigma \%$ 介于 $1.5\% \sim 25.4\%$ 。

![](image/261e5efc8985ff4210bc20613790601c36d3b526b382bd9d9f5de9f222c33c84.jpg)

<details>
<summary>line</summary>

| ζ | σ% |
| --- | --- |
| 0.0 | 100 |
| 0.2 | 70 |
| 0.4 | 30 |
| 0.6 | 10 |
| 0.8 | 2 |
| 1.0 | 0 |
</details>

图 3-12 欠阻尼二阶系统 $\zeta$ 与 $\sigma\%$ 关系曲线
