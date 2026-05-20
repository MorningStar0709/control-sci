# 5.3.3 干扰观测器鲁棒稳定性

设 $G_{\mathrm{p}}(s)$ 的名义模型为 $G_{\mathrm{n}}(s)$ ，则不确定对象的集合可以用乘积摄动来描述，即

$$G _ {\mathrm{p}} (s) = G _ {\mathrm{n}} (s) (1 + \Delta (s)) \tag {5.23}$$

式中， $\Delta(s)$ 表明了实际对象频率特性对名义模型的摄动，通常情况下，频率增加时，对象的不确定性也增大，因此 $\left|\Delta(j\omega)\right|$ 表现为 $\omega$ 的增函数。

由图 5-12 可得

$$
\begin{array}{l} \Delta G _ {\mathrm{uy}} (s) = \frac {\left(G _ {\mathrm{p}} (s) + \Delta G _ {\mathrm{p}} (s)\right) G _ {\mathrm{n}} (s)}{G _ {\mathrm{n}} (s) + \left[ G _ {\mathrm{p}} (s) + \Delta G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) \right] Q (s)} - \frac {G _ {\mathrm{p}} (s) G _ {\mathrm{n}} (s)}{G _ {\mathrm{n}} (s) + \left[ G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) \right] Q (s)} \\ = \frac {G _ {\mathrm{n}} (s) \Delta G _ {\mathrm{p}} (s) G _ {\mathrm{n}} (s) (1 - Q (s))}{\left\{G _ {\mathrm{n}} (s) + \left[ G _ {\mathrm{p}} (s) + \Delta G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) \right] Q (s) \right\} \left\{G _ {\mathrm{n}} (s) + \left[ G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) \right] Q (s) \right\}} \\ \end{array}
$$

则

$$\frac {\Delta G _ {\mathrm{uy}} (s)}{G _ {\mathrm{uy}} (s)} = \frac {G _ {\mathrm{n}} (s) \Delta G _ {\mathrm{p}} (s) G _ {\mathrm{n}} (s) (1 - Q (s))}{\left\{G _ {\mathrm{n}} (s) + \left[ G _ {\mathrm{p}} (s) + \Delta G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) \right] Q (s) \right\} \left\{G _ {\mathrm{n}} (s) + \left[ G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) \right] Q (s) \right\}}\times \frac {G _ {\mathrm{n}} (s) + \left[ G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) \right] Q (s)}{G _ {\mathrm{p}} (s) G _ {\mathrm{n}} (s)} = \frac {\Delta G _ {\mathrm{p}} (s) G _ {\mathrm{n}} (s) (1 - Q (s))}{\left\{G _ {\mathrm{n}} (s) + \left[ G _ {\mathrm{p}} (s) + \Delta G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) \right] Q (s) \right\} G _ {\mathrm{p}} (s)}$$

则

$$\frac {\Delta G _ {\mathrm{uy}} (s) / G _ {\mathrm{uy}} (s)}{\Delta G _ {\mathrm{p}} (s) / G _ {\mathrm{p}} (s)} = \frac {\Delta G _ {\mathrm{p}} (s) G _ {\mathrm{n}} (s) (1 - Q (s))}{\left\{G _ {\mathrm{n}} (s) + \left[ G _ {\mathrm{p}} (s) + \Delta G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) \right] Q (s) \right\} G _ {\mathrm{p}} (s)} \cdot \frac {G _ {\mathrm{p}} (s)}{\Delta G _ {\mathrm{p}} (s)}= \frac {G _ {\mathrm{n}} (s) (1 - Q (s))}{G _ {\mathrm{n}} (s) + [ G _ {\mathrm{p}} (s) + \Delta G _ {\mathrm{p}} (s) - G _ {\mathrm{n}} (s) ] Q (s)}$$

则灵敏度函数 $S(s)$ 为
