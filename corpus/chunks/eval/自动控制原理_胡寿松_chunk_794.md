因 $\varphi[\bar{\pmb{x}}(t_f)]=x_0(t_f)$ , 故上式可表示为

$$
\left[ \begin{array}{c} \lambda_ {0} (t _ {f}) \\ \boldsymbol {\lambda} (t _ {f}) \end{array} \right] = \left[ \begin{array}{c} \frac {\partial \varphi}{\partial x _ {0} (t _ {f})} \\ \frac {\partial \varphi}{\partial \boldsymbol {x} (t _ {f})} \end{array} \right] = \left[ \begin{array}{c} 1 \\ \boldsymbol {0} \end{array} \right]
$$

从而 $\pmb{\lambda}(t_f) = \mathbf{0},\quad \lambda_0(t) = \lambda_0(t_f) = 1$

哈密顿函数

$$\bar {H} (\bar {x}, u, \bar {\lambda}) = L (x, u) + \lambda^ {\mathrm{T}} f (x, u) = H (x, u, \lambda) \tag {10-62}$$

由定理 10-8, 其状态方程为

$$\dot {\bar {x}} (t) = \frac {\partial \bar {H}}{\partial \bar {\lambda}} = \frac {\partial H}{\partial \bar {\lambda}}$$

代入 $\bar{x}(t)$ 和 $\bar{\lambda}(t)$ 的增广形式，证得

$$\dot {\pmb {x}} (t) = \frac {\partial H}{\partial \pmb {\lambda}}, \qquad \dot {x} _ {0} (t) = L (\pmb {x}, \pmb {u})$$

再将式(10-62)代入式(10-61)，有

$$\dot {\lambda} (t) = - \frac {\partial H}{\partial x}$$

由定理 10-8, 其极小值条件为

$$\bar {H} \left(\bar {x} ^ {*}, u ^ {*}, \bar {\lambda}\right) = \min _ {u \in \Omega} \bar {H} \left(\bar {x} ^ {*}, u, \bar {\lambda}\right)$$

已证 $\bar{H} (\bar{x}^{*},u,\bar{\lambda}) = H(x,u,\lambda)$ ，立即证得

$$H \left(x ^ {*}, u ^ {*}, \lambda\right) = \min _ {u \in \Omega} H \left(x ^ {*}, u, \lambda\right)$$

由定理 10-8, 在最优轨线末端有

$$\bar {H} \left[ \bar {\boldsymbol {x}} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {u} ^ {*} \left(t _ {f} ^ {*}\right), \bar {\lambda} \left(t _ {f} ^ {*}\right) \right] = 0$$

代入式(10-62)，立即证得 $H^{*}(t_{f}^{*})=0$ 。

比较定理 10-10、定理 10-8 可见，积分型性能指标改变了哈密顿函数的形式，也影响了横截条件表达式。应当指出，不论是复合型性能指标，还是积分型性能指标，抑或是末值型性能指标，其哈密顿函数的统一形式应为

$$H (\boldsymbol {x}, \boldsymbol {u}, \lambda) = L (\boldsymbol {x}, \boldsymbol {u}) + \lambda^ {\mathrm{T}} (t) \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}) \tag {10-63}$$

这一规定，对时变系统同样适用。

例10-8 设一阶系统方程为

$$\dot {x} (t) = x (t) - u (t), \quad x (0) = 5$$

其中控制约束： $0.5\leqslant u(t)\leqslant 1$ 。试求使性能指标

$$J = \int_ {0} ^ {1} [ x (t) + u (t) ] \mathrm{d} t$$

为极小值的最优控制 $u^{*}(t)$ 及最优轨线 $x^{*}(t)$ 。

解 本例为定常系统、积分型性能指标、 $t_{f}$ 固定、末端自由、控制受约束的最优控制问题。令哈密顿函数

$$H = x + u + \lambda (x - u) = x (1 + \lambda) + u (1 - \lambda)$$

由于 $H$ 是 $\pmb{u}$ 的线性函数，根据极小值原理知，使 $H$ 绝对极小就相当于使性能指标极小，因此要求 $u(1 - \lambda)$ 极小。因 $\pmb{u}$ 的取值上限为1，下限为0.5，故应取

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 1, & \lambda > 1 \\ 0. 5, & \lambda <   1 \end{array} \right.
$$

由协态方程
