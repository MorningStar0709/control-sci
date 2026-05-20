$$
\begin{array}{l} \Delta J _ {a} = \varphi [ x ^ {*} (t _ {f}) + \delta x _ {f}, t _ {f} + \delta t _ {f} ] - \varphi [ x ^ {*} (t _ {f}), t _ {f} ] \\ + \boldsymbol {\gamma} ^ {T} \left\{\boldsymbol {\psi} \left[ \boldsymbol {x} ^ {*} \left(t _ {f}\right) + \delta \boldsymbol {x} _ {t}, t _ {f} + \delta t _ {f} \right] - \boldsymbol {\psi} \left[ \boldsymbol {x} ^ {*} \left(t _ {f}\right), t _ {f} \right] \right\} \\ + \int_ {t _ {f}} ^ {t _ {f} + \delta x _ {f}} \left\{H (x ^ {*} + \delta x, u ^ {*} + \delta u, \lambda , t) - \lambda^ {\mathrm{T}} (t) [ \dot {x} ^ {*} + \delta \dot {x} ] \right\} \mathrm{d} t \\ + \int_ {t _ {0}} ^ {t _ {f}} [ H (\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \boldsymbol {u} ^ {*} + \delta \boldsymbol {u}, \lambda , t) - H (\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \lambda , t) - \lambda^ {\mathrm{T}} \delta \dot {\boldsymbol {x}} ] \mathrm{d} t \\ \end{array}
$$

将上式展成泰勒级数并取主部，以及应用积分中值定理并考虑到 $\delta x(t_0) = 0$ ，可得广义泛函变分表达式

$$
\begin{array}{l} \delta J _ {a} = \left[ \frac {\partial \varphi}{\partial \boldsymbol {x} (t _ {f})} \right] ^ {\mathrm{T}} \delta \boldsymbol {x} _ {f} + \frac {\partial \varphi}{\partial t _ {f}} + \boldsymbol {\gamma} ^ {\mathrm{T}} \left\{\left[ \frac {\partial \boldsymbol {\psi} ^ {\mathrm{T}}}{\partial \boldsymbol {x} (t _ {f})} \right] ^ {\mathrm{T}} \delta \boldsymbol {x} _ {f} + \frac {\partial \boldsymbol {\psi}}{\partial t _ {f}} \delta t _ {f} \right\} + (H - \boldsymbol {\lambda} ^ {\mathrm{T}} \dot {\boldsymbol {x}}) \Big | _ {t _ {f}} \delta t _ {f} \\ + \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial H}{\partial \boldsymbol {x}} + \dot {\boldsymbol {\lambda}}\right) ^ {\mathrm{T}} \delta \boldsymbol {x} + \left(\frac {\partial H}{\partial \boldsymbol {u}}\right) ^ {\mathrm{T}} \delta \boldsymbol {u} \right] \mathrm{d} t - (\boldsymbol {\lambda} ^ {\mathrm{T}} \delta \boldsymbol {x}) \Big | _ {t _ {f}} \tag {10-51} \\ \end{array}
$$

由式(10-26)知,如下关系式成立:

$$\partial \boldsymbol {x} (t _ {f}) = \partial \boldsymbol {x} _ {f} - \dot {\boldsymbol {x}} (t _ {f}) \partial t _ {f}$$

将式(10-26)代入式(10-51)，整理得
