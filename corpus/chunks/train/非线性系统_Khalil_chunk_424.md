$$
\begin{array}{l} \dot {z} = f _ {0} (z + \eta_ {\mathrm{ss}}, \xi , w) \stackrel {\text { def }} {=} \tilde {f} _ {0} (z, e, w, r) \\ \dot {e} _ {0} = e _ {1} \\ \dot {e} _ {1} = e _ {2} \\ \begin{array}{c c} \vdots & \vdots \\ \vdots & \vdots \\ \vdots & \vdots \end{array} \\ \dot {e} _ {\rho - 1} = e _ {\rho} \\ \dot {e} _ {\rho} = L _ {f} ^ {\rho} h (x) + L _ {\delta_ {1}} L _ {f} ^ {\rho - 1} h (x, w) + L _ {g} L _ {f} ^ {\rho - 1} h (x, w) [ u + \delta (x, u, w) ] \\ \end{array}
$$

保持系统为由 $\rho+1$ 个积分器组成的标称形式结构。因此，滑模控制的设计可以采用上一节的方法，特别是可取

$$s = k _ {0} e _ {0} + k _ {1} e _ {1} + \dots + k _ {\rho - 1} e _ {\rho - 1} + e _ {\rho}$$

选择 $k_{0}$ 到 $k_{\rho-1}$ ，使多项式 $s^{\rho} + k_{\rho-1}s^{\rho-1} + \cdots + k_{1}s + k_{0}$

为赫尔维茨的,则

$$\dot {s} = k _ {0} e _ {1} + \dots + k _ {\rho - 1} e _ {\rho} + L _ {f} ^ {\rho} h (x) + L _ {\delta_ {1}} L _ {f} ^ {\rho - 1} h (x, w) + L _ {g} L _ {f} ^ {\rho - 1} h (x, w) [ u + \delta (x, u, w) ]$$

控制律 u 可取为

$$u = v \quad \text {或} \quad u = - \frac {1}{L _ {\hat {g}} L _ {f} ^ {\rho - 1} h (x)} \left[ k _ {0} e _ {1} + \dots + k _ {\rho - 1} e _ {\rho} + L _ {f} ^ {\rho} h (x) \right] + v$$

这里 $\hat{g}(x)$ 是 $g(x,w)$ 的标称模型, 可得

$$\dot {s} = L _ {g} L _ {f} ^ {\rho - 1} h (x, w) v + \Delta (x, v, w, r)$$

如果 $\left|\frac{\Delta(x,v,w,r)}{L_gL_f^{\rho - 1}h(x,w)}\right| \leqslant \varrho (x) + \kappa_0|v|, \quad 0 \leqslant \kappa_0 < 1$

对于所有 $(x,v,w,r)\in D\times R\times D_{w}\times D_{r}$ ，有 $\varrho$ 和 $\kappa_{0}$ 已知，v可取为

$$v = - \beta (x) \operatorname{sat} \left(\frac {s}{\varepsilon}\right)$$

其中 $\beta (x)\geqslant \varrho (x) / (1 - \kappa_0) + \beta_0,\beta_0 > 0$ 。闭环系统在 $(z,e_0,e) = (0,\bar{e}_0,0)$ 处有一个平衡点，该平衡点的收敛性可利用14.1.2节的方法证明。特别是对于系统 $\dot{z} = \tilde{f}_0(z,e,w,r)$ ，存在李雅普诺夫函数 $V_{1}(z,w,r)$ ，使得对于某些K类函数 $\tilde{\alpha}_{1},\tilde{\alpha}_{2},\tilde{\alpha}_{3}$ 和 $\tilde{\gamma}$ ，在 $(w,r)$ 上一致满足不等式

$$\tilde {\alpha} _ {1} (\| z \|) \leqslant V _ {1} (z, w, r) \leqslant \tilde {\alpha} _ {2} (\| z \|)\frac {\partial V _ {1}}{\partial z} \tilde {f} _ {0} (z, e, w, r) \leqslant - \tilde {\alpha} _ {3} (\| z \|), \quad \forall \| z \| \geqslant \tilde {\gamma} (\| e \|)$$

则可以证明存在两个正不变紧集 $\Omega$ 和 $\Omega_{\varepsilon}$ ，使得始于 $\Omega$ 的每条轨线都能在有限时间内进入 $\Omega_{\varepsilon}$ 。构造集合 $\Omega$ 和 $\Omega_{\varepsilon}$ 需要三个步骤。首先，把闭环系统写为如下形式：

$$\dot {z} = \tilde {f} _ {0} (z, e, w, r)\dot {\zeta} = A \zeta + B s\dot {s} = - \left(L _ {g} L _ {f} ^ {\rho - 1} h\right) \beta \operatorname{sat} \left(\frac {s}{\varepsilon}\right) + \Delta$$
