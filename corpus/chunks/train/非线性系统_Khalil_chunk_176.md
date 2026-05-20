当作用到包含执行部件动态特性的执行系统时,该控制能达到设计目标吗?这是关于控制器对未建模执行部件的动力学因素①的鲁棒性问题。当该控制用于实际系统时,闭环方程为

$$\dot {x} = f (t, x, C z + d _ {1} (t))\varepsilon \dot {z} = A z + B [ \gamma (t, x) + d _ {2} (t) ]$$

假设 $d_{2}(t)$ 是可微的，且 $\dot{d}_2\in \mathcal{L}$ 。进行变量代换

$$\eta = z + A ^ {- 1} B [ \gamma (t, x) + d _ {2} (t) ]$$

闭环系统变为 $\dot{x} = f(t, x, \gamma(t, x) + d(t) + C\eta)$

$$\varepsilon \dot {\eta} = A \eta + \varepsilon A ^ {- 1} B [ \dot {\gamma} + \dot {d} _ {2} (t) ]$$

其中 $\dot{\gamma}=\frac{\partial\gamma}{\partial t}+\frac{\partial\gamma}{\partial x}f(t,x,\gamma(t,x)+d(t)+C\eta)$

不难发现,闭环系统可由图5.1表示,其中 $H_{1}$ 定义为

$$\dot {x} = f (t, x, \gamma (t, x) + e _ {1})y _ {1} = \dot {\gamma} = \frac {\partial \gamma}{\partial t} + \frac {\partial \gamma}{\partial x} f (t, x, \gamma (t, x) + e _ {1})$$

$H_{2}$ 定义为 $\dot{\eta} = \frac{1}{\varepsilon} A \eta + A^{-1} B e_{2}$

$$y _ {2} = - C \eta$$

且 $u_{1}=d_{1}+d_{2}=d,\quad u_{2}=\dot{d}_{2}$

在上述表达式中,系统 $H_{1}$ 为标称降阶闭环系统,而 $H_{2}$ 代表未建模动力学因素的作用。设定 $\varepsilon=0$ ,打开环路,并使整个闭环系统简化为标称系统。假设反馈函数 $\gamma(t,x)$ 对所有 $(t,x,e_{1})$ 满足不等式

$$\left\| \frac {\partial \gamma}{\partial t} + \frac {\partial \gamma}{\partial x} f (t, x, \gamma (t, x) + e _ {1}) \right\| \leqslant c _ {1} \| x \| + c _ {2} \| e _ {1} \| \tag {5.43}$$

其中 $c_{1}$ 和 $c_{2}$ 为非负常数。由式(5.42)和式(5.43)可证明

$$\left\| y _ {1} \right\| _ {\mathcal {L}} \leqslant \gamma_ {1} \left\| e _ {1} \right\| _ {\mathcal {L}} + \beta_ {1}$$

其中 $\gamma_{1}=c_{1}\gamma+c_{2},\quad\beta_{1}=c_{1}\beta$

由于 $H_{2}$ 为线性时不变系统， $A$ 为赫尔维茨矩阵，应用推论5.2可证明，对于任意 $p \in [1, \infty]$ ， $H_{2}$ 为有限增益 $\mathcal{L}_p$ 稳定的，同时

$$\| y _ {2} \| _ {\mathcal {L}} \leqslant \gamma_ {2} \| e _ {2} \| _ {\mathcal {L}} + \beta_ {2} \stackrel {\text { def }} {=} \varepsilon \gamma_ {f} \| e _ {2} \| _ {\mathcal {L}} + \beta_ {2}$$

其中 $\gamma_{f} = \frac{2\lambda_{max}^{2}(Q)\|A^{-1}B\|_{2}\|C\|_{2}}{\lambda_{min}(Q)},\beta_{2} = \rho \| C\|_{2}\| \eta (0)\| \sqrt{\frac{\lambda_{max}(Q)}{\lambda_{min}(Q)}}$

$$
\rho = \left\{ \begin{array}{l l} 1, & p = \infty \\ \left(\frac {2 \varepsilon \lambda_ {m a x} (Q)}{p}\right) ^ {1 / p}, & p \in [ 1, \infty) \end{array} \right.
$$

且 $Q$ 为李雅普诺夫方程 $QA + A^{\mathrm{T}}Q = -I^{①}$ 的解。因此，假设存在明确定义的反馈连接，由小增益定理可推得，如果 $\varepsilon \gamma_{1}\gamma_{f} < 1$ ，则从 $u$ 到 $e$ 的输入-输出映射是 $\mathcal{L}$ 稳定的。由式(5.40)有
