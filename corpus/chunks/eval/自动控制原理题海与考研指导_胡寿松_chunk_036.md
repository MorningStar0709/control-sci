# 4）积分定理

如果函数 $f(t)$ 是指数级的，且 $f(0_{-}) = f(0_{+}) = f(0), F(s) = \mathcal{L}[f(t)]$ ，则

$$
\begin{array}{l} \mathscr {L} \left[ \int f (t) \mathrm{d} t \right] = \int_ {0} ^ {\infty} \left[ \int f (t) \mathrm{d} t \right] \mathrm{e} ^ {- s t} \mathrm{d} t = \left[ \int f (t) \mathrm{d} t \right] \frac {\mathrm{e} ^ {- s t}}{- s} \Bigg | _ {0} ^ {\infty} - \int_ {0} ^ {\infty} f (t) \frac {\mathrm{e} ^ {- s t}}{- s} \mathrm{d} t \\ = \frac {1}{s} \int f (t) \mathrm{d} t \mid_ {t = 0} + \frac {1}{s} \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \frac {f ^ {- 1} (0)}{s} + \frac {F (s)}{s} \\ \end{array}
$$

如果 $f(t)$ 在 t=0 处包含一个脉冲函数，则 $f^{-1}(0_{+})\neq f^{-1}(0_{-})$ 。此时，必须对积分定理作如下修改：

$$\mathscr {L} _ {+} \left[ \int f (t) \mathrm{d} t \right] = \frac {F (s)}{s} + \frac {f ^ {- 1} \left(0 _ {+}\right)}{s}\mathscr {L} _ {-} \left[ \int f (t) \mathrm{d} t \right] = \frac {F (s)}{s} + \frac {f ^ {- 1} (0 _ {-})}{s}$$
