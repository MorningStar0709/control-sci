# 4) 沿最优轨线哈密顿函数变化律( $t_{f}$ 自由时用)

$$H \left[ \boldsymbol {x} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {u} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {\lambda} \left(t _ {f} ^ {*}\right) \right] = 0$$

证明 引入拉格朗日乘子向量 $\pmb{\lambda}(t) \in \mathbb{R}^n$ 和 $\gamma \in \mathbb{R}^r$ ，构造等价末值型性能指标

$$\tilde {J} (\boldsymbol {u}) = \tilde {\varphi} [ \boldsymbol {x} (t _ {f}) ] = \varphi [ \boldsymbol {x} (t _ {f}) ] + \boldsymbol {\gamma} ^ {\mathrm{T}} \boldsymbol {\psi} [ \boldsymbol {x} (t _ {f}) ]$$

则最优控制问题等同于定理 10-8。

根据定理 10-8, 横截条件为

$$\boldsymbol {\lambda} (t _ {f}) = \frac {\partial \tilde {\varphi}}{\partial \boldsymbol {x} (t _ {f})} = \frac {\partial \varphi}{\partial \boldsymbol {x} (t _ {f})} + \frac {\partial \boldsymbol {\psi} ^ {\mathrm{T}}}{\partial \boldsymbol {x} (t _ {f})} \boldsymbol {\gamma}$$

其余结论同定理 10-8，故本定理得证。

不难证明，上述定理可以推广到时变情况。

定理10-12 对于如下时变系统、末值型性能指标、末端受约束、控制也受约束的最优控制问题

$$\min _ {\boldsymbol {u} (t) \in \Omega} J (\boldsymbol {u}) = \varphi [ \boldsymbol {x} \left(t _ {f}\right), t _ {f} ]$$

s. t. ① $\dot{\pmb{x}}(t) = \pmb{f}(\pmb{x},\pmb{u},t)$ ， $\pmb{x}(t_0) = \pmb{x}_0$

② $\psi [x(t_f),t_f] = 0$

式中， $t_f$ 固定或自由，假设条件同定理10-11。则必存 $r$ 维非零常向量 $\pmb{\gamma}$ 和 $n$ 维向量 $\lambda (t)$ ，使最优解满足如下必要条件：

1) 正则方程

$$\dot {\boldsymbol {x}} (t) = \frac {\partial H}{\partial \boldsymbol {\lambda}}, \quad \dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}}$$

其中哈密顿函数

$$H (\boldsymbol {x}, \boldsymbol {u}, \lambda , t) = \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t)$$

2）边界条件与横截条件

$$\boldsymbol {x} \left(t _ {0}\right) = \boldsymbol {x} _ {0}, \quad \psi [ \boldsymbol {x} \left(t _ {f}\right), t _ {f} ] = 0\boldsymbol {\lambda} \left(t _ {f}\right) = \frac {\partial \varphi}{\partial \boldsymbol {x} \left(t _ {f}\right)} + \frac {\partial \boldsymbol {\psi} ^ {\mathrm{T}}}{\partial \boldsymbol {x} \left(t _ {f}\right)} \boldsymbol {\gamma}$$

3) 极小值条件

$$H (x ^ {*}, u ^ {*}, \lambda , t) = \min _ {u \in \Omega} H (x ^ {*}, u, \lambda , t)$$

4) 沿最优轨线哈密顿函数变化律 $(t_f$ 自由时用）

$$H [ \boldsymbol {x} ^ {*} (t _ {f} ^ {*}), \boldsymbol {u} ^ {*} (t _ {f} ^ {*}), \boldsymbol {\lambda} (t _ {f} ^ {*}), t _ {f} ^ {*} ] = - \frac {\partial \varphi}{\partial t _ {f}} - \boldsymbol {\gamma} ^ {\mathrm{T}} \frac {\partial \boldsymbol {\psi}}{\partial t _ {f}}$$
