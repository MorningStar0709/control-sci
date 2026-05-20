# 5.1.2 观测器设计

设计观测器为 $^{[1]}$

$$\dot {\hat {d}} = k _ {1} (\hat {\omega} - \dot {\theta}) \tag {5.2}\dot {\hat {\omega}} = - \hat {d} + a u - k _ {2} (\hat {\omega} - \dot {\theta}) - b \dot {\theta} \tag {5.3}$$

式中， $\hat{d}$ 为对 d 项的估计； $\hat{\omega}$ 为对 $\dot{\theta}$ 的估计； $k_{1}>0$ ； $k_{2}>0$ 。

稳定性分析：

定义 Lyapunov 函数为

$$V = \frac {- 1}{2 k _ {1}} \tilde {d} ^ {2} + \frac {1}{2} \tilde {\omega} ^ {2} \tag {5.4}$$

式中， $\tilde{d}=d-\hat{d}$ ； $\tilde{\omega}=\dot{\theta}-\hat{\omega}$ ，则

$$\dot {V} = \frac {1}{k _ {1}} \tilde {d} \dot {\tilde {d}} + \tilde {\omega} \dot {\tilde {\omega}} = \frac {1}{k _ {1}} \tilde {d} (\dot {d} - \dot {\hat {d}}) + \tilde {\omega} (\ddot {\theta} - \dot {\hat {\omega}}) \tag {5.5}$$

假设干扰 d 为慢时变信号， $\dot{d}$ 很小，当取 $k_{1}$ 较大值时，有

$$\frac {1}{k _ {1}} \dot {d} \approx 0 \tag {5.6}$$

将式（5.2）、式（5.3）、式（5.6）代入式（5.5），得

$$
\begin{array}{l} \dot {V} = \frac {1}{k _ {1}} \tilde {d} \dot {d} - \frac {1}{k _ {1}} \tilde {d} \dot {\hat {d}} + \tilde {\omega} (\ddot {\theta} - (- \hat {d} + a u - k _ {2} (\hat {\omega} - \dot {\theta}) - b \dot {\theta})) \\ = \frac {1}{k _ {1}} \tilde {d} \dot {d} - \frac {1}{k _ {1}} \tilde {d} k _ {1} (\hat {\omega} - \dot {\theta}) + \tilde {\omega} (- b \dot {\theta} + a u - d - (- \hat {d} + a u - k _ {2} (\hat {\omega} - \dot {\theta}) - b \dot {\theta})) \\ = \frac {1}{k _ {1}} \tilde {d} \dot {d} - \tilde {d} (\hat {\omega} - \dot {\theta}) + \tilde {\omega} (- d + \hat {d} + k _ {2} (\hat {\omega} - \dot {\theta})) \\ = \frac {1}{k _ {1}} \tilde {d} \dot {d} + \tilde {d} \tilde {\omega} + \tilde {\omega} (- \tilde {d} - k _ {2} \tilde {\omega}) = \frac {1}{k _ {1}} \tilde {d} \dot {d} - k _ {2} \tilde {\omega} ^ {2} \leqslant 0 \\ \end{array}
$$

通过采用本观测器，对 d 项进行有效的观测，从而实现补偿。根据式（5.1），加入补偿后的控制律为

$$u = u _ {0} + \frac {1}{a} \hat {d} \tag {5.7}$$

式中， $u_{0}$ 为 PID 控制。

![](image/73bd503dd7dd11a765854f561368a81a11a931342fdf22ed8bad17e12ab36b47.jpg)
