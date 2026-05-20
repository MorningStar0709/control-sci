在 $[0, b]$ 上有唯一解 $\bar{y}(s)$ ，对所有 $s \in [0, b]$ ， $\bar{y}(s) \in D$ ，且 $y(0, \varepsilon) - x_{\mathrm{av}}(0) = O(\varepsilon)$ ，则存在 $\varepsilon^* > 0$ ，使得对于所有 $0 < \varepsilon < \varepsilon^*$ ，扰动系统(10.30)对于所有 $s \in [0, b]$ 有唯一解，且两个解之间距离为 $O(\varepsilon)$ 。由式(10.28)可知， $t = s / \varepsilon$ 且 $x - y = O(\varepsilon)$ ，所以平均系统(10.24)的解给出方程(10.23)的解在以 $t$ 为时间尺度的时间区间 $[0, b / \varepsilon]$ 上的一个 $O(\varepsilon)$ 逼近。

假设平均系统(10.24)在原点有一个指数稳定平衡点，D是包含原点的定义域。设 $V(y)$ 是由（逆李雅普诺夫）定理4.17得出的李雅普诺夫函数，则对原点吸引区内的任何紧子集 $\Omega$ ，存在常数c>0，使得 $\Omega$ 在紧集 $\{V(y)\leqslant c\}$ 内。假设 $y_{\mathrm{av}}(0)\in\Omega$ ，且 $y(0,\varepsilon)-y_{\mathrm{av}}(0)=O(\varepsilon)$ ，应用定理9.1可证明对于所有 $s\geqslant0$ ，也就是说对于所有 $t\geqslant0,O(\varepsilon)$ 逼近成立。

最后,定理10.3证明在原点的一个 $O(\varepsilon)$ 邻域内,方程(10.30)有一个指数稳定的以 $\varepsilon T$ 为周期的解 $\bar{y}(s/\varepsilon,\varepsilon)$ 。周期解在s时间尺度内的周期为 $\varepsilon T$ ,即在t时间尺度内周期为T。由式(10.28)可知方程(10.23)有一个周期为T的解

$$\bar {x} (t, \varepsilon) = \bar {y} (t, \varepsilon) + \varepsilon u (t, \bar {y} (t, \varepsilon))$$

因为 u 是有界的, 所以周期解 $\bar{x}(t, \varepsilon)$ 位于原点的 $O(\varepsilon)$ 邻域内。下面的定理给出了结论。

定理 10.4 设对于每个紧集 $D_{0} \subset D$ ，以及 $(t, x, \varepsilon) \in [0, \infty) \times D_{0} \times [0, \varepsilon_{0}]$ ， $f(t, x, \varepsilon)$ 及其关于 $(x, \varepsilon)$ 的一阶与二阶偏导数是连续有界的， $D \subset D^{R}$ 是定义域。假设 f 是以 T 为周期的 t 的函数，T > 0， $\varepsilon$ 是一个正参数。令 $x(t, \varepsilon)$ 和 $x_{\mathrm{av}}(\varepsilon t)$ 分别表示方程 (10.23) 和方程 (10.24) 的解。

\- 如果 $x_{\mathrm{av}}(\varepsilon t) \in D, \forall t \in [0, b / \varepsilon]$ 且 $x(0, \varepsilon) - x_{\mathrm{av}}(0) = O(\varepsilon)$ , 则存在 $\varepsilon^{*} > 0$ , 使得对于所有 $0 < \varepsilon < \varepsilon^{*}, x(t, \varepsilon)$ 有定义, 且在 $[0, b / \varepsilon]$ 上有

$$x (t, \varepsilon) - x _ {\mathrm{av}} (\varepsilon t) = O (\varepsilon)$$

\- 如果原点 $x = 0 \in D$ 是平均系统(10.24)的一个指数稳定平衡点, $\Omega \subset D$ 是其吸引区的一个紧子集, $x_{\mathrm{av}}(0) \in \Omega$ , 且 $x(0, \varepsilon) - x_{\mathrm{av}}(0) = O(\varepsilon)$ , 则存在 $\varepsilon^{*} > 0$ , 使得对于所有 $0 < \varepsilon < \varepsilon^{*}, x(t, \varepsilon)$ 有定义, 且对于所有 $t \in [0, \infty)$

$$x (t, \varepsilon) - x _ {\mathrm{av}} (\varepsilon t) = O (\varepsilon)$$
