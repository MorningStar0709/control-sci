# 14.1.4 积分控制调节

考虑单输入-单输出系统

$$\dot {x} = f (x) + \delta_ {1} (x, w) + g (x, w) [ u + \delta (x, u, w) ] \tag {14.25}y = h (x) \tag {14.26}$$

其中， $x \in R^{n}$ 是状态， $u \in R$ 是控制输入， $y \in R$ 是受控输出， $w \in R^{l}$ 是由未知的不变参数和扰动组成的向量。对于 $x \in D \subset R^{n}, u \in R$ 和 $w \in D_{w} \subset R^{l}$ ，函数 $f, g, h, \delta$ 和 $\delta_{1}$ 对 $(x, u)$ 充分光滑，对 $w$ 是连续的，其中 $D$ 和 $D_{w}$ 是开连通集。假设系统

$$\dot {x} = f (x) + g (x, w) u \tag {14.27}y = h (x) \tag {14.28}$$

在 D 内, 相对阶 $\rho$ 对 w 一致, 即对于所有 $(x, w) \in D \times D_{w}$ , 有

$$L _ {g} h (x, w) = \dots = L _ {g} L _ {f} ^ {\rho - 2} h (x, w) = 0, \quad L _ {g} L _ {f} ^ {\rho - 1} h (x, w) \geqslant a > 0$$

我们的目标是设计一个状态反馈控制律,使得输出 y 渐近跟踪一个不变的参考信号 $r \in D_{r} \subset R$ , 其中 $D_{r}$ 是开连通集。这是前一节介绍的跟踪问题的一个特例, 即参考信号是常数, 不确定项以 $w$ 为参数, 因此可以采用前一节所述的滑模控制器实现。当符号函数 $\operatorname{sgn}(s)$ 由饱和函数 $\operatorname{sat}(s / \varepsilon)$ 逼近时, 调节误差是毕竟有界的, 其边界值为常数 $k\varepsilon, k > 0$ 。这是一般跟踪问题所能达到的最好结果, 但在调节问题中可以利用积分控制达到零稳态误差。我们继续12.3节的讨论, 为系统增加对调节误差 $y - r$ 的积分, 设计一个反馈控制器, 使增广系统在平衡点 $y = r$ 处稳定。为此, 假设对于每对 $(r, w) \in D_r \times D_w$ , 存在唯一的 $(x_{ss}, u_{ss})$ , 连续依赖于 $(r, w)$ , 且满足

方程组 $0 = f(x_{\mathrm{ss}}) + \delta_1(x_{\mathrm{ss}},w) + g(x_{\mathrm{ss}},w)[u_{\mathrm{ss}} + \delta (x_{\mathrm{ss}},u_{\mathrm{ss}},w)]$

$$r = h \left(x _ {\mathrm{ss}}\right)$$

使得 $x_{ss}$ 是期望的平衡点， $u_{ss}$ 是系统在点 $x_{ss}$ 保持平衡所要求的稳态控制。假设

$$\frac {\partial (L _ {f} ^ {i} h)}{\partial x} \delta_ {1} (x, w) = 0, \quad 1 \leqslant i \leqslant \rho - 2, \quad \forall (x, w) \in D \times D _ {w}$$

通过变量代换(14.23)将系统(14.25)\~(14.26)转换为标称形式

$$
\begin{array}{l} \dot {\eta} = f _ {0} (\eta , \xi , w) \\ \dot {\xi} _ {1} = \xi_ {2} \\ \vdots \quad \vdots \\ \dot {\xi} _ {\rho - 1} = \xi_ {\rho} \\ \dot {\xi} _ {\rho} = L _ {f} ^ {\rho} h (x) + L _ {\delta_ {1}} L _ {f} ^ {\rho - 1} h (x, w) + L _ {g} L _ {f} ^ {\rho - 1} h (x, w) [ u + \delta (x, u, w) ] \\ y = \xi_ {1} \\ \end{array}
$$

并将平衡点 $x_{ss}$ 映射到 $(\eta_{\mathrm{ss}}, \xi_{\mathrm{ss}})$ ，其中 $\xi_{ss} = [r, 0, \cdots, 0]^{T}$ 。前述方程的积分器增强为

$$\dot {e} _ {0} = y - r$$

运用变量代换 $z = \eta -\eta_{\mathrm{ss}},\quad e = \left[ \begin{array}{c}e_{1}\\ e_{2}\\ \vdots \\ e_{\rho} \end{array} \right] = \left[ \begin{array}{c}\xi_{1} - r\\ \xi_{2}\\ \vdots \\ \xi_{\rho} \end{array} \right]$

可得到增广系统
