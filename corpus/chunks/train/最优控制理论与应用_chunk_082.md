# 5.3.1 用极小值原理求解上面的问题

因 $U(t)$ 无约束, 故等同于用经典变分法求解。取哈密顿函数为

$$H = \frac {1}{2} \left[ \boldsymbol {X} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {X} (t) + \boldsymbol {U} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {U} (t) \right] +\boldsymbol {\lambda} ^ {T} (t) [ \boldsymbol {A} (t) \boldsymbol {X} (t) + \boldsymbol {B} (t) \boldsymbol {U} (t) ] \tag {5-7}$$

最优解的必要条件如下：

协态方程为

$$\dot {\boldsymbol {\lambda}} = - \frac {\partial H}{\partial \boldsymbol {X}} = - [ \boldsymbol {Q} (t) \boldsymbol {X} (t) + \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) ] \tag {5-8}$$

控制方程为

$$\frac {\partial H}{\partial \boldsymbol {U}} = \boldsymbol {R} (t) \boldsymbol {U} (t) + \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) = \boldsymbol {0}\boldsymbol {U} = - \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) \tag {5-9}$$

因 $\boldsymbol{R}(t)$ 正定，故 $\boldsymbol{R}^{-1}(t)$ 存在，由上式可确定最优控制。为寻求最优反馈控制律还需把 $\boldsymbol{U}(t)$ 与状态 $\boldsymbol{X}(t)$ 联系起来。

横截条件为

$$\boldsymbol {\lambda} \left(t _ {\mathrm{f}}\right) = \frac {\partial \phi}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} = \frac {\partial}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} \left[ \frac {1}{2} \boldsymbol {X} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {P} \boldsymbol {X} \left(t _ {\mathrm{f}}\right) \right] = \boldsymbol {P} \boldsymbol {X} \left(t _ {\mathrm{f}}\right) \tag {5-10}$$

这里再一次遇到了两点边值问题(已知 $X(t_{0})$ 和 $\lambda(t_{f})$ )，如前所述，一般要试凑 $\lambda(t_{0})$ 再积分协态方程使 $\lambda(t_{f})$ 满足要求。但这里处理的是线性微分方程，可找到更简单的解法。从(5-10)可见，协态 $\lambda(t)$ 和状态 $X(t)$ 在终端时刻 $t_{f}$ 成线性关系。由此可以假定：

$$\boldsymbol {\lambda} (t) = \boldsymbol {K} (t) \boldsymbol {X} (t) \tag {5-11}$$

然后再来求出 $K(t)$ （这种方法称为扫描法）。将式(5-11)代入式(5-9)，再代入式(5-5)，得

$$\dot {\boldsymbol {X}} (t) = \boldsymbol {A} (t) \boldsymbol {X} (t) - \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) \boldsymbol {X} (t) \tag {5-12}$$

由式(5-11)和式(5-8)可得

$$\dot {\boldsymbol {\lambda}} (t) = \dot {\boldsymbol {K}} (t) \boldsymbol {X} (t) + \boldsymbol {K} (t) \dot {\boldsymbol {X}} (t) = - \boldsymbol {Q} (t) \boldsymbol {X} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) \boldsymbol {X} (t) \tag {5-13}$$

将式(5-12)代入式(5-13)可得
