$$\dot {V} = - \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {E} + \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P b} \omega$$

由于 $-\frac{1}{2}E^{T}QE \leqslant 0$ ，通过选取 Q 和最小逼近误差 $\omega$ 非常小的模糊系统，可实现 $\dot{V} \leqslant 0$ 。

由于且当且仅当 E=0 时， $\dot{V}=0$ 。即当 $\dot{V}\equiv0$ 时， $E\equiv0$ ，但不能保证 $\omega\equiv0$ 。根据 LaSalle 不变性原理，闭环系统为渐进稳定，即当 $t\to\infty$ 时， $E\to0$ ，从而 $e\to0$ ， $\dot{e}\to0$ ，系统的收敛速度取决于 Q。

由于 $V \geqslant 0$ ， $\dot{V} \leqslant 0$ ，则当 $t \to \infty$ 时， $V$ 有界，因此，可以证明 $\theta_f$ 有界，但无法保证 $\theta_f$ 收敛于 $\theta_f^*$ ，即无法保证 $\hat{f}(x)$ 收敛于 $f(x)$ 。

![](image/5f314e39732d8cba18989db6d64e05a2fcc80ec48068fe98fb229320a3028201.jpg)
