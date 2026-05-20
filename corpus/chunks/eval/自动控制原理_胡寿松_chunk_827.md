取 $u(t) = u^{*}(t)$ ，命题10-2仍然成立。由定理10-18知，最优性能指标

$$J ^ {*} [ \boldsymbol {x} (t), t ] = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) \boldsymbol {x} (t) \geqslant 0, \quad \forall t \in [ t _ {0}, t _ {f} ]$$

则由二次型函数性质知，命题成立。

(3) 最优控制解的存在与唯一性

若问题10-2有最优控制解，该解必满足定理10-18的结论。可以证明，该解是存在且唯一的。

定理10-19 在定理10-18中，最优控制解

$$\boldsymbol {u} (t) = - \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) \boldsymbol {x} (t)$$

存在且唯一。

证明 先证存在性: 因 $P(t)$ 存在且唯一, 故 $u^{*}(t)$ 存在。再证唯一性: 反设 $u^{*}(t)$ 不唯一, 不失一般性, 令 $u_{1}^{*}(t)$ 和 $u_{2}^{*}(t)$ 均为最优控制解, 则由 $P(t)$ 的唯一性可知

$$\boldsymbol {u} _ {1} ^ {*} (t) = - \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) \boldsymbol {x} _ {1} (t)\boldsymbol {u} _ {2} ^ {*} (t) = - \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) \boldsymbol {x} _ {2} (t)$$

相应的闭环系统方程(10-101)为

$$\dot {\boldsymbol {x}} _ {1} ^ {*} (t) = [ \boldsymbol {A} (t) - \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) ] \boldsymbol {x} _ {1} ^ {*} (t), \quad \boldsymbol {x} _ {1} ^ {*} \left(t _ {0}\right) = \boldsymbol {x} _ {0}\dot {\boldsymbol {x}} _ {2} ^ {*} (t) = [ \boldsymbol {A} (t) - \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) ] \boldsymbol {x} _ {2} ^ {*} (t), \quad \boldsymbol {x} _ {2} ^ {*} \left(t _ {0}\right) = \boldsymbol {x} _ {0}$$

可见,最优轨线 $\boldsymbol{x}_{1}^{*}(t)$ 和 $\boldsymbol{x}_{2}^{*}(t)$ 是同一向量微分方程且具有同样初始条件下的解。根据微分方程对初值问题解的唯一性,显然有

$$\boldsymbol {x} _ {1} ^ {*} (t) = \boldsymbol {x} _ {2} ^ {*} (t), \quad \forall t \in [ t _ {0}, t _ {f} ]$$

从而必有 $u_{1}^{*}(t) = u_{2}^{*}(t),\quad \forall t\in [t_{0},t_{f}]$

唯一性得证。

例10-12 设系统状态方程为

$$\dot {x} _ {1} (t) = x _ {2} (t), \quad \dot {x} _ {2} (t) = u (t)$$

初始条件为： $x_{1}(0) = 1, x_{2}(0) = 0$ 。性能指标

$$J = \frac {1}{2} \int_ {0} ^ {t _ {f}} \left[ x _ {1} ^ {2} (t) + u ^ {2} (t) \right] \mathrm{d} t$$

式中， $t_{f}$ 为某一给定值。试求最优控制 $u^{*}(t)$ ，使 J=min。

解 本例为有限时间状态调节器问题。由题意：

$$
\mathbf {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], \quad \mathbf {b} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right], \quad \mathbf {F} = \mathbf {0}, \quad \mathbf {Q} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right], \quad r = 1
$$

由里卡蒂方程
