# 10.5 弱非线性二阶振荡器

考虑二阶系统

$$\ddot {y} + \omega^ {2} y = \varepsilon g (y, \dot {y}) \tag {10.33}$$

其中，在 $(y, \dot{y})$ 的紧集上， $g(\cdot, \cdot)$ 足够光滑，且 $|g|$ 以 $k|y|$ 或 $k| \dot{y}|$ 为界， $k$ 为正常数。选择 $x_{1} = y$ 和 $x_{2} = \dot{y} / \omega$ 作为状态变量，得到状态方程

$$
\begin{array}{l} \dot {x} _ {1} = \omega x _ {2} \\ \dot {x} _ {2} = - \omega x _ {1} + \frac {\varepsilon}{\omega} g (x _ {1}, \omega x _ {2}) \\ \end{array}
$$

用极坐标

$$x _ {1} = r \sin \phi , \quad x _ {2} = r \cos \phi$$

表示系统,有 $\dot{r} = \frac{1}{r}(x_{1}\dot{x}_{1} + x_{2}\dot{x}_{2}) = \frac{\varepsilon}{\omega}g(r\sin\phi,\omega r\cos\phi)\cos\phi$ (10.34)

$$\dot {\phi} = \frac {1}{r ^ {2}} (x _ {2} \dot {x} _ {1} - x _ {1} \dot {x} _ {2}) = \omega - \frac {\varepsilon}{\omega r} g (r \sin \phi , \omega r \cos \phi) \sin \phi \tag {10.35}$$

方程(10.35)右边的第二项在 r 的有界集上是 $O(\varepsilon)$ ，这是假设 $|g|$ 以 $k|y|$ 或 $k|\dot{y}|$ 为界的结果。因此，对于足够小的 $\varepsilon$ ，方程(10.35)的右边为正。式(10.34)除以式(10.35)得

$$\frac {d r}{d \phi} = \frac {\varepsilon g (r \sin \phi , \omega r \cos \phi) \cos \phi}{\omega^ {2} - (\varepsilon / r) g (r \sin \phi , \omega r \cos \phi) \sin \phi}$$

把方程重写为 $\frac{dr}{d\phi} = \varepsilon f(\phi, r, \varepsilon)$ (10.36)

其中 $f(\phi ,r,\varepsilon) = \frac{g(r\sin\phi,\omega r\cos\phi)\cos\phi}{\omega^2 - (\varepsilon /r)g(r\sin\phi,\omega r\cos\phi)\sin\phi}$

如果把 $\phi$ 看成独立变量,则方程(10.36)具有方程(10.23)的形式,其中 $f(\phi,r,\varepsilon)$ 是以 $2\pi$ 为周期的 $\phi$ 的函数。函数 $f_{\mathrm{av}}(r)$ 由下式给出:

$$f _ {\mathrm{av}} (r) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} f (\phi , r, 0) d \phi = \frac {1}{2 \pi \omega^ {2}} \int_ {0} ^ {2 \pi} g (r \sin \phi , \omega r \cos \phi) \cos \phi d \phi$$

假设平均系统 $\frac{dr}{d\phi} = \varepsilon f_{\mathrm{av}}(r)$ (10.37)

有一个平衡点 $r^*$ ，其中 $[\partial f_{\mathrm{av}} / \partial r](r^*) < 0$ ，则存在 $\varepsilon^* > 0$ ，使得 $\forall 0 < \varepsilon < \varepsilon^*$ ，方程(10.36)在 $r^*$ 的 $O(\varepsilon)$ 邻域内有唯一以 $2\pi$ 为周期的指数稳定解 $r = R(\phi, \varepsilon)$ 。这并不能说方程(10.33)有一个关于 $t$ 的周期解，要得到这个结论还有更多工作要做。将 $r = R(\phi, \varepsilon)$ 代入方程(10.35)，得

$$\dot {\phi} = \omega - \frac {\varepsilon}{\omega R (\phi , \varepsilon)} g (R (\phi , \varepsilon) \sin \phi , \omega R (\phi , \varepsilon) \cos \phi) \sin \phi$$

设 $\phi^{*}(t,\varepsilon)$ 是该方程始于 $\phi^{*}(0,\varepsilon)=0$ 的解。为了证明方程(10.33)有一个周期解,需要证明存在 $T=T(\varepsilon)>0$ (一般来说T与 $\varepsilon$ 有关),使得
