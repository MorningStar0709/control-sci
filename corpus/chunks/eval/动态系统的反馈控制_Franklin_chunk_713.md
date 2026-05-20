# 例A.8 正弦信号的时域乘积

求 $f(t)=t\sin(\omega t)$ 的拉普拉斯变换。

解答。 $\sin(\omega t)$ 的拉普拉斯变换为

$$\mathcal {L} \{\sin (\omega t) \} = \frac {\omega}{s ^ {2} + \omega_ {2}}$$

所以，用式(A.22)，得到

$$F (s) = - \frac {\mathrm{d}}{\mathrm{d} s} \left[ \frac {\omega}{s ^ {2} + \omega^ {2}} \right] = \frac {2 \omega s}{(s ^ {2} + \omega^ {2}) ^ {2}}$$

在 Matlab 中使用如下命令也可以得到相同的结果，

$$
\begin{array}{l} \text {syms stw} \\ \text {laplace(t*sin(w*t)).} \end{array}
$$
