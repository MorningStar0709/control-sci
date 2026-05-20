# 5.5.1 系统描述

考虑对象

$$G (s) = \frac {k}{s ^ {2} + a s + b} \tag {5.48}$$

式（5.48）可表示为

$$\ddot {\theta} = - a \dot {\theta} - b \theta + k u (t) \tag {5.49}$$

式中， $\theta(t)$ 为位置信号；u为控制输入。

取 $z=\left[\begin{matrix}\theta & \dot{\theta}\end{matrix}\right]^{T}$ ，式（5.49）可表示为

$$\dot {z} (t) = A z (t) + H u (t) \tag {5.50}$$

式中， $A=\begin{bmatrix}0&1\\ -b&-a\end{bmatrix},\quad H=\begin{bmatrix}0&k\end{bmatrix}^{\mathrm{T}}$ 。

假设输出信号有延迟， $\Delta$ 为输出的位置时间延迟，则实际输出可表示为

$$\overline {{{y}}} (t) = \theta (t - \Delta) = C z (t - \Delta) \tag {5.51}$$

式中， $C=\begin{bmatrix}1 & 0\end{bmatrix}$ 。

观测的目标为：当 $t\to\infty$ 时， $\hat{\theta}(t)\to\theta(t)$ ， $\hat{\dot{\theta}}(t)\to\dot{\theta}(t)$ 。

![](image/19177ca6148295a294cd69633992d5c42c4bf5e30a07ac358bd5ab899d3fbbff.jpg)
