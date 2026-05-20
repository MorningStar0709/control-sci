# 7.2.3 稳定性分析

Lyapunov 函数取为

$$V = \frac {1}{2} J s ^ {2} + \frac {1}{2} k _ {\mathrm{i}} \left(\int_ {0} ^ {t} s \mathrm{d} \tau\right) ^ {2}$$

则

$$\dot {V} = s \left(J \dot {s} + k _ {i} \int_ {0} ^ {t} s \mathrm{d} \tau\right)$$

将式（7.8）代入上式，得

$$\dot {V} = s \left(- C s - k _ {\mathrm{p}} s - k _ {\mathrm{r}} \operatorname{sign} (s) + d\right) = - C s ^ {2} - k _ {\mathrm{p}} s ^ {2} - k _ {\mathrm{r}} | s | + d s \leqslant 0$$

当 $\dot{V} \equiv 0$ 时， $s \equiv 0$ ，根据 LaSalle 不变性原理，闭环系统为渐进稳定，即当 $t \to \infty$ 时， $e \to 0$ ， $\dot{e} \to 0$ ，系统的收敛速度取决于 $k_{p}$ 。

![](image/0a08b59e59919602781a87b7a22deae82bbc3af9b64f752f619cb99c23e1e401.jpg)
