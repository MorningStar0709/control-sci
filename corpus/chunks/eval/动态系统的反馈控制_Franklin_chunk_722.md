# 终值定理的证明

下面我们可以证明这个结果。对式(3.41)求导得

$$\mathcal {L} \left[ \frac {\mathrm{d} y}{\mathrm{d} t} \right] = s Y (s) - y (0 ^ {-}) = \int_ {0 ^ {-}} ^ {+ \infty} \mathrm{e} ^ {- s t} \frac {\mathrm{d} y}{\mathrm{d} t} \mathrm{d} t$$

假设我们感兴趣的是 $s \to 0$ 时。那么

$$\lim _ {s \rightarrow 0} [ s Y (s) - y (0) ] = \lim _ {s \rightarrow 0} \left(\int_ {0} ^ {+ \infty} \mathrm{e} ^ {- s t} \frac {\mathrm{d} y}{\mathrm{d} t} \mathrm{d} t\right) = \lim _ {t \rightarrow + \infty} [ y (t) - y (0) ]$$

并且我们有

$$\lim _ {t \rightarrow + \infty} y (t) = \lim _ {s \rightarrow 0} s Y (s)$$

另一种方法是，对 $Y(s)[$ 式(3.51)]进行部分分式展开，得

$$Y (s) = \frac {C _ {1}}{s - p _ {1}} + \frac {C _ {2}}{s - p _ {2}} + \dots + \frac {C _ {n}}{s - p _ {n}}$$

让 $p_1 = 0$ ，以及所有其他的 $p_i$ 位于左半平面内，以使 $C_1$ 是 $y(t)$ 的稳态值。用式(3.53)，我们得

$$C _ {1} = \lim _ {t \rightarrow + \infty} y (t) = s Y (s) | _ {s = 0}$$

与之前结果一致。

对拉普拉斯变换更深入更广泛的分析，请参考 Churchill(1972) 和 Campbell 和 Foster (1948)；双边拉普拉斯变换详见 Van der Pol 和 Bremmer(1955)。
