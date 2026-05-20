$$\dot {\vartheta} = \Gamma (\vartheta , x, \zeta) \tag {14.107}u = \gamma (\vartheta , x, \zeta) \tag {14.108}$$

其中 $\gamma$ 和 $\Gamma$ 在定义域内是其自变量的局部利普希茨函数, 是 x 的全局有界函数, 且有 $\gamma(0,0,0)=0$ , $\Gamma(0,0,0)=0$ 。去掉 $\dot{\vartheta}$ 方程后, 把静态状态反馈控制器 $u=\gamma(x,\zeta)$ 看成上述方程的特例。为了方便起见, 将状态反馈下的闭环系统表示为

$$\dot {\mathcal {X}} = f (\mathcal {X}) \tag {14.109}$$

其中 $\mathcal{X}=(x,z,\vartheta)$ 。输出反馈控制器取为

$$\dot {\vartheta} = \Gamma (\vartheta , \hat {x}, \zeta) \tag {14.110}u = \gamma (\vartheta , \hat {x}, \zeta) \tag {14.111}$$

其中 $\hat{x}$ 由高增益观测器

$$\dot {\hat {x}} = A \hat {x} + B \phi_ {0} (\hat {x}, \zeta , u) + H (y - C \hat {x}) \tag {14.112}$$

产生。选择观测器的增益 H 为

$$
H = \text { block   diag } [ H _ {1}, \dots , H _ {m} ], \quad H _ {i} = \left[ \begin{array}{c} \alpha_ {1} ^ {i} / \varepsilon \\ \alpha_ {2} ^ {i} / \varepsilon^ {2} \\ \vdots \\ \alpha_ {\rho_ {i} - 1} ^ {i} / \varepsilon^ {\rho_ {i} - 1} \\ \alpha_ {\rho_ {i}} ^ {i} / \varepsilon^ {\rho_ {i}} \end{array} \right] _ {\rho_ {i} \times 1} \tag {14.113}
$$

其中 $\varepsilon$ 是指定的正常数,选择正常数 $\alpha_{i}^{i}$ ,使得对于所有 $i=1,\cdots,m$ ,方程

$$s ^ {\rho_ {i}} + \alpha_ {1} ^ {i} s ^ {\rho_ {i} - 1} + \dots + \alpha_ {\rho_ {i} - 1} ^ {i} s + \alpha_ {\rho_ {i}} ^ {i} = 0$$

的根在左半开平面, 函数 $\phi_{0}(x,\zeta,u)$ 是 $\phi(x,z,u)$ 的标称模型, 要求在定义域内对其自变量是局部利普希茨的, 对 x 全局有界, 且有 $\phi_{0}(0,0,0)=0$ 。

定理 14.6 考虑闭环系统(14.103)～(14.106)和输出反馈控制器(14.110)～(14.112)。假设方程(14.109)的原点是渐近稳定的，且R是其吸引区，设S是R内的任意紧集，Q是 $R^{p}$ 的任意紧子集，则

- 存在 $\varepsilon_{1}^{*} > 0$ ，使得对于每个 $0 < \varepsilon \leqslant \varepsilon_{1}^{*}$ ，闭环系统始于 $\mathcal{S} \times \mathcal{Q}$ 内的解 $(\mathcal{X}(t), \hat{x}(t))$ ，对于所有 $t \geqslant 0$ 都是有界的。  
- 任意给定 $\mu > 0$ , 存在 $\varepsilon_{2}^{*} > 0$ 和 $T_{2} > 0$ , 二者都与 $\mu$ 有关, 使得对于每个 $0 < \varepsilon \leqslant \varepsilon_{2}^{*}$ , 闭环系统始于 $S \times Q$ 内的解. 满足

$$\| \mathcal {X} (t) \| \leqslant \mu , \quad \| \hat {x} (t) \| \leqslant \mu , \quad \forall t \geqslant T _ {2} \tag {14.114}$$

\- 任意给定 $\mu > 0$ ，存在 $\varepsilon_3^* > 0$ ，与 $\mu$ 有关，使得对于每个 $0 < \varepsilon \leqslant \varepsilon_3^*$ ，闭环系统始于 $S \times Q$ 内的解，满足

$$\| \mathcal {X} (t) - \mathcal {X} _ {r} (t) \| \leqslant \mu , \quad \forall t \geqslant 0 \tag {14.115}$$

其中 $\chi_{r}$ 是式(14.109)始于 $\chi(0)$ 的解。
