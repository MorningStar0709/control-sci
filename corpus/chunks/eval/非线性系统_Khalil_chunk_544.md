# C. 23 证明定理 14.6

出于分析的需要,我们把观测器的动力学方程用与其等价的尺度估计误差动力学方程

$$\eta_ {i j} = \frac {x _ {i j} - \hat {x} _ {i j}}{\varepsilon^ {\rho_ {i} - j}}$$

代替,其中 $1 \leqslant i \leqslant m, 1 \leqslant j \leqslant \rho_{i}$ 。因此有 $\hat{x} = x - D(\varepsilon)\eta$ , 其中

$$
\begin{array}{l} \eta = \left[ \eta_ {1 1}, \dots , \eta_ {1 \rho_ {1}}, \dots , \eta_ {m 1}, \dots , \eta_ {m \rho_ {m}} \right] ^ {\mathrm{T}} \\ D (\varepsilon) = \text { block   diag } [ D _ {1}, \dots , D _ {m} ] \\ D _ {i} = \operatorname{diag} [ \varepsilon^ {\rho_ {i} - 1}, \dots , 1 ] _ {\rho_ {i} \times \rho_ {i}} \\ \end{array}
$$

闭环系统表示为 $\dot{x} = Ax + B\phi(x, z, \gamma(\vartheta, x - D(\varepsilon)\eta, \zeta))$

$$\dot {z} = \psi (x, z, \gamma (\vartheta , x - D (\varepsilon) \eta , \zeta))\dot {\vartheta} = \Gamma (\vartheta , x - D (\varepsilon) \eta , \zeta)\varepsilon \dot {\eta} = A _ {0} \eta + \varepsilon B \delta (x, z, \vartheta , D (\varepsilon) \eta)$$

其中 $\delta(x,z,\vartheta,D(\varepsilon)\eta)=\phi(x,z,\gamma(\vartheta,\hat{x},\zeta))-\phi_{0}(\hat{x},\zeta,\gamma(\vartheta,\hat{x},\zeta))$

$(1/\varepsilon)A_{0}=D^{-1}(\varepsilon)(A-HC)D(\varepsilon)$ 是 $\rho\times\rho$ 赫尔维茨矩阵,为方便,将系统改写为紧奇异扰动形式 $\dot{\mathcal{X}} = F(\mathcal{X}, D(\varepsilon)\eta)$ (C.94)

$$\varepsilon \dot {\eta} = A _ {0} \eta + \varepsilon B \Delta (\mathcal {X}, D (\varepsilon) \eta) \tag {C.95}$$

其中 $F(\mathcal{X},0) = f(\mathcal{X})$ 。初始状态为 $\mathcal{X}(0) = (x(0),z(0),\vartheta (0))\in \mathcal{S},\hat{x} (0)\in \mathcal{Q}$ 。因此有 $\eta (0)$ $= D^{-1}(\varepsilon)[x(0) - \hat{x} (0)]$ ，在式(C.95)中设定 $\varepsilon = 0$ ，则 $\eta = 0$ ，并得到降价系统

$$\dot {\mathcal {X}} = f (\mathcal {X}) \tag {C.96}$$

这正是状态反馈下的闭环系统。运用时间变量代换 $\tau = t / \varepsilon$ ，然后设定 $\varepsilon = 0$ ，可得边界层模型

$$\frac {d \eta}{d \tau} = A _ {0} \eta$$

由于系统(C.96)的原点是渐近稳定的,且R是其吸引区,根据(逆李雅普诺夫)定理4.17,存在一个光滑正定函数 $V(\mathcal{X})$ 及连续正定函数 $U(\mathcal{X})$ ,都对于 $\mathcal{X}\in\mathcal{R}$ 有定义,满足

$$
\begin{array}{l} V (\mathcal {X}) \rightarrow \infty \text {   as   } \mathcal {X} \rightarrow \partial \mathcal {R} \\ \frac {\partial V}{\partial \mathcal {X}} f (\mathcal {X}) \leqslant - U (\mathcal {X}), \quad \forall \mathcal {X} \in \mathcal {R} \\ \end{array}
$$
