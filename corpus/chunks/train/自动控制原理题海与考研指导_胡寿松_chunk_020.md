# 1. 拉普拉斯变换

设 $f(t)$ 为时间 $t$ 的函数，且当 $t < 0$ 时 $f(t) = 0$ ，则 $f(t)$ 的拉普拉斯变换定义为

$$F (s) = \mathcal {L} [ f (t) ] = \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

相应的拉普拉斯反变换则为

$$f (t) = \mathcal {L} ^ {- 1} [ F (s) ] = \frac {1}{2 \pi \mathrm{j}} \int_ {c - \mathrm{j} \infty} ^ {c + \mathrm{j} \infty} F (s) \mathrm{e} ^ {s t} \mathrm{d} s$$

式中，收敛横坐标 $c$ 为实常量，其实部应大于 $F(s)$ 所有奇点的实部。
