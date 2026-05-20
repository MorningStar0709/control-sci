# 5.4.1 扩张观测器的设计

考虑如下对象

$$J \ddot {\theta} = u (t) - d (t) \tag {5.32}$$

式中，J 为转动惯量；u 为控制输入； $\theta$ 为实际角度； $d(t)$ 为外加干扰。

式（5.32）可写为

$$\ddot {\theta} = b u (t) + f (t) \tag {5.33}$$

式中， $b=\frac{1}{J}$ 为已知； $f(t)=-\frac{1}{J}d(t)$ 为未知， $f(\cdot)$ 的导数存在且有界。

式（5.33）可写为

$$\dot {x} = A \boldsymbol {x} + B (b u + f (t)) \tag {5.34}y = C x \tag {5.35}$$

式中， $x=\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}=\begin{bmatrix}\theta\\ \dot{\theta}\end{bmatrix};\quad A=\begin{bmatrix}0&1\\ 0&0\end{bmatrix};\quad B=\begin{bmatrix}0\\1\end{bmatrix};\quad C=\begin{bmatrix}1&0\end{bmatrix};\quad\left|\dot{f}(\cdot)\right|\leqslant L$ 。

参考文献[6]，扩张观测器设计为

$$\dot {\hat {x}} _ {1} = \hat {x} _ {2} + \frac {\alpha_ {1}}{\varepsilon} (y - \hat {x} _ {1}) \tag {5.36}\dot {\hat {x}} _ {2} = b u + \hat {\sigma} + \frac {\alpha_ {2}}{\varepsilon^ {2}} (y - \hat {x} _ {1}) \tag {5.37}\dot {\hat {\sigma}} = \frac {\alpha_ {3}}{\varepsilon^ {3}} (y - \hat {x} _ {1}) \tag {5.38}$$

采用该扩张观测器，可实现

当 $t\to\infty$ 时， $\hat{x}_{1}(t)\to x_{1}(t),\hat{x}_{2}(t)\to x_{2}(t),\hat{\sigma}(t)\to f(\theta,\dot{\theta},t)$ 。

式中， $\hat{x}_{1}$ 、 $\hat{x}_{2}$ 和 $\hat{\sigma}$ 为观测器状态； $\varepsilon>0$ ； $\alpha_{1}$ 、 $\alpha_{2}$ 和 $\alpha_{3}$ 为正实数；多项式 $s^{3}+\alpha_{1}s^{2}+\alpha_{2}s+\alpha_{3}$ 满足 Hurwitz 条件。

在 PID 控制中，可将对干扰项 $f(t)$ 的观测结果加到控制器 $u(t)$ 中，以提高控制精度。

![](image/df5e6d8a57337faba53ab4098267fae8a06a4e43a144475086d10df85f5a40ca.jpg)
