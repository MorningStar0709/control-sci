# 9.3 比较法

考虑扰动系统(9.1)，设 $V(x)$ 为标称系统(9.2)的一个李雅普诺夫函数， $V$ 沿系统(9.1)轨线的导数满足微分不等式

$$\dot {V} \leqslant h (t, V)$$

由引理3.4(比较引理)得 $V(t,x(t))\leqslant y(t)$

其中， $y(t)$ 是微分方程 $\dot{y} = h(t,y),\quad y(t_0) = V(t_0,x(t_0))$

的解。当微分不等式为线性的时，即 $h(t,V) = a(t)V + b(t)$ 时，这种方法是非常有效的，因为此时可以写出关于 $y$ 的一阶线性微分方程解的闭式表达式。当标称系统(9.2)的原点是指数稳定的时，就可能得出线性微分不等式。

设 $V(t,x)$ 是标称系统(9.2)的一个李雅普诺夫函数，对于所有 $(t,x)\in [0,\infty)\times D$ ，满足式(9.3)至式(9.5)，其中 $D = \{x\in R^n\mid \| x\| < r\}$ 。假设扰动项 $g(t,x)$ 满足边界

$$\| g (t, x) \| \leqslant \gamma (t) \| x \| + \delta (t), \forall t \geqslant 0, \forall x \in D \tag {9.15}$$

其中， $\gamma: R \to R$ 对于所有 $t \geqslant 0$ 是非负且连续的， $\delta: R \to R$ 对于所有 $t \geqslant 0$ 是非负、连续且有界的。 $V$ 沿系统(9.1)轨线的导数满足

$$\dot {V} (t, x) = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) + \frac {\partial V}{\partial x} g (t, x)\leqslant - c _ {3} \| x \| ^ {2} + \left\| \frac {\partial V}{\partial x} \right\| \| g (t, x) \| \tag {9.16}\leqslant - c _ {3} \| x \| ^ {2} + c _ {4} \gamma (t) \| x \| ^ {2} + c _ {4} \delta (t) \| x \|$$

运用式(9.3)，可以得到 $\dot{V}$ 的上界

$$\dot {V} \leqslant - \left[ \frac {c _ {3}}{c _ {2}} - \frac {c _ {4}}{c _ {1}} \gamma (t) \right] V + c _ {4} \delta (t) \sqrt {\frac {V}{c _ {1}}}$$

为了得到线性微分不等式,取 $W(t)=\sqrt{V(t,x(t))}$ , 当 $V\neq0$ 时, 利用 $\dot{W}=\dot{V}/2\sqrt{V}$ 可以得出

$$\dot {W} \leqslant - \frac {1}{2} \left[ \frac {c _ {3}}{c _ {2}} - \frac {c _ {4}}{c _ {1}} \gamma (t) \right] W + \frac {c _ {4}}{2 \sqrt {c _ {1}}} \delta (t) \tag {9.17}$$

当 V=0 时, 可以证明 $D^{+}W(t)\leqslant c_{4}\delta(t)/2\sqrt{c_{1}}$ 。因此对于 V 的所有取值, $D^{+}W(t)$ 满足式(9.17)(见习题9.14)。运用比较引理, $W(t)$ 满足不等式

$$W (t) \leqslant \phi (t, t _ {0}) W (t _ {0}) + \frac {c _ {4}}{2 \sqrt {c _ {1}}} \int_ {t _ {0}} ^ {t} \phi (t, \tau) \delta (\tau) d \tau \tag {9.18}$$

其中,转移函数 $\phi(t,t_{0})$ 为

$$\phi (t, t _ {0}) = \exp \left[ - \frac {c _ {3}}{2 c _ {2}} (t - t _ {0}) + \frac {c _ {4}}{2 c _ {1}} \int_ {t _ {0}} ^ {t} \gamma (\tau) d \tau \right]$$

将式(9.3)代入式(9.18)，可得

$$\| x (t) \| \leqslant \sqrt {\frac {c _ {2}}{c _ {1}}} \phi (t, t _ {0}) \| x (t _ {0}) \| + \frac {c _ {4}}{2 c _ {1}} \int_ {t _ {0}} ^ {t} \phi (t, \tau) \delta (\tau) d \tau \tag {9.19}$$

现在假设对于非负常数 $\varepsilon$ 和 $\eta, \gamma(t)$ 满足条件

$$\int_ {t _ {0}} ^ {t} \gamma (\tau) d \tau \leqslant \varepsilon (t - t _ {0}) + \eta \tag {9.20}$$

其中 $\varepsilon < \frac{c_{1}c_{3}}{c_{2}c_{4}}$ (9.21)
