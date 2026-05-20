以 $x_{3}$ 作为输入时, 控制律

$$x _ {3} = - x _ {1} - (1 + 2 x _ {1}) \left(x _ {1} ^ {2} - x _ {1} ^ {3} + x _ {2}\right) - \left(x _ {2} + x _ {1} + x _ {1} ^ {2}\right) \stackrel {\text { def }} {=} \phi \left(x _ {1}, x _ {2}\right)$$

可使系统达到全局稳定,相应的李雅普诺夫函数为

$$V (x _ {1}, x _ {2}) = \frac {1}{2} x _ {1} ^ {2} + \frac {1}{2} (x _ {2} + x _ {1} + x _ {1} ^ {2}) ^ {2}$$

为运用反步法,应用变量代换 $z_{3}=x_{3}-\phi(x_{1},x_{2})$

可得 $\dot{x}_1 = x_1^2 -x_1^3 +x_2$

$$\dot {x} _ {2} = \phi (x _ {1}, x _ {2}) + z _ {3}\dot {z} _ {3} = u - \frac {\partial \phi}{\partial x _ {1}} (x _ {1} ^ {2} - x _ {1} ^ {3} + x _ {2}) - \frac {\partial \phi}{\partial x _ {2}} (\phi + z _ {3})$$

以 $V_{c}=V+z_{3}^{2}/2$ 作为复合李雅普诺夫函数, 得

$$
\begin{array}{l} \dot {V} _ {c} = \frac {\partial V}{\partial x _ {1}} (x _ {1} ^ {2} - x _ {1} ^ {3} + x _ {2}) + \frac {\partial V}{\partial x _ {2}} (z _ {3} + \phi) \\ + z _ {3} \left[ u - \frac {\partial \phi}{\partial x _ {1}} \left(x _ {1} ^ {2} - x _ {1} ^ {3} + x _ {2}\right) - \frac {\partial \phi}{\partial x _ {2}} \left(z _ {3} + \phi\right) \right] \\ = - x _ {1} ^ {2} - x _ {1} ^ {4} - \left(x _ {2} + x _ {1} + x _ {1} ^ {2}\right) ^ {2} \\ + z _ {3} \left[ \frac {\partial V}{\partial x _ {2}} - \frac {\partial \phi}{\partial x _ {1}} \left(x _ {1} ^ {2} - x _ {1} ^ {3} + x _ {2}\right) - \frac {\partial \phi}{\partial x _ {2}} \left(z _ {3} + \phi\right) + u \right] \\ \end{array}
$$

取 $u = -\frac{\partial V}{\partial x_2} + \frac{\partial \phi}{\partial x_1}(x_1^2 - x_1^3 + x_2) + \frac{\partial \phi}{\partial x_2}(z_3 + \phi) - z_3$

得 $\dot{V}_c = -x_1^2 - x_1^4 - (x_2 + x_1 + x_1^2)^2 - z_3^2$

因此，原点是全局渐近稳定的。

△

现在讨论系统(14.49)\~(14.50)的更一般表示

$$\dot {\eta} = f (\eta) + g (\eta) \xi \tag {14.53}\dot {\xi} = f _ {a} (\eta , \xi) + g _ {a} (\eta , \xi) u \tag {14.54}$$

$f_{a}$ 和 $g_{a}$ 是光滑的。如果在讨论的区域内 $g_{a}(\eta, \xi) \neq 0$ ，把输入变换为

$$u = \frac {1}{g _ {a} (\eta , \xi)} [ u _ {a} - f _ {a} (\eta , \xi) ] \tag {14.55}$$

则方程(14.54)就简化为积分器 $\xi = u_{a}$ 。因此，如果存在一个稳定状态反馈控制律 $\phi(\eta)$ 及李雅普诺夫函数 $V(\eta)$ ，使方程(14.53)满足引理14.2的条件，则由引理及式(14.55)可得整个系统(14.53)～(14.54)的稳定状态反馈控制律

$$
\begin{array}{l} u = \phi_ {c} (\eta , \xi) \\ = \frac {1}{g _ {a} (\eta , \xi)} \left\{\frac {\partial \phi}{\partial \eta} [ f (\eta) + g (\eta) \xi ] - \frac {\partial V}{\partial \eta} g (\eta) - k [ \xi - \phi (\eta) ] - f _ {a} (\eta , \xi) \right\} \tag {14.56} \\ \end{array}
$$

对于 k > 0, 及李雅普诺夫函数

$$V _ {c} (\eta , \xi) = V (\eta) + \frac {1}{2} [ \xi - \phi (\eta) ] ^ {2} \tag {14.57}$$

迭代运用反步法,可稳定形如
