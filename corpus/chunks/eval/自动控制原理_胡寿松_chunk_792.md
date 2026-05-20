$$\bar {\lambda} (t _ {f}) = \frac {\partial \varphi [ \bar {x} (t _ {f}) ]}{\partial \bar {x} (t _ {f})}$$

代入 $\bar{\lambda}(t_f)$ 和 $\bar{x}(t_f)$ 表达式，易得

$$\lambda \left(t _ {f}\right) = \frac {\partial \varphi}{\partial x \left(t _ {f}\right)}, \quad \lambda_ {n + 1} \left(t _ {f}\right) = \frac {\partial \varphi}{\partial t _ {f}} \tag {10-57}$$

于是，证明了本定理的结论2)。

由定理 10-8, 极小值条件为

$$\bar {H} (\bar {x} ^ {*}, u ^ {*}, \bar {\lambda}) = \min _ {u \in \Omega} \bar {H} (\bar {x} ^ {*}, u, \bar {\lambda})$$

代入式(10-54)，上式可写为

$$H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \lambda , t\right) + \lambda_ {n + 1} (t) = \min _ {\boldsymbol {u} \in \Omega} H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u}, \lambda , t\right) + \lambda_ {n + 1} (t)$$

立即证得本定理的结论 3)。

根据定理 10-8 中的沿最优轨线哈密顿函数变化律以及式(10-54)，有

$$
\begin{array}{l} \bar {H} \left[ \bar {\boldsymbol {x}} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {u} ^ {*} \left(t _ {f} ^ {*}\right), \bar {\lambda} \left(t _ {f} ^ {*}\right) \right] \\ = H \left[ \boldsymbol {x} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {u} ^ {*} \left(t _ {f} ^ {*}\right), \lambda \left(t _ {f} ^ {*}\right), t _ {f} ^ {*} \right] + \lambda_ {n + 1} \left(t _ {f} ^ {*}\right) = 0 \\ \end{array}
$$

代入式(10-57)，证得本定理结论4):

$$H ^ {*} \left(t _ {f} ^ {*}\right) = - \frac {\partial \varphi}{\partial t _ {f}}$$

比较定理 10-9 与定理 10-8 可见,时变性并不影响极小值原理中的正则方程、横截条件和极小值条件,但却改变了哈密顿函数沿最优轨线的变化律。

定理 10-8 的形式还可推广于积分型性能指标的问题。

定理 10-10 对于如下定常系统、积分型性能指标、末端自由、控制受约束的最优控制问题

$$\min _ {\boldsymbol {u} (t) \in \Omega} J (\boldsymbol {u}) = \int_ {t _ {0}} ^ {t _ {f}} L (\boldsymbol {x}, \boldsymbol {u}) \mathrm{d} t\text { s. t. } \quad \dot {\boldsymbol {x}} (t) = f (\boldsymbol {x}, \boldsymbol {u}), \quad \boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0}$$

式中， $t_{f}$ 固定或自由，假设同定理 10-8。则最优解的必要条件为

1）正则方程

$$\dot {\pmb {x}} (t) = \frac {\partial H}{\partial \pmb {\lambda}}, \qquad \dot {\pmb {\lambda}} (t) = - \frac {\partial H}{\partial \pmb {x}}$$

其中哈密顿函数

$$H (\boldsymbol {x}, \boldsymbol {u}, \lambda) = L (\boldsymbol {x}, \boldsymbol {u}) + \lambda^ {T} (t) f (\boldsymbol {x}, \boldsymbol {u})$$

2) 边界条件与横截条件

$$\boldsymbol {x} (t _ {0}) = \boldsymbol {x} _ {0}, \quad \lambda (t _ {f}) = \mathbf {0}$$

3）极小值条件

$$H (x ^ {*}, u ^ {*}, \lambda) = \min _ {u \in \Omega} H (x ^ {*}, u, \lambda)$$

4) 沿最优轨线哈密顿函数变化律( $t_{f}$ 自由时用)
