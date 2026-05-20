# 2. 分析参数 $\alpha$ 的设计

根据典型环节的频率特性可知，积分环节 $\frac{1}{s}$ 的相频为 $-\frac{\pi}{2}$ ，一阶惯性环节 $\frac{1}{s + 1}$ 的相频为 $-\arctan T\omega$ ；一阶微分环节 $\tau s + 1$ 的相频为 $\arctan \tau \omega$ ，则 $G(s) = \frac{K_{\mathrm{g}}}{s(T_{\mathrm{g}}s + 1)}$ 的相位为 $\varphi_{\mathrm{G}}(\omega) = -\frac{\pi}{2} - \arctan T_{\mathrm{g}}\omega$ ，PI 控制器 $K(s) = K_{\mathrm{p}}\left(1 + \frac{1}{T_{\mathrm{i}}s}\right) = K_{\mathrm{p}}\frac{1}{T_{\mathrm{i}}}\frac{1}{s}\left(T_{\mathrm{i}}s + 1\right)$ 的相位为 $\varphi_{\mathrm{K}}(\omega) = -\frac{\pi}{2} + \arctan T_{\mathrm{i}}\omega$ 。

根据相位裕度的定义，可得闭环系统 $G(s)K(s)$ 的相位裕度为

$$
\begin{array}{l} \varphi_ {\mathrm{GK}} (\omega) = \varphi_ {\mathrm{G}} (\omega) + \varphi_ {\mathrm{K}} (\omega) - (- \pi) \\ = - \frac {\pi}{2} - \arctan T _ {\mathrm{g}} \omega - \frac {\pi}{2} + \arctan T _ {\mathrm{i}} \omega - (- \pi) \\ = - \arctan T _ {\mathrm{g}} \omega + \arctan T _ {\mathrm{i}} \omega \\ \end{array}
$$

闭环系统 $G(s)K(s)$ 的最大相位裕度为

$$
\begin{array}{l} \phi_ {\mathrm{m}} = \varphi_ {\mathrm{GK}} \left(\omega_ {\mathrm{c}}\right) = - \arctan T _ {\mathrm{g}} \omega_ {\mathrm{c}} + \arctan T _ {\mathrm{i}} \omega_ {\mathrm{c}} \\ = - \arctan \frac {\omega_ {\mathrm{c}}}{\omega_ {\mathrm{g}}} + \arctan \frac {\omega_ {\mathrm{c}}}{\omega_ {\mathrm{i}}} = - \arctan \frac {1}{\sqrt {\alpha}} + \arctan \sqrt {\alpha} \\ \end{array}
$$

根据 $\tan(\alpha-\beta)=\frac{\tan\alpha-\tan\beta}{1+\tan\alpha\tan\beta}$ ，则

$$\tan \phi_ {\mathrm{m}} = \tan \left(\arctan \sqrt {\alpha} - \arctan \frac {1}{\sqrt {\alpha}}\right) = \frac {\sqrt {\alpha} - \frac {1}{\sqrt {\alpha}}}{1 + \sqrt {\alpha} \frac {1}{\sqrt {\alpha}}} = \frac {\sqrt {\alpha} - \frac {1}{\sqrt {\alpha}}}{2} = \frac {\alpha - 1}{2 \sqrt {\alpha}}$$

由 $\tan\phi_{m}=\frac{\sin\phi_{m}}{\cos\phi_{m}}$ 代入，整理得

$$\alpha \cos \phi_ {\mathrm{m}} - 2 \sqrt {\alpha} \sin \phi_ {\mathrm{m}} - \cos \phi_ {\mathrm{m}} = 0$$

令 $x=\sqrt{\alpha}$ ，则上式写为

$$x ^ {2} \cos \phi_ {\mathrm{m}} - 2 x \sin \phi_ {\mathrm{m}} - \cos \phi_ {\mathrm{m}} = 0 \tag {2.22}$$

解方程，得

$$x _ {1, 2} = \frac {2 \sin \phi_ {\mathrm{m}} \pm \sqrt {4 \sin \phi_ {\mathrm{m}} ^ {2} - 4 \cos \phi_ {\mathrm{m}} (- \cos \phi_ {\mathrm{m}})}}{2 \cos \phi_ {\mathrm{m}}} = \frac {\sin \phi_ {\mathrm{m}} \pm 1}{\cos \phi_ {\mathrm{m}}}$$
