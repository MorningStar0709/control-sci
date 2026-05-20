# 12.3.2 最优导引律的求解与仿真验证

当不考虑弹体惯性时,而且假定目标不机动,即 $a_{T}=0$ , 导弹运动状态方程为

$$\dot {\boldsymbol {X}} = \boldsymbol {A} \boldsymbol {X} + \boldsymbol {B} \boldsymbol {u} \tag {12-24}$$

指标函数为

$$J = \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {C X} \left(t _ {\mathrm{f}}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left(\boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {X} + \boldsymbol {u} ^ {\mathrm{T}} \boldsymbol {R} \boldsymbol {u}\right) \mathrm{d} t \tag {12-25}$$

式中，

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], \boldsymbol {B} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right], \boldsymbol {C} = \left[ \begin{array}{l l} c _ {1} & 0 \\ 0 & c _ {2} \end{array} \right], \boldsymbol {Q} = \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right]
$$

给出 $t = t_0$ 时刻， $\pmb{x}_1$ 和 $\pmb{x}_2$ 的初值 $\pmb{x}_1(t_0)$ 和 $\pmb{x}_2(t_0)$ ，采用极小值原理可求得最优控制 $\pmb{u}^*(t)$ 为

$$\boldsymbol {u} ^ {*} (t) = \frac {\left(c _ {1} \left(t _ {\mathrm{f}} - t\right) + \frac {c _ {1} c _ {2} \left(t _ {\mathrm{f}} - t\right) ^ {2}}{2 R}\right) \boldsymbol {x} _ {1} + \left(c _ {2} + c _ {1} \left(t _ {\mathrm{f}} - t\right) ^ {2} + \frac {c _ {1} c _ {2} \left(t _ {\mathrm{f}} - t\right) ^ {3}}{3 R}\right) \boldsymbol {x} _ {2}}{\boldsymbol {R} \left(1 + \frac {c _ {2} \left(t _ {\mathrm{f}} - t\right)}{R} + \frac {c _ {1} \left(t _ {\mathrm{f}} - t\right) ^ {3}}{3 R} + \frac {c _ {1} c _ {2} \left(t _ {\mathrm{f}} - t\right) ^ {4}}{1 2 R ^ {2}}\right)} \tag {12-26}$$

在指标函数中,如不考虑导弹的相对运动速度 $x_{2}$ 项,则可令 $c_{2}=0$ 。 $u^{*}(t)$ 变成

$$\boldsymbol {u} ^ {*} (t) = - \frac {c _ {1} (t _ {\mathrm{f}} - t) \boldsymbol {x} _ {1} + c _ {1} (t _ {\mathrm{f}} - t) ^ {2} \boldsymbol {x} _ {2}}{\boldsymbol {R} \left(1 + \frac {c _ {1} (t _ {\mathrm{f}} - t) ^ {3}}{3 \boldsymbol {R}}\right)} \tag {12-27}$$

以 $c_{1}$ 除上式的分子和分母，得

$$\boldsymbol {u} ^ {*} (t) = - \frac {3 (t _ {\mathrm{f}} - t) \boldsymbol {x} _ {1} + 3 (t _ {\mathrm{f}} - t) ^ {2} \boldsymbol {x} _ {2}}{\frac {3 R}{c _ {1}} + (t _ {\mathrm{f}} - t) ^ {3}} \tag {12-28}$$

为了使脱靶量为最小,应选取 $c_{1} \rightarrow \infty$ , 则

$$\boldsymbol {u} ^ {*} (t) = - 3 \left[ \frac {\boldsymbol {x} _ {1}}{\left(t _ {\mathrm{f}} - t\right) ^ {2}} + \frac {\boldsymbol {x} _ {2}}{t _ {\mathrm{f}} - t} \right] \tag {12-29}$$

根据图12-6可得

$$\tan q = \frac {x _ {1}}{y} = \frac {x _ {1}}{V _ {c} (t _ {\mathrm{f}} - t)}$$

当 q 比较小时, $\tan q = q$ , 则
