# 知识点：离散化仿真方法

为了实现 PDE 模型的仿真，目前的方法是将 PDE 动力学模型离散化。离散化过程中，时间差分与 x 轴差分二者之间应满足一定关系。取采样时间为 $\Delta t = T$ ，x 轴间距为 $\Delta x = dx$ ，文献 $^{[12]}$ 针对 ODE 模型离散化给出了一个经验关系式，即时间差分与 x 轴差分之间的关系应满足 $\Delta t \leqslant \frac{1}{2} \Delta x^{2}$ ，仿真分析表明，在满足该关系式同时，应尽量降低 $\Delta t$ 和 $\Delta x$ 的值，并保证二者之间在一定的比值范围内。

采用差分方法对模型式（13.38）～式（13.40）进行离散化，从而求 $\theta(j)$ 和 $y(i,j)$ ，具体介绍如下：

(1) 关节转动角度 $\theta(t)$ 的离散化

由边界点力平衡动力学方程式（13.39）可知 $I_{\mathrm{h}}\ddot{\theta}(t) = \tau +\mathrm{EI}y_{xx}(0,t)$ ，采用向前差分，即 $\ddot{\theta} (t) = \frac{\dot{\theta} (j) - \dot{\theta} (j - 1)}{T}$ ，则

$$\ddot {\theta} (t) = \frac {\frac {\theta (j) - \theta (j - 1)}{T} - \frac {\theta (j - 1) - \theta (j - 2)}{T}}{T} = \frac {\theta (j) - 2 \theta (j - 1) + \theta (j - 2)}{T ^ {2}}.$$

将动力学模型展开，得

$$I _ {\mathrm{h}} \frac {\theta (j) - 2 \theta (j - 1) + \theta (j - 2)}{T ^ {2}} = \tau + \mathrm{EI} y _ {x x} (0, t)$$

则可求出

$$\theta (j) = 2 \theta (j - 1) - \theta (j - 2) + \frac {T ^ {2}}{I _ {\mathrm{h}}} (\tau + \mathrm{EI} y _ {x x} (0, t)) \tag {13.49}$$

其中采用向前差分方法，取当前时间为 $j - 1$ ，则 $y_{xx}(0,t)$ 相当于 $y_{xx}(1,j - 1)$ ，则有 $y_{x}(2,j - 1) = \frac{y(3,j - 1) - y(2,j - 1)}{\mathrm{d}x},\quad y_{x}(1,j - 1) = \frac{y(2,j - 1) - y(1,j - 1)}{\mathrm{d}x}$ ，则

$$y _ {x x} (0, t) = \frac {y _ {x} (2 , j - 1) - y _ {x} (1 , j - 1)}{\mathrm{d} x} = \frac {y (3 , j - 1) - 2 y (2 , j - 1) + y (1 , j - 1)}{\mathrm{d} x ^ {2}} 。$$

仿真时，考虑当前时刻的 $\theta(j)$ 未知，取 $\theta(t)$ 为 $\theta(j-1)$ 。
