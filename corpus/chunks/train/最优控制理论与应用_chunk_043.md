# 3.2.2 泛函的自变量函数为向量函数的情况

现在, 将上面对 $x(t)$ 是标量函数时所得到的公式推广到 $X(t)$ 是 $n$ 维向量函数的情况。这时, 性能泛函为

$$J = \int_ {t _ {0}} ^ {t _ {f}} F (\boldsymbol {X}, \dot {\boldsymbol {X}}, t) \mathrm{d} t \tag {3-9}$$

式中

$$
\boldsymbol {X} = \left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \\ \vdots \\ x _ {n} (t) \end{array} \right] \quad \dot {\boldsymbol {X}} = \left[ \begin{array}{c} \dot {x} _ {1} (t) \\ \dot {x} _ {2} (t) \\ \vdots \\ \dot {x} _ {n} (t) \end{array} \right] \tag {3-10}
$$

泛函变分由式(3-2)改为

$$\delta J = \int_ {t _ {0}} ^ {t _ {f}} \delta \boldsymbol {X} ^ {\mathrm{T}} \left[ \frac {\partial F}{\partial \boldsymbol {X}} - \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {\partial F}{\partial \dot {\boldsymbol {X}}}\right) \right] \mathrm{d} t + \delta \boldsymbol {X} ^ {\mathrm{T}} \left. \frac {\partial F}{\partial \dot {\boldsymbol {X}}} \right| _ {t _ {0}} ^ {t _ {f}}$$

向量欧拉-拉格朗日方程为

$$\frac {\partial F}{\partial \boldsymbol {X}} - \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {\partial F}{\partial \dot {\boldsymbol {X}}}\right) = 0 \tag {3-11}$$

式中

$$
\frac {\partial F}{\partial \boldsymbol {X}} = \left[ \begin{array}{c} \frac {\partial F}{\partial x _ {1}} \\ \frac {\partial F}{\partial \dot {x} _ {2}} \\ \vdots \\ \frac {\partial F}{\partial x _ {n}} \end{array} \right] \quad \frac {\partial F}{\partial \dot {\boldsymbol {X}}} = \left[ \begin{array}{c} \frac {\partial F}{\partial \dot {x} _ {1}} \\ \frac {\partial F}{\partial \dot {x} _ {2}} \\ \vdots \\ \frac {\partial F}{\partial \dot {x} _ {n}} \end{array} \right] \tag {3-12}
$$

横截条件为(自由端点情况)

$$\frac {\partial F}{\partial \dot {X}} = 0 \qquad (\text {当} t = t _ {0} \text {和} t = t _ {\mathrm{f}} \text {时})$$

例3-1 求通过点 $(0,0)$ 及 $(1,1)$ 且使

$$J = \int_ {0} ^ {1} (x ^ {2} + \dot {x} ^ {2}) \mathrm{d} t$$

取极值的轨迹 $x^{*}(t)$ 。

解 这是固定端点问题,相应的欧拉-拉格朗日方程为

$$2 x - \frac {\mathrm{d}}{\mathrm{d} t} (2 \dot {x}) = 0$$

即

$$\ddot {x} - x = 0$$

它的通解形式为

$$x (t) = A \operatorname{ch} t + B \operatorname{sh} t$$

式中，ch $t = \frac{\mathrm{e}^t + \mathrm{e}^{-t}}{2}$ ,sh $t = \frac{\mathrm{e}^t - \mathrm{e}^{-t}}{2}$

由初始条件 $x(0) = 0$ ，可得 $A = 0$ 。再由终端条件 $x(1) = 1$ ，可得 $B = \frac{1}{\mathrm{sh}1}$ 因而极值轨迹为

$$x ^ {*} (t) = \frac {\mathrm{sh} t}{\mathrm{sh} 1}$$

例3-2 求使指标

$$J = \int_ {0} ^ {1} \left(\dot {x} ^ {2} + \dot {x} ^ {3}\right) d t$$

取极值的轨迹 $x^{*}(t)$ ，并要求 $x^{*}(0) = 0$ ，但对 $x^{*}(1)$ 没有限制。

解 这是终端自由的情况。欧拉-拉格朗日方程为

$$\frac {\mathrm{d}}{\mathrm{d} t} (2 \dot {x} + 3 \dot {x} ^ {2}) = 0$$

即

$$2 \dot {x} + 3 \dot {x} ^ {2} = \text {常数}$$

于是 $\dot{x}$ 是常数， $x$ 则是时间的线性函数，令

$$x (t) = A t + B$$

由 $x(0) = 0$ 可得 $B = 0$ ，又终端是自由的，由式(3-7)可得横截条件为

$$\left(\frac {\partial F}{\partial \dot {x}}\right) _ {t = 1} = (2 \dot {x} + 3 \dot {x} ^ {2}) _ {t = 1} = 0$$

即

$$2 A + 3 A ^ {2} = 0$$

由上式解得 A=0 或 $A=-\frac{2}{3}$ 。A=0 时的极值轨迹为 $x^{*}(t)=0; A=-\frac{2}{3}$ 时的极值轨迹为 $x^{*}(t)=-\frac{2t}{3}$ 。容易验证 $x(t)=0$ 时，J=0 对应局部极小； $x(t)=-\frac{2}{3}t$ 时， $J=\frac{4}{27}$ ，对应局部极大。
