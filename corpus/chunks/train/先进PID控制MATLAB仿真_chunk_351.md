# 7.2.2 PD 控制律的设计

定义误差函数为

$$s = \dot {e} + c e \tag {7.6}$$

式中，c>0。

定义 $\dot{x}_{\mathrm{r}} = s + x_{2}$ ，则

$$\dot {x} _ {\mathrm{r}} = \dot {x} _ {\mathrm{d}} + c e\ddot {x} _ {\mathrm{r}} = \ddot {x} _ {\mathrm{d}} + c \dot {e}$$

则由式（7.5）得

$$u = J \frac {\mathrm{d} x _ {2}}{\mathrm{d} t} + C x _ {2} + d$$

控制律设计为

$$u = u _ {\mathrm{m}} + k _ {\mathrm{p}} \mathrm{s} + k _ {\mathrm{i}} \int_ {0} ^ {t} s \mathrm{d} t + u _ {\mathrm{r}} \tag {7.7}$$

式中， $k_{p}>0$ ； $k_{i}>0$ ； $u_{m}$ 为基于模型的控制项； $u_{r}$ 为鲁棒项。

取

$$u _ {\mathrm{m}} = J \ddot {x} _ {\mathrm{r}} + C \dot {x} _ {\mathrm{r}}u _ {\mathrm{r}} = k _ {\mathrm{r}} \operatorname{sgn} (s)$$

式中， $k_{r} \geqslant \left|d_{\max}\right|$ ，则

$$J \dot {x} _ {2} + C x _ {2} = J \ddot {x} _ {\mathrm{r}} + C \dot {x} _ {\mathrm{r}} + k _ {\mathrm{p}} s + k _ {\mathrm{i}} \int_ {0} ^ {t} s \mathrm{d} t + k _ {\mathrm{r}} \operatorname{sgn} (s) - d$$

从而

$$J \dot {s} + k _ {\mathrm{i}} \int_ {0} ^ {t} s \mathrm{d} t = - C s - k _ {\mathrm{p}} \mathrm{s} - k _ {\mathrm{r}} \mathrm{sgn} (s) + d \tag {7.8}$$

![](image/bd158d8e19fb7f066339e704e30e9163b155466a2067a765ac455aa51c9f8f4f.jpg)
