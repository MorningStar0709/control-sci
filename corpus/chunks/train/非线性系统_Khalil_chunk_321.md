(a) 取 $x_{1}=y, x_{2}=\dot{y}, \tau=\omega t$ 和 $\varepsilon=1/\omega$ ，证明方程可由 $dx/d\tau=\varepsilon f(\tau, x, \varepsilon)$ 表示。

(b) 证明对于充分大的 $\omega$ ，系统有一个指数稳定周期解。估计振荡频率和周期轨道在相平面内的位置。

10.19 验证式(10.44)。

提示:从式(10.43)开始,利用当 $t\leqslant1/\sqrt{\eta}$ 时, $\sigma(t)$ 是有界的,而当 $t\geqslant1/\sqrt{\eta}$ 时, $\sigma(t)\leqslant\sigma(1/\sqrt{\eta})$ 。

10.20 应用一般平均化法研究标量系统

$$\dot {x} = \varepsilon (\sin^ {2} t + \sin 1. 5 t + e ^ {- t}) x$$

10.21（见文献[168]） $n$ 阶线性时不变单输入-单输出系统的输出可表示为 $y(t) = \theta^{\mathrm{T}}w(t)$ ，其中 $\theta$ 是 $2n + 1$ 维常参数向量， $w(t)$ 是一个辅助信号，在不知道 $\theta$ 时可由系统的输入和输出合成。假设向量 $\theta$ 未知，并由 $\theta^{*}$ 表示。在辨识实验中，参数 $\theta(t)$ 可由形如 $\dot{\theta} = -\varepsilon e(t)w(t)$ 的适应性定律更新，其中 $e(t) = [\theta(t) - \theta^{*}]^{\mathrm{T}}w(t)$ 是实际系统输出与应用 $\theta(t)$ 得到的估计输出之间的误差。设 $\phi(t) = \theta(t) - \theta^{*}$ 表示参数误差。

(a) 证明 $\dot{\phi} = \varepsilon A(t)\phi$ ，其中 $A(t) = -w(t)w^{\mathrm{T}}(t)$ 。

(b) 运用(一般)平均化法, 推导关于 $w(t)$ 的条件, 以保证对于充分小的 $\varepsilon$ , 当 t 趋于无穷时, $\theta(t)$ 趋于 $\theta^{*}$ 。
