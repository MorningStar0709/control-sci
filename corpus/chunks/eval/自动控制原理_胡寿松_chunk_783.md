# (2) 末端时刻自由时的最优解

当 $t_{f}$ 自由时,末端状态又可区分为受约束、自由和固定等三种情况。其中,以复合型性能指标、末端受约束的泛函极值问题最具一般性,所得到的结果可以方便地推广到末端自由和末端固定情况。末端时刻自由时所讨论的问题,除 $t_{f}$ 自由外,其余与末端时刻固定时所讨论的内容相同。

定理 10-7 对于如下最优控制问题：

$$\min _ {\boldsymbol {u} (t)} J = \varphi [ \boldsymbol {x} (t _ {f}), t _ {f} ] + \int_ {t _ {0}} ^ {t _ {f}} L (\boldsymbol {x}, \boldsymbol {u}, t) d t$$

s. t. ① $\dot{\pmb{x}}(t) = \pmb{f}(\pmb{x},\pmb{u},t),\pmb{x}(t_0) = \pmb{x}_0$

② $\psi [x(t_f),t_f] = 0$

式中， $t_{f}$ 自由，其余假设同定理 10-6，则最优解的必要条件为

1) $x(t)$ 和 $\lambda (t)$ 满足正则方程

$$\dot {\boldsymbol {x}} (t) = \frac {\partial H}{\partial \boldsymbol {\lambda}}, \quad \dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}}$$

其中

$$H (x, u, \lambda , t) = L (x, u, t) + \lambda^ {\mathrm{T}} (t) f (x, u, t)$$

2）边界条件与横截条件

$$\boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0}, \quad \psi [ \boldsymbol {x} (t _ {f}), t _ {f} ] = \mathbf {0}\boldsymbol {\lambda} (t _ {f}) = \frac {\partial \varphi}{\partial \boldsymbol {x} (t _ {f})} + \frac {\partial \boldsymbol {\psi} ^ {\mathrm{T}}}{\partial \boldsymbol {x} (t _ {f})} \boldsymbol {\gamma}$$

3）极值条件

$$\frac {\partial H}{\partial \boldsymbol {u}} = \boldsymbol {0}$$

4）在最优轨线末端哈密顿函数变化律

$$H (t _ {f}) = - \frac {\partial \varphi}{\partial t _ {f}} - \boldsymbol {\gamma} ^ {\mathrm{T}} \frac {\partial \boldsymbol {\psi}}{\partial t _ {f}}$$

证明 引入拉格朗日乘子向量 $\pmb{\lambda}(t) \in \mathbf{R}^n$ 和 $\pmb{\gamma} \in \mathbf{R}^r$ ，构造广义泛函

$$J _ {a} = \varphi [ \boldsymbol {x} (t _ {f}), t _ {f} ] + \boldsymbol {\gamma} ^ {\mathrm{T}} \boldsymbol {\psi} [ \boldsymbol {x} (t _ {f}), t _ {f} ] + \int_ {t _ {0}} ^ {t _ {f}} [ H (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {\lambda}, t) - \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \dot {\boldsymbol {x}} (t) ] \mathrm{d} t$$

式中，哈密顿函数 $H(x,u,\lambda,t)$ 定义同式(10-43)。

当末端位置由 $(x_{f},t_{f})$ 移动到 $(x_{f} + \delta x_{f},t_{f} + \delta t_{f})$ 时，产生如下广义泛函增量：
