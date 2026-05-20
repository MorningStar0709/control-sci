# 13.1.2 控制器设计

式（13.1）可写为

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = \frac {1}{m} \left(- b x _ {2} - k x _ {1} + F u\right) \tag {13.4} \\ \end{array}
$$

式中， $x_{1}$ 为位置； $x_{2}$ 为速度信号。

取位置指令为 $x_{\mathrm{d}}$ ，误差为 $e = x_{1} - x_{\mathrm{d}}$ ，控制律设计为

$$u = k _ {\mathrm{p}} e + k _ {\mathrm{d}} \dot {e} \tag {13.5}$$

式中， $k_{p}>0;\quad k_{d}>0$ 。

![](image/b59370013ced5a7e166821638f9291c8b99232106ef006de0c3f34014ec7dfcf.jpg)
