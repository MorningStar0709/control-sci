# (2) 开环频域指标和时域指标的关系

对于典型二阶系统，第三章已建立了时域指标超调量 $\sigma \%$ 和调节时间 $t_s$ 与阻尼比 $\zeta$ 的关系式。而欲确定 $\gamma$ 和 $\omega_{c}$ 与 $\sigma \%$ 和 $t_s$ 的关系，只需确定 $\gamma$ 和 $\omega_{c}$ 关于 $\zeta$ 的计算公式。因为典型二阶系统的开环频率特性为

$$G (\mathrm{j} \omega) = \frac {\omega_ {n} ^ {2}}{\mathrm{j} \omega (\mathrm{j} \omega + 2 \zeta \omega_ {n})} = \frac {\omega_ {n} ^ {2}}{\omega \sqrt {\omega^ {2} + 4 \zeta^ {2} \omega_ {n} ^ {2}}} \left\lfloor - 9 0 ^ {\circ} - \arctan \frac {\omega}{2 \zeta \omega_ {n}} \right.$$

由 $\omega_{c}$ 定义及式(5-85)求得

$$\frac {\omega_ {c}}{\omega_ {n}} = \left(\sqrt {4 \zeta^ {4} + 1} - 2 \zeta^ {2}\right) ^ {\frac {1}{2}} \tag {5-105}$$

由式(5-86)求出相角裕度

$$
\begin{array}{l} \gamma = 1 8 0 ^ {\circ} + \underline {{{G (\mathrm{j} \omega_ {c})}}} = 1 8 0 ^ {\circ} - 9 0 ^ {\circ} - \arctan \frac {\omega_ {c}}{2 \zeta \omega_ {n}} \\ = \arctan \frac {2 \zeta \omega_ {n}}{\omega_ {c}} = \arctan \left[ 2 \zeta \left(\sqrt {4 \zeta^ {4} + 1} - 2 \zeta^ {2}\right) ^ {- \frac {1}{2}} \right] \tag {5-106} \\ \end{array}
$$

上式表明,典型二阶系统的相角裕度 $\gamma$ 与阻尼比 $\zeta$ 存在一一对应关系,图5-47是根据式(5-106)绘制的 $\gamma \zeta$ 曲线。由图5-47可知, $\gamma$ 为 $\zeta$ 的增函数。

当选定 $\gamma$ 后，可由 $\gamma -\zeta$ 曲线确定 $\zeta$ ，再由 $\zeta$ 确定 $\sigma \%$ 和 $t_{s}$ 。

例5-16 设一单位反馈系统的开环传递函数

$$G (s) = \frac {K}{s (T s + 1)}$$

若已知单位速度信号输入下的稳态误差 $e_{s}(\infty) = \frac{1}{9}$ ，相角裕度 $\gamma = 60^{\circ}$ ，试确定系统时域指标 $\sigma \%$ 和 $t_s$ 。

解 因为该系统为 I 型系统, 单位速度输入下的稳态误差为 $\frac{1}{K}$ , 由题设条件得 K=9 。由 $\gamma=60^{\circ}$ , 查图 5-47 得阻尼比 $\zeta=0.62$ , 因此超调量

$$\sigma \% = \mathrm{e} ^ {- \pi \zeta / \sqrt {1 - \zeta^ {2}}} \times 100 \% = 7.5 \%$$

由于 $K / T = \omega_{n}^{2},\quad 1 / T = 2\zeta \omega_{n}$

$$\omega_ {n} = 2 K \zeta = 1 1. 1 6$$

调节时间

![](image/7b4e8d4a67d70043c5d8a10fc4f36db4bb2e2170a54ec1c0cc2059968e178d06.jpg)

<details>
<summary>line</summary>

| γ | ξ |
| --- | --- |
| 0° | 0.0 |
| 10° | 0.1 |
| 20° | 0.2 |
| 30° | 0.3 |
| 40° | 0.4 |
| 50° | 0.5 |
| 60° | 0.6 |
| 70° | 0.7 |
| γ | 0.9 |
</details>

图 5-47 典型二阶系统的 $\gamma-\zeta$ 曲线

$$t _ {s} = \frac {3 . 5}{\zeta \omega_ {n}} = 0. 5 0 6 (\Delta = 5 \%)$$

如果采用 MATLAB 仿真方法, 可得系统的时域指标为

$$\sigma \% = 8.29 \%, \quad t _ {s} = 0.47 (\Delta = 5 \%)$$

表明对于典型的无零点二阶系统，时域指标的估算结果是较准确的。
