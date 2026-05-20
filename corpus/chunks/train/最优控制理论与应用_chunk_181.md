$$H _ {1} (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda} _ {1}, t) = F (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v} ^ {*}, t) + \boldsymbol {\lambda} _ {1} ^ {\mathrm{T}} f (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v} ^ {*}, t) \tag {10-31}$$

根据第四章中的极小值原理,知 J 取极小值的必要条件是 $x^{*}$ 、 $u^{*}$ 、 $\lambda_{1}$ 和 $t_{f}$ 满足

① 正则方程

$$
\begin{array}{l} \dot {\boldsymbol {\lambda}} _ {1} = - \frac {\partial H _ {1}}{\partial \boldsymbol {x}} \tag {10-32} \\ \dot {\boldsymbol {x}} = \frac {\partial H _ {1}}{\partial \boldsymbol {\lambda} _ {1}} \\ \end{array}
$$

② 边界条件

$$\boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0}, \quad \boldsymbol {G} \left[ \boldsymbol {x} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] = \mathbf {0} \tag {10-33}$$

③ 横截条件

$$\boldsymbol {\lambda} _ {1} \left(t _ {\mathrm{f}}\right) = \frac {\partial \boldsymbol {\Phi}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} \boldsymbol {v} \tag {10-34}$$

④ 最优终端时刻条件

$$H _ {1} (t _ {\mathrm{f}}) = - \frac {\partial \Phi}{\partial t _ {\mathrm{f}}} - \frac {\partial G ^ {\mathrm{T}}}{\partial t _ {\mathrm{f}}} \boldsymbol {v} \tag {10-35}$$

⑤ 在最优轨线 $x^{*}(t)$ 和最优控制 $u^{*}(t)$ 上，哈密顿函数取极小值

$$\min _ {u \in U} H _ {1} \left(\boldsymbol {x} ^ {*}, \boldsymbol {u}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda} _ {1}, t\right) = H _ {1} \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda} _ {1}, t\right) \tag {10-36}$$

2）关于 $v^{*}$ 的极大值原理——最优控制问题(二)

状态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u} ^ {*}, \boldsymbol {v}, t) \tag {10-37}$$

终端约束

$$\boldsymbol {G} \left[ \boldsymbol {x} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] = \boldsymbol {0}$$

指标函数

$$J \left[ \boldsymbol {u} ^ {*}, \boldsymbol {v} \right] = \Phi \left[ \boldsymbol {x} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} F \left(\boldsymbol {x}, \boldsymbol {u} ^ {*}, \boldsymbol {v}, t\right) \mathrm{d} t \quad (1 0 - 3 8)$$

对 $\pmb{v}$ 取极大。即寻求 $\pmb{v}^{*}$ ，使满足

$$J \left[ \boldsymbol {u} ^ {*}, \boldsymbol {v} \right] \leqslant J \left[ \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*} \right] \tag {10-39}$$

对于上面的最优控制问题(二)，引入哈密顿函数 $H_{2}$
