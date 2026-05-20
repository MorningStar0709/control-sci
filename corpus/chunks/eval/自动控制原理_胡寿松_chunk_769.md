# (2) 有等式约束泛函极值的必要条件

在求解实际系统的最优控制问题时,要求使指标泛函取极值的极值轨线同时满足系统的运动微分方程式。因此,控制系统的最优控制问题,要求确定在微分方程等式约束条件下的泛函极值,即条件极值变分问题。

在讨论条件极值的变分问题时,我们仍然先考虑最简单的两端固定情况。利用拉格朗日乘子法,可以将有等式约束的泛函条件极值问题化为无约束泛函极值问题。

定理10-5 设有如下条件泛函极值问题：

$$\min _ {\boldsymbol {x} (t)} J [ \boldsymbol {x} ] = \int_ {t _ {0}} ^ {t _ {f}} g (\boldsymbol {x}, \dot {\boldsymbol {x}}, t) \mathrm{d} t\text { s. t. } \quad f (x, \dot {x}, t) = 0$$

式中， $f(x,\dot{x},t)=0$ 为系统运动微分方程； $g(x,\dot{x},t)$ 及 $x(t)$ 在 $[t_{0},t_{f}]$ 上连续可微； $x,\dot{x},f(\cdot)\in R^{n}$ ; $t_{0}$ 及 $t_{f}$ 给定。已知 $x(t_{0})=x_{0},x(t_{f})=x_{f}$ ，则极值轨线 $x^{*}(t)$ 满足如下欧拉方程及相应的横截条件：

$$\frac {\partial L}{\partial \boldsymbol {x}} - \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {\boldsymbol {x}}} = \mathbf {0}\left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \Big | _ {t _ {f}} \delta \boldsymbol {x} (t _ {f}) - \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \Big | _ {t _ {0}} \delta \boldsymbol {x} (t _ {0}) = 0$$

其中 $L(x,\dot{x},\lambda ,t) = g(x,\dot{x},,t) + \lambda^{\mathrm{T}}(t)f(x,\dot{x},t)$

为拉格朗日函数， $\lambda(t) \in \mathbb{R}^n$ 为待定拉格朗日乘子。

证明 设 $\pmb{\lambda}(t) \in \mathbb{R}^n$ 待定，构造广义泛函

$$
\begin{array}{l} J _ {a} [ \boldsymbol {x} ] = \int_ {t _ {0}} ^ {t _ {f}} [ g (\boldsymbol {x}, \dot {\boldsymbol {x}}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} (t) f (\boldsymbol {x}, \dot {\boldsymbol {x}}, t) ] \mathrm{d} t \\ = \int_ {t _ {0}} ^ {t _ {f}} L (\boldsymbol {x}, \dot {\boldsymbol {x}}, \boldsymbol {\lambda}, t) d t \\ \end{array}
$$

于是，原性能泛函的条件极值问题，转化为广义泛函的无约束极值问题。根据定理10-4，本定理得证。

与定理10-4情况相同，在两端固定情况下，定理10-5的横截条件退化为已知的两点边界条件。

例 10-3 设人造地球卫星姿态控制系统的状态方程为

$$
\dot {\boldsymbol {x}} (t) = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \boldsymbol {x} (t) + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u} (t)
$$

指标泛函取

$$J = \frac {1}{2} \int_ {0} ^ {2} u ^ {2} (t) \mathrm{d} t$$

边界条件为

$$
\boldsymbol {x} (0) = \left[ \begin{array}{l} 1 \\ 1 \end{array} \right], \quad \boldsymbol {x} (2) = \left[ \begin{array}{l} 0 \\ 0 \end{array} \right]
$$

试求使指标泛函取极值的极值轨线 $x^{*}(t)$ 和极值控制 $u^{*}(t)$ 。

解 本例为有等式约束泛函极值问题。由题意

$$
g = \frac {1}{2} u ^ {2}, \quad \boldsymbol {\lambda} ^ {\mathrm{T}} = \left[ \begin{array}{l l} \lambda_ {1} & \lambda_ {2} \end{array} \right]
