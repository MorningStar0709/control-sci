# 7.1.2 PD 控制律的设计

定义 Lyapunov 函数为

$$V = \frac {1}{2} J \dot {e} ^ {2} + \frac {1}{2} K _ {\mathrm{p}} e ^ {2} \tag {7.2}$$

式中， $K_{\mathrm{p}} > 0$ ，则

$$\dot {V} = J \ddot {e} \ddot {e} + K _ {\mathrm{p}} e \dot {e} = \dot {e} (J \ddot {e} + K _ {\mathrm{p}} e) = \dot {e} (u - C \dot {e} + K _ {\mathrm{p}} e)$$

控制律设计为

$$u = - K _ {\mathrm{p}} e - K _ {\mathrm{d}} \dot {e} \tag {7.3}$$

式中， $K_{d}>0$ ，则闭环系统为

$$J \ddot {e} + C \dot {e} = - K _ {\mathrm{p}} e - K _ {\mathrm{d}} \dot {e} \tag {7.4}$$

从而

$$\dot {V} = \dot {e} \left(- K _ {\mathrm{p}} e - K _ {\mathrm{d}} \dot {e} - C \dot {e} + K _ {\mathrm{p}} e\right) = - \left(K _ {\mathrm{d}} + C\right) \dot {e} ^ {2} \leqslant 0$$

当且仅当 $\dot{e} = 0$ 时， $\dot{V} = 0$ 。即当 $\dot{V} \equiv 0$ 时， $\dot{e} \equiv 0$ ，从而 $\ddot{e} \equiv 0$ ，代入式（7.4），可得 $e \equiv 0$ 。根据LaSalle不变性原理[1]，闭环系统为渐进稳定，当 $t \to \infty$ 时， $e \to 0$ ， $\dot{e} \to 0$ 。系统的收敛速度取决于 $K_{\mathrm{d}}$ 。

![](image/165902a295bdfa3709b9e1f2620bc61169633092a5d349bfc9b5987aa84431e2.jpg)
