$$
\begin{array}{l} f _ {T} (t) = \sum_ {n = - \infty} ^ {\infty} \frac {\Delta \omega}{2 \pi} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t} \mathrm{d} t \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} \\ = \frac {1}{2 \pi} \sum_ {n = - \infty} ^ {\infty} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t} \mathrm{d} t \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} \Delta \omega \tag {B.5.5} \\ \end{array}
$$

当 $T \to \infty$ 时， $f_{T}(t) \to f(t), \int_{-\frac{T}{2}}^{\frac{T}{2}} f_{T}(t) \mathrm{e}^{-\mathrm{j}n\omega_{T} t} \mathrm{d}t \to \int_{-\infty}^{\infty} f(t) \mathrm{e}^{-\mathrm{j}\omega t} \mathrm{d}t$ ，式(B.5.5)中的加和也将变成积分。因此，式(B.5.5)可以写成

$$f (t) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} f (t) \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t \mathrm{e} ^ {\mathrm{j} \omega t} \mathrm{d} \omega \tag {B.5.6}$$

其中，令

$$F (\omega) = \int_ {- \infty} ^ {\infty} f (t) \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t \tag {B.5.7}$$

$F(\omega)$ 被称为 $f(t)$ 的傅里叶变换。同时，称 $f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)\mathrm{e}^{\mathrm{j}\omega t}\mathrm{d}\omega$ 为 $F(\omega)$ 的傅里叶逆变换。

通过上述详细的推导,我们得到了函数 $f(t)$ 的傅里叶变换,对比式(B.5.7)与拉普拉斯变换:

$$\mathcal {L} [ f (t) ] = F (s) = \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t \tag {B.5.8}$$

会发现傅里叶变换是拉普拉斯变换的一种特殊情况(当 $s = j\omega$ 时)。所以,傅里叶变换有拉普拉斯变换的一切性质。此外,实函数的傅里叶变换为埃尔米特函数,符合共轭对称。根据傅里叶变换的定义:

$$\overline {{{F (\omega)}}} = \int_ {- \infty} ^ {\infty} \overline {{{f (t) \mathrm{e} ^ {- \mathrm{j} \omega t}}}} \mathrm{d} t = \int_ {- \infty} ^ {\infty} \overline {{{f (t)}}} \mathrm{e} ^ {\mathrm{j} \omega t} \mathrm{d} t = \int_ {- \infty} ^ {\infty} f (t) \mathrm{e} ^ {\mathrm{j} \omega t} \mathrm{d} t = F (- \omega) \tag {B.5.9}$$

其中， $\overline{F(\omega)}$ 代表 $F(\omega)$ 的共轭复数。 $\overline{F(\omega)}=F(-\omega)$ 是一个非常重要的性质，它被运用在第9章中推导频率响应。
