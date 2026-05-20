# 3.尺度变换性质

如果时间 t 乘以 a，那么时间比例信号的拉普拉斯变换为

$$F _ {1} (s) = \int_ {0} ^ {+ \infty} f (a t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

再次定义 $t' = at$ 。于是， $dt' = adt$ 并且

$$F _ {1} (s) = \int_ {0} ^ {+ \infty} f \left(t ^ {\prime}\right) \frac {\mathrm{e} ^ {- s ^ {\prime} / a}}{| a |} \mathrm{d} t ^ {\prime} = \frac {1}{| a |} F \left(\frac {s}{a}\right) \tag {A.8}$$

例A.3 频率为 $\omega$ 的正弦信号

求 $f(t) = A\sin (\omega t)$ 的拉普拉斯变换。

解答。 $\sin (t)$ 的拉普拉斯变换为

$$\mathscr {L} \left\{\sin (t) \right\} = \frac {1}{s ^ {2} + 1}$$

所以，用式(A.8)我们可以得到预期结果

$$F (s) = \frac {1}{| \omega |} \frac {1}{\left(\frac {s}{\omega}\right) ^ {2} + 1} = \frac {A \omega}{s ^ {2} + \omega^ {2}}$$

在 Matlab 中使用如下命令也可以得到相同的结果，

syms s t w A

laplace(A\*sin(w\*t)).
