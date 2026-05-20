# 1. $z$ 变换定义

设连续函数 $e(t)$ 是可拉氏变换的，则拉氏变换定义为

$$E (s) = \int_ {0} ^ {\infty} e (t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

由于 $t < 0$ 时，有 $e(t) = 0$ ，故上式亦可写为

$$E (s) = \int_ {- \infty} ^ {\infty} e (t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

对于采样信号 $e^{*}(t)$ ，其表达式为

$$e ^ {*} (t) = \sum_ {n = 0} ^ {\infty} e (n T) \delta (t - n T)$$

故采样信号 $e^{*}(t)$ 的拉氏变换

$$
\begin{array}{l} E ^ {*} (s) = \int_ {- \infty} ^ {\infty} e ^ {*} (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \int_ {- \infty} ^ {\infty} \left[ \sum_ {n = 0} ^ {\infty} e (n T) \delta (t - n T) \right] \mathrm{e} ^ {- s t} \mathrm{d} t \\ = \sum_ {n = 0} ^ {\infty} e (n T) \left[ \int_ {- \infty} ^ {\infty} \delta (t - n T) \mathrm{e} ^ {- s t} \mathrm{d} t \right] \tag {7-20} \\ \end{array}
$$

由广义脉冲函数的筛选性质

$$\int_ {- \infty} ^ {\infty} \delta (t - n T) f (t) \mathrm{d} t = f (n T)$$

故有 $\int_{-\infty}^{\infty}\delta (t - nT)\mathrm{e}^{-st}\mathrm{d}t = \mathrm{e}^{-snT}$

于是，采样拉氏变换(7-20)可以写为

$$E ^ {*} (s) = \sum_ {n = 0} ^ {\infty} e (n T) \mathrm{e} ^ {- n s T} \tag {7-21}$$

在上式中，各项均含有 $\mathbf{e}^{sT}$ 因子，故上式为 $s$ 的超越函数。为便于应用，令变量

$$z = \mathrm{e} ^ {s T} \tag {7-22}$$

式中， $T$ 为采样周期； $z$ 是在复数平面上定义的一个复变量，通常称为 $z$ 变换算子。

将式(7-22)代入式(7-21)，则采样信号 $e^{*}(t)$ 的z变换定义为

$$E (z) = E ^ {*} (s) \mid_ {s = \frac {1}{T} \ln z} = \sum_ {n = 0} ^ {\infty} e (n T) z ^ {- n} \tag {7-23}$$

记为

$$E (z) = \mathscr {L} [ e ^ {*} (t) ] = \mathscr {L} [ e (t) ] \tag {7-24}$$

后一记号是为了书写方便，并不意味着是连续信号 $e(t)$ 的 $z$ 变换，而是仍指采样信号 $e^{*}(t)$ 的 $z$ 变换。

应当指出， $z$ 变换仅是一种在采样拉氏变换中，取 $z = \mathrm{e}^{sT}$ 的变量置换。通过这种置换，可将 $s$ 的超越函数转换为 $z$ 的幂级数或 $z$ 的有理分式。
