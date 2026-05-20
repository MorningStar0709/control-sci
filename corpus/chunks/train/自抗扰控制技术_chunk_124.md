$$
\left\{ \begin{array}{l} x _ {2} (\tau) = - r \tau \\ x _ {1} (\tau) = r \frac {\tau^ {2}}{2} \end{array} \right.
$$

然后取 $u = +r_{1}$ ，以上式为初值，从 $\tau$ 积分倒推方程

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = - x _ {2} \\ \dot {x} _ {2} = - r _ {1} \end{array} \right.
$$

到 t 时刻, 得

$$
\left\{ \begin{array}{l} x _ {2} = - r _ {1} (t - \tau) - r \tau \\ x _ {1} = r _ {1} \frac {(t - \tau) ^ {2}}{2} + r \tau (t - \tau) + r \frac {r ^ {2}}{2} \end{array} \right. \tag {3.5.29}
$$

从式(3.5.29)中第1式解出 $\tau$ 和 $t-\tau$ ，然后把此表达式代到第2式，有

$$x _ {2} = - r _ {1} (t - \tau) - r \tau \Rightarrow \tau = \frac {x _ {2} + r _ {1} t}{r _ {1} - \tau}, t - \tau = \frac {r t + x _ {2}}{r _ {1} - r}x _ {1} = \frac {r _ {1} - \tau}{2} (t - \tau) ^ {2} + \frac {r}{2} t ^ {2}2 (r _ {1} - r) x _ {1} = (r t + x _ {2}) ^ {2} + r (r _ {1} - r) t ^ {2}2 \left(r _ {1} - r\right) \left(x _ {1} - \frac {x _ {2}}{2 r _ {1}}\right) = r _ {1} r \left(t + \frac {x _ {2}}{r _ {1}}\right) ^ {2} \tag {3.5.30}$$

由此得时间 $t$ 的表达式

$$t = - \frac {x _ {2}}{r _ {1}} \pm \sqrt {2 \frac {r _ {1} - r}{r _ {1} r}} \sqrt {x _ {1} - \frac {x _ {2} ^ {2}}{2 r _ {1}}} \tag {3.5.31}$$

把四个 t 的表达式 (3.5.22)，式 (3.5.25)，式 (3.5.28)，式

(3.5.31) 放在一起, 有

$$
t = \left\{ \begin{array}{l} \frac {x _ {2}}{r _ {1}} + \sqrt {2 \frac {r + r _ {1}}{r r _ {1}}} \sqrt {x _ {1} + \frac {x _ {2} ^ {2}}{2 r _ {1}}} \\ \frac {x _ {2}}{r _ {1}} + \sqrt {2 \frac {r _ {1} - r}{r r _ {1}}} \sqrt {- \left(x _ {1} + \frac {x _ {2} ^ {2}}{2 r _ {1}}\right)} \\ - \frac {x _ {2}}{r _ {1}} + \sqrt {2 \frac {r + r _ {1}}{r r _ {1}}} \sqrt {- \left(x _ {1} - \frac {x _ {2} ^ {2}}{2 r _ {1}}\right)} \\ - \frac {x _ {2}}{r _ {1}} + \sqrt {2 \frac {r _ {1} - r}{r r _ {1}}} \sqrt {x _ {1} - \frac {x _ {2} ^ {2}}{2 r _ {1}}} \end{array} \right. \tag {3.5.32}
$$

令 $a_{1} = \sqrt{2\frac{r + r_{1}}{rr_{1}}}$ ， $a_{2} = \sqrt{2\frac{r_{1} - r}{rr_{1}}}$ ， $s = \mathrm{sign}\left(x_1 + \frac{x_2}{2r}\right)$

$$s _ {1} = \operatorname{sign} \left(x _ {1} + \frac {x _ {2}}{2 r _ {1}}\right)$$

$a = a_{1} \frac{1 + s_{1}s}{2} + a_{2} \frac{1 - s_{1}s}{2}$ , 则有

$$
t = \left\{ \begin{array}{l} \frac {x _ {2}}{r _ {1}} + a \sqrt {x _ {1} + \frac {x _ {2} ^ {2}}{2 r _ {1}}}, s _ {1} \geqslant 0, s \geqslant 0 \\ \frac {x _ {2}}{r _ {1}} + a \sqrt {- x _ {1} - \frac {x _ {2} ^ {2}}{2 r _ {1}}}, s _ {1} \leqslant 0, s \geqslant 0 \\ - \frac {x _ {2}}{r _ {1}} + a \sqrt {- x _ {1} + \frac {x _ {2} ^ {2}}{2 r _ {1}}}, s _ {1} \leqslant 0, s \leqslant 0 \\ - \frac {x _ {2}}{r _ {1}} + a \sqrt {x _ {1} - \frac {x _ {2} ^ {2}}{2 r _ {1}}}, s _ {1} \geqslant 0, s \leqslant 0 \end{array} \right.
$$
