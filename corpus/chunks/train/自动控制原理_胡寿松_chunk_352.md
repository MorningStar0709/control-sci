首先, 考虑采用串联超前校正。要把待校正系统的相角裕度从 $-55.5^{\circ}$ 提高到 $45^{\circ}$ , 至少选用两级串联超前网络。显然, 校正后系统的截止频率将过大, 可能超过 $25\mathrm{rad/s}$ 。从理论上说, 截止频率越大, 则系统的响应速度越快。譬如说, 在 $\omega_{c}^{\prime \prime}=25\mathrm{rad/s}$ 时, 系统动态过程的调节时间近似为 $0.34\mathrm{s}$ , 这将比性能指标要求提高近 10 倍, 然而进一步分析发现: ① 伺服电机将出现速度饱和, 这是因为超前校正系统要求伺服机构输出的变化速率超过了伺服电机的最大输出转速之故, 于是, $0.34\mathrm{s}$ 的调节时间将变得毫无意义; ② 系统带宽过大, 造成输出噪声电平过高; ③ 需要附加前置放大器, 使系统结构复杂化。

其次，若采用串联滞后校正，可以使系统的相角裕度提高到 $45^{\circ}$ 左右，但是对于本例高性能系统，会产生两个很严重的缺点：①滞后网络时间常数太大，这是因为静态速度误差系数越大，所需要的滞后网络时间常数越大之故。对于本例，要求选 $\omega_{c}^{\prime \prime} = 1$ ，相应的 $L^{\prime}(\omega_{c}^{\prime \prime}) = 45.1\mathrm{dB}$ ，根据式(6-41)求出 $b = 1 / 200$ ，若取 $1 / bT = 0.1\omega_c^{\prime \prime}$ ，可得 $T = 2000s$ ，这样大的时间常数，实际上是无法实现的；②响应速度指标不满足，由于滞后校正极大地减小了系统的截止频率，使得系统响应滞缓。对于本例，粗略估算的调节时间约为9.6s，该值远大于性能指标的要求值。

上述论证表明，纯超前校正及纯滞后校正都不宜采用，应当选用串联滞后-超前校正。

为了利用滞后-超前网络的超前部分微分段的特性,研究图 6-23 发现,可取 $\omega_{b}=2rad/s$ ,于是待校正系统对数幅频特性在 $\omega\leqslant6rad/s$ 区间,其斜率均为 -20dB/dec。

根据 $t_s \leqslant 3s$ 和 $\gamma'' = 45^\circ$ 的指标要求，不难算得 $\omega_c'' \geqslant 3.2\mathrm{rad/s}$ 。考虑到要求中频区斜率为 $-20\mathrm{dB/dec}$ ，故 $\omega_c''$ 应在 $3.2 \sim 6\mathrm{rad/s}$ 范围内选取。由于 $-20\mathrm{dB/dec}$ 的中频区应占据一定宽度，故选 $\omega_c'' = 3.5\mathrm{rad/s}$ ，相应的 $L'(\omega_c'') + 20\lg T_b\omega_c'' = 34\mathrm{dB}$ 。由式(6-43)可算出 $1/\alpha = 0.02$ ，此时，滞

后-超前校正网络的频率特性可写为

$$G _ {c} (\mathrm{j} \omega) = \frac {(1 + \mathrm{j} \omega / \omega_ {a}) (1 + \mathrm{j} \omega / \omega_ {b})}{(1 + \mathrm{j} \alpha \omega / \omega_ {a}) (1 + \mathrm{j} \omega / \alpha \omega_ {b})} = \frac {(1 + \mathrm{j} \omega / \omega_ {a}) (1 + \mathrm{j} \omega / 2)}{(1 + \mathrm{j} 5 0 \omega / \omega_ {a}) (1 + \mathrm{j} \omega / 1 0 0)}$$

相应的已校正系统的频率特性为

$$G _ {c} (\mathrm{j} \omega) G _ {0} (\mathrm{j} \omega) = \frac {1 8 0 (1 + \mathrm{j} \omega / \omega_ {a})}{\mathrm{j} \omega (1 + \mathrm{j} \omega / 6) (1 + \mathrm{j} 5 0 \omega / \omega_ {a}) (1 + \mathrm{j} \omega / 1 0 0)}$$

根据上式,利用相角裕度指标要求,可以确定校正网络参数 $\omega_{a}$ 。已校正系统的相角裕度
