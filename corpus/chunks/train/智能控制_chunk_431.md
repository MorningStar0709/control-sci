# 9.7.1 问题描述

考虑一种简单的动力学系统

$$\ddot {\theta} = f (\theta , \dot {\theta}) + u \tag {9.30}$$

式中， $\theta$ 为转动角度，u 为控制输入。

写成状态方程形式为

$$\dot {x} _ {1} = x _ {2} \tag {9.31}\dot {x} _ {2} = f (x) + u$$

式中， $f(x)$ 为未知。

位置指令为 $x_{d}$ ，则误差及其导数为

$$e = x _ {1} - x _ {\mathrm{d}}, \dot {e} = x _ {2} - \dot {x} _ {\mathrm{d}}$$

定义误差函数为

$$s = \lambda e + \dot {e}, \lambda > 0 \tag {9.32}$$

则

$$\dot {s} = \lambda \dot {e} + \ddot {e} = \lambda \dot {e} + \dot {x} _ {2} - \ddot {x} _ {\mathrm{d}} = \lambda \dot {e} + f (x) + u - \ddot {x} _ {\mathrm{d}} 。$$

由式(9.32)可见,如果 $s \rightarrow 0$ , 则 $e \rightarrow 0$ 且 $e \rightarrow 0$ 。
