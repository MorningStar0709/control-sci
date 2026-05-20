# B.3 周期为 2L 的函数展开成傅里叶级数

B. 2节讨论了周期函数 $f_{T}(x) = f_{T}(x + 2\pi)$ 的傅里叶级数。本节将在此基础上进行拓展，定义一个新的周期函数为

$$f _ {T} (t) = f _ {T} (t + 2 L), \quad T = 2 L \tag {B.3.1}$$

它是周期为 T=2L 的函数。通过换元法，令 $t=\frac{L}{\pi}x$ ，得到

$$f _ {T} (t) = f _ {T} \left(\frac {L}{\pi} x\right) \triangleq g _ {T} (x) \tag {B.3.2a}$$

可得

$$g _ {T} (x + 2 \pi) = f _ {T} \left(\frac {L}{\pi} (x + 2 \pi)\right) = f _ {T} \left(\frac {L}{\pi} x + 2 L\right) = f _ {T} \left(\frac {L}{\pi} x\right) = g _ {T} (x) \tag {B.3.2b}$$

因此，换元之后 $g_{T}(x)$ 是一个周期为 $2\pi$ 的函数，根据式(B.2.12)，它可以展开为傅里叶级数，即

$$g _ {T} (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right) \tag {B.3.3a}$$

其中， $\left\{\begin{aligned}a_{n}&=\frac{1}{\pi}\int_{-\pi}^{\pi}g_{T}(x)\cos nx\mathrm{d}x\\ b_{n}&=\frac{1}{\pi}\int_{-\pi}^{\pi}g_{T}(x)\sin nx\mathrm{d}x\end{aligned}\quad n=0,1,2,\cdots\right.$ (B.3.3b)

将 $t=\frac{L}{\pi}x$ （即 $x=\frac{\pi}{L}t$ ）代入式(B.3.3a)，得到

$$f _ {T} (t) = g _ {T} (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n \frac {\pi}{L} t + b _ {n} \sin n \frac {\pi}{L} t\right) \tag {B.3.4}$$

此外，当 $x$ 的上下限为 $[\pi, -\pi]$ 时， $t$ 的上下限为 $\left[\pi \frac{L}{\pi}, -\pi \frac{L}{\pi}\right] = [L, -L]$ ，式(B.3.3b)可写成

$$
\begin{array}{l} a _ {n} = \frac {1}{\pi} \int_ {- L} ^ {L} f _ {T} (t) \cos n \frac {\pi}{L} t d \frac {\pi}{L} t \\ = \frac {1}{\pi} \frac {\pi}{L} \int_ {- L} ^ {L} f _ {T} (t) \cos n \frac {\pi}{L} t d t = \frac {1}{L} \int_ {- L} ^ {L} f _ {T} (t) \cos n \frac {\pi}{L} d t \tag {B.3.5} \\ \end{array}
b _ {n} = \frac {1}{\pi} \int_ {- L} ^ {L} f _ {T} (t) \sin n \frac {\pi}{L} t d \frac {\pi}{L} t= \frac {1}{\pi} \frac {\pi}{L} \int_ {- L} ^ {L} f _ {T} (t) \sin n \frac {\pi}{L} t d t = \frac {1}{L} \int_ {- L} ^ {L} f _ {T} (t) \sin n \frac {\pi}{L} d t \tag {B.3.6}
$$

式(B.3.4)、式(B.3.5)和式(B.3.6)是周期为 2L 的函数展开为傅里叶级数的表达。引入基频率 $\omega_{T}$ ，令

$$\omega_ {T} = \frac {\pi}{L} = \frac {2 \pi}{T} \tag {B.3.7}$$

将式(B.3.7)代入式(B.3.4)～式(B.3.6)，得到

$$
f _ {T} (t) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n \omega_ {T} t + b _ {n} \sin n \omega_ {T} t\right) \tag {B.3.8a}
\left\{ \begin{array}{l l} a _ {n} = \frac {2}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \cos n \omega_ {T} t \mathrm{d} t & n = 0, 1, 2, \dots \\ b _ {n} = \frac {2}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \sin n \omega_ {T} t \mathrm{d} t & n = 1, 2, 3, \dots \end{array} \right. \tag {B.3.8b}
$$

在式(B.3.8)中,如果考虑该函数 $f_{T}(t)$ 周期无限大 $(T \to \infty)$ , 即函数将在无限久之后才重复。此时的周期函数就变成了非周期函数, 即 $f_{T}(t) \to f(t)$ 。这意味着可以将任意的函数展开为三角函数的叠加。在处理它之前,首先要找到傅里叶级数的复数表达形式。
