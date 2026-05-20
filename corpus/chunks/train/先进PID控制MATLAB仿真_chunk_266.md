# 5.2.4 PID 控制器的设计及分析

采用观测器式（5.13）观测干扰 d，在 PID 控制中对干扰进行补偿，可实现高精度跟踪。

取控制目标为 $\theta \rightarrow \theta_{d}$ ， $\dot{\theta} \rightarrow \dot{\theta}_{d}$ ，取跟踪误差为 $e = \theta_{d} - \theta$ ，设计基于前馈和干扰估计补偿的 PD 控制律为

$$u (t) = k _ {\mathrm{p}} e + k _ {\mathrm{d}} \dot {e} + J \ddot {\theta} _ {\mathrm{d}} + b \dot {\theta} _ {\mathrm{d}} - \hat {d} \tag {5.14}$$

式中， $k_{p}>0$ ; $k_{d}>0$ 。

收敛性分析如下：将控制律代入模型式（5.8）中，可得

$$J \ddot {\theta} + b \dot {\theta} = k _ {\mathrm{p}} e + k _ {\mathrm{d}} \dot {e} + J \ddot {\theta} _ {\mathrm{d}} + b \dot {\theta} _ {\mathrm{d}} - \hat {d} + d$$

即

$$k _ {\mathrm{p}} e + \left(k _ {\mathrm{d}} + b\right) \dot {e} + J \ddot {e} + \tilde {d} = 0$$

由于 $\tilde{d}(t)$ 指数收敛，收敛精度取决于 K 值，则通过设计 $k_{p}$ 和 $k_{d}$ ，可实现跟踪误差 e 及变化率 $\dot{e}$ 指数收敛，收敛精度取决于观测器参数 K 及参数 $k_{p}$ 和 $k_{d}$ 的值。

![](image/4e025f849a56bea6e3fa3d3295a4bf65e9dd4416cb09bf7ec7e04ba9e5df2862.jpg)
