# 8) 脉冲函数

考虑下列脉冲函数：

$$
g (t) = \left\{\begin{array}{l l}\lim _ {t _ {0} \rightarrow 0} \frac {A}{t _ {0}},&0 <   t <   t _ {0}\\0,&t <   0, \quad t _ {0} <   t\end{array}\right.
$$

则脉冲函数的拉普拉斯变换

$$
\begin{array}{l} \mathscr {L} [ g (t) ] = \lim _ {t _ {0} \rightarrow 0} \left[ \frac {A}{t _ {0} s} \left(1 - e ^ {- s t _ {0}}\right)\right] = \lim _ {t _ {0} \rightarrow 0} \frac {\frac {d}{d t _ {0}} \left[ A \left(1 - e ^ {- s t _ {0}}\right)\right]}{\frac {d}{d t _ {0}} \left(t _ {0} s\right)} \\ = \lim _ {t _ {0} \rightarrow 0} \frac {A s}{s} = A \\ \end{array}
$$

9) $f(t)$ 与 $\mathrm{e}^{-\alpha t}$ 相乘

若 $f(t)$ 可拉普拉斯变换, 且其拉普拉斯变换为 $F(s)$ , 则 $\mathrm{e}^{-\alpha t}f(t)$ 的拉普拉斯变换为

$$\mathcal {L} \left[ \mathrm{e} ^ {- \alpha t} f (t) \right] = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \alpha t} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t = F (s + \alpha)$$

类似地,若有

$$\mathcal {L} \left[ \sin \omega t \right] = \frac {\omega}{s ^ {2} + \omega^ {2}} = F (s), \qquad \mathcal {L} \left[ \cos \omega t \right] = \frac {s}{s ^ {2} + \omega^ {2}} = G (s)$$

则有 $\mathcal{L}\left[\mathrm{e}^{-\alpha t}\sin \omega t\right] = F(s + \alpha) = \frac{\omega}{(s + \alpha)^2 + \omega^2}$

$$\mathcal {L} \left[ \mathrm{e} ^ {- \alpha t} \cos \omega t \right] = G (s + \alpha) = \frac {s + \alpha}{(s + \alpha) ^ {2} + \omega^ {2}}$$
