# 9.7.3 控制算法设计与分析

由于 $f(x) - \hat{f} (x) = W^{*\mathrm{T}}h(x) + \varepsilon -\hat{W}^{\mathrm{T}}h(x) = -\widetilde{W}^{\mathrm{T}}h(x) + \varepsilon$

定义 Lyapunov 函数为

$$V = \frac {1}{2} s ^ {2} + \frac {1}{2 \gamma} \widetilde {\boldsymbol {W}} ^ {\mathrm{T}} \widetilde {\boldsymbol {W}} \tag {9.36}$$

式中， $\gamma > 0, \widetilde{\pmb{W}} = \hat{\pmb{W}} - \pmb{W}^{*}$ 。则

$$\dot {V} = s \dot {s} + \frac {1}{\gamma} \widetilde {\boldsymbol {W}} ^ {\mathrm{T}} \dot {\hat {\boldsymbol {W}}} = s (\lambda \dot {e} + f (x) + u - \ddot {x} _ {\mathrm{d}}) + \frac {1}{\gamma} \widetilde {\boldsymbol {W}} ^ {\mathrm{T}} \dot {\hat {\boldsymbol {W}}}$$

设计控制律为

$$u = - \lambda \dot {e} - \hat {f} (x) + \ddot {x} _ {\mathrm{d}} - \eta \text {sign} (s) \tag {9.37}$$

则

$$
\begin{array}{l} \dot {V} = s (f (x) - \hat {f} (x) - \eta \operatorname{sign} (s)) + \frac {1}{\gamma} \widetilde {\boldsymbol {W}} ^ {\mathrm{T}} \dot {\hat {\boldsymbol {W}}} \\ = s \left(- \widetilde {\boldsymbol {W}} ^ {\mathrm{T}} \boldsymbol {h} (\boldsymbol {x}) + \varepsilon - \eta \operatorname{sign} (s)\right) + \frac {1}{\gamma} \widetilde {\boldsymbol {W}} ^ {\mathrm{T}} \dot {\hat {\boldsymbol {W}}} \\ = \varepsilon s - \eta | s | + \widetilde {\boldsymbol {W}} ^ {\mathrm{T}} \left(\frac {1}{\gamma} \dot {\hat {\boldsymbol {W}}} - s \boldsymbol {h} (\boldsymbol {x})\right) \\ \end{array}
$$

取 $\eta > |\varepsilon|_{\max}$ , 自适应律为

$$\dot {\hat {W}} = \gamma_ {s} h (x) \tag {9.38}$$

则 $\dot{V} = \varepsilon s - \eta |s|\leqslant 0$

由于当且仅当 s=0 时， $\dot{V}=0$ ，即当 $\dot{V}\equiv0$ 时， $s\equiv0$ 。根据 LaSalle 不变性原理 $^{[35]}$ ，闭环系统为渐近稳定，即当 $t\to\infty$ 时， $s\to0$ ，系统的收敛速度取决于 $\eta$ 。

由于 $V \geqslant 0, \dot{V} \leqslant 0$ ，则当 $t \to \infty$ 时， $V$ 有界，从而 $\widetilde{W}$ 有界。

可见,控制律中的鲁棒项 $\eta\mathrm{sgn}(s)$ 的作用是克服神经网络的逼近误差,以保证系统稳定。
