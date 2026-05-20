# 例 A.1 正弦信号

求 $f(t)=1+2\sin(\omega t)$ 的拉普拉斯变换。

解答。 $\sin (\omega t)$ 的拉普拉斯变换为

$$\mathcal {L} \left\{\sin (\omega t) \right\} = \frac {\omega}{s ^ {2} + \omega^ {2}}$$

所以，用式(A.5)我们得到

$$F (s) = \frac {1}{s} + \frac {2 \omega}{s ^ {2} + \omega^ {2}} = \frac {s ^ {2} + 2 \omega s + \omega^ {2}}{s ^ {3} + \omega^ {2} s}$$

在 Matlab 中使用如下命令也可以得到相同的结果：

syms stw
laplace(1+2\*sin(w\*t)).
