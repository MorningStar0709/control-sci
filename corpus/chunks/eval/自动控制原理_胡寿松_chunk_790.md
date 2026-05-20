$$\varphi [ \pmb {x} (t _ {f}) ] = x _ {2} (1), \qquad t _ {f} = 1$$

令 $H(x,u,\lambda) = \lambda_1(-x_1 + u) + \lambda_2x_1$

由协态方程

$$\dot {\lambda} _ {2} = - \frac {\partial H}{\partial x _ {2}} = 0, \quad \lambda_ {2} (t) = c _ {2}\dot {\lambda} _ {1} = - \frac {\partial H}{\partial x _ {1}} = \lambda_ {1} - \lambda_ {2}, \quad \lambda_ {1} (t) = c _ {1} \mathrm{e} ^ {t} + c _ {2}$$

式中， $c_{1}$ 和 $c_{2}$ 为待定常数。

由横截条件

$$\lambda_ {1} (1) = \frac {\partial \varphi}{\partial x _ {1} (1)} = 0, \quad \lambda_ {2} (1) = \frac {\partial \varphi}{\partial x _ {2} (1)} = 1$$

解出 $c_{1}=-e^{-1},c_{2}=1$ 。故有 $\lambda_{1}(t)=1-e^{t-1}$ 。

由极小值条件

$$
u ^ {*} (t) = - \operatorname{sgn} \left(\lambda_ {1}\right) = \left\{ \begin{array}{l l} - 1, & \lambda_ {1} > 0 \\ 1, & \lambda_ {1} <   0 \end{array} \right.
$$

易知 $\lambda_1(t) = 1 - \mathrm{e}^{t - 1} > 0, \quad \forall t \in [0,1)$

$$\lambda_ {1} (t) = 0, \quad t = 1$$

故所求最优控制

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} - 1, & \forall t \in [ 0, 1) \\ 0, & t = 1 \end{array} \right.
$$

定理 10-8 是适用于定常系统、末值型性能指标、末端自由时的极小值原理，但许多常见的最优控制问题都可以化为这种形式，例如可推广于时变系统。

定理 10-9 对于如下时变系统、末值型性能指标、末端自由、控制受约束的最优控制问题

$$
\begin{array}{l} \min _ {\boldsymbol {u} (t) \in \Omega} J (\boldsymbol {u}) = \varphi [ \boldsymbol {x} (t _ {f}), t _ {f} ] \\ \mathrm{s.t.} \dot {\boldsymbol {x}} (t) = \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t), \quad \boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0} \\ \end{array}
$$

式中， $t_{f}$ 固定或自由，假设同定理 10-8。则最优解的必要条件如下：

1) 正则方程

$$\dot {\boldsymbol {x}} (t) = \frac {\partial H}{\partial \boldsymbol {\lambda}}, \quad \dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}}$$

其中哈密顿函数

$$H (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {\lambda}, t) = \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t)$$

2）边界条件与横截条件

$$\boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0}, \quad \boldsymbol {\lambda} (t _ {f}) = \frac {\partial \varphi}{\partial \boldsymbol {x} (t _ {f})}$$

3）极小值条件

$$H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \lambda , t\right) = \min _ {\boldsymbol {u} (t) \in \Omega} H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u}, \lambda , t\right)$$

4) 沿最优轨线哈密顿函数变化律( $t_{f}$ 自由时用)
