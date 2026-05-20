# 5.2.3 控制算法设计与分析

设最优参数为

$$\boldsymbol {\theta} ^ {*} = \arg \min _ {\boldsymbol {\theta} \in \Omega} \left[ \sup _ {x \in R ^ {2}} | \hat {f} (\boldsymbol {x} | \boldsymbol {\theta}) - f (\boldsymbol {x}) | \right] \tag {5.14}$$

式中， $\Omega$ 为 $\theta$ 的集合。则

$$f (x) = \boldsymbol {\theta} ^ {* T} \boldsymbol {\xi} (\boldsymbol {x}) + \varepsilon$$

式中， $\varepsilon$ 为模糊系统的逼近误差。

$$f (\boldsymbol {x}) - \hat {f} (\boldsymbol {x}) = \boldsymbol {\theta} ^ {* T} \boldsymbol {\xi} (\boldsymbol {x}) + \varepsilon - \hat {\boldsymbol {\theta}} \boldsymbol {\xi} (\boldsymbol {x}) = - \tilde {\boldsymbol {\theta}} ^ {T} \boldsymbol {\xi} (\boldsymbol {x}) + \varepsilon$$

定义 Lyapunov 函数为

$$V = \frac {1}{2} s ^ {2} + \frac {1}{2 \gamma} \tilde {\boldsymbol {\theta}} ^ {\mathrm{T}} \tilde {\boldsymbol {\theta}} \tag {5.15}$$

式中， $\gamma>0,\tilde{\theta}=\hat{\theta}-\theta^{*}$ 。则

$$\dot {V} = s \dot {s} + \frac {1}{\gamma} \tilde {\boldsymbol {\theta}} ^ {\mathrm{T}} \dot {\hat {\boldsymbol {\theta}}} = s (c \dot {e} + f (x) + u - \ddot {x} _ {d}) + \frac {1}{\gamma} \tilde {\boldsymbol {\theta}} ^ {\mathrm{T}} \dot {\hat {\boldsymbol {\theta}}}$$

设计控制律为

$$u = - c \dot {e} - \hat {f} (x) + \ddot {x} _ {d} - \eta \operatorname{sgn} (s) \tag {5.16}$$

则

$$
\begin{array}{l} \dot {V} = s (f (x) - \hat {f} (x) - \eta \operatorname{sgn} (s)) + \frac {1}{\gamma} \tilde {\boldsymbol {\theta}} ^ {\mathrm{T}} \dot {\hat {\boldsymbol {\theta}}} \\ = s \left(- \tilde {\boldsymbol {\theta}} ^ {T} \boldsymbol {\xi} (\boldsymbol {x}) + \varepsilon - \eta \operatorname{sgn} (s)\right) + \frac {1}{\gamma} \tilde {\boldsymbol {\theta}} ^ {T} \dot {\hat {\boldsymbol {\theta}}} \\ = \varepsilon s - \eta | s | + \tilde {\boldsymbol {\theta}} ^ {T} \left(\frac {1}{\gamma} \dot {\hat {\boldsymbol {\theta}}} - s \xi (\boldsymbol {x})\right) \\ \end{array}
$$

取 $\eta > |\varepsilon|_{\max}$ ，自适应律为

$$\dot {\hat {\boldsymbol {\theta}}} = \gamma s \xi (\boldsymbol {x}) \tag {5.17}$$

则

$$\dot {V} = \varepsilon s - \eta | s |$$

当 $\eta$ 足够大，且逼近误差 $\varepsilon$ 很小时，可保证 $\dot{V} \leqslant 0$ 。

当 $\dot{V} \equiv 0$ 时, $s \equiv 0$ , 根据 LaSalle 不变性原理[35], 闭环系统为渐近稳定, 即当 $t \to \infty$ 时, $s \to 0$ , 从而 $e \to 0$ , $\dot{e} \to 0$ , 系统的收敛速度取决于 $\eta$ 。由于 $V \geqslant 0$ , $\dot{V} \leqslant 0$ , 则当 $t \to \infty$ 时, $V$ 有界, 从而 $\tilde{\theta}$ 有界。
