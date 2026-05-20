# (1) 系统闭环和开环频域指标的关系

系统开环指标截止频率 $\omega_{c}$ 与闭环指标带宽频率 $\omega_{b}$ 有着密切的关系。如果两个系统的稳定程度相仿，则 $\omega_{c}$ 大的系统， $\omega_{b}$ 也大； $\omega_{c}$ 小的系统， $\omega_{b}$ 也小。因此 $\omega_{c}$ 和系统响应速度存在正比关系， $\omega_{c}$ 可用来衡量系统的响应速度。鉴于闭环振荡性指标谐振峰值 $M_{r}$ 和开环指标相角裕度 $\gamma$ 都能表征系统的稳定程度，故下面建立 $M_{r}$ 和 $\gamma$ 的近似关系：

设系统开环相频特性可以表示为

$$\varphi (\omega) = - 1 8 0 ^ {\circ} + \gamma (\omega) \tag {5-100}$$

其中 $\gamma(\omega)$ 表示相角相对于 $-180^{\circ}$ 的相移。因此开环频率特性可以表示为

$$G (\mathrm{j} \omega) = A (\omega) \mathrm{e} ^ {- \mathrm{j} [ 1 8 0 ^ {\circ} - \gamma (\omega) ]} = A (\omega) [ - \cos \gamma (\omega) - \mathrm{j} \sin \gamma (\omega) ] \tag {5-101}$$

闭环幅频特性

$$
\begin{array}{l} M (\omega) = \left| \frac {G (\mathrm{j} \omega)}{1 + G (\mathrm{j} \omega)} \right| = \frac {A (\omega)}{\left[ 1 + A ^ {2} (\omega) - 2 A (\omega) \cos \gamma (\omega) \right] ^ {\frac {1}{2}}} \\ = \frac {1}{\sqrt {\left[ \frac {1}{A (\omega)} - \cos \gamma (\omega) \right] ^ {2} + \sin^ {2} \gamma (\omega)}} \tag {5-102} \\ \end{array}
$$

一般情况下，在 $M(\omega)$ 的极大值附近， $\gamma(\omega)$ 变化较小，且使 $M(\omega)$ 为极值的谐振频率 $\omega_r$ 常位于 $\omega_c$ 附近，即有

$$\cos \gamma (\omega_ {r}) \approx \cos \gamma (\omega_ {c}) = \cos \gamma \tag {5-103}$$

由式(5-102)可知，令 $\frac{\mathrm{d}M(\omega)}{\mathrm{d}A(\omega)} = 0$ ，得 $A(\omega) = \frac{1}{\cos\gamma(\omega)}$ ，相应的 $M(\omega)$ 为极值，故谐振峰值为

$$M _ {r} = M \left(\omega_ {r}\right) = \frac {1}{\left| \sin \gamma \left(\omega_ {r}\right) \right|} \approx \frac {1}{\left| \sin \gamma \right|} \tag {5-104}$$

由于 $\cos \gamma (\omega_r)\leqslant 1$ ，故在闭环幅频特性的峰值处对应的开环幅值 $A(\omega_r)\geqslant 1$ ，而 $A(\omega_c) = 1$ ，显然 $\omega_{r}\leqslant \omega_{c}$ 。因此随着相角裕度 $\gamma$ 的减小， $\omega_{c} - \omega_{r}$ 减小，当 $\gamma = 0$ 时， $\omega_{r} = \omega_{c}$ 。由此可知， $\gamma$ 较小时，式(5-104)的近似程度较高。控制系统的设计中，一般先根据控制要求提出闭环频域指标 $\omega_{b}$ 和 $M_r$ ，再由式(5-104)确定相角裕度 $\gamma$ 和选择合适的截止频率 $\omega_{c}$ ，然后根据 $\gamma$ 和 $\omega_{c}$ 选择校正网络的结构并确定参数。
