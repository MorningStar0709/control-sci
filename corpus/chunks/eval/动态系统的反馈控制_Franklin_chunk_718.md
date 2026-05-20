# 初值定理

对任意的拉普拉斯变换对

$$\lim _ {s \to + \infty} s F (s) = f (0 ^ {+}) \tag {A.27}$$

我们可证明如下。利用式(A.11)，我们得到

$$\mathcal {L} \left\{\frac {\mathrm{d} f}{\mathrm{d} t} \right\} = s F (s) - f (0 ^ {-}) = \int_ {0 ^ {-}} ^ {+ \infty} \mathrm{e} ^ {- s t} \frac {\mathrm{d} f}{\mathrm{d} t} \mathrm{d} t \tag {A.28}$$

当 $s \to +\infty$ 时，积分重写为

$$\int_ {0 ^ {-}} ^ {+ \infty} \mathrm{e} ^ {- s t} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{d} t = \int_ {0 ^ {+}} ^ {+ \infty} \mathrm{e} ^ {- s t} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{d} t + \int_ {0 ^ {-}} ^ {0 ^ {+}} \mathrm{e} ^ {- s t} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{d} t$$

当 $s \to +\infty$ 时，求式(A.28)的极限得

$$\lim _ {s \rightarrow + \infty} [ s F (s) - f (0 ^ {-}) ] = \lim _ {s \rightarrow + \infty} \left[ \int_ {0 ^ {-}} ^ {0 ^ {+}} \mathrm{e} ^ {0} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{d} t + \int_ {0 ^ {+}} ^ {+ \infty} \mathrm{e} ^ {- s t} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{d} t \right]$$

因为当 $s \to +\infty$ 时，有 $e^{-st} \to 0$ ，所以上式右边第二项是趋于零的。所以

$$\lim _ {s \rightarrow + \infty} [ s F (s) - f (0 ^ {-}) ] = \lim _ {s \rightarrow + \infty} [ f (0 ^ {+}) - f (0 ^ {-}) ] = f (0 ^ {+}) - f (0 ^ {-})$$

或

$$\lim _ {s \rightarrow + \infty} s F (s) = f (0 ^ {+})$$

与终值定理相比，初值定理可用于任意函数 $F(s)$ 。
