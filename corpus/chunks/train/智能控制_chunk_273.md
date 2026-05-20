# 5.2.1 问题描述

简单的机械系统动力学方程为

$$\ddot {\theta} = f (\theta , \dot {\theta}) + u \tag {5.7}$$

式中， $\theta$ 为角度，u 为控制输入。

取 $f(\pmb {x}) = f(x_{1},x_{2}) = f(\theta ,\dot{\theta})$ ，写成状态方程形式为

$$\dot {x} _ {1} = x _ {2} \tag {5.8}\dot {x} _ {2} = f (\boldsymbol {x}) + u$$

式中， $f(x)$ 为未知函数。

位置指令为 $x_{\mathrm{d}}$ ，则误差及其变化率为

$$e = x _ {1} - x _ {\mathrm{d}}, \dot {e} = x _ {2} - \dot {x} _ {\mathrm{d}}$$

定义误差函数为

$$s = c e + \dot {e}, c > 0 \tag {5.9}$$

则

$$\dot {s} = c \dot {e} + \ddot {e} = c \dot {e} + \dot {x} _ {2} - \ddot {x} _ {\mathrm{d}} = c \dot {e} + f (x) + u - \ddot {x} _ {\mathrm{d}} 。$$

由式(5.9)可见,如果 $s \rightarrow 0$ , 则 $e \rightarrow 0$ 且 $\dot{e} \rightarrow 0$ 。
