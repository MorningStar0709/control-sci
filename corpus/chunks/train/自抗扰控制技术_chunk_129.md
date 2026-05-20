$$6 \frac {x _ {1}}{r} = \left(\frac {2}{\sqrt {r}} \sqrt {- x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} - \frac {x _ {3}}{r}\right) ^ {3} - 2 \left(\frac {1}{\sqrt {r}} \sqrt {- x _ {2} + \frac {x _ {3} ^ {2}}{2 r} - \frac {x _ {3}}{r}}\right) ^ {3}x _ {1} = \left(- x _ {2} + \frac {x _ {3} ^ {2}}{2 r}\right) \left(\frac {1}{\sqrt {r}} \sqrt {- x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} - \frac {x _ {3}}{r}\right) + \frac {x _ {3} ^ {3}}{6 r ^ {2}},- x _ {2} + \frac {x _ {3} ^ {2}}{2 r} = - \left(x _ {2} - \frac {x _ {3} ^ {2}}{2 r}\right) \geqslant 0 \tag {3.6.9}$$

把式(3.6.6)，式(3.6.9)放在一起

$$
\left\{ \begin{array}{l} x _ {1} = - \left(x _ {2} + \frac {x _ {3} ^ {2}}{2 r}\right) \left(\frac {1}{\sqrt {r}} \sqrt {x _ {2} + \frac {x _ {3} ^ {2}}{2 r} + \frac {x _ {1}}{r}}\right) + \frac {x _ {3} ^ {3}}{6 r ^ {2}}, \\ x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \geqslant 0 \\ x _ {1} = \left(- x _ {2} + \frac {x _ {3} ^ {2}}{2 r}\right) \left(\frac {1}{\sqrt {r}} \sqrt {- x _ {2} + \frac {x _ {1} ^ {2}}{2 r}} - \frac {x _ {1}}{r}\right) + \frac {x _ {3} ^ {3}}{6 r ^ {2}}, \\ - x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \geqslant 0 \end{array} \right. \tag {3.6.10}
$$

在这里，由于有

$$x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \geqslant x _ {2} + \frac {\left| x _ {3} \right| x _ {3}}{2 r}, - x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \geqslant - \left(x _ {2} + \frac {\left| x _ {3} \right| x _ {3}}{2 r}\right)x _ {2} + \frac {\mid x _ {3} \mid x _ {3}}{2 r} \geqslant 0 \Rightarrow x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \geqslant 0,x _ {2} + \frac {\mid x _ {3} \mid x _ {3}}{2 r} \leqslant 0 \Rightarrow - x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \geqslant 0$$

因此，令

$$s = \operatorname{sign} \left(x _ {2} + \frac {\mid x _ {3} \mid x _ {3}}{2 r}\right)$$

则式 $(3.6.10)$ 的两式统一地写成

$$x _ {1} = - s \left(s x _ {2} + \frac {x _ {3} ^ {2}}{2 r}\right) \left(\frac {1}{\sqrt {r}} \sqrt {s x _ {2} + \frac {x _ {3} ^ {2}}{2 r}} + s \frac {x _ {3}}{r}\right) + \frac {x _ {3} ^ {3}}{6 r ^ {2}} \tag {3.6.11}$$

这就是三维状态空间中的最速开关曲面的表达式. 此开关曲面也可以表示成

$$
\left\{ \begin{array}{l} s = \operatorname{sign} \left(x _ {2} + \frac {\mid x _ {3} \mid x _ {3}}{2 r}\right) \\ a = s x _ {2} + \frac {x _ {3} ^ {2}}{2 r} \\ b = \frac {x _ {3}}{r} \\ x _ {1} = - s a \left(\sqrt {\frac {a}{r}} + s b\right) + \frac {r}{6} b ^ {3} \end{array} \right. \tag {3.6.12}
$$

于是最速控制综合函数的表达式变成
