$$
\begin{array}{l} \delta J _ {\mathrm{a}} = \left[ \frac {\partial \theta}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} \right] _ {*} ^ {\mathrm{T}} \delta \boldsymbol {X} \left(t _ {\mathrm{f}}\right) + \left[ \frac {\partial \theta}{\partial t _ {\mathrm{f}}} \right] _ {*} \delta t _ {\mathrm{f}} + \\ \int_ {t _ {0}} ^ {t _ {\mathrm{f}} ^ {*}} \left[ \left(\frac {\partial H}{\partial X} + \dot {\lambda}\right) ^ {\mathrm{T}} \delta X + \left(\frac {\partial H}{\partial U}\right) ^ {\mathrm{T}} \delta U \right] _ {*} \mathrm{d} t + H ^ {*} \delta t _ {\mathrm{f}} - \boldsymbol {\lambda} ^ {\mathrm{T}} \left(t _ {\mathrm{f}} ^ {*}\right) \delta X \left(t _ {\mathrm{f}}\right) \\ \end{array}
$$

$J_{a}$ 取极值的必要条件为 $\delta J_{a}=0$ ，因 $\delta X(t_{\mathrm{f}})$ 、 $\delta t_{f}$ 、 $\delta X$ 、 $\delta U$ 为任意，故得（省去 \* 号）

$$\dot {\lambda} = - \frac {\partial H}{\partial \boldsymbol {X}} \quad (\text {协态方程}) \tag {3-53}\dot {X} = \frac {\partial H}{\partial \boldsymbol {\lambda}} \quad (\text {状态方程}) \tag {3-54}\frac {\partial H}{\partial \boldsymbol {U}} = 0 \quad (\text {控制方程}) \tag {3-55}\boldsymbol {\lambda} \left(t _ {\mathrm{f}}\right) = \frac {\partial \theta}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} = \frac {\partial \phi}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} \boldsymbol {v} \quad (\text {横截方程}) \tag {3-56}H \left(t _ {\mathrm{f}}\right) = - \frac {\partial \theta}{\partial t _ {\mathrm{f}}} = - \frac {\partial \phi}{\partial t _ {\mathrm{f}}} - \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial t _ {\mathrm{f}}} \boldsymbol {v} \tag {3-57}$$

与 $t_{f}$ 固定情况相比, 这里多了一个方程, $H(t_{\mathrm{f}}) = -\frac{\partial\theta}{\partial t_{\mathrm{f}}}$ , 用它可求出最优终端时间 $t_{f} = t_{f}^{*}$ 。

例3-5 设系统状态方程为

$$\dot {x} = u$$

边界条件为

$$x (0) = 1 \qquad x (t _ {\mathrm{f}}) = 0 \qquad t _ {\mathrm{f}} \text {自由}$$

性能指标为

$$J = t _ {\mathrm{f}} + \frac {1}{2} \int_ {0} ^ {t _ {\mathrm{f}}} u ^ {2} \mathrm{d} t$$

要求确定最优控制 $u^{*}$ ，使 J 最小。

解 这是 $t_{f}$ 自由问题。终端状态固定， $x(t_{f})=0$ 是满足约束集的特殊情况，即

$$\boldsymbol {G} \left[ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} \right] = x (t _ {\mathrm{f}}) = 0$$

作哈密顿函数

$$H = \frac {1}{2} u ^ {2} + \lambda u$$

正则方程是
