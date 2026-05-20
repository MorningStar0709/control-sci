定理12.2 考虑前述假设下的闭环系统(12.58)\~(12.60)。假设对于所有 $t \geqslant 0, \rho(t)$ 是连续可微的， $\rho(t) \in S(D_{\rho}$ 的一个紧子集），并且 $\| \dot{\rho}(t) \| \leqslant \mu$ ，那么存在正常数 $k_{1}, k_{2}, k_{3}, k$ 和 $T$ ，使得如果当 $\mu < k_{1}$ 时 $\| \mathcal{X}(0) - \mathcal{X}_{\mathrm{ss}}(\rho(0), w) \| < k_{2}$ ，以及 $\varepsilon < k_{3}$ ，则对于所有 $t \geqslant 0, \mathcal{X}(t)$ 是一致有界的，且 $\| e(t) \| \leqslant k\mu, \quad \forall t \geqslant T$

进而, 当 t 趋于无穷时, 如果 $\rho(t)$ 趋于 $\rho_{ss}$ , 且 $\dot{\rho}(t)$ 趋于零, 则

$$e (t) \rightarrow 0$$

证明: 见附录 C.20。

这个定理说明如果分配变量缓慢变化,在初始时刻初始状态足够靠近平衡点,且 $\varepsilon$ 足够小,跟踪误差将最终与分配变量的导数具有相同的数量级,而且如果分配变量趋于常数极限,则跟踪误差将趋于零。

例12.6 考虑二阶系统

$$\dot {x} _ {1} = \tan x _ {1} + x _ {2}\dot {x} _ {2} = x _ {1} + uy = x _ {2}$$

其中 y 是唯一的被测信号, 即 $y_{m} = y$ 。希望 y 跟踪参考信号 r。以 r 作为分配变量, 当 $r = \alpha$ 为常数时, 平衡方程 (12.31) \~ (12.32) 有唯一解

$$
x _ {\mathrm{ss}} (\alpha) = \left[ \begin{array}{c} - \arctan \alpha \\ \alpha \end{array} \right], u _ {\mathrm{ss}} (\alpha) = \arctan \alpha
$$

采用基于观测器的积分控制器

$$\dot {\sigma} = e = y - r \tag {12.61}\dot {\hat {x}} = A (\alpha) \hat {x} + B u + H (\alpha) (y - C \hat {x}) \tag {12.62}u = - K _ {1} (\alpha) \hat {x} - K _ {2} (\alpha) \sigma \tag {12.63}$$

其中 $A(\alpha) = \left[ \begin{array}{cc}1 + \alpha^2 & 1\\ 1 & 0 \end{array} \right],B = \left[ \begin{array}{c}0\\ 1 \end{array} \right],C = \left[ \begin{array}{cc}0 & 1 \end{array} \right]$

$$
K _ {1} (\alpha) = \left[ (1 + \alpha^ {2}) (3 + \alpha^ {2}) + 3 + \frac {1}{1 + \alpha^ {2}} \quad 3 + \alpha^ {2} \right], \quad K _ {2} (\alpha) = - \frac {1}{1 + \alpha^ {2}}
H (\alpha) = \left[ \begin{array}{c} 1 0 + (4 + \alpha^ {2}) (1 + \alpha^ {2}) \\ (4 + \alpha^ {2}) \end{array} \right]
$$
