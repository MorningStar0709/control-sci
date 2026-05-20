# B. 5 傅里叶变换

本节将推导傅里叶变换,在开始之前,首先思考傅里叶级数的物理意义。在 B.4 节中介绍了周期为 $T$ 的函数 $f_{T}(t)$ 的傅里叶级数展开的复数表达,即

$$f _ {T} (t) = \sum_ {n = - \infty} ^ {\infty} c _ {n} \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} \tag {B.5.1}$$

其中

$$c _ {n} = \frac {1}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t} \mathrm{d} t \quad n = 0, \pm 1, \pm 2, \pm 3, \dots \tag {B.5.2}$$

观察式(B.5.1)可以发现,任何周期为 $T$ 的函数展开后的表达形式都是一致的,都是一系列的复数 $c_{n}$ 与 $\mathrm{e}^{\mathrm{j}n\omega_{T}t}$ 的乘积之后加和的结果。因此,将不同周期函数区别开的是式(B.5.2)中所计算的 $c_{n}$ 项。例如,图 B.5.1(a)是周期函数 $f_{T}(t)$ , 图 B.5.1(b)则是其所对应的 $c_{n}$ 。

![](image/d109f8653639290d4c5a9ef202a729c7498506c4eee1070ab6565a221c489def.jpg)

<details>
<summary>text_image</summary>

(a) fT(t)的时域表达
fT(t)
O
t
jω(cn)
σ(cn)
-2ωT -ωT O ωT 2ωT nωT
(b) fT(t)的频域表达
</details>

图B.5.1 周期函数 $f_{T}(t)$ 的时域与频域表达

其中, 图 B.5.1(a) 以时间 $t$ 为横坐标, 称为 $f_{T}(t)$ 的时域表达, 而图 B.5.1(b) 则显示了周期函数在不同频率下 $c_{n}$ 的值, 称为频域表达, 它是 $f_{T}(t)$ 的频谱 (Spectral Density)。这就是从不同的角度看世界, 每一个周期函数都将对应一种频谱。请注意, 一般情况下看到的频谱很少是图 B.5.1(b) 这种三维复平面的, 而是会把复数的模 $|c_{n}|$ 单独列出来, 这样就可以得到时间函数在不同频率下的强度了。这在分析系统信号及设计滤波器中是非常重要的。

到此为止,我们讨论的一直都是周期函数 $f_{T}(t)$ 的傅里叶级数的展开,是否可以将其推广到更一般的形式呢?如果考虑 $f_{T}(t)$ 周期无限大,即 $T \to \infty$ ,即函数将在无限久之后才重复。此时的周期函数就变成了非周期函数,即 $f_{T}(t) \to f(t)$ 。首先考虑周期函数的频谱,如图 B.5.2(a) 所示,它的横坐标是离散的形式,之间的间隔为

$$\Delta \omega = (n + 1) \omega_ {T} - n \omega_ {T} = \omega_ {T} = \frac {2 \pi}{T} \tag {B.5.3}$$

随着周期 $T$ 的增加，间隔 $\Delta \omega$ 会变得越来越小。当 $T \to \infty$ 时， $\Delta \omega \to 0$ ，原本的离散形式就变成了连续形式，如图 B.5.2(b) 所示，此时横坐标变成了连续变量 $\omega$ 。因此，原本离散的 $c_n$ 也将变成一条连续的曲线。

![](image/4890b6b5c2069647a11dd29e7f3b0b6eed02c17c9abcf9878d978f0c87aacde9.jpg)

<details>
<summary>text_image</summary>

jω(cn)
σ(cn)
-2ωT -ωT O ωT 2ωT
nωT
Δω
</details>

(a) $f_{i}(t)$ 的频域表达

![](image/848ca6495f81c0ce379ce4409e0fe9d9f2ef5d9c7529834accafdff90c3488d9.jpg)

<details>
<summary>text_image</summary>

jω(cn)
σ(cn)
T→∞
Δω→0
O
ω
</details>

(b) $f(t)$ 的频域表达  
图 B.5.2 当周期 $T \rightarrow \infty$ 时的频谱变化

将式(B.5.2)代入式(B.5.1)，得到

$$f _ {T} (t) = \sum_ {n = - \infty} ^ {\infty} \frac {1}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t} \mathrm{d} t \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} \tag {B.5.4}$$

根据式(B.5.3)， $\frac{1}{T}=\frac{\Delta\omega}{2\pi}$ ，代入式(B.5.4)，得到
