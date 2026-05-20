$$u _ {\rho} (t) = \frac {1}{\| \mathrm{e} ^ {- \rho t ^ {2}} \cos \omega_ {0} t \| _ {2}} \mathrm{e} ^ {- \rho t ^ {2}} \cos \omega_ {0} t, \qquad t \geqslant 0,$$

其中 $\rho > 0$ 是正数， $\omega_0$ 是满足 $|G(\mathrm{j}\omega_0)| = \sup_{-\infty < \omega < \infty} |G(\mathrm{j}\omega)| - \varepsilon$ 的常数， $\varepsilon > 0$ 为充分小的正数.

由定义显然有 $\| u_{\rho}(\cdot)\| _2 = 1$ 又由于

$$
\begin{array}{l} \lim _ {\rho \rightarrow \infty} \mathcal {F} \left\{\mathrm{e} ^ {- \rho t ^ {2}} \cos \omega_ {0} t \right\} = \lim _ {\rho \rightarrow \infty} \frac {1}{2} \sqrt {\frac {\pi}{\rho}} \left\{\mathrm{e} ^ {- \frac {\left(\omega - \omega_ {0}\right) ^ {2}}{4 \rho}} + \mathrm{e} ^ {- \frac {\left(\omega + \omega_ {0}\right) ^ {2}}{4 \rho}} \right\}, \\ = \pi \left\{\delta \left(\omega - \omega_ {0}\right) + \delta \left(\omega + \omega_ {0}\right) \right\}, \\ \end{array}
$$

其中 $\mathcal{F}\{\cdot\}$ 表示Fourier变换， $\delta(t)$ 为单位脉冲函数。因此

$$\lim _ {\rho \rightarrow \infty} \| e ^ {- \rho t ^ {2}} \cos \omega_ {0} t \| _ {2} = \lim _ {\rho \rightarrow \infty} \left\{\frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} \pi^ {2} | \delta (\omega - \omega_ {0}) + \delta (\omega + \omega_ {0}) | ^ {2} d \omega \right\} ^ {1 / 2} = \sqrt {\pi},$$

而且与 $u_{\rho}(t)$ 对应的输出 $y_{\rho}(t)$ 满足

$$\lim _ {\rho \rightarrow \infty} \| y _ {\rho} (\cdot) \| _ {2} ^ {2} = \lim _ {\rho \rightarrow \infty} \frac {1}{2 \pi} \int_ {- \infty} ^ {+ \infty} | G (\mathrm{j} \omega) u _ {\rho} (\mathrm{j} \omega) | ^ {2} \mathrm{d} \omega = | G (\mathrm{j} \omega_ {0}) | ^ {2}.$$

这表明对于任意给定的充分小正数 $\varepsilon > 0$ ，存在 $u_{\rho} \in L_2, \| u_{\rho} \|_2 = 1$ 使得

$$\frac {\left\| y _ {\rho} \right\| _ {2}}{\left\| u _ {\rho} \right\| _ {2}} = \frac {\left\| G (\cdot) u _ {\rho} \right\| _ {2}}{\left\| u _ {\rho} \right\| _ {2}} = | G \left(\omega_ {0}\right) | = \| G (\cdot) \| _ {\infty} - \varepsilon . \tag {6.1.7}$$

由式 (6.1.6) 和式 (6.1.7), 式 (6.1.5) 得证.

引理6.1.2 设 $G_{1}(\cdot) \in RH_{\infty}^{n \times r}, G_{2}(\cdot) \in RH_{\infty}^{r \times m}$ , 则有

$$\left\| G _ {1} (\cdot) G _ {2} (\cdot) \right\| _ {\infty} \leqslant \left\| G _ {1} (\cdot) \right\| _ {\infty} \left\| G _ {2} (\cdot) \right\| _ {\infty}. \tag {6.1.8}$$

证明 记 $y = G_{2}(\cdot)u$ ，则根据引理6.1.1，得
