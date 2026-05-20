$$y (t) = f \left(A \sin \omega t\right) = - y \left(t + \frac {\pi}{\omega}\right) \tag {8-59}$$

则由式(8-54)

$$A _ {0} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} y (t) d \omega t = \frac {1}{2 \pi} \left[ \int_ {0} ^ {\pi} y (t) d \omega t + \int_ {\pi} ^ {2 \pi} y (t) d \omega t \right]$$

取变换 $\omega t = \omega u + \pi$ ，有

$$A _ {0} = \frac {1}{2 \pi} \left[ \int_ {0} ^ {\pi} y (t) d \omega t + \int_ {0} ^ {\pi} y \left(u + \frac {\pi}{\omega}\right) d \omega u \right]= \frac {1}{2 \pi} \left[ \int_ {0} ^ {\pi} y (t) d \omega t + \int_ {0} ^ {\pi} - y (u) d \omega u \right] = 0$$

而当非线性特性为输入 $x$ 的奇函数时，即 $f(x) = -f(-x)$ ，有

$$y \left(t + \frac {\pi}{\omega}\right) = f \left[ A \sin \omega \left(t + \frac {\pi}{\omega}\right) \right]= f [ \operatorname{Asin} (\pi + \omega t) ] = f [ - \operatorname{Asin} \omega t ]= f (- x) = - f (x) = - y (t)$$

即 $y(t)$ 为 $t$ 的奇对称函数，直流分量为零。 $A_{1}, B_{1}$ 按下式计算：

$$A _ {1} = \frac {2}{\pi} \int_ {0} ^ {\pi} y (t) \cos \omega t d \omega t, \quad B _ {1} = \frac {2}{\pi} \int_ {0} ^ {\pi} y (t) \sin \omega t d \omega t \tag {8-60}$$

关于描述函数计算,还具有以下特点。若 $y(t)$ 为奇函数,即 $y(t)=-y(-t)$ ,则

$$
\begin{array}{l} A _ {1} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} y (t) \cos \omega t d \omega t = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} y (t) \cos \omega t d \omega t \\ = \frac {1}{\pi} \left[ \int_ {- \pi} ^ {0} y (t) \cos \omega t d \omega t + \int_ {0} ^ {\pi} y (t) \cos \omega t d \omega t \right] \\ = \frac {1}{\pi} \left[ \int_ {0} ^ {\pi} y (- t) \cos (- \omega t) d \omega t + \int_ {0} ^ {\pi} y (t) \cos \omega t d \omega t \right] = 0 \tag {8-61} \\ \end{array}
$$

若 $y(t)$ 为奇函数，且又为半周期内对称，即 $y(t) = y\left(\frac{\pi}{\omega} - t\right)$ 时

$$B _ {1} = \frac {4}{\pi} \int_ {0} ^ {\frac {\pi}{2}} y (t) \sin \omega t d \omega t \tag {8-62}$$

例 8-4 设某非线性元件的特性为

$$y (x) = \frac {1}{2} x + \frac {1}{4} x ^ {3} \tag {8-63}$$

试计算其描述函数。

解 因 $y(x)$ 为 $x$ 的奇函数，故 $A_0 = 0$ 。当输入 $x = A\sin \omega t$ 时

$$y (t) = \frac {A}{2} \sin \omega t + \frac {A ^ {3}}{4} \sin^ {3} \omega t \tag {8-64}$$

为 $t$ 的奇函数，故 $A_{1} = 0$ 。又因为 $y(t)$ 具有半周期对称，按式(8-62)，有

$$
\begin{array}{l} B _ {1} = \frac {4}{\pi} \int_ {0} ^ {\frac {\pi}{2}} y (t) \sin \omega t d \omega t \\ = \frac {4}{\pi} \left(\int_ {0} ^ {\frac {\pi}{2}} \frac {A}{2} \sin^ {2} \omega t d \omega t + \int_ {0} ^ {\frac {\pi}{2}} \frac {A ^ {3}}{4} \sin^ {4} \omega t d \omega t\right) \\ \end{array}
$$

由定积分公式
