# 2.2.2 拉普拉斯变换的收敛域

重新分析例2.2.1， $\mathcal{L}[\mathrm{e}^{-at}] = \int_0^\infty \mathrm{e}^{-at}\mathrm{e}^{-st}\mathrm{d}t = \frac{1}{s + a}$ 。在求它的拉普拉斯变换时，需要假设这个积分是收敛的。

可以举一个反例,例如选取 s = -2a,且 a > 0,这时积分可写成

$$F (s) = \mathcal {L} [ \mathrm{e} ^ {- a t} ] = \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- a t} \mathrm{e} ^ {- (- 2 a) t} \mathrm{d} t = \int_ {0} ^ {\infty} \mathrm{e} ^ {a t} \mathrm{d} t \tag {2.2.13}$$

当 $a > 0$ 时, $\mathrm{e}^{at}$ 随着时间的增加会趋于无穷。显然, 式(2.2.13)的积分不存在 (无穷大)。所以求它的拉普拉斯变换, 就需要对变量 $s$ 加一个限制条件。而这个限制条件称为拉普拉斯变换的收敛域 (Region of Convergence, ROC)。

将 $s = \sigma +\mathrm{j}\omega$ 代入式(2.2.13)，得到

$$F (s) = \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- a t} \mathrm{e} ^ {- (\sigma + \mathrm{j} \omega) t} \mathrm{d} t = \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- (a + \sigma) t} \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t \tag {2.2.14}$$

式(2.2.14)中的积分由两部分相乘而得,首先看 $e^{-j\omega t}$ 这一项,它是一个复数。根据欧拉公式, $e^{-j\omega t} = \cos\omega t - j\sin\omega t$ 。 $e^{-j\omega t}$ 在复平面中的表达如图2.2.2所示,随着t的增加,它在复平面上会沿着一个圆做顺时针运动,而它的幅值 $|e^{-j\omega t}|$ 是恒定不变的: $|e^{-j\omega t}| = \cos^{2}\omega t + \sin^{2}\omega t = 1$ 。所以,用它乘以 $e^{-(a+\sigma)t}$ 这一项并不会对积分的收敛产生影响。这也很好理解,根据欧拉公式, $e^{-j\omega t}$ 仅仅引入了正弦和余弦函数(引入了振动),而振动会有正有负,不会在单一的方向增加或者减少。因此,分析积分是否收敛需要看式(2.2.14)积分中前面的一项,即 $e^{-(a+\sigma)t}$ 。若要求这部分收敛,显而易见,e的指数部分要小于0,即

![](image/be58ccf1cd708ec98dcd8e8456e12e88b536daf23012b04ae8b644d89f0dc186.jpg)

<details>
<summary>text_image</summary>

jω
|e⁻ʲʷᵗ|=1
-ωt
O
σ
</details>

图2.2.2 $\mathbf{e}^{-\mathrm{j}\omega t}$ 的复平面表达

$$- (a + \sigma) < 0 \Rightarrow \sigma > - a \tag {2.2.15}$$

所以， $\sigma > -a$ 是 $\mathcal{L}[\mathrm{e}^{-at}] = \frac{1}{s + a}$ 的收敛域。其他常见拉普拉斯变换的收敛域请参考表2.2.1。
