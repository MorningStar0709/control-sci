$$\dot {\boldsymbol {x}} ^ {*} = \boldsymbol {f} (\boldsymbol {x} ^ {*} (t), \boldsymbol {u} ^ {*} (t), \boldsymbol {v} ^ {*} (t), t) \tag {10-24}\boldsymbol {x} ^ {*} \left(t _ {0}\right) = \boldsymbol {x} _ {0}, \quad \boldsymbol {G} \left[ \boldsymbol {x} ^ {*} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] = \boldsymbol {0}\dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}} \tag {②}\boldsymbol {\lambda} \left(t _ {\mathrm{f}}\right) = \frac {\partial \boldsymbol {\Phi}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} \boldsymbol {v} \tag {10-25}H (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \lambda (t), t) \tag {③}= \min _ {u} \max _ {v} H (x ^ {*}, u, v, \lambda , t)= \max _ {v} \min _ {u} H (x ^ {*}, u, v, \lambda , t) \tag {10-26}H \left(\boldsymbol {x} ^ {*} \left(t _ {\mathrm{f}}\right), \boldsymbol {u} ^ {*} \left(t _ {\mathrm{f}}\right), \boldsymbol {v} ^ {*} \left(t _ {\mathrm{f}}\right), \boldsymbol {\lambda} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}}\right) \tag {4}= - \frac {\partial \boldsymbol {\Phi} [ \boldsymbol {x} (t _ {\mathrm{f}}) , t _ {\mathrm{f}} ]}{\partial t _ {\mathrm{f}}} - \frac {\partial \boldsymbol {G} ^ {\mathrm{T}} [ \boldsymbol {x} (t _ {\mathrm{f}}) , t _ {\mathrm{f}} ]}{\partial t _ {\mathrm{f}}} \boldsymbol {v} \tag {10-27}$$

证明 上述双方极值原理的证明分三步。先给出关于 $v^{*}$ 的极大值原理，再给出关于 $u^{*}$ 的极小值原理，最后将前两步组合起来，给出双方极值（极大极小）原理。

1）关于 $u^{*}$ 的极小值原理——最优控制问题（一）

状态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v} ^ {*}, t) \tag {10-28}$$

终端约束

$$
\mathbf {G} \left[ \begin{array}{c c} \boldsymbol {x} (t _ {f}), t _ {f} \end{array} \right] = \mathbf {0}
$$

指标函数

$$J [ \boldsymbol {u}, \boldsymbol {v} ^ {*} ] = \Phi [ \boldsymbol {x} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} F (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v} ^ {*}, t) \mathrm{d} t \tag {10-29}$$

对 $\pmb{u}$ 取极小。即寻求 $u^{*}$ ，使满足

$$J [ \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*} ] \leqslant J [ \boldsymbol {u}, \boldsymbol {v} ^ {*} ] \tag {10-30}$$

对于上面的最优控制问题(一)，引入哈密顿函数 $H_{1}$
