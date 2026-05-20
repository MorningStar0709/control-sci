$$\frac {\partial V \left(x _ {1} , x _ {2}\right)}{\partial x _ {1}} = \frac {1}{2 k ^ {2} \zeta} \left[ \left(k + k ^ {2} + 4 k ^ {2} \zeta^ {2}\right) x _ {1} + 2 k \zeta x _ {2} \right]\frac {\partial V \left(x _ {1} , x _ {2}\right)}{\partial x _ {2}} = \frac {1}{2 k ^ {2} \zeta} \left[ 2 k \zeta x _ {1} + (1 + k) x _ {2} \right]\dot {V} = \frac {\partial V (x _ {1} , x _ {2})}{\partial x _ {1}} x _ {2} + \frac {\partial V (x _ {1} , x _ {2})}{\partial x _ {2}} (- k x _ {1} - 2 k \zeta x _ {2} + w) =\frac {1}{2 k ^ {2} \zeta} \left[ (k + k ^ {2} + 4 k ^ {2} \zeta^ {2}) x _ {1} x _ {2} + 2 k \zeta x _ {2} ^ {2} \right] +\frac {1}{2 k ^ {2} \zeta} \left[ 2 k \zeta x _ {1} + x _ {2} + k x _ {2} \right] (- k x _ {1} - 2 k \zeta x _ {2} + w) =- (x _ {1} ^ {2} + x _ {2} ^ {2}) + \frac {1}{k} x _ {1} w + \frac {1 + k}{2 k ^ {2} \zeta} x _ {2} w \tag {3.2.23}\dot {V} = - \left(x _ {1} - \frac {w}{2 k}\right) ^ {2} - \left(x _ {2} - \frac {1 + k}{4 k ^ {2} \zeta} w\right) ^ {2} + \left(1 + \frac {(1 + k) ^ {2}}{4 k ^ {2} \zeta^ {2}}\right) \frac {w ^ {2}}{4 k ^ {2}}$$

欲使 $\dot{V} < 0$ 成立, 必须

$$\left(x _ {1} - \frac {w}{2 k}\right) ^ {2} + \left(x _ {2} - \frac {1 + k}{4 k ^ {2} \zeta} w\right) ^ {2} > \left(1 + \frac {(1 + k) ^ {2}}{4 k ^ {2} \zeta^ {2}}\right) \frac {w ^ {2}}{4 k ^ {2}}$$

这个不等式的意义是，所有以矩形 $|x_1| \leqslant \frac{1}{2k} |w|, |x_2| \leqslant \frac{1}{2k}\left(\frac{1+k}{2k\zeta}\right)|w|$ 之内的点为圆心，半径为 $\frac{|w|}{2k}\sqrt{1 + \left(\frac{1+k}{2k\zeta}\right)^2}$ 的圆内点的并集之外，将有

$$\dot {V} = \frac {\partial V}{\partial x _ {1}} \dot {x} _ {1} + \frac {\partial V}{\partial x _ {2}} \dot {x} _ {2} < 0$$

因此，当

$$\left| x _ {1} \right| > \frac {| w |}{2 k} \left[ 1 + \sqrt {1 + \left(\frac {1 + k}{2 k \zeta}\right) ^ {2}} \right],\left| x _ {2} \right| > \frac {| w |}{2 k} \left[ \frac {1 + k}{2 k \zeta} + \sqrt {1 + \left(\frac {1 + k}{2 k \zeta}\right) ^ {2}} \right]$$

时, 就有 $\dot{V} < 0$ . 如果 $\zeta > 0.5, k > 1$ (一般情况下是要满足这个条件的), 上面不等式可简化为

$$\left| x _ {1} \right| > 3 \frac {\left| w \right|}{k}, \left| x _ {2} \right| > 3 \frac {\left| w \right|}{k}$$

现在我们假定存在一常数 $w_0$ ，满足 $|w| < w_0$ （在实际系统中做这样的假定并不苛刻，因为实际有意义的系统的运行，大部分都是在有限范围之内进行的），那么在 $\zeta > 0.5, k > 1$ 的情况下，只要系统状态满足不等式

$$\mid x _ {1} \mid > 3 \frac {w _ {0}}{k}, \mid x _ {2} \mid > 3 \frac {w _ {0}}{k}$$

就有 $V < 0$ ，闭环系统的所有轨线都收敛到方形 $\mid x_{1}\mid \leqslant 3\frac{w_{0}}{k},$ $\mid x_2\mid \leqslant 3\frac{w_0}{k}$ 之内，因此闭环的稳态误差将限制在由不等式

$$\mid x _ {1} \mid \leqslant 3 \frac {w _ {0}}{k}, \mid x _ {2} \mid \leqslant 3 \frac {w _ {0}}{k} \tag {3.2.24}$$

限定的范围之内.
