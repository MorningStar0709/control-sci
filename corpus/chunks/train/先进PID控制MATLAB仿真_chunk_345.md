# 7.1.1 问题的提出

不确定性机械系统可描述为

$$\frac {\mathrm{d} x _ {1}}{\mathrm{d} t} = x _ {2} \tag {7.1}J \frac {\mathrm{d} x _ {2}}{\mathrm{d} t} + C x _ {2} = u$$

式中， $x=\left[x_{1}\quad x_{2}\right]^{T}$ 为位置和速度；J 为系统转动惯量，J>0；C 为黏性系数，C>0。

假设 $x_{\mathrm{d}}$ 为位置指令且为常值， $e = x_{1} - x_{\mathrm{d}}$ 为位置跟踪误差， $\dot{e} = \dot{x}_1 - \dot{x}_{\mathrm{d}} = x_2$ ， $\ddot{e} = \ddot{x}_1 - \ddot{x}_{\mathrm{d}} = \dot{x}_2$ ，则

$$J \ddot {e} + C \dot {e} = u$$

![](image/bcc5cd64954bdd5615b9698ee0c8780f4b9f47e4df5955e0e14afd9aa007fe46.jpg)
