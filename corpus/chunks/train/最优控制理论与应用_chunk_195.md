$$H (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, \boldsymbol {\lambda}, t) = \frac {1}{2} \left[ \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} _ {\mathrm{p}} (t) \boldsymbol {u} (t) - \boldsymbol {v} ^ {\mathrm{T}} (t) \boldsymbol {R} _ {\mathrm{e}} (t) \boldsymbol {v} (t) \right] +\boldsymbol {\lambda} ^ {T} \left[ \boldsymbol {G} _ {p} (t) \boldsymbol {u} (t) - \boldsymbol {G} _ {e} (t) \boldsymbol {v} (t) \right] \tag {10-99}$$

由双方极值原理,知共轭方程和横截条件为

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}} = \boldsymbol {0} \\ \boldsymbol {\lambda} \left(t _ {\mathrm{f}}\right) = \frac {\partial \boldsymbol {\Phi}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} = \boldsymbol {x} \left(t _ {\mathrm{f}}\right) \end{array} \right. \tag {10-100}
$$

因为 $H$ 对 $\pmb{u},\pmb{v}$ 是二次连续可微的，最优解应满足：

$$\frac {\partial H}{\partial \boldsymbol {u}} = \boldsymbol {u} ^ {T} (t) \boldsymbol {R} _ {p} (t) + \boldsymbol {\lambda} ^ {T} (t) \boldsymbol {G} _ {p} (t) = \boldsymbol {0}\frac {\partial H}{\partial \boldsymbol {v}} = - \boldsymbol {v} ^ {\mathrm{T}} (t) \boldsymbol {R} _ {\mathrm{e}} (t) - \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \boldsymbol {G} _ {\mathrm{e}} (t) = \boldsymbol {0}$$

由上二式可解出

$$
\left\{ \begin{array}{l} \boldsymbol {u} ^ {*} (t) = - \boldsymbol {R} _ {\mathrm{p}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{p}} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) \\ \boldsymbol {v} ^ {*} (t) = - \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}} (t) \boldsymbol {\lambda} (t) \end{array} \right. \tag {10-101}
$$

故 $\boldsymbol{u}^{*}(t)$ 使 H 达到极大, $\boldsymbol{v}^{*}(t)$ 使 H 达到极小, $(\boldsymbol{u}^{*}(t), \boldsymbol{v}^{*}(t))$ 确实为极小极大解。

由于相对运动方程式(10-96)、共轭方程式(10-100)都是线性的，求解 $x^{*}(t)$ 和 $\lambda(t)$ 的两点边值问题为线性的，可以采用第5章中的扫描法。令

$$\boldsymbol {\lambda} (t) = \boldsymbol {K} (t) \boldsymbol {x} (t) \tag {10-102}$$

将上式两边对 $t$ 求导
