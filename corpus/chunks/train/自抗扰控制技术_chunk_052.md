当然,这种做法只能用于参数 $a_{1}$ 确知的情形.如果对参数 $a_{1}$ 的估计有误差,那么按上述方式确定的 PID 增益,使闭环的过渡过程将会变形,即这种做法对参数 $a_{1}$ 的估计误差很敏感.

然而,如果我们在安排过渡过程的基础上运用这种时间尺度变换的办法,那么对对象参数的认知程度就大为宽松了.

原先对二阶系统

$$
\left\{ \begin{array}{l} \ddot {x} = - a _ {1} x - a _ {2} \dot {x} + u \\ y = x \end{array} \right. \tag {1.5.17}
$$

施加 PID 控制律所得的闭环系统为

$$
\left\{ \begin{array}{l} \ddot {x} = - a _ {1} x - a _ {2} \dot {x} + k _ {0} \int_ {0} ^ {t} e (\tau) \mathrm{d} \tau + k _ {1} e + k _ {2} \dot {e} \\ y = x \end{array} \right.
$$

如果事先安排一个光滑的过渡过程 $v(t)$ ，那么有

$$e = v (t) - x, \dot {e} = \dot {v} (t) - \dot {x}, \ddot {e} = \ddot {v} (t) - \ddot {x} \tag {1.5.18}$$

于是安排过渡过程时的闭环方程变成

$$
\left\{ \begin{array}{l} \ddot {e} = - (a _ {1} + k _ {1}) e - (a _ {2} + k _ {2}) \dot {e} - k _ {0} \int_ {0} ^ {t} e (\tau) \mathrm{d} \tau + \\ \quad \ddot {v} (t) + a _ {1} v (t) + a _ {2} \dot {v} (t) \\ y = v (t) - e \end{array} \right.
$$

今记

$$
e _ {0} = \int_ {0} ^ {t} e (\tau) \mathrm{d} \tau , e _ {1} = e, e _ {2} = \dot {e},w (t) = \ddot {v} (t) + a _ {1} v (t) + a _ {2} \dot {v} (t) \tag {1.5.19}
\left\{ \begin{array}{l l} \dot {e} _ {0} = e _ {1}, & e _ {0} (0) = 0 \\ \dot {e} _ {1} = e _ {2}, & e _ {1} (0) = 0 \\ \dot {e} _ {2} = - k _ {0} e _ {0} - \left(a _ {1} + k _ {1}\right) e _ {1} - \left(a _ {2} + k _ {2}\right) e _ {2} + w (t), & e _ {2} (0) = 0 \\ y = v (t) - e _ {1} \end{array} \right. \tag {1.5.20}
$$

今取安排的过渡过程为如下函数(见式 $(1.4.7)$ )

$$
v (t) = \left\{ \begin{array}{c c} \frac {v _ {0}}{2} \left(1 + \sin \left(\pi \left(\frac {t}{T _ {0}} - \frac {1}{2}\right)\right)\right), & t \leqslant T _ {0} \\ v _ {0}, & t > T _ {0} \end{array} \right.
$$

其一阶，二阶导数为

$$
\dot {v} (t) = \left\{ \begin{array}{c c} \frac {v _ {0}}{2} \frac {\pi}{T _ {0}} \cos \left(\pi \left(\frac {t}{T _ {0}} - \frac {1}{2}\right)\right), & t \leqslant T _ {0} \\ 0, & t > T _ {0} \end{array} \right.

\ddot {v} (t) = \left\{ \begin{array}{c c} - \frac {v _ {0}}{2} \left(\frac {\pi}{T _ {0}}\right) ^ {2} \sin \left(\pi \left(\frac {t}{T _ {0}} - \frac {1}{2}\right)\right), & t \leqslant T _ {0} \\ 0, & t > T _ {0} \end{array} \right.
$$

把这些表达式代到方程(1.5.20)中,就可以做仿真对比了.

现在取对象(1.5.17)的参数为 $a_{1}=1,a_{2}=1$ （是“标准”对象），设定值为 $v_{0}=1$ ，而安排的过渡过程时间为 $T_{0}=2$ . PID控制律增益分别取

$$k _ {0} = 5 0, k _ {1} = 5 0, k _ {2} = 5 0;k _ {0} = 3 0, k _ {1} = 3 0, k _ {2} = 3 0;k _ {0} = 7 0, k _ {1} = 7 0, k _ {2} = 7 0$$

所作的仿真结果示于图 1.5.5.

这个仿真结果说明,安排了过渡过程之后:

(1) 由于“误差”本身很小, PID 的增益都可以取比较大的值.  
(2) 对给定的对象来说,保证过渡过程品质的 PID 增益的允许范围很大.  
(3) 对给定的 PID 增益来说, 它所能控制的对象范围很大.
