$$
\begin{array}{l} \dot {V} = \eta (\eta^ {2} - \eta \xi) + (\xi - \eta - \eta^ {2}) [ u - (1 + 2 \eta) (\eta^ {2} - \eta \xi) ] \\ = - \eta^ {4} + (\xi - \eta - \eta^ {2}) [ - \eta^ {2} + u - (1 + 2 \eta) (\eta^ {2} - \eta \xi) ] \\ \end{array}
$$

控制律取 $u=(1+2\eta)(\eta^{2}-\eta\xi)+\eta^{2}-k(\xi-\eta-\eta^{2}),\quad k>0$

得 $\dot{V} = -\eta^4 - k(\xi - \eta - \eta^2)^2$

说明原点是全局渐近稳定的。

△

前面两节讨论了当不确定项满足匹配条件时,如何利用滑模控制及李雅普诺夫再设计对不确定系统进行鲁棒稳定控制,而反步法可放宽匹配条件。为了说明这一点,考虑单输入系统

$$\dot {\eta} = f (\eta) + g (\eta) \xi + \delta_ {\eta} (\eta , \xi) \tag {14.58}\dot {\xi} = f _ {a} (\eta , \xi) + g _ {a} (\eta , \xi) u + \delta_ {\xi} (\eta , \xi) \tag {14.59}$$

该系统定义在包含原点 $(\eta = 0, \xi = 0)$ 的定义域 $D \subset R^{n + 1}$ 上， $\eta \in R^n, \xi \in R$ 。假设对于所有 $(\eta, \xi) \in D, g_a(\eta, \xi) \neq 0$ ，且所有函数都是光滑的。设 $f, g, f_a$ 和 $g_a$ 已知， $\delta_\eta$ 和 $\delta_\xi$ 为不确定项，并假设 $f$ 和 $f_a$ 在原点为零，不确定项对于所有 $(\eta, \xi) \in D$ ，满足不等式

$$\left\| \delta_ {\eta} (\eta , \xi) \right\| _ {2} \leqslant a _ {1} \| \eta \| _ {2} \tag {14.60}\left| \delta_ {\xi} (\eta , \xi) \right| \leqslant a _ {2} \| \eta \| _ {2} + a _ {3} | \xi | \tag {14.61}$$

不等式(14.60)限制了不确定项的类型,因为它限定 $\delta_{\eta}(\eta,\xi)$ 的上界取决于 $\eta$ , 不过这个限定没有匹配条件 $\delta_{\eta}=0$ 严格。从系统(14.58)入手, 假设能找到一个稳定的状态反馈控制律 $\xi=\phi(\eta),\phi(0)=0$ , 和一个(光滑、正定的)李雅普诺夫函数 $V(\eta)$ , 使得对于所有 $(\eta,\xi)\in D$ 和某个正常数 b, 满足

$$\frac {\partial V}{\partial \eta} [ f (\eta) + g (\eta) \phi (\eta) + \delta_ {\eta} (\eta , \xi) ] \leqslant - b \| \eta \| _ {2} ^ {2} \tag {14.62}$$

不等式(14.62)说明 $\eta = 0$ 是系统

$$\dot {\eta} = f (\eta) + g (\eta) \phi (\eta) + \delta_ {\eta} (\eta , \xi)$$

的渐近稳定平衡点。进一步假设 $\phi (\eta)$ 在 $D$ 上满足不等式

$$\left| \phi (\eta) \right| \leqslant a _ {4} \| \eta \| _ {2}, \quad \left\| \frac {\partial \phi}{\partial \eta} \right\| _ {2} \leqslant a _ {5} \tag {14.63}$$

现在考虑备选李雅普诺夫函数 $V_{c}(\eta ,\xi) = V(\eta) + \frac{1}{2} [\xi -\phi (\eta)]^{2}$ (14.64)

$V_{c}$ 沿方程(14.58)和方程(14.59)轨线的导数为

$$
\begin{array}{l} \dot {V} _ {c} = \frac {\partial V}{\partial \eta} (f + g \phi + \delta_ {\eta}) + \frac {\partial V}{\partial \eta} g (\xi - \phi) \\ + (\xi - \phi) \left[ f _ {a} + g _ {a} u + \delta_ {\xi} - \frac {\partial \phi}{\partial \eta} (f + g \xi + \delta_ {\eta}) \right] \\ \end{array}
$$

取 $u = \frac{1}{g_a}\left[\frac{\partial\phi}{\partial\eta} (f + g\xi) - \frac{\partial V}{\partial\eta} g - f_a - k(\xi -\phi)\right],\quad k > 0$ (14.65)
