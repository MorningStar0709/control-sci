$$
\begin{array}{l} \dot {\eta} = f _ {0} (\eta , \xi) \\ \dot {\xi} _ {1} = \xi_ {2} \\ \begin{array}{c c} \bullet & \bullet \\ \bullet & \bullet \\ \bullet & \bullet \end{array} \\ \dot {\xi} _ {\rho - 1} = \xi_ {\rho} \\ \dot {\xi} _ {\rho} = L _ {f} ^ {\rho} h (x) + L _ {\delta_ {1}} L _ {f} ^ {\rho - 1} h (x) + L _ {g} L _ {f} ^ {\rho - 1} h (x) [ u + \delta (t, x, u) ] \\ y = \xi_ {1} \\ \end{array}
$$

设

$$
\mathcal {R} = \left[ \begin{array}{c} r \\ \vdots \\ r ^ {(\rho - 1)} \end{array} \right], \quad e = \left[ \begin{array}{c} \xi_ {1} - r \\ \vdots \\ \xi_ {\rho} - r ^ {(\rho - 1)} \end{array} \right] = \xi - \mathcal {R}
$$

进行变量代换 $e=\xi-\mathcal{R}$ ，得

$$
\begin{array}{l} \dot {\eta} = f _ {0} (\eta , \xi) \\ \dot {e} _ {1} = e _ {2} \\ \begin{array}{c c} \cdot & \cdot \\ \cdot & \cdot \\ \cdot & \cdot \end{array} \\ \dot {e} _ {\rho - 1} = e _ {\rho} \\ \dot {e} _ {\rho} = L _ {f} ^ {\rho} h (x) + L _ {\delta_ {1}} L _ {f} ^ {\rho - 1} h (x) + L _ {g} L _ {f} ^ {\rho - 1} h (x) [ u + \delta (t, x, u) ] - r ^ {(\rho)} (t) \\ \end{array}
$$

如果设计一个状态反馈控制律,能保证 $e(t)$ 有界且当 t 趋于无穷时收敛到零,就可以实现渐近跟踪。e 的有界性能够保证 $\xi$ 有界,因为 $\mathcal{R}(t)$ 是有界的。此外还要保证 $\eta$ 有界,为此将分析限定在系统 $\dot{\eta}=f_{0}(\eta,\xi)$

是有界输入-有界状态稳定的情况,这就是系统 $\dot{\eta}=f_{0}(\eta,\xi)$ 在输入-状态稳定时,对任何有界输入 $\xi$ 和任何初始状态 $\eta(0)$ 的情况。从这一角度出发,我们就可以将分析的重点放在证明 e 的有界性及收敛性上。 $\dot{e}$ 方程采用方程(14.4)和方程(14.5)的正则形式, $\eta=\left[e_{1},\cdots,e_{\rho-1}\right]^{T}$ , $\xi=e_{\rho}$ 。首先研究系统

$$
\begin{array}{l} \dot {e} _ {1} = e _ {2} \\ \begin{array}{c c} \vdots & \vdots \\ \vdots & \vdots \end{array} \\ \dot {e} _ {\rho - 1} = e _ {\rho} \\ \end{array}
$$

其中 $e_{\rho}$ 视为控制输入,我们要设计 $e_{\rho}$ 使原点稳定,对于线性系统(以可控标准形表示),可以通过线性控制

$$e _ {\rho} = - (k _ {1} e _ {1} + \dots + k _ {\rho - 1} e _ {\rho - 1})$$

实现,其中选择 $k_{1}$ 到 $k_{\rho-1}$ ,使多项式

$$s ^ {\rho - 1} + k _ {\rho - 1} s ^ {\rho - 2} + \dots + k _ {1}$$

为赫尔维茨的,则滑动流形为 $s=(k_{1}e_{1}+\cdots+k_{\rho-1}e_{\rho-1})+e_{\rho}=0$

并且 $\dot{s}=k_{1}e_{2}+\cdots+k_{\rho-1}e_{\rho}+L_{f}^{\rho}h(x)+L_{\delta_{1}}L_{f}^{\rho-1}h(x)+L_{g}L_{f}^{\rho-1}h(x)[u+\delta(t,x,u)]-r^{(\rho)}(t)$

然后可以把 u = v 设计为纯切换分量, 或可以取

$$u = - \frac {1}{L _ {\hat {g}} L _ {f} ^ {\rho - 1} h (x)} \left[ k _ {1} e _ {2} + \dots + k _ {\rho - 1} e _ {\rho} + L _ {f} ^ {\rho} h (x) - r ^ {(\rho)} (t) \right] + v$$

消去方程右边的已知项,其中 $\hat{g}(x)$ 为 $g(x)$ 的标称模型。注意,当 g 已知时,即 $\hat{g}=g$ 时,

$$- \frac {1}{L _ {g} L _ {f} ^ {\rho - 1} h (x)} \left[ L _ {f} ^ {\rho} h (x) - r ^ {(\rho)} (t) \right]$$
