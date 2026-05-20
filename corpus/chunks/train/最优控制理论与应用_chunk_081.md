# 5.3 终端时间有限时连续系统的状态调节器问题

考虑下面的系统状态方程和性能指标 J

$$\dot {\boldsymbol {X}} (t) = \boldsymbol {A} (t) \boldsymbol {X} (t) + \boldsymbol {B} (t) \boldsymbol {U} (t) \quad \boldsymbol {X} \left(t _ {0}\right) = \boldsymbol {X} _ {0} \tag {5-5}J = \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {P} \boldsymbol {X} \left(t _ {\mathrm{f}}\right) +\frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ \boldsymbol {X} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {X} (t) + \boldsymbol {U} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {U} (t) ] \mathrm{d} t \tag {5-6}$$

要求寻找最优控制 $U(t)$ ，使 J 最小。这里 $U(t)$ 无约束。P、 $Q(t)$ 为对称半正定阵， $R(t)$ 为对称正定阵。终端时间 $t_{f}$ 为有限值。
