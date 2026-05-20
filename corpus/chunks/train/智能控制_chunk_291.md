式中，Q 是一个任意的 $n \times n$ 正定矩阵， $\Lambda$ 由式(5.54)给出，其特征根实部为负。

取 $V_{1}=\frac{1}{2}e^{T}Pe,V_{2}=\frac{b}{2\gamma}(\boldsymbol{\theta}^{*}-\boldsymbol{\theta})^{\mathrm{T}}(\boldsymbol{\theta}^{*}-\boldsymbol{\theta})$ ，令 $M=b(\boldsymbol{\theta}^{*}-\boldsymbol{\theta})^{\mathrm{T}}\xi(x)-b_{\omega}$ ，则式(5.59)变为

$$
\dot {\boldsymbol {e}} = \boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {M}
\begin{array}{l} \dot {V} _ {1} = \frac {1}{2} \dot {\boldsymbol {e}} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {e} + \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {P} \dot {\boldsymbol {e}} = \frac {1}{2} \left(\boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {\Lambda} ^ {\mathrm{T}} + \boldsymbol {M} ^ {\mathrm{T}}\right) \boldsymbol {P} \boldsymbol {e} + \frac {1}{2} \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {P} (\boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {M}) \\ = \frac {1}{2} e ^ {\mathrm{T}} \left(\boldsymbol {\Lambda} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P} \boldsymbol {\Lambda} e\right) + \frac {1}{2} \boldsymbol {M} ^ {\mathrm{T}} \boldsymbol {P} e + \frac {1}{2} e ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {M} \\ = - \frac {1}{2} e ^ {\mathrm{T}} Q e + \frac {1}{2} \left(M ^ {\mathrm{T}} P e + e ^ {\mathrm{T}} P M\right) = - \frac {1}{2} e ^ {\mathrm{T}} Q e + e ^ {\mathrm{T}} P M \\ \end{array}
$$

即

$$
\begin{array}{l} \dot {V} _ {1} = - \frac {1}{2} e ^ {T} Q e + e ^ {T} P b \left(\left(\boldsymbol {\theta} ^ {*} - \boldsymbol {\theta}\right) ^ {T} \xi (\boldsymbol {x}) - \omega\right) \\ \dot {V} _ {2} = - \frac {b}{\gamma} (\boldsymbol {\theta} ^ {*} - \boldsymbol {\theta}) ^ {\mathrm{T}} \dot {\boldsymbol {\theta}} \\ \end{array}
$$

$V$ 的导数为

$$\dot {V} = - \frac {1}{2} e ^ {\mathrm{T}} Q e + e ^ {\mathrm{T}} P b \left[ (\boldsymbol {\theta} ^ {*} - \boldsymbol {\theta}) ^ {\mathrm{T}} \xi (x) - \omega \right] - \frac {b}{\gamma} (\boldsymbol {\theta} ^ {*} - \boldsymbol {\theta}) ^ {\mathrm{T}} \dot {\boldsymbol {\theta}} \tag {5.62}$$

令 $p_{n}$ 为 P 的最后一列，由 $b = [0, \cdots, 0, b]^{T}$ 可知 $e^{T}Pb = e^{T}p_{n}b$ 。则式(5.62)变为

$$\dot {V} = - \frac {1}{2} e ^ {\mathrm{T}} Q e + \frac {b}{\gamma} \left(\boldsymbol {\theta} ^ {*} - \boldsymbol {\theta}\right) ^ {\mathrm{T}} \left[ \gamma e ^ {\mathrm{T}} p _ {n} \xi (x) - \dot {\boldsymbol {\theta}} \right] - e ^ {\mathrm{T}} p _ {n} b \omega \tag {5.63}$$

取自适应律
