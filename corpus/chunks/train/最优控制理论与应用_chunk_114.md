# 6.5 连续系统的动态规划

设系统的状态方程和性能指标为

$$\dot {\boldsymbol {X}} = \boldsymbol {f} (t, \boldsymbol {X}, \boldsymbol {U}) \quad \boldsymbol {X} (t _ {0}) = \boldsymbol {X} _ {0} \tag {6-19}J = \phi [ X (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} F (X, U, t) \mathrm{d} t \tag {6-20}$$

U 受约束, 可写成 $U \in \Omega, \Omega$ 为某一闭集。要寻找满足此约束且使 J 最小的最优控制 U。

设时间 t 在区间 $[t_{0}, t_{f}]$ 内，则根据最优性原理，从 t 到 $t_{f}$ 这一段过程应当是最优过程。把这段最优指标写成 $V(X, t)$ ，则

$$V (X, t) \triangleq J ^ {*} (X, t) = \min _ {u \in \Omega} \left\{\phi \left[ X \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] + \int_ {t} ^ {t _ {\mathrm{f}}} F (X, U, \tau) \mathrm{d} \tau \right\} \tag {6-21}$$

显然 $V(X,t)$ 满足终端条件

$$V \left[ X \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] = \phi \left[ X \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] \tag {6-22}$$

通常假定 $V(X,t)$ 对 $\pmb{X}$ 及 $t$ 的二阶偏导数存在且有界。

现在,考虑系统从 t 出发,到 $t_{f}$ 分两步走:先从 t 到 $t + \Delta t$ ,再从 $t + \Delta t$ 到 $t_{f}, \Delta t$ 是小量,则

$$V (\boldsymbol {X}, t) = \min _ {u \in \Omega} \left\{\phi \left[ \boldsymbol {X} \left(t _ {\mathrm{f}}, t _ {\mathrm{f}}\right) \right] + \int_ {t} ^ {t + \Delta t} F (\boldsymbol {X}, \boldsymbol {U}, \tau) \mathrm{d} \tau + \int_ {t + \Delta t} ^ {t _ {\mathrm{f}}} F (\boldsymbol {X}, \boldsymbol {U}, \tau) \mathrm{d} \tau \right\} \tag {6-23}$$

根据最优性原理,从 $t + \Delta t$ 到 $t_{f}$ 也应是最优过程。因 $X(t + \Delta t) \approx X + \dot{X} \Delta t$ , 故

$$V (X + \dot {X} \Delta t, t + \Delta t) = \min _ {u \in \Omega} \left\{\phi [ X (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t + \Delta t} ^ {t _ {\mathrm{f}}} F (X, U, \tau) \mathrm{d} \tau \right\}$$

这样,式(6-23)可写成

$$
\begin{array}{l} V (\boldsymbol {X}, t) = \min _ {u \in \Omega} \left\{F (\boldsymbol {X}, \boldsymbol {U}, t) \Delta t + V (\boldsymbol {X} + \dot {\boldsymbol {X}} \Delta t, t + \Delta t) \right\} \\ = \min _ {u \in \Omega} \left\{F (X, U, t) \Delta t + V (X, t) + \right. \\ \left. \left(\frac {\partial V}{\partial X}\right) ^ {T} \Delta X + \frac {\partial V}{\partial t} \Delta t + o \left(\Delta t ^ {2}\right) \right\} \tag {6-24} \\ \end{array}
$$

注意到 $\Delta X = \dot{X}\Delta t = f(X,U,t)\Delta t$ ，上式右边括号中 $V(X,t)$ 表示最优指标，其中 $\pmb{U}$ 为最优控制，不需再选择， $\frac{\partial V}{\partial t}\Delta t$ 也与 $\pmb{U}$ 选择无关。故
