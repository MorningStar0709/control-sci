# (1) 采样信号的拉氏变换

对采样信号 $e^{*}(t)$ 进行拉氏变换, 可得

$$E ^ {*} (s) = \mathcal {L} [ e ^ {*} (t) ] = \mathcal {L} \Big [ \sum_ {n = 0} ^ {\infty} e (n T) \delta (t - n T) \Big ] \tag {7-4}$$

根据拉氏变换的位移定理,有

$$\mathcal {L} [ \delta (t - n T) ] = \mathrm{e} ^ {- n T s} \int_ {0} ^ {\infty} \delta (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \mathrm{e} ^ {- n T s}$$

所以，采样信号的拉氏变换

$$E ^ {*} (s) = \sum_ {n = 0} ^ {\infty} e (n T) \mathrm{e} ^ {- n T s} \tag {7-5}$$

应当指出，式(7-5)将 $E^{*}(s)$ 与采样函数 $e(nT)$ 联系了起来，可以直接看出 $e^{*}(t)$ 的时间响应。但是，由于 $e^{*}(t)$ 只描述了 $e(t)$ 在采样瞬时的数值，所以 $E^{*}(s)$ 不能给出连续函数 $e(t)$ 在采样间隔之间的信息，这是要特别强调指出的。还应当注意的是，式(7-5)描述的采样拉氏变换，与连续信号 $e(t)$ 的拉氏变换 $E(s)$ 非常类似。因此，如果 $e(t)$ 是一个有理函数，则无穷级数 $E^{*}(s)$ 也总是可以表示成 $\mathbf{e}^{Ts}$ 的有理函数形式。在求 $E^{*}(s)$ 的过程中，初始值通常规定采用 $e(0_{+})$ 。

例 7-3 设 $e(t)=1(t)$ ，试求 $e^{*}(t)$ 的拉氏变换。

解 由式(7-5)，有

$$E ^ {*} (s) = \sum_ {n = 0} ^ {\infty} e (n T) \mathrm{e} ^ {- n T s} = 1 + \mathrm{e} ^ {- T s} + \mathrm{e} ^ {- 2 T s} + \dots$$

这是一个无穷等比级数，公比为 $\mathbf{e}^{-Ts}$ ，求和后得闭合形式

$$E ^ {*} (s) = \frac {1}{1 - \mathrm{e} ^ {- T s}} = \frac {\mathrm{e} ^ {T s}}{\mathrm{e} ^ {T s} - 1}, \quad | \mathrm{e} ^ {- T s} | < 1$$

显然， $E^{*}(s)$ 是 $e^{Ts}$ 的有理函数。

例7-4 设 $e(t) = \mathrm{e}^{-at}, t \geqslant 0, a$ 为常数，试求 $e^{*}(t)$ 的拉氏变换。

解 由式(7-5)，有

$$
\begin{array}{l} E ^ {*} (s) = \sum_ {n = 0} ^ {\infty} \mathrm{e} ^ {- a n T} \mathrm{e} ^ {- n T s} = \sum_ {n = 0} ^ {\infty} \mathrm{e} ^ {- n (s + a) T} \\ = \frac {1}{1 - e ^ {- (s + a) T}} = \frac {e ^ {T s}}{e ^ {T s} - e ^ {- a T}}, \quad | e ^ {- (\sigma + a) T} | <   1 \\ \end{array}
$$

式中， $\sigma$ 为 $s$ 的实部。上式也是 $\mathbf{e}^{Ts}$ 的有理函数。

上述分析表明, 只要 $E(s)$ 可以表示为 $s$ 的有限次多项式之比时, 总可以用式(7-5)推导出 $E^{*}(s)$ 的闭合形式。然而, 如果用拉氏变换法研究离散系统, 尽管可以得到 $\mathbf{e}^{Ts}$ 的有理函数, 但却是一个复变量 $s$ 的超越函数, 不便于进行分析和设计。为了克服这一困难, 通常采用 $z$ 变换法研究离散系统。 $z$ 变换可以把线性离散系统的 $s$ 超越方程, 变换为变量 $z$ 的代数方程。有关 $z$ 变换理论将在下节介绍。
