$$\phi^ {*} (t + T, \varepsilon) = 2 \pi + \phi^ {*} (t, \varepsilon), \forall t \geqslant 0 \tag {10.38}$$

则有 $R(\phi^{*}(t + T,\varepsilon),\varepsilon) = R(2\pi +\phi^{*}(t,\varepsilon),\varepsilon) = R(\phi^{*}(t,\varepsilon),\varepsilon)$

这表示 $R(\phi^{*}(t,\varepsilon),\varepsilon)$ 是以 $T$ 为周期的 $t$ 的函数。因为

$$\phi^ {*} (t + \tau , \varepsilon) = \phi^ {*} (t, \varepsilon) + \omega \tau + O (\varepsilon)$$

其中 $\tau \geqslant 0$ 有界，所以很容易看出，对于足够小的 $\varepsilon$ ，方程(10.38)有唯一的解 $T(\varepsilon) = 2\pi /\omega +O(\varepsilon)$ 。

在状态平面 $x_{1} - x_{2}$ 内，解 $r = R(\phi^{*}(t,\varepsilon),\varepsilon)$ 是在圆 $r = r^{*}$ 邻域内的一个闭轨道。由于周期解 $r = R(\phi ,\varepsilon)$ 是指数稳定的，所以闭轨道会将所有的解吸引至其邻域内，也就是说闭轨道是一个稳定的极限环。

例10.11 范德波尔方程 $\ddot{y} + y = \varepsilon \dot{y}(1 - y^2)$

是方程(10.33)的一个特例,其中 $\omega=1,g(y,\dot{y})=\dot{y}(1-y^{2})$ 。函数 $f_{\mathrm{av}}(r)$ 由下式给出:

$$
\begin{array}{l} f _ {\mathrm{av}} (r) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} \left(1 - r ^ {2} \sin^ {2} \phi\right) r \cos^ {2} \phi d \phi \\ = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} r \cos^ {2} \phi d \phi - \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} r ^ {3} \sin^ {2} \phi \cos^ {2} \phi d \phi \\ = \frac {1}{2} r - \frac {1}{8} r ^ {3} \\ \end{array}
$$

平均系统 $\frac{dr}{d\phi} = \varepsilon \left(\frac{1}{2} r - \frac{1}{8} r^3\right)$

有三个平衡点,分别在 r=0,r=2 和 r=-2。根据定义 $r \geqslant 0$ , 故舍去负根。通过线性化方法检验各平衡点的稳定性。其雅可比矩阵为

$$\frac {d f _ {\mathrm{av}}}{d r} = \frac {1}{2} - \frac {3}{8} r ^ {2}$$

即 $\frac{df_{\mathrm{av}}}{dr}\bigg|_{r = 0} = \frac{1}{2} >0;\quad \frac{df_{\mathrm{av}}}{dr}\bigg|_{r = 2} = -1 <   0$

这样,平衡点 r=2 是指数稳定的,因此对于足够小的 $\varepsilon$ , 范德波尔方程在 r=2 的一个 $O(\varepsilon)$ 邻域内有一个稳定极限环, 振荡周期是接近于 $2\pi$ 的 $O(\varepsilon)$ 。在例 2.6 中通过仿真可以观察到这个稳定的极限环。

可以推断,上述过程可用于证明非稳定极限圆的存在。对方程(10.33)进行反向时间变换,即用 $\tau = -t$ 代换t。如果系统在反向时间内有一个稳定极限环,则在正向时间内就有一个非稳定极限环。
