# 3.2.1 泛函的自变量函数为标量函数的情况

为简单起见,先讨论自变量函数为标量函数(一维)的情况。要寻求极值曲线 $x(t)=x^{*}(t)$ ，使下面的性能泛函取极值

$$J = \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} F [ x (t), \dot {x} (t), t ] \mathrm{d} t \tag {3-1}$$

为此，让自变量函数 $x(t),\dot{x} (t)$ 在极值曲线 $x^{*}(t),\dot{x}^{*}(t)$ 附近发生微小变分 $\delta x,\delta \dot{x}$ ，即

$$
\begin{array}{l} x (t) = x ^ {*} (t) + \delta x (t) \\ \dot {x} (t) = \dot {x} ^ {*} (t) + \delta \dot {x} (t) \\ \end{array}
$$

于是泛函 $J$ 的增量 $\Delta J$ 可计算如下（以下将 \* 号省去）：

$$
\begin{array}{l} \Delta J = \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left\{F [ x + \delta x, \dot {x} + \delta \dot {x}, t ] - F [ x, \dot {x}, t ] \right\} d t \\ = \int_ {t _ {0}} ^ {t _ {f}} \left\{\frac {\partial F}{\partial x} \delta x + \frac {\partial F}{\partial \dot {x}} \delta \dot {x} + o [ (\delta x) ^ {2}, (\delta \dot {x}) ^ {2} ] \right\} d t \\ \end{array}
$$

上式中 $o[(\delta x)^2, (\delta \dot{x})^2]$ 是高阶项。

根据定义,泛函的变分 $\delta J$ 是 $\Delta J$ 的线性主部,即

$$\delta J = \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left[ \frac {\partial F}{\partial x} \delta x + \frac {\partial F}{\partial \dot {x}} \delta \dot {x} \right] \mathrm{d} t$$

对上式第二项作分部积分,按公式

$$\int_ {t _ {0}} ^ {t _ {\mathrm{f}}} u \mathrm{d} v = u v \left| _ {t _ {0}} ^ {t _ {\mathrm{f}}} - \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} v \mathrm{d} u \right.$$

可得

$$\delta J = \int_ {t _ {0}} ^ {t _ {f}} \left[ \frac {\partial F}{\partial x} - \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {\partial F}{\partial \dot {x}}\right) \right] \delta x \mathrm{d} t + \left. \frac {\partial F}{\partial \dot {x}} \delta x \right| _ {t _ {0}} ^ {t _ {f}} \tag {3-2}$$

$J$ 取极值的必要条件是 $\delta J$ 等于0。因 $\delta x$ 是任意的，要使式(3-2)中第一项（积分项）为0，必有

$$\frac {\partial F}{\partial x} - \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {\partial F}{\partial \dot {x}}\right) = 0 \tag {3-3}$$

上式称为欧拉－拉格朗日方程。

式(3-2)中第二项为0的条件要分两种情况来讨论：
