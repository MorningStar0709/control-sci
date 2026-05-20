# 例 9.3 回顾水箱的线性化

利用本节给出的概念重复例 2.19 的线性化过程。

解答。式 $(2.94)$ 可以写为

$$\dot {x} = f (x, u) \tag {9.8}$$

其中： $x\stackrel {\mathrm{def}}{=}h$ ； $u\stackrel {\mathrm{def}}{=}\omega_{\mathrm{in}}$ ，且

$$f (x, u) = - \frac {1}{R A \rho} \sqrt {p _ {1} - p _ {\mathrm{a}}} + \frac {1}{A \rho} w _ {\mathrm{in}} = - \frac {1}{R A \rho} \sqrt {\rho g h - p _ {\mathrm{a}}} + \frac {1}{A \rho} w _ {\mathrm{in}}$$

线性化方程为

$$\delta \dot {x} = A \delta x + B \delta u \tag {9.9}$$

其中：

$$[ A ] _ {x _ {0}, u _ {0}} = \frac {\partial f}{\partial x} = \left[ \frac {\partial f}{\partial h} \right] _ {h _ {0}, u _ {0}} = \frac {\partial}{\partial h} \left[ - \frac {1}{R A \rho} \sqrt {\rho g h - p _ {\mathrm{n}}} \right] _ {h _ {0}, u _ {0}} \tag {9.10}= - \frac {g}{2 A R} \frac {1}{\sqrt {\rho g h _ {0} - p _ {\mathrm{a}}}} = - \frac {g}{2 A R} \frac {1}{\sqrt {p _ {0} - p _ {\mathrm{a}}}} \tag {9.11}[ B ] _ {x _ {0}, u _ {0}} = \frac {\partial f}{\partial u} = \frac {\partial f}{\partial w _ {\mathrm{in}}} = \frac {1}{A \rho} \tag {9.12}$$

然而，注意到需要靠某种流量来将系统保持在某个平衡点，这样式(9.9)才会有效；具体地说，从式(2.94)可以看出，对于 $\dot{h}=0$ ，

$$u _ {0} = w _ {\bar {m} _ {0}} = \frac {1}{R} \sqrt {p _ {0} - p _ {\mathrm{a}}} \tag {9.13}$$

且式(9.9)中的 $\delta u$ 是 $\delta w_{\mathrm{in}}$ ，其中 $w_{\mathrm{in}} = w_{i n_0} + \delta w_{\mathrm{in}}$ 。因此，式(9.9)变为

$$\delta \dot {h} = A \delta h + B \delta w _ {\mathrm{in}} = A \dot {\delta} h + B w _ {\mathrm{in}} - B \frac {1}{R} \sqrt {p _ {0} - p _ {\mathrm{a}}} \tag {9.14}$$

与式 $(2.97)$ 精确匹配。
