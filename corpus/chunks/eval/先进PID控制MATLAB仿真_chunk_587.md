# 15.1.3 针对第二个子系统的控制

针对第二个子系统，即滚转跟踪子系统设计内环控制输入 $u_{2}$ 。

$$\dot {\theta} = \omega\dot {\omega} = u _ {2}$$

取角度指令为 $\theta_{d}$ ， $e=\theta-\theta_{d}$ 为跟踪误差。设计基于前馈补偿的 PD 控制律为

$$u _ {2} = - k _ {\mathrm{p}} e - k _ {\mathrm{d}} \dot {e} + \ddot {\theta} _ {\mathrm{d}} \tag {15.9}$$

式中， $k_{p}>0,\quad k_{d}>0$ ，则 $\ddot{e}+k_{d}\dot{e}+k_{p}e=0$ 。按极点配置设计 PD 参数，取极点为 -5.0，则 $k_{p}=25,\quad k_{d}=10$ 。姿态控制律的设计中，为了使内环较外环收敛速度快，需要采用较大的 PD 增益。

在控制律式（15.9）中，需要对式（15.8）中的 $\theta_{\mathrm{d}}$ 求导，而该求导过程过于复杂，为了简单起见，可采用如下三阶积分链式微分器实现 $\dot{\theta}_{\mathrm{d}}$ 和 $\ddot{\theta}_{\mathrm{d}}^{[4]}$ ：

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = x _ {3} \tag {15.10}\dot {x} _ {3} = - \frac {k _ {1}}{\varepsilon^ {3}} \left(x _ {1} - \theta_ {\mathrm{d}}\right) - \frac {k _ {2}}{\varepsilon^ {2}} x _ {2} - \frac {k _ {3}}{\varepsilon} x _ {3}$$

微分器的输出 $x_{1}$ 和 $x_{2}$ 即为 $\dot{\theta}_{\mathrm{d}}$ 和 $\ddot{\theta}_{\mathrm{d}}$ 。为了抑制微分器中的峰值现象，在初始时刻 $0\leqslant t\leqslant 1.0$ 时，取

$$\varepsilon = \frac {1}{1 0 0} \left(1 - \mathrm{e} ^ {- 2 t}\right)$$

![](image/8719a8b1f447d2620da55b4b8333d6a263fa5ffa80376b084a40553e11407ddc.jpg)
