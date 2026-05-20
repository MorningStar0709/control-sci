$$\mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} T _ {\mathrm{p}}} \sqrt {\frac {1}{1 - \zeta^ {2}}} (\zeta \omega_ {\mathrm{n}} \sin (\omega_ {\mathrm{d}} T _ {\mathrm{p}} + \varphi) - \omega_ {\mathrm{d}} \cos (\omega_ {\mathrm{d}} T _ {\mathrm{p}} + \varphi)) = 0 \tag {5.4.4b}$$

式(5.4.4b)中的第一项 $\mathrm{e}^{-\zeta \omega_{\mathrm{n}}T_{\mathrm{p}}}\sqrt{\frac{1}{1 - \zeta^2}}\neq 0$ ，所以等式成立时， $\zeta \omega_{\mathrm{n}}\sin (\omega_{\mathrm{d}}T_{\mathrm{p}} + \varphi) -$ $\omega_{\mathrm{d}}\cos (\omega_{\mathrm{d}}T_{\mathrm{p}} + \varphi) = 0$ ，得到

$$\zeta \omega_ {\mathrm{n}} \sin \left(\omega_ {\mathrm{d}} T _ {\mathrm{p}} + \varphi\right) = \omega_ {\mathrm{d}} \cos \left(\omega_ {\mathrm{d}} T _ {\mathrm{p}} + \varphi\right)\Rightarrow \tan (\omega_ {\mathrm{d}} T _ {\mathrm{p}} + \varphi) = \frac {\omega_ {\mathrm{d}}}{\zeta \omega_ {\mathrm{n}}} = \frac {\sqrt {1 - \zeta^ {2}}}{\zeta} \tag {5.4.4c}$$

根据式(5.3.11)的定义, $\frac{\sqrt{1-\zeta^{2}}}{\zeta}=\tan(\varphi)$ ，所以 $\tan(\omega_{\mathrm{d}}T_{\mathrm{p}}+\varphi)=\tan(\varphi)$ ，即

$$\omega_ {\mathrm{d}} T _ {\mathrm{p}} = k \pi \quad k = 1, 2, 3, \dots \tag {5.4.4d}$$

因为最大超调量出现在第一次的峰值,所以 k=1,可得

$$T _ {\mathrm{p}} = \frac {\pi}{\omega_ {\mathrm{d}}} = \frac {\pi}{\omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}}} \tag {5.4.5}$$

对比式(5.4.3)和式(5.4.5)可以发现, $T_{p}$ 与 $T_{r}$ 的性质相同,因为它们都反映了系统的反应速度。将式(5.4.5)代入式(5.4.1)中,可得

$$x \left(T _ {\mathrm{p}}\right) = 1 - \mathrm{e} ^ {\frac {- \zeta \pi}{\sqrt {1 - \zeta^ {2}}}} \sqrt {\frac {1}{1 - \zeta^ {2}}} \sin (\pi + \varphi) = 1 + \mathrm{e} ^ {\frac {- \zeta \pi}{\sqrt {1 - \zeta^ {2}}}} \sqrt {\frac {1}{1 - \zeta^ {2}}} \sin (\varphi) \tag {5.4.6a}$$

因为 $\frac{\sqrt{1 - \zeta^2}}{\zeta} = \tan (\varphi)$ ，所以 $\sin (\varphi) = \sqrt{1 - \zeta^2}$ ，代入式(5.4.6a)，可得

$$x \left(T _ {\mathrm{p}}\right) = 1 + \mathrm{e} ^ {\frac {- \zeta \pi}{\sqrt {1 - \zeta^ {2}}}} \sqrt {\frac {1}{1 - \zeta^ {2}}} \sqrt {1 - \zeta^ {2}} = 1 + \mathrm{e} ^ {\frac {- \zeta \pi}{\sqrt {1 - \zeta^ {2}}}} \tag {5.4.6b}$$

将式(5.4.6b)代入最大超调量的定义中,可得

$$M _ {\mathrm{p}} = \frac {1 + \mathrm{e} ^ {\frac {- \zeta \pi}{\sqrt {1 - \zeta^ {2}}}} - 1}{1} \times 100 \% = \mathrm{e} ^ {\frac {- \zeta \pi}{\sqrt {1 - \zeta^ {2}}}} \times 100 \% \tag{5.4.7}$$

式(5.4.7)说明最大超调量只与阻尼比 $\zeta$ 相关。 $\zeta$ 越大, $M_{\mathrm{p}}$ 就越小。从物理角度来理解, 阻尼比的定义为 $\zeta = \frac{b}{2\sqrt{km}}$ 。当阻尼比越大时, 阻尼 $b$ 在系统中产生的影响相较于弹簧系数 $k$

与质量 m 就越大, 因此系统的“弹性”就会降低, 超调就会减小。在无阻尼状态 $\zeta=0$ 时, 系统的“弹性”最大, $M_{p}=100\%$ , 即最大会超调 1 倍(参考图 5.3.4)。
