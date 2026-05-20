# 7.2.1 问题的提出

不确定性机械系统可描述为

$$\frac {\mathrm{d} x _ {1}}{\mathrm{d} t} = x _ {2} \tag {7.5}J \frac {\mathrm{d} x _ {2}}{\mathrm{d} t} + C x _ {2} = u - d$$

式中， $x=\left[x_{1}\quad x_{2}\right]^{T}$ 为位置和速度；J 为系统转动惯量；C 为黏性系数；d 为加在控制输入上的扰动。

假设 $x_{\mathrm{d}}$ 为位置指令， $e = x_{1} - x_{\mathrm{d}}$ 为位置跟踪误差，则 $\dot{e} = \dot{x}_{\mathrm{d}} - \dot{x}_{1}$ ， $\ddot{e} = \ddot{x}_{\mathrm{d}} - \ddot{x}_{1}$ 。

![](image/927a33fff10450e336a4c05dcc869a17912384a48e3d93f177f840350e185ce8.jpg)
