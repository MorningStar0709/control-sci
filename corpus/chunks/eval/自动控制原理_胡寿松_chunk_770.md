\boldsymbol {f} = \left[ \begin{array}{l} f _ {1} \\ f _ {2} \end{array} \right] = \left[ \begin{array}{l} x _ {2} - \dot {x} _ {1} \\ u - \dot {x} _ {2} \end{array} \right]
$$

故拉格朗日标量函数

$$L = g + \boldsymbol {\lambda} ^ {T} \boldsymbol {f} = \frac {1}{2} u ^ {2} + \lambda_ {1} (x _ {2} - \dot {x} _ {1}) + \lambda_ {2} (u - \dot {x} _ {2})$$

欧拉方程

$$\frac {\partial L}{\partial x _ {1}} - \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {x} _ {1}} = \dot {\lambda} _ {1} = 0, \quad \lambda_ {1} = a\frac {\partial L}{\partial x _ {2}} - \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {x} _ {2}} = \lambda_ {1} + \dot {\lambda} _ {2} = 0, \quad \lambda_ {2} = - a t + b\frac {\partial L}{\partial u} - \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {u}} = u + \lambda_ {2} = 0, \quad u = a t - b$$

式中，常数 $a, b$ 待定。

由状态约束方程

$$\dot {x} _ {2} = u = a t - b, \quad x _ {2} = \frac {1}{2} a t ^ {2} - b t + c\dot {x} _ {1} = x _ {2} = \frac {1}{2} a t ^ {2} - b t + c, \qquad x _ {1} = \frac {1}{6} a t ^ {3} - \frac {1}{2} b t ^ {2} + c t + d$$

式中，常数 $c, d$ 待定。代入已知边界条件： $x_{1}(0) = 1, x_{2}(0) = 1, x_{1}(2) = 0, x_{2}(2) = 0$ ，可求得

$$a = 3, \quad b = 3. 5, \quad c = d = 1$$

于是极值轨线

$$x _ {1} ^ {*} (t) = 0. 5 t ^ {3} - 1. 7 5 t ^ {2} + t + 1x _ {2} ^ {*} (t) = 1. 5 t ^ {2} - 3. 5 t + 1$$

极值控制

$$u ^ {*} (t) = 3 t - 3. 5$$
