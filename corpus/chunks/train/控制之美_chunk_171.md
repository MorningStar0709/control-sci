(1) 当 $\omega_{i}=0$ 时, $\Omega=0$ , $|G(j0)|=\sqrt{\frac{1}{(1-0)^{2}+4\zeta^{2}\times0}}=1$ 。  
(2) 当 $\omega_{\mathrm{i}} = \omega_{\mathrm{n}}$ 时, $\Omega = 1$ , $|G(\mathrm{j}\omega_{\mathrm{n}})| = \sqrt{\frac{1}{(1 - 1^2)^2 + 4\xi^2}} = \frac{1}{2\xi}$ 。在这种情况下, 如果 $\zeta < 0.5$ , $|G(\mathrm{j}\omega_{\mathrm{n}})| > 1$ , 输出的振幅就会被加强; 如果 $\zeta > 0.5$ , $|G(\mathrm{j}\omega_{\mathrm{n}})| < 1$ , 输出的振幅则会被减弱。当 $\zeta = 0$ 时 (无阻尼系统), $|G(\mathrm{j}\omega_{\mathrm{n}})| \to \infty$ 。  
(3) 当 $\omega_{\mathrm{i}} \to \infty$ 时, $\Omega \to \infty$ , 此时 $\lim_{\omega_{\mathrm{i}} \to \infty} |G(\mathrm{j}\omega_{\mathrm{i}})| = \lim_{\Omega \to \infty} \sqrt{\frac{1}{(1 - \Omega^2)^2 + 4\zeta^2\Omega^2}} = 0$ 。

根据上面三点可以判断出, $\zeta$ 在某些条件下,当输入频率 $\omega_{i}$ 从0到 $\infty$ 变化时,输出的振幅 $|G(j\omega_{i})|$ 会呈现先增后减的趋势。求 $|G(j\omega_{i})|$ 的极值,令式(9.4.3a)的分母部分对 $\Omega$ 求导等于0,得到

$$
\frac {\mathrm{d} ((1 - \Omega^ {2}) ^ {2} + 4 \zeta^ {2} \Omega^ {2})}{\mathrm{d} \Omega} = 0
$$

$$
\Rightarrow 2 (1 - \Omega^ {2}) (- 2 \Omega) + 8 \zeta^ {2} \Omega = 0
$$

$$
\Rightarrow - 1 + \Omega^ {2} + 2 \zeta^ {2} = 0
$$

$$
\Rightarrow \Omega = \pm \sqrt {1 - 2 \zeta^ {2}} \tag {9.4.4}
$$

因为 $\Omega > 0$ ，所以取 $\Omega = \sqrt{1 - 2\zeta^2} = \frac{\omega_i}{\omega_n}$ 。同时因为 $\Omega$ 为正实数，所以只有在阻尼比 $\zeta < \sqrt{0.5}$ 时，式(9.4.4)才有意义， $|G(j\omega_i)|$ 才会表现出先增后减的性质。定义 $|G(j\omega_i)|$ 最大值时的输入频率为 $\omega_R = \omega_n \sqrt{1 - 2\zeta^2}$ ，称为共振频率（Resonant Frequency）（此时 $\Omega = \frac{\omega_i}{\omega_n} = \sqrt{1 - 2\zeta^2}$ ）。同时可以发现，当阻尼比 $\zeta$ 很小的时候，共振频率约等于系统的固有频率，即 $\omega_R \approx \omega_n$ 。

不同阻尼比条件下的二阶系统频率响应如图9.4.2所示(目前请读者主要关注图形的示意,暂时忽略横轴与纵轴的单位),可见,如果阻尼比 $\zeta$ 较小,当外界输入的频率 $\omega_{\mathrm{i}}$ 在共振频率 $\omega_{\mathrm{R}}$ 附近时,系统输出会表现出强烈的振幅响应,这个现象称为共振。

从系统稳定性的角度考虑, 当 $\zeta = 0$ 时, 二阶系统的传递函数为 $G(s) = \frac{\omega_{\mathrm{n}}^{2}}{s^{2} + \omega_{\mathrm{n}}^{2}}$ , 它的极点在虚轴上, $s_{\mathrm{p}} = \pm \mathrm{j}\omega_{\mathrm{n}}$ 。根据第6章的分析, 该动态系统符合临界稳定但不满足BIBO稳定,此时一个有界的正弦输入,例如 $u(t) = \sin (\omega_{\mathrm{n}}t)$ , 也会导致其振幅响应 $|G(\mathrm{j}\omega_{\mathrm{n}})| \to \infty$ 。

![](image/a1ebc70afbddd261eff356bee919a1b55891a541b6ae92e20e1f0b24268a7312.jpg)  
图 9.4.2 二阶系统的振幅频率响应
