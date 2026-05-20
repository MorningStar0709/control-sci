$$
\begin{array}{l} \gamma^ {\prime \prime} = 1 8 0 ^ {\circ} + \arctan \frac {\omega_ {c} ^ {\prime \prime}}{\omega_ {a}} - 9 0 ^ {\circ} - \arctan \frac {\omega_ {c} ^ {\prime \prime}}{6} - \arctan \frac {5 0 \omega_ {c} ^ {\prime \prime}}{\omega_ {a}} - \arctan \frac {\omega_ {c} ^ {\prime \prime}}{1 0 0} \\ = 5 7. 7 ^ {\circ} + \arctan \frac {3 . 5}{\omega_ {a}} - \arctan \frac {1 7 5}{\omega_ {a}} \\ \end{array}
$$

考虑到 $\omega_{a} < \omega_{b} = 2\mathrm{rad / s}$ , 故可取 $-\arctan (175 / \omega_{a}) \approx -90^{\circ}$ 。因为要求 $\gamma'' = 45^{\circ}$ , 所以上式可简化为

$$\arctan (3. 5 / \omega_ {a}) = 7 7. 3 ^ {\circ}$$

从而求得 $\omega_{a}=0.78rad/s$ 。这样，已校正系统-20dB/dec 斜率的中频区宽度 H=6/0.78=7.69，满足在期望特性校正法中导出的中频区宽度近似关系式

$$H \geqslant \frac {1 + \sin \gamma^ {\prime \prime}}{1 - \sin \gamma^ {\prime \prime}} = \frac {1 + \sin 4 5 ^ {\circ}}{1 - \sin 4 5 ^ {\circ}} = 5. 8 3$$

于是，校正网络和已校正系统的传递函数分别为

$$G _ {c} (s) = \frac {(1 + 1 . 2 8 s) (1 + 0 . 5 s)}{(1 + 6 4 s) (1 + 0 . 0 1 s)}G _ {c} (s) G _ {0} (s) = \frac {1 8 0 (1 + 1 . 2 8 s)}{s (1 + 0 . 1 6 7 s) (1 + 6 4 s) (1 + 0 . 0 1 s)}$$

其对数幅频特性 $L_{c}(\omega)$ 和 $L''(\omega)$ 已分别表示在图6-23之中。

最后，用计算的方法验算已校正系统的相角裕度和幅值裕度指标，求得 $\gamma'' = 45.5^{\circ}$ ， $h''(\mathrm{dB}) = 27\mathrm{dB}$ ，完全满足指标要求。
