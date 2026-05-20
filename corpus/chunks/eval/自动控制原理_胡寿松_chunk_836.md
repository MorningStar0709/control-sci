# 4. 无限时间定常输出跟踪系统

对于无限时间输出跟踪系统问题,目前还没有严格的一般性求解方法。当理想输出为常值向量时,无限时间定常输出最优跟踪系统问题,有如下工程上可以应用的近似结果。

定理 10-23 设线性定常系统的动态方程为

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t), \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \tag {10-130}\mathbf {y} (t) = \mathbf {C x} (t)$$

式中， $x(t)\in\mathbb{R}^{n};u(t)\in\mathbb{R}^{m}$ ，无约束； $y(t)\in\mathbb{R}^{l},0<l\leqslant m\leqslant n;A,B,C$ 为维数适当的常值矩阵。

设 $\hat{z} \in \mathbf{R}^l$ 为理想输出常向量， $e(t)$ 为输出误差向量，由

$$\boldsymbol {e} (t) = \hat {\mathbf {z}} - \mathbf {y} (t) \tag {10-131}$$

定义性能指标

$$J = \frac {1}{2} \int_ {0} ^ {\infty} [ \boldsymbol {e} ^ {\mathrm{T}} (t) \boldsymbol {Q e} (t) + \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R u} (t) ] \mathrm{d} t \tag {10-132}$$

式中，权阵 Q 和 R 均为对称正定常值矩阵，维数适当。

若阵对 $\{A,B\}$ 完全可控，阵对 $\{A,C\}$ 完全可观，则使性能指标(10-132)极小的近似最优控制

$$\hat {\boldsymbol {u}} ^ {*} (t) = - \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \hat {\boldsymbol {P}} \boldsymbol {x} (t) + \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \hat {\boldsymbol {g}} \tag {10-133}$$

式中， $\hat{P}$ 为对称正定常阵，满足下列里卡蒂矩阵代数方程：

$$\hat {\boldsymbol {P}} \boldsymbol {A} + \boldsymbol {A} ^ {\mathrm{T}} \hat {\boldsymbol {P}} - \hat {\boldsymbol {P}} \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \hat {\boldsymbol {P}} + \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {C} = \mathbf {0} \tag {10-134}$$

常值伴随向量

$$\hat {\boldsymbol {g}} = \left[ \hat {\boldsymbol {P}} \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} - \boldsymbol {A} ^ {\mathrm{T}} \right] ^ {- 1} \boldsymbol {C} ^ {\mathrm{T}} \boldsymbol {Q} \hat {\boldsymbol {z}} \tag {10-135}$$

闭环系统方程

$$\dot {\boldsymbol {x}} (t) = \left(\boldsymbol {A} - \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \hat {\boldsymbol {P}}\right) \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \hat {\boldsymbol {g}}, \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \tag {10-136}$$

的解，为近似最优轨线 $\hat{\boldsymbol{x}}^{*}(t)$ 。

应当指出,定理 10-23 并没有论证闭环系统的稳定性,因此在实际应用时,需对闭环系统的渐近稳定性加以检验。

例10-15 设有一理想化轮船操纵系统，其从激励信号 $u(t)$ 到实际航向 $y(t)$ 的传递函数为 $4 / s^2$ ，试设计近似最优激励信号 $\hat{u}^{*}(t)$ ，使性能指标

$$J = \int_ {0} ^ {\infty} \left\{\left[ \hat {z} - y (t) \right] ^ {2} + u ^ {2} (t) \right\} \mathrm{d} t$$
