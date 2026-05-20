# (3) 振荡环节和二阶微分环节

振荡环节的传递函数为

$$G (s) = \frac {1}{(s / \omega_ {n}) ^ {2} + 2 \zeta (s / \omega_ {n}) + 1}; \quad \omega_ {n} > 0, \quad 0 < \zeta < 1 \tag {5-32}$$

振荡环节的频率特性

$$
A (\omega) = \frac {1}\sqrt {\left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) ^ {2} + 4 \zeta^ {2} \frac {\omega^ {2}}{\omega_ {n} ^ {2}}} \tag {5-33}
\varphi (\omega) = - \arctan \left(\frac {2 \zeta \frac {\omega}{\omega_ {n}}}{1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}}\right) = \left\{ \begin{array}{l l} - \arctan \frac {2 \zeta \frac {\omega}{\omega_ {n}}}{1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}}, & \omega \leqslant \omega_ {n} \\ - \left(1 8 0 ^ {\circ} - \arctan \frac {2 \zeta \frac {\omega}{\omega_ {n}}}{\frac {\omega^ {2}}{\omega_ {n} ^ {2}} - 1}\right), & \omega > \omega_ {n} \end{array} \right. \tag {5-34}
$$

显然， $\varphi(0)=0^{\circ}, \varphi(\infty)=-180^{\circ}$ ，故相频特性曲线从 $0^{\circ}$ 单调减至 $-180^{\circ}$ 。当 $\omega=\omega_{n}$ 时， $\varphi(\omega_{n})=-90^{\circ}$ ，由式(5-33)得 $A(\omega_{n})=\frac{1}{2\zeta}$ ，表明振荡环节与虚轴的交点为 $-j\frac{1}{2\zeta}$ 。

由式(5-33)可得 $A(0) = 1, A(\infty) = 0$ 。为分析 $A(\omega)$ 的变化，求 $A(\omega)$ 的极值，即令

$$\frac {\mathrm{d} A (\omega)}{\mathrm{d} \omega} = \frac {- \left[ - \frac {2 \omega}{\omega_ {n} ^ {2}} \left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) + 4 \zeta^ {2} \frac {\omega}{\omega_ {n} ^ {2}} \right]}{\left[ \left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) ^ {2} + 4 \zeta^ {2} \frac {\omega^ {2}}{\omega_ {n} ^ {2}} \right] ^ {\frac {3}{2}}} = 0 \tag {5-35}$$

得谐振频率

$$\omega_ {r} = \omega_ {n} \sqrt {1 - 2 \zeta^ {2}}, \quad 0 < \zeta \leqslant \sqrt {2} / 2 \tag {5-36}$$

将 $\omega_{r}$ 代入式(5-33)，求得谐振峰值

$$M _ {r} = A (\omega_ {r}) = \frac {1}{2 \zeta \sqrt {1 - \zeta^ {2}}}, \quad 0 < \zeta \leqslant \sqrt {2} / 2 \tag {5-37}$$

因为 $\zeta = \frac{\sqrt{2}}{2}$ 时 $M_r = 1$ ，当 $0 < \zeta < \sqrt{2} / 2$ 时

$$\frac {\mathrm{d} M _ {r}}{\mathrm{d} \zeta} = \frac {- (1 - 2 \zeta^ {2})}{\zeta^ {2} (1 - \zeta^ {2}) ^ {\frac {3}{2}}} < 0 \tag {5-38}$$

可见 $\omega_r, M_r$ 均为阻尼比 $\zeta$ 的减函数 $(0 < \zeta \leqslant \sqrt{2} / 2)$ 。当 $0 < \zeta < \frac{\sqrt{2}}{2}$ ，且 $\omega \in (0, \omega_r)$ 时， $A(\omega)$ 单调增； $\omega \in (\omega_r, \infty)$ 时， $A(\omega)$ 单调减。而当 $\frac{\sqrt{2}}{2} < \zeta < 1$ 时， $A(\omega)$ 单调减。不同阻尼比 $\zeta$ 情况下，振荡环节的幅相曲线和对数频率特性曲线分别如图5-12和图5-13所示，其中 $u = \frac{\omega}{\omega_n}$ 。
