# 5.5 本章要点总结

\- 二阶系统的一般表达形式：

- 微分方程： $\frac{\mathrm{d}^2x(t)}{\mathrm{d}t^2} + 2\zeta \omega_{\mathrm{n}}\frac{\mathrm{d}x(t)}{\mathrm{d}t} + \omega_{\mathrm{n}}^2 x(t) = \omega_{\mathrm{n}}^2 u(t)$ 。  
- 传递函数： $G(s)=\frac{X(s)}{U(s)}=\frac{\omega_{n}^{2}}{s^{2}+2\zeta\omega_{n}s+\omega_{n}^{2}}$

零输入状态空间方程表达： $\frac{\mathrm{dz}(t)}{\mathrm{dt}} = Az(t),A = \left[ \begin{array}{cc}0 & 1\\ -\omega_{\mathrm{n}}^{2} & -2\zeta \omega_{\mathrm{n}} \end{array} \right]$

\- 二阶系统对初始状态的响应：

\- 特征方程： $\lambda^{2}+2\zeta\omega_{n}\lambda+\omega_{n}^{2}=0$ 。

特征方程的解： $\left\{ \begin{array}{l} \lambda_{1} = -\zeta \omega_{n} + \omega_{n}\sqrt{\zeta^{2} - 1}\\ \lambda_{2} = -\zeta \omega_{n} - \omega_{n}\sqrt{\zeta^{2} - 1} \end{array} \right.$

\- 可采用相轨迹的方法分情况讨论分析。

\- 二阶系统的单位阶跃响应：

\- 系统输出的三个极点： $\left\{ \begin{array}{l} s_{p1} = 0 \\ s_{p2} = -\zeta \omega_n + \omega_n \sqrt{\zeta^2 - 1}, \text{其中 } s_{p1} \text{ 来自输入，} s_{p2} \text{ 和 } s_{p3} \\ s_{p3} = -\zeta \omega_n - \omega_n \sqrt{\zeta^2 - 1} \end{array} \right.$ 是传递函数的极点。

\- 欠阻尼系统 $(0 < \zeta < 1)$ : $x(t) = 1 - \mathrm{e}^{-\zeta \omega_{\mathrm{n}} t}[\cos \omega_{\mathrm{d}} t + \frac{\zeta}{\sqrt{1 - \zeta^2}} \sin \omega_{\mathrm{d}} t]$ 。

\- 无阻尼系统 $(\zeta = 0)$ ： $x(t) = 1 - \cos \omega_{\mathrm{n}}t$ 。

\- 临界阻尼系统 $(\zeta = 1): x(t) = 1 - \mathrm{e}^{-\omega_{\mathrm{n}}t}(1 + \omega_{\mathrm{n}}t)$ 。

。过阻尼系统( $\zeta>1$ ):

$$
\begin{array}{l} x (t) = 1 - \frac {1}{2 \sqrt {\zeta^ {2} - 1} (\zeta - \sqrt {\zeta^ {2} - 1})} \mathrm{e} ^ {(- \zeta \omega_ {\mathrm{n}} + \omega_ {\mathrm{n}} \sqrt {\zeta^ {2} - 1}) t} + \\ \frac {1}{2 \sqrt {\zeta^ {2} - 1} (\zeta + \sqrt {\zeta^ {2} - 1})} e ^ {(- \zeta \omega_ {n} - \omega_ {n} \sqrt {\zeta^ {2} - 1}) t} 。 \\ \end{array}
$$

\- 二阶系统性能指标：

\- 上升时间：系统第一次到达稳定点的时间，体现了系统的反应速度。

。最大超调量：系统输出的最大值(峰值)减去稳态值，再乘以100%。

\- 稳定时间：系统进入稳态的误差范围内的时间，一般就是最终状态的 $2 \%$ 以内。
