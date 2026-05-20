# (4) Bang-Bang 控制原理

对于线性定常系统,若系统正常,则可应用极小值原理求解时间最优控制问题,其最优控制在容许控制域内,从一个边界值来回切换到另一个边界值,形成 Bang-Bang 控制特色。其主要结果可以归纳为如下定理。

定理 10-17 对于问题 10-1, 若系统(10-74)正常, 则最优解的必要条件为

1）正则方程

$$
\begin{array}{l} \dot {\boldsymbol {x}} (t) = \frac {\partial H}{\partial \boldsymbol {\lambda}} = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t) \\ \dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}} = - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {\lambda} (t) \\ \end{array}
$$

式中，哈密顿函数

$$H (\boldsymbol {x}, \boldsymbol {u}, \lambda) = 1 + \lambda^ {\mathrm{T}} (t) [ \boldsymbol {A x} (t) + \boldsymbol {B u} (t) ]$$
