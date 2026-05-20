jω
ωₙ=ωₙ√(1-ζ²)
-ζωₙ O σ
-ωₙ
-ωₐ
</details>

图 5.3.1 极点、固有频率与阻尼固有频率的关系

此时，式(5.3.9)可以化简为

$$
\begin{array}{l} x (t) = 1 - \mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} t} \left[ \frac {1}{2} \left(1 - \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \mathrm{e} ^ {\omega_ {\mathrm{d}} \mathrm{j} t} + \frac {1}{2} \left(1 + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \mathrm{e} ^ {- \omega_ {\mathrm{d}} \mathrm{j} t} \right] \\ = 1 - \mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} t} \left[ \frac {1}{2} \left(\mathrm{e} ^ {\omega_ {\mathrm{d}} \mathrm{j} t} + \mathrm{e} ^ {- \omega_ {\mathrm{d}} \mathrm{j} t}\right) + \frac {1}{2} \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j} \left(- \mathrm{e} ^ {\omega_ {\mathrm{d}} \mathrm{j} t} + \mathrm{e} ^ {- \omega_ {\mathrm{d}} \mathrm{j} t}\right) \right] \tag {5.3.10a} \\ \end{array}
$$

根据欧拉公式， $\mathrm{e}^{\omega_{\mathrm{d}}\mathrm{j}t} = \cos \omega_{\mathrm{d}}t + \mathrm{j}\sin \omega_{\mathrm{d}}t,\mathrm{e}^{-\omega_{\mathrm{d}}\mathrm{j}t} = \cos \omega_{\mathrm{d}}t - \mathrm{j}\sin \omega_{\mathrm{d}}t$ 。可得

$$\frac {1}{2} \left(\mathrm{e} ^ {\omega_ {\mathrm{d}} \mathrm{j} t} + \mathrm{e} ^ {- \omega_ {\mathrm{d}} \mathrm{j} t}\right) = \cos \omega_ {\mathrm{d}} t \tag {5.3.10b}\frac {1}{2} \mathrm{j} \left(- \mathrm{e} ^ {\omega_ {\mathrm{d}} \mathrm{j} t} + \mathrm{e} ^ {- \omega_ {\mathrm{d}} \mathrm{j} t}\right) = \sin \omega_ {\mathrm{d}} t \tag {5.3.10c}$$

代入式(5.3.10a)，化简后得到

$$x (t) = 1 - \mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} t} \left[ \cos \omega_ {\mathrm{d}} t + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {\mathrm{d}} t \right] \tag {5.3.11a}$$

令 $\varphi=\arctan\frac{\sqrt{1-\zeta^{2}}}{\zeta}$ ，可得

$$
\begin{array}{l} \cos \omega_ {\mathrm{d}} t + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {\mathrm{d}} t = \sqrt {1 ^ {2} + \left(\frac {\zeta}{\sqrt {1 - \zeta^ {2}}}\right) ^ {2}} \sin (\omega_ {\mathrm{d}} t + \varphi) \\ = \sqrt {\frac {1}{1 - \zeta^ {2}}} \sin \left(\omega_ {\mathrm{d}} t + \varphi\right) \tag {5.3.11b} \\ \end{array}
$$

代入式(5.3.11a)，可得

$$x (t) = 1 - \mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} t} \sqrt {\frac {1}{1 - \zeta^ {2}}} \sin (\omega_ {\mathrm{d}} t + \varphi) \tag {5.3.12}$$
