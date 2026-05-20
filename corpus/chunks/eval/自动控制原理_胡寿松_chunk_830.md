# (1) 问题描述

问题 10-3 设线性定常系统状态方程

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t), \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \tag {10-119}$$

性能指标

$$J = \frac {1}{2} \int_ {0} ^ {\infty} [ \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {Q} \boldsymbol {x} (t) + \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} \boldsymbol {u} (t) ] \mathrm{d} t \tag {10-120}$$

式中， $x(t)\in \mathbf{R}^n$ ； $u(t)\in \mathbf{R}^m$ ，无约束； $\pmb {A},\pmb {B},\pmb {Q}$ 和 $\pmb{R}$ 为维数适当的常值矩阵；权阵 $Q = Q^{\mathrm{T}}\geqslant 0,R =$ $R^{\mathrm{T}} > 0$ 。要求确定最优控制 $\pmb{u}^{*}(t)$ ，使性能指标(10-120)极小。
