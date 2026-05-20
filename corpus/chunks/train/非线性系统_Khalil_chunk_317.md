其中，对于足够小的 $\varepsilon, q(t, y, \varepsilon)$ 在 $[0, \infty) \times D_0$ 上有界。在推导方程(10.47)的过程中，用到 $\alpha(\varepsilon) \geqslant c\varepsilon$ 。方程(10.47)是平均系统

$$\dot {x} = \varepsilon f _ {\mathrm{av}} (x) \tag {10.48}$$

的一个扰动。平均系统方程与方程(10.29)相似,只是q的系数为 $\varepsilon\alpha(\varepsilon)$ ,而不是 $\varepsilon^{2}$ ,由此可得到如下定理,除估算值 $O(\varepsilon)$ 由 $O(\alpha(\varepsilon))$ 代替之外,该定理与定理10.4相似。

定理10.5 设 $f(t, x, \varepsilon)$ 及其关于 $(x, \varepsilon)$ 的一阶与二阶偏导数，对于每个紧集 $D_0 \subset D$ ，以及 $(t, x, \varepsilon) \in [0, \infty) \times D_0 \times [0, \varepsilon_0]$ 是连续有界的，其中 $\varepsilon > 0, D \subset R^n$ 是定义域。假设在 $[0, \infty) \times D_0$ 上， $f(t, x, 0)$ 有平均函数 $f_{\mathrm{av}}(x)$ ，且 $h(t, x) = f(t, x, 0)f_{\mathrm{av}}(x)$ 的雅可比函数有零平均，并具有与 $f$ 相同的收敛函数。设 $x(t, \varepsilon)$ 和 $x_{\mathrm{av}}(\varepsilon t)$ 分别表示方程(10.39)和方程(10.48)的解， $\alpha$ 是出现在式(10.44)和式(10.45)估算值中的 $\kappa$ 类函数。

\- 如果 $x_{\mathrm{av}}(\varepsilon t) \in D, \forall t \in [0, b / \varepsilon]$ 和 $x(0, \varepsilon) - x_{\mathrm{av}}(0) = O(\alpha(\varepsilon))$ ，则存在 $\varepsilon^{*} > 0$ ，使得对于所有 $0 < \varepsilon < \varepsilon^{*}, x(t, \varepsilon)$ 有定义，且在 $[0, b / \varepsilon]$ 有

$$x (t, \varepsilon) - x _ {\mathrm{av}} (\varepsilon t) = O (\alpha (\varepsilon))$$

\- 如果原点 $x = 0 \in D$ 是平均系统(10.48)的一个指数稳定平衡点, $\Omega \subset D$ 是其吸引区的一个紧子集, $x_{\mathrm{av}}(0) \in \Omega$ , 且 $x(0, \varepsilon) - x_{\mathrm{av}}(0, \varepsilon) = O(\alpha(\varepsilon))$ , 则存在 $\varepsilon^{*} > 0$ , 使得对于所有 $0 < \varepsilon < \varepsilon^{*}, x(t, \varepsilon)$ 有定义, 且对于所有 $t \in [0, \infty)$ 有

$$x (t, \varepsilon) - x _ {\mathrm{av}} (\varepsilon t) = O (\alpha (\varepsilon))$$

\- 如果原点 $x = 0 \in D$ 是平均系统(10.48)的一个指数稳定平衡点，且对于所有 $(t, \varepsilon) \in [0, \infty) \times [0, \varepsilon_0]$ ， $f(t, 0, \varepsilon) = 0$ ，则存在 $\varepsilon^* > 0$ ，使得对于所有 $0 < \varepsilon < \varepsilon^*$ ，原点是原系统(10.39)的一个指数稳定平衡点。

证明:通过用 $s = \varepsilon t$ 时间尺度表示方程(10.47)，应用定理3.4和定理3.5，以及式(10.46)的变量代换，可以得出定理的第一部分。对于第二部分，应用定理9.1中关于无限时间区间上解的连续性。最后，利用 $h(t,0)=0, w(t,0,\eta)=0$ 和边界 $\|\partial w/\partial x\| \leqslant k\alpha(\eta)/\eta$ ，可知 w 的估算值修正为

$$\eta \| w (t, x, \eta) \| \leqslant k \alpha (\eta) \| x \|$$

假设 $f(t,0,\varepsilon)=0$ 和f关于 $\varepsilon$ 的可微性表明， $f(t,x,\varepsilon)$ 关于 $\varepsilon$ 是利普希茨的，关于x是线性的，即
