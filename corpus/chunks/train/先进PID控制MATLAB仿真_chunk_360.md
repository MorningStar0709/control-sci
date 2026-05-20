# 7.3.3 稳定性分析

Lyapunov 函数取为

$$V = \frac {1}{2} \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {D} \boldsymbol {r} + \frac {1}{2} \left(\int_ {0} ^ {t} \boldsymbol {r} \mathrm{d} \tau\right) ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{i}} \left(\int_ {0} ^ {t} \boldsymbol {r} \mathrm{d} \tau\right) \tag {7.17}$$

则

$$\dot {V} = \boldsymbol {r} ^ {\mathrm{T}} \left[ \boldsymbol {D} \dot {\boldsymbol {r}} + \frac {1}{2} \dot {\boldsymbol {D}} \boldsymbol {r} + \boldsymbol {K} _ {\mathrm{i}} \int_ {0} ^ {t} \boldsymbol {r} \mathrm{d} \tau \right]$$

考虑到 $\dot{D}(q)-2C(q,\dot{q})$ 的斜对称特性，有

$$\dot {V} = \boldsymbol {r} ^ {\mathrm{T}} \left[ \boldsymbol {D} \dot {\boldsymbol {r}} + \boldsymbol {C r} + \boldsymbol {K} _ {\mathrm{i}} \int_ {0} ^ {t} \boldsymbol {r} \mathrm{d} \tau \right]$$

将式（7.16）代入上式，得

$$\dot {V} = - \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {r} + \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {E} - \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{r}} \operatorname{sgn} (\boldsymbol {r})$$

考虑 $k_{\mathrm{rii}} \geqslant |E_i|$ ，得

$$\dot {V} \leqslant - \boldsymbol {r} ^ {\mathrm{T}} \boldsymbol {K} _ {\mathrm{p}} \boldsymbol {r} \leqslant 0$$

当且仅当 $r = 0$ 时， $\dot{V} = 0$ ，即当 $\dot{V} \equiv 0$ 时， $r \equiv 0$ 。根据 LaSalle 不变性原理[1]，闭环系统为渐进稳定，当 $t \to \infty$ 时， $e \to 0$ ， $\dot{e} \to 0$ 。系统的收敛速度取决于 $K_{\mathrm{p}}$ 。

![](image/a5011bb1dbbe39a23b65a8f03325057b00d554316833809a533715584334d121.jpg)
