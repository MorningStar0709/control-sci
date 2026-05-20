# 9.5.2 典型系统的频率响应

本节将讨论典型系统的频率响应及其伯德图,在掌握这些典型系统的频率响应后,可以将它们串联组合以分析复杂的系统。

例 9.5.1 积分器, $G(s)=\frac{1}{s}$ 。

参考9.2节末尾处对积分频率响应的计算，其中： $|G(\mathrm{j}\omega_{\mathrm{i}})| = \frac{1}{\omega_{\mathrm{i}}},\angle G(\mathrm{j}\omega_{\mathrm{i}}) = -\frac{\pi}{2} =$ $-90^{\circ}$ 。可得

$$
2 0 \log | G (\mathrm{j} \omega_ {\mathrm{i}}) | = 2 0 \log \frac {1}{\omega_ {\mathrm{i}}} = - 2 0 \log \omega_ {\mathrm{i}} \mathrm{dB} \tag {9.5.7}
$$

式(9.5.7)说明其幅频图的斜率为-20dB/dec,其中dec代表十倍(decade)。输入频率 $\omega_{i}$ 每增加十倍,伯德图中幅频曲线就会下降20dB。当输入频率 $\omega_{i}=1$ 时, $20\log|G(j\omega_{i})|=0dB$ 。同时,它的相位 $\angle G(j\omega_{i})$ 始终为 $-90^{\circ}$ 。其伯德图如图9.5.3所示,它说明当输入频率 $\omega_{i}<1$ 时, $20\log|G(j\omega_{i})|>0$ ,即 $|G(j\omega_{i})|>1$ ,所以 $M_{o}=|G(j\omega_{i})|M_{i}>M_{i}$ ,输出的振幅大于输入的振幅,同时输入的频率越低,输出的振幅就越大。反之亦然。所以积分器是一个低通滤波器。从能量的角度考虑,当输入频率较低时,输出振幅的增加需要额外的能量来源。所以积分器无法通过被动元器件实现,需要额外供能。

![](image/e6b88903b6228dc18caf77f276a49bffc4dbdfe17c154dafa37c4fb5e03e657c.jpg)  
图9.5.3 $G(s) = \frac{1}{s}$ 的伯德图

例 9.5.2 一阶系统, $G(s)=\frac{1}{\frac{1}{a}s+1}$ ,其中 a>0。

参考式(9.3.2)，得到其频率响应，其中： $|G(j\omega_{i})|=\sqrt{\frac{1}{\left(\frac{\omega_{i}}{a}\right)^{2}+1}}$ ， $\angle G(j\omega_{i})=-\arctan\frac{\omega_{i}}{a}$ 。
可得：

(1) 当 $\omega_{\mathrm{i}} = 0$ 时， $|G(\mathrm{j}0)| = \sqrt{\frac{1}{\left(\frac{0}{a}\right)^2 + 1}} = 1 \Rightarrow 20 \log |G(\mathrm{j} \omega_{\mathrm{i}})| = 0 \mathrm{~dB}, \angle G(\mathrm{j} \omega_{\mathrm{i}}) = 0^\circ$ 。  
(2) 在截止频率 $\omega_{\mathrm{i}} = a$ 时， $|G(\mathrm{j}\omega_{\mathrm{i}})| = \sqrt{\frac{1}{1 + 1}} = 0.707 \Rightarrow 20\log |G(\mathrm{j}\omega_{\mathrm{i}})| = -3\mathrm{dB}, \angle G(\mathrm{j}\omega_{\mathrm{i}}) = -45^{\circ}$ 。  
(3) 当 $\omega_{\mathrm{i}} \gg a$ 时, $|G(\mathrm{j}\omega_{\mathrm{i}})| = \frac{1}{\omega_{\mathrm{i}}} \Rightarrow 20\log |G(\mathrm{j}\omega_{\mathrm{i}})| = -20\log \omega_{\mathrm{i}}\mathrm{dB}, \angle G(\mathrm{j}\omega_{\mathrm{i}}) = -90^{\circ}$ , 这说明一阶系统在高频区域的频率响应与积分系统一样, 幅频图的斜率都是 $-20\mathrm{dB / dec}$ , 相频图是 $-90^{\circ}$ 。

根据上述三点,得出一阶系统伯德图的渐近线,如图9.5.4所示。其幅频响应由两条渐近线组成,在低频段是从0开始的一条直线,在高频段则是斜率为-20dB/dec的直线。同时,幅频响应会经过(a,-3dB)点。相频图也是两条渐近线,分别是0°和-90°。同时,相频图经过(a,-45°)点。其伯德图曲线如图9.5.4所示(此图假设1<a<10)。
