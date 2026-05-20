$$
\begin{array}{l} x _ {1} = \frac {r}{2} \left(\frac {T}{2} + \frac {x _ {2}}{2 r}\right) ^ {2} - r \left(\frac {T}{2} - \frac {x _ {2}}{2 r}\right) \left(\frac {T}{2} + \frac {x _ {2}}{2 r}\right) - \frac {r}{2} \left(\frac {T}{2} - \frac {x _ {2}}{2 r}\right) ^ {2} = \\ - \frac {r}{4} \left(T + \frac {x _ {2}}{r}\right) ^ {2} + \frac {x _ {2} ^ {2}}{2 r} \\ \end{array}
$$

解出 T, 得

$$T = - \frac {x _ {2}}{r} \pm \frac {2}{\sqrt {r}} \sqrt {- x _ {1} + \frac {x _ {2} ^ {2}}{2 r}} \tag {3.5.12}$$

这就是从状态 $(x_{1},x_{2})\in\left\{(x_{1},x_{2})|x_{1}+\frac{|x_{2}|x_{2}}{2r}\leqslant0\right\}$ 出发按系统(3.5.2)最快地到达原点所花的时间T的表达式。在这里，由于 $-x_{1}+$ $\frac{x_{2}^{2}}{r}\geqslant-x_{1}-\frac{|x_{2}|x_{2}}{2r}\geqslant0$ ，表达式(3.5.12)的开方是有意义的。另外，在开关线的左下方，当 $x_{2}=0$ 时， $-x_{1}\geqslant0$ ，而时间T不能取负值，表达式(3.5.12)中的“+”号只能取“+”号，因此表达式(3.5.12)最终变成

$$T = - \frac {x _ {2}}{r} + \frac {2}{\sqrt {r}} \sqrt {- x _ {1} + \frac {x _ {2} ^ {2}}{2 r}} \tag {3.5.13}$$

考虑到表达式(3.5.11)和式(3.5.13)的施用范围,可以统一地表示成

$$s = \operatorname{sign} \left(x _ {1} + \frac {\mid x _ {2} \mid x _ {2}}{2 r}\right)T \left(x _ {1}, x _ {2}\right) = s \frac {x _ {2}}{r} + \frac {2}{\sqrt {r}} \sqrt {\frac {x _ {2} ^ {2}}{2 r} + s x _ {1}} \tag {3.5.14}$$

这个函数可以称作最速时间函数, 函数 $T(x_{1}, x_{2})$ 的意思是从点 $(x_{1}, x_{2})$ 出发沿最速轨线到达原点所花的时间.

最速时间函数 $T(x_{1},x_{2})$ 在原点上的值 $T(x_{1},x_{2}) = 0$ ，在整个相平面上是连续的正定数.最速时间函数 $T(x_{1},x_{2})$ ，将成为闭环系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r s \end{array} \right. \tag {3.5.15}
$$

的一个李亚普诺夫函数,而且满足等式

$$\frac {\partial T \left(x _ {1} , x _ {2}\right)}{\partial x _ {1}} x _ {2} + \frac {\partial T \left(x _ {1} , x _ {2}\right)}{\partial x _ {2}} (- r s) = - 1$$

事实上，有

$$\frac {\partial T}{\partial x _ {1}} = \frac {1}{\sqrt {r} \sqrt {\frac {x _ {2} ^ {2}}{2 r} + x _ {1}}},\frac {\partial T}{\partial x _ {2}} = \frac {1}{r} + \frac {x _ {2}}{r} \frac {1}{\sqrt {r} \sqrt {\frac {x _ {2} ^ {2}}{2 r} + x _ {1}}}, x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r} \geqslant 0;\frac {\partial T}{\partial x _ {1}} = - \frac {1}{\sqrt {r} \sqrt {\frac {x _ {2} ^ {2}}{2 r} - x _ {1}}},\frac {\partial T}{\partial x _ {2}} = - \frac {1}{r} + \frac {x _ {2}}{r} \frac {1}{\sqrt {r} \sqrt {\frac {x _ {2} ^ {2}}{2 r} - x _ {1}}}, x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r} \leqslant 0$$

统一两式,有
