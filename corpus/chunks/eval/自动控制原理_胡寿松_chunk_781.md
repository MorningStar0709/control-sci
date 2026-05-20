$$\boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0}, \quad \psi [ \boldsymbol {x} (t _ {f}) ] = \mathbf {0}\boldsymbol {\lambda} (t _ {f}) = \frac {\partial \varphi}{\partial \boldsymbol {x} (t _ {f})} + \frac {\partial \boldsymbol {\psi} ^ {\mathrm{T}}}{\partial \boldsymbol {x} (t _ {f})} \boldsymbol {\gamma}$$

3) 极值条件

$$\frac {\partial H}{\partial \boldsymbol {u}} = \boldsymbol {0}$$

定理 10-6 是 $t_{f}$ 固定、末端 $x(t_{f})$ 受约束时泛函极值的必要条件，通过适当修改，其结论可以移植到末端自由和末端固定时的情况。

当末端时刻 $t_f$ 固定、末端 $\pmb{x}(t_f)$ 自由时，由于不存在目标集条件(10-42)，因此在定理10-6的结论中，删除向量 $\psi[\pmb{x}(t_f)]$ ，即为 $t_f$ 固定、 $\pmb{x}(t_f)$ 自由时泛函极值的必要条件。这一结论，通过定理10-6的推导过程明显可见。

当末端时刻 $t_f$ 固定、末端 $\pmb{x}(t_f) = \pmb{x}_f$ 固定时，由于 $\delta \pmb{x}(t_0) = \mathbf{0}$ 以及 $\delta \pmb{x}(t_f) = \mathbf{0}$ ，广义泛函 $J_{a}$ 的一次变分(10-45)变成

$$\delta J _ {a} = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial H}{\partial x} + \dot {\lambda}\right) ^ {T} \delta x + \left(\frac {\partial H}{\partial u}\right) ^ {T} \delta u \right] d t \tag {10-50}$$

式中， $\delta x$ 是任意的，但容许控制变分 $\partial u$ 不再是完全任意的，必须满足某些限制条件。卡尔曼曾经论证：若系统完全可控，同样可以导出 $\partial H / \partial u = 0$ 的极值条件。因此，在系统可控条件下，令式(10-50)为零，由变分预备定理得

$$\dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}}, \quad \frac {\partial H}{\partial \boldsymbol {u}} = \mathbf {0}$$

应当特别注意的是，因为 $\delta x(t_f) = 0$ ，所以横截条件式(10-48)不成立，也不可能是 $\pmb{\lambda}(t_f) = \partial \varphi/\partial x(t_f)$ ；当 $\varphi (\cdot) = 0$ 时， $\lambda (t_f) = 0$ 也不能成立。此时，已知的 $x(t_0) = x_0$ 和 $x(t_{f}) = x_{f}$ ，就是求解正则方程的两端边界条件。

例10-5 设系统方程为

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = u (t)$$

求从已知初态 $x_0(0) = 0$ 和 $x_{2}(0) = 0$ ，在 $t_f = 1$ 时转移到目标集（末端约束）

$$x _ {1} (1) + x _ {2} (1) = 1$$

且使性能指标

$$J = \frac {1}{2} \int_ {0} ^ {1} u ^ {2} (t) \mathrm{d} t$$

为最小的最优控制 $u^{*}(t)$ 和相应的最优轨线 $x^{*}(t)$ 。

解 本例控制无约束, 可用变分法求解, 属积分型性能指标、 $t_f$ 固定、末端受约束的泛函极值问题。由题意:

$$\varphi [ \boldsymbol {x} (t _ {f}) ] = 0, \quad L (\bullet) = \frac {1}{2} u ^ {2}\psi [ \boldsymbol {x} (t _ {f}) ] = x _ {1} (1) + x _ {2} (1) - 1$$

构造哈密顿函数

$$H = \frac {1}{2} u ^ {2} + \lambda_ {1} x _ {2} + \lambda_ {2} u$$

由协态方程

$$\dot {\lambda} _ {1} = - \frac {\partial H}{\partial x _ {1}} = 0, \quad \lambda_ {1} (t) = c _ {1}\dot {\lambda} _ {2} = - \frac {\partial H}{\partial x _ {2}} = - \lambda_ {1}, \quad \lambda_ {2} (t) = - c _ {1} t + c _ {2}$$

由极值条件
