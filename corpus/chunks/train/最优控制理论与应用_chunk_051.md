$$
\begin{array}{l} \delta J _ {\mathrm{a}} = \left[ \frac {\partial \theta}{\partial X (t _ {\mathrm{f}})} \right] _ {*} ^ {\mathrm{T}} \delta X (t _ {\mathrm{f}}) + \left[ \frac {\partial \theta}{\partial t _ {\mathrm{f}}} \right] _ {*} \delta t _ {\mathrm{f}} + \\ \int_ {t _ {0}} ^ {t _ {f} ^ {*}} \left[ \left(\frac {\partial H}{\partial \boldsymbol {X}}\right) ^ {T} \delta \boldsymbol {X} + \left(\frac {\partial H}{\partial \boldsymbol {U}}\right) ^ {T} \delta \boldsymbol {U} - \boldsymbol {\lambda} ^ {T} \delta \dot {\boldsymbol {X}} \right] _ {*} d t + \\ \int_ {t _ {\mathrm{f}} ^ {*}} ^ {t _ {\mathrm{f}} ^ {*} + \delta t _ {\mathrm{f}}} \left[ H (\boldsymbol {X} + \delta \boldsymbol {X}, \boldsymbol {U} + \delta \boldsymbol {U}, \boldsymbol {\lambda}, t) - \boldsymbol {\lambda} ^ {\mathrm{T}} (\dot {\boldsymbol {X}} + \delta \dot {\boldsymbol {X}}) \right] _ {*} \mathrm{d} t \\ \end{array}
$$

对第三项作分部积分,可得

$$\int_ {t _ {0}} ^ {t _ {\mathrm{f}} ^ {*}} \left[ \left(\frac {\partial H}{\partial X} + \dot {\lambda}\right) ^ {\mathrm{T}} \delta X + \left(\frac {\partial H}{\partial U}\right) ^ {\mathrm{T}} \delta U \right] _ {*} \mathrm{d} t - \boldsymbol {\lambda} ^ {\mathrm{T}} \left(t _ {\mathrm{f}} ^ {*}\right) \delta X \left(t _ {\mathrm{f}} ^ {*}\right)$$

第四项可表示为(忽略二阶小量)

$$
\begin{array}{l} \int_ {t _ {\mathrm{f}} ^ {*}} ^ {t _ {\mathrm{f}} ^ {*} + \delta t _ {\mathrm{f}}} \left[ H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) + \left(\frac {\partial H}{\partial \boldsymbol {X}}\right) ^ {\mathrm{T}} \delta \boldsymbol {X} + \left(\frac {\partial H}{\partial \boldsymbol {U}}\right) ^ {\mathrm{T}} \delta \boldsymbol {U} - \boldsymbol {\lambda} ^ {\mathrm{T}} \dot {\boldsymbol {X}} - \boldsymbol {\lambda} ^ {\mathrm{T}} \delta \dot {\boldsymbol {X}} \right] _ {*} \mathrm{d} t \\ \approx H ^ {*} (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) \delta t _ {\mathrm{f}} - \boldsymbol {\lambda} ^ {\mathrm{T}} \left(t _ {\mathrm{f}} ^ {*}\right) \dot {\boldsymbol {X}} \left(t _ {\mathrm{f}} ^ {*}\right) \delta t _ {\mathrm{f}} \\ = H ^ {*} \delta t _ {f} - \boldsymbol {\lambda} ^ {T} \left(t _ {f} ^ {*}\right) \left[ \delta \boldsymbol {X} \left(t _ {f}\right) - \delta \boldsymbol {X} \left(t _ {f} ^ {*}\right) \right] \\ \end{array}
$$

上式最后一个等号用到了式(3-52)。 $H^{*}$ 表示 H 的自变量取最优值时 H 的值。

根据上面的结果可得
