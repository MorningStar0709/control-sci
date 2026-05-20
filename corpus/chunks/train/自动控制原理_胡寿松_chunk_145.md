# 5. 二阶系统的单位斜坡响应

当输入信号为单位斜坡函数时，由式(3-11)知，系统输出量的拉氏变换式为

$$
\begin{array}{l} C (s) = \frac {\omega_ {n} ^ {2}}{s ^ {2} \left(s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}\right)} \\ = \frac {1}{s ^ {2}} - \frac {\frac {2 \zeta}{\omega_ {n}}}{s} + \frac {\frac {2 \zeta}{\omega_ {n}} (s + \zeta \omega_ {n}) + (2 \zeta^ {2} - 1)}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}} \\ \end{array}
$$

对上式取拉氏反变换，可得不同 $\zeta$ 值下的二阶系统的单位斜坡响应。

(1) 欠阻尼单位斜坡响应

$$c (t) = t - \frac {2 \zeta}{\omega_ {n}} + \frac {1}{\omega_ {n} \sqrt {1 - \zeta^ {2}}} \mathrm{e} ^ {- \zeta \omega_ {n} t} \sin (\omega_ {d} t + 2 \beta), \quad t \geqslant 0 \tag {3-27}$$

上式表明，欠阻尼二阶系统的单位斜坡响应由稳态分量 $c_{s}(\infty) = t - 2\zeta /\omega_{n}$ 和瞬态分量

$$c _ {t} = \frac {\mathrm{e} ^ {- \zeta \omega_ {n} t}}{\omega_ {d}} \sin (\omega_ {d} t + 2 \beta).$$

组成。在3-6节将要指出，对于图3-8所示的单位反馈系统，误差响应为 $e(t)=r(t)-c(t)$ 。当时间t趋于无穷时，误差响应 $e(t)$ 的稳态值称为稳态误差，以 $e_{s}(\infty)$ 标志。对于单位斜坡响应[式(3-27)]，其稳态误差为

$$e _ {s} (\infty) = t - c _ {s} (\infty) = \frac {2 \zeta}{\omega_ {n}} \tag {3-28}$$

误差响应为

$$e (t) = \frac {2 \zeta}{\omega_ {n}} - \frac {1}{\omega_ {d}} \mathrm{e} ^ {- \zeta \omega_ {n} t} \sin (\omega_ {d} t + 2 \beta) \tag {3-29}$$

将上式对 $t$ 求导并令其为零，得误差响应的峰值时间

$$t _ {p} = \frac {\pi - \beta}{\omega_ {d}} \tag {3-30}$$

它正好等于单位阶跃响应的上升时间。将式(3-30)代入式(3-29)，得误差响应的峰值

$$e (t _ {p}) = \frac {2 \zeta}{\omega_ {n}} \left(1 + \frac {1}{2 \zeta} \mathrm{e} ^ {- \zeta \omega_ {n} t _ {p}}\right)$$

从而，误差响应的最大偏离量可表示为

$$e _ {m} = e \left(t _ {p}\right) - e _ {s s} (\infty) = \frac {1}{\omega_ {n}} \mathrm{e} ^ {- \zeta \omega_ {n} t _ {p}} \tag {3-31}$$

若令 D 表示误差响应对其稳态值的偏差, 则由于

$$e (t) = \frac {2 \zeta}{\omega_ {n}} \left[ 1 - \frac {1}{2 \zeta \sqrt {1 - \zeta^ {2}}} \mathrm{e} ^ {- \zeta \omega_ {n} t} \sin (\omega_ {d} t + 2 \beta) \right]$$

所以 $D$ 由下式限定：

$$D = \left| \frac {1}{2 \zeta \sqrt {1 - \zeta^ {2}}} e ^ {- \zeta \omega_ {n} t} \sin (\omega_ {d} t + 2 \beta) \right| \leqslant \frac {1}{2 \zeta \sqrt {1 - \zeta^ {2}}} e ^ {- \zeta \omega_ {n} t}$$

当取 $\zeta \leqslant 0.8$ 时，上式可进一步表示为 $D \leqslant 1.04\mathrm{e}^{-\zeta \omega_n t}$ 。取 $5\%$ 误差带，可得响应调节时间的近似表达式

$$t _ {s} = \frac {3}{\zeta \omega_ {n}} \tag {3-32}$$

稳态误差、峰值时间、最大偏离量和调节时间，表示了欠阻尼二阶系统的单位斜坡响应性能。图3-18给出了几种 $\zeta$ 值下的无因次误差响应曲线。由图及性能计算公式可以明显看出：减小系统的阻尼比 $\zeta$ ，可以减小系统的稳态误差和峰值时间，但是最大偏离量要增大、调节时间会加长，从而使动态性能恶化。

![](image/1bbd4ad6426745e60754c59f139b5a75a887da29d04eb66bebbc575419d4fb18.jpg)
