$$
\begin{array}{l} c (t) = 1 - \mathrm{e} ^ {- \zeta \omega_ {n} t} \left[ \cos \omega_ {d} t + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {d} t \right] \\ = 1 - \frac {1}{\sqrt {1 - \zeta^ {2}}} \mathrm{e} ^ {- \zeta \omega_ {n} t} (\sqrt {1 - \zeta^ {2}} \cos \omega_ {d} t + \zeta \sin \omega_ {d} t) \\ = 1 - \frac {1}{\sqrt {1 - \zeta^ {2}}} \mathrm{e} ^ {- \zeta \omega_ {n} t} \sin (\omega_ {d} t + \beta), \quad t \geqslant 0 \tag {3-14} \\ \end{array}
$$

式中， $\beta=\arctan(\sqrt{1-\zeta^{2}}/\zeta)$ ，或者 $\beta=arccos\zeta$ 。

式(3-14)表明,欠阻尼二阶系统的单位阶跃响应由两部分组成:稳态分量为1,表明图3-8系统在单位阶跃函数作用下不存在稳态位置误差;瞬态分量为阻尼正弦振荡项,其振荡频率为 $\omega_{d}$ ,故称为阻尼振荡频率。由于瞬态分量衰减的快慢程度取决于包络线 $1\pm e^{-\zeta\omega_{n}t}/\sqrt{1-\zeta^{2}}$ 收敛的速度,当 $\zeta$ 一定时,包络线的收敛速度又取决于指数函数 $e^{-\zeta\omega_{n}t}$ 的幂,所以 $\sigma=\zeta\omega_{n}$ 称为衰减系数。

若 $\zeta=0$ ，则二阶系统无阻尼时的单位阶跃响应为

$$c (t) = 1 - \cos \omega_ {n} t, \qquad t \geqslant 0 \tag {3-15}$$

这是一条平均值为1的正、余弦形式的等幅振荡，其振荡频率为 $\omega_{\mathrm{n}}$ ，故可称为无阻尼振荡频率。由图3-6位置控制系统可知， $\omega_{\mathrm{n}}$ 由系统本身的结构参数K和 $\mathrm{T}_{\mathrm{m}}$ 或 $\mathbf{K}_1$ 和J确定，故 $\omega_{\mathrm{n}}$ 常称为自然频率。

应当指出，实际的控制系统通常都有一定的阻尼比，因此不可能通过实验方法测得 $\omega_{\mathrm{n}}$ ，而只能测得 $\omega_{\mathrm{d}}$ ，其值总小于自然频率 $\omega_{\mathrm{n}}$ 。只有在 $\zeta = 0$ 时，才有 $\omega_{\mathrm{d}} = \omega_{\mathrm{n}}$ 。当阻尼比 $\zeta$ 增大时，阻尼振荡频率 $\omega_{\mathrm{d}}$ 将减小。如果 $\zeta \geqslant 1, \omega_{\mathrm{d}}$ 将不复存在，系统的响应不再出现振荡。但是，为了便于分析和叙述， $\omega_{\mathrm{n}}$ 和 $\omega_{\mathrm{d}}$ 的符号和名称在 $\zeta \geqslant 1$ 时仍将沿用下去。

(2) 临界阻尼 $(\zeta=1)$ 二阶系统的单位阶跃响应

设输入信号为单位阶跃函数,则系统输出量的拉氏变换可写为

$$
\begin{array}{l} C (s) = \frac {\omega_ {n} ^ {2}}{s (s + \omega_ {n}) ^ {2}} \\ = \frac {1}{s} - \frac {\omega_ {n}}{(s + \omega_ {n}) ^ {2}} - \frac {1}{s + \omega_ {n}} \\ \end{array}
$$

对上式取拉氏反变换，得临界阻尼二阶系统的单位阶跃响应

$$c (t) = 1 - \mathrm{e} ^ {- \omega_ {n} t} \left(1 + \omega_ {n} t\right), \quad t \geqslant 0 \tag {3-16}$$

上式表明，当 $\zeta = 1$ 时，二阶系统的单位阶跃响应是稳态值为1的无超调单调上升过程，其变化率

$$\frac {\mathrm{d} c (t)}{\mathrm{d} t} = \omega_ {n} ^ {2} t \mathrm{e} ^ {- \omega_ {n} t}$$

当 $t = 0$ 时，响应过程的变化率为零；当 $t > 0$ 时，响应过程的变化率为正，响应过程单调上升；当 $t \to \infty$ 时，响应过程的变化率趋于零，响应过程趋于常值1。通常，临界阻尼情况下的二阶系统的单位阶跃响应称为临界阻尼响应。

(3) 过阻尼 $(\zeta>1)$ 二阶系统的单位阶跃响应

设输入信号为单位阶跃函数，且令
