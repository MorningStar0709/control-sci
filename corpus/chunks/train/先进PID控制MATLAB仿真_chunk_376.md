$$\dot {V} = - \frac {1}{2} \boldsymbol {\varepsilon} ^ {\mathrm{T}} Q \varepsilon + \hat {e} (\Delta - a u) - \frac {\dot {k} _ {0}}{\lambda_ {0}} (b - a k _ {0}) - \frac {\dot {k} _ {1}}{\lambda_ {1}} (a _ {2} - b _ {2} - a k _ {1}) - \frac {\dot {k} _ {2}}{\lambda_ {2}} (a _ {1} - b _ {1} - a k _ {2})$$

将式（7.24）中的 $\Delta$ 项和控制律式（7.27）代入上式，得

$$\hat {e} (\Delta - a u) = \hat {e r} (b - a k _ {0}) + \hat {e} \theta (a _ {2} - b _ {2} - a k _ {1}) + \hat {e} \dot {\theta} (a _ {1} - b _ {1} - a k _ {2})$$

则

$$\dot {V} = - \frac {1}{2} \boldsymbol {\varepsilon} ^ {\mathrm{T}} Q \boldsymbol {\varepsilon} + \left(\hat {e r} - \frac {\dot {k} _ {0}}{\lambda_ {0}}\right) (b - a k _ {0}) + \left(\hat {e} \theta - \frac {\dot {k} _ {1}}{\lambda_ {1}}\right) (a _ {2} - b _ {2} - a k _ {1}) + \left(\hat {e} \dot {\theta} - \frac {\dot {k} _ {2}}{\lambda_ {2}}\right) (a _ {1} - b _ {1} - a k _ {2})$$

设计自适应律为

$$\dot {k} _ {0} = \lambda_ {0} \hat {e r} \tag {7.29a}\dot {k} _ {1} = \lambda_ {1} \hat {e} \theta \tag {7.29b}\dot {k} _ {2} = \lambda_ {2} \hat {e} \dot {\theta} \tag {7.29c}$$

将以上三式代入 $\dot{V}$ 中，得

$$\dot {V} = - \frac {1}{2} \boldsymbol {\varepsilon} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {\varepsilon} \leqslant 0$$

当且仅当 $\varepsilon=0$ 时， $\dot{V}=0$ ，即当 $\dot{V}\equiv0$ 时， $\varepsilon\equiv0$ 。根据 LaSalle 不变性原理 $^{[1]}$ ，闭环系统为渐进稳定，当 $t\to\infty$ 时， $\varepsilon\to0$ ，即 $e\to0$ ， $\dot{e}\to0$ 。系统的收敛速度取决于 Q。

![](image/eff057c337687b201a884081fc7bcff93f07ac489404fd15ae999d1535da0af0.jpg)
