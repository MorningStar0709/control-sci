# 10) 时间比例尺

设函数 $f(t)$ 的拉普拉斯变换为 $F(s)$ ，改变时间比例尺的函数为 $f(t/\alpha)$ ，其中 $\alpha$ 为正常数，则 $f(t/\alpha)$ 的拉普拉斯变换为

$$\mathcal {L} \left[ f (t / \alpha) \right] = \int_ {0} ^ {\infty} f (t / \alpha) \mathrm{e} ^ {- s t} \mathrm{d} t$$

令 $t / \alpha = t_{1},\alpha s = s_{1}$ ，得到

$$
\begin{array}{l} \mathcal {L} \left[ f (t / \alpha) \right] = \int_ {0} ^ {\infty} f (t _ {1}) \mathrm{e} ^ {- s _ {1} t _ {1}} \mathrm{d} (\alpha t _ {1}) \\ = \alpha \int_ {0} ^ {\infty} f (t _ {1}) \mathrm{e} ^ {- s _ {1} t _ {1}} \mathrm{d} t _ {1} \\ = \alpha F (s _ {1}) = \alpha F (\alpha s) \\ \end{array}
$$

例如，考虑 $f(t) = \mathrm{e}^{-t}, f(t / 5) = \mathrm{e}^{-0.2t}$ ，由于

$$\mathcal {L} [ f (t) ] = \mathcal {L} [ \mathrm{e} ^ {- t} ] = \frac {1}{s + 1} = F (s)$$

因此 $\mathcal{L}[f(t / 5)] = \mathcal{L}[\mathrm{e}^{-0.2t}] = 5F(5s) = \frac{5}{5s + 1}$
