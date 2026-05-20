# 6.8 非线性 $H_{\infty}$ 控制器设计方法

根据上节讨论可知，在一定的条件下，一个非线性系统具有小于 $\gamma$ 的 $L^2$ 增益，当且仅当该系统是 $\gamma-$ 耗散的，或等价地Hamilton-Jacobi偏微分方程具有半正定解。因此，如果我们能够得到使闭环系统具有 $\gamma-$ 耗散性的反馈控制器，并且当干扰信号为零时该控制器能够保证平衡点的渐近稳定性，那么该控制器就是 $H_{\infty}$ 标准设计问题的解。在本节我们将看到，只要广义受控对象满足一定的零状态能检测条件，就可以通过这种途径得到 $H_{\infty}$ 标准设计问题的解。

首先考虑静态状态反馈问题，即设广义受控对象 (6.7.16) 满足

$$y = x, \quad h _ {2} (x) - x, \quad d _ {2 1} (x) = 0, \tag {6.8.1}$$

求状态反馈控制器

$$u = \alpha (x), \tag {6.8.2}$$

使得闭环系统满足上一节描述的性能指标 (H1) 和 (H2).

定理 6.8.1 设广义受控对象 (6.7.16) 满足

$$d _ {1 2} ^ {\mathrm{T}} (x) [ d _ {1 2} (x) h _ {1} (x) ] = [ I \quad 0 ], \tag {6.8.3}$$

则对于给定的 $\gamma > 0$ , 存在状态反馈控制器 (6.8.2), 使得闭环系统是 $\gamma$ -耗散的充分必要条件是如下给定的 Hamilton-Jacobi 偏微分不等式具有半正定解 $V(x)$ :

$$\frac {\partial V}{\partial x} f (x) + \frac {1}{2} \frac {\partial V}{\partial x} \left\{\frac {1}{\gamma^ {2}} g _ {1} (x) g _ {1} ^ {\mathrm{T}} (x) - g _ {2} (x) g _ {2} ^ {\mathrm{T}} (x) \right\} \frac {\partial^ {\mathrm{T}} V}{\partial x} + \frac {1}{2} h _ {1} ^ {\mathrm{T}} (x) h _ {1} (x) \leqslant 0, \quad \forall x. \tag {6.8.4}$$

如果上式存在半正定解 $V(x)$ , 则使得闭环系统是 $\gamma-$ 耗散的状态反馈控制器给定如下:

$$u = \alpha (x) = - g _ {2} ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x}. \tag {6.8.5}$$

证明 充分性 设 Hamilton-Jacobi 偏微分不等式 (6.8.4) 有半正定解 $V(x)$ . 利用不等式 (6.8.4), 得

$$
\begin{array}{l} \dot {V} = \frac {\partial V}{\partial x} (f (x) + g _ {1} (x) w + g _ {2} (x) u) \\ \leqslant - \frac {1}{2 \gamma^ {2}} \frac {\partial V}{\partial x} g _ {1} (x) g _ {1} ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x} + \frac {1}{2} \frac {\partial V}{\partial x} g _ {2} (x) g _ {2} ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x} \\ + \frac {\partial V}{\partial x} g _ {2} (x) u + \frac {\partial V}{\partial x} g _ {1} (x) w - \frac {1}{2} h _ {1} ^ {T} (x) h _ {1} (x) \\ = - \frac {1}{2} \left\| \frac {1}{\gamma} g _ {1} ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x} - \gamma w \right\| ^ {2} + \frac {1}{2} \left\| g _ {2} ^ {\mathrm{T}} (x) \frac {\partial^ {\mathrm{T}} V}{\partial x} + u \right\| ^ {2} \\ + \frac {\gamma^ {2}}{2} \| w \| ^ {2} - \frac {1}{2} \| u \| ^ {2} - \frac {1}{2} h _ {1} ^ {\mathrm{T}} (x) h _ {1} (x). \tag {6.8.6} \\ \end{array}
$$

因此，设反馈控制律由式 $(6.8.5)$ 给定，则有
