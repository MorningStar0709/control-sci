# 6) 平移函数

设函数为 $f(t)$ ，当 $t < 0$ 时 $f(t) = 0$ ；平移函数为 $f(t - \alpha)1(t - \alpha)$ ，其中 $\alpha \geqslant 0$ ，且 $t < \alpha$ 时 $f(t - \alpha)1(t - \alpha) = 0$ ，则平移函数的拉普拉斯变换为

$$\mathcal {L} [ f (t - \alpha) 1 (t - \alpha) ] = \int_ {0} ^ {\infty} f (t - \alpha) 1 (t - \alpha) \mathrm{e} ^ {- s t} \mathrm{d} t$$

令 $\tau = t - \alpha$ ，有

$$\int_ {0} ^ {\infty} f (t - \alpha) 1 (t - \alpha) \mathrm{e} ^ {- s t} \mathrm{d} t = \int_ {- \alpha} ^ {\infty} f (\tau) 1 (\tau) \mathrm{e} ^ {- s (\tau + \alpha)} \mathrm{d} \tau$$

因 $\tau < 0$ 时 $f(\tau)1(\tau) = 0$ ，故有

$$
\begin{array}{l} \int_ {- \alpha} ^ {\infty} f (\tau) 1 (\tau) \mathrm{e} ^ {- s (\tau + \alpha)} \mathrm{d} \tau = \int_ {0} ^ {\infty} f (\tau) 1 (\tau) \mathrm{e} ^ {- s \tau} \mathrm{e} ^ {- \alpha s} \mathrm{d} \tau \\ = \mathrm{e} ^ {- \alpha s} \int_ {0} ^ {\infty} f (\tau) \mathrm{e} ^ {- s \tau} \mathrm{d} \tau \\ = \mathrm{e} ^ {- \alpha s} F (s) \\ \end{array}
$$

式中 $F(s) = \mathcal{L}[f(t)] = \int_{0}^{\infty}f(t)\mathrm{e}^{-st}\mathrm{d}t$

于是 $\mathcal{L}[f(t - \alpha)1(t - \alpha)] = \mathrm{e}^{-\alpha s}F(s),\quad \alpha \geqslant 0$
