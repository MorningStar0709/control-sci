# 8.1.2 控制律设计

设位置指令为 $\theta_{\mathrm{d}}$ ，实际位置为 $\theta$ ，取误差为 $e = \theta_{\mathrm{d}} - \theta$ ，取控制律为

$$u = \frac {1}{g (\boldsymbol {x})} \left[ - f (\boldsymbol {x}) + \ddot {\theta} _ {\mathrm{d}} + k _ {\mathrm{p}} e + k _ {\mathrm{d}} \dot {e} \right] \tag {8.2}$$

式中， $x=\left[\theta,\dot{\theta}\right]^{T}$ 。

将式（8.2）代入式（8.1），得到闭环控制系统的方程：

$$\ddot {e} + k _ {\mathrm{d}} \dot {e} + k _ {\mathrm{p}} e = 0 \tag {8.3}$$

通过 $k_{p}$ 和 $k_{d}$ 的选取，可得 $t\to\infty$ 时， $e(t)\to0,\quad\dot{e}(t)\to0$ ，即系统的输出 $\theta$ 和 $\dot{\theta}$ 渐进地收敛于理想输出 $\theta_{d}$ 和 $\dot{\theta}_{d}$ 。

如果非线性函数 $f(x)$ 是已知的，则可以选择控制 u 来消除其非线性的性质，然后再根据线性控制理论设计控制器。

选择 $k_{p}$ 和 $k_{d}$ ，使多项式 $s^{2} + k_{d}s + k_{p}$ 的所有根部都在复平面左半开平面上，即需要使 $s^{2} + k_{d}s + k_{p} = 0$ 的根为负。

对于任意负根为 $-\lambda(\lambda>0)$ ，有 $(s+\lambda)^{2}=0$ ，可得 $s^{2}+2\lambda s+\lambda^{2}=0$ ，则可设计 $k_{d}=2\lambda$ ， $k_{p}=\lambda^{2}$ 。

![](image/b37ed0bff341194f227e3b9d5673f88fab422c4d8268a0eed2f9e505235cce3c.jpg)
