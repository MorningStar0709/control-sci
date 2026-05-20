$$\dot {\hat {z}} = A _ {\mathrm{s}} \hat {z} + B _ {\mathrm{s}} u + L (e - C _ {\mathrm{s}} \hat {z}) \tag {7.252a}u = - \mathbf {K} \hat {\mathbf {x}} - \hat {\rho} \tag {7.252b}$$

按照原始变量，估计器方程为

$$
\dot {\hat {z}} = \left[ \begin{array}{c} \dot {\hat {\rho}} \\ \ddot {\hat {\rho}} \\ \dot {\hat {x}} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & \mathbf {0} \\ - \alpha_ {2} & - \alpha_ {1} & \mathbf {0} \\ \boldsymbol {B} & \mathbf {0} & \boldsymbol {A} \end{array} \right] \left[ \begin{array}{c} \hat {\rho} \\ \dot {\hat {\rho}} \\ \hat {x} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ \boldsymbol {B} \end{array} \right] u + \left[ \begin{array}{c} l _ {1} \\ l _ {2} \\ L _ {3} \end{array} \right] [ e - C   \hat {x} ] \tag {7.253}
$$

系统设计的总框图如图 7.71b 所示。若写出式(7.253)中含 $\hat{x}$ 的最后一个方程，并代入式(7.252b)，消掉含 $\hat{\rho}$ 的项，得到了结果的简化形式为

$$\dot {\hat {x}} = \boldsymbol {B} \hat {\rho} + \boldsymbol {A} \hat {x} + \boldsymbol {B} (- \boldsymbol {K} \hat {x} - \hat {\rho}) + \boldsymbol {L} _ {3} (e - \boldsymbol {C} \hat {x})= \boldsymbol {A} \hat {\boldsymbol {x}} + \boldsymbol {B} (- \boldsymbol {K} \hat {\boldsymbol {x}}) + \boldsymbol {L} _ {3} (e - \boldsymbol {C} \hat {\boldsymbol {x}})= \boldsymbol {A} \hat {\boldsymbol {x}} + \boldsymbol {B} \bar {u} + \boldsymbol {L} _ {3} (e - \boldsymbol {C} \hat {\boldsymbol {x}})$$

由式 $(7.253)$ 的估计器和式 $(7.252b)$ 的控制，可得状态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} (- \boldsymbol {K} \hat {\boldsymbol {x}} - \hat {\rho}) + \boldsymbol {B} _ {\rho} \tag {7.254}$$

根据估计误差，式 $(7.254)$ 可改写为

$$\dot {x} = (A - B K) x + B K \widetilde {x} + B \widetilde {p} \tag {7.255}$$

由于设计的估计器必须为稳定的，所以稳态下， $\widetilde{\rho}$ 与 $\widetilde{x}$ 的值趋于零，而且状态的终值不会受到外部输入的影响。用于实现的系统框图由图7.71c给出。下面给出一个非常简单的例子来说明设计的步骤。
