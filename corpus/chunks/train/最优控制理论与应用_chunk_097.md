# 5.6 伺服跟踪问题

设系统的状态方程和输出方程为

$$\boldsymbol {X} (t) = \boldsymbol {A} (t) \boldsymbol {X} (t) + \boldsymbol {B} (t) \boldsymbol {U} (t) \quad \boldsymbol {X} \left(t _ {0}\right) = \boldsymbol {X} _ {0} \tag {5-85}\boldsymbol {Y} (t) = \boldsymbol {C} (t) \boldsymbol {X} (t) \tag {5-86}$$

其中，X 为 n 维，U 为 m 维，Y 为 q 维。设理想输出为 $Z(t)$ ，跟踪误差 $e(t)$ 为

$$\boldsymbol {e} (t) = \mathbf {Z} (t) - \mathbf {Y} (t) \tag {5-87}$$

寻找控制 $u(u$ 不受约束)使下列性能指标最小：

$$J = \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {P e} \left(t _ {\mathrm{f}}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left[ \boldsymbol {e} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {e} (t) + \boldsymbol {U} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {U} (t) \right] \mathrm{d} t \tag {5-88}$$

其中 $R(t)$ 为正定阵， $P, Q(t)$ 为半正定阵， $t_{f}$ 给定。

跟踪问题的哈密顿函数为

$$H = \frac {1}{2} [ \boldsymbol {Z} (t) - \boldsymbol {C} (t) \boldsymbol {X} (t) ] ^ {\mathrm{T}} \boldsymbol {Q} (t) [ \boldsymbol {Z} (t) - \boldsymbol {C} (t) \boldsymbol {X} (t) ] +\frac {1}{2} \boldsymbol {U} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {U} (t) + \boldsymbol {\lambda} ^ {\mathrm{T}} (t) [ \boldsymbol {A} (t) \boldsymbol {X} (t) + \boldsymbol {B} (t) \boldsymbol {U} (t) ] \tag {5-89}$$

因 $\pmb{U}$ 无约束，由控制方程

$$\frac {\partial H}{\partial \boldsymbol {U}} = \boldsymbol {R} (t) \boldsymbol {U} (t) + \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) = 0$$

可得

$$\boldsymbol {U} (t) = - \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) \tag {5-90}$$

由协态方程得出

$$\dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {X} (t)} = - \boldsymbol {C} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {C} (t) \boldsymbol {X} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) +\boldsymbol {C} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {Z} (t) \tag {5-91}$$

由横截条件得
