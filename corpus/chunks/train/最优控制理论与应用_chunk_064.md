$$H \left(\boldsymbol {X} ^ {*}, \boldsymbol {\lambda} ^ {*}, \boldsymbol {U} ^ {*}, t\right) \leqslant H _ {U \in \Omega} \left(\boldsymbol {X} ^ {*}, \boldsymbol {\lambda} ^ {*}, \boldsymbol {U}, t\right) \tag {4-15}$$

或 $\min_{U\in \Omega}H(X^{*},\lambda^{*},U,t) = H(X^{*},\lambda^{*},U^{*},t)$

于是定常系统、末值型性能指标、 $t_{f}$ 固定、末端受约束情况下极小值原理得以证明。

总结上述讨论,可将庞特里亚金极小值原理写为如下形式:

定理(极小值原理):

系统状态方程

$$\dot {\boldsymbol {X}} = \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \quad \boldsymbol {X} (t) \in \mathbf {R} ^ {n}$$

初始条件

$$\boldsymbol {X} \left(t _ {0}\right) = \boldsymbol {X} _ {0}$$

控制向量 $U(t)\in \mathbb{R}^m$ ，并受下面的约束

$$\boldsymbol {U} \in \Omega$$

终端约束

$$\mathbf {G} \left[ \mathbf {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} \right] = \mathbf {0}$$

指标函数

$$J = \phi [ X (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} F (X, U, t) \mathrm{d} t$$

要求选择最优控制 $U^{*}(t)$ ，使 J 取极小值。

$J$ 取极小值的必要条件是 $X(t), U(t), \lambda(t)$ 和 $t_{\mathrm{f}}$ 满足下面的一组方程：

(1) 正则方程

$$\dot {\boldsymbol {\lambda}} = - \frac {\partial H}{\partial \boldsymbol {X}} \quad (\text {协态方程}) \tag {4-16}\dot {\boldsymbol {X}} = \frac {\partial H}{\partial \boldsymbol {\lambda}} \quad (\text {状态方程}) \tag {4-17}$$

(2) 边界条件

$$\boldsymbol {X} \left(t _ {0}\right) = \boldsymbol {X} _ {0} \quad \boldsymbol {G} \left[ \boldsymbol {X} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] = \mathbf {0} \tag {4-18}$$

(3) 横截条件

$$\boldsymbol {\lambda} \left(t _ {\mathrm{f}}\right) = \frac {\partial \phi}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {X} \left(t _ {\mathrm{f}}\right)} \boldsymbol {v} \tag {4-19}$$

(4) 最优终端时刻条件

$$H \left(t _ {\mathrm{f}}\right) = - \frac {\partial \phi}{\partial t _ {\mathrm{f}}} - \frac {\partial G ^ {\mathrm{T}}}{\partial t _ {\mathrm{f}}} \boldsymbol {v} \tag {4-20}$$

(5) 在最优轨线 $X^{*}(t)$ 和最优控制 $U^{*}(t)$ 上哈密顿函数取极小值

$$\min _ {U \in \Omega} H \left(\boldsymbol {X} ^ {*}, \boldsymbol {\lambda} ^ {*}, \boldsymbol {U}, t\right) = H \left(\boldsymbol {X} ^ {*}, \boldsymbol {\lambda} ^ {*}, \boldsymbol {U} ^ {*}, t\right) \tag {4-21}$$

将上面的结果与用古典变分法所得的结果(式 $(3-34)\sim(3-38)$ )对比可见,只是将 $\frac{\partial H}{\partial U}=0$ 这个条件用式 $(4-21)$ 代替,其他无变化。

应该指出, 当 $\frac{\partial H}{\partial U}$ 存在, 且 $\frac{\partial H}{\partial U} = 0$ 得出 $H$ 的绝对极小, 如图 4-1(a) 所示时, $\frac{\partial H}{\partial U} = 0$ 即为条件式 (4-21)。所以极小值原理可以解决变分法所能解决的问题, 还能解决变分法不能解决的问题。如何应用条件式 (4-21), 这是一个关键, 下面将用具体例子来说明。
