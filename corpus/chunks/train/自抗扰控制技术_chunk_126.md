$$\frac {\mathrm{d} t \left(x _ {1} , x _ {2}\right)}{\mathrm{d} t} = \frac {a s _ {1} x _ {2}}{2 \sqrt {s _ {1} \left(x _ {1} + s \frac {x _ {2} ^ {2}}{2 r _ {1}}\right)}} + \left(\frac {s}{r _ {1}} + \frac {x _ {2}}{r _ {1}} \frac {a s _ {1} s}{2 \sqrt {s _ {1} \left(x _ {1} + s \frac {x _ {2} ^ {2}}{2 r _ {1}}\right)}}\right) (- r _ {1} s) =\frac {a s _ {1} x _ {2}}{2 \sqrt {s _ {1} \left(x _ {1} + s \frac {x _ {2} ^ {2}}{2 r _ {1}}\right)}} + \left(- s s + \frac {a s _ {1} s s x _ {2}}{2 \sqrt {s _ {1} \left(x _ {1} + s \frac {x _ {2} ^ {2}}{2 r _ {1}}\right)}}\right) = - 1$$

在此,有意思的是如下一个显然的事实,即如下一个命题:

命题. 对一个二阶系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}) \end{array} \right. \tag {3.5.34}
$$

若有一个连续的李亚普诺夫函数 $V(x_{1},x_{2})$ ，满足不等式

$$\frac {\mathrm{d} V}{\mathrm{d} t} = \frac {\partial V}{\partial x _ {1}} x _ {2} + \frac {\partial V}{\partial x _ {2}} f (x _ {1}, x _ {2}) < - a, a = \text { const } > 0$$

那么在满足条件 $\left|\frac{\partial V(x_1,x_2)}{\partial x_2} w(t)\right| \leqslant a$ 的扰动 $w(t)$ 的作用下，受扰系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}) + w (t) \end{array} \right.
$$

仍然渐近稳定.

如果我们把 $f(x_{1},x_{2})$ 当作开环系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = u + w (t) \end{array} \right.
$$

中的状态反馈,那么上述事实可以解释成:状态反馈 $f(x_{1},x_{2})$ 能够抑制满足条件 $\left|\frac{\partial V(x_{1},x_{2})}{\partial x_{2}}w(t)\right|\leqslant a$ 的扰动 $w(t)$ 的作用,使闭环系统渐近稳定.

上述式(3.5.14)和式(3.5.33)给出的到达原点的时间函数 $T(x_{1},x_{2})$ 和 $t(x_{1},x_{2})$ 分别满足

$$\frac {\partial T}{\partial x _ {1}} x _ {2} + \frac {\partial T}{\partial x _ {2}} \left(- r \operatorname{sign} \left(x _ {1} + \frac {| x _ {2} | x _ {2}}{2 r}\right) = - 1 < 0 \right.\frac {\partial t}{\partial x _ {1}} x _ {2} + \frac {\partial t}{\partial x _ {2}} \left(- r _ {1} \operatorname{sign} \left(x _ {1} + \frac {| x _ {2} | x _ {2}}{2 r}\right)\right) = - 1 < 0, r _ {1} > r$$

因此对闭环系统(3.5.18)，(3.5.19)分别施加满足

$$\frac {\partial T}{\partial x _ {2}} w \left(x _ {1}, x _ {2}, t\right) < 1, \frac {\partial t}{\partial x _ {2}} w \left(x _ {1}, x _ {2}, t\right) < 1$$

的扰动 $w(x_{1},x_{2},t)$ 的系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r \operatorname{sign} \left(x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r}\right) + w (x _ {1}, x _ {2}, t) \end{array} \right.
$$

和系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r _ {1} \text {sign} \left(x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r}\right) + w (x _ {1}, x _ {2}, t), r _ {1} > r \end{array} \right.
$$

仍然渐近稳定.
