# 13.4.2 跟踪

考虑一个单输入-单输出、可输入-输出线性化的系统,以标准形(13.16)\~(13.18)的形式表示为

$$
\begin{array}{l} \dot {\eta} = f _ {0} (\eta , \xi) \\ \dot {\xi} = A _ {c} \xi + B _ {c} \gamma (x) [ u - \alpha (x) ] \\ y = C _ {c} \xi \\ \end{array}
$$

为了不失一般性,假设 $f_{0}(0,0)=0$ 。我们希望设计一个状态反馈控制律,使输出y渐近跟踪参考信号 $r(t)$ 。当系统的相对阶为 $\rho = n$ 时，系统没有非平凡零动态，此时变量 $\eta$ 及其方程略去，但其他部分保持不变。假设

\- $r(t)$ 及其直到 $\rho$ 阶导数 $r^{(\rho)}(t)$ 对于所有 $t \geqslant 0$ 有界, 第 $\rho$ 阶导数 $r^{(\rho)}(t)$ 是 $t$ 的分段连续函数:

\- 信号 $r, \cdots, r^{(\rho)}$ 可在线获得。

参考信号 $r(t)$ 及其导数可以是某个指定的时间的函数, 或者是由某个输入信号 $w(t)$ 驱动的参考模型的输出。对后者可通过适当选择参考模型满足对 r 的假设。例如, 一个相对阶为 2 的系统, 其参考模型可能是二阶线性时不变系统, 由传递函数

$$\frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}$$

表示,其中 $\zeta$ 和 $\omega_{n}$ 为正常数,对于给定的输入信号 $w(t)$ ,应该适当选择这两个常数,以形成参考信号 $r(t)$ 。信号 $r(t)$ 可由状态模型

$$
\begin{array}{l} \dot {y} _ {1} = y _ {2} \\ \dot {y} _ {2} = - \omega_ {n} ^ {2} y _ {1} - 2 \zeta \omega_ {n} y _ {2} + \omega_ {n} ^ {2} w \\ r = y _ {1} \\ \end{array}
$$

在线产生。因此， $r(t)$ ， $\dot{r}(t)$ 和 $\ddot{r}(t)$ 都可在线获得。如果 $w(t)$ 是 t 的分段连续有界函数，则 $r(t)$ ， $\dot{r}(t)$ 和 $\ddot{r}(t)$ 满足所要求的假设条件。

设

$$
\mathcal {R} = \left[ \begin{array}{c} r \\ \vdots \\ r ^ {(\rho - 1)} \end{array} \right], \quad e = \left[ \begin{array}{c} \xi_ {1} - r \\ \vdots \\ \xi_ {\rho} - r ^ {(\rho - 1)} \end{array} \right] = \xi - \mathcal {R}
$$

通过变量代换 $e = \xi -\mathcal{R}$ ，可得

$$
\begin{array}{l} \dot {\eta} = f _ {0} (\eta , e + \mathcal {R}) \\ \dot {e} = A _ {c} e + B _ {c} \left\{\gamma (x) [ u - \alpha (x) ] - r ^ {(\rho)} \right\} \\ \end{array}
$$

状态反馈控制 $u = \alpha (x) + \beta (x)\left[v + r^{(\rho)}\right]$

把标准形简化为级联系统

$$
\begin{array}{l} \dot {\eta} = f _ {0} (\eta , e + \mathcal {R}) \\ \dot {e} = A _ {c} e + B _ {c} v \\ \end{array}
$$

其中 $\beta(x)=1/\gamma(x)$ 。设计任何使第二个方程稳定的 v，并对于所有 $t\geqslant0$ 保持 $\eta$ 有界，即可满足控制目标。若 v=-Ke，其中 $A_{c}-B_{c}K$ 是赫尔维茨矩阵，则完全状态反馈控制为 $^{①}$

$$u = \alpha (x) + \beta (x) \left\{- K [ T _ {2} (x) - \mathcal {R} ] + r ^ {(\rho)} \right\} \tag {13.47}$$

闭环系统为 $\dot{\eta} = f_{0}(\eta, e + \mathcal{R})$ (13.48)

$$\dot {e} = (A _ {c} - B _ {c} K) e \tag {13.49}$$

对于最小相位系统, $\dot{\eta}=f_{0}(\eta,0)$ 的原点是渐近稳定的。由(逆李雅普诺夫函数)定理4.16和定理4.18可知,对于足够小的 $e(0),\eta(0)$ 和 $\mathcal{R}(t)$ ,状态 $\eta(t)$ 对于所有 $t\geqslant0$ 有界。这样,状态反馈控制(13.47)就解决了局部跟踪问题。为了使该控制扩展到全局跟踪,我们要面对在全局稳定性中遇到的同样问题,这里 $\mathcal{R}(t)$ 是t的任意有界函数。确保全局跟踪的充分条件是系统 $\dot{\eta}=f_{0}(\eta,\xi)$ 为输入-状态稳定的。
