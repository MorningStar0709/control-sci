# (4) 初值定理

若函数 $f(t)$ 及其一阶导数都是可拉氏变换的，则函数 $f(t)$ 的初值为

$$f (0 _ {+}) = \lim _ {t \rightarrow 0 _ {+}} f (t) = \lim _ {s \rightarrow \infty} F (s)$$

即原函数 $f(t)$ 在自变量趋于零(从正向趋于零)时的极限值，取决于其象函数 $F(s)$ 在自变量趋于无穷大时的极限值。

证明 由微分定理,有

$$\int_ {0} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{e} ^ {- s t} \mathrm{d} t = s F (s) - f (0)$$

令 $s \to \infty$ ，对等式两边取极限，得

$$\lim _ {s \rightarrow \infty} \int_ {0} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{e} ^ {- s t} \mathrm{d} t = \lim _ {s \rightarrow \infty} [ s F (s) - f (0) ]$$

在 $0_{+} < t < \infty$ 的时间区间，当 $s \to \infty$ 时， $\mathrm{e}^{-s}$ 趋于零，因此等式左边为

$$\lim _ {s \rightarrow \infty} \int_ {0 _ {+}} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{e} ^ {- s} \mathrm{d} t = \int_ {0 _ {+}} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \lim _ {s \rightarrow \infty} \mathrm{e} ^ {- s} \mathrm{d} t = 0$$

于是 $\lim_{s\to \infty}[sF(s) - f(0_+)]=0$

即 $f(0_{+}) = \lim_{t\to 0_{+}}f(t) = \lim_{s\to \infty}F(s)$

式中 $f(0_{+})$ 表示 $f(t)$ 在 t=0 右极限时的值。
