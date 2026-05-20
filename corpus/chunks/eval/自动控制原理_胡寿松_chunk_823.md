# (1) 最优解的充分必要条件

定理 10-18 对于问题 10-2, 其最优控制的充分必要条件为

$$\boldsymbol {u} ^ {*} (t) = - \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) \boldsymbol {x} (t) \tag {10-97}$$

最优性能指标

$$J ^ {*} = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} \left(t _ {0}\right) \boldsymbol {P} \left(t _ {0}\right) \boldsymbol {x} \left(t _ {0}\right) \tag {10-98}$$

式中， $P(t)$ 为 $n \times n$ 对称非负矩阵，满足下列里卡蒂矩阵微分方程：

$$- \dot {\boldsymbol {P}} (t) = \boldsymbol {P} (t) \boldsymbol {A} (t) + \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) - \boldsymbol {P} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) + \boldsymbol {Q} (t) \tag {10-99}$$

其边界条件

$$\boldsymbol {P} \left(t _ {f}\right) = \boldsymbol {F} \tag {10-100}$$

而最优轨线 $x^{*}(t)$ ，则是下列线性向量微分方程的解：

$$\dot {\boldsymbol {x}} (t) = \left[ \boldsymbol {A} (t) - \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) \right] \boldsymbol {x} (t), \quad \boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0} \tag {10-101}$$

证明 必要性: 若 $u^{*}(t)$ 为最优控制, 可证式(10-97)成立。

因 $u^{*}(t)$ 最优，故必满足极小值原理。构造哈密顿函数

$$H = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {x} + \frac {1}{2} \boldsymbol {u} ^ {\mathrm{T}} \boldsymbol {R} \boldsymbol {u} + \lambda^ {\mathrm{T}} \boldsymbol {A} \boldsymbol {x} + \lambda^ {\mathrm{T}} \boldsymbol {B} \boldsymbol {u}$$

由极值条件

$$\frac {\partial H}{\partial \boldsymbol {u}} = \boldsymbol {R} \boldsymbol {u} + \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {\lambda} = \mathbf {0}, \quad \frac {\partial^ {2} H}{\partial \boldsymbol {u} ^ {2}} = \boldsymbol {R} > \mathbf {0}$$

故 $\boldsymbol{u}^{*}(t)=-\boldsymbol{R}^{-1}\boldsymbol{B}^{\mathrm{T}}\boldsymbol{\lambda}(t)$ (10-102)

可使哈密顿函数极小。再由正则方程

$$\dot {\boldsymbol {x}} (t) = \frac {\partial H}{\partial \boldsymbol {\lambda}} = \boldsymbol {A} (t) \boldsymbol {x} (t) - \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) \tag {10-103}\dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}} = - \boldsymbol {Q} (t) \boldsymbol {x} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) \tag {10-104}$$

因末态 $x(t_{f})$ 自由，所以横截条件为
