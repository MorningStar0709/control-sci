$$H \left[ \boldsymbol {x} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {u} ^ {*} \left(t _ {f} ^ {*}\right), \lambda \left(t _ {f} ^ {*}\right), t _ {f} ^ {*} \right] = - \frac {\partial \varphi \left[ \boldsymbol {x} ^ {*} \left(t _ {f} ^ {*}\right) , t _ {f} ^ {*} \right]}{\partial t _ {f}}$$

证明 令辅助变量 $\mathbf{x}_{n + 1}(t) = t$ ，则有

$$\dot {x} _ {n + 1} (t) = 1, \quad x _ {n + 1} (t _ {0}) = t _ {0}, \quad x _ {n + 1} (t _ {f}) = t _ {f}$$

构造增广向量

$$
\bar {\boldsymbol {x}} (t) = \left[ \begin{array}{c} \boldsymbol {x} (t) \\ x _ {n + 1} (t) \end{array} \right], \quad \bar {\boldsymbol {f}} (\bar {\boldsymbol {x}}, \boldsymbol {u}) = \left[ \begin{array}{c} f (\boldsymbol {x}, \boldsymbol {u}, t) \\ 1 \end{array} \right], \quad \bar {\boldsymbol {x}} _ {0} (t _ {0}) = \left[ \begin{array}{c} \boldsymbol {x} _ {0} \\ t _ {0} \end{array} \right] = \bar {\boldsymbol {x}} _ {0}
$$

于是，该时变问题转化为如下定常问题：

$$\min _ {\boldsymbol {u} (t) \in \Omega} J = \varphi [ \bar {\boldsymbol {x}} (t _ {f}) ] = \varphi [ \boldsymbol {x} (t _ {f}), x _ {n + 1} (t _ {f}) ]\text { s. t. } \quad \dot {\boldsymbol {x}} (t) = \overline {{\boldsymbol {f}}} [ \overline {{\boldsymbol {x}}} (t), \boldsymbol {u} (t) ], \quad \overline {{\boldsymbol {x}}} (t _ {0}) = \overline {{\boldsymbol {x}}} _ {0}$$

令辅助协态变量为 $\lambda_{n+1}(t)$ ，构造增广协态向量

$$
\bar {\lambda} (t) = \left[ \begin{array}{l} \lambda (t) \\ \lambda_ {n + 1} (t) \end{array} \right] \tag {10-53}
$$

哈密顿函数

$$
\begin{array}{l} \bar {H} (\bar {\boldsymbol {x}}, \boldsymbol {u}, \bar {\lambda}) = \bar {\lambda} ^ {\mathrm{T}} (t) \bar {\boldsymbol {f}} (\bar {\boldsymbol {x}}, \boldsymbol {u}) = \lambda^ {\mathrm{T}} (t) \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t) + \lambda_ {n + 1} (t) \\ = H (\boldsymbol {x}, \boldsymbol {u}, \lambda , t) + \lambda_ {n + 1} (t) \tag {10-54} \\ \end{array}
$$

其中 $H(x,u,\lambda ,t) = \lambda^{\mathrm{T}}(t)f(x,u,t)$ (10-55)

由定理 10-8, 协态方程为

$$\dot {\bar {\lambda}} (t) = - \frac {\partial \bar {H}}{\partial x}$$

代入式(10-53)和式(10-54)，得

$$\dot {\lambda} (t) = - \frac {\partial H}{\partial x}, \quad \dot {\lambda} _ {n + 1} (t) = - \frac {\partial H}{\partial t} \tag {10-56}$$

由式(10-55)，下式显然成立

$$\dot {\boldsymbol {x}} (t) = \frac {\partial H}{\partial \boldsymbol {\lambda}} = \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t)$$

从而证明了本定理的结论1)。

根据定理 10-8, 横截条件
