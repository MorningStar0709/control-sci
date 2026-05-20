# 6.6 动态规划与极小值原理

动态规划和极小值原理是最优控制理论的两大基石,它们都可以解决有约束的最优控制问题,虽然在形式上和解题方法上不同,但却存在着内在的联系。下面从动态规划来推演极小值原理,不过要说明这种推演是基于最优指标 $V(X,t)$ 对 X 和 t 两次连续可微这个条件的。设要解决的问题如下:系统状态方程为

$$\dot {\boldsymbol {X}} = \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \quad \boldsymbol {X} \left(t _ {0}\right) = \boldsymbol {X} _ {0} \tag {6-29}$$

要求确定 $U(t)$ 使性能指标

$$J = \phi [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \boldsymbol {F} (\boldsymbol {X}, \boldsymbol {U}, t) \mathrm{d} t \tag {6-30}$$

极小。其中， $t_{0}, t_{f}$ 固定， $X(t_{\mathrm{f}})$ 自由，U 可以有约束，也可以没有。

用极小值原理求解的结果可以由式(4-32)\~(4-37)来表示,因这里 $t_{f}$ 固定,故不需最优终端时刻条件; $X(t_{f})$ 自由,故无终端约束方程 $G[X(t_{f})]=0$ 。将最优解的条件再写在下面以对照。

1. $\dot{\pmb{X}} = \frac{\partial H}{\partial\pmb{\lambda}}$ （状态方程） (6-31)

2. $\dot{\pmb{\lambda}} = -\frac{\partial H}{\partial\pmb{X}}$ （协态方程） (6-32)

3. $X(t_0) = X_0$ （边界方程） (6-33)

4. $\pmb{\lambda}(t_{\mathrm{f}}) = \frac{\partial\phi}{\partial\pmb{X}(t_{\mathrm{f}})}$ （横截条件） (6-34)

5. $\min_{u\in \Omega}H(X^{*},\lambda^{*},U,t) = H(X^{*},\lambda^{*},U^{*},t)$ （极值条件）(6-35)

用动态规划求解的结果已在上节中得到,现在归纳一下:在动态规划中协态变量 $\lambda$ 满足

$$\lambda = \frac {\partial V}{\partial X}$$

哈密顿-雅可比-贝尔曼方程(6-28)本身说明了哈密顿函数 $H$ 在最优控制上取极值的条件，故等同于上面极小值原理所得的条件5，不过式(6-28)还多给出了一点信息，即 $H^{*} = -\frac{\partial V}{\partial t}$ 。

下面由动态规划法来推出协态方程。由(6-27)有

$$\dot {\boldsymbol {\lambda}} = \frac {\mathrm{d} \boldsymbol {\lambda}}{\mathrm{d} t} = \frac {\mathrm{d}}{\mathrm{d} t} \left[ \frac {\partial V (\boldsymbol {X} , t)}{\partial \boldsymbol {X}} \right] = \frac {\partial}{\partial t} \left[ \frac {\partial V (\boldsymbol {X} , t)}{\partial \boldsymbol {X}} \right] + \frac {\partial^ {2} V (\boldsymbol {X} , t)}{\partial \boldsymbol {X} \partial \boldsymbol {X} ^ {\mathrm{T}}} \frac {\mathrm{d} x}{\mathrm{d} t}$$

因假设 $V(X,t)$ 对 $X,t$ 两次连续可微，因此上式成立，且可交换求导次序，得
