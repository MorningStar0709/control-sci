$$
\dot {\boldsymbol {e}} = \boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {M}
\begin{array}{l} \dot {V} _ {1} = \frac {1}{2} \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {e} + \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {P} \dot {\boldsymbol {e}} = \frac {1}{2} \left(\boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {\Lambda} ^ {\mathrm{T}} + \boldsymbol {M} ^ {\mathrm{T}}\right) \boldsymbol {P} \boldsymbol {e} + \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {P} (\boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {M}) \\ = \frac {1}{2} e ^ {\mathrm{T}} \left(\boldsymbol {\Lambda} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P} \boldsymbol {\Lambda}\right) e + \frac {1}{2} \boldsymbol {M} ^ {\mathrm{T}} \boldsymbol {P} e + \frac {1}{2} e ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {M} \\ = - \frac {1}{2} e ^ {\mathrm{T}} Q e + \frac {1}{2} \left(M ^ {\mathrm{T}} P e + e ^ {\mathrm{T}} P M\right) = - \frac {1}{2} e ^ {\mathrm{T}} Q e + e ^ {\mathrm{T}} P M \\ \end{array}
$$

即

$$
\begin{array}{l} \dot {V} _ {1} = - \frac {1}{2} e ^ {\mathrm{T}} Q e + e ^ {\mathrm{T}} P b \omega + \left(\boldsymbol {\theta} _ {f} - \boldsymbol {\theta} _ {f} ^ {*}\right) ^ {\mathrm{T}} e ^ {\mathrm{T}} P b \xi (x) + \left(\boldsymbol {\theta} _ {g} - \boldsymbol {\theta} _ {g} ^ {*}\right) ^ {\mathrm{T}} e ^ {\mathrm{T}} P b \eta (x) u \\ \dot {V} _ {2} = \frac {1}{\gamma_ {1}} \left(\boldsymbol {\theta} _ {f} - \boldsymbol {\theta} _ {f} ^ {*}\right) ^ {\mathrm{T}} \dot {\boldsymbol {\theta}} _ {f} \\ \dot {V} _ {3} = \frac {1}{\gamma_ {2}} \left(\boldsymbol {\theta} _ {g} - \boldsymbol {\theta} _ {g} ^ {*}\right) ^ {T} \dot {\boldsymbol {\theta}} _ {g} \\ \end{array}
$$

$V$ 的导数为

$$
\begin{array}{l} \dot {V} = \dot {V} _ {1} + \dot {V} _ {2} + \dot {V} _ {3} \\ = - \frac {1}{2} e ^ {\mathrm{T}} Q e + e ^ {\mathrm{T}} P b \omega + \frac {1}{\gamma_ {1}} \left(\boldsymbol {\theta} _ {f} - \boldsymbol {\theta} _ {f} ^ {*}\right) ^ {\mathrm{T}} \left[ \dot {\boldsymbol {\theta}} _ {f} + \gamma_ {1} e ^ {\mathrm{T}} P b \xi (x) \right] + \\ \frac {1}{\gamma_ {2}} \left(\boldsymbol {\theta} _ {g} - \boldsymbol {\theta} _ {g} ^ {*}\right) ^ {\mathrm{T}} \left[ \dot {\boldsymbol {\theta}} _ {g} + \gamma_ {2} e ^ {\mathrm{T}} \boldsymbol {P b} \boldsymbol {\eta} (\boldsymbol {x}) u \right] \tag {5.40} \\ \end{array}
$$

将自适应律式(5.28)和式(5.29)代入式(5.40)，得

$$\dot {V} = - \frac {1}{2} e ^ {\mathrm{T}} Q e + e ^ {\mathrm{T}} P b _ {\omega} \tag {5.41}$$

当 Q 足够大, 且逼近误差 $\omega$ 很小时, 可保证 $\dot{V} \leqslant 0$ 。

当 $\dot{V}\equiv0$ 时, $e\equiv0$ ,根据LaSalle不变性原理 $^{[35]}$ ,闭环系统为渐近稳定,即当 $t\to\infty$ 时, $e\to0$ ,系统的收敛速度取决于Q。由于 $V\geqslant0,\dot{V}\leqslant0$ ,则当 $t\to\infty$ 时,V有界,从而 $\tilde{\theta}_{f}$ 和 $\tilde{\theta}_{g}$ 有界。
