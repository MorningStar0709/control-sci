$$
\begin{array}{l} \delta J (u (\cdot)) = \left\{\frac {\partial}{\partial x (t _ {j})} \left[ \frac {1}{2} x ^ {T} (t _ {j}) S x (t _ {j}) \right] - \frac {\partial}{\partial x ^ {T} (t _ {j})} [ x (t _ {j}) ] \lambda (t _ {j}) \right\} ^ {T} \delta x (t _ {j}) \\ + \int_ {0} ^ {t _ {f}} \left\{\left[ \frac {\partial}{\partial x} H (x, u, \lambda) + \frac {\partial}{\partial x ^ {T}} x \lambda \right] ^ {T} \delta x \right. \\ + \left[ \frac {\partial}{\partial u} H (x, u, \lambda) \right] ^ {T} \delta u \rbrace d t \tag {5.183} \\ \end{array}
$$

将其化简之则为：

$$
\begin{array}{l} \delta J (\boldsymbol {u} (\cdot)) = [ S \boldsymbol {x} (t _ {f}) - \lambda (t _ {f}) ] ^ {T} \delta \boldsymbol {x} (t _ {f}) + \int_ {0} ^ {t _ {f}} \left\{\left[ \frac {\partial H}{\partial \boldsymbol {x}} + \dot {\lambda} \right] ^ {T} \delta \boldsymbol {x} \right. \\ + \left[ \frac {\partial H}{\partial u} \right] ^ {T} \delta u \} d t \tag {5.184} \\ \end{array}
$$

但据变分法知， $J(\pmb{u}^{*}(\cdot))$ 取极小值的必要条件是 $\delta J(\pmb{u}^{*}(\cdot)) = 0$ 。由此，并考虑到 $\delta u(\cdot),\delta x(\cdot)$ 和 $\delta x(t_{j})$ 的任意性，故可由(5.184)进一步导出

$$\dot {\lambda} = - \frac {\partial}{\partial x} H (x, u ^ {*}, \lambda) \tag {5.185}\lambda \left(t _ {f}\right) = S x \left(t _ {f}\right) \tag {5.186}\frac {\partial}{\partial u} H (x, u ^ {*}, \lambda) = 0 \tag {5.187}$$

再次，利用（5.181）和（5.187），有

$$
\begin{array}{l} 0 = \frac {\partial H}{\partial u} = \frac {\partial}{\partial u} \left[ \frac {1}{2} \left(x ^ {T} Q x + u ^ {* T} R u ^ {*}\right) + \lambda^ {T} (A x + B u ^ {*}) \right] \\ - R \alpha^ {*} + B ^ {T} \lambda \tag {5.188} \\ \end{array}
$$

从而，得到

$$\boldsymbol {u} ^ {*} (\cdot) = - R ^ {- 1} B ^ {T} \lambda \tag {5.189}$$

并且，利用(5.189)的同时，可由(5.174)、(5.185)和(5.186)，导出如下的两点边值问题：

$$\dot {x} ^ {*} = A x ^ {*} - B R ^ {- 1} B ^ {T} \lambda , \quad x ^ {*} (0) = x _ {0} \tag {5.190}\dot {\lambda} = - A ^ {T} \lambda - Q x ^ {*}, \quad \lambda (t _ {j}) = S x ^ {*} (t _ {j}) \tag {5.191}$$

注意到上述方程和端点条件均为线性,所以可知 $\lambda(t)$ 和 $x(t)$ 之间必为线性关系,表为:

$$\lambda (t) = P (t) x ^ {*} (t) \tag {5.192}$$

其中， $P(t)$ 应满足的方程可由(5.190)—(5.192)来导出。为此，由(5.192)和(5.190)可得

$$
\begin{array}{l} \dot {\lambda} = \dot {P} (t) x ^ {*} (t) + P (t) \dot {x} ^ {*} (t) \\ = \dot {P} (t) x ^ {*} (t) + P (t) A x ^ {*} (t) - P (t) B R ^ {- 1} B ^ {T} P (t) x ^ {*} (t) \tag {5.193} \\ \end{array}
$$

而由(5.191)和(5.192)又可得

$$\dot {\lambda} = - A ^ {T} P (t) x ^ {*} (t) - Q x ^ {*} (t) \tag {5.194}$$
