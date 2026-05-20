$f(\tau ,x)$ 是以 $2\pi$ 为周期的 $\tau$ 的函数。平均系统为

$$\frac {d x}{d \tau} = \varepsilon f _ {\mathrm{av}} (x) \tag {10.32}$$

其中 $f_{\mathrm{av1}}(x) = \frac{1}{2\pi}\int_0^{2\pi}f_1(\tau ,x)d\tau = x_2$

$$f _ {\mathrm{av} 2} (x) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} f _ {2} (\tau , x) d \tau = - \alpha \beta x _ {2} - \alpha^ {2} \sin x _ {1} - \frac {1}{4} \sin 2 x _ {1}$$

在推导上述表达式时,用到 $\cos\tau$ 的平均值为 0, 而 $\cos^{2}\tau$ 的平均值为 1/2。原系统 (10.31) 和平均系统 (10.32) 的平衡点都在 $(x_{1}=0, x_{2}=0)$ 和 $(x_{1}=\pi, x_{2}=0)$ , 这与悬摆的平衡位置 $\theta=0$ 和 $\theta=\pi$ 相对应。当悬点固定时, 平衡位置 $\theta=0$ 是指数稳定的, 而平衡位置 $\theta=\pi$ 是非稳定的。现在研究悬点振动着的系统特性。应用定理 10.4, 通过线性化方法分析平均系统 (10.32) 的平衡点的稳定性。 $f_{\mathrm{av}}(x)$ 的雅可比矩阵为

$$
\frac {\partial f _ {\mathrm{av}}}{\partial x} = \left[ \begin{array}{c c} 0 & 1 \\ - \alpha^ {2} \cos x _ {1} - 0. 5 \cos 2 x _ {1} & - \alpha \beta \end{array} \right]
$$

在平衡点 $(x_{1} = 0, x_{2} = 0)$ ，雅可比矩阵

$$
\left[ \begin{array}{c c} 0 & 1 \\ - \alpha^ {2} - 0. 5 & - \alpha \beta \end{array} \right]
$$

对于所有正的 $\alpha$ 和 $\beta$ 是赫尔维茨的。因此定理10.4表明，对于足够小的 $\varepsilon$ ，原系统(10.31)在原点的 $O(\varepsilon)$ 邻域内有唯一的以 $2\pi$ 为周期的指数稳定解。因为原点是原系统的平衡点，所以周期解是平凡解 $x = 0$ 。在这种情况下，定理10.4确定了对于足够小的 $\varepsilon$ ，原点是原系统(10.31)的一个指数稳定平衡点。换言之，在悬点（小幅高频）振动情况下，保持了摆在下平衡位置的指数稳定性。在平衡点 $(x_{1} = \pi ,x_{2} = 0)$ ，雅可比矩阵

$$
\left[ \begin{array}{c c} 0 & 1 \\ \alpha^ {2} - 0. 5 & - \alpha \beta \end{array} \right]
$$

对于 $0 < \alpha < 1 / \sqrt{2}$ 和 $\beta > 0$ 是赫尔维茨的。还要注意， $(x_{1} = \pi, x_{2} = 0)$ 是原系统的一个平衡点，运用定理10.4可以得到结论：如果 $\alpha < 1 / \sqrt{2}$ ，则对于足够小的 $\varepsilon$ ，上平衡位置 $\theta = \pi$ 是原系统(10.31)的指数稳定平衡点。这是一个很有趣的发现，因为它表明摆在上方的非稳定平衡位置可以通过悬点在竖直方向的小幅高频振动达到稳定①。
