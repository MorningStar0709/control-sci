# (5) 终值定理

若函数 $f(t)$ 及其一阶导数都是可拉氏变换的，则函数 $f(t)$ 的终值为

$$\lim _ {t \rightarrow \infty} f (t) = \lim _ {s \rightarrow 0} s F (s)$$

即原函数 $f(t)$ 在自变量 $t$ 趋于无穷大时的极限值，取决于象函数 $F(s)$ 在自变量 $s$ 趋于零时的极限值。

证明 由微分定理,有

$$\int_ {0} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{e} ^ {- s t} \mathrm{d} t = s F (s) - f (0)$$

令 $s \to 0$ ，对等式两边取极限，得

$$\lim _ {s \rightarrow 0} \int_ {0} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{e} ^ {- s t} \mathrm{d} t = \lim _ {s \rightarrow 0} [ s F (s) - f (0) ]$$

等式左边为

$$\lim _ {s \rightarrow 0} \int_ {0} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{e} ^ {- s t} \mathrm{d} t = \int_ {0} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \lim _ {s \rightarrow 0} \mathrm{e} ^ {- s t} \mathrm{d} t= \int_ {0} ^ {\infty} \mathrm{d} f (t) = \lim _ {t \rightarrow \infty} \int_ {0} ^ {t} \mathrm{d} f (t) = \lim _ {t \rightarrow \infty} [ f (t) - f (0) ]$$

于是

$$\lim _ {t \rightarrow \infty} f (t) = \lim _ {s \rightarrow 0} s F (s)$$

注意, 当 $f(t)$ 是周期函数, 如正弦函数 $\sin\omega t$ 时, 由于它没有终值, 故终值定理不适用。
