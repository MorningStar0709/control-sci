$$X (s) = \frac {1}{\left(s - s _ {\mathrm{p} 1}\right)} - \frac {1}{2} \left(1 - \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \frac {1}{\left(s - s _ {\mathrm{p} 2}\right)} - \frac {1}{2} \left(1 + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \frac {1}{\left(s - s _ {\mathrm{p} 3}\right)} \tag {5.3.7}$$

对式 $(5.3.7)$ 等号两边进行拉普拉斯逆变换,可得

$$
\begin{array}{l} x (t) = \mathcal {L} ^ {- 1} [ X (s) ] \\ = \mathcal {L} ^ {- 1} \left[ \frac {1}{s - s _ {\mathrm{p} 1}} - \frac {1}{2} \left(1 - \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \frac {1}{(s - s _ {\mathrm{p} 2})} - \frac {1}{2} \left(1 + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \frac {1}{(s - s _ {\mathrm{p} 3})} \right] \\ = \mathrm{e} ^ {s _ {\mathrm{p} 1} t} - \frac {1}{2} \left(1 - \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \mathrm{e} ^ {s _ {\mathrm{p} 2} t} - \frac {1}{2} \left(1 + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \mathrm{e} ^ {s _ {\mathrm{p} 3} t} \tag {5.3.8} \\ \end{array}
$$

将式(5.3.3)代入式(5.3.8)，可得

$$
\begin{array}{l} x (t) = \mathrm{e} ^ {0 t} - \frac {1}{2} \left(1 - \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \mathrm{e} ^ {(- \zeta \omega_ {\mathrm{n}} + \omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}} \mathrm{j}) t} - \frac {1}{2} \left(1 + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \mathrm{e} ^ {\left(- \zeta \omega_ {\mathrm{n}} - \omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}} \mathrm{j}\right) t} \\ = 1 - \mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} t} \left[ \frac {1}{2} \left(1 - \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \mathrm{e} ^ {\omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}} \mathrm{j} t} + \frac {1}{2} \left(1 + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \mathrm{j}\right) \mathrm{e} ^ {- \omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}} \mathrm{j} t} \right] \tag {5.3.9} \\ \end{array}
$$

定义一个新的参数 $\omega_{\mathrm{d}} = \omega_{\mathrm{n}}\sqrt{1 - \zeta^{2}}$ ，称其为阻尼固有频率（Damped Natural Frequency）。可以通过复平面图形辅助理解这一参数，将式(5.3.3)中 $G(s)$ 的两个共轭极点 $s_{\mathrm{p2}}$ 和 $s_{\mathrm{p3}}$ 在图5.3.1中的复平面上绘制出来，可以发现它们的横坐标为 $-\zeta \omega_{\mathrm{n}}$ ，纵坐标分别为 $\pm \omega_{\mathrm{n}}\sqrt{1 - \zeta^{2}}$ ，即阻尼固有频率。根据三角关系，它们的模（即长度）等于系统的固有频率 $\omega_{\mathrm{n}}$ 。

![](image/828f24705c91faf167d2eb591d9a404c6f116c3506fa6497edb3dd9bb183c96a.jpg)

<details>
<summary>text_image</summary>
