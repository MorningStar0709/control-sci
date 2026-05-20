# 2. 欧拉方程

欧拉方程又称欧拉-拉格朗日方程，是无约束泛函极值及有约束泛函极值的必要条件。在推导欧拉方程的过程中，应用了式(10-21)所示的泛函极值的必要条件，并且为了便于讨论，假定了 $t_{0}$ 和 $t_{f}$ 给定，且初态 $x(t_{0})$ 和末态 $x(t_{f})$ 为两端固定的情况。

(1) 无约束泛函极值的必要条件

定理 10-4 设有如下泛函极值问题：

$$\min _ {\boldsymbol {x} (t)} J [ \boldsymbol {x} ] = \int_ {t _ {0}} ^ {t _ {f}} L (\boldsymbol {x}, \dot {\boldsymbol {x}}, t) d t$$

式中， $L(x,\dot{x},t)$ 及 $\pmb {x}(t)$ 在 $[t_0,t_f]$ 上连续可微， $t_0$ 及 $t_f$ 给定。已知 $\pmb {x}(t_0) = \pmb {x}_0,\pmb {x}(t_f) = \pmb {x}_f,\pmb {x}(t)\in$ $\mathbf{R}^n$ ，则极值轨线 $\pmb{x}^{*}(t)$ 满足如下欧拉方程

$$\frac {\partial L}{\partial \boldsymbol {x}} - \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {\boldsymbol {x}}} = \mathbf {0} \tag {10-22}$$

及横截条件

$$\left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \Big | _ {t _ {f}} \delta \boldsymbol {x} (t _ {f}) - \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \Big | _ {t _ {0}} \delta \boldsymbol {x} (t _ {0}) = 0 \tag {10-23}$$

证明 设 $x^{*}(t)$ 是满足边界条件 $x(t_0) = x_0$ 和 $x(t_f) = x_f$ 的极值轨线， $x(t)$ 是 $x^{*}(t)$ 邻域中的一条容许轨线。 $x(t)$ 与 $x^{*}(t)$ 之间有下列关系：

$$\boldsymbol {x} (t) = \boldsymbol {x} ^ {*} (t) + \delta \boldsymbol {x} (t), \quad \dot {\boldsymbol {x}} (t) = \dot {\boldsymbol {x}} ^ {*} (t) + \delta \dot {\boldsymbol {x}} (t)$$

以及 $x(t_0) = x^* (t_0) = x_0, \quad x(t_f) = x^* (t_f) = x_f$

取泛函增量

$$
\begin{array}{l} \Delta J [ x ] = J \left[ x ^ {*} + \delta x \right] - J \left[ x ^ {*} \right] \\ = \int_ {t _ {0}} ^ {t _ {f}} \left[ L \left(\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \dot {\boldsymbol {x}} ^ {*} + \delta \dot {\boldsymbol {x}}, t\right) - L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}}, t \right] \mathrm{d} t \right. \\ = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial L}{\partial \boldsymbol {x}}\right) ^ {T} \delta \boldsymbol {x} + \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \delta \dot {\boldsymbol {x}} + H O T \right] d t \\ \end{array}
$$

式中，HOT代表泰勒展开式中的高阶项。由变分定义知，取上式主部可得

$$\delta J = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial L}{\partial \boldsymbol {x}}\right) ^ {T} \delta \boldsymbol {x} + \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \delta \dot {\boldsymbol {x}} \right] d t$$

对上式中的第二项作分部积分，有
