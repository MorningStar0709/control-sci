其中 $\phi (x) = \sqrt{\alpha_3(\| x\|_2)}$ 。设 $\eta (x) = \eta_0 + \eta_1\phi (x),\eta_0\geqslant \rho_0 / (1 - k_0),\eta_1\geqslant \rho_1 / (1 - \kappa_0)$ 。考虑反馈控制

$$
v = \left\{ \begin{array}{l l} - [ \eta_ {0} + \eta_ {1} \phi (x) ] (w / \| w \| _ {2}), & \| w \| _ {2} \geqslant \varepsilon \\ - [ \eta_ {0} + \eta_ {1} \phi (x) ] (w / \varepsilon), & \| w \| _ {2} <   \varepsilon \end{array} \right.
$$

(a) 证明 $V$ 沿闭环系统(14.38)轨线的导数满足

$$\dot {V} \leqslant - \phi^ {2} (x) + \frac {\varepsilon}{4} [ \rho_ {0} + \rho_ {1} \phi (x) ] \leqslant - \frac {1}{2} \alpha_ {3} (\| x \| _ {2}) + \frac {\varepsilon^ {2} \rho_ {1} ^ {2}}{3 2} + \frac {\varepsilon \rho_ {0}}{4}$$

(b) 应用定理 4.18 推出类似于定理 14.3 的结论。  
(c) 把该控制器与式(14.41)进行比较。

14.24 考虑 14.2 节中讨论的问题, 并假设式(14.35)在 2 范数下成立, 进一步假设式(14.44)和式(14.46)也成立。证明控制律

$$u = \psi (t, x) - \gamma w; \quad w ^ {\mathrm{T}} = \frac {\partial V}{\partial x} G (t, x)$$

对足够大的 $\gamma$ ，仍能稳定原点。

14.25 考虑 14.2 节讨论的问题,证明不采用控制律 $u = \psi(t, x) + v$ , 而是简单地采用 u = v 也可以实现, 其中 $\rho(t, x)$ 满足不等式

$$\| \delta (t, x, u) - \psi (t, x) \| _ {2} \leqslant \rho (t, x) + \kappa_ {0} \| u \| _ {2}, 0 \leqslant \kappa_ {0} < 1$$

14.26 除匹配的不确定项 $\delta$ 外, 假设系统(14.30)还有未匹配不确定项 $\Delta$ , 即

$$\dot {x} = f (t, x) + \Delta (t, x) + G (t, x) [ u + \delta (t, x, u) ]$$

假设在定义域 $D \subset R^n$ 上, 定理 14.3 的所有假设以及不等式 (14.44) 到不等式 (14.46) 都成立, 对某个 $\mu \geqslant 0$ 不匹配的不确定项满足 $\| [\partial V / \partial x] \Delta(t, x) \|_2 \leqslant \mu \phi^2(x)$ 。设 $u = \psi(t, x) + v$ , 其中 $v$ 由式 (14.41) 确定。证明如果 $\mu < 1$ , 则反馈控制律将稳定闭环系统的原点, 其中 $\varepsilon$ 足够小, 满足 $\varepsilon < 4(1 - \mu)(1 - \kappa_0) \eta_0^2 / \rho_1^2$ 。

14.27 考虑系统 $\dot{x}=f(x)+G(x)[u+\delta(x,u)]$ ，并假设存在已知的光滑函数 $\psi(x)$ ， $V(x)$ 和 $\rho(x)$ ，它们都在 x=0 时为零，另存在一个已知常数 k 满足

$$c _ {1} \| x \| ^ {2} \leqslant V (x) \leqslant c _ {2} \| x \| ^ {2}, \quad {\frac {\partial V}{\partial x}} [ f (x) + G (x) \psi (x) ] \leqslant - c _ {3} \| x \| ^ {2}\| \delta (x, \psi (x) + v) \| \leqslant \rho (x) + \kappa_ {0} \| v \|, 0 \leqslant \kappa_ {0} < 1, \quad \forall x \in R ^ {n}, \forall v \in R ^ {p}$$

其中 $c_{1}$ 到 $c_{3}$ 是正常数。

(a) 证明可能设计一个连续状态反馈控制器 $u = \gamma(x)$ , 使得

$$\dot {x} = f (x) + G (x) [ \gamma (x) + \delta (x, \gamma (x)) ]$$

的原点达到全局渐近稳定。

(b) 将(a)中的结果用于系统

$$\dot {x} _ {1} = x _ {2}, \quad \dot {x} _ {2} = (1 + a _ {1}) (x _ {1} ^ {3} + x _ {2} ^ {3}) + (1 + a _ {2}) u$$

其中 $a_{1}$ 和 $a_{2}$ 是未知常数，满足 $\left|a_{1}\right|\leqslant1,\left|a_{2}\right|\leqslant1/2$ 。
