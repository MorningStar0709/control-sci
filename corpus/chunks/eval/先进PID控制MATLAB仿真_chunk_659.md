# 17.6.2 控制律设计

设位置指令为 $\theta_{d}$ ，令 $e=\theta_{d}-\theta$ ，设计滑模切换函数为

$$s = \dot {e} + c e \tag {17.28}$$

式中， $c > 0$ ，则

$$\dot {s} = \ddot {e} + c \dot {e} = \ddot {\theta} _ {\mathrm{d}} - \ddot {\theta} + c \dot {e} = \ddot {\theta} _ {\mathrm{d}} - f - g u - d + c \dot {e}$$

将控制律设计为

$$u = \frac {1}{g} \Big [ - f + \ddot {\theta} _ {\mathrm{d}} + c \dot {e} + \eta \mathrm{sgn} (s) \Big ] \tag {17.29}$$

定义 Lyapunov 函数:

$$L = \frac {1}{2} s ^ {2}$$

对 $L$ 求导，并将式（17.29）代入，得

$$
\begin{array}{l} \dot {L} = s \dot {s} = s \left(\ddot {\theta} _ {\mathrm{d}} - f - g u - d + c \dot {e}\right) \\ = s \left(\ddot {\theta} _ {\mathrm{d}} - f - \left(- f + \ddot {\theta} _ {\mathrm{d}} + c \dot {e} + \eta \operatorname{sgn} (s)\right) - d + c \dot {e}\right) \\ = s (- d - \eta \operatorname{sgn} (s)) \\ = - s d - \eta | s | \\ \end{array}
$$

只要满足 $\eta \geqslant D$ ，则有 $\dot{L} = -sd - \eta |s|\leqslant 0$ ，即 $s\cdot \dot{s}\leqslant 0$ 。

当 $\ddot{L} \equiv 0$ 时， $s \equiv 0$ ，根据 LaSalle 不变性原理 $^{[2]}$ ，闭环系统渐进稳定，当 $t \to \infty$ 时， $s \to 0$ 。

为了消除滑模控制中的抖振，采用饱和函数 $\mathrm{sat}(s)$ 代替控制律式（17.29）中的符号函数 $\mathrm{sgn}(s)$ ，表达如下：

$$
\operatorname{sat} (s) = \left\{ \begin{array}{l l} 1 & s > \Delta \\ k s & | s | \leqslant \Delta , k = 1 / \Delta \\ - 1 & s <   - \Delta \end{array} \right. \tag {17.30}
$$

式中， $\Delta$ 为 “边界层”。

饱和函数消除抖振的本质：在边界层外，采用切换控制，在边界层内，采用线性反馈控制。由于滑模控制中，切换函数s的值大部分时间都在边界层之内，此时控制律式（17.29）中采用的是反馈控制而不是切换控制，因此抖振得到了很好的抑制。

![](image/40b5e6756eccc512e896a042d55727ac5e1bf0b6e970dee9504e9b821f9df1bb.jpg)
