# (1) 最小时间控制问题

问题10-1 设线性定常系统

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t) \tag {10-74}$$

是完全可控的， $x(t)\in \mathbf{R}^n,u(t)\in \mathbf{R}^m,A,B$ 为维数适当的常阵。求满足下列不等式约束的容许控制：

$$\mid u _ {j} (t) \mid \leqslant 1; \quad j = 1, 2, \dots , m$$

使系统(10-74)从已知初态 $x(0) = x_0$ 转移到 $x(t_f) = 0$ ，并使性能指标

$$J = \int_ {0} ^ {t _ {f}} \mathrm{d} t \tag {10-75}$$

极小，其中 $t_f$ 自由。

求解问题 10-1 之前, 应首先判断该问题是否可用极小值原理求解? 可以证明, 只有当系统 (10-74) 正常时, 才能应用极小值原理求得最优解。
