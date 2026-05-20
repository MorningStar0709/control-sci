$$\frac {\partial \Phi}{\partial t} = - \min _ {u} \left\{\frac {1}{2} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right) + \frac {\partial \Phi}{\partial x} (f (x) + g (x) u) \right\}. \tag {6.7.15}$$

又因为 $\Phi(x) = -V(x)$ , 且有 $\frac{\partial \Phi}{\partial t} = 0$ , 所以根据上式得

$$
\begin{array}{l} \min _ {u} \left\{\frac {1}{2} \left(\gamma^ {2} \| u \| ^ {2} - \| y \| ^ {2}\right) + \frac {\partial \Phi}{\partial x} (f (x) + g (x) u) \right\} \\ = - \frac {\partial V}{\partial x} f (x) - \frac {1}{2 \gamma^ {2}} \frac {\partial V}{\partial x} g (x) g ^ {T} (x) \left(\frac {\partial^ {T} V}{\partial x}\right) - \frac {1}{2} h ^ {T} (x) h (x) = 0. \\ \end{array}
$$

因此定理6.7.1成立，充分性得证.

现在我们描述非线性系统的 $H_{\infty}$ 标准设计问题，设广义受控对象为

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + g _ {1} (x) w + g _ {2} (x) u, \\ z = h _ {1} (x) + d _ {1 2} (x) u, \\ y = h _ {2} (x) + d _ {2 1} (x) w, \end{array} \right. \tag {6.7.16}
$$

其中 $w \in \mathbb{R}^{p_1}, u \in \mathbb{R}^{p_2}$ 分别为广义干扰输入和控制输入信号， $z \in \mathbb{R}^{q_1}, y \in \mathbb{R}^{q_2}$ 分别表示评价信号和可检测输出信号， $f, g_1, g_2, h_1, h_2, d_{12}, d_{21}$ 则分别是相应维数的函数向量或矩阵，且 $f(0) = 0$ 。所谓 $H_\infty$ 标准设计问题就是求静态反馈控制器

$$u = \alpha (y), \quad \alpha (0) = 0, \tag {6.7.17}$$

或者动态反馈控制器

$$u = \alpha (\xi , y), \quad \dot {\xi} = \beta (\xi , y), \tag {6.7.18}$$

使得闭环系统满足如下性能指标：

(H1) 当 $w = 0, \forall t \geqslant 0$ 时，闭环系统在原点是渐近稳定的；

(H2) 闭环系统具有小于 1 的 $L^2$ 增益.

沿用线性系统的术语，我们称满足上述条件的控制器为 $H_{\infty}$ 控制器.

在最后两节，我们将介绍几种 $H_{\infty}$ 标准设计问题的解法。应该指出，为了叙述简便，我们不特别指出系统的稳定域以及在输入信号激励下内部状态轨迹的存在域。这就是说我们不再详细区分所讨论的问题是否具有全局或局部的属性。读者可根据内容自行判别。
