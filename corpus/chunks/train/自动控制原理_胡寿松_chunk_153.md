式中 $\beta_{d} = \arctan (\sqrt{1 - \zeta_{d}^{2}} / \zeta_{d})$ (3-46)

超调量 将式(3-45)代入式(3-42)，得

$$c (t _ {p}) = 1 + r \exp \left[ \frac {- \zeta_ {d}}{\sqrt {1 - \zeta_ {d} ^ {2}}} (\beta_ {d} - \psi) \right] \sin \beta_ {d} = 1 + r e ^ {- \zeta_ {d} \omega_ {n} t _ {p}} \sin \beta_ {d}$$

根据超调量定义，并将 $\sin \beta_{d} = \sqrt{1 - \zeta_{d}^{2}}$ 代入上式，经整理可得

$$\sigma \% = r \sqrt {1 - \zeta_ {d} ^ {2}} \mathrm{e} ^ {- \zeta_ {d} \omega_ {n} t _ {p}} \times 100 \% \tag{3 - 47}$$

调节时间 令 $\Delta$ 表示实际响应与稳态输出之间的误差, 由式(3-42)可见, 下列不等式成立:

$$\Delta = \left| r e ^ {- \zeta_ {d} \omega_ {n} t} \sin (\omega_ {n} \sqrt {1 - \zeta_ {d} ^ {2}} t + \psi) \right| \leqslant r e ^ {- \zeta_ {d} \omega_ {n} t}$$

取 $\Delta = 0.05$ ，由上式可解出

$$t _ {s} = \frac {3 + \frac {1}{2} \ln \left(z ^ {2} - 2 \zeta_ {d} \omega_ {n} z + \omega_ {n} ^ {2}\right) - \ln z - \frac {1}{2} \ln \left(1 - \zeta_ {d} ^ {2}\right)}{\zeta_ {d} \omega_ {n}} = \frac {3 + \ln r}{\zeta_ {d} \omega_ {n}} \tag {3-48}$$

若取 $\Delta = 0.02$ ，则有

$$t _ {s} = (4 + \ln \gamma) / \xi_ {d} \omega_ {n} \tag {3-49}$$

例 3-4 设单位反馈系统开环传递函数为

$$G (s) = \frac {K (T _ {d} s + 1)}{s (1 . 6 7 s + 1)}$$

其中 K 为开环增益。已知系统在单位斜坡函数输入时，稳态误差 $e_{s}(\infty)=1/K$ 。若要求 $e_{s}(\infty)\leqslant0.2\mathrm{rad},\zeta_{d}=0.5$ ，试确定 K 与 $T_{d}$ 的数值，并估算系统在阶跃函数作用下的动态性能。

解 由 $e_{s}(\infty) = 1 / K \leqslant 0.2$ 要求，取 $K = 5$ 。令 $T_{d} = 0$ ，可得无零点二阶系统闭环特征方程

$$s ^ {2} + 0. 6 s + 3 = 0$$

因此得 $\zeta=0.173,\omega_{n}=1.732rad/s$ 。此时，系统的阶跃响应动态性能由式(3-19)～式(3-22)得

$$t _ {r} = 1. 0 2 \mathrm{s}, \quad t _ {p} = 1. 8 4 \mathrm{s}\sigma \% = 57.6 \%, \quad t _ {s} = 11.70 \mathrm{s}$$

当 $T_{d} \neq 0$ 时，由于要求 $\zeta_{d} = 0.5$ ，故由式(3-41)可知

$$T _ {d} = \frac {1}{z} = \frac {2 (\zeta_ {d} - \zeta)}{\omega_ {n}} = 0. 3 8 \mathrm{s}$$

此时为有零点的二阶系统，其阶跃响应动态性能指标，查图3-23得 $t_r = 0.70s$ ，由式(3-45)、式(3-47)及式(3-48)算得 $t_p = 1.63s, \sigma \% = 22\%, t_s = 3.49s$ 。可见，比例-微分控制改善了系统的动态性能，且满足对系统稳态误差的要求。

最后, 简要归纳比例-微分控制对系统性能的影响: 比例-微分控制可以增大系统的阻尼, 使阶跃响应的超调量下降, 调节时间缩短, 且不影响常值稳态误差及系统的自然频率。由于采用微分控制后, 允许选取较高的开环增益, 因而在保证一定的动态性能条件下, 可以减小稳态误差。应当指出, 微分器对于噪声, 特别是对于高频噪声的放大作用, 远大于对缓慢变化输入信号的放大作用, 因此在系统输入端噪声较强的情况下, 不宜采用比例-微分控制方式。此时, 可考虑选用控制工程中常用的测速反馈控制方式。
