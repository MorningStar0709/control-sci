# 2) 终值定理

如果函数 $f(t)$ 和 $\mathrm{d}f(t)/\mathrm{d}t$ 是可拉普拉斯变换的，象函数 $F(s)$ 是 $f(t)$ 的拉普拉斯变换，并且极限 $\lim f(t)$ 存在，则有

$$\lim _ {t \rightarrow \infty} f (t) = \lim _ {s \rightarrow 0} s F (s)$$

为了证明该定理，在 $\mathrm{d}f(t)/\mathrm{d}t$ 的拉普拉斯变换中，令 s 趋于零，即

$$\lim _ {s \rightarrow 0} \int_ {0} ^ {\infty} \left[ \frac {\mathrm{d}}{\mathrm{d} t} f (t) \right] \mathrm{e} ^ {- s t} \mathrm{d} t = \lim _ {s \rightarrow 0} [ s F (s) - f (0) ]$$

因为 $\lim_{s\to0}e^{-st}=1$ ，所以得

$$\int_ {0} ^ {\infty} \left[ \frac {\mathrm{d}}{\mathrm{d} t} f (t) \right] \mathrm{d} t = f (t) \mid_ {0} ^ {\infty} = f (\infty) - f (0) = \lim _ {s \rightarrow 0} s F (s) - f (0)$$

从而 $f(\infty) = \lim_{t\to \infty}f(t) = \lim_{s\to 0}sF(s)$

应当指出，当且仅当 $\lim_{t\to \infty}f(t)$ 存在，才能应用终值定理，这意味着当 $t\to \infty$ 时， $f(t)$ 将稳定到确定值。如果 $sF(s)$ 的所有极点均位于左半 $s$ 平面，则 $\lim_{t\to \infty}f(t)$ 存在；如果 $sF(s)$ 有极点位于虚轴或位于右半 $s$ 平面内， $f(t)$ 将分别包含振荡的或按指数规律增长的时间函数分量，因而 $\lim_{t\to \infty}f(t)$ 将不存在。显然，如果 $f(t)$ 是正弦函数 $\sin \omega t$ ，则 $sF(s)$ 将有位于虚轴上的极点 $s = \pm \mathrm{j}\omega$ ，因此 $\lim_{t\to \infty}f(t)$ 不存在，所以终值定理不适用于这类函数。
