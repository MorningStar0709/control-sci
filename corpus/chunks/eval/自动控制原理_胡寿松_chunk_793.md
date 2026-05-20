$$H \left[ \boldsymbol {x} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {u} ^ {*} \left(t _ {f} ^ {*}\right), \boldsymbol {\lambda} \left(t _ {f} ^ {*}\right) \right] = 0$$

证明 令辅助变量 $x_0(t) = \int_{t_0}^t L(x, u) \mathrm{d}t$ ，则有

$$\dot {x} _ {0} (t) = L (\boldsymbol {x}, \boldsymbol {u}), \quad x _ {0} \left(t _ {0}\right) = 0x _ {0} \left(t _ {f}\right) = \int_ {t _ {0}} ^ {t _ {f}} L (\boldsymbol {x}, \boldsymbol {u}) \mathrm{d} t = J (\boldsymbol {u})$$

构造增广向量

$$
\bar {\boldsymbol {x}} (t) = \left[ \begin{array}{c} x _ {0} (t) \\ \boldsymbol {x} (t) \end{array} \right], \quad \bar {\boldsymbol {f}} (\bar {\boldsymbol {x}}, \boldsymbol {u}) = \left[ \begin{array}{c} L (\boldsymbol {x}, \boldsymbol {u}) \\ f (\boldsymbol {x}, \boldsymbol {u}) \end{array} \right], \quad \bar {\boldsymbol {x}} (t _ {0}) = \left[ \begin{array}{c} 0 \\ \boldsymbol {x} _ {0} \end{array} \right] = \bar {\boldsymbol {x}} _ {0}
$$

于是，积分型性能指标问题转化为如下末值型性能指标问题：

$$\min _ {\boldsymbol {u} (t) \in \Omega} J (\boldsymbol {u}) = x _ {0} \left(t _ {f}\right) \triangleq \varphi [ \bar {\boldsymbol {x}} \left(t _ {f}\right) ]\text { s. t. } \quad \dot {\bar {x}} (t) = \bar {f} (\bar {x}, u), \quad \bar {x} (t _ {0}) = \bar {x} _ {0}$$

令 $\lambda_{0}(t)$ 为辅助协态变量, 构造增广协态向量

$$
\bar {\lambda} (t) = \left[ \begin{array}{c} \lambda_ {0} (t) \\ \lambda (t) \end{array} \right] \tag {10-58}
$$

及哈密顿函数

$$
\begin{array}{l} \bar {H} (\bar {x}, u, \bar {\lambda}) = \bar {\lambda} ^ {T} (t) \bar {f} (\bar {x}, u) = \lambda_ {0} L (x, u) + \lambda^ {T} f (x, u) \\ = H _ {0} (\boldsymbol {x}, \boldsymbol {u}, \lambda) + \lambda_ {0} L (\boldsymbol {x}, \boldsymbol {u}) \tag {10-59} \\ \end{array}
$$

由定理 10-8, 协态方程为

$$\dot {\bar {\lambda}} (t) = \frac {\partial \bar {H}}{\partial \bar {x}}$$

代入式(10-58)及式(10-59)，得

$$
\left[ \begin{array}{l} \dot {\lambda} _ {0} (t) \\ \dot {\boldsymbol {\lambda}} (t) \end{array} \right] = - \left[ \begin{array}{l} \frac {\partial \bar {H}}{\partial x _ {0}} \\ \frac {\partial \bar {H}}{\partial \boldsymbol {x}} \end{array} \right] = - \left[ \begin{array}{l} 0 \\ \frac {\partial \bar {H}}{\partial \boldsymbol {x}} \end{array} \right]
$$

因而有

$$\lambda_ {0} (t) = \text { const } \tag {10-60}\dot {\lambda} (t) = - \frac {\partial \bar {H}}{\partial x} \tag {10-61}$$

再由定理 10-8 的横截条件可得

$$\bar {\lambda} (t _ {f}) = \frac {\partial \varphi [ \bar {x} (t _ {f}) ]}{\partial \bar {x} (t _ {f})}$$
