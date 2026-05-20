$$
\left\{ \begin{array}{l} x _ {1} (T) = - r \frac {(T - \tau) ^ {2}}{2} + (r \tau) (T - \tau) + r \frac {\tau^ {2}}{2} \\ x _ {2} (T) = r (T - \tau) - r \tau = r (T - 2 \tau) \end{array} \right. \tag {3.5.7}
$$

点 $(x_{1}(T),x_{2}(T))$ 将位于开关线的右上方且以时间T来到达原点的状态(图3.5.1)，即坐标 $(x_{1},x_{2})$ 满足

$$x _ {1} + \frac {\mid x _ {2} \mid x _ {2}}{2 r} > 0$$

从式(3.5.7)的第二式解出 $\tau$ ，得

![](image/851643c3dce2fb6035d8b2a7f369a09fa8818c63ce094d4b751d148a2105ff1c.jpg)  
图3.5.1

$$\tau = \frac {T}{2} - \frac {x _ {2}}{2 r}, T - \tau = \frac {T}{2} + \frac {x _ {2}}{2 r} \tag {3.5.8}$$

把这些表达式代到第一式，有

$$
\begin{array}{l} x _ {1} = - \frac {r}{2} \left(\frac {T}{2} + \frac {x _ {2}}{2 r}\right) ^ {2} - r \left(\frac {T}{2} - \frac {x _ {2}}{2 r}\right) \left(\frac {T}{2} + \frac {x _ {2}}{2 r}\right) - \frac {r}{2} \left(\frac {T}{2} - \frac {x _ {2}}{2 r}\right) ^ {2} = \\ \frac {1}{4 r} (r T - x _ {2}) ^ {2} - T ^ {2} + \frac {x _ {2} ^ {2}}{2 r} \tag {3.5.9} \\ \end{array}
$$

由此解出 T, 得

$$T = \frac {x _ {2}}{r} \pm \frac {2}{\sqrt {r}} \sqrt {x _ {1} + \frac {x _ {2} ^ {2}}{2 r}} \tag {3.5.10}$$

式(3.5.10)要有意义,必须 $x_{1}+\frac{x_{2}^{2}}{2r}\geqslant0$ .但是开关线右上方的点 $(x_{1},x_{2})$ 的坐标满足 $x_{1}+\frac{|x_{2}|x_{2}}{2r}\geqslant0$ ,从而由于 $0\leqslant x_{1}+\frac{|x_{2}|x_{2}}{2r}\leqslant x_{1}+\frac{x_{2}^{2}}{2r}$ 表达式(3.5.10)在开关线右上方是有意义的.而当 $x_{2}=0$ 时开关线右上方必有 $x_{1}>0$ ,时间T不能取负值,因此表达式(3.5.10)的“±”符号只能取“+”号,所以在开关线右上方,时间T的表达式最终变成

$$T = \frac {x _ {2}}{r} + \frac {2}{\sqrt {r}} \sqrt {x _ {1} + \frac {x _ {2} ^ {2}}{2 r}} \tag {3.5.11}$$

然后，从原点出发先取 $u = -r$ 积分倒退的方程

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = - x _ {2} \\ \dot {x} _ {2} = r \end{array} \right.
$$

到 $\tau,0\leqslant \tau \leqslant T$ 时间，得

$$
\left\{ \begin{array}{l} x _ {1} (\tau) = - r \frac {\tau^ {2}}{2} \\ x _ {2} (\tau) = r \tau \end{array} \right.
$$

这些点位于抛物线 $x_{1} + \frac{x_{2}^{2}}{2r} = 0$ 的 $x_{2} > 0$ 部分上. 然后从这些 $(x_{1}(\tau), x_{2}(\tau))$ 点出发, 取相反加速度 $u = r$ , 从 $\tau$ 到时刻 $T \geqslant \tau$ , 积分倒退的方程

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = - x _ {2} \\ \dot {x} _ {2} = - r \end{array} \right.
$$

得

$$
\left\{ \begin{array}{l} x _ {1} (T) = r \frac {(T - \tau) ^ {2}}{2} - (r \tau) (T - \tau) - r \frac {\tau^ {2}}{2} \\ x _ {2} (T) = - r (T - \tau) + r \tau = r (- T + 2 \tau) \end{array} \right.
$$

这些点将位于开关线 $x_{1} + \frac{|x_{2}|x_{2}}{2r} = 0$ 的左下方.从上面式的第二个方程解出 $\tau$ ，得

$$\tau = \frac {T}{2} + \frac {x _ {2}}{2 r}, T - \tau = \frac {T}{2} - \frac {x _ {2}}{2 r}$$

把这些表达式代到第一式，有
