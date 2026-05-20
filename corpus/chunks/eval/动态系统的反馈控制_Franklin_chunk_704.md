# 4. 复频移性质

在时域中将 $f(t)$ 乘以指数因子，对应于频率的平移为：

$$F _ {1} (s) = \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- a t} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \int_ {0} ^ {+ \infty} f (t) \mathrm{e} ^ {- (s + a) t} \mathrm{d} t = F (s + a) \tag {A.9}$$

例 A.4 指数衰减的正弦曲线

求 $f(t) = A\sin (\omega t)\mathrm{e}^{-at}$ 的拉普拉斯变换。

解答。 $\sin(\omega t)$ 的拉普拉斯变换为

$$\mathcal {L} \left\{\sin (\omega t) \right\} = \frac {\omega}{s ^ {2} + \omega^ {2}}$$

所以，用式(A.9)我们得到

$$F (s) = \frac {A \omega}{(s + a) ^ {2} + \omega^ {2}}$$
