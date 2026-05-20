$$\delta J _ {\mathrm{a}} = \delta \boldsymbol {X} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \frac {\partial \phi}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} - \delta \boldsymbol {X} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {\lambda} \left(t _ {\mathrm{f}}\right) +\int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left[ \delta \boldsymbol {X} ^ {\mathrm{T}} \left(\frac {\partial H}{\partial \boldsymbol {X}} + \dot {\boldsymbol {\lambda}}\right) + \delta \boldsymbol {U} ^ {\mathrm{T}} \frac {\partial H}{\partial \boldsymbol {U}} \right] \mathrm{d} t \tag {3-20}$$

$J_{a}$ 为极小的必要条件是: 对任意的 $\delta X, \delta U, \delta X(t_{f})$ ，变分 $\delta J_{a}$ 等于 0。由式(3-18)及(3-20)可得下面的一组关系式：

$$\dot {\boldsymbol {\lambda}} = - \frac {\partial H}{\partial \boldsymbol {X}} \quad (\text {协态方程}) \tag {3-21}\dot {\boldsymbol {X}} = \frac {\partial H}{\partial \boldsymbol {\lambda}} \quad (\text {状态方程}) \tag {3-22}\frac {\partial H}{\partial \boldsymbol {U}} = 0 \quad (\text {控制方程}) \tag {3-23}\boldsymbol {\lambda} \left(t _ {\mathrm{f}}\right) = \frac {\partial \phi}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} \quad (\text {横截条件}) \tag {3-24}$$

式(3-21)\~(3-24)即为 $J_{\mathrm{a}}$ 取极值的必要条件，由此即可求得最优值 $U^{*}(t),X^{*}(t),\lambda^{*}(t)$ 。式(3-22)即为状态方程，这可由 $H$ 的定义式(3-18)看出，实际解题时无需求 $\frac{\partial H}{\partial\lambda}$ ，只要直接用状态方程即可，这里为形式上对称而写成式(3-22)。式(3-21)与式(3-22)一起称为哈密顿正则方程。式(3-23)是控制方程，它表示 $H$ 在最优控制处取极值。注意，这是在 $\delta U$ 为任意时得出的方程，当 $U(t)$ 有界且在边界上取得最优值时，就不能用这方程，这时要用极小值原理求解。式(3-24)是在 $t_\mathrm{f}$ 固定、 $X(t_{\mathrm{f}})$ 自由时得出的横截条件。当 $X(t_{\mathrm{f}})$ 固定时， $\delta X(t_{\mathrm{f}}) = 0$ ，就不需要这个横截条件了。横截条件表示协态终端所满足的条件。

在求解式 $(3-21)\sim(3-24)$ 时,只知道初值 $X(t_{0})$ 和由横截条件 $(3-24)$ 求得的协态终端值 $\lambda(t_{\mathrm{f}})$ ,这种问题称为两点边值问题,一般情况下它们是很难求解的。因为 $\lambda(t_{0})$ 不知道,如果假定一个 $\lambda(t_{0})$ ,然后正向积分式 $(3-21)\sim(3-24)$ ,则在 $t=t_{f}$ 时的 $\lambda$ 值一般与给定的 $\lambda(t_{\mathrm{f}})$ 不同,于是要反复修正 $\lambda(t_{0})$ 的值,直至 $\lambda(t_{\mathrm{f}})$ 与给定值的差可忽略不计为止。非线性系统最优控制两点边值问题的数值求解是一个重要的研究领域。对于线性系统两点边值问题的求解,则可寻找缺少的边界条件,并只要进行一次积分,下面的例3-4给出了求解过程。

例3-3 设系统状态方程为

$$\dot {x} = - x (t) + u (t)$$

$x(t)$ 的边界条件为 $x(0) = 1, x(t_{\mathrm{f}}) = 0$ 。求最优控制 $u(t)$ ，使下列性能

指标

$$J = \frac {1}{2} \int_ {0} ^ {t _ {\mathrm{f}}} (x ^ {2} + u ^ {2}) \mathrm{d} t$$

为最小。
