# 2. 有限时间时变状态调节器

当末端时刻 $t_{f}$ 有限时，有限时间时变状态调节器问题可以描述如下：

问题 10-2 设线性时变系统状态方程为

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} (t) \boldsymbol {x} (t) + \boldsymbol {B} (t) \boldsymbol {u} (t), \quad \boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0} \tag {10-96}$$

式中， $x(t)\in \mathbf{R}^n$ ； $u(t)\in \mathbf{R}^m$ ，无约束；矩阵 $\pmb {A}(t)$ 与 $\pmb {B}(t)$ 维数适当，其各元在 $[t_0,t_f]$ 上连续且有界。要求确定最优控制 $\pmb{u}^{*}(t)$ ，使性能指标(10-94)极小。其中，权阵 $F = F^{\mathrm{T}}\geqslant 0,Q(t) = Q^{\mathrm{T}}(t)\geqslant 0,$ $R(t) = R^{\mathrm{T}}(t) > 0$ ，其各元在 $[t_0,t_f]$ 上均连续且有界；末端状态 $\pmb {x}(t_f)$ 自由；末端时刻 $t_f$ 给定且有限。
