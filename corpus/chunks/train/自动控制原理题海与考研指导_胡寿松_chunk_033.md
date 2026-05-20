# 1) 实微分定理

设 $F(s) = \mathcal{L}[f(t)]$ ，则应用分部积分法求拉普拉斯变换积分，有

$$\int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t = f (t) \frac {\mathrm{e} ^ {- s t}}{- s} \Big | _ {0} ^ {\infty} - \int_ {0} ^ {\infty} \left[ \frac {\mathrm{d}}{\mathrm{d} t} f (t) \right] \frac {\mathrm{e} ^ {- s t}}{- s} \mathrm{d} t = \frac {f (0)}{s} + \frac {1}{s} \mathscr {L} \left[ \frac {\mathrm{d}}{\mathrm{d} t} f (t) \right]$$

从而 $\mathcal{L}\left[\frac{\mathrm{d}}{\mathrm{d}t} f(t)\right] = sF(s) - f(0)$

同理可证

$$
\begin{array}{l} \mathcal {L} \left[ \frac {\mathrm{d} ^ {2}}{\mathrm{d} t ^ {2}} f (t) \right] = s ^ {2} F (s) - s f (0) - \dot {f} (0) \\ \mathcal {L} \left[ \frac {\mathrm{d} ^ {n}}{\mathrm{d} t ^ {n}} f (t) \right] = s ^ {n} F (s) - s ^ {n - 1} f (0) - s ^ {n - 2} \dot {f} (0) - \dots - f ^ {(n - 1)} (0) \\ \end{array}
$$
