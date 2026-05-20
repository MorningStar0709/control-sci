# 3) 初值定理

初值定理是终值定理的对偶定理。如果函数 $f(t)$ 和 $\mathrm{df}(t) / \mathrm{dt}$ 均可拉普拉斯变换，并且 $\lim sF(s)$ 存在，则有

$$f (0 _ {+}) = \lim _ {s \rightarrow \infty} s F (s)$$

为了证明该定理,利用 $\mathrm{d}f(t)/\mathrm{d}t$ 的 $L_{+}$ 变换

$$\mathcal {L} _ {+} \left[ \frac {\mathrm{d}}{\mathrm{d} t} f (t) \right] = s F (s) - f (0 _ {+})$$

由于 $\lim_{s\to \infty}\mathrm{e}^{-st}\rightarrow 0,\quad \forall t\in [0_+, \infty)$

因此 $\lim_{s\to \infty}\int_{0_+}^{\infty}\left[\frac{\mathrm{d}}{\mathrm{d}t} f(t)\right]\mathrm{e}^{-st}\mathrm{d}t = \lim_{s\to \infty}[sF(s) - f(0_+)] = 0$

证得 $f(0_{+})=\lim_{s\to\infty}sF(s)$

应当指出,在应用初值定理时,对 $sF(s)$ 的极点位置没有限制,因此对于正弦函数,初值定理是成立的。
