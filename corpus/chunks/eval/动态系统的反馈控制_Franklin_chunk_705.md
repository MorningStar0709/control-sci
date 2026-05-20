# 5. 微分性质

信号的微分的拉普拉斯变换与其自身的拉普拉斯变换和它的初始条件有关，如下：

$$\mathscr {L} \left\{\frac {\mathrm{d} f}{\mathrm{d} t} \right\} = \int_ {0 ^ {-}} ^ {+ \infty} \left(\frac {\mathrm{d} f}{\mathrm{d} t}\right) \mathrm{e} ^ {- s t} \mathrm{d} t = \mathrm{e} ^ {- s t} f (t) \mid_ {0 ^ {-}} ^ {+ \infty} + s \int_ {0 ^ {-}} ^ {+ \infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t \tag {A.10}$$

因为假设 $f(t)$ 有一个拉普拉斯变换，当 $t \to +\infty$ 时 $\mathrm{e}^{-st} f(t) \to 0$ 。所以

$$\mathcal {L} [ \dot {f} ] = - f (0 ^ {-}) + s F (s) \tag {A.11}$$

再次应用式(A.11)得出

$$\mathscr {L} \{\ddot {f} \} = s ^ {2} F (s) - s f \left(0 ^ {-}\right) - \dot {f} \left(0 ^ {-}\right) \tag {A.12}$$

多次应用式(A.11)得

$$\mathscr {L} \left\{f ^ {m} (t) \right\} = s ^ {m} F (s) - s ^ {m - 1} f \left(0 ^ {-}\right) - s ^ {m - 2} f \left(0 ^ {-}\right) - \dots - f ^ {(m - 1)} \left(0 ^ {-}\right) \tag {A.13}$$

这里 $f^{m}(t)$ 表示 $f(t)$ 对时间 t 的 m 阶导数。

例 A.5 余弦信号的导数

求 $g(t) = \frac{\mathrm{d}}{\mathrm{d}t} f(t)$ 的拉普拉斯变换，其中 $f(t) = \cos (\omega t)$ 。

解答。 $\cos(\omega t)$ 的拉普拉斯变换是

$$F (s) = \mathcal {L} \{\cos (\omega t) \} = \frac {s}{s ^ {2} + \omega^ {2}}$$

用式(A.11)，其中 $f(0^{-}) = 1$ ，我们得到

$$G (s) = \mathscr {L} \{g (t) \} = s \cdot \frac {s}{s ^ {2} + \omega^ {2}} - 1 = - \frac {\omega^ {2}}{s ^ {2} + \omega^ {2}}$$
