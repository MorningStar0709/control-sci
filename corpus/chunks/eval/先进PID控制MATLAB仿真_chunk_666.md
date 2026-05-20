为了防止 $\hat{\theta}$ 过大而造成控制输入信号 $u(t)$ 过大，需要通过自适应律的设计使 $\hat{\theta}$ 的变化在 $\left[\theta_{\min}\quad\theta_{\max}\right]$ 范围内，可采用一种映射自适应算法 $^{[1]}$ ，对式（17.32）进行以下修正：

$$
\dot {\hat {\theta}} = \operatorname{Proj} _ {\hat {\theta}} \left(- \gamma s \left(\ddot {x} _ {\mathrm{d}} - c \dot {e}\right)\right) \tag {17.43}
\operatorname{Proj} _ {\hat {\theta}} (\cdot) = \left\{ \begin{array}{l l} 0 & \text {if} \hat {\theta} \geqslant \theta_ {\max} \quad \text {and} \cdot > 0 \\ 0 & \text {if} \hat {\theta} \leqslant \theta_ {\min} \quad \text {and} \cdot <   0 \\ \cdot & \text {otherwise} \end{array} \right. \tag {17.44}
$$

即当 $\hat{\theta}$ 超过最大值时，如果有继续增大的趋势，即 $\dot{\hat{\theta}} > 0$ ，则取 $\hat{\theta}$ 值不变，即 $\dot{\hat{\theta}} = 0$ ；当 $\hat{\theta}$ 超过最小值时，如果有继续减小的趋势，即 $\dot{\hat{\theta}} < 0$ ，则取 $\hat{\theta}$ 值不变，即 $\dot{\hat{\theta}} = 0$ 。

![](image/ab16cf96101e02cc1478b6a61318beff8eba6012007e43fb5a65b6db21c73e5c.jpg)
