$$v _ {0} \left(t _ {\mathrm{f}} - t _ {0}\right) > \frac {1}{2} \left(a _ {p m} - a _ {e m}\right) \left(t _ {\mathrm{f}} - t _ {0}\right) ^ {2}$$

这表明由初始相对速度引起的位移大于由于机动加速度引起的位移，则从式(10-74)可得出解 $y(t_{\mathrm{f}})>0$ 。反之，若

$$v _ {0} \left(t _ {\mathrm{f}} - t _ {0}\right) < - \frac {1}{2} \left(a _ {p m} - a _ {e m}\right) \left(t _ {\mathrm{f}} - t _ {0}\right) ^ {2}$$

则可得出解 $y(t_{\mathrm{f}}) < 0$ 。于是有

$$
y (t _ {\mathrm{f}}) = \left\{ \begin{array}{l} \frac {1}{2} (t _ {\mathrm{f}} - t _ {0}) ^ {2} \left[ \frac {2 v _ {0}}{t _ {\mathrm{f}} - t _ {0}} - (a _ {p m} - a _ {e m}) \right] > 0, \text {若} \frac {2 v _ {0}}{(t _ {\mathrm{f}} - t _ {0}) (a _ {p m} - a _ {e m})} > 1 \\ - \frac {1}{2} (t _ {\mathrm{f}} - t _ {0}) ^ {2} \left[ \frac {- 2 v _ {0}}{t _ {\mathrm{f}} - t _ {0}} - (a _ {p m} - a _ {e m}) \right] <   0, \text {若} \frac {2 v _ {0}}{(t _ {\mathrm{f}} - t _ {0}) (a _ {p m} - a _ {e m})} <   - 1 \end{array} \right. \tag {10-75}
$$

式中，可将最优策略 $\pmb{u}^{*}$ 看成 $a_{pm},\pmb{v}^{*}$ 为 $a_{em}$ ；令非最优策略为 $\pmb{u} = a_{p} \leqslant a_{pm}$ ， $\pmb{v} = a_{e} \leqslant a_{em}$ 因为 $J = \frac{1}{2} y^{2}(t_{\mathrm{f}})$ ，由（10-75）可得出

$$J (a _ {p m}, a _ {e}) \leqslant J (a _ {p m}, a _ {e m}) \leqslant J (a _ {p}, a _ {e m})$$

即 $J(u^{*},v)\leqslant J(u^{*},v^{*})\leqslant J(u,v^{*})$

所以鞍点条件满足。

注意,对于

$$- 1 \leqslant \frac {2 v _ {0}}{\left(t _ {\mathrm{f}} - t _ {0}\right) \left(a _ {p m} - a _ {e m}\right)} \leqslant 1 \tag {10-76}$$

(10-74)无解。事实上，对于(10-76)这样的初始条件范围，追逐者总有可能使脱靶量为零。例如，只要选择 $a_{p}(t)$ 使

$$a _ {p} (t) = a _ {e} (t) + \frac {2 v _ {0} (t)}{t _ {\mathrm{f}} - t _ {0}} \tag {10-77}$$

便可做到这一点。这种问题已不是双方对策问题了。

例10-4 近地圆形轨道上的卫星拦截问题

设 A 为拦截卫星, B 为目标卫星。A 欲控制自己, 使在给定时间内尽可能接近 B; B 则控制自己, 使在此时间内尽可能远离 A。

A、B 两卫星的相对运动可用下面的状态方程表示

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {4} \\ \dot {x} _ {2} = x _ {5} \\ \dot {x} _ {3} = x _ {6} \\ \dot {x} _ {4} = 2 \omega x _ {5} + T _ {\mathrm{A}} \cos u _ {1} \cos u _ {2} - T _ {\mathrm{B}} \cos v _ {1} \cos v _ {2} \\ \dot {x} _ {5} = 3 \omega^ {2} x _ {2} - 2 \omega x _ {4} + T _ {\mathrm{A}} \cos u _ {1} \sin u _ {1} - T _ {\mathrm{B}} \cos v _ {1} \sin v _ {2} \\ \dot {x} _ {6} = - \omega^ {2} x _ {3} - T _ {\mathrm{A}} \sin u _ {1} - T _ {\mathrm{B}} \sin v _ {1} \end{array} \right. \tag {10-78}
$$

式中， $x_{1}, x_{2}, x_{3}$ 是两卫星之间的相对距离在直角坐标系上的投影分量； $\omega$ 是卫星运行的角速率； $T_{A}$ 、 $T_{B}$ 分别为作用在 A、B 卫星上的单位质量所受的推力幅值； $u_{1}$ 、 $u_{2}$ 是 $T_{A}$ 在直角坐标系中的两个方向角； $v_{1}$ 、 $v_{2}$ 是 $T_{B}$ 直角坐标系中的两个方向角。

性能指标是终端时间的相对距离的平方,即
