$$
\begin{array}{l} \dot {V} _ {1} = \frac {1}{2} \dot {\boldsymbol {E}} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {E} + \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} \dot {\boldsymbol {E}} = \frac {1}{2} \left(\boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {\Lambda} ^ {\mathrm{T}} + \boldsymbol {M} ^ {\mathrm{T}}\right) \boldsymbol {P} \boldsymbol {E} + \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} (\boldsymbol {\Lambda} \boldsymbol {E} + M) \\ = \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} (\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A}) \boldsymbol {E} + \frac {1}{2} \boldsymbol {M} ^ {\mathrm{T}} \boldsymbol {P E} + \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P M} \\ = - \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {E} + \frac {1}{2} \left(\boldsymbol {M} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {E} + \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {M}\right) = - \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {E} + \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {M} \\ \end{array}
$$

将 $M$ 代入上式，并考虑 $\pmb{E}^{\mathrm{T}}\pmb{P}\pmb{b}\left(\hat{\pmb{W}} -\pmb{W}^{*}\right)^{\mathrm{T}}\pmb{h}(\pmb{x}) = \left(\hat{\pmb{W}} -\pmb{W}^{*}\right)^{\mathrm{T}}\left[\pmb{E}^{\mathrm{T}}\pmb{P}\pmb{b}\pmb{h}(\pmb{x})\right]$ ，得

$$
\begin{array}{l} \dot {V} _ {1} = - \frac {1}{2} E ^ {\mathrm{T}} Q E + E ^ {\mathrm{T}} P b (\hat {W} - W ^ {*}) ^ {\mathrm{T}} h (x) + E ^ {\mathrm{T}} P b \omega \\ = - \frac {1}{2} E ^ {\mathrm{T}} Q E + \left(\hat {W} - W ^ {*}\right) ^ {\mathrm{T}} E ^ {\mathrm{T}} P b h (x) + E ^ {\mathrm{T}} P b \omega \\ \dot {V} _ {2} = \frac {1}{\gamma} \left(\hat {\boldsymbol {W}} - \boldsymbol {W} ^ {*}\right) ^ {\mathrm{T}} \dot {\hat {\boldsymbol {W}}} \\ \end{array}
$$

$V$ 的导数为

$$\dot {V} = \dot {V} _ {1} + \dot {V} _ {2} = - \frac {1}{2} E ^ {\mathrm{T}} Q E + E ^ {\mathrm{T}} P b \omega + \frac {1}{\gamma} (\hat {W} - W ^ {*}) ^ {\mathrm{T}} [ \dot {\hat {W}} + \gamma E ^ {\mathrm{T}} P b h (x) ]$$

将自适应律式（9.19）代入上式，得

$$\dot {V} = - \frac {1}{2} E ^ {\mathrm{T}} Q E + E ^ {\mathrm{T}} P b \omega$$

由于 $-\frac{1}{2} E^{\mathrm{T}}QE \leqslant 0$ ，通过选取 $Q$ 和选取最小逼近误差 $\omega$ 非常小的神经网络，可实现 $\dot{V} \leqslant 0$ 。

由于且当且仅当 E=0 时， $\dot{V}=0$ 。即当 $\dot{V}\equiv0$ 时， $E\equiv0$ ，但不能保证 $\omega\equiv0$ 。根据 LaSalle 不变性原理，闭环系统为渐进稳定，即当 $t\to\infty$ 时， $E\to0$ ，从而 $e\to0$ ， $\dot{e}\to0$ ，系统的收敛速度取决于 Q。

由于 $V \geqslant 0$ ， $\dot{V} \leqslant 0$ ，则当 $t \to \infty$ 时， $V$ 有界，因此，可以证明 $\hat{W}$ 有界，但无法保证 $\hat{W}$ 收敛于 $W$ ，即无法保证 $\hat{f}(x)$ 收敛于 $f(x)$ 。

![](image/406acc6ca0178ff1e69c1559a6fb000b27bcd77804ed038679fcf7d0f2aafa8c.jpg)
