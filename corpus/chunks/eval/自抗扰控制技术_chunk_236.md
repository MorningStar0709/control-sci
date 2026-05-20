$$\ddot {y} = - \omega_ {0} y - 2 \xi_ {0} \omega_ {0} \dot {y} - \sum_ {1} ^ {m} \left[ \left(\omega_ {i} ^ {2} - \omega_ {0} ^ {2}\right) x _ {i} \right.\left. + 2 \left(\xi_ {i} \omega_ {i} - \xi_ {0} \omega_ {0}\right) \dot {x} _ {i} \right] + \left(\sum_ {1} ^ {m} b _ {i}\right) u \tag {6.6.5}$$

现在记

$$w (x, \dot {x}) = - \sum_ {1} ^ {m} \left[ \left(\omega_ {i} ^ {2} - \omega_ {0} ^ {2}\right) x _ {i} + 2 \left(\xi_ {i} \omega_ {i} - \xi_ {0} \omega_ {0}\right) \dot {x} _ {i} \right] \tag {6.6.6}b = \sum_ {1} ^ {m} b _ {i} \tag {6.6.7}$$

则得

$$\ddot {y} = - \omega_ {0} y - 2 \xi_ {0} \omega_ {0} \dot {y} + b u + w (x, \dot {x}) \tag {6.6.8}$$

在这里我们把 $w(x,\dot{x})$ 当作外扰来处理．实际上每个分频是衰减振荡，因此控制过程中的扰动量 $w(x,\dot{x})$ 总是在有界范围内变化，这就可以用自抗扰控制器来有效地抑制其作用了.

例 设某一柔性弹性体的振荡按频谱分解取前三项的结果为

$$y = \frac {1}{1 7 6} \left(\frac {1}{s ^ {2}} + \frac {1 . 2 8}{s ^ {2} + 0 . 0 1 2 4 2 s + 4 . 2 8 4 9} \frac {0 . 0 3}{s ^ {2} + 0 . 1 4 2 2 s + 5 6 1 . 6 9}\right) u \tag {6.6.9}$$

其状态变量实现为

$$
\left\{ \begin{array}{l} \ddot {x} _ {1} = \frac {1}{1 7 6} u \\ \ddot {x} _ {2} = - 4. 2 8 4 9 x _ {2} - 0. 0 1 2 4 2 \dot {x} _ {2} + \frac {1 . 2 8}{1 7 6} u \\ \ddot {x} _ {3} = - 5 6 1. 6 9 x _ {3} - 0. 1 4 2 2 \dot {x} _ {3} + \frac {0 . 0 3}{1 7 6} u \\ y = x _ {1} + x _ {2} + x _ {3} \end{array} \right. \tag {6.6.10}
$$

把它化成(6.6.8)的形式

$$\ddot {y} = - a _ {1} y - a _ {2} \dot {y} + w (x, \dot {x}) + b u \tag {6.6.11}$$

那么

$$b = \frac {1 + 1 . 2 8 + 0 . 0 0 3}{1 7 6} = 0. 0 1 2 9 7 2 \tag {6.6.12}$$

在这里控制的目的是尽快消除振荡，即 $y$ 尽快趋近零．只要 $a_1, a_2$ 在一定范围之内不管怎么变，自抗扰控制器是能够控制好这个对象的.

对象(6.6.9)的设定值是 $y^{*}=0,y$ 的初始条件假设为 $y(0)=1.0$ .

整个自抗扰控制器算法为

安排过渡过程

$$
\left\{ \begin{array}{l} \mathrm{fh} = \operatorname{fhan} \left(v _ {1} - y ^ {*}, v _ {2}, r _ {0}, h\right) \\ v _ {1} = v _ {1} + h v _ {2}, v _ {1} (0) = \gamma (0) \\ v _ {2} = v _ {2} + h \mathrm{fh}, v _ {2} (0) = 0. 0, r _ {0} = 0. 0 0 2 \end{array} \right. \tag {6.6.13}
$$

状态与扰动估计

$$
\begin{array}{l} e = z _ {1} - y, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} \mathrm{fe} + b _ {0} u\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {1}\right) \end{array} \tag {6.6.14}
$$

生成误差和误差反馈律

$$
\left\{ \begin{array}{l} e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2} \\ \mathrm{uu} = - \text {fhan} (e _ {1}, c e _ {2}, r, h _ {0}) \end{array} \right. \tag {6.6.15}
$$

最终控制量

$$u = \mathrm{uu} - \frac {z _ {3}}{b _ {0}} \tag {6.6.16}$$
