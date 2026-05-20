# 13.2.3 控制律设计

针对慢系统 $\dot{x}=3x^{2}+2+3u_{s}$ ，设计基于 P 控制加补偿的控制律为

$$u _ {\mathrm{s}} = - \frac {1}{3} \left(3 x ^ {2} + 2 + k _ {\mathrm{ps}} x\right), \quad k _ {\mathrm{ps}} > 0 \tag {13.18}$$

则 $\dot{x} = -k_{p}x$ ，从而 $t \to \infty$ 时， $x \to 0$ 。

针对快系统 $\frac{dz_{f}}{d\tau}=-z_{f}+u_{f}$ ，设计P控制律为

$$u _ {\mathrm{f}} = - k _ {\mathrm{pf}} z _ {\mathrm{f}}, k _ {\mathrm{pf}} > 0 \tag {13.19}$$

则 $\frac{\mathrm{d}z_{\mathrm{f}}}{\mathrm{d}\tau} = -\left(k_{\mathrm{pf}} + 1\right)z_{\mathrm{f}}$ ，可知快系统的闭环系统是指数稳定的。

由式（13.18）和式（13.19），可得复合控制律为

$$u = u _ {\mathrm{s}} + u _ {\mathrm{f}} \tag {13.20}$$

![](image/bdbb03ea4f6b50e01d3718427501caac1adffdd72a4d7bcc9e10acbfa14fb26c.jpg)
