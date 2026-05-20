# 14.5.1 启发性例子

考虑二阶非线性系统

$$\dot {x} _ {1} = x _ {2} \tag {14.88}\dot {x} _ {2} = \phi (x, u) \tag {14.89}y = x _ {1} \tag {14.90}$$

其中， $x = [x_{1},x_{2}]^{\mathrm{T}}$ 。假设 $u = \gamma (x)$ 是局部利普希茨状态反馈控制律，能使闭环系统

$$\dot {x} _ {1} = x _ {2} \tag {14.91}\dot {x} _ {2} = \phi (x, \gamma (x)) \tag {14.92}$$

在原点 x=0 稳定。为了只利用输出 y 的测量值实现该反馈控制，利用观测器

$$\dot {\hat {x}} _ {1} = \hat {x} _ {2} + h _ {1} (y - \hat {x} _ {1}) \tag {14.93}\dot {\hat {x}} _ {2} = \phi_ {0} (\hat {x}, u) + h _ {2} (y - \hat {x} _ {1}) \tag {14.94}$$

其中 $\phi_0(x,u)$ 是非线性函数 $\phi (x,u)$ 的标称模型。估计误差

$$
\tilde {x} = \left[ \begin{array}{l} \tilde {x} _ {1} \\ \tilde {x} _ {2} \end{array} \right] = \left[ \begin{array}{l} x _ {1} - \hat {x} _ {1} \\ x _ {2} - \hat {x} _ {2} \end{array} \right]
$$

满足方程

$$\dot {\tilde {x}} _ {1} = - h _ {1} \tilde {x} _ {1} + \tilde {x} _ {2} \tag {14.95}\dot {\tilde {x}} _ {2} = - h _ {2} \tilde {x} _ {1} + \delta (x, \tilde {x}) \tag {14.96}$$

这里 $\delta (x,\tilde{x} = \phi (x,\gamma (\hat{x})) - \phi_0(\hat{x},\gamma (\hat{x}))$ 。我们想要设计的观测器增益是 $H = [h_1,h_2]^{\mathrm{T}}$ ，使 $\lim_{t\to \infty}\tilde{x} (t) = 0$ 。在无扰动项 $\delta$ 的情况下，设计 $H$ 使

$$
A _ {o} = \left[ \begin{array}{l l} - h _ {1} & 1 \\ - h _ {2} & 0 \end{array} \right]
$$

为赫尔维茨矩阵,就能实现渐近误差的收敛。该二阶系统对于任意正常数 $h_{1}$ 和 $h_{2}$ , 矩阵 $A_{o}$ 都是赫尔维茨的。在存在 $\delta$ 的情况下, 设计 H 时还要考虑抵消 $\delta$ 对 $\tilde{x}$ 的作用。对于任何 $\delta$ , 如果从 $\delta$ 到 $\tilde{x}$ 的传递函数

$$
G _ {o} (s) = \frac {1}{s ^ {2} + h _ {1} s + h _ {2}} \left[ \begin{array}{c} 1 \\ s + h _ {1} \end{array} \right]
$$

恒等于零,即可理想地实现上述目标。虽然这是不可能的,但可以选择 $h_{2}\gg h_{1}\gg1$ ,使 $\sup_{\omega\in R}|G_{o}(j\omega)|$ 任意小。特别地,取

$$h _ {1} = \frac {\alpha_ {1}}{\varepsilon}, \quad h _ {2} = \frac {\alpha_ {2}}{\varepsilon^ {2}} \tag {14.97}$$

其中 $\alpha_{1},\alpha_{2}$ 和 $\varepsilon$ 为正常数，且 $\varepsilon \ll 1$ ，可以证明

$$
G _ {o} (s) = \frac {\varepsilon}{(\varepsilon s) ^ {2} + \alpha_ {1} \varepsilon s + \alpha_ {2}} \left[ \begin{array}{c} \varepsilon \\ \varepsilon s + \alpha_ {1} \end{array} \right]
$$

因此有 $\lim_{\varepsilon\to0}G_{o}(s)=0$ 。高增益观测器的扰动抑制特性也可以在时域理解，只要将误差方程(14.95)～(14.96)表示为奇异扰动形式即可。为此，换算估计误差为

$$\eta_ {1} = \frac {\tilde {x} _ {1}}{\varepsilon}, \quad \eta_ {2} = \tilde {x} _ {2} \tag {14.98}$$

新定义的变量满足奇异扰动方程

$$\varepsilon \dot {\eta} _ {1} = - \alpha_ {1} \eta_ {1} + \eta_ {2} \tag {14.99}\varepsilon \dot {\eta} _ {2} = - \alpha_ {2} \eta_ {1} + \varepsilon \delta (x, \tilde {x}) \tag {14.100}$$
