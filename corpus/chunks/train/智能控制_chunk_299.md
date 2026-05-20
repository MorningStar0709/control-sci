$$
\begin{array}{l} \dot {V} (t) = - s ^ {\mathrm{T}} (\hat {\boldsymbol {F}} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}) - \hat {\boldsymbol {F}} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} | \boldsymbol {\Theta}) + \boldsymbol {K} _ {\mathrm{D}} s) + \sum_ {i = 1} ^ {n} \tilde {\boldsymbol {\Theta}} _ {i} ^ {\mathrm{T}} \boldsymbol {\Gamma} _ {i} \dot {\tilde {\boldsymbol {\Theta}}} _ {i} \\ = - s ^ {T} \left(\boldsymbol {F} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}) - \hat {\boldsymbol {F}} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} \mid \boldsymbol {\Theta}) + \hat {\boldsymbol {F}} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} \mid \boldsymbol {\Theta} ^ {*}\right) \\ - \hat {\boldsymbol {F}} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} \mid \boldsymbol {\Theta} ^ {*}) + \boldsymbol {K} _ {\mathrm{D}} \boldsymbol {s}) + \sum_ {i = 1} ^ {n} \widetilde {\boldsymbol {\Theta}} _ {i} ^ {\mathrm{T}} \boldsymbol {\Gamma} _ {i} \dot {\widetilde {\boldsymbol {\Theta}}} _ {i} \\ = - \boldsymbol {s} ^ {\mathrm{T}} \left(\widetilde {\boldsymbol {\Theta}} ^ {\mathrm{T}} \xi (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}) + \boldsymbol {\omega} + \boldsymbol {K} _ {\mathrm{D}} \boldsymbol {s}\right) + \sum_ {i = 1} ^ {n} \widetilde {\boldsymbol {\Theta}} _ {i} ^ {\mathrm{T}} \boldsymbol {\Gamma} _ {i} \dot {\widetilde {\boldsymbol {\Theta}}} _ {i} \\ = - s ^ {T} K _ {D} s - s ^ {T} \omega + \sum_ {i = 1} ^ {n} \left(\widetilde {\boldsymbol {\Theta}} _ {i} ^ {T} \boldsymbol {\Gamma} _ {i} \dot {\widetilde {\boldsymbol {\Theta}}} _ {i} - s _ {i} \widetilde {\boldsymbol {\Theta}} _ {i} ^ {T} \xi (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}})\right) \\ \end{array}
$$

式中， $\widetilde{\boldsymbol{\Theta}} = \boldsymbol{\Theta}^{*} - \boldsymbol{\Theta}$ 。

设计自适应律为

$$\dot {\boldsymbol {\Theta}} _ {i} = - \Gamma_ {i} ^ {- 1} s _ {i} \xi (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}), i = 1, 2, \dots , n \tag {5.75}$$

则

$$\dot {V} (t) = - \mathbf {s} ^ {\mathrm{T}} \mathbf {K} _ {\mathrm{D}} \mathbf {s} - \mathbf {s} ^ {\mathrm{T}} \boldsymbol {\omega}$$

当 $K_{D}$ 足够大，且逼近误差 $\omega$ 很小时，可保证 $\dot{V} \leqslant 0$ 。

当 $\dot{V}\equiv0$ 时, $s\equiv0$ ,根据LaSalle不变性原理 $^{[35]}$ ,闭环系统为渐近稳定,即当 $t\to\infty$ 时, $s\to0$ ,系统的收敛速度取决于 $K_{D}$ 。由于 $V\geqslant0,\dot{V}\leqslant0$ ,则当 $t\to\infty$ 时,V有界,从而 $\tilde{\theta}_{i}$ 有界。
