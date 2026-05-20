$$6 \frac {x _ {1}}{r} = - \left(\frac {2}{\sqrt {r}} \sqrt {x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} + \frac {x _ {3}}{r}\right) ^ {3} + 2 \left(\frac {1}{\sqrt {r}} \sqrt {x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} + \frac {x _ {3}}{r}\right) ^ {3}6 \frac {x _ {1}}{r} = - \frac {6}{r} \left(x _ {2} + \frac {x _ {3} ^ {2}}{2 r}\right) \left(\frac {1}{\sqrt {r}} \sqrt {x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} + \frac {x _ {3}}{r}\right) + \left(\frac {x _ {3}}{r}\right) ^ {3}x _ {1} = - \left(x _ {2} + \frac {x _ {3} ^ {2}}{2 r}\right) \left(\frac {1}{\sqrt {r}} \sqrt {x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} + \frac {x _ {3}}{r}\right) + \frac {x _ {3} ^ {3}}{6 r ^ {2}}, x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \geqslant 0 \tag {3.6.6}$$

然后取 $u = -r$ ，从原点倒退积分，得

$$
\left\{ \begin{array}{l} x _ {3} (\tau) = r \tau \\ x _ {2} (\tau) = - r \frac {\tau^ {2}}{2} \\ x _ {1} (\tau) = r \frac {\tau^ {3}}{6} \end{array} \right.
$$

开关一次后取 $u = +r$ ，以上式表示的点为初值倒退积分，得

$$
\left\{ \begin{array}{l} x _ {3} = r \tau - r (t - \tau) = - r t + 2 r \tau \\ x _ {2} = - r \frac {\tau^ {2}}{2} + r \frac {(t - \tau) ^ {2}}{2} - r \tau (t - \tau) \\ x _ {1} = r \frac {\tau^ {3}}{6} + r \frac {\tau^ {2}}{2} (t - \tau) - r \frac {(t - \tau) ^ {3}}{6} + r \tau \frac {(t - \tau) ^ {2}}{2} \end{array} \right. \tag {3.6.7}
$$

从式(3.6.7)中第1式解出 $t-\tau=\tau-\frac{x_{3}}{r}$ ，把它代到第2式，得

$$2 \frac {x _ {2}}{r} = - \tau^ {2} - 2 \tau \left(\tau - \frac {x _ {3}}{r}\right) + \left(\tau - \frac {x _ {3}}{r}\right) ^ {2} = - 2 \tau^ {2} + \frac {x _ {3} ^ {2}}{r ^ {2}}$$

由此

$$
\left\{ \begin{array}{l} \tau = \frac {1}{\sqrt {r}} \sqrt {- x _ {2} + \frac {x _ {3} ^ {2}}{2 r}}, x _ {2} - \frac {x _ {3} ^ {2}}{2 r} \leqslant 0 \\ t = 2 \tau - \frac {x _ {3}}{r} = \frac {2}{\sqrt {r}} \sqrt {- x _ {2} + \frac {x _ {3} ^ {2}}{2 r} - \frac {x _ {3}}{r}} \\ t - \tau = \tau - \frac {x _ {3}}{r} = \frac {1}{\sqrt {r}} \sqrt {- x _ {2} + \frac {x _ {3} ^ {2}}{2 r} - \frac {x _ {3}}{r}} \end{array} \right. \tag {3.6.8}
$$

把式 $(3.6.7)$ 的第3式整理成

$$
\begin{array}{l} 6 \frac {x _ {1}}{r} = \tau^ {3} + 3 \tau^ {2} (t - \tau) + 3 \tau (t - \tau) ^ {2} - (t - \tau) ^ {3} \\ 6 \frac {x _ {1}}{r} = (\tau + t - \tau) ^ {3} - 2 (t - \tau) ^ {3} = t ^ {3} - 2 (t - \tau) ^ {3} \\ \end{array}
$$

把 $\tau$ 和 t 的表达式(式 3.6.8 中第 2 式和第 3 式)代进去, 最后得
