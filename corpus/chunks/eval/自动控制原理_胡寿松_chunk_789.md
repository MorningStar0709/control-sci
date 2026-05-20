# 1. 连续系统的极小值原理

为方便阐述,先研究定常系统、末值型性能指标、末端自由时的极小值原理,然后将所得结果加以推广。

(1) 末端自由时的极小值原理

定理 10-8 对于如下定常系统、末值型性能指标、末端自由、控制受约束的最优控制问题

$$\min _ {\boldsymbol {u} (t) \in \Omega} J (\boldsymbol {u}) = \varphi [ \boldsymbol {x} (t _ {f}) ]\text { s. t. } \quad \dot {\boldsymbol {x}} (t) = f (\boldsymbol {x}, \boldsymbol {u}), \quad \boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0}$$

式中， $x(t)\in \mathbf{R}^n$ ； $u(t)\in \Omega \subset \mathbf{R}^m$ ，为任意分段连续函数， $\Omega$ 为容许控制域；末端状态 $x(t_{f})$ 自由；末端时刻 $t_f$ 固定或自由。假设：

1) 向量函数 $f(x, u)$ 和标量函数 $\varphi(x)$ 都是其自变量的连续可微函数。

2）在有界集上，函数 $f(x,u)$ 对变量 $\pmb{x}$ 满足利普希茨条件。

$$\mid f (x ^ {1}, u) - f (x ^ {2}, u) \mid \leqslant a \mid x ^ {1} - x ^ {2} \mid , \quad a > 0$$

则对于最优解 $u^{*}(t), t_{f}^{*}$ 和 $x^{*}(t)$ ，必存在非零的 $\lambda(t) \in \mathbb{R}^{n}$ ，使下列必要条件成立：

1) 正则方程

$$\dot {\boldsymbol {x}} (t) = \frac {\partial H}{\partial \boldsymbol {\lambda}}, \quad \dot {\boldsymbol {\lambda}} = - \frac {\partial H}{\partial \boldsymbol {x}}$$

式中，哈密顿函数

$$H (x, u, \lambda) = \lambda^ {\mathrm{T}} (t) f (x, u)$$

2) 边界条件与横截条件

$$\boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0}, \quad \boldsymbol {\lambda} (t _ {f}) = \frac {\partial \varphi}{\partial \boldsymbol {x} (t _ {f})}$$

3）极小值条件

$$H \left(x ^ {*}, u ^ {*}, \lambda\right) = \min _ {u \in \Omega} H \left(x ^ {*}, u, \lambda\right)$$

4) 沿最优轨线哈密顿函数变化律( $t_{f}$ 自由时用)

$$H \left[ \boldsymbol {x} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {u} ^ {*} \left(t _ {f} ^ {*}\right), \lambda \left(t _ {f} ^ {*}\right) \right] = 0$$

应当指出，定理10-8中的必要条件3)又可表示为

$$H \left[ x ^ {*} (t), u ^ {*} (t), \lambda (t) \right] \leqslant H _ {u (t) \in \Omega} \left[ x ^ {*} (t), u (t), \lambda (t) \right]$$

上式表示，对所有 $t \in [t_0, t_f]$ ， $\pmb{u}(t)$ 遍取 $\Omega$ 中所有点，使 $H$ 为绝对极小值的 $\pmb{u}(t) = \pmb{u}^*(t)$ 。因而庞特里亚金原理一般称为极小值原理。

与经典变分法相比，极小值原理的重要意义有如下几方面：

1）容许控制条件放宽了。极小值条件对通常的控制约束均适用。  
2）最优控制使哈密顿函数取全局极小值。当满足经典变分法的应用条件时，其极值条件 $\partial H / \partial u = 0$ 是极小值原理中极小值条件 $H^{*} = \min_{u\in \Omega}H$ 的一种特例。  
3) 极小值原理不要求哈密顿函数对控制向量的可微性, 因而扩大了应用范围。  
4) 极小值原理给出的是最优解的必要而非充分条件。如果由实际工程问题的物理意义可以判定解是存在的，而由极小值原理求出的控制又是唯一的，则该控制为要求的最优控制。实际遇到的工程问题往往属于这种情况。

例 10-7 设系统方程及初始条件为

$$\dot {x} _ {1} (t) = - x _ {1} (t) + u (t), \quad x _ {1} (0) = 1\dot {x} _ {2} (t) = x _ {1} (t), \quad x _ {2} (0) = 0$$

式中， $|u(t)|\leqslant 1$ 。若系统末态 $\pmb {x}(t_f)$ 自由，试求 $u^{*}(t)$ 使性能指标

$$J = x _ {2} (1) = \min$$

解 本例为定常系统、末值型性能指标、末端自由、 $t_{f}$ 固定、控制受约束的最优控制问题。由题意
