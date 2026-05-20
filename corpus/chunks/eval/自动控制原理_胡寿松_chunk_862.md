# (2) 微分定理

设 $F(s) = \mathcal{L}[f(t)]$ ，则有

$$\mathcal {L} \left[ \frac {\mathrm{d} f (t)}{\mathrm{d} t} \right] = s F (s) - f (0)$$

式中， $f(0)$ 是函数 $f(t)$ 在t=0时的值。

证明 由式(A-11)有

$$\mathcal {L} \left[ \frac {\mathrm{d} f (t)}{\mathrm{d} t} \right] = \int_ {0} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{e} ^ {- s t} \mathrm{d} t$$

用分部积分法，令 $u = \mathrm{e}^{-st},\mathrm{d}v = \frac{\mathrm{d}f(t)}{\mathrm{d}t}\mathrm{d}t$ ，则

$$\mathcal {L} \left[ \frac {\mathrm{d} f (t)}{\mathrm{d} t} \right] = \left[ \mathrm{e} ^ {- s t} f (t) \right] \Big | _ {0} ^ {\infty} + s \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t = s F (s) - f (0)$$

同理,函数 $f(t)$ 的高阶导数的拉氏变换为

$$\mathscr {L} \left[ \frac {\mathrm{d} ^ {n} f (t)}{\mathrm{d} t ^ {n}} \right] = s ^ {n} F (s) - \left[ s ^ {n - 1} f (0) + s ^ {n - 2} \dot {f} (0) + \dots + f ^ {(n - 1)} (0) \right]$$

式中， $f(0)$ ， $\dot{f}(0)$ ， $\ddot{f}(0)$ ， $\cdots$ ， $f^{(n-1)}(0)$ 为 $f(t)$ 及其各阶导数在t=0时的值。

显然, 如果原函数 $f(t)$ 及其各阶导数的初始值都等于零, 则原函数 $f(t)$ 的 $n$ 阶导数的拉氏变换就等于其象函数 $F(s)$ 乘以 $s^n$ , 即

$$\mathscr {L} \left[ \frac {\mathrm{d} ^ {n} f (t)}{\mathrm{d} t ^ {n}} \right] = s ^ {n} F (s)$$
