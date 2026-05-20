# 5.2 线性二次型问题的提法

一般情况的线性二次型问题可表示如下：

设线性时变系统的方程为

$$\dot {\boldsymbol {X}} (t) = \boldsymbol {A} (t) \boldsymbol {X} (t) + \boldsymbol {B} (t) \boldsymbol {U} (t) \tag {5-1}\mathbf {Y} (t) = \mathbf {C} (t) \mathbf {X} (t) \tag {5-2}$$

其中， $X(t)$ 为 n 维状态向量， $U(t)$ 为 m 维控制向量， $Y(t)$ 为 l 维输出向量。设 $U(t)$ 不受约束。

令误差向量 $e(t)$ 为

$$\boldsymbol {e} (t) = Z (t) - Y (t) \tag {5-3}$$

其中， $Z(t)$ 为 l 维理想输出向量。寻找最优控制，使下面的性能指标最小

$$J (u) = \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \left(t _ {\mathrm{f}}\right) \boldsymbol {P e} \left(t _ {\mathrm{f}}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left[ \boldsymbol {e} ^ {\mathrm{T}} (t) \boldsymbol {Q} (t) \boldsymbol {e} (t) + \boldsymbol {U} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {U} (t) \right] \mathrm{d} t \tag {5-4}$$

其中， $\pmb{P}$ 是 $l \times l$ 对称半正定常数阵， $\pmb{Q}(t)$ 是 $l \times l$ 对称半正定阵， $\pmb{R}(t)$ 是 $m \times m$ 对称正定阵。一般将 $\pmb{P}, \pmb{Q}(t), \pmb{R}(t)$ 取成对角阵。

下面对性能指标 $J$ 中的每一项作一说明。因 $\pmb{R}(t)$ 为正定阵，则当 $\pmb {U}(t)\neq \pmb{0}$ ，就有 $\pmb{U}^{\mathrm{T}}(t)\pmb {R}(t)\pmb {U}(t) > 0$ 。例如

$$
\boldsymbol {U} (t) = \left[ \begin{array}{l} u _ {1} (t) \\ u _ {2} (t) \end{array} \right] \quad \boldsymbol {R} (t) = \left[ \begin{array}{c c} r _ {1} (t) & 0 \\ 0 & r _ {2} (t) \end{array} \right]
$$

设 $r_1(t) > 0, r_2(t) > 0$ ，则 $\pmb{R}(t)$ 为正定阵，于是

$$\frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \boldsymbol {U} ^ {\mathrm{T}} (t) \boldsymbol {R} (t) \boldsymbol {U} (t) \mathrm{d} t = \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left[ r _ {1} (t) u _ {1} ^ {2} (t) + r _ {2} (t) u _ {2} ^ {2} (t) \right] \mathrm{d} t$$

它与消耗的控制能量成正比，消耗得越多，则性能指标值 $J$ 越大。故性能指标中这一项表示了对消耗控制能量的惩罚。 $r_1(t), r_2(t)$ 可看作加权系数，如认为 $u_1(t)$ 的重要性大于 $u_2(t)$ ，则可加大 $r_1(t)$ 。将 $\pmb{R}(t)$ 选成时间函数，是为了对不同时刻的 $U(t)$ 加权不一样。实际上，为了简单起见常选用常数阵 $\pmb{R}$ 。 $\pmb{Q}(t)$ 为半正定阵，则当 $\pmb{e}(t) \neq \mathbf{0}$ ，就有 $\pmb{e}^{\mathrm{T}}(t)\pmb{Q}(t)\pmb{e}(t) \geqslant 0, \frac{1}{2} \int_{t_0}^{t_f} e^{\mathrm{T}}(t) \pmb{Q}(t) e(t) \mathrm{d}t$ 表示误差平方和积分，故这项表示对系统误差的惩罚。 $\frac{1}{2} e^{\mathrm{T}}(t_f) Pe(t_f)$ 表示对终端误差的惩罚，当对终端误差要求较严时，可将这项加到性能指标中。总之，性能指标 $J(u)$ 最小表示了要用不大的控制量来保持较小的误差，以达到能量和误差的综合最优。

下面讨论几种特殊情况：

（1）调节器问题。这时 $C(t)=I$ （单位阵），理想输出 $Z(t)=0$ ，则 $Y(t)=X(t)=-e(t)$ ，这时，问题归结为用不大的控制量使 $X(t)$ 保持在零值附近。因而称为状态调节器问题。例如电机转速调节系统中，由于外加电压波动使转速偏离要求值，通过施加控制使转速偏差趋于 0。

（2）伺服机问题。这时 $\mathbf{Z}(t) \neq \mathbf{0}, e(t) = \mathbf{Z}(t) - \mathbf{Y}(t)$ ，这时要用不大的控制量使 $\mathbf{Y}(t)$ 跟踪 $\mathbf{Z}(t)$ ，因而称为跟踪问题。例如，用雷达跟踪飞行器的运动，通过控制使跟踪误差趋于 0。
