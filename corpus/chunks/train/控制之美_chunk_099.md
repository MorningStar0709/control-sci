式(5.3.12)为二阶欠阻尼系统单位阶跃响应的时间函数,它由两部分相减而成。其中“1”来自系统输入(极点为 $s_{\mathrm{pl}} = 0$ ,因此输出包含一个常数)。后半部分的 $\mathrm{e}^{-\zeta \omega_{\mathrm{n}} t}\sqrt{\frac{1}{1 - \zeta^{2}}}\sin (\omega_{\mathrm{d}}t + \varphi)$ 是两项相乘,其中 $\mathrm{e}^{-\zeta \omega_{\mathrm{n}} t}\sqrt{\frac{1}{1 - \zeta^{2}}}$ 项会随着时间的增加而递减并趋于0,如图5.3.2(a)所示。而 $\sin (\omega_{\mathrm{d}}t + \varphi)$ 则是周期为 $\frac{2\pi}{\omega_{\mathrm{d}}}$ 、初相位为 $\varphi$ 的三角函数,如图5.3.2(b)所示。这两部分相乘之后就形成了图5.3.2(c)中振荡且递减的曲线。

同时，式(5.3.12)说明 $x(t)$ 的收敛速度是由指数部分 $-\zeta \omega_{\mathrm{n}}$ 决定的，它同时也是传递函数极点 $s_{\mathrm{p2},3}$ 的实数部分。周期是由 $\omega_{\mathrm{d}}$ 决定的，而 $\omega_{\mathrm{d}} = \omega_{\mathrm{n}}\sqrt{1 - \zeta^2}$ 则是传递函数极点 $s_{\mathrm{p2},3}$ 的虚部。这再一次验证了传递函数极点对系统输出的影响。

![](image/84532d1a9594ad6c383578a9e9785a69295c134c1befbe3e589d62f543ed5515.jpg)

<details>
<summary>text_image</summary>

x(t)
O
t
</details>

(a) $e^{-\zeta\omega_{n}t}\sqrt{\frac{1}{1-\zeta^{2}}}$

![](image/b0ce3e09d229f6b7093f13ed8c1e45defab4333a0cd99074998908904f4bbec0.jpg)

<details>
<summary>line</summary>

| t | x(t) |
| --- | --- |
| 0 | 1 |
| 0.5 | 0 |
| 1 | -1 |
| 1.5 | 0 |
| 2 | 1 |
| 2.5 | 0 |
| 3 | -1 |
| 3.5 | 0 |
| 4 | 1 |
| 4.5 | 0 |
| 5 | -1 |
</details>

(b) $\sin (\omega_{\mathrm{d}}t + \varphi)$

![](image/20b4d5d8f3d9b202574dd19f4555a73d28b47c4864c37261b75d58c8cc60913d.jpg)

<details>
<summary>text_image</summary>

x(t)
=
O
t
</details>

(c) $e^{-\zeta\omega_{n}t}\sqrt{\frac{1}{1-\zeta^{2}}}\sin(\omega_{d}t+\varphi)$   
图5.3.2 $\mathrm{e}^{-\zeta \omega_{\mathrm{n}}t}\sqrt{\frac{1}{1 - \zeta^2}}\sin (\omega_{\mathrm{d}}t + \varphi)$ 的图像组成

![](image/d9fb767517d557852f9805e2281f23fc22bb8707ff7c18e0b9008c59a86d1d06.jpg)

<details>
<summary>line</summary>

| t | x(t) |
| --- | --- |
| 0 | 0 |
| Peak | 1 |
| Decline | 0.5 |
| Final | 1 |
</details>

图5.3.3 欠阻尼二阶系统的单位阶跃响应

而 $x(t)$ 的图像就是用“1”减去图 5.3.2(c) 的图像, 其结果如图 5.3.3 所示。

读者可以用同样的方法去推导过阻尼、临界阻尼和无阻尼的情况。这里不再赘述，只给出结果如下。

无阻尼情况(当 $\zeta=0$ 时):

$$x (t) = 1 - \cos \omega_ {\mathrm{n}} t \tag {5.3.13}$$

临界阻尼情况(当 $\zeta=1$ 时):

$$x (t) = 1 - \mathrm{e} ^ {- \omega_ {\mathrm{n}} t} (1 + \omega_ {\mathrm{n}} t) \tag {5.3.14}$$

过阻尼情况(当 $\zeta>1$ 时):
