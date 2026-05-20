# (1) 末端时刻固定时的最优解

当 $t_f$ 固定时，引入拉格朗日乘子向量： $\lambda (t)\in \mathbf{R}^n,\gamma \in \mathbf{R}^r$ ，构造如下广义泛函：

$$
\begin{array}{l} J _ {a} = \varphi [ \boldsymbol {x} (t _ {f}) ] + \boldsymbol {\gamma} ^ {\mathrm{T}} \boldsymbol {\psi} [ \boldsymbol {x} (t _ {f}) ] + \int_ {t _ {0}} ^ {t _ {f}} \left\{L (\boldsymbol {x}, \boldsymbol {u}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} (t) [ \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t) - \dot {\boldsymbol {x}} (t) ] \right\} \mathrm{d} t \\ = \varphi [ \boldsymbol {x} (t _ {f}) ] + \boldsymbol {\gamma} ^ {\mathrm{T}} \boldsymbol {\psi} [ \boldsymbol {x} (t _ {f}) ] + \int_ {t _ {0}} ^ {t _ {f}} [ H (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {\lambda}, t) - \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \dot {\boldsymbol {x}} (t) ] \mathrm{d} t \\ \end{array}
$$

由于分部积分

$$- \int_ {t _ {0}} ^ {t _ {f}} \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \dot {\boldsymbol {x}} (t) \mathrm{d} t = - \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) \Big | _ {t _ {0}} ^ {t _ {f}} + \int_ {t _ {0}} ^ {t _ {f}} \dot {\boldsymbol {\lambda}} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) \mathrm{d} t$$

故广义泛函可表示为

$$
\begin{array}{l} J _ {a} = \varphi [ \boldsymbol {x} (t _ {f}) ] + \boldsymbol {\gamma} ^ {\mathrm{T}} \boldsymbol {\psi} [ \boldsymbol {x} (t _ {f}) ] - \dot {\boldsymbol {\lambda}} ^ {\mathrm{T}} (t _ {f}) \boldsymbol {x} (t _ {f}) + \boldsymbol {\lambda} ^ {\mathrm{T}} (t _ {0}) \boldsymbol {x} (t _ {0}) \\ + \int_ {t _ {0}} ^ {t _ {f}} [ H (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {\lambda}, t) + \dot {\boldsymbol {\lambda}} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) ] \mathrm{d} t \tag {10-44} \\ \end{array}
$$

对广义泛函式(10-44)取一次变分,注意到待定乘子向量 $\lambda(t)$ 和 $\gamma$ 不变分,以及 $\delta x(t_{0})=0$ , 可得

$$\delta J _ {a} = \delta \boldsymbol {x} ^ {\mathrm{T}} (t _ {f}) \left[ \frac {\partial \varphi}{\partial \boldsymbol {x} (t _ {f})} + \frac {\partial \boldsymbol {\psi} ^ {\mathrm{T}}}{\partial \boldsymbol {x} (t _ {f})} \boldsymbol {\gamma} - \boldsymbol {\lambda} (t _ {f}) \right]+ \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial H}{\partial \boldsymbol {x}} + \dot {\boldsymbol {\lambda}}\right) ^ {\mathrm{T}} \delta \boldsymbol {x} + \left(\frac {\partial H}{\partial \boldsymbol {u}}\right) ^ {\mathrm{T}} \delta \boldsymbol {u} \right] \mathrm{d} t \tag {10-45}$$
