# 9.4 二阶系统的频率响应

本节将分析二阶系统的频率响应。如图 9.4.1 所示, 二阶系统的传递函数 $G(s) = \frac{\omega_{\mathrm{n}}^{2}}{s^{2} + 2\zeta\omega_{\mathrm{n}}s + \omega_{\mathrm{n}}^{2}}$ , 其中, $\omega_{\mathrm{n}}$ 是其固有频率, $\zeta$ 是阻尼比。

为分析其频率响应，先计算 $G(\mathrm{j}\omega_{\mathrm{i}})$ ，得到

$$
G (\mathrm{j} \omega_ {\mathrm{i}}) = \frac {\omega_ {\mathrm{n}} ^ {2}}{(\mathrm{j} \omega_ {\mathrm{i}}) ^ {2} + 2 \zeta \omega_ {\mathrm{n}} (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{n}} ^ {2}} = \frac {1}{- \frac {\omega_ {\mathrm{i}} ^ {2}}{\omega_ {\mathrm{n}} ^ {2}} + 2 \zeta \frac {\omega_ {\mathrm{i}}}{\omega_ {\mathrm{n}}} \mathrm{j} + 1}
$$

![](image/21fd62892fb576a08cebde2fee9730d0e15d6cbc3bdece1e2ad35029ef85a06e.jpg)  
图 9.4.1 二阶系统框图

(9.4.1)

为简化运算，令 $\frac{\omega_{\mathrm{i}}}{\omega_{\mathrm{n}}} = \Omega$ ，可得

$$
\begin{array}{l} G \left(\mathrm{j} \omega_ {\mathrm{i}}\right) = \frac {1}{- \Omega^ {2} + 2 \zeta \Omega \mathrm{j} + 1} = \frac {- \Omega^ {2} - 2 \zeta \Omega \mathrm{j} + 1}{(- \Omega^ {2} + 2 \zeta \Omega \mathrm{j} + 1) (- \Omega^ {2} - 2 \zeta \Omega \mathrm{j} + 1)} = \frac {1 - \Omega^ {2} - 2 \zeta \Omega \mathrm{j}}{(1 - \Omega^ {2}) ^ {2} + 4 \zeta^ {2} \Omega^ {2}} \\ = \frac {1 - \Omega^ {2}}{(1 - \Omega^ {2}) ^ {2} + 4 \zeta^ {2} \Omega^ {2}} - \frac {2 \zeta \Omega}{(1 - \Omega^ {2}) ^ {2} + 4 \zeta^ {2} \Omega^ {2}} \mathrm{j} \tag {9.4.2} \\ \end{array}
$$

它的实部部分为 $\frac{1 - \Omega^2}{(1 - \Omega^2)^2 + 4\zeta^2\Omega^2}$ ，虚部部分为 $-\frac{2\zeta\Omega}{(1 - \Omega^2)^2 + 4\zeta^2\Omega^2}$ 。可得

$$
\left| G \left(\mathrm{j} \omega_ {\mathrm{i}}\right) \right| = \sqrt {\left(\frac {1 - \Omega^ {2}}{\left(1 - \Omega^ {2}\right) ^ {2} + 4 \zeta^ {2} \Omega^ {2}}\right) ^ {2} + \left(- \frac {2 \zeta \Omega}{\left(1 - \Omega^ {2}\right) ^ {2} + 4 \zeta^ {2} \Omega^ {2}}\right) ^ {2}} = \sqrt {\frac {1}{\left(1 - \Omega^ {2}\right) ^ {2} + 4 \zeta^ {2} \Omega^ {2}}} \tag {9.4.3a}
$$

$$
\angle G (\mathrm{j} \omega_ {\mathrm{i}}) = \arctan \frac {- \frac {2 \zeta \Omega}{(1 - \Omega^ {2}) ^ {2} + 4 \zeta^ {2} \Omega^ {2}}}{\frac {1 - \Omega^ {2}}{(1 - \Omega^ {2}) ^ {2} + 4 \zeta^ {2} \Omega^ {2}}} = - \arctan \frac {2 \zeta \Omega}{1 - \Omega^ {2}} \tag {9.4.3b}
$$

分析式(9.4.3a)可以发现：
