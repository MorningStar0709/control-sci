# 12.5 增益分配

线性化设计的主要局限是控制器只能在单工作点(平衡点)的某个邻域内工作。本节介绍的增益分配可以将线性化方法的有效性扩展到若干个工作点。在很多情况下,系统随其工作点变化的动态特性是已知的,甚至可能在系统建模时,用一个或多个变量作为参数描述工作点,这些变量称为分配变量。这样,就可以在几个平衡点对系统线性化,针对每个平衡点设计线性反馈控制器,并把得到的一组线性控制器作为一个控制器执行,通过监测分配变量改变其参数,这样的控制器称为增益分配控制器。

增益分配的概念最早出现在飞行控制系统中①。把飞机或导弹的非线性运动方程在若干选定的工作点线性化,这些工作点捕获了整个飞行曲线上的一些关键状态,所设计的各线性控制器对于在选定工作点上线性化的系统都能达到理想的稳定性和性能要求。然后,把各控制器的参数作为增益分配变量的函数插值,典型的变量有动态压力、马赫数、高度及攻击角。最终在非线性系统上实现增益分配控制器。下面通过一个简单的例子说明增益分配的概念。

例 12.5 考虑习题 1.19 中的水槽系统, 其中水槽的横截面 A 随水槽的高度而变化, 系统模型可由

$$\frac {d}{d t} \left(\int_ {0} ^ {h} A (y) d y\right) = w _ {i} - k \sqrt {\rho g h}$$

表示,其中 h 是水槽内液体的高度, $w_{i}$ 是注入的流速, $\rho$ 是液体密度,g 是重力加速度,k 是正常数。取 x=h 作为状态变量, $u=w_{i}$ 作为控制输入,则状态模型为

$$\dot {x} = \frac {1}{A (x)} (u - c \sqrt {x}) \stackrel {\mathrm{def}} {=} f (x, u)$$

其中 $c = k\sqrt{\rho g}$ 为不定参数，假设希望设计的控制器以 $x$ 跟踪参考信号 $r$ 。定义 $y = x$ 为受控输出， $r$ 为分配变量，则当 $r = \alpha$ （正常数）时，输出 $y$ 应该调节到 $\alpha$ 。为了解决 $c$ 的不确定性，我们采用积分控制，平衡方程(12.16)～(12.17)为

$$0 = u _ {\mathrm{ss}} - c \sqrt {x _ {\mathrm{ss}}}, \quad \alpha = x _ {\mathrm{ss}}$$

即 $x_{\mathrm{ss}} = \alpha ,u_{\mathrm{ss}} = c\sqrt{\alpha}$ ，将积分器 $\dot{\sigma} = e = y - r$ 与状态方程一起讨论，可得

$$\dot {x} = f (x, u)\dot {\sigma} = x - r$$

采用PI控制器 $u = -k_{1}(\alpha)e - k_{2}(\alpha)\sigma$

在点 $(x_{\mathrm{ss}},\sigma_{\mathrm{ss}})$ 稳定所讨论的状态方程，其中 $\sigma_{\mathrm{ss}} = -u_{\mathrm{ss}} / k_2(\alpha)(k_2\neq 0)$ ，得到的闭环系统为

$$\dot {x} = f (x, - k _ {1} (\alpha) (x - r) - k _ {2} (\alpha) \sigma)\dot {\sigma} = x - r$$

当 $r = \alpha$ 时，系统有一个平衡点 $(x_{\mathrm{ss}},\sigma_{\mathrm{ss}})$ 。对闭环系统在 $(x,\sigma) = (x_{\mathrm{ss}},\sigma_{\mathrm{ss}})$ 线性化，当 $r = \alpha$ 时可得

$$
\dot {\xi} _ {\delta} = \left[ \begin{array}{c c} a (\alpha) - b (\alpha) k _ {1} (\alpha) & - b (\alpha) k _ {2} (\alpha) \\ 1 & 0 \end{array} \right] \xi_ {\delta} + \left[ \begin{array}{c} b (\alpha) k _ {1} (\alpha) \\ - 1 \end{array} \right] r _ {\delta}, \quad y _ {\delta} = x _ {\delta}
$$

其中 $\xi_{\delta} = \left[x_{\delta}\quad \sigma_{\delta}\right]^{\mathrm{T}},x_{\delta} = x - \alpha ,\sigma_{\delta} = \sigma -\sigma_{\mathrm{ss}},r_{\delta} = r - \alpha ,$
