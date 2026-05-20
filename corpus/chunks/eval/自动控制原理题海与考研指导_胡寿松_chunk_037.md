# 5) 复微分定理

若函数 $f(t)$ 可拉普拉斯变换，则除了在 $F(s)$ 的极点之外，有

$$
\begin{array}{l} \mathscr {L} [ t f (t) ] = \int_ {0} ^ {\infty} t f (t) \mathrm{e} ^ {- s t} \mathrm{d} t = - \int_ {0} ^ {\infty} f (t) \frac {\mathrm{d}}{\mathrm{d} s} (\mathrm{e} ^ {- s t}) \mathrm{d} t \\ = - \frac {\mathrm{d}}{\mathrm{d} s} \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t = - \frac {\mathrm{d}}{\mathrm{d} s} F (s) \\ \end{array}
$$

类似地，令 $tf(t) = g(t)$ ，有

$$\mathscr {L} [ t ^ {2} f (t) ] = \mathscr {L} [ \tan (t) ] = - \frac {\mathrm{d}}{\mathrm{d} s} G (s) = - \frac {\mathrm{d}}{\mathrm{d} s} \left[ - \frac {\mathrm{d}}{\mathrm{d} s} F (s) \right] = (- 1) ^ {2} \frac {\mathrm{d} ^ {2}}{\mathrm{d} s ^ {2}} F (s)$$

重复上述过程,可得

$$\mathcal {L} [ t ^ {n} f (t) ] = (- 1) ^ {n} \frac {\mathrm{d} ^ {n}}{\mathrm{d} s ^ {n}} F (s), \quad n = 1, 2, 3, \dots$$
