# 4. 输出可控性

如果系统需要控制的是输出量而不是状态，则需研究系统的输出可控性。

输出可控性 若在有限时间间隔 $[t_0, t_1]$ 内，存在无约束分段连续控制函数 $u(t), t \in [t_0, t_1]$ ，能使任意初始输出 $y(t_0)$ 转移到任意最终输出 $y(t_1)$ ，则称此系统输出完全可控，简称输出可控。

输出可控性判据 设线性定常连续系统的状态方程和输出方程为

$$\dot {\pmb {x}} = \pmb {A} \pmb {x} + \pmb {B} \pmb {u}, \quad \pmb {x} (0) = \pmb {x} _ {0}, \quad t \in [ 0, t _ {1} ] \tag {9-118}\mathbf {y} = \mathbf {C x} + \mathbf {D u} \tag {9-119}$$

式中，u 为 p 维输入向量；y 为 q 维输出向量；x 为 n 维状态向量。状态方程(9-118)的解为

$$\boldsymbol {x} (t _ {1}) = \mathrm{e} ^ {\boldsymbol {A} t _ {1}} \boldsymbol {x} _ {0} + \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} (t _ {1} - t)} \boldsymbol {B u} (t) \mathrm{d} t$$

则输出为

$$\mathbf {y} (t _ {1}) = \mathbf {C e} ^ {\mathbf {A} t _ {1}} \mathbf {x} _ {0} + \mathbf {C} \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {\mathbf {A} (t _ {1} - t)} \mathbf {B u} (t) \mathrm{d} t + \mathbf {D u} (t _ {1}) \tag {9-120}$$

不失一般性，令 $y(t_{1})=0$ ，并应用凯莱-哈密顿定理的推论2有

$$
\begin{array}{l} \boldsymbol {C} \mathrm{e} ^ {\boldsymbol {A} t _ {1}} \boldsymbol {x} _ {0} = - \boldsymbol {C} \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {\boldsymbol {A} (t _ {1} - t)} \boldsymbol {B u} (t) \mathrm{d} t - \boldsymbol {D u} (t _ {1}) \\ = - \boldsymbol {C} \int_ {0} ^ {t _ {1}} \sum_ {m = 0} ^ {n - 1} \alpha_ {m} (t) \boldsymbol {A} ^ {m} \boldsymbol {B u} (t) d t - \boldsymbol {D u} (t _ {1}) \\ \end{array}
= - \boldsymbol {C} \sum_ {m = 0} ^ {n - 1} \boldsymbol {A} ^ {m} \boldsymbol {B} \int_ {0} ^ {t _ {1}} \alpha_ {m} (t) \boldsymbol {u} (t) d t - \boldsymbol {D u} \left(t _ {1}\right)
$$

令 $\pmb{u}_m(t_1) = \int_0^{t_1}\alpha_m(t)\pmb {u}(t)\mathrm{d}t$ ，则

$$
\begin{array}{l} \mathbf {C e} ^ {\mathbf {A} t _ {1}} \mathbf {x} _ {0} = - \mathbf {C} \sum_ {m = 0} ^ {n - 1} \mathbf {A} ^ {m} \mathbf {B u} _ {m} (t _ {1}) - \mathbf {D u} (t _ {1}) \\ = - \boldsymbol {C B u} _ {0} \left(t _ {1}\right) - \boldsymbol {C A B u} _ {1} \left(t _ {1}\right) - \dots - \boldsymbol {C A} ^ {n - 1} \boldsymbol {B u} _ {n - 1} \left(t _ {1}\right) - \boldsymbol {D u} \left(t _ {1}\right) \\ = - \left[ \begin{array}{l l l l l} \boldsymbol {C B} & \boldsymbol {C A B} & \dots & \boldsymbol {C A} ^ {n - 1} \boldsymbol {B} & \boldsymbol {D} \end{array} \right] \left[ \begin{array}{c} \boldsymbol {u} _ {0} \left(t _ {1}\right) \\ \boldsymbol {u} _ {1} \left(t _ {1}\right) \\ \vdots \\ \boldsymbol {u} _ {n - 1} \left(t _ {1}\right) \\ \boldsymbol {u} \left(t _ {1}\right) \end{array} \right] \tag {9-121} \\ \end{array}
$$
