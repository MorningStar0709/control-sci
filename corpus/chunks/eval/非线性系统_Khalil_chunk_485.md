# Gronwall-Bellman 不等式

引理A.1 令 $\lambda : [a, b] \to R$ 是连续的, $\mu : [a, b] \to R$ 是连续非负的, 如果连续函数 $y: [a, b] \to R$ 在 $a \leqslant t \leqslant b$ 时满足

$$y (t) \leqslant \lambda (t) + \int_ {a} ^ {t} \mu (s) y (s) d s$$

那么在同一个区间上

$$y (t) \leqslant \lambda (t) + \int_ {a} ^ {t} \lambda (s) \mu (s) \exp \left[ \int_ {s} ^ {t} \mu (\tau) d \tau \right] d s$$

特殊的情况是,如果 $\lambda(t)\equiv\lambda$ 是一个常数,那么

$$y (t) \leqslant \lambda \exp \left[ \int_ {a} ^ {t} \mu (\tau) d \tau \right]$$

另外,如果 $\mu(t)\equiv\mu\geq0$ 是一个常数,那么

$$y (t) \leqslant \lambda \exp [ \mu (t - a) ]$$

证明：令 $z(t) = \int_{a}^{t}\mu (s)y(s)$ 和 $v(t) = z(t) + \lambda (t) - y(t)\geqslant 0$ ，则 $z$ 是可微的，且

$$\dot {z} = \mu (t) y (t) = \mu (t) z (t) + \mu (t) \lambda (t) - \mu (t) v (t)$$

这是一个具有状态传递函数 $\phi (t,s) = \exp \left[\int_s^t\mu (\tau)d\tau \right]$

的标量线性状态方程。由于 $z(a) = 0$ ，因此有

$$z (t) = \int_ {a} ^ {t} \phi (t, s) [ \mu (s) \lambda (s) - \mu (s) v (s) ] d s$$

其中 $\int_{a}^{t}\phi (t,s)\mu (s)v(s)ds$

是非负的,故 $z(t)\leqslant \int_{a}^{t}\exp \left[\int_{s}^{t}\mu (\tau)d\tau \right]\mu (s)\lambda (s)ds$

由于 $y(t) \leqslant \lambda(t) + z(t)$ ，因此完成了一般意义上的证明。对于特殊情况 $\lambda(t) \equiv \lambda$ ，我们有

$$
\begin{array}{l} \int_ {a} ^ {t} \mu (s) \exp \left[ \int_ {s} ^ {t} \mu (\tau) d \tau \right] d s = - \int_ {a} ^ {t} \frac {d}{d s} \left\{\exp \left[ \int_ {s} ^ {t} \mu (\tau) d \tau \right] \right\} d s \\ = - \left\{\exp \left[ \int_ {s} ^ {t} \mu (\tau) d \tau \right] \right\} \Bigg | _ {s = a} ^ {s = t} \\ = - 1 + \exp \left[ \int_ {a} ^ {t} \mu (\tau) d \tau \right] \\ \end{array}
$$

上述推导就是 $\lambda$ 为常数时对引理的证明。当 $\lambda, \mu$ 都是常数时，可综合上述两种情况证明。证毕。
