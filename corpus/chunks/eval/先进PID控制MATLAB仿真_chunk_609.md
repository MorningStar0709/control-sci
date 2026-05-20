# 16.1.2 $H_{\infty}$ 控制器要求

针对系统

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} _ {1} w + \boldsymbol {B} _ {2} \boldsymbol {u}\mathbf {z} = \boldsymbol {C} _ {1} \boldsymbol {x} + \boldsymbol {D} _ {1 1} w + \boldsymbol {D} _ {1 2} \boldsymbol {u} \tag {16.4}y = x$$

式中，w 为控制扰动；z 为控制系统性能评价信号； $D_{11}=0$ 。

本控制系统的设计要求：

（1）x=0 是闭环系统的局部渐进稳定平衡点，即对于任意初始状态 $x(0)\subset R^{4}$ ， $x(t)\rightarrow0$ ；

（2）对于任意扰动 $w \in L_{2}[0, +\infty)$ ，闭环系统具有扰动抑制性能，即

$$\int_ {0} ^ {\infty} \left(q _ {1} x ^ {2} (t) + q _ {2} \theta^ {2} (t) + q _ {3} \dot {x} ^ {2} (t) + q _ {4} \dot {\theta} ^ {2} (t) + \rho u ^ {2} (t)\right) d t < \int_ {0} ^ {\infty} w ^ {2} (t) d t \tag {16.5}$$

式中， $q_{i}\geqslant 0(i = 1,2,3,4)$ 和 $\rho >0$ 为加权系数，令

$$
C _ {1} = \left[ \begin{array}{c c c c} \sqrt {q _ {1}} & 0 & 0 & 0 \\ 0 & \sqrt {q _ {2}} & 0 & 0 \\ 0 & 0 & \sqrt {q _ {3}} & 0 \\ 0 & 0 & 0 & \sqrt {q _ {4}} \\ 0 & 0 & 0 & 0 \end{array} \right], D _ {1 2} = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 0 \\ \sqrt {\rho} \end{array} \right] \tag {16.6}
$$

则式（16.5）等价于

$$\left\| z \right\| _ {2} < \left\| w \right\| _ {2} \tag {16.7}$$

定义 $T_{\mathrm{sw}}(s)$ 为w至z的闭环传递函数，表达式为

$$\left\| T _ {\mathrm{sw}} (s) \right\| _ {\infty} = \sup _ {w \neq 0} \frac {\left\| z \right\| _ {2}}{\left\| w \right\| _ {2}} \tag {16.8}$$

则闭环系统的扰动抑制性能等价于 $\left\|T_{\mathrm{sw}}(s)\right\|_{\infty}<1$ 。

![](image/ec88fcda6e620a819dc65c3fc53f3978e75c863b3b477dfed4f446ae8ac7975c.jpg)
